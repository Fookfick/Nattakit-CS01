lis=[5,10,15,20,25,50,20]
def my_list(lis):
    x = 0
    for x in range (len(lis)):
        if lis[x]==20:
            lis[x]=200
    print(lis)
my_list(lis)