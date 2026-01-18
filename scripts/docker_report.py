import json
import subprocess
from datetime import datetime
from pathlib import Path

REPORTS_DIR = Path("reports")
REPORTS_DIR.mkdir(exist_ok=True)

timestamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
output_file = REPORTS_DIR / f"docker_status_{timestamp}.json"

result = subprocess.run(
    ["docker", "ps", "--format", "{{json .}}"],
    capture_output=True,
    text=True,
    check=True
)

containers = []
for line in result.stdout.splitlines():
    containers.append(json.loads(line))

report = {
    "generated_at": datetime.now().isoformat(),
    "container_count": len(containers),
    "containers": containers
}

output_file.write_text(json.dumps(report, indent=2))
print(f"✅ Report saved to: {output_file}")
print(f"📦 Containers found: {len(containers)}")
