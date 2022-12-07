class Conection:
    def __init__(self, host='localhost') -> None:
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):
        self.user = user


    def set_password(self, password):
        self.password = password


    @classmethod
    def create_with_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection

    @staticmethod
    def log(msg):
        print('LOG:', msg)


# c1 = Conection()
c1 = Conection.create_with_auth('Wesley', '123456')
# c1.set_user('Wesley')
# c1.set_password('1234')
Conection.log('Apenas um teste!')
print(c1.user)
print(c1.password)