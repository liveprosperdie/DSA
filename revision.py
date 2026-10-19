def sort(d):
    s=sorted(d.items(),key=lambda s:s[1], reverse=True)
    return [x[0][0] for x in s]
print(sort({"A": 70, "B": 95, "C": 82}))
