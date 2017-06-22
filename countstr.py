n=input("Enter the String:")
    a=0
    d=0
    al=0
    l=len(n)
    for i in range(0,l):
        if n.isalpha():
            a=a+1
        if n.isdigit():
            d=d+1
        if n.isalnum():
            al=al+1
    print(a)
    print(d)
    print(al)
