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
