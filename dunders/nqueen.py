class Solution:
    """
    Get all distinct N-Queen solutions
    @param n: The number of queens.
    @return: All distinct solutions.
    """
    n = 0
    results = []
    cols = {}

    def attack(self, row, col):
        for c, r in self.cols.iteritems():
            if c - r == col - row or c + r == col + row:
                return True
        return False

    def search(self, row):
        if row == self.n:
            result = []
            for i in range(self.n):
                r = ['.'] * self.n
                r[self.cols[i]] = 'Q'
                result.append(''.join(r))
            self.results.append(result)
            return

        for col in range(self.n):
            if col in self.cols:
                continue
            if self.attack(row, col):
                continue
            self.cols[col] = row
            self.search(row + 1)
            del self.cols[col]

    def solveNQueens(self, n):
        self.n = n
        self.search(0)
        return self.results


s = Solution()
print(s.solveNQueens(8))