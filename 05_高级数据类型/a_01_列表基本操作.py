
name_list = ["zhangsan", "lisi", "wangwu", "lisi"]

# 1. 取值和取索引
# index out of range
print(name_list[2])

# 知道数据的内容，想确定数据在列表中的位置
print(name_list.index("lisi"))

# 2. 修改
name_list[3] = "李四"

# 3. 增加
name_list.append("whx")
name_list.insert(2, "第二个")

temp_list = ["sun", "zhu", "shashidi"]
name_list.extend(temp_list)
print(" ------ ")

# 4. 删除
# clear 清空列表
temp_list.clear()

# 弹出最后一个，或者弹出制定索引的值
name_list.pop()

# 删除指定的值
name_list.remove("sun")
print(len(name_list))
print(" ------ ")
print(temp_list)
print(name_list)

