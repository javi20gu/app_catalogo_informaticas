

class Login:

    __user: str
    __password: str
    __login: bool = False

    def __str__(self) -> str:
        return 'Login <{}: {}>'.format(self.__user, self.__login)

    def connect(self, username: str, password: str) -> bool:
        self.__user = username
        self.__password = password
        check = self.__user.strip() == 'prueba' and self.__password.strip() == 'prueba'
        if check:
            self.__login = True
        return self.__login

    def get_username(self):
        return self.__user

    def is_login(self) -> bool:
        return self.__login

    def close_session(self) -> None:
        if self.__login is True:
            self.__login = not self.__login
