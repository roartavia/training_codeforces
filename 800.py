# 1
# Watermelon
# https://codeforces.com/problemset/problem/4/A
# Input
# The first (and the only) input line contains integer number w (1 ≤ w ≤ 100) — the weight of the watermelon bought by the boys.
# Output
# Print YES, if the boys can divide the watermelon into two parts, each of them weighing even number of kilos; and NO in the opposite case.

# inputFromUser = input()
# watermelonWeight = int(inputFromUser)
# nTimes = watermelonWeight//2
# isCorrect = False
# lesserNumber = nTimes

# for i in range(nTimes):
#     if lesserNumber % 2 == 0 and (watermelonWeight - lesserNumber) % 2 == 0:
#         isCorrect = True
#         break
#     lesserNumber = lesserNumber - 1
# if (isCorrect):
#     print("YES")
# else:
#     print("NO")
# ---------------------------------------------------------------------------------------------------------------------

# 2
# Way Too Long Words
# https://codeforces.com/problemset/problem/71/A
# Input
# The first line contains an integer n (1 ≤ n ≤ 100). Each of the following n lines contains one word. All the words consist of lowercase Latin letters and possess the lengths of from 1 to 100 characters.
# Output
# Print n lines. The i-th line should contain the result of replacing of the i-th word from the input data.

# howManyInputs = int(input())
# wordsReplacedList = []
# for i in range(howManyInputs):
#     newWord = input()
#     wordLength = len(newWord)
#     if (wordLength > 10):
#         newWord = newWord[0] + str(wordLength - 2) + \
#             newWord[wordLength - 1]
#     wordsReplacedList.append(newWord)
# for word in wordsReplacedList:
#     print(word)
# ---------------------------------------------------------------------------------------------------------------------

# 3
# Team
# https://codeforces.com/problemset/problem/231/A
# Input
# The first input line contains a single integer n (1 ≤ n ≤ 1000) — the number of problems in the contest. Then n lines contain three integers each, each integer is either 0 or 1. If the first number in the line equals 1, then Petya is sure about the problem's solution, otherwise he isn't sure. The second number shows Vasya's view on the solution, the third number shows Tonya's view. The numbers on the lines are separated by spaces.
# Output
# Print a single integer — the number of problems the friends will implement on the contest.

# howManyInputs = int(input())
# listProblems = []
# listProblemsSolved = 0
# for i in range(howManyInputs):
#     solutionsInput = input()
#     solutionList = solutionsInput.split(" ")
#     countOne = 0
#     for numberStr in solutionList:
#         if numberStr == "1":
#             countOne = countOne + 1
#     if (countOne >= 2):
#         listProblemsSolved = listProblemsSolved + 1
# print(listProblemsSolved)
# ---------------------------------------------------------------------------------------------------------------------

# 4
# Next Round
# https://codeforces.com/problemset/problem/158/A
# Input
# The first line of the input contains two integers n and k (1 ≤ k ≤ n ≤ 50) separated by a single space.
# The second line contains n space-separated integers a1, a2, ..., an (0 ≤ ai ≤ 100), where ai is the score earned by the participant who got the i-th place. The given sequence is non-increasing (that is, for all i from 1 to n - 1 the following condition is fulfilled: ai ≥ ai + 1).
# Output
# Output the number of participants who advance to the next round.

# def toInt(strNumber):
#     return int(strNumber)


# numberInputsAndMinScore = input()
# scores = input()
# numberInputsAndMinScoreList = numberInputsAndMinScore.split(" ")
# scoresList = scores.split(" ")
# nextRoundCounter = 0
# scoresListToInt = list(map(toInt, scoresList))
# isDone = False
# for i in range(int(numberInputsAndMinScoreList[1])):
#     if scoresListToInt[i] != 0:
#         nextRoundCounter += 1
#     else:
#         isDone = True
#         break

# if not isDone:
#     minScore = scoresListToInt[int(numberInputsAndMinScoreList[1]) - 1]
#     for i in range(int(numberInputsAndMinScoreList[1]), int(numberInputsAndMinScoreList[0])):
#         if scoresListToInt[i] == minScore:
#             nextRoundCounter += 1

# print(nextRoundCounter)
# ---------------------------------------------------------------------------------------------------------------------

# 5
# Domino piling
# https://codeforces.com/problemset/problem/50/A
# Input
# In a single line you are given two integers M and N — board sizes in squares (1 ≤ M ≤ N ≤ 16).
# Output
# Output one number — the maximal number of dominoes, which can be placed.
# area = input()
# areaList = area.split(" ")
# totalArea = int(areaList[0]) * int(areaList[1])

# print(totalArea//2)
# ---------------------------------------------------------------------------------------------------------------------

# 6
# Bit++
# https://codeforces.com/problemset/problem/282/A
# Input
# The first line contains a single integer n (1 ≤ n ≤ 150) — the number of statements in the programme.
# Next n lines contain a statement each. Each statement contains exactly one operation (++ or --) and exactly one variable x (denoted as letter «X»). Thus, there are no empty statements. The operation and the variable can be written in any order.
# Output
# Print a single integer — the final value of x.

times = int(input())
answer = 0
for i in range(times):
    statement = input()
    if statement == "--X" or statement == "X--":
        answer -= 1
    else:
        answer += 1
print(answer)
# ---------------------------------------------------------------------------------------------------------------------
