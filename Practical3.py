newArray = ["bedha", True, 99.9, None, 100]
firstArraylen = len(newArray)
newArray.append("new")
secondarraylen = len(newArray)
print(firstArraylen - secondarraylen)

# loop
newArray = ["bedha", True, 99.9, None, 100, 2900394, "earth"]
arraylen = len(newArray)
for index in range(arraylen):
    print(newArray[index])


newArray = ["IT", "ECE", "SWE", "WRE", "MCM", "ME", "EE", "A" , "ICE", "MRE"]

newArraylen = len(newArray)
new_array = []

for index in range(newArraylen):
    elements = newArray[index]
    new_array.append(elements.lower())
for secondindex in range(len(new_array)):
    print(new_array[secondindex])
