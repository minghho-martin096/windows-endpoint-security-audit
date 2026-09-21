import json

from src.audit_service import run_audit


def main():
    results = run_audit()

    print(json.dumps(results))


if __name__ == "__main__":
    main()