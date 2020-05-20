# 0~100 之间的偶/奇数累加求和
i = 0
s = 0
while i <= 100:
    if i % 2 == 1:
        s += i
        print(i)
    i += 1
print("结果为%d" % s)