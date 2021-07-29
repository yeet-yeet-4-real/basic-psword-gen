import time
import random
import string
import re


class Password:
    def __init__(self):
        self.password = ''
        self.mid_len = 9
        self.chars = string.ascii_letters + string.digits + string.punctuation

    def is_strong(self, password) -> bool:
        return len(password) >= self.mid_len and bool(re.match(r'(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*]).{7,20}', password)) or (len(password) >= self.mid_len and bool(re.match(r'(?=.*\d)(?=.*[a-z])(?=.*[!@#$%^&*]).{9,20}', password)))

    # Unnecessary
    def is_weak(self, password) -> bool:
        if not self.is_strong(password):
            return not self.is_strong(password)
        return False

    def save_to_file(self, file):
        with open(file, 'a') as password_file:
            if self.is_strong(self.password):
                password_file.write(self.password + '\n')
                print("Password saved")
            else:
                print('Password is weak, therefore has not been saved')
                return -1

    def get_passwords(self, file) -> None:
        with open(file, 'r') as f:
            content = f.readlines()

        for password in content:
            if password != content[-1]:
                print(password)
            else:
                print('-------------')
                print('Latest saved password:', content[-1])

        

    def main(self) -> None:
        for _ in range(0, random.randrange(5, 20)):
            gen_password = random.choice(self.chars)
            self.password += gen_password
        print("----------------------\nPassword: {}\nStrong: {}\nWeak: {}\n----------------------".format( self.password, self.is_strong(self.password), self.is_weak(self.password)))

file = 'passwords.txt'
password = Password()
password.main()
password.save_to_file(file)
print('----------------------')

user_res = False
while not user_res:
    user_input = input('Would you like to see all saved passwords??(Y/N): ')
    if user_input.lower() == 'y':
        user_res = True
        with open(file, 'r') as f:
            content = f.read()
        
        if len(content) != 0:
            print('')
            password.get_passwords(file)
        else:
            print('The file is empty...')
    elif user_input.lower() == 'n':
        user_res = True
        print('Goodbye...')
    else:
        print('I\'m sorry, I do not understand....')
