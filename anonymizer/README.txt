Script name: "anonymize_url_user.py"
Execution: $ python anonymize_url_user.py

Description:
The script 'anonymize_mongo.py' is a Python script created to run adhoc in Linux shell and modify the data in MongoDB.
In the interest of the data owner, data is not presented here and hence the script cannot be executed by itself.
The first part of the script is to query documents for distinct URLs from data collection called "we_interested", 
	map the URL strings with anonymous strings like "url_<index>" and 
	insert the {<URL>:<Anonymous string>} dictionaries into another collection called "anonymous_url_mapping". 
	Then, update the original collection "we_interested"'s "url" values with "url_<index>" strings.
The second part of the script is to query documents by distinct URs (for users) from the collection "we_interested",
	map the Username strings with anonymous strings like "user_<index>" and
	insert the {<Username>:<Anonymous string>} dictionaries into another collection called "anonymous_user_mapping".
	Then, update the original collection "we_interested"'s "ur" values with "user_<index>" strings.
