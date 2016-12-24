"""
This is a Python script to:
-Retrieve all the Facebook posts from BillGates public wall
-Save everything in a text file.

Before you run this script, you need to:
1- Create an access token from https://developers.facebook.com/tools/explorer/
2- Update the field for access_token below
3- You should install the Facebook SDk if you don`t have it yet. 
sudo pip install facebook-sdk requests  (for unix users)
4- Create the text file named gates.txt
"""
import facebook
import requests
import datetime
import sys

#Encoding for saving the content into the file
reload(sys)
sys.setdefaultencoding('utf-8')


##############Configuration##################

# Insert your access token here.  You can get a temporary one
# here: https://developers.facebook.com/tools/explorer/
access_token = 'your_access_token_should_be_pasted_here'
# Fetch contents from the user`s wall
#user = 'me' # if you want to get your own wall content
user = 'BillGates' #Bill Gates wall


graph = facebook.GraphAPI(access_token, version='2.2')
profile = graph.get_object(user)
posts = graph.get_connections(profile['id'], 'posts')

##############END Configuration##################

def savePost(post):

    #Open the file then write the retrieve content inside
    f = open("gates.txt", "a")
    f.write("\n###################\n "+post['created_time'])
    f.write(post['message'])
    f.close()


counter = 0
while True:
    try:
        # Process each post retrieved
        [savePost(post=post) for post in posts['data']]
        #Update the number of posts retrieved
        counter = counter + len(posts['data'])
        # Go to the next page, if there is.
        posts = requests.get(posts['paging']['next']).json()
        
    except KeyError:
        break


#Write the total number of posts retrieved
f = open("gates.txt", "a")
f.write("\n Posts retrieved: %s" % (counter))
f.close()
print "Done!"


