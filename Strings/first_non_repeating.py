
# program to find the first non repeating character in the string and repeat its index 
def first_non_repeating(st):
    # string characters characters aur unke corresponding count ko dictionary mai store karenge
    d = dict()
    for i in st:
        if i in d:
            d[i] = d[i] + 1
        else:
            d[i] = 1

    for i in d:
        if d[i] == 1:
            return i
         
    return -1
        
    
        

st = "aabxxzcbflfz"
print(first_non_repeating(st))
        

