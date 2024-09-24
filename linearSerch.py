#By Prodceseral Approch

L=[10,29,-54,5,-3,7,78,3,-1]
target=6
for ind in range(len(L)):
    if L[ind]==target:
        print(ind)
        break
else:
    print(-1)
    
    
# By Function Approch

def leanerSearch(l,target):
    for ind in range(len(l)):
        if l[ind]==target:
            return ind
    else:
        return -1
    
L=[10,29,-54,5,-3,7,78,3,-1]
target=3
print(leanerSearch(L,target))