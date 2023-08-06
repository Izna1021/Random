
class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        # Add the start and end points of the stick to the cuts list
        cuts.append(0)
        cuts.append(n)
        cuts.sort()

        m = len(cuts)
        # Initialize a 2D array to store the minimum cost between two points
        dp = [[0] * m for _ in range(m)]

        # Iterate over the lengths of the cuts
        for length in range(2, m):
            for i in range(m - length):
                j = i + length
                # Initialize the minimum cost with a large value
                dp[i][j] = float('inf')

                # Calculate the cost for all possible cuts between i and j
                for k in range(i + 1, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + cuts[j] - cuts[i])

        return dp[0][m - 1]
