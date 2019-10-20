from InstaBagOfWord import *

# Login session
username = "tryxmehhh" #masukkan username ig disini
password = "gatauahcapek" #masukkan password ig disini

data = [username, password]
insta = InstaBagOfWord(data)

for process in SetAndGet :
    if process == 'set' : 
        profile = insta.getProfile("tryxmehhh")
        insta.setBagOfWords(profile, words_list)

        followers = insta.getFollowers(profile)

        for follower in followers :
            print(follower)
            profile = insta.getProfile(follower)
            insta.setBagOfWords(profile, words_list)
            followers2 = insta.getFollowers(profile)
            level2.append(followers2)
    
        for list_followers in level2 :
            count = 1
            for follower in list_followers :
                print(follower)
                profile = insta.getProfile(follower)
                insta.setBagOfWords(profile, words_list)
                count += 1

    elif process == 'get':
        profile = insta.getProfile("tryxmehhh")
        bag_of_words.append(insta.getBagOfWords(profile))
        followers = insta.getFollowers(profile)

        for follower in followers :
            print(follower)
            profile = insta.getProfile(follower)
            bag_of_words.append(insta.getBagOfWords(profile))
            followers2 = insta.getFollowers(profile)
            level2.append(followers2)
    
        for list_followers in level2 :
            count = 1
            for follower in list_followers :
                print(follower)
                profile = insta.getProfile(follower)
                bag_of_words.append(insta.getBagOfWords(profile))
                count += 1


SaveToJson(bag_of_words)
