
# creatinga lists of users, their PINs and  bank amount
users = ['user', 'user2', 'user3']
pins = ['1234', '2222', '3333']
amounts = [1000, 2000, 3000]
count = 0
# while loop checks existance of the enterd username
while True:
    user = input('\nENTER USER NAME: ')
    user = user.lower()
    if user in users:
        if user == users[0]:
            n = 0
        elif user == users[1]:
            n = 1
        else:
            n = 2
        break
    else:
        print('-'*20)
        print('INVALID USERNAME')
        print('-'*20)

# comparing pin
while count < 3:
    print('*'*20)
    pin = input('PLEASE ENTER PIN: ')
    print('*'*20)
    if pin.isdigit():
        if user == 'user1':
            if pin == pins[0]:
                break
            else:
                count += 1
                print('-'*20)
                print('INVALID PIN')
                print('-'*20)
                print()

        if user == 'user2':
            if pin == pins[1]:
                break
            else:
                count += 1
                print('-'*20)
                print('INVALID PIN')
                print('-'*20)
                print()

        if user == 'user3':
            if pin == pins[2]:
                break
            else:
                count += 1
                print('-'*20)
                print('INVALID PIN')
                print('-'*20)
                print()
    else:
        print('-'*20)
        print('*'*20)
        print('PIN CONSISTS OF 4 DIGITS')
        print('*'*20)
        print('-'*20)
        count += 1
# if you enter 3 times wrong password it gets locked
if count == 3:
    print('-----------------------------------')
    print('3 UNSUCCESFUL PIN ATTEMPTS, EXITING')
    print('!!YOUR CARD HAS BEEN LOCKED!!')
    print('-----------------------------------')
    exit()

print('-------------------------')
print('*************************')
print('LOGIN SUCCESFUL, CONTINUE')
print('*************************')
print('-------------------------')
print()
print('--------------------------')
print('**************************')	
print(users[n].upper(), 'welcome to ATM')
print('**************************')
print('----------ATM SYSTEM-----------')
# Main menu
while True:
    #os.system('clear')
    print('-------------------------------')
    print('*******************************')
    response = input('SELECT FROM FOLLOWING OPTIONS: \nBalance__(B) \nWithdraw___(W) \nDeposite__(D)  \nChange PIN_(P)  \nQuit_______(Q) \n: ').lower()
    print('*******************************')
    print('-------------------------------')
    valid_responses = ['b', 'w', 'd', 'p', 'q']
    response = response.lower()
    if response == 'b':
        print('*********************************************')
        print(users[n].upper(), 'YOU HAVE ', amounts[n],' RUPEES ON YOUR ACCOUNT.')
        print('*********************************************')

    elif response == 'w':
        print('---------------------------------------------')
        cash_out = int(input('ENTER AMOUNT YOU WOULD LIKE TO WITHDRAW: '))
        print('---------------------------------------------')
        if cash_out <= 0:
            print('------------------------------------------------------')
            print('******************************************************')
            print('AMOUNT YOU WANT TO WITHDRAW')
            print('******************************************************')
            print('------------------------------------------------------')
        elif cash_out > amounts[n]:
            print('-----------------------------')
            print('*****************************')
            print('YOU HAVE INSUFFICIENT BALANCE')
            print('*****************************')
            print('-----------------------------')
        else:
            amounts[n] = amounts[n] - cash_out
            print('-----------------------------------')
            print('***********************************')
            print('YOUR NEW BALANCE IS: ', amounts[n])
            print('***********************************')
            print('-----------------------------------')

    elif response == 'd':
        print()
        print('---------------------------------------------')
        print('*********************************************')
        cash_in = int(input('ENTER AMOUNT YOU WANT TO DEPOSITE: '))
        print('*********************************************')
        print('---------------------------------------------')
        print()
        if cash_in <= 0:
            print('----------------------------------------------------')
            print('****************************************************')
            print('AMOUNT YOU WANT TO DEPOSITE')
            print('****************************************************')
            print('----------------------------------------------------')
        else:
            amounts[n] = amounts[n] + cash_in
            print('----------------------------------------')
            print('****************************************')
            print('YOUR NEW BALANCE IS: ', amounts[n])
            print('****************************************')
            print('----------------------------------------')
    elif response == 'p':
        print('-----------------------------')
        print('*****************************')
        new_pin =input('ENTER A NEW PIN: ')
        print('*****************************')
        print('-----------------------------')
        if new_pin.isdigit() and new_pin != pins[n] and len(new_pin) == 4:
            print('------------------')
            print('******************')
            new_ppin = input('CONFIRM NEW PIN: ')
            print('*******************')
            print('-------------------')
            if new_ppin != new_pin:
                print('------------')
                print('************')
                print('PIN MISMATCH')
                print('************')
                print('------------')
            else:
                pins[n] = new_pin
                print('NEW PIN SAVED')
        else:
            print('-------------------------------------')
            print('*************************************')
            print('   NEW PIN MUST CONSIST OF 4 DIGITS \nAND MUST BE DIFFERENT TO PREVIOUS PIN')
            print('*************************************')
            print('-------------------------------------')
    elif response == 'q':
        exit()
    else:
        print('------------------')
        print('******************')
        print('RESPONSE NOT VALID')
        print('******************')
        print('------------------')
