# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

class Record:
    def status(self,percent):    # this parameter should be self so added self to it as python passes object automatically,so method needs self to receive it
        return percent

r = Record()
print(r.status(95))
