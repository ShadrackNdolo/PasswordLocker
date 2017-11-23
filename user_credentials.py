  import pyperclip
  
 +# Global Variables
 +global users_list 
  class User:
  	'''
  	Class to create user accounts and save their information
  	'''
 +	# Class Variables
 +	users_list =[]
  	def __init__(self,first_name,last_name,password):
  		'''
  		Method to define the properties for each user object will hold.
 @@ -13,4 +16,12 @@ def __init__(self,first_name,last_name,password):
  		# instance variables
  		self.first_name = first_name
  		self.last_name = last_name
 +		self.password = password
 +
 +	def save_user(self):
 +		'''
 +		Function to save a newly created user instance
 +		'''
 +		# global users_list
 +		User.users_list.append(self)

 +class Credential:
 +	'''
 +	Class to create  account credentials, generate passwords and save their information
 +	'''
 +	def __init__(self,site_name,account_name,password):
 +		'''
 +		Method to define the properties for each user object will hold.
 +		'''
 +
 +		# instance variables
 +		self.site_name = site_name
 +		self.account_name = account_name
 +		self.password = password