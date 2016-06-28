import json, os, sys
from pprint import pprint

list_of_files = []
for root, dirs, files in os.walk(os.path.abspath('./data')):
	for file in files:
		if file.endswith(".json"):
			list_of_files.append(os.path.join(root,file))

#for file in os.listdir("./data"):
#    if file.endswith(".json"):
#        list_of_files.append(file)

if not list_of_files:
	print "There are no json files in the directory ./data"
	sys.exit()

pprint(list_of_files)

for each in list_of_files:
	while True:
		try:
			head, tail = os.path.split(each)
			m = './mask/m_' + tail
			masked_policy_file = open(m, 'w')
			print "Reading from " + each
			print "Writing to " + m
			with open(each, 'r') as policy_file:
       				policy_object = json.load(policy_file)	# dictionary

			for i in range(len(policy_object['policies'])):
				arr_user_col =  policy_object['policies'][i].get('user_col', None)
				if arr_user_col != None:
					for x in range(len(arr_user_col)):
			 			policy_object['policies'][i]['user_col'][x] = "User"+ str(x)

				arr_group_col =  policy_object['policies'][i].get('group_col', None)
				if arr_group_col != None:
					for x in range(len(arr_group_col)):
			 			policy_object['policies'][i]['group_col'][x] = "Group"+ str(x)

			#pprint(policy_object, stream=masked_policy_file)
			with open(m, 'w') as outfile:
    				json.dump(policy_object, masked_policy_file, indent=4, separators=(',', ': '))
    				#json.dump(policy_object, masked_policy_file)

		except ValueError: 
			print "Error reading the json file: " + each + ". Continuing to the next..."
			break
		else:
			#print sys.exc_info()
			break
			#print "Error while executing the script. Exiting..."
