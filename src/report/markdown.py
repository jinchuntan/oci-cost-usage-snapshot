from datetime import datetime
from pathlib import Path


def write_markdown(records, path: Path):
    lines = []
    lines.append("# OCI Cost & Usage Snapshot")
    lines.append("")
    lines.append(f"Generated: {datetime.utcnow().isoformat()}Z")
    lines.append("")
    lines.append("| Type | Name | State | Details |")
    lines.append("|---|---|---|---|")

    for r in records:
        details = []
        for k, v in r.items():
            if k not in ["resource_type", "name", "state"]:
                details.append(f"{k}={v}")
        lines.append(
            f"| {r['resource_type']} | {r['name']} | {r['state']} | {'; '.join(details)} |"
        )

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")
