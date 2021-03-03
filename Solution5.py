from datetime import date

def server_cost(d1,m1,y1,d2,m2,y2):
    cost=0
    mon1,mon2,mon3=[1,3,5,7,8,10,12],[4,6,9,11],[2]
    date1=date(y1,m1,d1)
    date2=date(y2,m2,d2)
    dif_day=(date2-date1).days
    dif_month=(y2 - y1) * 12 + ( m2- m1)

    if date1==date2:
        cost=20
    elif((m1==m2)and((m1 in mon1 and dif_day<32)or(m1 in mon2 and dif_day<31)or(m1 in mon3 and dif_day<30))):
        cost=30*dif_day
    elif(dif_day<365):
        cost=1000*dif_month
    else:
        cost=20000
    return(cost)
        
        
print("Enter the  date of server creation")

d1=int(input("enter the day:"))
m1=int(input("enter the month:"))
y1=int(input("enter the year:"))

print("\nEnter the  date of server deletion")

d2=int(input("enter the day:"))
m2=int(input("enter the month:"))
y2=int(input("enter the year:"))
output=server_cost(d1,m1,y1,d2,m2,y2)
print("cost is:",output)
