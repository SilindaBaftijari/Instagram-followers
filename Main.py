import json

with open('following.json') as f:
    following_json = json.load(f)

# extract the list of dictionaries from the "relationships_following" key
following_data = following_json['relationships_following']

# open the JSON file and read its contents
with open('followers.json', 'r') as f:
    followers_json = f.read()

# load the JSON data from a string
followers_data = json.loads(followers_json)

# extract the set of users you are following
following_set = set([user_dict['value'] for data in following_data for user_dict in data['string_list_data']])

# extract the set of users following you
followers_set = set([user_dict['value'] for data in followers_data for user_dict in data['string_list_data']])

# calculate the set of users who don't follow you back
not_following_back = following_set - followers_set

# print the result
for user in not_following_back:
    print(user)