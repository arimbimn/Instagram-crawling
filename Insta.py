# Import Packages
import instaloader
import json
import csv
import time
import pandas as pd

# Bikin objek instaloader
L = instaloader.Instaloader(max_connection_attempts=0)

## variable output file
tempat_pensil = []
level2 = []

def SaveToJson(memory, file = open("json_output" + ".json", "w+")):
    data = json.dumps(memory)
    file.write(data)
    file.close()

class Insta():    
    def __init__(self, data):
        self.username = data[0]
        self.password = data[1]
        
        L.login(self.username, self.password)

    def getProfile(self, username):
        self.username_target = username
        profile = instaloader.Profile.from_username(L.context, self.username_target)
        return profile

    def getFollowers(self, profile):
        followers = []
        for follower in profile.get_followers():
            follower_username = follower.username
            followers.append(follower_username)
        return followers

    def getPosts(self, profile):
        posts = []
        count_post = 1
        private = profile.is_private
        username = profile.username
    
        if sum(1 for _ in profile.get_posts()) == 0:
            print(profile.username + " PRIVATE")
            data = {"account": username, "post":"", "tag":[], "likes":"0", "comments":[], "date":"", "private":str(private)}
            posts.append(data)
            
        for post in profile.get_posts():
            if count_post > 100:
                break
            print(profile.username + " post ke-" + str(count_post) + " dari " + str(profile.mediacount))

            post_date = post.date_local
            post_username = post.owner_username
            post_hashtag = post.caption_hashtags #list str
            post_likes = post.likes #int

            if post.caption == None:
                post_caption = ""
            else:
                try:
                    post_caption = post.caption.encode('ascii', 'ignore').decode('ascii')
                except :
                    post_caption = ""

            post_comments = post.get_comments()
            memory_comments = []
            for post_comment in post_comments:
                data_comment = post_comment.text.encode('ascii', 'ignore').decode('ascii')
                memory_comments.append(data_comment)

            data = {"account": post_username, "post":post_caption, "tag":post_hashtag, "likes":str(post_likes), "comments":memory_comments, "date":str(post_date), "private":str(private)}
            posts.append(data)
            count_post += 1
        
        return posts
