# 1.定义 holiday_name 字符串变量记录节日名称
# 2.如果是 情人节应该 买玫瑰/看电影
# 3.如果是平安夜 应该买苹果/吃大餐
# 4.如果是生日应该买蛋糕
# 5.其他的日子每天都是节日啊

holiday_name = "平安夜"

if holiday_name == "平安夜":  # 注意
    print("买苹果")
    print("吃大餐")

elif holiday_name == "情人节":
    print("买玫瑰")
    print("看电影")

elif holiday_name == "生日":
    print("买蛋糕")

else:
    print("每天都是节日啊")
