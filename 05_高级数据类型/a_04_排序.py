import keyword

name_list = ["张三", "李四", "王五", "张三"]
num_list = [3, 5, 7, 8, 0, 5, 4]

name_list.sort()
num_list.sort()

name_list.sort(reverse=True)
num_list.sort(reverse=True)

print(name_list)



print(len(keyword.kwlist))
