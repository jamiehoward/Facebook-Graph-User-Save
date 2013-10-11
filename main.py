import urllib2, json

def SearchUser(user_id):
	# user_id = raw_input('User ID: ')
	req = urllib2.Request('http://graph.facebook.com/' + str(user_id))

	# Test graph response for an HTTP error
	try:
		response = urllib2.urlopen(req)
	except urllib2.HTTPError:
		print "Could not retrieve user data." 
		ContinueSearch(user_id)

	# If the page has not returned an HTTP error, then get JSON data
	the_page = response.read()
	data = json.loads(the_page)

	record = '{'
	for (a,v) in data.iteritems():
			record += '"' + a + '" : "' + v + '", '
			
	with open('graph.db', 'ab') as f:
		record += '} '
		f.write(record)
		f.close

	print "Record saved for user: " + str(user_id)
	
	ContinueSearch(user_id)

def ContinueSearch(user_id):
	if int(user_id) == int(ending_id):
		exit()
	else:
		SearchUser(int(user_id) + 1)

starting_id = raw_input('Starting ID: ')
ending_id = raw_input('Ending ID: ')
SearchUser(starting_id)