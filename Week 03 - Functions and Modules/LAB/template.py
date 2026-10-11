"""
RECORD CHECK - my version
==============================

Name :Mariam aamir
Lane : AI / Data Science
Date :7-10-2026

Run it:  python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""


# ====================================================================== FUNCTIONS
# 1. Write a function called status_of(percent) that returns "OVER LIMIT"
#    (100% or more), "WARNING" (90% or more), or "OK" (anything else).
#
#    Typical and above: also write check(value, limit) that returns the
#    difference and the percentage as two values - do not print anything
#    inside it, only calculate and return.
#
#    Excellent: also write print_report(label, value, limit, difference,
#    percent, status) that does ALL of the printing below - nothing outside
#    it should contain a print() of its own.
#
#    Give each function a one-line docstring saying what it does.

def status_of(percent):
    """Return OVER LIMIT, WARNING or OK based on the percentage."""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"


def check(value, limit):
    """Return the difference and the percentage of value against limit."""
    difference = limit - value
    percent = value / limit * 100 
    return difference, percent


def print_report(label, value, limit, difference, percent, status):
    """Print the bordered record check report."""
    border = "=" * 34
    print()
    print(border)
    print(f"  RECORD CHECK  -  {label}")
    print(border)
    print(f"  {'Loaded':<10}: {value:>12.2f}")
    print(f"  {'Expected':<10}: {limit:>12.2f}")
    print(f"  {'Missing':<10}: {difference:>12.2f}")
    print(f"  {'Percent':<10}: {percent:>12.2f} %")
    print(f"  {'Status':<10}: {status:>12}")
    print(border)


over_limit_count = 0

while True:

    # ================================================================== INPUT
    # 2. Ask for your three values.
    #
    #    - the first is TEXT      (a name, a hostname, an IP)  -> no conversion needed
    #    - the second is a NUMBER (use float(), not int())
    #    - the third  is a NUMBER (use float(), not int())

    label = input("Dataset name (or 'quit' to stop): ")
    if label.lower() == "quit":
        break
    value = float(input("Rows loaded: "))
    limit = float(input("Rows expected: "))

    # ================================================================== PROCESS
    # 3. Work out the difference, the percentage, and the status.
    #
    #    Threshold : call status_of() to get the status. Work out the
    #                difference and percentage inline, not in a function.
    #
    #    Typical   : call check() to get the difference and percentage instead.

    difference, percent = check(value, limit)
    status = status_of(percent)
    if status == "OVER LIMIT":
        over_limit_count += 1

    # ================================================================== OUTPUT
    # 4. Print the report.
    #
    #    Threshold : the three values you were given, plus status, inside a border
    #    Typical   : add difference and percent, 2 decimal places, right-aligned
    #    Excellent : call print_report() instead of printing directly here, and
    #                wrap sections 2-4 in a loop so you can check as many records
    #                as you like in one run - type "quit" as the label to stop.
    #                Keep count of how many came back OVER LIMIT and print that
    #                once, after the loop ends.

    print_report(label, value, limit, difference, percent, status)

print()
print(f"Records that came back OVER LIMIT: {over_limit_count}")


# ====================================================================== CHECKLIST
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every function does one job - if a function both calculates
#        and prints, split it

# Zero test: entered test, 100, 0
# Error: ZeroDivisionError: flosat division by zero
# Happens in check() on line 43 (percent = value / limit * 100)
# Cause: limit is 0 so the program divides by zero. Fix later with an if limit == 0 check.