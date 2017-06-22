n=input("Enter the number:")
a=n
b=0
r=0
while n>0:
	r=n%10
	b=b+r*r*r
	n=n/10
if b==a:
	print("armstrong number")
else:
	print("not armstrong number")
