n = 2
for i in range(0,n):
    
    s = "abcd"
    tem_even = []
    tem_odd = []
    for i in range(len(s)):
        if i%2==0:
            tem_even.append(s[i])
        else:
            tem_odd.append(s[i])
    even = ""
    odd = ""
    print(even.join(tem_even)+ " "+odd.join(tem_odd))