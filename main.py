#SPYCHAT project

#MPORTING VARIABLES FROM SPY_DETAILS FILE

from spy_details import spy_name,spy_salutation,spy_rating,spy_age,spy_is_online

print "Welcome!! to SPY CHAT"
print "Let's get Started!"

#asking user about if he wants to conitue with the same name and age as previously logged in

question = "Do you want to continue as %s %s(Y/N)? " %(spy_salutation,spy_name)
existing=raw_input(question)

def start_chat(spy_name,spy_salutation,spy_age,spy_rating):

    current_status_message = None

    spy_name = spy_salutation + " " + spy_name


    if spy_age > 12 and spy_age < 50:

        if spy_rating > 4.5 and spy_rating <= 5.0:
            print "Great Ace!!"

        elif spy_rating >3.5:
            print "You are one of the Good Ones."

        elif spy_rating >= 2.5:
            print "You can always do Better!"

        else:
            print "We can always use somebody to help in the office."

        print "Authentication complete. Welcome %s Age: %d and Rating of: %.2f \nProud to have you onboard" % (
        spy_name, spy_age, spy_rating)

        spy_is_online=True

        while(True):

            print "1.STATUS UPDATE"
            print "2.EXIT"
            choice = raw_input("ENTER YOUR CHOICE:")
            if choice == "1":

                #it is not yet do any work
                print "something"

            else:

                exit(0)


    else:
        print "You are not of the correct age to be a SPY!!"


if existing == "Y" or existing =="y":
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