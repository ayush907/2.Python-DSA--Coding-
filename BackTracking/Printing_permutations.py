def print_perm(st, perm):
    # base case
    if len(st) == 0:
        print(perm)
        return
    
    for i in range(len(st)):
        current = st[i]
        newstr = st[:i] + st[i+1:]
        print_perm(newstr, perm + current)


st = "ABC"

print_perm(st, "")
