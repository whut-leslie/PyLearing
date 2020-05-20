str1 = "hello python hello"
str2 = '我的外号是"大西瓜"'
print(str2)
print(str1[0])
# 循环遍历字符串
for c in str2:
    print(c,end="")
print(" ")
# 1.统计字符串长度
length = len(str1)
print(length)

# 2.统计某一个小字符串出现的次数
print(str1.count("o"))

# 3.统计某一个子字符串出现的位置
print(str.rindex("h"))