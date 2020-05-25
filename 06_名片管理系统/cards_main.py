import cards_input
import cards_tools

if __name__ == '__main__':
    while True:
        cards_tools.show_menu()
        selection = int(input("请输入操作选项"))
        print("您选择的操作是【%s】" % selection)
        if selection == 1:
            cards_tools.add_card()
        elif selection == 2:
            cards_tools.show_cards()
        elif selection == 3:
            cards_tools.search_card()
        elif selection == 0:
            print("欢迎再次使用名片管理系统")
            break
        else:
            print("输入错误，请重新输入")
            continue