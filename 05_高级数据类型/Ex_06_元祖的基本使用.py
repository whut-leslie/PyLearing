info_tuple = ("zhangsan", 18, 1.75)

# 1.取值和取索引
print(info_tuple[0])
# 已经知道数据的内容，希望知道该数据在元组中的索引
print(info_tuple.index("zhangsan"))

# 2.统计计数
print(info_tuple.count("zhangsan"))
# 统计元组中包含元素的个数
print(len(info_tuple))

# 3.元组的遍历
for my_info in info_tuple:
    print(my_info, end=" ")