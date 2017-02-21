def harshard(a):
    digits = list(str(a))
    digits = map(int,digits)
    digit_sum = 0
    for i in digits:
        digit_sum += int(i)
    digit_sum = a/digit_sum
    if digit_sum == round(digit_sum):
        return True
    else:
        return False
Harshad_Num = [] 
for a in range (1,1001):
    if harshard(a) == True:
        Harshad_Num.append(a)
print "Harshad Numbers are:\n", (Harshad_Num)
def ginomeno(a):
    digits = list(str(a))
    digits = map(int,digits)
    digit_gin = 1
    for i in digits:
        digit_gin *= int(i)
    if digit_gin != 0:
        digit_gin= a/digit_gin
        if digit_gin == round(digit_gin):
            return True
        else:
            return False
       
G_num=[]
for i in range (1,1001):
    if ginomeno(i) == True:
        G_num.append(i)
print "Number divided by the product of their digits are:\n",(G_num)



