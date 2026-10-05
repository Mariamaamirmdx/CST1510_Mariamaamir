# BROKEN ON PURPOSE.
# Run it, type 23.7 when asked, read the last line, then fix it.
# Guess: The last line says ValueError, so the type is right but the value is impossible.
# int() can't turn "23.7" into a whole number because it has a decimal point.
# Fix: use float() instead of int(), since float() accepts decimals.

value = float(input("Value: "))

print(value)
