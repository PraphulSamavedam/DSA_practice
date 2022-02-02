from abc import ABC, abstractmethod


class UnionFind:
    @abstractmethod
    def find(self, x):
        pass

    @abstractmethod
    def union(self, x, y):
        pass


    def is_connected(self, x, y):
        return self.find(x) == self.find(y)


def checkImplementation(DisjointSolution: UnionFind):
    graphs = int(input())
    for graph in range(graphs):
        vertices, edges, testCases = map(int, input().split(" "))
        uf = DisjointSolution(vertices)
        for edge in range(edges):
            x, y = map(int, input().split(" "))
            uf.union(x, y)
        for testCase in range(testCases):
            test_X, test_y = map(int, input().split(" "))
            print(uf.is_connected(test_X, test_y))


class UnionFindQuickFind(UnionFind):
    # Quick Find implementation
    def __init__(self, size: int):  # Space Complexity: O(n)
        self.root = [x for x in range(size)]

    def find(self, x):  # Time Complexity: O(1)
        return self.root[x]

    def union(self, x, y):  # Time Complexity: O(n)
        rootX, rootY = self.find(x), self.find(y)
        if rootX != rootY:
            for i in range(len(self.root)):
                if self.root[i] == rootY:
                    self.root[i] = rootX
        return None


class UnionFindQuickUnion(UnionFind):
    def __init__(self, size: int):  # Space Complexity: O(n)
        self.root = [x for x in range(size)]

    def find(self, x):  # Time Complexity: O(n)
        while x != self.root[x]:
            x = self.root[x]
        return x

    def union(self, x, y):  # Time Complexity: O(n)
        rootX, rootY = self.find(x), self.find(y)
        if rootY != rootX:
            self.root[rootY] = rootX
        return None


class UnionFindUnionByRank(UnionFind):
    def __init__(self, size: int):  # Space Complexity: O(n)
        self.root = [x for x in range(size)]
        self.rank = [1 for x in range(size)]

    def find(self, x):  # Time Complexity: O(LogN)
        while x != self.root[x]:
            x = self.root[x]
        return x

    def union(self, x, y):  # Time Complexity: O(LogN)
        rootX, rootY = self.find(x), self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1


class UnionFindPathCompression(UnionFind):
    def __init__(self, size: int):  # Space Complexity: O(n)
        self.root = [x for x in range(size)]

    def find(self, x):  # Time Complexity: O(log N)
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):  # Time Complexity: O(log N)
        rootX, rootY = self.find(x), self.find(y)
        if rootX != rootY:
            self.root[rootY] = rootX


class UnionFindOptimized(UnionFind):
    def __init__(self, size):
        self.root =[i for i in range(size)]
        self.rank = [1]*size


    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]


    def union(self, x, y):
        rootX, rootY = self.find(x), self.find(y)
        rankX, rankY = self.rank[x], self.rank[y]
        if rootX != rootY:
            if rankX<rankY:
                self.root[rootX] = rootY
            elif rankX>rankY:
                self.root[rootY] = rootX
            else:
                self.root[rootY] = rootX
                self.rank[x] += 1



# While testing the results have to be True False
# checkImplementation(UnionFindQuickFind)
# checkImplementation(UnionFindQuickUnion)
# checkImplementation(UnionFindUnionByRank)
# checkImplementation(UnionFindPathCompression)
checkImplementation(UnionFindOptimized)
