import requests,os,re
import bs4

def getVideo(url):
    videoUrl = {'video': url}
    responce = requests.get('http://www.youtubeinmp3.com/download/',    params=videoUrl)
    soup = bs4.BeautifulSoup(responce.content, 'lxml')
    videoTitle = soup.find('span', id='videoTitle').text
    videoTitle=regex.sub('',videoTitle)
    try:
        videoLink = soup.find('a', id='download')['href']
        vidList.append([videoTitle,rawUrl+videoLink])
    except:
        print(videoTitle+' could not be downloaded')


def getList(videoListUrl):
    global folderName
    url='https://www.youtube.com'
    soup=bs4.BeautifulSoup(requests.get(videoListUrl).content,'lxml')
    folderName=soup.title.text
    links = soup.select('a.pl-video-title-link.yt-uix-tile-link.yt-uix-sessionlink.spf-link')
    print(len(links),'videos found')
    for link in links:
        getVideo(url+link['href'])

def download():
    directory = homedir+folderName
    if not os.path.exists(directory):
        print('creating diretory')
        os.makedirs(directory)
    print(directory)
    i =1
    for name,link in vidList:
        if os.path.exists(directory+'\\'+name+'.mp3'):
            print('skiping '+name+' songs   remaining:',len(vidList)-i)
            i=i+1
        else:
            video = requests.get(link)
            with open(directory+'\\'+name+ '.mp3', 'wb') as writefile:
                writefile.write(video.content)
            print('video downloaded, check it out.        Remaining videos:',len(vidList)-i)
            i=i+1

vidList=[]
folderName=''
homedir=os.path.expanduser('~')+'\\Music\\'
regex = re.compile('[^a-zA-Z]')
rawUrl='http://www.youtubeinmp3.com'
videoListUrl=str(input('enter the playlist link:'))
getList(videoListUrl)
print(len(vidList),'vides are ready to download')
download()
