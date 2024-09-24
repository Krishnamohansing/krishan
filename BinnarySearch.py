# L=[1,32,356,23,46,8,5,3,45]
# target=8
# l=sorted(L)
# print(l)
# l_ind=0
# h_ind=len(l)-1

# while l_ind<=h_ind and l[l_ind]<=target<=l[h_ind]:
#     m_ind=(l_ind+h_ind)//2
    
#     if l[m_ind]>target:
#         h_ind=m_ind-1
        
#     elif l[m_ind]<target:
#         l_ind=m_ind+1
        
#     elif l[m_ind]==target:
#         print(m_ind)
#         break
# else:
#     print(-1)
    
    
#By funtional Approch

def BinnaryS(l,target):
    print(l)
    l_ind=0
    h_ind=len(l)-1
    while l_ind<=h_ind and l[l_ind]<=target<=l[h_ind]:
        
        mid=(l_ind+h_ind)//2
        
        if l[mid] > target:
            h_ind=mid-1
        
        elif l[mid] < target:
            l_ind=mid+1
            
        elif l[mid]==target:
            return mid
        
    else:
        return -1
    
L=[1,32,356,23,46,8,5,3,45]
target=46
L=sorted(L)

print(BinnaryS(L,target))
    

            
    
    