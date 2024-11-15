from typing import List

MAXSIZE = 100

def edit_dist_arrays_DP(a: List[int], b: List[int], m: int, n: int) -> int:
    # Create a table to store results of subproblems
    dp = [[0] * (MAXSIZE + 1) for _ in range(MAXSIZE + 1)]

    # Fill dp[][] in bottom-up manner
    for i in range(m + 1):
        for j in range(n + 1):
            # If first string is empty, only option is to insert all characters of second string
            if i == 0:
                dp[i][j] = j  # Min. operations = j

            # If second string is empty, only option is to remove all characters of second string
            elif j == 0:
                dp[i][j] = i  # Min. operations = i

            # If last characters are same, ignore last char and recur for remaining string
            elif a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]

            # If the last character is different, consider all possibilities and find the minimum
            else:
                x = dp[i][j - 1]  # Insert
                y = dp[i - 1][j]  # Remove
                z = dp[i - 1][j - 1]  # Replace

                # Find the minimum of the three operations (Insert, Remove, Replace)
                dp[i][j] = 1 + min(x, y, z)

    return dp[m][n]
