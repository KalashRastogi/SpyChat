#SPYCHAT project

print "Welcome!! to SPY CHAT"
print "Let's get Started!"

spy_name = raw_input("What is your Name?")

if len(spy_name) > 0:  # to check whether user eneterd something or not

    spy_salutation = raw_input("What should we call you(Mr./Mrs./Miss)?")

    spy_name = spy_salutation + " " + spy_name  # concatenation

    print "Welcome!! " + spy_name + ".\nGlad to have you with us."

    print "Alright " + spy_name + ". I'd like to know a little bit more about you before we proceed..."

    spy_age=0
    spy_rating=0.0
    spy_is_online=False

    spy_age = input("What's your Age?")

    if spy_age > 12 and spy_age < 50:

        spy_rating=input("Enter ratings?(0-5)")

        if spy_rating > 4.5 and spy_rating <= 5.0:
            print "Great Ace!!"

        elif spy_rating >3.5:
            print "You are one of the Good Ones."

        elif spy_rating >= 2.5:
            print "You can always do Better!"

        else:
            print "We can always use somebody to help in the office."

        spy_is_online=True

        print "Authentication complete. Welcome " + spy_name + " age: " + str(spy_age) + " and rating of: " + str(spy_rating) + " Proud to have you onboard"

    else:
        print "You are not of the correct age to be a SPY!!"

else:

    print("Sorry!! A Spy need to have a Valid Name.Try Again Please!!")