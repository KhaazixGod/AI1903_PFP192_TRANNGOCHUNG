def check():
    f=0
    x = input()
    while not f:
        try: x = float(x)
        except :
            print("Error")
            x=input()
        else:
            return x
x=check()
if x<4:
    print('F 0')
elif x<5.5:
    print("D 1")
elif x<7:
    print("C 2")
elif x<8.5:
    print("B 3")
else:
    print("A 4")