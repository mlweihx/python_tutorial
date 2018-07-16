# 1打开
file = open("README")
file_copy = open("README_copy", "w")

# 2读 写
text = file.read()
file_copy.write(text)

# 3关闭
file.close()
file_copy.close()
