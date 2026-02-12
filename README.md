# OCI Cost & Usage Snapshot Analyzer

This project captures a point-in-time snapshot of OCI resource usage
focused on Compute instances and Block Volumes, and uploads structured
reports to OCI Object Storage.

## Features

- Read-only collection of OCI resources
- JSON + Markdown report generation
- Object Storage upload
- No billing or risky permissions required

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
```

## Output
<img width="940" height="61" alt="image" src="https://github.com/user-attachments/assets/5f194d4b-bffd-4bd9-89f2-b10eb2445933" />
<img width="940" height="286" alt="image" src="https://github.com/user-attachments/assets/3427da6e-f05f-48f5-b212-598a4770b597" />
<img width="940" height="111" alt="image" src="https://github.com/user-attachments/assets/e709f2c4-d5c4-4bc7-bf1b-d073c288ad62" />


