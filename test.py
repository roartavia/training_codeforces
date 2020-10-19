houses = int(input().split()[0])
tasks = list(map(int, input().split()))
current = tasks[0]
# because she is in the house #1
moves = current - 1
idx = 1
while idx < len(tasks):
    nextTask = tasks[idx]
    if nextTask != current:
        if nextTask < current:
            # need to go all around
            moves += (houses - current) + nextTask
            current = nextTask
        else:
           # just add the dif
            moves += nextTask - current
            current = nextTask
    idx += 1
print(moves)
