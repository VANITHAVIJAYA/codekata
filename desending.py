 print 'Enter numers,use q to stop'
    l = []
    while True:
     user_input = raw_input('Enter numers: ')
     if user_input == 'q':
        break
     else:
        l.append(user_input)
        num_list = (float(i) for i in l)
#Ascending order
    #print sorted(num_list)
#Descending order
    print sorted(num_list, reverse=True)
