#! /Users/weihx/anaconda3/bin/python

import cards_tools

while True:

    # 显示功能菜单
    cards_tools.show_menu()

    action_str = input("请选择希望执行的操作： ", )
    print("您选择的操作是：【%s】" % action_str)  # , end=""

    # 1,2,3 针对名片的操作
    if action_str in ["1", "2", "3"]:

        # 新增名片
        if action_str == "1":
            cards_tools.new_card()

        # 显示全部
        elif action_str == "2":
            cards_tools.show_all()

        # 查询名片
        elif action_str == "3":
            cards_tools.search_card()

    # 0 推出系统
    elif action_str == "0":

        print("欢迎再次使用【名片管理系统】")
        break

        # pass
        # 如果在开发程序时，不希望立刻编写分之内部代码
        # 可以使用 pass 关键字，表示一个占位符，能够保证程序的代码结构完整性正确
        # 程序运行时， pass 关键字不会执行任何操作

    # 其他内容表示输入错误，需要进行提示
    else:
        print("您输入的不正确，您重新选择！")



