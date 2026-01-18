venv:
	python3 -m venv .venv

install:
	. .venv/bin/activate && pip install -r requirements.txt

validate:
	. .venv/bin/activate && python scripts/infra_validate.py

report:
	. .venv/bin/activate && python scripts/docker_report.py

all:
	. .venv/bin/activate && python scripts/run_all.py
