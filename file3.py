class User :
    def __init__(self, username, login, password):
        self.username = username
        self.login = login
        self.password = password

    def access_level(self):
        return f"malumotlarni kiriting "

class Admin(User):
    def access_level(self):
        return f" {self.username} siz Admin sifatida tizimga kirdingiz "

class Guest(User):
    def access_level(self):
        return f"{self.username} siz mehmon sifatida tizimga kirdingiz "


admin = Admin("@abdurauf", "Abdurauf_._", "passwords")
guest = Guest("@abdurauf", "Abdurauf_._", "passwords")

users = [admin, guest]

for user in users:
    print(user.access_level())