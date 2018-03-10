from clint.textui import progress
import bs4
import requests
import sys
import  os
import time

def download_song(songs):
    print("Songs:\n")
    for i in range(len(songs)):
        print(" " + str(i) + ' ' + songs[i].getText())
    print("  " + str(i + 2) + ". Download all songs")
    n=input()
    if n== len(songs)+1:
        for song in songs:
            download_song1(song)
    else:
        download_song(songs[n-1])

def download(song):
    total_downloads=0
    song_url = "http://songspk3.co/" + song.get("href")
    dirrectory_name=os.path.basename(song_url)[0:len(os.path.basename(song_url))-5].replace('-'," ").title()
    response=requests.get(song_url)
    soup=bs4.BeautifulSoup(response,'html.parser')
    download_link=soup.select("a")[2].get("href")
    try:
        requests.get(download_link,stream=True)
    except requests.exceptions.RequestException as e:
        print("Download nhi hora shayad song available nhi hai")
        sys.exit()
    os.makedirs(dirrectory_name,exist_ok=True)
    music=open(os.path.join(dirrectory_name,song.getText()+".mp3"),"wb")
    print("Downloading.........")
    length=int(response.headers.get("content-length"))
    strt=time.mktime(time.localtime())
    end=0
    for chuck in progress.bar(res.iter_content(chuck_size=10000),expected_size=(total_length/10000)+1):
        if chuck:
            total_downloads+=len(chuck)
            music.write(chuck)
            end=time.mktime(time.localtime())
            if end >start:
                sys.stdout.write("> Speed:%.2f Kbps Progess:"%((total_downloads/100)))
            else:
                 sys.stdout.write("> Speed:%.2f Kbps Progress: " %((dl/1000)))
            sys.stdout.flush()
            if(dl>=total_length):
                break
            music.flush()
    print("Complete")
    music.close()

def suggest(movie_name):
    movies=movie_name.split(" ")
    movie1=movies[0]
    if(movie1.lower().isdigit()):
        url = "http://songspk3.me/songs-movies-0-9.html"
    else:
        url = "http://songspk3.in/songs-movies-" + movie1.lower() + ".html"
    response=requests.get(url)
    response.raise_for_status()
    soup=bs4.BeautifulSoup(response.text,'html.parser')
    movies1=soup.select(".list>li a")
    count=0
    dic={}
    for i in range(len(movies1)):
        flag=False
        cache = movie1[i].getText.split(" ")
        for item in cache:
            for item1 in movies:
                if(item1 in item or item in item1):
                    flag_movie=1
                    count+=1
                    dic[count]=1
                    flag=True
                    break
            if(flag):
                break
    if(not count):
        print("Nhi hai")
        sys.exit()
    url = "http://songspk3.co/" + movie_list[dic[n]].getText() + "-songs.html"
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    songs = soup.select(".single-grid > ul > li > a")
    song_download(songs)

def downloads():
    movie_name=input("\n > Enter movie:").lower()
    url="http://songspk3.in/" + movie_name + "-songs.html"
    res=requests.get(url)
    res.raise_for_status()
    soup=bs4.BeautifulSoup(res.text,'html.parser')
    songs=soup.select(".single-grid>ul>li>a")
    print("here")
    if(len(songs))==0:
        suggest(movie_name)
    else:
        download_song(songs)




downloads()
