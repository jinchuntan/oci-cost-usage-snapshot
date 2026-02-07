import oci


def collect_block_volumes(config, signer, compartment_id):
    client = oci.core.BlockstorageClient(config, signer=signer)
    volumes = client.list_volumes(compartment_id=compartment_id).data


    data = []
    for v in volumes:
        data.append({
            "resource_type": "block_volume",
            "name": v.display_name,
            "size_gb": v.size_in_gbs,
            "state": v.lifecycle_state,
            "ocid": v.id,
            "availability_domain": v.availability_domain,
        })

    return data
