class User:  # initializing - setting starting values

    def __init__(self, user_id, username):  # Constructor method that initializes the class object with attributes
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "Jack")
user_2 = User("002", "Jane")

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)