import sys
import json
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sys.path.append('/Users/grferrei/Documents/ncsu/791/fss16gui/code/3')
from reader import Table

dic = {}
dicx = []

with open("/Users/grferrei/Documents/data/dump/github/issues.bson.json") as f:
	for line in f:
		issue = json.loads(line)
		issue_link = issue.get("url")
		contents = {}
		comments = []
		contents.setdefault("title", issue.get("title"))
		contents.setdefault("body", issue.get("body"))
		contents.setdefault("comments",comments)
		dic.setdefault(issue_link, contents)

with open("/Users/grferrei/Documents/data/dump/github/issue_comments.bson.json") as f:
	for line in f:
		issue_comments = json.loads(line)
		issue_link = issue_comments.get("issue_url")
		if issue_link in dic:
			dic[issue_link]["comments"].append(issue_comments.get("body"))

# with open("/Users/grferrei/Documents/data/dump/github/commits.bson.json") as f:
# 	print f.next()
pos,neg,comp,neut = [],[],[],[]
sid = SentimentIntensityAnalyzer()
for num,key in enumerate(dic.iterkeys()):
	if (num < 2):
		dic2 = dic[key]
		print "ISSUE #" + str(num) + ":"

		title = dic2['title']
		print "TITLE: " + title
		ss = sid.polarity_scores(title)
		# print "SENTIMENT ANALYSIS: ",
		# sa = ()
		for k in sorted(ss):
		#     sa += '{0}: {1}, '.format(k, ss[k]),
		# print sa
		#


		# body = dic2['body']
		# print "BODY: " + body
		# ss = sid.polarity_scores(body)
		# print "SENTIMENT ANALYSIS: ",
		# sa = ()
		# for k in sorted(ss):
		#     sa += '{0}: {1}, '.format(k, ss[k]),
		# print sa 

		# comments = dic2['comments']
		# for comment in comments:
		# 	print "COMMENT: " + comment
		# 	ss = sid.polarity_scores(comment)
		# 	print "SENTIMENT ANALYSIS: ",
		# 	sa = ()
		# 	for k in sorted(ss):
		# 		sa += '{0}: {1}, '.format(k, ss[k]),
		# 	print sa
		# print 
	else:
		break
	

