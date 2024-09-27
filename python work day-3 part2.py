s = [7, "Amit", 4.5, True]
s.append(65)
s.insert(2, 58)
s.insert(3, "Kumar")

s.pop()
s.pop()

s.remove(4.5)

print(s[1:3])
print(len(s))

t = (6, "Amit", 4.5)
print(type(t))
print(t[0])

Days = {"Sunday", "Mondays", "Tuesday"}
print(type(Days))

set2 = set(["GECV", "GEVM", "GECC"])
print(type(set2))
