from classes import User, Post, PostNotification, Feed, Cellphone

# Posts
post1 = Post(title="My first post", content="Hello world!")
post2 = Post(title="My second post", content="Hello again!")
post3 = Post(title="My third post", content="Hello again! Again!")

# Post notification
post_notification = PostNotification()

# Users
user1 = User(name="John")
user2 = User(name="Mary")

# Observers
feed1 = Feed(user=user1)
cellphone1 = Cellphone(user=user1, model="iPhone 12")

feed2 = Feed(user=user2)
cellphone2 = Cellphone(user=user2, model="Samsung Galaxy S20")

# Subscribe observers
post_notification.follow(feed1)
post_notification.follow(cellphone1)
post_notification.follow(feed2)
post_notification.follow(cellphone2)

print("Notify all users:")
post_notification.notify_all_users()

print("\nUnfollow John's feed and cellphone...")
post_notification.unfollow(feed1)
post_notification.unfollow(cellphone1)

print("Notify all users AGAIN:")
post_notification.notify_all_users()