# Instabot(For ubuntu)

A python class to automate basic instagram operations that can be performed on PC using selenium framework.
This bot is not build to 'get 10K follower in one day'.It is a simple bot that will run on your machine.The bots which are in the market usually 
give more functionalities but they will get banned sooner or later.

# Motivation
- After reading [this](https://medium.com/better-programming/lets-create-an-instagram-bot-to-show-you-the-power-of-selenium-349d7a6744f7) article ,I try to add some functionalities to the given code in the article.
- Insta Users (specially bots) first follow and then unfollow you after you follow them back,
  this practice is not an ethical way to gain followers and this is often frustrating.
- This class contains a method **analysis** that can return a list of these traitors and unfollow them using another method.

# Screenshots
  ![alt go to repo and see the screenshots folder](https://github.com/Harry-kp/Instabot/blob/master/Screenshots/IMG_20200503_192436.jpg?raw=true)
  ![alt go to repo and see the screenshots folder](https://github.com/Harry-kp/Instabot/blob/master/Screenshots/IMG_20200503_192624.jpg?raw=true)
  ![alt go to repo and see the screenshots folder](https://github.com/Harry-kp/Instabot/blob/master/Screenshots/IMG_20200503_192814.jpg?raw=true)
  ![alt go to repo and see the screenshots folder](https://github.com/Harry-kp/Instabot/blob/master/Screenshots/IMG_20200503_192841.jpg?raw=true)
  ![alt go to repo and see the screenshots folder](https://github.com/Harry-kp/Instabot/blob/master/Screenshots/IMG_20200503_192530.jpg?raw=true)
  
# Tech Used
  - **PYTHON**
  - **SELENIUM**
# Installation
  1. Follow the [link](https://docs.python-guide.org/starting/install3/linux/) to know how to install python 3.x version ,pip and pipenv in your system if not already installed.
  2. Install Firefox in your system if not already installed.

  3. Download geckodriver tar.gz file of your system specification from [this](https://github.com/mozilla/geckodriver/releases) link.

  4. After downloading,extract the tar.gz file using archive manager and move the geckodriver file(not directory) at /usr/local/bin by using command:
  ```
  sudo mv 'path to the file' 'usr/local/bin
  ```
  To make it executable
  ```
  sudo chmod a+x /usr/local/bin/(name of the file)
  ```
  5. Clone the repository from **Harry-kp-patch-1**

  6. In terminal,move to project directory and create a virtual environment using pipenv and pip install the requirement.txt file.
  
  7. Create a python file in preferablly in the same project folder or you can import the module wherever you want your file to be placed(in other directories just resolve 'module not found error').

  8. Write the script and run your file.

# Docs

instagram.py contain only one class Instagrambot().

- #### Initialization of class.
```
bot = Instagrambot('your username,'your password,headless = [Boolean])
```
headless:- headless depicts how you want your browser to work .If you want a browsing screen as you see in the screenshots do not set its value if not then set it to **True**.

- #### Attributes
    1. **self.followers**:-number of people that follows you.
    2. **self.following** = number of people you are following
    3. **self.posts** = number of posts

- #### Methods
  1. **followUsername** :- It takes a username as a input whom you want to follow.

  2. **unfollowUsername**:- It takes a username as a input whom you want to unfollow.

  3. **followerList**:- if a username is provided as an argument ,it will return the list of followers it has otherwise it will return the list of followers of the current login account.

  4. **followingList**:- Same as followerList but returns a list of people you follow.

  5. **analysis**:- It takes two list as an argument followers and following and return three list as traitor,fans and friends.
      - traitor:-people you follow but they aren't following you back.
      - fans:- people that follows you but you are not following them.
      - friends:- people who are maintaining symbiotic relationship.
      ```
      traitor,fans,friends  = bot.analysis(bot.followerList,bot.followingList)
      ```
  6. **isFollowing**:- Take username as an argument and returns boolean value if you follow the given account or not.
      
  6. **closeBot**:- It doesn't take any argument and used at the last of the script to close the bot and return to the terminal.

# Future Goals
  - Method that will download posts from the users timeline.
  - Method that will upload the pictures or stories on a regular basis.
  - Method that can accept or reject according to followers:following ratio the request if you have a private account.
  - Method that can download the bio of users.

# Credits
  Credit goes to [Jérôme Mottet](https://medium.com/@mottet.dev) for  
  [this](https://medium.com/better-programming/lets-create-an-instagram-bot-to-show-you-the-power-of-selenium-349d7a6744f7)    article.
  This article build the base of the project.






      
  
  





  
  
