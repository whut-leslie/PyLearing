# 定义布尔类型变量 has_ticket 表示是否有车票
# 定义整型变量 knife_length 表示刀的长度
# 首先检查是否有车票 ，如果有，才允许进行安检
# 安检时，需要检查刀的长度，判断是否超过20厘米
# 如果超过20厘米，提示刀的长度不允许上车
# 如果没有车票，不允许进门
has_ticket = True
has_knife = True
knife_length = 11
if has_ticket:
    print("车票检查通过，准备开始安检")
    if has_knife:
        if knife_length > 20:
            print("刀的长度有%d不允许上车" % knife_length)
        else:
            print("允许上车")
    else:
        print("允许上车")
else:
    print("没有车票，不能上车")
