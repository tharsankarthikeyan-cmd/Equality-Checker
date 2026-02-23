

LOCK = 1710
def check_lock(no):
    if no == LOCK:
        print('Lock Code Correct !!')
    else:
        print('Lock Code Incorrect ??')
no = int(input('Enter Lock Code: '))
check_lock(no)

