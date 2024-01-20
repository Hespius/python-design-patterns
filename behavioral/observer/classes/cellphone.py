from interfaces import IObserver
from classes import User, Post

class Cellphone(IObserver):

    def __init__(self, user: User, model: str):
        self.__user = user
        self.__model = model

    def update(self, post: Post) -> None:
        print(f"User {self.__user.name} received notification: {post.title} from your {self.__model}")