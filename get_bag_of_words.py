# Import Packages
import instaloader
import json
import re
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory #install terlebih dahulu di pip install Sastrawi

# Bikin objek instaloader
L = instaloader.Instaloader(max_connection_attempts=0)

# Login session
username = "cobaakudong" #"doonat.id" #masukkan username ig disini
password = "cobaaku123" #"0355103552" #masukkan password ig disini

L.login(username, password)

# Profile instagram yang ingin kita telusuri
username_target = "cobaakudong" #masukkan username ig target yang ingin kita lihat informasinya

profile = instaloader.Profile.from_username(L.context, username_target)

# Membuat pengecekan kata imbuhan
stemmer = StemmerFactory().create_stemmer()

# Print list of followers dari instagram target
count=0
file = open("json_output_BagOfWords.json", "w+")
word_list = [line.rstrip('\n') for line in open("kamus.txt", "r")] #kumpulan kata baku
memory = []
for followee in profile.get_followers():
    username = followee.username
    profile_dump = instaloader.Profile.from_username(L.context, username)
    count_post = 1
    for post in profile_dump.get_posts():
        print(username, str(count_post), 'dari', str(profile_dump.mediacount), 'post')
        if post.caption == None:
            count_post += 1
            continue
        else:
            count_post += 1
            post_caption = post.caption.encode('ascii', 'ignore').decode('ascii') # menghapus emotikon di dalam caption
            post_caption = re.sub('\\n', ' ', post_caption) # menghapus enter di dalam caption
            post_caption = re.sub('[^A-Za-z]', ' ', post_caption) #menghapus karakter yg bukan alphabet
            if (len(post_caption) == 0) :
                continue
            else:
                print('\n', post_caption, '\n')
                """
                Pengecekan agar memenuhi constraints bag of words

                """
                konjungsi_list = ["dan","dengan","serta","atau","tetapi","tapi","namun","sedangkan","sebaliknya","malah","malahan","bahkan","itupun","apalagi","jangankan","melainkan","hanya"]

                for words_in_post_caption in post_caption.split() :

                    isKonjungsi = False #Pengondisian apakah kata tersebut termasuk konjungsi atau tidak
                    words_in_post_caption = words_in_post_caption.lower() #mengecilkan kata yg kapital
                    
                    for konjungsi in konjungsi_list :
                                if (words_in_post_caption == konjungsi) :
                                    isKonjungsi = True  #terdeteksi kata tersebut merupakan Konjungsi
                                    print("Terdeteksi kata konjungsi ", words_in_post_caption)

                    '''

                    Mengecek Apakah kata tersebut kata baku atau bukan.
                    Mengambil sumber kata baku dari list di https://github.com/kangfend/bahasa/blob/master/bahasa/data/kamus.txt


                    '''
                    for kata_baku in word_list:
                        if(kata_baku == words_in_post_caption) :
                            #print("we here")

                            '''

                            Mengecek imbuhan

                            '''
                            if (words_in_post_caption != stemmer.stem(words_in_post_caption)) :
                            
                                #Print Jika ada perubahan penghapusan sebuah imbuhan
                                
                                print ("Terdeteksi Imbuhan = ",words_in_post_caption+ " -> ", stemmer.stem(words_in_post_caption))
                                words_in_post_caption = stemmer.stem(words_in_post_caption)
                                

                            '''

                            Memproses Kata yang bukan konjungsi dan sudah menghapus imbuhan
                            
                            '''
                            if not isKonjungsi :
                                '''
                                If & else disini menambahkan kata pertama terlebih dahuluagar bisa selanjutnya mengecek agar kata tersebut
                                tidak masuk dua kali di data json.

                                '''
                                if (len(memory) >= 1) :
                                    for i in range(len(memory)):
                                        if i == len(memory)-1 :
                                            if (memory[i] != words_in_post_caption) :
                                                memory.append(words_in_post_caption)
                                                print('Berhasil Menambahkan Kata ', words_in_post_caption)
                                        else :
                                            if (memory[i] == words_in_post_caption) :
                                                break
                                else :
                                    memory.append(words_in_post_caption)
                                    print('Berhasil Menambahkan Kata ', words_in_post_caption)
                            
        print("\n") 
    count += 1

data = {"post":memory}
y = json.dumps(memory)
file.write(y)
file.close()
