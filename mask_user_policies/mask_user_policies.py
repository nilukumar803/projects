#Copyright (C) 2016 Nilu Kumar
#
#This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.
#
#This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
#

import json, os, sys
from pprint import pprint

# Get the list of .json files in the dir ./data
list_of_files = []
for root, dirs, files in os.walk(os.path.abspath('./data')):
	for file in files:
		if file.endswith(".json"):
			list_of_files.append(os.path.join(root,file))

if not list_of_files:
	print "There are no json files in the directory ./data"
	sys.exit()

pprint(list_of_files)

# For each of the .json files, mask the policy_object's user_name and group_name
# create a corresponding mask_<file> in ./mask dir 
# and write the content of the file into mask_<file> with the masked values
for each in list_of_files:
	while True:
		try:
			head, tail = os.path.split(each)
			masked_policy_file = './mask/m_' + tail
			print "Reading from " + each
			print "Writing to " + m
			with open(each, 'r') as policy_file:
       				policy_object = json.load(policy_file)	# dictionary

			for i in range(len(policy_object['policies'])):
				arr_user_name =  policy_object['policies'][i].get('user_name', None)
				if arr_user_name != None:
					for x in range(len(arr_user_name)):
			 			policy_object['policies'][i]['user_name'][x] = "User"+ str(x)

				arr_group_name =  policy_object['policies'][i].get('group_name', None)
				if arr_group_name != None:
					for x in range(len(arr_group_name)):
			 			policy_object['policies'][i]['group_name'][x] = "Group"+ str(x)

			#pprint(policy_object, stream=masked_policy_file)
			with open(masked_policy_file, 'w') as outfile:
    				json.dump(policy_object, masked_policy_file, indent=4, separators=(',', ': '))

		except ValueError: 
			print "Error reading the json file: " + each + ". Continuing to the next..."
			break
		else:
			#print sys.exc_info()
			break
			#print "Error while executing the script. Exiting..."
