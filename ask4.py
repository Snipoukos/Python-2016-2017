alist=[]
i=0
while 1:
    i+=1
    a=raw_input('Enter number %d,press enter to finish: '%i)
    if a=='':
        break
    alist.append(a)
alist= map(int,alist)
if len(alist) == 1:
    print "max value,min value = ",alist[0]
elif len(alist) == 0:
    print "please input data"
elif len(alist) < 4:
    print "not enough data, you need at least 4+ non different values"
else:
    print (alist)
    def minmaxremove(alist):
        a=0
        mp=0
        mip=0
        while (a<len(alist)):
            if alist[a] == max(alist):
                mp=a
            
            if alist[a] == min(alist):
                mip=a
            
            a=a+1
        del alist[mp]
        del alist[mip]
    minmaxremove(alist)
    minmaxremove(alist)
    print (alist)
    max2=max(alist)
    min2=min(alist)
    print max2,min2,(max2-min2)


