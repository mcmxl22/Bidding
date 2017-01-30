#By Micah M. 2017            

#Create a database of all employees with their seniority numbers and current bid line numbers.
#def Create_DataBase():
    #conn = sqlite3.connect('bid.db') 
    #cursor = conn.cursor()
    #sql = '''create table bid (
        #Name text,
        #Seniority int,
        #Bidline int)'''
    #cursor.execute(sql)
    #cursor.close()

#Create a database of all existing bid lines.

#Create an interface to allow employees to bid on the bid lines starting with the highest seniority.
def Activity_Choices():
    Actions = ('1 New Bid', '2 View available bid lines', '3 View current bid assignments', '4 Edit bid lines',  '5 Edit Employees\n')
    for i in Actions:
        print ('%s' % i)
        
    Ask = raw_input('Choose an option. > ')
    #New bid
    if Ask == '1':
        #Ask if a new bid is being started.
        print ('Do you want to start a new bid?') 
        choices = {'y', 'n'}
        for i in choices:
            print ('%s' % i)
        Ask = raw_input('> ')
        #If yes, proceed.
        if Ask == 'y':
            
        #Have the employee enter their name and seniority number.

        #Check employee is next in line by seniority number.
        
        #List available bid lines and employee's current bid line.
        
        #Have employee enter new bid line choice.
    
        #If chosen bid line is available assign it to the employee and make it unavailable to others.

        #If chosen bidline is not available have employee choose another one.

            print ('Under development')
            Activity_Choices()

        #If no, return to activity list.
        elif Ask == 'n':
            Activity_Choices()
        else:
            print('Invalid entry')
            print(choices)
            
    #View available bid lines.
    if Ask == '2':
        print('Under development')
        Activity_Choices()
        #Display database of all existing bid lines.
    
    #View current bid assignments.
    if Ask == '3':
        print('Under development')
        Activity_Choices()
    #List choices.
        Actions = ('By employee', 'By bid line')
    
    #Edit bid lines.
    if Ask == '4':
        #List choices
        Actions = ('Change existing bid lines', 'Add new bid lines', 'Delete bid lines')
        #for i in Actions:
            #print ('%s' % i)
        print('Under development')
        Activity_Choices()

    #Edit Employees.
    if Ask == '5':
        #List choices.
        Edit_Choices = ('Change existing employee', 'Add new employee', 'Delete employee')
        #for i in Edit_Choices:
            #print ('%s' % i)
        print('Under development')
        Activity_Choices()
        
Activity_Choices()
