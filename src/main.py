import os
from datetime import datetime
from pathlib import Path

import oci
from dotenv import load_dotenv

from collectors.compute import collect_compute_instances
from collectors.storage import collect_block_volumes
from report.serializer import write_json
from report.markdown import write_markdown


def require(name):
    v = os.getenv(name)
    if not v:
        raise RuntimeError(f"Missing env var: {name}")
    return v


def main():
    load_dotenv()

    compartment_id = require("OCI_COMPARTMENT_OCID")
    bucket_name = require("OCI_BUCKET_NAME")
    prefix = os.getenv("OCI_OBJECT_PREFIX", "cost-snapshots")

    config = oci.config.from_file()
    signer = oci.signer.Signer(
        tenancy=config["tenancy"],
        user=config["user"],
        fingerprint=config["fingerprint"],
        private_key_file_location=config["key_file"],
        pass_phrase=config.get("pass_phrase"),
    )

    os_client = oci.object_storage.ObjectStorageClient(config, signer=signer)
    namespace = os_client.get_namespace().data

    records = []
    records += collect_compute_instances(config, signer, compartment_id)
    records += collect_block_volumes(config, signer, compartment_id)

    ts = datetime.utcnow().strftime("%Y-%m-%d_%H%M%S_UTC")
    reports_dir = Path("reports")

    json_path = reports_dir / f"cost_snapshot_{ts}.json"
    md_path = reports_dir / f"cost_snapshot_{ts}.md"

    write_json(records, json_path)
    write_markdown(records, md_path)

    for p in [json_path, md_path]:
        with p.open("rb") as f:
            os_client.put_object(
                namespace,
                bucket_name,
                f"{prefix}/{p.name}",
                f,
            )

    print("Snapshot generated and uploaded successfully.")
    print(f"Uploaded: {prefix}/{json_path.name}")
    print(f"Uploaded: {prefix}/{md_path.name}")

if __name__ == "__main__":
    main()
