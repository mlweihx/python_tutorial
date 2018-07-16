i = 0
sum_i = 0

while i <= 100:
    sum_i += i
    i += 1

print("i is %d, sum is %d" % (i, sum_i))

# 0-100 之间的偶数（even）求和

i = 0
sum_even = 0

while i <= 100:
    if i % 2 == 0:
        print(i)
        if i == 50:
            break
        sum_even += i
    i += 1

print("i is %d, sum is %d" % (i, sum_even))
