import csv
import sys
import json
import codecs
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sys.path.append('/Users/grferrei/Documents/ncsu/791/fss16gui/code/3')
from reader import Table

def grab_data():
	dics = []

	with open("/Users/grferrei/Documents/data/dump/github/issues.bson.json") as f:
		for line in f:
			issue = json.loads(line)
			contents = {}
			comments = []
			contents.setdefault("link", issue.get("url"))
			contents.setdefault("title", issue.get("title"))
			contents.setdefault("body", issue.get("body"))
			contents.setdefault("comments",comments)
			dics.append(contents)

	with open("/Users/grferrei/Documents/data/dump/github/issue_comments.bson.json") as f:
		for line in f:
			issue_comments = json.loads(line)
			issue_link = issue_comments.get("issue_url")
			for dic in dics:
				if issue_link == dic.get("link"):
					dic["comments"].append(issue_comments.get("body"))
					break
	# with open("/Users/grferrei/Documents/data/dump/github/commits.bson.json") as f:
	# 	print f.next()

	sid = SentimentIntensityAnalyzer()

	for num,dic in enumerate(dics):
			title = dic['title']
			try:
				ss = sid.polarity_scores(title)
			except AttributeError as e:
				ss = None
			sa = ()
			for k in sorted(ss):
			    sa += '{0}: {1}, '.format(k, ss[k]),
			dic.setdefault("title_sa",sa)

			body = dic['body']
			try:
				ss = sid.polarity_scores(title)
			except AttributeError as e:
				ss = None
			sa = ()
			for k in sorted(ss):
			    sa += '{0}: {1}, '.format(k, ss[k]),
			dic.setdefault("body_sa",sa)

			sa_list = []
			comments = dic['comments']
			for comment in comments:
				try:
					ss = sid.polarity_scores(title)
				except AttributeError as e:
					ss = None
				sa = ()
				for k in sorted(ss):
				    sa += '{0}: {1}, '.format(k, ss[k]),
				sa_list.append(sa)
			dic.setdefault("comments_sa",sa)

	return dics

def write_csv(dics):
	f = csv.writer(open("test.csv", "wb+"))

	# Write CSV Header, If you dont need that, remove this line
	f.writerow(["title", "title_sa", "body", "body_sa", "comments", "comments_sa", "link"])

	for dic in dics:
		try:
			f.writerow([dic["title"], 
		                dic["title_sa"],
		                dic["body"],
		                dic["body_sa"],
		                dic["comments"],
		                dic["comments_sa"],
		                dic["link"]
		                ])
		except UnicodeEncodeError as e:
			print e
			continue

dics = grab_data()
write_csv(dics)

