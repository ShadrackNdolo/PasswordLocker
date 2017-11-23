import unittest
 import pyperclip
  from user_credentials import User
  
 -class TestUserCredentials(unittest.TestCase):
 +class TestUser(unittest.TestCase):
  	'''
  	Test class that defines test cases for the contact class behaviours.
  
 @@ -23,5 +23,12 @@ def test__init__(self):
  		self.assertEqual(self.new_user.last_name,'N\'dol\'o')
  		self.assertEqual(self.new_user.password,'pswd100')
  
 +	def test_save_user(self):
 +		'''
 +		Test to check if the new users info is saved into the users list
 +		'''
 +		self.new_user.save_user()
 +		self.assertEqual(len(User.users_list),1)
 +
  if __name__ == '__main__':
  	unittest.main(verbosity=2) 