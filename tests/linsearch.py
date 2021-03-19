l=[1, 2, 3, 4, 5]

k=2
flag=False
for i in range(len(l)):
    if (l[i]==k):
        flag=True
        print(i)
if (flag):
    print(-1)
