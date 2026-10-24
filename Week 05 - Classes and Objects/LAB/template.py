"""
RECORD CHECK  -  my version
===========================

Name  : Mariam aamir
Lane  :   IT      
Date  : 19-10-2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ====================================================================== CLASS
# 1. Define a class called Record.
#
#    Threshold : __init__(self, label, value, limit) storing all three as
#                attributes. No methods yet.
#    Typical   : add a method status(self) that returns "OVER LIMIT" (100%+),
#                "WARNING" (90%+) or "OK", worked out from self.value and
#                self.limit. Give it a one-line docstring.
#    Excellent : also add over_limit_count as a class-level running total -
#                see the note below.

# your class goes here

class Record:
    
    def __init__(self,label,value,limit):
        """Store the hostname, GB used, and GB total"""
        self.label = label
        self.value = value
        self.limit = limit
        


    def status(self):
            """Return OVER LIMIT, WARNING, or OK based on value vs limit."""
            percent = (self.value/self.limit)*100
            if percent >= 100:
                return "OVER LIMIT"
            elif percent >= 90:
                return "WARNING"
            else:
                return "OK"




# ==================================================================== RECORDS
# 2. Create your records.
#
#    Threshold : create at least 2 Record instances directly in the code.
#    Typical   : same, but now print each one's .status() as well.
#    Excellent : instead, write load_records(path) that reads label,value,limit
#                lines from a file and returns a list of Record objects. Make
#                your own data file, one record per line.

   # replace with your code
records =[
     Record("srv-001",23,100),
Record("srv-100",95,100),
Record("srv-200",120,100)]






# ==================================================================== OUTPUT
# 3. Print a report for each record.
#
#    Threshold : label, value, limit, inside a border.
#    Typical   : add the result of .status().
#    Excellent : also keep a running count of how many came back OVER LIMIT
#                across every record, and print that once, after the loop.
#                (Simplest: a plain variable outside the loop, same pattern
#                as Week 4. If you want it to live ON the object instead,
#                that is a stretch worth trying - but a variable is enough.)
over_limit_total= 0
for record in records:
    
    result=record.status()
    if result=="OVER LIMIT":
         over_limit_total+= 1
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)

    # your report lines go here
    print(f"Value:{record.value}")
    print(f"Limit:{record.limit}")
    print(f"Status:{result}")
    print("=" * 34)

print(f"\nTotal OVER LIMIT : {over_limit_total}")

# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers by hand
#    [ ] Check every method only reads/changes its OWN object (self) -
#        nothing reaches outside itself
#    [ ] Check every method and __init__ has a one-line docstring
