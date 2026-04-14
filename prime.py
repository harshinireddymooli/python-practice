num = int(input("Enter number: "))
flag = False

if num > 1:
    for i in range(2, int(num/2)+1):
        if num % i == 0:
            flag = True
            break

if flag:
    print("Not Prime")
else:
    print("Prime")
