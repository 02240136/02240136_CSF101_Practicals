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

newArray = ["ECE", "Cv", "IT", "ME", "WRE", "EE", "SWE", "ICE", "arch", "EG"]
print("Original array: ", newArray)

lowercasearray = [str(item).lower() for item in newArray]
print("lowercase array: ", lowercasearray)

sampleArray = ["ECE", "CV", "IT", "ME", "WRE", "EE", "SWE", "ICE", "ARCH", "EG"]
arraylen = len(sampleArray)
newArray = []
for index in range(arraylen):
    allElement = sampleArray[index]
    newArray.append(allElement.lower())

for secondindex in range(len(newArray)):
    print(newArray[secondindex]) 