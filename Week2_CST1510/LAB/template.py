RECORD CHECK  -  my version
===========================

<<<<<<< HEAD
Name  : Mariam aamir
Lane  :  AI / Cyber / IT      (delete two)
=======
Name  :
Name  : Mariam aamir
Lane  :  AI / Cyber / IT      (delete two)
Date  :
>>>>>>> a9fd976 (Add project files)
Date  : 30-09-2026

Run it:   python template.py

@@ -19,23 +19,28 @@
#    - the second is a NUMBER (use float(), not int())
#    - the third  is a NUMBER (use float(), not int())

<<<<<<< HEAD
=======
label = ""      # replace with an input() call
value = 0.0     # replace with an input() call, converted with float()
limit = 0.0     # replace with an input() call, converted with float()
>>>>>>> a9fd976 (Add project files)
label = input("enter your hostname: ")    # replace with an input() call
value = float(input("enter used: "))     # replace with an input() call, converted with float()
limit = float(input("enter limit: "))    # replace with an input() call, converted with float()


# ================================================================== PROCESS
# 2. Work out the difference and the percentage.       [Typical and above]

<<<<<<< HEAD
=======
difference = 0.0   # replace with your calculation
percent = 0.0       # replace with your calculation
>>>>>>> a9fd976 (Add project files)
difference = limit - value   # replace with your calculation
percent = (value/limit)*100      # replace with your calculation
# 3. Decide a status and store it in a variable called status.
#
#    Threshold : if / else        -> "OVER LIMIT" or "OK"
#    Typical   : if / elif / else -> "OVER LIMIT" (100% or more),
#                                     "WARNING" (90% or more), otherwise "OK"
<<<<<<< HEAD
=======

status = ""   # replace with your if / else (or if / elif / else)
>>>>>>> a9fd976 (Add project files)
if percent>=100:
    status = "OVER LIMIT"
elif percent>=90:
    status = "WARNING"
else:
    status = " OK "
   # replace with your if / else (or if / elif / else)


# =================================================================== OUTPUT
@@ -53,7 +58,7 @@
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

<<<<<<< HEAD
=======
# your report lines go here
>>>>>>> a9fd976 (Add project files)
print(f"USED:{value:>10.2f}\nTOTAL:{limit:>10.2f}\nFREE:{difference:>10.2f}\nPERCENT:{percent:>10.2f}%\nSTATUS:{status:>10}")

print("=" * 34)
