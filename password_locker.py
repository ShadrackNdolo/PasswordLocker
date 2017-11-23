#! /usr/bin/env python3
  import pyperclip
  from user_credentials import User, Credential

    def create_user(fname,lname,password):
	'''
 	Function to create a new user account
	'''
	new_user = User(fname,lname,password)
	return new_user

    def save_user(user):
	'''
	Function to save a new user account
	'''
	User.save_user(user)

def generate_password():
	'''
	Function to generate a password automatically
	'''
	User.generate_password()

    def create_credential(site_name,user_name,password):
	'''
	Function to create a new credential
	'''
	new_credential=Credential(site_name,user_name,password)
	return new_credential

    def save_credential(credential):
	'''
	Function to save a newly created credential
	'''
	Credential.save_credentials(credential)


def verify_user(first_name,password):
	'''
	Function that verifies the existance of the user before creating credentials
	'''
	checking_user = Credential.check_user(first_name,password)
 	return checking_user

def main():
	print('Hello! Welcome to password locker.')
	while True:
		print('Use these codes to navigate: ca-Create an Account, li-Log In, ex-Exit')
		print("-"*60)
		short_code = input('Enter a choice: ').lower().strip()
		if short_code == 'ex':
			print('Goodbye')
			break

		elif short_code == 'ca':
			print('To create a new account')
			print("-"*60)
            print('To create a new account')            
            print('Enter your account details:')
			first_name = input('Enter your first name - ').strip()
			password = input('Enter your password - ').strip()
			save_user(create_user(first_name,last_name,password))
			print("-"*60)
			print(f'New Account Created for: {first_name} {last_name} using password: {password}')
			print("-"*60)


			# print('Use these codes to choose an option for your password: ep - to enter an existing password, np - to generate a new password automatically')
			# print("*"*60)
			# psw_choice = input('Enter an option: ').lower().strip()
			# if psw_choice == 'ep':
			# 	password = input('Enter your password: ')

elif short_code == 'cc':
						print('Enter your credential details:')
						site_name = input('Enter the site\'s name- ').strip()
						user_name = input('Enter your username - ').strip()
						while True:
							print(' ')
							print('Please choose an option for entering a password: ep-enter existing password, gp-generate a password, ex-exit')
							psw_choice = input('Enter an option: ').lower().strip()
							if psw_choice == 'ep':
								password = input('Enter your password: ').strip()
								break
							elif psw_choice == 'gp':
								password = generate_password()
								break
							elif psw_choice == 'ex':
								break
							else:
								print('Oops! Wrong option entered.')

 
 
 if __name__ == '__main__':
 	main()
 