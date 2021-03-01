import numpy as np

def sockMerchant(arr):
  
    values,counts = np.unique(arr, return_counts=True)
    
    for i in range(0,len(counts)):
        counts[i]= int(counts[i]/2)  
        
    a=sum(counts)
    return(a)

arr=[]
n=int(input("Enter the total number of sock:\t"))
print("\nEnter the available socks colours as integer\n")

for i in range(0,n):
    temp=int(input("Enter the value:"))
    arr.append(temp)
    
pairs=sockMerchant(arr)

print("\nThe number of pairs are:",pairs)
