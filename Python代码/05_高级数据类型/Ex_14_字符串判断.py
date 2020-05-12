# 1.判断空白字符
str1 = "   "
print(str1.isspace())
str2 = "    a"
print(str2.isspace())
str3 = "        \t\n\r"
print(str3.isspace())

# 2.判断字符串中是否只包含数字
# 1>都不能判断小数
# num1="1.1"
# 2> unicode 字符串
# num = "\u00b2"
# 3> 中文数字
# num ="一千零一"

num1 = "123"
print(num1)
print(num1.isdecimal())
print(num1.isdigit())
print(num1.isnumeric())
num2 = "1.1"
print(num2)
print(num2.isdecimal())
print(num2.isdigit())
print(num2.isnumeric())
num3 = "①"
print(num3)
print(num3.isdecimal())
print(num3.isdigit())
print(num3.isnumeric())
num4 = "\u00b2"
print(num4)
print(num4.isdecimal())
print(num4.isdigit())
print(num4.isnumeric())
num5 = "一千零一"
print(num5)
print(num5.isdecimal())
print(num5.isdigit())
print(num5.isnumeric())