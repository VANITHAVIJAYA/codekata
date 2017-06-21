 n=input("Enter the number")
  l=len(n)
  count=0
  for i in range(0,l):
    if n.isdigit():
        count+=1
  print(count)
