# The class Login has an initializer that sets the username and password attributes.
class Login():
     def __init__(self, username, password=None):
          self.username = username
          self.passwors = password

# The class "User" inherits from "Login" and has attributes for username, password, first name, last
# name, and email address, with a string representation method.
class User(Login):
     def __init__(self, username, password, first_name, last_name, email_address):
          super.__init__(username)
          super.__init__(password)
          self.first_name = first_name
          self.last_name = last_name
          self.email_address = email_address

     def __str__(self):
        return f"Your name is {self.first_name} {self.last_name} and your username is {self.username} and password is {self.password} and the email address is {self.email_address}"

def  main():
     """
     The function creates a User object with specific attributes and prints it.
     """
user = User("Bostone001", "TUK001", "Ochieng", "Kevin", "bostone@gmail.com")
print(user)

if __name__ == '__main__':
    main()