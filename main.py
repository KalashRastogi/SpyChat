#--------------------SPYCHAT project-------------------------

#MPORTING VARIABLES FROM SPY_DETAILS FILE

from spy_details import spy_name,spy_salutation,spy_rating,spy_age,spy_is_online

print "Welcome!! to SPY CHAT"
print "Let's get Started!"

#asking user about if he wants to conitue with the same name and age as previously logged in

question = "Do you want to continue as %s %s(Y/N)? " %(spy_salutation,spy_name)
existing=raw_input(question)

#-------------------FUNCTION TO START CHAT-------------------------

def start_chat(spy_name,spy_salutation,spy_age,spy_rating):

    current_status_message = None

    spy_name = spy_salutation + " " + spy_name

    #TO CHECK IF USER'S AGE IS BETWEEN 12 AND 50

    if spy_age > 12 and spy_age < 50:

        if spy_rating > 4.5 and spy_rating <= 5.0:
            print "Great Ace!!"

        elif spy_rating >3.5:
            print "You are one of the Good Ones."

        elif spy_rating >= 2.5:
            print "You can always do Better!"

        else:
            print "We can always use somebody to help in the office."

        print "Authentication complete. Welcome %s Age: %d and Rating of: %.2f \nProud to have you onboard" %(spy_name, spy_age, spy_rating)

        spy_is_online = True

        show_menu = True

        while(show_menu):

            print "1.STATUS UPDATE\n2.ADD FRIEND\n3.SEND A SECRET MESSAGE\n4.READ A SECRET MESSAGE\n5.READ CHATS FROM A USER\n6.CLOSE THE APPLICATION"
            choice = input("ENTER YOUR CHOICE:")
            if choice == 1:

                current_status_message = add_status(current_status_message)

            if choice == 6:

                show_menu = False



    else:
        print "You are not of the correct age to be a SPY!!"

#-----------STATUS MESSAGES LIST--------------------

STATUS_MESSAGES = ['Winter is coming','HODOR?','Everything is better with some wine in belly','VALAR MORGHULIS!','You know nothing JON SNOW!!']


#--------------FUNCTION TO ADD STATUS--------------------------

def add_status(current_status_message):

    if current_status_message is not None:
        print """Your current status message is " %s " \n""" % current_status_message

    else:
        print "You don't have any status message currently \n"


    default = raw_input("Do you want to select from the older status (y/n)?")

    if default.upper() == "N":

        temp1 = True

        while (temp1):
            new_status_message = raw_input("What status message do you want to select?")

            if len(new_status_message) > 0:
                updated_status_message = new_status_message
                STATUS_MESSAGES.append(updated_status_message)
                temp1 = False

            else:
                print "Type something!! Try Again!"

    elif default.upper() == "Y":
        status_number = 1
        for message in STATUS_MESSAGES:
            print str(status_number) + "." + message
            status_number = status_number + 1

        temp1 = True

        while (temp1):
            message_selection = input("\nChoose from the above message ")

            if len(STATUS_MESSAGES) >= message_selection:
                updated_status_message = STATUS_MESSAGES[message_selection - 1]
                print "Status Updated!!"
                temp1 = False
            else:
                print "Choose a valid option!"


    #if user enter other than y or n
    else:
        print "Plz! Input Y or N..."

    return updated_status_message



if existing.upper() == 'Y':
    start_chat(spy_name,spy_salutation,spy_age,spy_rating)

else:

    # ducktyping

    spy_age = 0
    spy_rating = 0.0
    spy_is_online = False

    spy_name = raw_input("Welcome! to SpyChat You must tell me your name first:")

    # to check whether user enetered something or not
    if len(spy_name) > 0:

        spy_salutation = raw_input("What should we call you(Mr./Mrs./Miss)?")

        spy_age = input("What's your Age:")

        spy_rating = input("What is your Spy Rating:")

        spy_is_online = True

        start_chat(spy_name,spy_salutation,spy_age,spy_rating)

    else:

        print("Sorry!! A Spy need to have a Valid Name.Try Again Please!!")