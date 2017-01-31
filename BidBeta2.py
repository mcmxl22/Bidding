#By Micah M. 2017 
#Version 1.2 Beta            
#Python 2.7.12


import sqlite3
import sys
import os.path


#Create a list of all team members with their seniority numbers 
#and current bid line numbers.
def Create_Lists():
    Create_Choices = ('1 Create general list', '2 Create bid line list', '3 Back')
    for i in Create_Choices:
        print ('%s' % i)

    Create_Ask = raw_input('What do you want to do? > ')

    #Create create team member list
    if Create_Ask == '1':
        if os.path.exists('TeamMember_Status.txt') == True:
            file = open('TeamMember_Status.txt', 'w')
            print ('Openning file!')
            cont = raw_input('Add a team member? ')
            if cont[0].lower() == 'n':
            file.close()
            Create_Lists()

        elif os.path.exists('TeamMember_Status.txt') == False:
            print ('File TeamMember_Status.txt does not exist!')
            print ('Do you want to create the file?')
            Ask = ('y', 'n')
            for i in Ask:
                print ('%s' % i)
            Create_File = open('TeamMember_Status.txt', 'w+')
			
    #Create a list of all existing bid lines.
    elif Create_Ask == '2':
        if os.path.exists('Bid_Lines.txt') == True:
            file = open('Bid_Lines.txt', 'w')
            file
            print ('Openning file!')
            cont = raw_input('Add a bid line? ')
            if cont[0].lower() == 'n':
            file.close()
            Create_Lists()

        elif os.path.exists('Bid_Lines.txt') == False:
            print ('File Bid_Lines.txt does not exist!') 
            print ('Do you want to create the file?')
            Ask = ('y', 'n')
            for i in Ask:
                print ('%s' % i)
            Create_File = open('Bid_Lines.txt', 'w+')
			
    elif Create_Ask == '3':
        Activity_Choices()

    else:
        print ('Invalid entry!')
        Create_Lists()

#Create an interface to allow team members to bid on the bid lines starting
#with the highest seniority.
def Activity_Choices():
    Actions = ('1 New Bid', '2 View available bid lines',
    '3 View current bid assignments', '4 Edit bid lines',  
    '5 Edit team members', '6 Create Database\n', '7 Exit')
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
            #Name_Ask = raw_input('Enter your name and seniority numer. > ')

            #Check team member is next in line by seniority number.
            #if Name_Ask...:
                #file = open('TeamMember_Status.txt', 'r')
                #...
                #file.close()

            #List available bid lines and team member's current bid line.
            #with open('Bid_Lines.txt', 'r') as fin:
                #for file in fin.readlines():
                #print(file)
            #file.close()

            #Have team member enter new bid line choice.
            #Line_Ask = raw_input('Enter your bid. > ')
            #...

            #If chosen bid line is available assign it to the team member and make it unavailable to others.
            #if Line_Ask...:

            #If chosen bidline is not available have team member choose another one.
            #elif Line_Ask...:
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
        print ('Under development\n')
        Activity_Choices()

    #Edit bid lines.
    elif New_Ask == '4':
        Edit_Actions = ('1 Change existing bid line(s)',
        '2 Add new bid line(s)', '3 Delete bid line(s)', '4 Back')

        for i in Edit_Actions:
            print ('%s' % i)
        #Edit_Ask = raw_input('Choose an option. > ')
        #if Edit_Ask == '1':
            #...
        #elif Edit_Ask == '2':
            #...
        #elif Edit_Ask == '3':
            #...
        elif New_Ask == '4':
            Activity_Choices()
        else:
            print ('Invalid entry!')
            print (Edit_Actions)
        print ('Under development\n')
        Activity_Choices()

    #Edit team members.
    elif New_Ask == '5':
        Edit_Choices = ('1 Change existing team member(s)',
        '2 Add new team member(s)', '3 Remove team member(s)', '4 Back')

        for i in Edit_Choices:
            print ('%s' % i)
        #Edit_Ask = raw_input('Choose an option. > ')
        #if Edit_Ask == '1':
            #...
        #elif Edit_Ask == '2':
            #...
        #elif Edit_Ask == '3':
            #...
        elif New_Ask == '4':
            Activity_Choices()

        else:
            print ('Invalid entry!')
            print (Edit_Actions)
        print ('Under development\n')
        Activity_Choices()

    elif New_Ask == '6':
        print ('Under development\n')	
        Create_Lists()
        #...
    
    elif New_Ask == '7':
        quit()

    else:
        print ('Invalid entry!')
        Activity_Choices()

Activity_Choices()
