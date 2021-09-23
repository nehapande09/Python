li=["Apple","Banana","Pineapple","orange","Pomegrnet"]
# i=1
# for item in li:
#     if i%2 !=0:
#       print(item)
#     i=i+1
for index,item in enumerate(li):
    if index %2== 0:
        print(f" Please bring  {item}")
