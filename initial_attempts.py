from birdy.twitter import AppClient
from birdy.twitter import TwitterApiError
from birdy.twitter import TwitterRateLimitError
import networkx as net
import matplotlib.pyplot as plt
import time

CONSUMER_KEY = 'vaP7IuNKKiaQdS5bJu7p0yVui'
CONSUMER_SECRET = '69hDzO08lSeO42REjhZo3gcwZXLoXt0PsGlBKJm3qA4gO58acE'
ACCESS_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAKAfXwAAAAAAF7oWrApsqSNCrt2blKpzQ7D%2ByTI%3D0pUxpiT33W74hpcwcflI4wFhLdLO3gWU0HlS920TCWHkPYHGZ9'
client = AppClient(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN)

g = net.Graph()



def addUsersFollowed(username, depth=0, taboo_list=[]):
	if depth>2 or username in taboo_list:
		return
	taboo_list.append(username)

	print 'adding followers for ' + username
	ids = getFolloweesIds(username)
	users = usersFromIds(ids)

	for user in users:
		# i.e. if the user is a celebrity
		if user.friends_count > 200:
			continue
		else:
			g.add_edge(username, user.screen_name)
			addUsersFollowed(user.screen_name, depth+1)



def usersFromIds(ids):
	print "getting user data for " + str(len(ids)) + " users"
	sublists = partitionList(ids, 100)
	qstrings = []
	for l in sublists:
		qstring = ""
		for uid in l:
			qstring = qstring+str(uid)+","
		# slice off the last comma
		qstring = qstring[:-1]
		qstrings.append(qstring)
	data = []
	for qstring in qstrings:
		data += dataFromIdList(qstring)
	return data

def dataFromIdList(qstring):
	try:
		return client.api.users.lookup.get(user_id=qstring).data
	except TwitterApiError as e:
		pass
	except TwitterRateLimitError as e:
		print "hit a rate limit! sleeping..."
		time.sleep(3)
		return dataFromIdList(qstring)

def getFolloweesIds(username):
	try:
		return client.api.friends.ids.get(screen_name=username).data['ids']
	except TwitterRateLimitError as e:
		print "hit a rate limit! sleeping..."
		time.sleep(3)
		return getFolloweesIds(username)
	

def partitionList(l, n):
	return [l[i:i+n] for i in range(0, len(l), n)]

addUsersFollowed('kanaborama')

net.draw(g)
plt.show()