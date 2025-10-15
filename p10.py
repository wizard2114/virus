#--- Facts ---
male = {"Ram", "Raju", "Mohan", "Anil", "Rahul"}
female = {"Sita", "Meena", "Rekha", "Sunita", "Neha"}
# parent(child, parent)
parent = {
("Ram", "Raju"),
("Sita", "Raju"),
("Ram", "Rekha"),
("Sita", "Rekha"),
("Raju", "Anil"),
("Meena", "Anil"),
("Raju", "Sunita"),
("Meena", "Sunita"),
("Rekha", "Neha"),
("Mohan", "Neha"),
("Rekha", "Rahul"),
("Mohan", "Rahul"),}

# --- Rules ---
def father(x, y):
    return x in male and (x, y) in parent
def mother(x, y):
    return x in female and (x, y) in parent
def grandfather(x, y):
    return x in male and any((x, z) in parent and (z, y) in parent for z in male | female)
def grandmother(x, y):
    return x in female and any((x, z) in parent and (z, y) in parent for z in male | female)
def brother(x, y):
    return x in male and any((p, x) in parent and (p, y) in parent for p in male | female) and x!= y
def sister(x, y):
    return x in female and any((p, x) in parent and (p, y) in parent for p in male | female) and x!= y

def uncle(x, y):
    return x in male and any(brother(x, p) and (p, y) in parent for p in male | female)
def aunt(x, y):
    return x in female and any(sister(x, p) and (p, y) in parent for p in male | female)
def nephew(x, y):
    return x in male and (uncle(y, x) or aunt(y, x))
def niece(x, y):
    return x in female and (uncle(y, x) or aunt(y, x))
def cousin(x, y):
    return any((p1, x) in parent and (p2, y) in parent and brother(p1, p2) or sister(p1, p2)
        for p1 in male|female for p2 in male | female) and x != y

print("Father of Anil:",[p for p in male if father(p, "Anil")])
print("Mother of Anil:",[p for p in female if mother(p, "Anil")])
print("Grandfather of Neha:",[p for p in male if grandfather(p, "Neha")])
print("Grandmother of Neha:",[p for p in female if grandmother(p, "Neha")])
print("Brother of Sunita:",[p for p in male if brother(p, "Sunita")])
print("Sister of Anil:",[p for p in female if sister(p, "Anil")])
print("Uncle of Neha:", [p for p in male if uncle(p, "Neha")])
print("Aunt of Rahul:",[p for p in female if aunt(p, "Rahul")])
print("Cousins of Anil:", [p for p in male|female if cousin(p, "Anil")])
