#Decoder And Encoder
     

def make_login():
     print( "Lets make an account")
     print("First pick a username and password:")
     user = input("Enter desired username: ")
     password = input("Enter desired password: ")
     
     login_val = [user, password]

     return login_val





def login_get(login_val ):
    print("Trying to log you in now: " )
    
    user_attempt = input("Enter login: ")

    pass_attempt = input("Enter password: ")
    
    login_attempt = [user_attempt,pass_attempt ]
    

    return login_attempt
   



def login_check(login_attempt, login_val):
    
    if login_attempt == login_val:
            print("Login Successful: ")       

    else:
        trys = 0;
        while trys <= 6 : 
                
                print("Username or Password are incorrect! Try again!" )
                
                user_attempt = input("Enter login: ")

                pass_attempt= input("Enter password: ")

                login_attempt = [user_attempt,pass_attempt ]
               

                if login_attempt == login_val:
                                print("Login Successful: ")
                                trys = 10
                                
                else:

                    print("In else!")
                    trys = trys + 1
        if trys == 6:
            print("Out of Attempts! Try Again in 30 sec!")
            
    return login_attempt 

    


def encoder():
            print ( "This is the encoder")

            message = input("Enter message you want to encode: ")

            print("This is the encoded verison: ")
            
            message0 = []
            for ch in message:
                 print("In for loop")
                 message0.append(str((ord(ch))))
            print (message0)

            return message0
        
                
def decoder():
            print ("This is the decoder: ")
                    
            inString = input("Enter message you want to decode: ")

            message =""
            

            for numstr in inString.split():
                  codeNum = int(numstr)
                  message = message + chr(codeNum)

            return message
                      
            print("This is the decoded version : ")
            print(message)
def save_message( login_val):
            print("To save re log in!")
            login_attempt = login_get(login_val)
            login_attempt1 = login_check(login_attempt, login_val)
        
            return login_attempt1, login_val
        
def saving(login_attempt1, login_val):
            if login_attempt1 == login_val:
                print("Message Saved!")

                     
def choice():
    choice = int(input("To encode a meassage type 0 to decode type 1 to do both type any other number. But first make an account : "))
    login_val1 = make_login()
    if choice == 0 :
                
               saved = encoder()
               print()
               login_attempt1, login_val1 = save_message( login_val1)
               saving(login_attempt1, login_val1) 
               #print(saved)                     

               

               
    elif choice == 1:
                
               decoder()
               print()

               login_attempt1, login_val1 = save_message( login_val1)
               saving(login_attempt1, login_val1)               

               
    else:
               encoder()

               login_attempt1, login_val1 = save_message( login_val1)
               saving(login_attempt1, login_val1)

               print()
               decoder()
               
               login_attempt1, login_val1 = save_message( login_val1)
               saving(login_attempt1, login_val1)

choice()


         
   

