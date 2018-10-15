#!/usr/bin/env python3
'''By Micah M. 2018
   Bid Version 1.2
   Python 3.7'''


import sys
import subprocess


# Create lists of all bid lines, and all team members with their
# seniority numbers and current bid line numbers.

def activityChoices():
    entry = ('\nInvalid Entry!\n')
    actions = ['1 Create new bid',  '2 View current bid files',
               '3 Edit bid lines', '4 Edit team members', '5 Create Lists',
               '6 Delete a bid', '7 Exit\n']
    print(' \n'.join(actions))

    select = input('Select an option.\n> ')

    if select == '1':
        createBid = [sys.executable, 'createbid.py']
        subprocess.call(createBid)

    # View available bid files.
    elif select == '2':
        seeBid = [sys.executable, 'seeBid.py']
        subprocess.call(seeBid)

    # Edit bid lines.
    elif select == '3':

        editActions = ['1 Change existing bidlines.',
                       '2 Add new bid lines.',
                       '3 Delete bid lines.', '4 Back']

        print(' \n'.join(editActions))
        select = input('Select an option.\n> ')

        if select == '1':
            print('Under development!')
            activityChoices()

        elif select == '2':
            print('Under development!')
            activityChoices()

        elif select == '3':
            print('Under development!')
            activityChoices()

        if select == '4':
            activityChoices()

    # Edit team members.
    elif select == '4':
        editChoices = ['1 Change existing team members.',
                       '2 Add new team members.',
                       '3 Remove team members.', '4 Back']

        print(' \n'.join(editChoices))
        select = input('Select an option.\n> ')

        if select == '1':
            print('Under development!')
            activityChoices()

        elif select == '2':
            print('Under development!')
            activityChoices()

        elif select == '3':
            print('Under development!')
            activityChoices()

        elif select == '4':
            activityChoices()

        else:
            print(entry)
            activityChoices()

    elif select == '5':
        print('\nunder development!\n')
        activityChoices()

    elif select == '6':
        deleteBid = [sys.executable, 'deleteBid.py']
        subprocess.call(deleteBid)

    elif select == '7':
        raise SystemExit

    else:
        print(entry)
        activityChoices()


if __name__ == "__main__":
    activityChoices()
