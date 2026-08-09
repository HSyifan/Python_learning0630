matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12]]

# 获取二维列表的行数并存放到变量 rows 中
# 获取二维列表的列数并存放到变量 cols 中

left = 0
right = cols - 1
top = 0
bottom = rows - 1

result = []

while left <= right and top <= bottom:
    # 从左往右遍历

    # 从上往下遍历

    if left < right and top < bottom:
        # 从右往左遍历

        # 从下往上遍历

    left = left + 1
    right = right - 1
    top = top + 1
    bottom = bottom - 1

print(result)
