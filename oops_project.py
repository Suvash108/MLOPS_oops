class chatbook:
    def __init__(self) :
        self.username=''
        self.password=''
        self.loggedin=False
        self.menu()
    
    def menu(self):
        user_input=input("""welcome to chatbook! how would l ie to proceed ?
                         1. Press 1 to signup
                         2. Press 2 to Signin  
                         3. Press 3 to write a post
                         4. press 4 to upload message a friend
                         5. press any other key to exit""")
        if user_input == "1":
            pass
        elif user_input == "2":
            pass

        elif user_input == "3":
            pass

        elif user_input == "4":
            pass

        else:
            exit()


obj =chatbook()      