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

# get the politics subreddit instance
subreddit = reddit.subreddit('politics')

best_posts = subreddit.hot(limit=1)

# this is a terrible way to do this but we're on a time crunch
for submission in best_posts:
    best_post = submission

print('Getting comments for id: ' + str(best_post.id) + ' title: ' + str(best_post.title))


top_level_comments = list(submission.comments)


for comment in top_level_comments[0:10]:
    print(comment.body)
