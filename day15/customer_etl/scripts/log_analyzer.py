from pathlib import Path

# Resolve file paths relative to this script
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_DIR = SCRIPT_DIR.parent

log_file = PROJECT_DIR / "logs" / "etl.log"

# Initialize counters
info_count = 0
warning_count = 0
error_count = 0

# Store error messages
error_messages = []

# Read and analyze the log file
with open(log_file, "r") as file:
    for line in file:

        if " INFO " in line:
            info_count += 1

        elif " WARNING " in line:
            warning_count += 1

        elif " ERROR " in line:
            error_count += 1
            error_messages.append(line.strip())

# Display analysis report
print("ETL LOG ANALYSIS")
print("----------------")
print("INFO messages:", info_count)
print("WARNING messages:", warning_count)
print("ERROR messages:", error_count)

# Display error details
print("\nERROR DETAILS")

if error_messages:
    for message in error_messages:
        print(message)
else:
    print("No errors found.")
# Save analysis report
report_path = PROJECT_DIR / "logs" / "log_analysis_report.txt"

report_lines = [
    "ETL LOG ANALYSIS",
    "----------------",
    f"INFO messages: {info_count}",
    f"WARNING messages: {warning_count}",
    f"ERROR messages: {error_count}",
    "",
    "ERROR DETAILS",
]

if error_messages:
    report_lines.extend(error_messages)
else:
    report_lines.append("No errors found.")

report_path.write_text("\n".join(report_lines) + "\n")

print("\nReport saved to:", report_path)
