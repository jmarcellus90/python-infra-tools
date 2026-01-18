### infra_validate.py
Validates that core home lab services are reachable locally:

- Nginx (8080)
- Node Exporter (9100)
- PostgreSQL (5432)
- Redis (6379)

Run:
```bash
python scripts/infra_validate.py

## Makefile Commands

Run common tasks quickly:

```bash
make validate
make report
make all
