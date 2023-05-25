# Warbler

Warbler is a social media application that allows users to post short messages called "warbles". Users can sign up, log in, follow other users, and like warbles. This project is built using Flask, a Python web framework.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- User registration: Users can sign up for a new account with a unique username, email, and password.
- User authentication: Users can log in with their username and password to access their account.
- User profiles: Each user has a profile page that displays their warbles, follower count, and following count.
- Warble creation: Users can create new warbles and post them to their profile.
- Warble feed: Users can view a feed of the most recent warbles from the users they follow.
- Following system: Users can follow/unfollow other users to see their warbles in their feed.
- Like warbles: Users can like/unlike warbles posted by other users.
- Edit profile: Users can update their profile information, including username, email, bio, and profile picture.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/warbler.git

2. Navigate to the project directory:
   
   ```bash
   cd warbler

3. Create a virtual environment:

   ```bash
   python3.7.12 -m venv venv

4. Activate the virtual environment:
   
  - For Mac/Linux:

    ```bash
    source venv/bin/activate

  - For Windows

    ```bash
    venv\Scripts\activate

5. Install the dependencies:

   ```bash
   pip install -r requirements.txt

6. Set up the database:

   ```bash
   createdb warbler
   python3.7.12 seed.py

7. Start the development server:

   ```bash
   flask run

8. Open your browser and navigate to:
  
   ```bash 
   http://localhost:5000


## Usage

- Sign up for a new account with a unique username, email, and password.

- Log in with your username and password to access your account.

- Explore other user's profiles and follow them to see their warbles in you feed. 

- Create a new warbles and post them to your profile.

- Like warbles posted by other users.

- Edit your profile information, including username, email, bio, and profile picture.


## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request. Make sure to follow the project's code style and guidelines.


## License

This project is licensed under the MIT License.
