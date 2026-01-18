import socket
import requests
from rich import print

def check_tcp(host: str, port: int, timeout: int = 3) -> bool:
    """Check if a TCP port is open by attempting a connection."""
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except OSError:
        return False

def check_http(url: str, timeout: int = 3) -> bool:
    """Check if an HTTP endpoint responds successfully."""
    try:
        r = requests.get(url, timeout=timeout)
        return r.status_code < 500
    except requests.RequestException:
        return False

checks = [
    ("Nginx HTTP", lambda: check_http("http://localhost:8080")),
    ("Node Exporter Metrics", lambda: check_http("http://localhost:9100/metrics")),
    ("Postgres TCP 5432", lambda: check_tcp("localhost", 5432)),
    ("Redis TCP 6379", lambda: check_tcp("localhost", 6379)),
]

print("[bold]Infra Validation Results[/bold]\n")

failed = 0
for name, fn in checks:
    ok = fn()
    if ok:
        print(f"[green]✅ {name}[/green]")
    else:
        failed += 1
        print(f"[red]❌ {name}[/red]")

print()
if failed == 0:
    print("[bold green]All checks passed.[/bold green]")
else:
    print(f"[bold red]{failed} check(s) failed.[/bold red]")
