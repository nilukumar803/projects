#Copyright (C) 2016 Nilu Kumar
#
#This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.
#
#This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
#

import pymongo, json, string, sys
#from pymongo import MongoClient
import pymongo

def mongodb_conn():
	try:
		conn = pymongo.MongoClient()
	except (pymongo.errors.ConnectionFailure, pymongo.errors.ServerSelectionTimeoutError), e:
		print "Could not connect to server: %s" %e
	else:
		return conn

# Database name is test
client = mongodb_conn()
db = client['test']

# Create WE collection object
we_obj = db.we_interested
anonymous_url_mapping_obj = db.anonymous_url_mapping
anonymous_user_mapping_obj = db.anonymous_user_mapping


# 1. Anonymize "url"
# Get Distinct URLs, insert a record for entry into Anonymize_mapping collection. 
# At the same time, update the WE_Interested collection with corresponding "URL_" value
try:
	we_url_list = we_obj.distinct("url")
	print "Count of distinct URLs: " + str(len(we_url_list))

	for i in xrange(0, len(we_url_list)):
    		key_orig = we_url_list[i]
    		# Since dicts do not allow '.', we replace it with 'DOT'
    		key = we_url_list[i].replace(".", "DOT")
    		value = 'url_'+ str(i)
    		anonymous_url_mapping_obj.insert_one({key: value})
    		we_obj.update_many({"url": {"$eq": key_orig}}, {"$set": {"url": value}})
      
	# 2. Anonymize "ur" 
	# Get Distinct URs, insert a record for entry into Anonymize_mapping collection. 
	# At the same time, update the WE_Interested collection with corresponding "USER_" value
	we_user_list = we_obj.distinct("ur")
	print "Count of distinct Users: " + str(len(we_user_list))

	for i in xrange(0, len(we_user_list)):
    		key_orig = we_user_list[i]
    		# Since dicts do not allow '.', we replace it with 'DOT'
    		key = we_user_list[i].replace(".", "DOT")
    		value = 'user_'+ str(i)
    		print key, value
    		anonymous_user_mapping_obj.insert_one({key: value})
    		we_obj.update_many({"ur": {"$eq": key_orig}}, {"$set": {"ur": value}})

except:
	print sys.exc_info()[1]
	print "Error! Exiting..."
