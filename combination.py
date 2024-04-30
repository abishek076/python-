"""def combs(a):
    if len(a) == 0:
        return [[]]
    cs = []
    for c in combs(a[1:]):
        cs += [c, c+[a[0]]]
    return cs
k=[1,2,3,4]
x = combs(k)
m=[]
for i in range(len(x)):
    if len(x[i])==3:
        m.append(x[i])
print(m)"""
def string_combs(s):
    if len(s) == 0:
        return ['']
    cs = []
    for c in string_combs(s[1:]):
        cs += [c, s[0] + c]
    return cs

# Example usage:
input_string = "abc"
combinations = string_combs(input_string)
print(sorted(combinations))
