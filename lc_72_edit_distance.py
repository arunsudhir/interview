# this is a DP problem to find the minimum edit distance from one word to another
'''
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character
 

Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')


Solution method:
To solve we will use a two dimenstional DP matrix to memoize
the idea is
to convert from empty string to word1 of length m , we need m steps
to convert from empty string to word1 of length n , we need n steps
we use those as the base cases
and populate the array with those values for the lat \st column (word1)
and last row (word2) respectively

Then we go and and see if two letters word1[i] and word2[j] are same . \if so, we jsut populate 
the value at [i+1][j+1] onto i,j. If not we need to take the minimum of i+1,j (delete)
j+1,i (insert) or i+1,j+1 (replace) 

'''

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        # first initialize the array to all inf
        dp_arr = [[0] * (n+1) for _ in range(m + 1)]

        # initialize base cases
        for i in range(m,-1,-1):
            dp_arr[i][n] = m - i # last column
        for i in range(n,-1,-1):
            dp_arr[m][i] = n - i # last row

        #fill dp table bottom right to top left
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                #if same char jsut get the next diagonal value
                if word1[i] == word2[j]:
                    dp_arr[i][j] = dp_arr[i+1][j+1]   
                else:
                    dp_arr[i][j] = 1 + min (dp_arr[i+1][j],  # delete
                                            dp_arr[i][j+1],  # insert 
                                            dp_arr[i+1][j+1]) #replace
        return dp_arr[0][0]
