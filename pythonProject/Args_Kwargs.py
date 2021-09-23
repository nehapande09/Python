# Args and Kwargs
# normal argument --> *args --> **kwargs
def function_name(a,b,c,d,e):
    print(a,b,c,d)
def funargs(n,*args,**kwargs) : # We can give any name instead of args like *neha
    print(type(args))
    print(n)
    for item in args:
        print(item)
    print(kwargs)
#function_name("neha","nishant","abhi","sarrthak","sonu")
list=["neha","nishant","abhi","sarthak","sonu"]
kw={"Neha":"09/1/2002","Nishant":"08/3/1999","Abhi":"7/2/2016"}
normalarg="This is normal arguement"
funargs(normalarg, *list,**kw)
