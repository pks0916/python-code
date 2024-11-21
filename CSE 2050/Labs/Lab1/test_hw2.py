import unittest
from hw2 import Profile, Activity, Post, Message, User

class TestProfile(unittest.TestCase):
    """Test cases for the Profile class."""
    
    def test_profile_init(self):
        test_profile = Profile("parth", "pass", "pks904", "parth.sachdev@uconn.edu")
        self.assertEqual(test_profile.username, "parth")
        self.assertEqual(test_profile.password, "pass")
        self.assertEqual(test_profile.screen_name, "pks904")
        self.assertEqual(test_profile.email, "parth.sachdev@uconn.edu")

class TestActivity(unittest.TestCase):
    """Test cases for the Activity class."""
    def test_activity_init(self):
        test_activity = Activity("jack", "this is content")
        self.assertEqual(test_activity.user, "jack")
        self.assertEqual(test_activity.content, "this is content")
        

class TestPost(unittest.TestCase):
    """Test cases for the Post class."""
    def test_post_init(self):
        test_post = Post("jack", "this is content")
        self.assertEqual(test_post.user, "jack")
        self.assertEqual(test_post.content, "this is content")
        

class TestMessage(unittest.TestCase):
    """Test cases for the Message class."""
    def test_message_init(self):
        test_message = Message("jack", "this is content", "this is reciever")
        self.assertEqual(test_message.user, "jack")
        self.assertEqual(test_message.content, "this is content")
        self.assertEqual(test_message.receiver, "this is reciever")

class TestUser(unittest.TestCase):
    """Test cases for the User class."""
    # Add more test cases for other methods and classes
    
    def setUp(self):
        self.user = User("user1", "password1", "User One", "user1@example.com")
    
    def test_user_init(self):
        test_user = User("parth", "pass", "pks904", "parth.sachdev@uconn.edu")
        test_profile = Profile("parth", "pass", "pks904", "parth.sachdev@uconn.edu")
        self.assertEqual(test_user.profile.username, test_profile.username)
        self.assertEqual(test_user.profile.password, test_profile.password)
        self.assertEqual(test_user.profile.screen_name, test_profile.screen_name)
        self.assertEqual(test_user.profile.email, test_profile.email)
        self.assertEqual(test_user.posts, [])
        self.assertEqual(test_user.messages, [])

    def test_create_post(self):
        """Test creating a post for a user."""
        post = self.user.create_post("Test Post Content")
        # Check if the post is added to the user's posts list
        self.assertIn(post, self.user.posts)
        # Check if the user is correct
        self.assertEqual(post.user, self.user)
        # Check if the content of the post is correct
        self.assertEqual(post.content, "Test Post Content")
    
    def test_create_post_with_empty_content(self):
        """Test creating a post with empty content for a user."""
        with self.assertRaises(ValueError):
            self.user.create_post("")

    def test_send_message_empty_content(self):
        with self.assertRaises(ValueError):
            self.user.send_message(self.user, "")

    def test_send_message_empty_receiver(self):
        with self.assertRaises(ValueError):
            self.user.send_message(None, "Hello")
    

if __name__ == "__main__":
    unittest.main()
