d={
    "Admin":set(),
    "User":set(),
    "Manager":set()
    }
print(d)
d["Admin"].add(1)
d["Admin"].add(2)
print(d)
if 1 in d["Admin"]:
    print("present")