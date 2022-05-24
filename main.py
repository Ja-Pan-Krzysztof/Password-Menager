from PasswordMenager import PasswordMenager
from GeneratePassword import GeneratePassword
from Gui.gui import AppGui

generated_password = ''


def main():

    password = {
        'defecault': 'XYZ'
    }

    pm = PasswordMenager()

    print('''What do you want to do?
        [1] \t Create a new key
        [2] \t Create new password file
        [3] \t Add a new password to existing password file
        [4] \t Get a password
        
        [q] \t Quit
    ''')

    done = False

    while not done:
        choice = str(input('\nEnter your choice : '))
        match choice:
            case '1':
                path = input('Enter path : ')
                pm.create_key(path)

            case '2':
                path = input('Enter path : ')
                pm.create_password_file(path)

            case '3':
                site = input('Enter site : ')
                password = input('Enter the password ( Enter `g_password` to use it ) : ')
                if password == 'g_password':
                    a = input('Enter lenght of password : ')
                    try:
                        a = int(a)
                        p = GeneratePassword(a)

                        pm.add_password(site, p.generate_pass())

                    except ValueError:
                        print('Invalid lenght!')
                        continue

                else:
                    pm.add_password(site, password)

            case '4':
                site = input('What site do you want : ')
                print(f'\nPasssword for \033[35m{site}\033[0m is \033[35m{pm.get_password(site)}\033[0m')

            case 'q':
                done = True
                print('Bye 🐍')

            case _:
                print('Invalid choice !')


if __name__ == '__main__':
    gui = AppGui()
    gui.mainloop()
