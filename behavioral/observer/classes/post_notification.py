from interfaces import ISubject, IObserver
from post import Post

class PostNotification(ISubject):
    def __init__(self):
        self.__followers = []
        
    def follow(self, observer: IObserver):
        self.__followers.append(observer)

    def unfollow(self, observer: IObserver):
        self.__followers.remove(observer)

    def unfollow_all(self):
        self.__followers.clear()

    def notify_user(self, observer: IObserver) -> None:
        observer.show_notification()

    def notify_all_users(self,):
        for follower in self.__followers:
            follower.show_notification()
