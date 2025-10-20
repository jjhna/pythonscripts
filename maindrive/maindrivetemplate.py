# Test flask
# cd D:\PythonProject\pythonscripts
# python .\flasktest.py

class Account:
    def __init__(self,name,age,username,password,addresses):
        if not isinstance(age, int):
            raise TypeError("age must be an integer")
        if not isinstance(addresses, dict):
            raise TypeError("addresses must be a dict")
        self.name = name
        self.age = age
        self.username = username
        self.password = password
        self.addresses = addresses
    
    def printAddresses(self):
        reply = "The previous Addresses are: \n"
        for key,value in self.addresses.items():
            reply += "the key: " + str(key) + " and the value is: " + str(value) + " \n"
        reply += "these address are the users previous addresses\n"
        return reply

    def speak(self):
        return "New user is: " , self.name , " the users age is: " , self.age , " the users user name and password are: " , self.username , "," , self.password , " the address keys are: " , self.addresses.keys() , " and the address values are: " , self.addresses.values()

