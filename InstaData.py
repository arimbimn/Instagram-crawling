# Import Packages
import instaloader
import json

# Bikin objek instaloader
L = instaloader.Instaloader(max_connection_attempts=0)

# Login session
username = "cobaakudong" #masukkan username ig disini
password = "cobaaku123" #masukkan password ig disini

L.login(username, password)

# Profile instagram yang ingin kita telusuri
username_target = "cobaakudong" #masukkan username ig target yang ingin kita lihat informasinya

profile = instaloader.Profile.from_username(L.context, username_target)

# Print list of followers dari instagram target 

file = open("json_output.json", "w+")
memory = []
for followee in profile.get_followers():
    username = followee.username
    profile_dump = instaloader.Profile.from_username(L.context, username)
    #profile_followers = profile_dump.followers #get followers
    #profile_following = profile_dump.followees #get following
    count_post = 1
    for post in profile_dump.get_posts():
        print(username, str(count_post), 'of', str(profile_dump.mediacount))
        #print(username, str(count))
        if post.caption == None:
            count_post += 1
            continue
        else:
            new_caption = post.pcaption.encode('unicode-escape').decode('utf-8')
            print(new_caption)
            count_post += 1
            post_caption = post.caption.encode('unicode-escape').decode('utf-8')
            post_hashtag = post.caption_hashtags #list str
            post_likes = post.likes #int
            post_comments = post.get_comments()
            memory_comments = []
            for post_comment in post_comments:
                data_comment = post_comment.text.encode('unicode-escape').decode('utf-8')
                memory_comments.append(data_comment)
            data = {"account": username, "post":post_caption, "tag":post_hashtag, "likes":str(post_likes), "comments":memory_comments}
            memory.append(data)             
y = json.dumps(memory)
file.write(y)
file.close()
