# PolarizationOfInformation
A work in progress: Can we quantify the polarization of opinions and information surrounding a topic on the web?


There are a few things that need to be done to the code before it will work on your machine besides having 
the proper python packages installed as well as a mysql database.

In MySqlNewsCrawler.py : edit the appropriate host name, port, username, password, database, and charset. These are just defaults and mostlikely won't work on your machine.

In newsCrawler2.py tweetSearch (currently line 302) : add your twitter account OAuth tokens for acces to the twitter API. This can be easily obtained if you have a twitter account.



newsCrawler2.py crawlByTopic(topic) searches the topic string in google news, google search(ToDo), and twiiter's api and begins following the articles and creating or updating tables in existing mysql database.

NewsCrawlerGraph.py contains the newsCrawlerGraph class which connects articles covering a news topic as nodes to other articles with calculated edge weights based on parameters (so far just longest common subsequence).
