# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

def check(value, limit):
    status = "OVER LIMIT" if value > limit else "OK"
    return status # add return status inside the function
status=check(87, 100) # add status =. (status was not defined before it is a local variable before)

print(status)
