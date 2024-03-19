#Basic calcy
print('\t\t\tCALCULATOR')
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b==0:
        return 'Error! divideded by 0'
    else:
        return a/b
def mod(a,b):
    if b==0:
        return 'Zero dividedend error'
    else:
        return a%b
def calcy():
    while True:
        n1=float(input('Enter the 1st number: '))
        n2=float(input('Enter the 2nd number: '))
        o=input("Choose the opeation you want to perform :\n'+'/n'-'/n'*'/n'/'")
        if o=='+':
            a=add(n1,n2)
            print("The sum of ",n1,"and",n2,"is : ",a)
        if o=='-':
            s=sub(n1,n2)
            print("The subtraction of ",n1,"and",n2,"is : ",s)
        if o=='*':
            m=mul(n1,n2)
            print("The multiplication of ",n1,"and",n2,"is : ",m)
        if o=='/':
            d=div(n1,n2)
            print("The division of ",n1,"and",n2,"is : ",d)
        if o=='%':
            n1=int(n1);n2=int(n2)
            mo=mod(n1,n2)
            print('The modulus division of ',n1,'and',n2,'is :',mo)
        d=input('You want to do any other calculation or you want to stop/n"yes" or "no"')
        if d=='yes':
            continue
        else:
            print("Done 'have a good day'")
            break
calcy()