# OCI Cost & Usage Snapshot Analyzer

This project captures a point-in-time snapshot of OCI resource usage
focused on Compute instances and Block Volumes, and uploads structured
reports to OCI Object Storage.

## Features

- Read-only collection of OCI resources
- JSON + Markdown report generation
- Object Storage upload
- No billing API access required; Object Storage write permission is required

## Setup and Run

Run these commands from the repository root with Python 3.11 or newer.
Configure OCI API-key authentication in `~/.oci/config` first
(`%USERPROFILE%\.oci\config` on Windows).

### Windows PowerShell

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
Copy-Item .env.example .env
notepad .env
.\.venv\Scripts\python.exe src/main.py
```

### macOS / Linux

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
cp .env.example .env
# Edit .env with your compartment OCID and destination bucket before running.
.venv/bin/python src/main.py
```

Copy the template only on first setup; keep an existing `.env` when updating.
If your Windows installation uses `python` instead of `py -3.11`, substitute
that command when creating the environment. No environment activation is needed.

### Configuration and Permissions

| Setting | Meaning |
| --- | --- |
| `OCI_COMPARTMENT_OCID` | Required: the compartment to inspect. |
| `OCI_BUCKET_NAME` | Required: the destination bucket for reports. |
| `OCI_OBJECT_PREFIX` | Report object prefix; defaults to `cost-snapshots`. |

This tool uses the `DEFAULT` OCI SDK profile; it does not read `OCI_PROFILE`.

The configured identity must be allowed to read Compute instances and Block Volumes,
resolve the Object Storage namespace, and upload objects to the selected bucket.
The bucket must already exist; this script does not create it.
This is a resource snapshot, not an invoice or a billing-cost calculation.
Reports are saved under `reports/` before upload. Resource collection is read-only,
but uploading reports writes to Object Storage.

Local `.env` files, signing keys, environments and generated reports are ignored by Git.

## Output
<img width="940" height="61" alt="image" src="https://github.com/user-attachments/assets/5f194d4b-bffd-4bd9-89f2-b10eb2445933" />
<img width="940" height="286" alt="image" src="https://github.com/user-attachments/assets/3427da6e-f05f-48f5-b212-598a4770b597" />
<img width="940" height="111" alt="image" src="https://github.com/user-attachments/assets/e709f2c4-d5c4-4bc7-bf1b-d073c288ad62" />


