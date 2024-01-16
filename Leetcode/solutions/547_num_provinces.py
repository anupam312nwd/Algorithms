from collections import defaultdict

class Solution:
    def findCircleNum(self, isConnected) -> int:
        N = len(isConnected)
        self.root = {i: i for i in range(N)}
        self.rank = {i: 0 for i in range(N)}

        for i in range(N - 1):
            for j in range(i + 1, N):
                if isConnected[i][j] == 1:
                    self.union(i, j)

        total_provinces = set()
        for i in range(N):
            self.root[i] = self.find(i)
            total_provinces.add(self.root[i])
        print(total_provinces)
        return len(total_provinces)

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[x] > self.rank[y]:
                self.root[y] = rootX
            elif self.rank[x] < self.rank[y]:
                self.root[x] = rootY
            else:
                self.root[x] = rootY
                self.rank[y] += 1

if __name__ == '__main__':
    isConnected = [[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]
    solution = Solution()
    num_provinces = solution.findCircleNum(isConnected)
    print(num_provinces)
