from abc import ABC, abstractmethod
from .iobserver import IObserver

class ISubject(ABC):

    @abstractmethod
    def follow(self, observer: IObserver) -> None:
        raise NotImplementedError

    @abstractmethod
    def unfollow(self, observer: IObserver) -> None:
        raise NotImplementedError

    @abstractmethod
    def unfollow_all(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def notify_user(self, observer: IObserver) -> None:
        raise NotImplementedError
    
    @abstractmethod	
    def notify_all_users(self) -> None:
        raise NotImplementedError
