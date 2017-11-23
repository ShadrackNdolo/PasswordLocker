import unittest
  import pyperclip
 -#from user_credentials import User, Credentials 
 +from user_credentials import User
  
  class TestUserCredentials(unittest.TestCase):
  	'''
 @@ -13,7 +13,15 @@ def setUp(self):
  		'''
  		Function to create a user account before each test
  		'''
 -		self.new_user = User('Mary','pswd100')
 +		self.new_user = User('Mary','Ng\'ang\'a','pswd100')
 +
 +	def test__init__(self):
 +		'''
 +		Test to if check the initialization/creation of instances is properly done
 +		'''
 +		self.assertEqual(self.new_user.first_name,'Mary')
 +		self.assertEqual(self.new_user.last_name,'Ng\'ang\'a')
 +		self.assertEqual(self.new_user.password,'pswd100')
  
  if __name__ == '__main__':
 -	unittest.main() 
 +	unittest.main(verbosity=2)