# 定义字符串变量 name,输出 我的名字叫小明，请多多关照
name = "小明"
print("我的名字叫 %s,请多多关照!" % name)
# 定义整数变量 student_no，输出我的学号是000001
student_1 = 1
print("我的学号是%06d" % student_1)
student_2 = 100
print("我的学号是%06d" % student_2)
student_3 = 1234567
print("我的学号是%06d" % student_3)

# 定义小数 price、weight、money
# 输出 苹果单价 9.00元/斤，购买了5.00斤
price = 9.0
weight = 5.0
money = price * weight
print("苹果单价为 %.2f元/斤，购买了 %.2f 斤，需要支付%.2f元" % (price ,weight ,money))

# 定义一个小数 scale，输出数据比例是10.00%
scale = 0.1
print("数据比例是%.02f%%" % (scale*100))
