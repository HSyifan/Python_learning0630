"""递归的另一种应用：汉诺塔问题"""

def hanoi(n, x, y, z):
    if n == 1:
        print(x, '-->', z) # 如果只有一层，直接将金片从X移动到Z
    else:
        hanoi(n-1, x, z, y) # 将x上的n-1个金片移动到y上
        print(x, '-->', z)# 最底下的金片从X移动到Z
        hanoi(n-1, y, x, z)# 将y上的n-1个金片移动到z上
    
# n = int(input('请输入汉诺塔的层数: '))
# hanoi(n, 'A', 'B', 'C')

# 总过程：
# hanoi(3, A, B, C)
#  ├─① hanoi(2, A, C, B)     # 上面2片：A → B（借助 C）
#  ├─② print A --> C         # 最底片
#  └─③ hanoi(2, B, A, C)     # 上面2片：B → C（借助 A）

# 拆解过程：
# hanoi(2, A, C, B)
#  ├─ hanoi(1, A, B, C) → print A --> C     【第1行】
#  ├─ print A --> B                         【第2行】
#  └─ hanoi(1, C, A, B) → print C --> B     【第3行】
# print A --> C                             【第4行】
# hanoi(2, B, A, C)
#  ├─ hanoi(1, B, C, A) → print B --> A     【第5行】
#  ├─ print B --> C                         【第6行】
#  └─ hanoi(1, A, B, C) → print A --> C     【第7行】


# 动动手0：给定一个整数 n，请编写一个递归函数，计算从 1 + 2 + 3 + ... + n 的结果（比如 n = 10，那么结果就是 55）。
def get_sum(n):
    if n == 1:
        return 1
    else:
        return n + get_sum(n-1)
print(get_sum(10)) # 55
print(get_sum(100)) # 5050

# 动动手1：给定一个整数 n，请编写一个递归函数，判断该整数是否为 2 的幂次方。如果是返回 True，否则返回 False。
def isPowerOfTwo(n):
    if n <= 0:          # 0 和负数都不是 2 的幂；没有这句会 0//2→0 死递归
        return False
    if n == 1:
        return True
    elif n % 2 != 0: # 奇数不是2的幂
        return False
    else:
        return isPowerOfTwo(n / 2) # 如果是偶数，非1，非0
print(isPowerOfTwo(1)) # True
print(isPowerOfTwo(0)) # False
print(isPowerOfTwo(8)) # True
print(isPowerOfTwo(15)) # False

# 动动手2：请实现一个递归函数，要求只使用加号运算符（+）来实现乘法运算的结果。
def mul(x, y):
    if x == 0 or y == 0:
        return 0
    if y == 1:
        return x
    else:
        return x + mul(x, y-1)
    
print(mul(3, 4)) # 12
print(mul(3, 5)) # 15
print(mul(12, 24)) # 288

# 动动手3：给定一个列表 L，请编写一个递归函数，找到该列表中最大的元素。
def get_max(L):
    if len(L) == 1:
        return L[0]
    else:
        return max(L[0], get_max(L[1:]))

print(get_max([1, 2, 3, 4, 5])) # 5
print(get_max([1, 2, 3, 43, 5, 7, 8, 9, 19])) # 43
print(get_max([123, 23, 43, 5, 7, 8, 9, 19])) # 123

# 答案：
def get_max(L):
    if len(L) == 2:
        return L[0] if L[0] > L[1] else L[1]
    else:
        sub = get_max(L[1:])
        return L[0] if L[0] > sub else sub

# 动动手4：假设僧侣每秒钟都能正确地移动一枚金片，请问将 64 枚金片从一根银针移动到另外一根银针上，大概需要使用多少时间？
print(2**64 - 1) # 18446744073709551615












































