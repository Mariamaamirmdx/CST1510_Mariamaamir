"""
RECORD CHECK  -  my version
==============================

Name  : Mariam aamir 
Lane  : ai and data science
Date  : 5 Oct 2026

Run it:  python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""


# ============================================================================ INPUT
# 1. Ask the user for your three values.
#
#    - the first is TEXT      (a name, a hostname, an IP)  -> no conversion needed
#    - the second is a NUMBER (use float(), not int())
#    - the third  is a NUMBER (use float(), not int())
#
#    Remember: input() always gives back text.

label = input("Hostname: ")                # input() call, no conversion (text)
first = float(input("GB used: "))          # input() call, converted with float()
second = float(input("GB total: "))        # input() call, converted with float()


# ============================================================================ PROCESS
# 2. Work out what you were NOT given.       [Typical and above]
#
#    - difference : how far the first is from the second
#    - percent    : the first as a percentage of the second
#
#    Do not type the answers. Calculate them.

difference = second - first                # calculated: GB still free
percent = first / second * 100             # calculated: used as a % of total


# ============================================================================ OUTPUT
# 3. Print the report.
#
#    Threshold : print the three values you were given, inside a border
#    Typical   : add difference and percent, 2 decimal places, right-aligned
#    Excellent : difference always shows its sign, plus one line of your own
#
#    Useful:  f"{value:>10.2f}"    right-aligned, 2 decimal places
#             f"{value:>+10.2f}"   the same, but always shows the sign

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

print(f"{'Used':<10}: {first:>10.2f}")
print(f"{'Total':<10}: {second:>10.2f}")
print(f"{'Free':<10}: {difference:>+10.2f}")
print(f"{'Percent':<10}: {percent:>10.2f} %")

# My own extra line: percent still free.
# WHY: an IT admin cares about how much headroom is left before a
# server fills up, not only how much is already used.
print(f"{'Free %':<10}: {100 - percent:>10.2f} %")

print("=" * 34)


# ============================================================================
# 4. Before you finish:
#
#    [x] Run it three times with different numbers
#          srv-01, 87, 120    -> Free +33.00,  Percent 72.50 %
#          srv-02, 50, 200    -> Free +150.00, Percent 25.00 %
#          srv-03, 99.5, 100  -> Free +0.50,   Percent 99.50 %
#
#    [x] Run it with a total of 0 and write the error in your journal
#          Error: ZeroDivisionError: float division by zero
#          Line:  percent = first / second * 100
#          Why:   second (the total) is 0.0 and Python cannot divide by zero.
#          Not fixing it. That is Week 2 (if statements).
#
#    [x] Check every variable name says what it holds
#          label = hostname, first = GB used, second = GB total,
#          difference = GB free, percent = % used
#
#    [x] Show it to the person next to you
