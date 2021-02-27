import numpy as np

even_count=0
moves_count=0
list1=[]

n=int(input("Enter the no of elements in the array\t"))
print("Enter the data")

for i in range(0,n):
    temp=int(input("Enter the number:\t"))
    list1.append(temp)
    
print("\nThe input array is:",list1,"\n")
arr=np.array(list1)

for i in range(0,n):
    if(arr[i]%2==0):  #calculating no of even numbers
        even_count+=1
        
for i in range(0,even_count):
    if(arr[i]%2==1):   #calculating misplaced no of odd numbers hence calculating no of swaps needed
        moves_count+=1
        
print("minimum number of swaps needed = ",moves_count)

    

    
    
