import praw
import pandas as pd
import time

#  Reddit API Credentials
reddit = praw.Reddit(
    client_id="OO63zV52CLvnU2ftp8_5gg",
    client_secret="FUJ8XiPZ0tFr0daJwzcWWAKAt8zqag",
    user_agent="SentimentScraper",
    username="Traditional-View1849",
    password="Pandu_reddit27"
)

#  Choose a subreddit & number of posts to scrape
subreddit_name = "technology"  
num_posts = 150  # Reduce posts to avoid rate limiting
num_comments_per_post = 20  # Reduce comments per post

#  Fetch posts from subreddit
subreddit = reddit.subreddit(subreddit_name)
posts = subreddit.hot(limit=num_posts)

#  Store data in a list
data = []
post_count = 0

for post in posts:
    post_count += 1
    print(f"Fetching Post {post_count}/{num_posts}: {post.title[:50]}...")

    post.comments.replace_more(limit=0)  # Remove "More Comments" links
    comment_count = 0

    for comment in post.comments[:num_comments_per_post]:  
        data.append([comment.body, post.title, subreddit_name])
        comment_count += 1

    print(f"{comment_count} comments collected!")

    # **Respect Reddit's API Rate Limits**
    time.sleep(2)  # Delay to avoid getting blocked

# 🔹 Convert to DataFrame
df = pd.DataFrame(data, columns=["Comment", "Post Title", "Subreddit"])
df.to_csv("reddit_comments.csv", index=False)

print(f"\n Reddit comments saved to 'reddit_comments.csv'! ({len(df)} comments collected)")
