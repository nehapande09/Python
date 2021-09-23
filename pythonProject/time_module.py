# Time module in python :
import time
initial=time.time()
print(initial)
print("k:")
k=1
while(k<=20) :
    print(k)
    time.sleep(2) #--> Sleep while running for x seconds
    k=k+1
print("While loop time",time.time()-initial)
initial2=time.time()
for i in range(10):
    print("hii,hello")
print("for loop time",time.time()-initial2)
local_time=time.asctime(time.localtime((time.time())))
print(local_time)