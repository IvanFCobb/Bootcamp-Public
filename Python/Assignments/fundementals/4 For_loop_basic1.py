for x in range(151):
    print(x)

for x in range(0, 1001, 5):
    print(x)

for x in range(0, 101, 1):
    if x % 10 == 0:
        print("Coding Dojo")
    elif x % 5 == 0:
        print("Coding")
    else:
        print(x)

total = 0
for x in range(1, 500000, 2):
    total = total + x

print(total)

year = 2018
while year > 0:
    print(year)
    year = year-4

lowNum = 2
highNum = 9
mult = 3

for x in range(lowNum, highNum+1):
    if x % mult == 0:
        print(x)
