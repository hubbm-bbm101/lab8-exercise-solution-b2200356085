import sys

student = {}

student_file = open(sys.argv[1], "r")
for l in student_file:
    name = l.split(":")[0]
    student[name] = (l.split(":")[1]).split(",")

for n in sys.argv[2].split(","):
    try:
        uni = student[n][0]
        dep = student[n][1]
        print(f"Student information for {n}: {uni},{dep}")
    except KeyError:
        print(f"There is no student such  as {n}")


