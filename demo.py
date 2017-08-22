# Reddit account for this application
# UN: CSE5914DemoApp Password: CSE5914DemoApp
# id: 7QB2D2urNdEo8A
# secret: 6u6Nqb1HAd6Al2kJ5grcAlNOTS8
# user_agent: dreese_305
client_id = "7QB2D2urNdEo8A"
client_secret = "6u6Nqb1HAd6Al2kJ5grcAlNOTS8"
password = "CSE5914DemoApp"
username = "CSE5914DemoApp"
user_agent = "dreese_305"

import praw

# get an instance of our reddit account
reddit = praw.Reddit(client_id=client_id, client_secret=client_secret, password=password, username=username, user_agent=user_agent)

# make sure you're logged into the right person
print('logged in as: ' + str(reddit.user.me()))
