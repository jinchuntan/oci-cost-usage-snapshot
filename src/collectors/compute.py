import oci


def collect_compute_instances(config, signer, compartment_id):
    client = oci.core.ComputeClient(config, signer=signer)
    instances = client.list_instances(compartment_id=compartment_id).data

    data = []
    for i in instances:
        data.append({
            "resource_type": "compute_instance",
            "name": i.display_name,
            "state": i.lifecycle_state,
            "shape": i.shape,
            "ocid": i.id,
            "availability_domain": i.availability_domain,
        })

    return data
