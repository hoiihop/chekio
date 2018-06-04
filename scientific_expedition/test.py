a = 'Hello'
b = 'Ole Oh'
a = list(a.lower())
b = list(''.join(b.lower().split()))
for i in b:
    if i in a:
        a.remove(i)
    else:
        print(False)
print(True)

