  import pyperclip
  
    # Global Variables
 global users_list 
  class User:
  	'''
  	Class to create user credentials, accounts and save their information
  	'''
      	# Class Variables
    credentials_list =[]
	users_list =[]
  	def __init__(self,first_name,last_name,password):
  		'''
  		Method to define the properties for each user object will hold.
 @@ -13,4 +16,12 @@ def __init__(self,first_name,last_name,password):
  		# instance variables
  		self.first_name = first_name
  		self.last_name = last_name
		self.password = password

	def save_user(self):
		'''
 		Function to save a newly created user instance
		'''
		# global users_list
		User.users_list.append(self)

class Credential:
	'''
	Class to create  account credentials, generate passwords and save their information
	'''
	def __init__(self,site_name,account_name,password):
 		'''
	Method to define the properties for each user object will hold.
 		'''

		# instance variables
		self.site_name = site_name
		self.account_name = account_name
		self.password = password


	def save_credentials(self):
		'''
		Function to save a newly created user instance
		'''
        # global users_list
        Credential.credentials_list.append(self)

        return cls.credentials_list
g9i		
	@classmethod
	def find_by_site_name(cls, site_name):
		'''
 	Method that takes in a site_name and returns a credential that matches that site_name.
		'''
		for credential in cls.credentials_list:
			if credential.site_name == site_name:
				return credential

            @classmethod
 +	def copy_credential(cls,site_name):
 +		'''
 +		Class method that copies a credential's info after the credential's site name is entered
 +		'''
 +		find_credential = cls.find_by_site_name(site_name)
 +		pyperclip.copy(f'Site Name: {find_credential.site_name} - UserName: {find_credential.site_name} - Password:  {find_credential.password}')