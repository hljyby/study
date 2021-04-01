def a(num):
    n = 0
    while n < num:
        yield n
        n+=1

# print(a(5))
for i in a(5):
    print(i)