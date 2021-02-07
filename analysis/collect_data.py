from sentiment import RedditCollector

# test

config = {"query": "batman",
 "start_date": "2020/01/01", 
 "end_date": "2020/01/02"}


reddit = RedditCollector(config=config)

subs = reddit.collect_submissions()
