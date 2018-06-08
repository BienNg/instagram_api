#Imports
import imageio
from nbformat.current import parse_py
imageio.plugins.ffmpeg.download()
from InstagramAPI import InstagramAPI
import time
import pprint

username="bien_ng_"
InstagramAPI = InstagramAPI(username, "instanbnB1i9e9n6")
InstagramAPI.login()
InstagramAPI.getProfileData()
result = InstagramAPI.LastJson
print(result)

myposts = []
has_more_posts = True
max_id = ""

while has_more_posts:
    InstagramAPI.getSelfUserFeed(maxid=max_id)
    if InstagramAPI.LastJson['more_available'] is not True:
        has_more_posts = False  # stop condition
        print("stopped")

    max_id = InstagramAPI.LastJson.get('next_max_id', '')
    myposts.extend(InstagramAPI.LastJson['items'])  # merge lists
    time.sleep(2)  # Slows the script down to avoid flooding the servers


# Init PrettyPrint for Json Strings
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(myposts)


# get all Followers
user_id = 269147980
followers_set = set()
i=0
for follower in InstagramAPI.getTotalFollowers(user_id):
    followers_set.add(follower.get("username"))
print("All Followers:")
print(followers_set)
print()

# Get Likers of all my posts
likers_set = set()
for post in myposts:
    if i<10:
        InstagramAPI.getMediaLikers(post.get("pk"))
        info = InstagramAPI.LastJson
        for user in info.get("users"):
            likers_set.add(user.get("username"))

        print("new post")
        print(post.get("pk"))
        print(post.get("image_versions2").get("candidates")[0].get("url"))

    else:
        break


print()

print("All likers:")
print(likers_set)
print()

print("Never liked any post!!!:")
never_liked_set = followers_set.difference(likers_set)
for p in never_liked_set:
    print(p)
print()
