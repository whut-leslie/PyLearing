name_list = ["张三", "李四", "王五"]
# 使用 del 关键字(delete)删除列表元素
del name_list[1]
# del 关键字本质上是用来将一个变量从内存中删除
name = "x"
del name
print(name)
print(name_list)

# 注意：如果使用del这个关键字将变量从内存中删除、
# 后续的代码就不能再使用这个变量了
print(name)
print(name_list)