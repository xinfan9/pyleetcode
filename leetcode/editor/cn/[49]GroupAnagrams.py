class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# 给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。 
# 
#  
# 
#  示例 1: 
# 
#  
#  输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"] 
#  
# 
#  输出: [["bat"],["nat","tan"],["ate","eat","tea"]] 
# 
#  解释： 
# 
#  
#  在 strs 中没有字符串可以通过重新排列来形成 "bat"。 
#  字符串 "nat" 和 "tan" 是字母异位词，因为它们可以重新排列以形成彼此。 
#  字符串 "ate" ，"eat" 和 "tea" 是字母异位词，因为它们可以重新排列以形成彼此。 
#  
# 
#  示例 2: 
# 
#  
#  输入: strs = [""] 
#  
# 
#  输出: [[""]] 
# 
#  示例 3: 
# 
#  
#  输入: strs = ["a"] 
#  
# 
#  输出: [["a"]] 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= strs.length <= 10⁴ 
#  0 <= strs[i].length <= 100 
#  strs[i] 仅包含小写字母 
#  
# 
#  Related Topics 数组 哈希表 字符串 排序 👍 2865 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        my_dict = {}
        for str in strs:
            fingerprint_list = (0)*26
            for c in str:
                fingerprint_list[ord(c) - ord('a')] += 1
            fingerprint = ".".join(f"{c}" for c in fingerprint_list)
            if fingerprint in my_dict:
                my_dict[fingerprint].append(str)
            else:
                my_dict[fingerprint] = [str]
        return [vs for _, vs in my_dict.items()]
# leetcode submit region end(Prohibit modification and deletion)
