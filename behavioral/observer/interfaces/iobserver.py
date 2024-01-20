from abc import ABC, abstractmethod
from classes import Post

class IObserver(ABC):

    @abstractmethod
    def update(self, post: Post) -> None:
        raise NotImplementedError