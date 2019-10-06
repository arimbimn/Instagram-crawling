# Import Packages
import instaloader
import json
import csv

# Bikin objek instaloader
L = instaloader.Instaloader(max_connection_attempts=0)

# Login session
username = "arimbimn" #masukkan username ig disini
password = "meganingrum123" #masukkan password ig disini

L.login(username, password)

# Profile instagram yang ingin kita telusuri
username_target = "arimbimn" #masukkan username ig target yang ingin kita lihat informasinya

profile = instaloader.Profile.from_username(L.context, username_target)

# Print list of followers dari instagram target 

## variable output file
#file = open("json_output.json", "w+")
file1 = open("csv_output_" + ".csv","w+")
file2 = open("json_output_" + ".json", "w+")
fieldnames = ['account', 'post', 'tag', 'likes', 'comments']
writer = csv.DictWriter(file1, fieldnames=fieldnames)
writer.writeheader()

memory = []
for follower in profile.get_followers():
    username = follower.username
    profile_dump = instaloader.Profile.from_username(L.context, username)
    count_post = 1
    for post in profile_dump.get_posts():
        print(username, str(count_post), 'of', str(profile_dump.mediacount))
        if post.caption == None:
            count_post += 1
            continue
        else:
            #new_caption = post.pcaption.encode('unicode-escape').decode('utf-8')
            #print(new_caption)
            count_post += 1
            post_caption = post.caption.encode('ascii', 'ignore').decode('ascii')
            post_hashtag = post.caption_hashtags #list str
            post_likes = post.likes #int
            post_comments = post.get_comments()
            memory_comments = []
            for post_comment in post_comments:
                data_comment = post_comment.text.encode('ascii', 'ignore').decode('ascii')
                memory_comments.append(data_comment)
            data = {"account": username, "post":post_caption, "tag":post_hashtag, "likes":str(post_likes), "comments":memory_comments}
            memory.append(data)
            writer.writerow(data)
            
y = json.dumps(memory)
file2.write(y)
file1.close()
file2.close()
