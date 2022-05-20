class Blog:
    def __init__(self):
        self.users = []
        self.posts = []
        self.current_user = None
        
    def _get_post_from_id(self, post_id):
        for post in self.posts:
            if post.id == int(post_id):
                return post
    
    # Method to add a new user to our blog
    def create_new_user(self):
        # Get user info from user input
        username = input('Please enter a username: ')
        if username in {u.username for u in self.users}:
            print(f"User with username {username} already exists")
        else:
            password = input('Please enter a password: ')
            # Create a new User instance with info from input
            new_user = (username, password)
            # Add user instance to list of users on blog
            self.users.append(new_user)
            print(f"{new_user} has been created")

Blog.create_new_user()