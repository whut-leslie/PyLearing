students = [
    {"name": "阿土"},
    {"name": "小美"}
]

# 在学员列表中搜索指定的姓名
find_name = "张三"
for stu_dict in students:
    print(stu_dict)
    if stu_dict["name"] == find_name:
        print("找到了 %s" % find_name)
        break
else:
    print("没找到用户 %s" % find_name)

print("循环结束")