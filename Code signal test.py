a = [1,3,2,1]
count = 0

for x,y in zip(a,a[1:]):
    print(x,y)
    
    if((a[x] - a[y]) < 0):
        a.pop(y)
        count+=1
        if(count > 1):
            print(False)
            break