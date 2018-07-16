# # 判断字符串是否仅由空格或其他空白字符组成
#
# space = "\n  333 \n \t \r "
# print(space)
# print(space.isspace())
#
# # 判断字符串中是否只包含数字
#
# print(space.strip())
# print(space)
#

str_test = "ni shi ge\n da\r hao\t ren"
print(str_test)

str_list = str_test.split()
print(str_list)

result = "|".join(str_list)
print(result)

str_python = "Life is short, you need python."
test = str_python[0: ]
print(test)


for num in [1, 2, 3, 4]:
    
    print(num)
    if num == 2:
        break

else:
    print("over")
