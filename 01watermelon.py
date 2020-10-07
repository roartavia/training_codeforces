inputFromUser = input()
watermelonWeight = int(inputFromUser)
nTimes = watermelonWeight//2
isCorrect = False
lesserNumber = nTimes

for i in range(nTimes):
    if lesserNumber % 2 == 0 and (watermelonWeight - lesserNumber) % 2 == 0:
        isCorrect = True
        break
    lesserNumber = lesserNumber - 1
if (isCorrect):
    print("YES")
else:
    print("NO")
