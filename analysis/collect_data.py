# An example of how to download data and preprocess

from sentiment import RedditCollector, RedditText

# test

config = {"query": "batman",
 "start_date": "2020/01/01", 
 "end_date": "2020/01/02"}

# Collect the data
reddit = RedditCollector(config=config)
subs = reddit.collect_submissions()

# Preprocess
processed = RedditText(subs)