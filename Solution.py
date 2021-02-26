import numpy as np
# creating a list to store result
result=[]
#creating a funtion which takes 2 strings as input
def almost_equal(x,y):
  #creating 2 arrays of size 26 to store the number occurance of each characters (a-z)
    ax=np.full((26),0)
    ay=np.full((26),0)
    
    #using lower() to change all the characters to lower case
    x=x.lower()
    y=y.lower()
    #checking condition 1
    if len(x)==len(y):
        status="YES"
        
        for i in x:
            w=ord(i)-ord('a') #reshaping the index to 0-25
            ax[w]=ax[w]+1     #incrementing to the array to count the occurance of characters
            
        for i in y:
            w=ord(i)-ord('a')
            ay[w]=ay[w]+1

            
        for i in range(0,26): #iterating the array
            check=ax[i]-ay[i] 
            if(check<(-3) or check>3): #checking condition 2
                status="NO"
                break;
        result.append(status)
    else:
        result.append("NO")
#function over

#creating 2 empty lists                
list1=[]
list2=[]

n=int(input("Enter the Number of elements in the array\t"))
print("\nEnter the elements of first array\n")

for i in range(1,n+1):
    temp=input("Enter string:\t")
    list1.append(temp)

print("\nEnter the elements of second array\n")
for i in range(1,n+1):
    temp=input("Enter string:\t")
    list2.append(temp)
#converting list to array    
array1=np.array(list1)
array2=np.array(list2)

for i in range(0,len(array1)):
    
    x,y=array1[i],array2[i]
    
    almost_equal(x,y) #calling function almost_equal
    
print("\n Result\t",result)     
                    
