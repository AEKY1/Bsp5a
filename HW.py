count=0
for i in range(1,1001):
    if(i%10!=4 and i%10!=7):
        print(i,end=' ')
        if (i%20==0):
            print("")
    else:
        count+=1
print('\nToltal number disappear',count)