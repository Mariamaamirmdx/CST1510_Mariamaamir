# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.
# Guess: The last line says TypeError, so I mixed text and a number.
# input() gives back text, so value is a string.
# I tried to add 1 (a number) to a string, and Python can't do that.
# Fix: convert value to a number with int() before adding.

value = input("Value: ")

print(int(value) + 1)
