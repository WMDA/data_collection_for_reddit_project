import pandas as pd
import datetime as dt
import yaml
from psaw import PushshiftAPI

pushshift = PushshiftAPI()

class RedditCollector():
    """
    Class to collect reddit data.
    """
    _REQUIRED_CONFIG = [
        "query",
        "start_date",
        "end_date"
    ]
    
    
    def __init__(self, config):
        self.pushshift = pushshift
        
        if not isinstance(config, dict):
            raise TypeError("config must be a dict")
        
        if not all(element in config for element in self._REQUIRED_CONFIG):
            raise ValueError(f"config must contain keys: {', '.join(self._REQUIRED_CONFIG)}")

        self.config = config
        
        self.config["start_date"] = int(dt.datetime.strptime(self.config["start_date"], "%Y/%m/%d").timestamp())
        self.config["end_date"] = int(dt.datetime.strptime(self.config["end_date"], "%Y/%m/%d").timestamp())
                

    def collect_submissions(self):
        """
        Collect reddit submissions for the given configuration
        parameters 
        """
        gen = self.pushshift.search_submissions(
            q=self.config["query"],
            after=self.config["start_date"],
            before=self.config["end_date"]
            )

        submissions = pd.DataFrame([obj.d_ for obj in gen])
        
        return submissions
        
        
    def collect_comments(self):
        """
        Collect reddit comments for the given configuration
        parameters.
        """
        gen = self.pushshift.search_comments(
            q=self.config["query"],
            after=self.config["start_date"],
            before=self.config["end_date"]
            )

        comments = pd.DataFrame([obj.d_ for obj in gen])
        
        return comments
    
