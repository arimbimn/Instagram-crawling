from Insta import *

# Login session
username = "tryxmehhh" #"cobaakudong" #masukkan username ig disini
password = "gatauahcapek" #"gatauahcapek" #masukkan password ig disini

data = [username, password]
insta = Insta(data)
print("Berhasil Login Instagram")

profile = insta.getProfile("tryxmehhh")

posts = insta.getPosts(profile)
followers = insta.getFollowers(profile)
for post in posts:
    print(profile.username)
    tempat_pensil.append(post)
    df = pd.DataFrame(tempat_pensil)
    export_csv = df.to_csv ('dataframe.csv')

for follower in followers :
    print(follower)
    profile = insta.getProfile(follower)
    posts = insta.getPosts(profile)
    for post in posts:
        tempat_pensil.append(post)
        df = pd.DataFrame(tempat_pensil)
        export_csv = df.to_csv ('dataframe.csv')
    followers2 = insta.getFollowers(profile)
    level2.append(followers2)
    print("sleeping for 20 second")
    time.sleep(20)
    
for list_followers in level2 :
    for follower in list_followers :
        print(follower)
        profile = insta.getProfile(follower)
        posts = insta.getPosts(profile)
        for post in posts:
            tempat_pensil.append(post)
            df = pd.DataFrame(tempat_pensil)
            export_csv = df.to_csv ('dataframe.csv')
        print("sleeping for 20 second")
        time.sleep(20)
    
SaveToJson(tempat_pensil)


