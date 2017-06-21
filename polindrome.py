a=input("enter the no:")
x=str(a)
l=len(x)
i=0
flag=0
for i in range(0,l):
  if(x[i]==x[l-i-1]):
	  flag=flag+1
  if(flag==l):
	  print("the given no is palindrome")
  else:
	  print("the given no is not a palindrome")

