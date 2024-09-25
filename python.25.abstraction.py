print("abstraction")

from abc import ABC, abstractmethod

class BankApp(ABC):

    def database(self):
        print("connected to database")

    @abstractmethod
    def security(self):
        pass

    @abstractmethod
    def id(self):
        print("id is")

class MobileApp(BankApp):

    def mobile_login(self):
        print("login into mobile")

## mob = MobileApp() #error instantiate abstract class MobileApp

    def security(self):
        print("mobile security")

    def id(self):
        print("id is")

print()
mob = MobileApp()

mob.security()
mob.mobile_login()
mob.database()
mob.id()

##mob1 = BankApp()  #Can't instantiate abstract class BankApp without an implementation for abstract methods

