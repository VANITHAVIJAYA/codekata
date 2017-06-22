lowerlimit=int(input("Enter the lower limit for the range:"))
 upperlimit=int(input("Enter the upper limit for the range:"))
 for i in range(lowerlimit,upperlimit+1):
  if(i%2==0):
    print(i)
