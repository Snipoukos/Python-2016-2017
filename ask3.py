alist=[]
i=0
while 1:
    i+=1
    a=raw_input('Enter item %d,press enter to finish: '%i)
    if a=='':
        break
    alist.append(a)
print (alist)
for i in range (len(alist)-1,0,-1):
    for j in range(i):
        if alist[j] == '0' :
            temp = alist[j]
            alist[j] = alist [j+1]
            alist[j+1] = temp
print (alist)