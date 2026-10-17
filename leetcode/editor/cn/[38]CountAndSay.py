class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# 「外观数列」是一个数位字符串序列，由递归公式定义： 
# 
#  
#  countAndSay(1) = "1" 
#  countAndSay(n) 是 countAndSay(n-1) 的行程长度编码。 
#  
# 
#  
# 
#  
#  
# 
#  行程长度编码（RLE）是一种字符串压缩方法，其工作原理是通过将每个最大连续相同字符组替换为该组的长度后加上该字符本身。例如，要压缩字符串 "3322251
# " ，我们将 "33" 用 "23" 替换，将 "222" 用 "32" 替换，将 "5" 用 "15" 替换并将 "1" 用 "11" 替换。因此压缩后字符串
# 变为 "23321511"。 
# 
#  给定一个整数 n ，返回 外观数列 的第 n 个元素。 
# 
#  示例 1： 
# 
#  
#  输入：n = 4 
#  
# 
#  输出："1211" 
# 
#  解释： 
# 
#  countAndSay(1) = "1" 
# 
#  countAndSay(2) = "1" 的行程长度编码 = "11" 
# 
#  countAndSay(3) = "11" 的行程长度编码 = "21" 
# 
#  countAndSay(4) = "21" 的行程长度编码 = "1211" 
# 
#  示例 2： 
# 
#  
#  输入：n = 1 
#  
# 
#  输出："1" 
# 
#  解释： 
# 
#  这是基本情况。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 30 
#  
# 
#  
# 进阶：你能迭代解决该问题吗？
# 
#  Related Topics 字符串 👍 1140 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"

        return self.convert(self.countAndSay(n - 1))

    def convert(self, nums):
        pos = 0
        res = ""
        while pos != len(nums):
            count = 1
            while pos + 1 < len(nums) and nums[pos + 1] == nums[pos]:
                pos = pos + 1
                count += 1
            res = res + f"{count}{nums[pos]}"
            pos += 1
        return res
# leetcode submit region end(Prohibit modification and deletion)
