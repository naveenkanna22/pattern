n=input()
if(len(n)%2!=0):
    for i in range(0,len(n)):
        for j in range(0,len(n)):
            if (i==j or j+i==len(n)-1):
                print(n[j],end=" ")
            else:
                print(" ",end=" ")
        print()
