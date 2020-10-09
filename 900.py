# WHERE: https://codeforces.com/problemset/page/4?order=BY_RATING_ASC

# 1
# Football
# https://codeforces.com/problemset/problem/96/A
# Input
# The first input line contains a non-empty string consisting of characters "0" and "1", which represents players. The length of the string does not exceed 100 characters. There's at least one player from each team present on the field.
# Output
# Print "YES" if the situation is dangerous. Otherwise, print "NO".

# listPlayers = input()
# currentTeam = 1

# for playerIndex in range(1, len(listPlayers)):
#     if currentTeam == 7:
#         break
#     if listPlayers[playerIndex - 1] == listPlayers[playerIndex]:
#         currentTeam += 1
#     else:
#         currentTeam = 1

# if currentTeam == 7:
#     print("YES")
# else:
#     print("NO")
# ---------------------------------------------------------------------------------------------------------------------

# 2
# Twins
# https://codeforces.com/problemset/problem/160/A
# Input
# The first line contains integer n (1 ≤ n ≤ 100) — the number of coins. The second line contains a sequence of n integers a1, a2, ..., an (1 ≤ ai ≤ 100) — the coins values. All numbers are separated with spaces.
# Output
# In the single line print the single number — the minimum needed number of coins.

# OTHER SOLUTION
# There is a better way to do it, sort the list, and add to my coins the until is greater than the sum of all the coins - the coins i removed

# def getIndexMaxNumber(listNumber):
#     maxIndex = 0
#     for i in range(1, len(listNumber)):
#         if listNumber[i] > listNumber[maxIndex]:
#             maxIndex = i
#     return maxIndex


# def getIndexLessNumber(listNumber):
#     lessIndex = 0
#     for i in range(1, len(listNumber)):
#         if listNumber[i] < listNumber[lessIndex]:
#             lessIndex = i
#     return lessIndex


# def sumCoins(listCoins):
#     sum = 0
#     for i in range(0, len(listCoins)):
#         sum += listCoins[i]
#     return sum


# numCoins = int(input())
# coins = list(map(int, input().split()))
# myCoins = []
# broCoins = []
# currentIndex = 0
# for i in range(numCoins):
#     maxCoinIndex = getIndexMaxNumber(coins)
#     lessCoinIndex = getIndexLessNumber(coins)
#     if sumCoins(myCoins) <= (sumCoins(broCoins) + coins[maxCoinIndex]):
#         myCoins.append(coins[maxCoinIndex])
#         del coins[maxCoinIndex]
#     else:
#         broCoins.append(coins[lessCoinIndex])
#         del coins[lessCoinIndex]
# print(len(myCoins))

# ---------------------------------------------------------------------------------------------------------------------

# 3
# HQ9+
# https://codeforces.com/problemset/problem/133/A
# Input
# The input will consist of a single line p which will give a program in HQ9+. String p will contain between 1 and 100 characters, inclusive. ASCII-code of each character of p will be between 33 (exclamation mark) and 126 (tilde), inclusive.
# Output
# Output "YES", if executing the program will produce any output, and "NO" otherwise.

# listPlayers = input()
# if "H" in listPlayers or "Q" in listPlayers or "9" in listPlayers:
#     print("YES")
# else:
#     print("NO")
# ---------------------------------------------------------------------------------------------------------------------

# 4
# Kefa and First Steps
# https://codeforces.com/problemset/problem/580/A
# Input
# The first line contains integer n (1 ≤ n ≤ 105).
# The second line contains n integers a1,  a2,  ...,  an (1 ≤ ai ≤ 109).
# Output
# Print a single integer — the length of the maximum non-decreasing subsegment of sequence a.

# cuantItems = int(input())
# itemsList = list(map(int, input().split()))

# maxSequenceCounter = 1
# prevMax = 1
# for idx in range(1, len(itemsList)):
#     if itemsList[idx - 1] <= itemsList[idx]:
#         maxSequenceCounter += 1
#     else:
#         maxSequenceCounter = 1
#     if prevMax < maxSequenceCounter:
#         prevMax = maxSequenceCounter
# print(prevMax)
# ---------------------------------------------------------------------------------------------------------------------
