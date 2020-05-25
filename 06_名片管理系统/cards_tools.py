# 记录所有的名片字典
card_list = []


def show_menu():
    print("*"*50)
    print("1.新建名片"'\n'
          "2.显示全部"'\n'
          "3.查询名片"'\n''\n'
          "0.退出系统")
    print("*"*50)


def add_card():
    """
    新增名片
    :return:
    """
    print("-"*50)
    print("***新增名片***")
    name_str = str(input("请输入姓名："))
    phone_str = str(input("请输入电话："))
    qq_str = str(input("请输入qq："))
    email_str = str(input("请输入邮箱："))
    card_dict = {"name": name_str,
                 "phone": phone_str,
                 "qq": qq_str,
                 "email": email_str}
    card_list.append(card_dict)
    print("添加成功")


def show_cards():
    """
    显示所有名片
    :param self:
    :param card_list:
    :return:
    """
    print("-" * 50)
    print("***显示所有名片***")
    if len(card_list) == 0:
        print("当前无名片记录，请使用【新建名片】添加")
        return
    else:
        for name in ["姓名", "电话", "QQ", "email"]:
            print(name, end="\t\t\t")
        print("="*50)
        for card_dict in card_list:
            print("%s\t\t\t%s\t\t\t%s\t\t\t%s"
                  % (card_dict["name"],
                     card_dict["phone"],
                     card_dict["qq"],
                     card_dict["email"]))


def search_card():
    """
    搜索名片
    :return:
    """
    print("-" * 50)
    print("***搜索名片***")