# 1打开
file = open("README")
file_copy = open("README_copy", "a")

# 2读 写
while True:
    # 读取一行文件
    text = file.readline()

    # 判断是否读取到内容
    if not text:
        break

    file_copy.write(text)

# 3关闭
file.close()
file_copy.close()
