import random

#generate a random number
# bignumber = random.randint(1,999)
bignumber = 234
print(bignumber)
smallnumbers = [1,10,2,3,32,2]
print(smallnumbers)

ops = ['+','-','*','/']

def infix(a,b,op):
    # strings returns string
    string  = '(' + a + ' ' + op + ' ' + b + ')'
    return string

def evaltup(atup,btup,op):
    # function on tuples (int value, str expression)
    if btup[0] > atup[0]:
        a, b = btup, atup
    else:
        a, b = atup, btup
    if op == '/':
        if a[0]%b[0] == 0:
            resultval = a[0]//b[0]
            resultexp = infix(a[1],b[1],op)
            return  (resultval, resultexp)
        else:
            resultval = 'N/a'
            resultexp = infix(a[1],b[1],op)
            return  (resultval, resultexp)
    else:
        resultval = eval(infix(str(a[0]),str(b[0]),op))
        resultexp = infix(a[1],b[1],op)
        return  (resultval, resultexp)   

def solve(nums):
    global bignumber
    for num in nums:
        if num[0] == bignumber:
            print(num[1] + ' = ' + str(num[0]))
            input('More?')
    for num in nums:
        remainingnums = nums.copy()
        remainingnums.remove(num)
        if len(remainingnums) > 0:
            for remnum in remainingnums:
                for op in ops:
                    if num[0] >= remnum[0] and (op != '/' or (remnum[0] != 0 and num[0]%remnum[0] == 0)):
                        remainingnums2 = remainingnums.copy()
                        remainingnums2.remove(remnum)
                        newnums = [evaltup(num,remnum,op)] + remainingnums2
                        # print(newnums)
                        solve(newnums)

nums = [(a,str(a)) for a in smallnumbers]
# print(nums)

solve(nums)
