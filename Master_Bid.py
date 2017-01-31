#By Micah M. 2017            
#Python 2.7.12


import sqlite3
import sys
import subprocess


#Create a database of all team members with their seniority numbers 
#and current bid line numbers.
def Create_DataBases():
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
    elif Create_Ask == '2':
        conn = sqlite3.connect('bid.db') 
        cursor = conn.cursor()
        sql = '''create table Bidlines (
            Bidlines int)'''
        cursor.execute(sql)
        cursor.close()

    else:
        print ('Invalid entry!')
        Create_DataBases()

#Create an interface to allow team members to bid on the bid lines starting
#with the highest seniority.
def Activity_Choices():
    Actions = ('1 New Bid', '2 View available bid lines',
    '3 View current bid assignments', '4 Edit bid lines',  
    '5 Edit team members', '6 Create Database\n')
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
            #Have the team member enter their name and seniority number.
            #Ask = raw_input('Enter your name and seniority numer. > ')

            #Check team member is next in line by seniority number.
            #if Ask...
            #file = open('Employee_Status.txt', 'r')
            #...
            #file.close()

            #List available bid lines and team member's current bid line.
            #with open('Bid_Lines.txt', 'r') as fin:
                #for file in fin.readlines():
                #print(file)
            #file.close()

            #Have team member enter new bid line choice.
            #Ask = raw_input('Enter your bid. > ')

            #If chosen bid line is available assign it to the team member and make it unavailable to others.

            #If chosen bidline is not available have team member choose another one.
            #print ('This line is taken. Choose another line.')
            #Ask

        #If no, return to activity list.
        elif Ask == 'n':
            Activity_Choices()

        else:
            print ('Invalid entry!')
            print (New_Choices)

    #View available bid lines.
    elif New_Ask == '2':
        print ('Under development\n')
        #Display all existing bid lines.
        with open('Bid_Lines.txt', 'r') as fin:
            for file in fin.readlines():
                print(file)
        Activity_Choices()

    #View current bid assignments.
    elif New_Ask == '3':
        conn = sqlite3.connect('bid.db')
        cursor = conn.cursor()
        sql = '''select * from bid'''
        results = cursor.execute(sql)
        All_TeamMembers = results.fetchall()

        for TeamMember in All_TeamMembers:
            print (TeamMember)
        cursor.close()
        Activity_Choices()

    #Edit bid lines.
    elif New_Ask == '4':
        Edit_Actions = ('1 Change existing bid lines',
        '2 Add new bid lines', '3 Delete bid lines')

        for i in Edit_Actions:
            print ('%s' % i)
        #Edit_Ask = raw_input('Choose an option. > ')
        #if Edit_Ask == '1':
            #...
        #elif Edit_Ask == '2':
            #...
        #elif Edit_Ask == '3':
            #...
        #else:
            #print ('Invalid entry!')
            #print (Edit_Actions)
        print ('Under development\n')
        Activity_Choices()

    #Edit team members.
    elif New_Ask == '5':
        Edit_Choices = ('1 Change existing team member',
        '2 Add new team member', '3 Remove team member')

        for i in Edit_Choices:
            print ('%s' % i)
        #Edit_Ask = raw_input('Choose an option. > ')
        #if Edit_Ask == '1':
            #...
        #elif Edit_Ask == '2':
            #...
        #elif Edit_Ask == '3':
            #...
        #else:
            #print ('Invalid entry!')
            #print (Edit_Actions)
        print ('Under development\n')
        Activity_Choices()

    elif New_Ask == '6':
        print ('Under development\n')	
        Create_DataBases()

    else:
        print ('Invalid entry!')
        Activity_Choices()

Activity_Choices()
