#By Micah M. 2017            


import sqlite3
import sys
import subprocess


#Create a database of all employees with their seniority numbers and current bid line numbers.
def Create_DataBase():
    Create_Choices = ('1 Create bid database.', '2 Create bid line database.')
    for i in Create_Choices:
        print ('%s' % i)
		
    Create_Ask = raw_input('What do you want to do? > ')
    
	if Create_Ask == '1':
        conn = sqlite3.connect('bid.db') 
        cursor = conn.cursor()
        sql = '''create table bid (
            Name text,
            Seniority int,
            Bidline int)'''
        cursor.execute(sql)
        cursor.close()
		
    #Create a database of all existing bid lines.
    elif Create_Ask == '2'
        conn = sqlite3.connect('bid.db') 
        cursor = conn.cursor()
        sql = '''create table bid (
            Bidline int)'''
        cursor.execute(sql)
        cursor.close()
	
    else:
        print('Invalid entry!')
        Create_DataBase()

#Create an interface to allow employees to bid on the bid lines starting with the highest seniority.
def Activity_Choices():
    Actions = ('1 New Bid', '2 View available bid lines', '3 View current bid assignments', 
    '4 Edit bid lines',  '5 Edit Employees\n')
    for i in Actions:
        print ('%s' % i)
        
    #New bid   
    New_Ask = raw_input('Choose an option. > ')
    if New_Ask == '1':
        print ('Do you want to start a new bid?') 
        New_Choices = {'y', 'n'}
        for i in New_Choices:
            print ('%s' % i)
			
        Ask = raw_input('> ')
            
        #If yes, proceed.
        if Ask == 'y':
            print ('Under development\n')
            Activity_Choices()
        
        #If no, return to activity list.
        elif Ask == 'n':
            Activity_Choices()
            
        else:
            print('Invalid entry!')
            print(choices)
            
        #Have the employee enter their name and seniority number.
        #Ask = raw_input('Enter your name and seniority numer. > ')

        #Check employee is next in line by seniority number.
        
        #List available bid lines and employee's current bid line.
        
        #Have employee enter new bid line choice.
        #Ask = raw_input('Enter your bid. > ')
    
        #If chosen bid line is available assign it to the employee and make it unavailable to others.

        #If chosen bidline is not available have employee choose another one.

    #View available bid lines.
    if New_Ask == '2':
        print('Under development\n')
        Activity_Choices()
        #Display database of all existing bid lines.

    #View current bid assignments.
    if New_Ask == '3':
        View_Actions = ('1 By employee', '2 By bid line')
        for i in View_Actions:
            print ('%s' % i)
        print('Under development\n')
        Activity_Choices()

    #Edit bid lines.
    if New_Ask == '4':
        Edit_Actions = ('1 Change existing bid lines', '2 Add new bid lines', '3 Delete bid lines')
        for i in Edit_Actions:
            print ('%s' % i)
        print('Under development\n')
        Activity_Choices()

    #Edit Employees.
    if New_Ask == '5':
        Edit_Choices = ('1 Change existing employee', '2 Add new employee', '3 Delete employee')
        for i in Edit_Choices:
            print ('%s' % i)
        print('Under development\n')
        Activity_Choices()

    else:
        print('Invalid entry!')
        Activity_Choices()

Activity_Choices()


    #View available bid lines.
    if New_Ask == '2':
        print('Under development\n')
        Activity_Choices()
        #Display database of all existing bid lines.
    
    #View current bid assignments.
    if New_Ask == '3':
        View_Actions = ('1 By employee', '2 By bid line')
        for i in View_Actions:
            print ('%s' % i)
        print('Under development\n')
        Activity_Choices()
    
    #Edit bid lines.
    if New_Ask == '4':
        Edit_Actions = ('1 Change existing bid lines', '2 Add new bid lines', '3 Delete bid lines')
        for i in Edit_Actions:
            print ('%s' % i)
        print('Under development\n')
        Activity_Choices()

    #Edit Employees.
    if New_Ask == '5':
        Edit_Choices = ('1 Change existing employee', '2 Add new employee', '3 Delete employee')
        for i in Edit_Choices:
            print ('%s' % i)
        print('Under development\n')
        Activity_Choices()
    
    else:
        print('Invalid entry!')
        Activity_Choices()
        
Activity_Choices()

        
        #List available bid lines and employee's current bid line.
        
        #Have employee enter new bid line choice.
        #Ask = raw_input('Enter your bid. > ')
    
        #If chosen bid line is available assign it to the employee and make it unavailable to others.

        #If chosen bidline is not available have employee choose another one.

    #View available bid lines.
    if New_Ask == '2':
        print('Under development\n')
        Activity_Choices()
        #Display database of all existing bid lines.
    
    #View current bid assignments.
    if New_Ask == '3':
        View_Actions = ('1 By employee', '2 By bid line')
        for i in View_Actions:
            print ('%s' % i)
        print('Under development\n')
        Activity_Choices()
    
    #Edit bid lines.
    if New_Ask == '4':
        Edit_Actions = ('1 Change existing bid lines', '2 Add new bid lines', '3 Delete bid lines')
        for i in Edit_Actions:
            print ('%s' % i)
        print('Under development\n')
        Activity_Choices()

    #Edit Employees.
    if New_Ask == '5':
        Edit_Choices = ('1 Change existing employee', '2 Add new employee', '3 Delete employee')
        for i in Edit_Choices:
            print ('%s' % i)
        print('Under development\n')
        Activity_Choices()
    
    else:
        print('Invalid entry!')
        Activity_Choices()
        
Activity_Choices()
