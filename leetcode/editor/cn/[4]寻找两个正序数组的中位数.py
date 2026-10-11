
# 给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。 
# 
#  算法的时间复杂度应该为 O(log (m+n)) 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums1 = [1,3], nums2 = [2]
# 输出：2.00000
# 解释：合并数组 = [1,2,3] ，中位数 2
#  
# 
#  示例 2： 
# 
#  
# 输入：nums1 = [1,2], nums2 = [3,4]
# 输出：2.50000
# 解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5
#  
# 
#  
# 
#  
# 
#  提示： 
# 
#  
#  nums1.length == m 
#  nums2.length == n 
#  0 <= m <= 1000 
#  0 <= n <= 1000 
#  1 <= m + n <= 2000 
#  -10⁶ <= nums1[i], nums2[i] <= 10⁶ 
#  
# 
#  Related Topics 数组 二分查找 分治 👍 8060 👎 0

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
    def getKth(self, nums1, start1, end1, nums2, start2, end2, k):
        len1 = end1 - start1 + 1
        len2 = end2 - start2 + 1
        if len1 > len2:
            return self.getKth(nums2, start2, end2, nums1, start1, end1, k)
        if len1 == 0:
            return nums2[start2 + k - 1]
        if k == 1:
            return min(nums1[start1], nums2[start2])

        i = start1 + min(len1, k // 2) - 1
        j = start2 + min(len2, k // 2) - 1
        if nums1[i] > nums2[j]:
            return self.getKth(nums1, start1, end1, nums2, j + 1, end2, k - (j + 1 - start2))
        else:
            return self.getKth(nums1, i + 1, end1, nums2, start2, end2, k - (i + 1 - start1))

    def findMedianSortedArrays(self, nums1, nums2):
        m, n = len(nums1), len(nums2)
        left = (m + n + 1) // 2
        right = (m + n + 2) // 2
        return (self.getKth(nums1, 0, m - 1, nums2, 0, n - 1, left) +
                self.getKth(nums1, 0, m - 1, nums2, 0, n - 1, right)) / 2.0
# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    s = Solution()
    print(s.findMedianSortedArrays([1,3,4,5],[2,4,5,6]))
