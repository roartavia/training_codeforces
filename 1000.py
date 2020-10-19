# WHERE:  https://codeforces.com/problemset/page/6?order=BY_RATING_ASC
import math

# Theatre Square
# https://codeforces.com/problemset/problem/1/A
# Input
# The input contains three positive integer numbers in the first line: n,  m and a (1 ≤  n, m, a ≤ 109).
# Output
# Write the needed number of flagstones.
# listInputs = list(map(int, input().split()))
# m, n, a = listInputs[0], listInputs[1], listInputs[2]
# print(math.ceil(m/a)*math.ceil(n/a))
# ---------------------------------------------------------------------------------------------------------------------

# String Task
# https://codeforces.com/problemset/problem/118/A
# Input
# The first line represents input string of Petya's program. This string only consists of uppercase and lowercase Latin letters and its length is from 1 to 100, inclusive.
# Output
# Print the resulting string. It is guaranteed that this string is not empty.
# strInput = input().lower()
# vocals = ["a", "o", "i", "e", "u", "y"]
# newStr = ""


# def isVocal(letter, _vocals):
#     for vocal in _vocals:
#         if vocal == letter:
#             return True
#     return False


# for letter in strInput:
#     if not isVocal(letter, vocals):
#         newStr += "." + letter

# print(newStr)
# ---------------------------------------------------------------------------------------------------------------------

# Young Physicist
# https://codeforces.com/problemset/problem/69/A
# Input
# The first line contains a positive integer n (1 ≤ n ≤ 100), then follow n lines containing three integers each: the xi coordinate, the yi coordinate and the zi coordinate of the force vector, applied to the body ( - 100 ≤ xi, yi, zi ≤ 100).
# Output
# Print the word "YES" if the body is in equilibrium, or the word "NO" if it is not.
# times = int(input())
# x = 0
# y = 0
# z = 0

# for time in range(times):
#     coordinates = list(map(int, input().split()))
#     x += coordinates[0]
#     y += coordinates[1]
#     z += coordinates[2]

# if x == 0 and y == 0 and z == 0:
#     print("YES")
# else:
#     print("NO")
# ---------------------------------------------------------------------------------------------------------------------


# Chat room
# https://codeforces.com/problemset/problem/58/A
# Input
# The first and only line contains the word s, which Vasya typed. This word consisits of small Latin letters, its length is no less that 1 and no more than 100 letters.
# Output
# If Vasya managed to say hello, print "YES", otherwise print "NO".
# strInput = input()
# isValid = False
# wordToValidate = "hello"
# wordLength = len(wordToValidate)
# currentIdx = 0

# for letter in strInput:
#     if letter == wordToValidate[currentIdx]:
#         currentIdx += 1
#     if currentIdx == wordLength:
#         isValid = True
#         break
# if isValid:
#     print("YES")
# else:
#     print("NO")
# ---------------------------------------------------------------------------------------------------------------------

# Lucky Division
# https://codeforces.com/problemset/problem/122/A
# Input
# The single line contains an integer n (1 ≤ n ≤ 1000) — the number that needs to be checked.
# Output
# In the only line print "YES" (without the quotes), if number n is almost lucky. Otherwise, print "NO" (without the quotes).
# integer = int(input())
# luckNumbers = [
#     4,
#     7,
#     44,
#     47,
#     74,
#     77,
#     444,
#     447,
#     474,
#     477]
# isValid = False
# for luckNumber in luckNumbers:
#     if integer == luckNumber or integer % luckNumber == 0:
#         isValid = True
#         break
# if isValid:
#     print("YES")
# else:
#     print("NO")

# ---------------------------------------------------------------------------------------------------------------------

# either it only contains uppercase letters
# or all letters except for the first one are uppercase.
# strToChange = input()
# isNeedChange = True
# newStr = strToChange
# for idx in range(1, len(strToChange)):
#     if strToChange[idx] != strToChange[idx].upper():
#         isNeedChange = False
#         break
# if strToChange[0] == strToChange[0].upper() and isNeedChange:
#     newStr = strToChange.lower()
#     isNeedChange = False
# if isNeedChange:
#     newStr = strToChange[0].upper() + strToChange[1:len(strToChange)].lower()
# print(newStr)
# ---------------------------------------------------------------------------------------------------------------------

# Dragons
# https://codeforces.com/problemset/problem/230/A
# Input
# The first line contains two space-separated integers s and n (1 ≤ s ≤ 104, 1 ≤ n ≤ 103). Then n lines follow: the i-th line contains space-separated integers xi and yi (1 ≤ xi ≤ 104, 0 ≤ yi ≤ 104) — the i-th dragon's strength and the bonus for defeating it.
# Output
# On a single line print "YES" (without the quotes), if Kirito can move on to the next level and print "NO" (without the quotes), if he can't.

# firstLine = list(map(int, input().split()))
# myStrength = firstLine[0]
# dragons = firstLine[1]
# dragonsLifes = []
# for dragon in range(dragons):
#     dragonInfo = list(map(int, input().split()))
#     dragonLife = dragonInfo[0]
#     dragonBonus = dragonInfo[1]
#     if dragonLife < myStrength:
#         myStrength += dragonBonus
#     else:
#         # Add it to the list
#         if len(dragonsLifes) > 0:
#             isInserted = False
#             for idx in range(len(dragonsLifes)):
#                 if dragonsLifes[idx]["life"] > dragonLife:
#                     isInserted = True
#                     dragonsLifes.insert((idx),
#                                         {
#                                             "life": dragonLife,
#                                             "bonus": dragonBonus
#                     }
#                     )
#                     break
#             if not isInserted:
#                 dragonsLifes.append(
#                     {
#                         "life": dragonLife,
#                         "bonus": dragonBonus
#                     }
#                 )
#         else:
#             dragonsLifes.append(
#                 {
#                     "life": dragonLife,
#                     "bonus": dragonBonus
#                 }
#             )
# isWinner = True
# for dragon in dragonsLifes:
#     if dragon["life"] < myStrength:
#         myStrength += dragon["bonus"]
#     else:
#         isWinner = False
#         break

# if isWinner:
#     print("YES")
# else:
#     print("NO")

# ---------------------------------------------------------------------------------------------------------------------

# Xenia and Ringroad
# https://codeforces.com/problemset/problem/339/B
# Input
# The first line contains two integers n and m (2 ≤ n ≤ 105, 1 ≤ m ≤ 105). The second line contains m integers a1, a2, ..., am (1 ≤ ai ≤ n). Note that Xenia can have multiple consecutive tasks in one house.
# Output
# Print a single integer — the time Xenia needs to complete all tasks.
# Please, do not use the %lld specifier to read or write 64-bit integers in С++. It is preferred to use the cin, cout streams or the %I64d specifier.
# houses = int(input().split()[0])
# tasks = list(map(int, input().split()))
# current = tasks.pop(0)
# # because she is in the house #1
# moves = current - 1
# while len(tasks) > 0:
#     nextTask = tasks.pop(0)
#     if nextTask != current:
#         if nextTask < current:
#             # need to go all around
#             moves += (houses - current) + nextTask
#             current = nextTask
#         else:
#            # just add the dif
#             moves += nextTask - current
#             current = nextTask

# print(moves)

# I removed the POP() and it reduce the time by two times:
# only use pop when its really necesarry
# houses = int(input().split()[0])
# tasks = list(map(int, input().split()))
# current = tasks[0]
# # because she is in the house #1
# moves = current - 1
# idx = 1
# while idx < len(tasks):
#     nextTask = tasks[idx]
#     if nextTask != current:
#         if nextTask < current:
#             # need to go all around
#             moves += (houses - current) + nextTask
#             current = nextTask
#         else:
#            # just add the dif
#             moves += nextTask - current
#             current = nextTask
#     idx += 1
# print(moves)


# ---------------------------------------------------------------------------------------------------------------------

# New Year Transportation
# https://codeforces.com/problemset/problem/500/A
# Input
# The first line contains two space-separated integers n (3 ≤ n ≤ 3 × 104) and t (2 ≤ t ≤ n) — the number of cells, and the index of the cell which I want to go to.
# The second line contains n - 1 space-separated integers a1, a2, ..., an - 1 (1 ≤ ai ≤ n - i). It is guaranteed, that using the given transportation system, one cannot leave the Line World.
# Output
# If I can go to cell t using the transportation system, print "YES". Otherwise, print "NO".

# ---------------------------------------------------------------------------------------------------------------------
