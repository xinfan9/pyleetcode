class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# 给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串的第一个匹配项的下标（下标从 0 开始）。
# 如果 needle 不是 haystack 的一部分，则返回 -1 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：haystack = "sadbutsad", needle = "sad"
# 输出：0
# 解释："sad" 在下标 0 和 6 处匹配。
# 第一个匹配项的下标是 0 ，所以返回 0 。
#  
# 
#  示例 2： 
# 
#  
# 输入：haystack = "leetcode", needle = "leeto"
# 输出：-1
# 解释："leeto" 没有在 "leetcode" 中出现，所以返回 -1 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= haystack.length, needle.length <= 10⁴ 
#  haystack 和 needle 仅由小写英文字符组成 
#  
# 
#  Related Topics 双指针 字符串 字符串匹配 KMP 算法 Boyer–Moore 算法 扩展 KMP 👍 2616 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n, m = len(haystack), len(needle)
        if m == 0:
            return 0
        next_arr = [0]*m
        j = 0
        for i in range(1, m):
            while j > 0 and needle[i] != needle[j]:
                j = next_arr[j - 1]
            if needle[i] == needle[j]:
                j += 1
            next_arr[i] = j
        j = 0
        for i in range(n):
            while j > 0 and haystack[i] != needle[j]:
                j = next_arr[j - 1]
            if haystack[i] == needle[j]:
                j += 1
            if j == m:
                return i - m + 1

        return -1


        
# leetcode submit region end(Prohibit modification and deletion)
