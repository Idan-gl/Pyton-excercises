shalom = {'avi' : 4, 'is' : 3, 'best' : 7, 'moshe' : 3, 'dudi' : 4}
shalom1 = {'avi' : 4, 'is' : 3, 'good' : 7, 'moshe' : 3, 'tzipi' : 4}
for i in shalom:
    a={}
    if i in shalom1:
        b=shalom[i]
        a[i]=b
    print(a)


shalom = {'avi' : 4, 'is' : 3, 'best' : 7, 'moshe' : 3, 'dudi' : 4}
shalom1 = {'avi' : 4, 'is' : 3, 'good' : 7, 'moshe' : 3, 'tzipi' : 4}
for i in shalom:
    a={}
    if i not in shalom1:
        b=shalom[i]
        a[i]=b
    print(a)
