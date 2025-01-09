for i in (2,3,5,7):
    print(i)
for i in range(1,100):
    if i == 1:
        pass
    elif i%2 == 0 or i%3 == 0 or i%5 == 0 or i%7 == 0:
        pass
    else:
        print(i)
