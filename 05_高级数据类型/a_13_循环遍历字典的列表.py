students = [
    {"name": "atu"},
    {"name": "xiaomei"}
]

find_name = "xiaomei1"

for stu_dict in students:

    print(stu_dict)

    if stu_dict["name"] == find_name:
        print("found %s" % find_name)
        break
else:
    print("not found %s" % find_name)

print("loop over")

