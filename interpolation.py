L=[1,32,356,23,46,8,5,3,45]

target=5
l_ind=0
h_ind=len(L)-1

while l_ind<=h_ind and L[l_ind]<=target<=L[h_ind]:
    ind=int((l_ind+((h_ind-l_ind)/L[h_ind]-L[l_ind]))*(target-L[l_ind]))
    
    if L[ind]>target:
        h_ind=ind-1
    elif L[ind]<target:
        l_ind=ind+1
        
    elif L[ind]==target:
        print(ind)
        break
else:
    print(-1)