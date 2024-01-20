from typing import List
from interfaces import IObserver
from classes import User, Post

class Feed(IObserver):

    def __init__(self, user: User):
        self.__user = user
        self.__posts: List[Post] = []

    def update(self, post: Post) -> None:
        self.__posts.append(post)
        print(f"New post added to {self.__user.name}'s feed: {post.title}")
    
    def show_feed(self):
        print(f"{self.__user.name}'s feed:")
        for post in self.__posts:
            print(f"\t{post.title}")


