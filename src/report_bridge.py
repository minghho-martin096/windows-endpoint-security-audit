import json
import sys

from reports.report_generator import generate_report


def main():
    try:
        # Read the audit results sent by the WPF application.
        input_data = sys.stdin.read()

        if not input_data.strip():
            raise ValueError("No audit results were provided.")

        results = json.loads(input_data)

        # Generate the report using the existing Python report generator.
        _, output_path = generate_report(results)

        # Return only the report path to the GUI.
        print(str(output_path))

    except Exception as error:
        print(str(error), file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()