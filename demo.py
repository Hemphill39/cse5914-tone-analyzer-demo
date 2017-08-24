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

# prompt the user for a url
article_url = input('Enter the URL of a page you want to know about! ')

# get the first post of the search results
submission = reddit.subreddit('all').search('url:' + article_url, sort='top').next()

# make sure its the correct article
print('Getting comments for id: ' + str(submission.id) + ' score: ' + str(submission.score) +  ' title: ' + str(submission.title))

for comment in list(submission.comments)[0:10]:
    print(comment.body)
