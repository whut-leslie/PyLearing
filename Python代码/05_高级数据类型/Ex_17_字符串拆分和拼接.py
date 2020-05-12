# 要求：
# 1.将字符串中的空白字符全部去掉
# 2.再使用 "　"作为分隔符，拼接成一个整齐的字符串

poem_str = "\t\n登鹳雀楼\t王焕之\t白日依山尽\t\n黄河入海流\t  欲穷千里目\t更上一层楼"
print(poem_str)

# 1.拆分字符串
poem = poem_str.split()
print(poem)

# 2.合并字符串
result = " ".join(poem)
print(result)

