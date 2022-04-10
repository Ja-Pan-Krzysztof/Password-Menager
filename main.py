from PasswordMenager import PasswordMenager
from GeneratePassword import GeneratePassword

generated_password = ''


def main():

    password = {
        'defecault': 'XYZ'
    }

    pm = PasswordMenager()

    print('''What do you want to do?
        [1] \t Create a new key
        [3] \t Create new password file
        [5] \t Add a new password to existing password file

        [2] \t Load an existing key
        [4] \t Load existing password file
        [6] \t Open exidting password file
        [7] \t Get a password
        
        [q] \t Quit
    ''')

    done = False

    while not done:
        choice = str(input('Enter your choice : '))
        match choice:
            case '1':
                path = input('Enter path : ')
                pm.create_key(path)

            case '2':
                path = input('Enter path : ')
                pm.load_key(path)

            case '3':
                path = input('Enter path : ')
                pm.create_password_file(path, password)

            case '4':
                path = input('Enter path : ')
                pm.load_password_file(path)

            case '5':
                site = input('Enter site : ')
                password = input('Enter the password ( Enter `g_password` to use it ) : ')
                if password == 'g_password':
                    a = input('Enter lenght of password : ')
                    try:
                        a = int(a)
                        p = GeneratePassword(a)

                        pm.add_password(site, p.generate_pass())

                    except ValueError:
                        print('Invalid lenght')
                        continue

                else:
                    pm.add_password(site, password)

            case '6':
                path = input('Enter path : ')
                pm.open_password_file(path)

            case '7':
                site = input('What site do you want : ')
                print(f'Passsword for {site} is {pm.get_password(site)}')

            case 'q':
                done = True
                print('Bye 🐍')

            case _:
                print('Invalid choice !')


if __name__ == '__main__':
    main()
