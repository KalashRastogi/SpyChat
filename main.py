# --S--P--Y--C--H--A--T____P--R--O--J--E--C--T--

# importing important pacjages and classes and lists

from steganography.steganography import Steganography
from spy_details import spy, friends
from spy_details import Spy, ChatMessage
from termcolor import colored
from datetime import datetime
import csv

# -------------------STATUS MESSAGES LIST-----------------------------

STATUS_MESSAGES = ['Winter is coming', 'HODOR?', 'Everything is better with some wine in belly', 'VALAR MORGHULIS!',
                   'You know nothing JON SNOW!!']


# ___________________________FUNCTIONS___________________________________

# --------------------FUNCTION TO LOAD CHATS----------------------------

def load_chats():
    with open('chats.csv', 'rb') as chat_data:
        csvreader = csv.reader(chat_data, delimiter=',')

        for row in csvreader:
            chat = ChatMessage(hidden_text=row[1],time=row[2],sent_by_me=row[3])
            friends[int(row[0])].chats.append(chat)

# -------------FUNCTION TO READ MESSAGES FROM THE USER------------------

def read_from_user():
    friend_choice = select_friend()

    if not friends[friend_choice].chats:
        print "No Chats Till NOW!!"

    else:
        print "\nNAME:%s\n" % colored(friends[friend_choice].name, 'red')

        for chat in friends[friend_choice].chats:
            if chat.sent_by_me is True:
                print "Message:%s\nTime:%s\t\t(Sent Message)\n" % (chat.hidden_text, colored(chat.time, 'blue'))
            else:
                print "Message:%s\nTime:%s\t\t(Recieved Message)\n" % (chat.hidden_text, colored(chat.time, 'blue'))


# -------------------FUNCTION TO SEND A MESSAGE------------------------

def send_message():
    friend_choice = select_friend()
    temp = True

    while (temp):

        original_image = input("What is the name of the image?")

        check_image = original_image.split('.')

        if check_image[1] != "jpg":
            print "Please Enter An image with jpg format!!"

        else:
            output_path = 'output.jpg'
            text = raw_input("What do you want to say?")

            Steganography.encode(original_image, output_path, text)
            sent_by_me = True
            new_chat = ChatMessage(text, datetime.now(), sent_by_me)

            friends[friend_choice].chats.append(new_chat)
            with open('chats.csv','a') as chat_data:
                writer = csv.writer(chat_data)
                writer.writerow([int(friend_choice), text,datetime.now(),sent_by_me])

            print "Message sent successfuly!!"

            temp = False


# ------------------FUNCTION TO READ MESSAGE----------------------------

def read_message():
    sender = select_friend()

    output_path = input("What is the name of the file?")
    secret_text = Steganography.decode(output_path)
    sent_by_me = False

    print secret_text

    new_chat = ChatMessage(secret_text,datetime.now(), sent_by_me)
    friends[sender].chats.append(new_chat)

    with open('chats.csv', 'a') as chat_data:
        writer = csv.writer(chat_data)
        writer.writerow([int(sender), secret_text, datetime.now(), sent_by_me])

    print "Your secret message hasb been saved!"


# -------------------FUNCTION TO SELECT FRIEND----------------------------

def select_friend():
    friend_number = 1

    print "Your friends are:"

    for friend in friends:
        print "%d. %s aged %d with rating %.2f is online" % (friend_number, friend.name, friend.age, friend.rating)
        friend_number = friend_number + 1

    friend_choose = input("\nSelect a Friend:")
    friend_index = friend_choose - 1

    return friend_index


# ---------------------FUNCTION TO ADD STATUS------------------------------

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

    else:
        print "Plz! Input Y or N..."

    print "Status Message:%s\n" % updated_status_message

    return updated_status_message


# ----------------------FUNCTION TO LOAD FRIENDS---------------------

def load_friends():
    with open('friends.csv', 'rb') as friend_data:
        csvreader = csv.reader(friend_data, delimiter=',')

        for row in csvreader:
            friend = Spy(name=row[0], salutation=row[1], age=int(row[2]), rating=float(row[3]))
            friends.append(friend)


# -----------------------FUNCTION TO ADD FRIEND-------------------------

def add_friend():
    friend = Spy('', '', 0, 0.0)

    friend.name = raw_input("Enter your friend's name:")
    friend.salutation = raw_input("Are they (Mr./Mrs./Miss):")
    friend.age = input("How old are they:")
    friend.rating = input("What are their Spy Rating:")

    if len(friend.name) > 0 and friend.age > 12 and friend.age < 50 and friend.rating >= spy.rating:
        new_friend = Spy(friend.name, friend.salutation, friend.age, friend.rating)
        friends.append(new_friend)

        with open('friends.csv', 'a') as friend_data:
            writer = csv.writer(friend_data)
            writer.writerow([friend.name, friend.salutation, int(friend.age), float(friend.rating), friend.is_online])

    else:
        print "Sorry! Invalid entry. We can't add spy with the details you provided"

    return len(friends)


# -----------------------FUNCTION TO START CHAT--------------------------

def start_chat(spy):
    current_status_message = None

    spy.name = spy.salutation + " " + spy.name

    if spy.age > 12 and spy.age < 50:

        if spy.rating > 4.5 and spy.rating <= 5.0:
            print "Great Ace!!"

        elif spy.rating > 3.5:
            print "You are one of the Good Ones."

        elif spy.rating >= 2.5:
            print "You can always do Better!"

        else:
            print "We can always use somebody to help in the office."

        print "Authentication complete. Welcome %s Age: %d and Rating of: %.2f \nProud to have you onboard" % (spy.name, spy.age, spy.rating)

        show_menu = True

        while (show_menu):

            print "\n------MENU------\n\t1.STATUS UPDATE\n\t2.ADD FRIEND\n\t3.SEND A SECRET MESSAGE\n\t4.READ A SECRET MESSAGE\n\t5.READ CHATS FROM A USER\n\t6.CLOSE THE APPLICATION\n"
            choice = input("ENTER YOUR CHOICE:")

            if choice == 1:

                current_status_message = add_status(current_status_message)

            elif choice == 2:

                print "WITHOUT FRIENDS CHATTING IS NOT THE CHATTING!!\n"
                number_of_friends = add_friend()
                print 'You have %d friends' % number_of_friends

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
                print "Invalid Choice,TRY AGAIN!!"



    else:
        print "You are not of the correct age to be a SPY!!"


# _______________MAIN PROJECT STARTS HERE!___________________

print "Welcome!!to SPY CHAT"
print "Let's get Started!"

# asking user about if he wants to conitue with the same name and age as previously logged in

question = "Do you want to continue as %s %s(Y/N)? " % (spy.salutation, spy.name)
existing = raw_input(question)

if existing.upper() == 'Y':
    load_friends()
    load_chats()
    start_chat(spy)

else:
    spy = Spy('', '', 0, 0.0)
    spy.name = raw_input("Welcome! to SpyChat You must tell me your name first:")

    # to check whether user enetered something or not
    if len(spy.name) > 0:
        spy.salutation = raw_input("What should we call you(Mr./Mrs./Miss)?")
        spy.age = input("What's your Age:")
        spy.rating = input("What is your Spy Rating:")
        start_chat(spy)

    else:
        print("Sorry!! A Spy need to have a Valid Name.Try Again Please!!")
