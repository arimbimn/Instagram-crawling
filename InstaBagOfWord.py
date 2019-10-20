# Import Packages
import instaloader
import json
import csv
import time
import re
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

# Bikin objek instaloader
L = instaloader.Instaloader(max_connection_attempts=0)
## variable output file
file1 = open("csv_output_" + ".csv","w+")
file2 = open("json_output_" + ".json", "w+")
fieldnames = ['account', 'post', 'tag', 'likes', 'comments']
writer = csv.DictWriter(file1, fieldnames=fieldnames)
writer.writeheader()
print("perintah ini dijalankan")
tempat_pensil = []
bag_of_words = []
level2 = []
words_list = []
SetAndGet = ['set','get']
# Membuat pengecekan kata imbuhan
stemmer = StemmerFactory().create_stemmer()
konjungsi_list = ["dan","dengan","serta","atau","tetapi","tapi","namun","sedangkan","sebaliknya","malah","malahan","bahkan","itupun","apalagi","jangankan","melainkan","hanya"]

def SaveToJson(memory, file = open("json_output_" + ".json", "w+")):
    data = json.dumps(memory)
    file.write(data)
    file.close()

class InstaBagOfWord():    
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
        count = 1
        private = profile.is_private
        if private:
            print(str(profile.username) + " PRIVATE ACCOUNT")
            data = {"account": profile.username, "post":"", "tag":"", "likes":"", "comments":""}
            posts.append(data)
        for post in profile.get_posts():
            if count > 1:
                break
            username_target = post.owner_username
            #print(post)
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
            data = {"account": username_target, "post":post_caption, "tag":post_hashtag, "likes":str(post_likes), "comments":memory_comments}
            posts.append(data)
            try:
                writer.writerow(data)
            except :
                pass
            count += 1
        
        return posts

    def setBagOfWords(self, profile, words_list) :
        print(profile.username)
        word_list = [line.rstrip('\n') for line in open("kamus.txt", "r")] #kumpulan kata baku
        for post in profile.get_posts():
            if post.caption == None:
                continue
            else:
                post_caption = post.caption.encode('ascii', 'ignore').decode('ascii') 
                post_caption = re.sub('\\n', ' ', post_caption) 
                post_caption = re.sub('[^A-Za-z]', ' ', post_caption)
                if (len(post_caption) == 0) :
                    continue
                else:
                    for words_in_post_caption in post_caption.split() :
                        isKonjungsi = False
                        words_in_post_caption = words_in_post_caption.lower()
                        for konjungsi in konjungsi_list :
                            if (words_in_post_caption == konjungsi) :
                                isKonjungsi = True  #terdeteksi kata tersebut merupakan Konjungsi
                        if (words_in_post_caption != stemmer.stem(words_in_post_caption)) :
                            #Print Jika ada perubahan penghapusan sebuah imbuhan
                            words_in_post_caption = stemmer.stem(words_in_post_caption)
                        for kata_baku in word_list:
                            if(kata_baku == words_in_post_caption) :
                                if not isKonjungsi :
                                    words_list.append(words_in_post_caption)
                                    print(words_in_post_caption)
        words_list = list(dict.fromkeys(words_list))
    
    def getBagOfWords(self, profile) :
        memory = {}
        word_list = [line.rstrip('\n') for line in open("kamus.txt", "r")] #kumpulan kata baku
        count_post = 1
        memory['account'] = profile.username
        for word in words_list:
            if (word == profile.username) :
                break
            memory[word] = 0
        for post in profile.get_posts():
            print(profile.username, str(count_post), 'dari', str(profile.mediacount), 'post')
            if post.caption == None:
                count_post += 1
                continue
            else:
                post_caption = post.caption.encode('ascii', 'ignore').decode('ascii') 
                post_caption = re.sub('\\n', ' ', post_caption) 
                post_caption = re.sub('[^A-Za-z]', ' ', post_caption)
                count_post += 1
                if (len(post_caption) == 0) :
                    continue
                else:
                    print('\n', post_caption, '\n')
                    for words_in_post_caption in post_caption.split() :
                        isKonjungsi = False
                        words_in_post_caption = words_in_post_caption.lower()
                        
                        for konjungsi in konjungsi_list :
                            if (words_in_post_caption == konjungsi) :
                                isKonjungsi = True  #terdeteksi kata tersebut merupakan Konjungsi
                                print("Terdeteksi kata konjungsi ", words_in_post_caption)
                        if (words_in_post_caption != stemmer.stem(words_in_post_caption)) :
                            #Print Jika ada perubahan penghapusan sebuah imbuhan
                            print ("Terdeteksi Imbuhan = ",words_in_post_caption+ " -> ", stemmer.stem(words_in_post_caption))
                            words_in_post_caption = stemmer.stem(words_in_post_caption)
                        for kata_baku in word_list:
                            if(kata_baku == words_in_post_caption) :
                                if not isKonjungsi :
                                    for word in memory:
                                        if (word == profile.username) :
                                            break
                                        if (words_in_post_caption == word) :
                                            memory[words_in_post_caption] = memory[words_in_post_caption] + 1
                                            print('Berhasil Menambahkan Frequency Kata ', words_in_post_caption)
            print("\n")
        return memory
        
