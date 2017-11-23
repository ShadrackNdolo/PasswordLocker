import unittest
 import pyperclip
  from user_credentials import User, Credential
  
class TestUser(unittest.TestCase):
  	'''
  	Test class that defines test cases for the user class behaviours.
  
 @@ -23,5 +23,12 @@ def test__init__(self):
  		self.assertEqual(self.new_user.last_name,'N\'dol\'o')
  		self.assertEqual(self.new_user.password,'pswd100')
  
	def test_save_user(self):
		'''
		Test to check if the new users info is saved into the users list
		'''
		self.new_user.save_user()
		self.assertEqual(len(User.users_list),1)

class TestCredentials(unittest.TestCase):
	'''
	Test class that defines test cases for the credentials class behaviours.

	Args:
	    unittest.TestCase: helps in creating test cases
	'''
 	def setUp(self):
		'''
		Function to create an account's credentials before each test
		'''
 		self.new_account = Credential('Soundcloud','Shaw','pswd100')


	def test__init__(self):
		'''
		Test to if check the initialization/creation of credential instances is properly done
		'''		self.assertEqual(self.new_account.site_name,'Soundcloud')
		self.assertEqual(self.new_account.account_name,'Shaw')
		self.assertEqual(self.new_account.password,'pswd100')

	def test_save_credential(self):
		'''
		Test to check if the new users info is saved into the users list
		'''
		self.new_user.save_account()
		self.twitter = Credential('Soundcloud','Shaw','pswd100')
        		self.twitter.save_account()
                		self.assertEqual(len(Credential.credentials_list),2)

  if __name__ == '__main__':
  	unittest.main(verbosity=2) 