
def reverse(num,rev):
    while num>0:
        # r=num%10
        rev=rev*10+num%10 
        num=num//10
    return rev 

print(reverse(133,0))
        