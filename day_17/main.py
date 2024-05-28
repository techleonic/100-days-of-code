# CREATE CLASS
class Users:
    def __init__(self):
        print("new user being created...")


# HOW TO USE THE CLASS
user_1 = Users()

# HOW TO ADD SOME PROPERTIES
user_1.id = "001"
user_1.username = "leonidas"
print(user_1.id)
print(user_1.username)

user_2 = Users()
user_2.id = "002"
user_2.username = "dania"
print(user_2.id)
print(user_2.username)


# CLASS WITH CONSTRUCTOR


class OtherUser:

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0  # optional parameter
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_3 = OtherUser("003", "leonidas")
user_4 = OtherUser("004", "dania")
print(user_3.id)
print(user_3.username)
print(user_3.followers)

print(user_3.following)
print(user_4.followers)
user_3.follow(user_4)
print(user_3.following)
print(user_4.followers)