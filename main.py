# --------------------SPYCHAT project-------------------------


from steganography.steganography import Steganography
from datetime import datetime
from spy_details import spy, friends

# -----------STATUS MESSAGES LIST--------------------

STATUS_MESSAGES = ['Winter is coming', 'HODOR?', 'Everything is better with some wine in belly', 'VALAR MORGHULIS!',
                   'You know nothing JON SNOW!!']

# -----------LIST NECESSARY TO ADD FRIEND FUNCTION-----------


print "Welcome!! to SPY CHAT"
print "Let's get Started!"

# asking user about if he wants to conitue with the same name and age as previously logged in

question = "Do you want to continue as %s %s(Y/N)? " % (spy['salutation'], spy['name'])
existing = raw_input(question)

#-------------FUNCTION TO READ MESSAGES FROM THE USER------------------

def read_from_user():

    friend_choice = select_friend()

    if not friends[friend_choice]['chats']:
        print "No Chats Till NOW!!"

    else:
        print "\n%s of Age %d and Rating %.2f and her Chats Record\n" %(friends[friend_choice]['name'],friends[friend_choice]['age'],friends[friend_choice]['rating'])
        for chat in friends[friend_choice]['chats']:
            print "Message:%s\t\tTime:%s" %(chat['message'],chat['time'])

# -----------FUNCTION TO SEND A MESSAGE------------------------

def send_message():

    friend_choice = select_friend()
    temp = True

    while(temp):
        original_image = input("What is the name of the image?")

        check_image = original_image.split('.')

        if check_image[1] != "jpg":
            print "Please Enter An image with jpg format!!"
        else:
            output_path = 'output.jpg'
            text = raw_input("What do you want to say?")
            Steganography.encode(original_image, output_path, text)

            new_chat = {
                'message': text,
                'time': datetime.now(),
                'sent_by_me': True
            }

            friends[friend_choice]['chats'].append(new_chat)

            print "Your secret image is ready!"
            temp = False


# ------------FUNCTION TO READ MESSAGE------------------------

def read_message():

    sender = select_friend()

    output_path = input("What is the name of the file?")

    secret_text = Steganography.decode(output_path)

    print secret_text

    new_chat = {
        'message': secret_text,
        'time': datetime.now(),
        'sent_by_me': False
    }

    friends[sender]['chats'].append(new_chat)

    print "Your secret message hasb been saved!"


# -----------FUNCTION TO SELECT FRIEND------------------------

def select_friend():
    friend_number = 0

    for friend in friends:
        print "%d. %s aged %d with rating %.2f is online" % (
        friend_number + 1, friend['name'], friend['age'], friend['rating'])
        friend_number = friend_number + 1

    friend_choose = input("\nSelect a Friend:")
    friend_index = friend_choose - 1

    return friend_index


# --------------FUNCTION TO ADD STATUS--------------------------

def add_status(current_status_message):
    updated_status_message = None

    if current_status_message is not None:
        print """Your current status message is "%s" \n""" % current_status_message

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
            print "%d.%s" % (status_number, message)
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


    # if user enter other than y or n
    else:
        print "Plz! Input Y or N..."

    print "Status Message:%s\n" % updated_status_message

    return updated_status_message


# -----------------------FUNCTION TO ADD FRIEND-----------------------

def add_friend():
    new_friend = {
        'name': '',
        'salutation': '',
        'rating': 0.0,
        'age': 0,
        'chats': []
    }

    new_friend['name'] = raw_input("Enter your friend's name:")
    new_friend['salutation'] = raw_input("Are they (Mr./Mrs./Miss):")
    new_friend['name'] = new_friend['salutation'] + " " + new_friend['name']

    new_friend['age'] = input("How old are they:")
    new_friend['rating'] = input("What are their Spy Rating:")

    if len(new_friend['name']) > 0 and new_friend['age'] > 12 and new_friend['age'] < 50 and new_friend['rating'] >= \
            spy['rating']:
        friends.append(new_friend)
    else:
        print "Sorry! Invalid entry. We can't add spy with the details you provided"

    return len(friends)


# -------------------FUNCTION TO START CHAT-------------------------

def start_chat(spy_name,spy_salutation, spy_age, spy_rating):
    current_status_message = None

    spy['name'] = spy['salutation'] + " " + spy['name']

    # TO CHECK IF USER'S AGE IS BETWEEN 12 AND 50

    if spy_age > 12 and spy_age < 50:

        if spy_rating > 4.5 and spy_rating <= 5.0:
            print "Great Ace!!"

        elif spy_rating > 3.5:
            print "You are one of the Good Ones."

        elif spy_rating >= 2.5:
            print "You can always do Better!"

        else:
            print "We can always use somebody to help in the office."

        print "Authentication complete. Welcome %s Age: %d and Rating of: %.2f \nProud to have you onboard" % (
        spy_name, spy_age, spy_rating)

        show_menu = True

        while (show_menu):

            print "\n------MENU------\n1.STATUS UPDATE\n2.ADD FRIEND\n3.SEND A SECRET MESSAGE\n4.READ A SECRET MESSAGE\n5.READ CHATS FROM A USER\n6.CLOSE THE APPLICATION\n"
            choice = input("ENTER YOUR CHOICE:")

            if choice == 1:

                current_status_message = add_status(current_status_message)

            elif choice == 2:

                print "WITHOUT FRIENDS CHATTING IS NOT THE CHATTING!!\n"
                number_of_friends = add_friend()
                print 'You have %d friends' % number_of_friends
                if number_of_friends > 0:

                    # to display all friends
                    print "Here are your Friends:"
                    friend_number = 1
                    for friend in friends:
                        print  "%d.%s" % (friend_number, friend['name'])
                        friend_number = friend_number + 1

            elif choice == 3:

                if not friends:
                    print "To use this Functionality you should have friends First!!!"
                else:
                    send_message()

            elif choice == 4:

                if not friends:
                    print "To use this Functionality you should have friends First!!!"
                else:
                    read_message()

            elif choice == 5:

                if not friends:
                    print "To use this Functionality you should have friends First!!!"
                else:
                    read_from_user()


            elif choice == 6:

                show_menu = False



    else:
        print "You are not of the correct age to be a SPY!!"


if existing.upper() == 'Y':
    start_chat(spy['name'], spy['salutation'], spy['age'], spy['rating'])

else:

    friends = []

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

        start_chat(spy_name, spy_salutation, spy_age, spy_rating)

    else:

        print("Sorry!! A Spy need to have a Valid Name.Try Again Please!!")
