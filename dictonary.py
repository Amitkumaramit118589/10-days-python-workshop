D = {101: "CE", 102: "ME", 105: "CSE(IOT)"}
D.pop(105)
D.update({105: ["cse", "cse(iot)"]})
print(D[105][1])
print(D[105][0])
