class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# 给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。 
# 
#  注意：不能使用任何内置的 BigInteger 库或直接将输入转换为整数。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: num1 = "2", num2 = "3"
# 输出: "6" 
# 
#  示例 2: 
# 
#  
# 输入: num1 = "123", num2 = "456"
# 输出: "56088" 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= num1.length, num2.length <= 200 
#  num1 和 num2 只能由数字组成。 
#  num1 和 num2 都不包含任何前导零，除了数字0本身。 
#  
# 
#  Related Topics 数学 字符串 模拟 👍 1505 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        m, n = len(num1), len(num2)
        res = [0] * (m + n)
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                p1, p2 = i + j, i + j + 1   # p2 放低位，p1 放进位
                total = mul + res[p2]       # 加上该位已有的值
                res[p2] = total % 10
                res[p1] += total // 10
        s = "".join(str(x) for x in res)
        return s.lstrip("0") or "0"

# leetcode submit region end(Prohibit modification and deletion)
