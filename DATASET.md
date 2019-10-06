# DataSet <h1>

### Data Description
This data is obtained from the list of followers of the target account.

## Format
Saved in .csv 

### Field Names
* Account :
contains a list of user accounts from the target Instagram account.
* Post : 
contains a caption in every post from the user's account.
* Hastag : 
contains hashtags that are used for each user posting account.
* Likes :
contains the number of likes obtained by user accounts for each user account post.
* Comments :
contains the contents of comments in each user account post.

| Account | Post | Hastag | Likes | Comments |
| -------- | ---- | ------ | ----- | ------- |
| ........ | ..... | ..... | ...... | ...... |
| ........ | ..... | ..... | ...... | ...... |
<h1> 
 
 ### How many dataset can be reached? 
Have reached about 19000 row of dataset and size about 1,33 mb

### How to process 
Login to your Instagram account with your username and password using the ```L.login``` method. After that we determine the target username that we want to see the account information. Create a profile object by using the ```instaloader.Profile.from_username``` method whose parameters are taken from previously created variables. We create a CSV file to store all the followers list information from the target username. This CSV file consists of the following field names: account, post, hashtag, likes and comments. After that, iterate the followers of the target username profile. In every profile followers have a post, after that iterate the post. If the post has no caption, then continue to the next post. But if the post has a caption, post, hashtag, likes, and comments will be filled.

