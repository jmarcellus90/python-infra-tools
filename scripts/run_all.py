import subprocess
from datetime import datetime
from pathlib import Path

REPORTS_DIR = Path("reports")
REPORTS_DIR.mkdir(exist_ok=True)

timestamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
summary_file = REPORTS_DIR / f"summary_{timestamp}.txt"

commands = [
    ("Infra Validation", ["python", "scripts/infra_validate.py"]),
    ("Docker Status Report", ["python", "scripts/docker_report.py"]),
]

lines = []
lines.append(f"Run Summary: {datetime.now().isoformat()}")
lines.append("-" * 60)

for title, cmd in commands:
    lines.append(f"\n[{title}]")
    lines.append(f"Command: {' '.join(cmd)}")
    lines.append("-" * 60)

    result = subprocess.run(cmd, capture_output=True, text=True)
    lines.append(result.stdout.strip())

    if result.returncode != 0:
        lines.append("\nERROR OUTPUT:")
        lines.append(result.stderr.strip())

summary_file.write_text("\n".join(lines) + "\n")
print(f"✅ Summary saved to: {summary_file}")
