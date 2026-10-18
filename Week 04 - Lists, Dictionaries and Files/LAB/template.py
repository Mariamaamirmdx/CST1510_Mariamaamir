"""
RECORD CHECK - my version
=========================

Name : Mariam aamir
Lane : IT
Date : 15-10-26

Run it:   python template.py
"""


# ======================================================================= FUNCTIONS
def check_record(value, limit):
    """Return difference, percent and status for one record."""
    difference = value - limit
    percent = value / limit * 100
    status = "OVER LIMIT" if value > limit else "OK"
    return difference, percent, status


def print_report(label, value, limit, difference, percent, status):
    """Print one formatted report line."""
    print(f"{label:<8} used={value:<6} total={limit:<6} "
          f"diff={difference:+.0f}  {percent:.1f}%  {status}")


def load_records(path):
    """Read label,value,limit lines from a file and return a list of dicts."""
    records = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line:
                label, value, limit = line.split(",")
                records.append({"label": label,
                                "value": float(value),
                                "limit": float(limit)})
    return records


def save_results(path, results):
    """Write one label,status line per record to a file."""
    with open(path, "w") as f:
        for label, status in results:
            f.write(f"{label},{status}\n")


# ============================================================================ STORE
try:
    # Missing file test , i changed record.txt to wrong.txt and ran it
    # The raw pythhon error is FileNotFoundError(no such file or directory )
    # With try/except,it prints a clear message and continue with no records
    records = load_records("records.txt") 
except FileNotFoundError:
    print("Error: records.txt was not found. Starting with no records.")
    records = []


# ================================================================ PROCESS + OUTPUT
over_count = 0
results = []

for record in records:
    difference, percent, status = check_record(record["value"], record["limit"])
    print_report(record["label"], record["value"], record["limit"],
                 difference, percent, status)
    results.append((record["label"], status))
    if status == "OVER LIMIT":
        over_count += 1

print(f"\nRecords over limit: {over_count}")
save_results("results.txt", results)