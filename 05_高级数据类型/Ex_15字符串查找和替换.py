hello_str = "hello world"
# 1.判断是否以指定字符串开始
print(hello_str.startswith("hello"))

# 2.判断是否以是定字符串结束
print(hello_str.endswith("orl"))

# 3.查找指定字符串
# index同样可以查找指定的字符串在大字符串中的索引
print(hello_str.find("or"))
print(hello_str.find("abc"))
# index如果指定的字符串不存在，会报错
# find如果指定的字符串不存在，会返回-1

# 4.替换字符串
# replace方法执行后会返回一个新的字符串
# 注意：不会修改原有的字符串的内容，假替换？
print(hello_str.replace("o","y"))
print(hello_str)