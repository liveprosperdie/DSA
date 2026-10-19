def largest2(a):
    l=float("-inf")
    sl=float("-inf")
    for i in a:
        if i>l:
            sl=l
            l=i
        elif sl<i<l:
            sl=i
    if sl==float("-inf"):
        sl=None
    return sl
