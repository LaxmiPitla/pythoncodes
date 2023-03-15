#Time module
import time
timestamp=time.strftime('%H:%M:%S')
a=timestamp
print(a)
timestamp=time.strftime('%H')
print(timestamp)
timestamp=time.strftime('%M')
print(timestamp)
timestamp=time.strftime('%S')
print(timestamp)

th=int(time.strftime('%H'))
if (th>=0 and th<12):
    print("Good Morning,time is:",a)
elif th in range(12,18):
    print("Good Afternoon,time is:",a)
elif th in range(18,24):
    print("Good night,time is:",a)
else:
    print("Good night,sleep now:",a)