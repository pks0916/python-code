class Profile:
    """Class representing a user's profile."""
    def __init__(self, username, password, screen_name, email):
        self.username = username
        self.password = password
        self.screen_name = screen_name
        self.email = email
        """the profile class holds helpfull information about the user """
    # TODO :Implement __init__ method
    # Make sure you add a docstring to all methods.
    
    

    def __str__(self):
        """ Return a string representation of the Profile."""
        return f"Profile - Username: {self.username}, Screen Name: {self.screen_name}, Email: {self.email}"
    
    def modify_profile(self, password=None, screen_name=None, email=None):
        self.password = password
        self.screen_name = screen_name
        self.email = email

class Activity:
    """Base class representing an activity."""

    
    """Serves as the base class for user activities. and the content of the activity."""
    # TODO :Implement __init__ method
    
    def __init__(self, user, content):
        self.user = user
        self.content = content

    def __str__(self):
        """ Return a string representation of the Activity."""
        return f"Activity - User: {self.user.profile.username}, Content: {self.content}"
    


class Post(Activity):
    """Class representing a user's post."""
    def __init__(self, user, content):
        """ Initialize a Post instance. """
        super().__init__(user, content)
    """Represents a user's post in the social network"""
    def __str__(self):
        """ Return a string representation of the Post. """
        return f"Post - {super().__str__()}"
    
    

class Message(Activity):
    """Class representing a user's message to another user."""
    # TODO :Implement __init__ method
    def __init__(self, user, content, receiver):
        super().__init__(user, content)
        self.receiver = receiver
        
    """shows a user's message to another user"""

    def __str__(self):
        """ Return a string representation of the Message."""
        return f"Message - {super().__str__()}, Receiver: {self.receiver.profile.username}"


class User:
    """Class representing a user in the social network."""
    # TODO :Implement __init__ method
    def __init__(self, username, password, screen_name, email):
        self.profile = Profile(username, password, screen_name, email)
        self.posts = []
        self.messages = []
        

    """Contains a Profile instance representing the user's details . Manages user activities such as creating posts and sending messages."""

    def create_post(self, content):
        self.content = content
        
        """Create a new post for the user.
        Args:
            content (str): The content of the post.

        Returns:
            Post: The created post.

        Raises:
            ValueError: If the content of the post is empty.
        """
        # TODO :Implement create_post method
        if not content:
            raise ValueError
        post = Post(self, content)
        self.posts.append(post)
        return post
    
    def send_message(self, receiver, content):
        self.content = content
        self.receiver = receiver
        
        """Send a message from the user to the specified receiver.

        Args:
            receiver (User): The user receiving the message.
            content (str): The content of the message.

        Returns:
            Message: The created message.

        Raises:
            ValueError: If the receiver ID or message content is empty.
        """
        # TODO :Implement send_message method
        if not receiver or not content:
            raise ValueError
        message = Message(self, content, receiver)
        self.messages.append(message)
        return message


    def __str__(self):
        """ Return a string representation of the User."""
        return f"User - {self.profile}"

# Example usage:
if __name__ == "__main__":
    user1 = User("user1", "password1", "User One", "user1@example.com")
    user2 = User("user2", "password2", "User Two", "user2@example.com")

    post1 = user1.create_post("This is my first post!")
    message1 = user2.send_message(user1, "Hi User One! How are you?")
    print(post1)
    print(message1)
    user1.profile.modify_profile(email="User1_1@uconn.edu")
    print(user1)
    print(user2)