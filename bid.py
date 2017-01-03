import subprocess
import sys


def questions():

    create = [sys.executable, 'createbid.py']
    view = [sys.executable, 'seebid.py']
    answer = ['yes', 'no']

    print('Create bid? ')

    for i in answer:
        print ('%s' % i)

    choice1 = raw_input('> ')

    if choice1 == answer[0]:
        subprocess.call(create)

    if choice1 == answer[1]:
        print('View bid?')
        choice2 = raw_input('> ')

    if choice2 == answer[0]:
        subprocess.call(view)

    elif choice2 == answer[1]:
        print ('Done!')
        quit()

if __name__ == "__main__":
    questions()
