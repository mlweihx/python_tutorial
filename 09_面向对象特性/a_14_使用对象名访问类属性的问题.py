class Tool(object):

    # 使用赋值语句定于类属性，记录所有工具对象的数量
    count = 0

    def __init__(self, name):
        self.name = name

        # 让类属性的值 +1
        Tool.count += 1


# 创建工具对象
tool1 = Tool("斧头")
tool2 = Tool("榔头")
tool3 = Tool("水桶")

# 打印工具对象数量
# print(Tool.count)
tool3.count = 99

print("工具对象总数 %d" % tool3 .count)

print(" ====> %d" % Tool.count)
print(" ====> %d" % tool2.count)
