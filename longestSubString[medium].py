
b=0
for i in range(len(s)):
    a=''
    for j in range(i,len(s)):
        if s[j] in a:
            break
        a = a + s[j]
    maxlen = max(len(a),b)
    b = maxlen
print(b)