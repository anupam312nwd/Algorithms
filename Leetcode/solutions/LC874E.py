class Solution:
    co_ordinate = [0, 0]
    direction = 0 % 4
    maxDistSq = 0

    def robotSim(self, commands, obstacles):
        for num in commands:
            if num == -2:
                direction = (direction + 3) % 4
            if num == -1:
                direction = (direction + 1) % 4
            if 1 <= num <= 9:
                if direction == 0 % 4:
                    for i in range(1, num + 1):
                        if (co_ordinate[0], co_ordinate[1] + 1) not in obstacles:
                            co_ordinate[1] += 1
                if direction == 1 % 4:
                    for i in range(1, num + 1):
                        if (co_ordinate[0] + 1, co_ordinate[1]) not in obstacles:
                            co_ordinate[0] += 1
                if direction == 2 % 4:
                    for i in range(1, num + 1):
                        if (co_ordinate[0], co_ordinate[1] - 1) not in obstacles:
                            co_ordinate[1] -= 1
                if direction == 3 % 4:
                    for i in range(1, num + 1):
                        if (co_ordinate[0] - 1, co_ordinate[1]) not in obstacles:
                            co_ordinate[0] -= 1
            maxDist = max(maxDist, co_ordinate[0] ** 2 + co_ordinate[1] ** 2)
        return maxDist
