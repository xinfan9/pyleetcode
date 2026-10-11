
# 给你一个字符串 s，找到 s 中最长的 回文 子串。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "babad"
# 输出："bab"
# 解释："aba" 同样是符合题意的答案。
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "cbbd"
# 输出："bb"
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 1000 
#  s 仅由数字和英文字母组成 
#  
# 
#  Related Topics 双指针 字符串 动态规划 Manacher 算法 👍 8189 👎 0

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        dp[i][j] : if palindrome from i to j
        dp[i][j] = dp[i + 1][j - 1] and s[i] == s[j]
        dp[x][x] = true
        """
        length = len(s)
        max_start = 0
        max_end = 0
        max_len = 0
        dp = [[False for _ in range(length)] for _ in range(length)]
        for i in range(length):
            for j in range(i):
                if s[i] == s[j] and (i - j <= 2 or dp[j + 1][i - 1]):
                    dp[j][i] = True
                    if i - j + 1 > max_len:
                        max_start = j
                        max_end = i
                        max_len = i - j + 1
        return s[max_start: max_end + 1]

# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    s = Solution()
    print(s.longestPalindrome("babad"))
    print(s.longestPalindrome("cbbd"))