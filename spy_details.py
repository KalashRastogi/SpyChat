
class Spy:
    def __init__(self, name, salutation, age, rating):

        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None

class ChatMessage():
    def __init__(self, hidden_text, time, sent_by_me):
        self.hidden_text = hidden_text
        self.sent_by_me = sent_by_me
        self.time = time

spy = Spy('JON SNOW', 'Mr.', 35, 4.0)


friend_one = Spy('Arya Stark', 'Miss', 4.9, 13)
friend_two = Spy('Sansa Stark', 'Miss', 4.5, 20)
friend_three = Spy('Daenerys Targerian', 'Mrs.', 4.2, 29)

# FRIENDS LIST
friends = [friend_one, friend_two, friend_three]