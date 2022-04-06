min=int(input('enter the minimum no. '))
max=int(input('enter the maximum no. '))
limit=int(input('enter the limit of disabled set '))
sett=[]
for i in range(0,limit):
    sett_num=int(input('enter no. to be added in disabled set within the min and max no.'))
    sett.append(sett_num)
print(sett)
check=int(input('enter a no. to validate'))
def func(i,x,chk,stt):
    if chk not in range(i + 1, x):
        print('Invalid Input')
    elif chk not in stt:
        print(chk)
    elif chk in stt:
        chk+=1
        print("check",chk)
        func(min,max,chk,sett)
func(min,max,check,sett)
