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
 		self.new_credential = Credential('Soundcloud','Shaw','pswd100')


	def test__init__(self):
		'''
		Test to if check the initialization/creation of credential instances is properly done
		'''		
        self.assertEqual(self.new_credential.site_name,'Soundcloud')
		self.assertEqual(self.new_credential.account_name,'Shaw')
		self.assertEqual(self.new_credential.password,'pswd100')

	def test_save_credentials(self):
		'''
		Test to check if the new credential info is saved into the credentials list
		'''
		self.new_credential.save_credentials()
		self.twitter = Credential('Soundcloud','Shaw','pswd100')
        self.twitter.save_credentials()
        self.assertEqual(len(Credential.credentials_list),2)

  if __name__ == '__main__':
  	unittest.main(verbosity=2) 