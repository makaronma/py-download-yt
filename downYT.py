from pytube import YouTube
import os


# ask for the link of the video to be downloaded
def askYTLink():
    # link = "https://www.youtube.com/watch?v=-ILcH66zGcY&t=1535s"
    link = input("###Youtube's link: ")
    try:
        # object creation using YouTube
        # which was imported in the beginning
        y = YouTube(link)
        print("=======================")
        print("###Title: "+y.title)
    except:
        print("Connection Error")  # to handle exception

    return y


def askDownloadPath():
    print("=======================")
    # set download path
    path = ("ytDown_Dir")
    print("Path: " + path)
    isExist = str(os.path.exists(path))
    print("Path exists?: "+isExist)
    
    if isExist == False:
        print("Creating Directory. . .")
        os.mkdir(path)
        print("Directory Created!")
    return path


def downloadYT(y, path):
    print("=======================")
    downloadType = str(input("only video or only audio or video+audio? (v/a/va): ").lower())
    print("=======================")
    print("Scanning Streams. . .")
    yt = y.streams
    if downloadType == "a":
        a = yt.filter(only_audio=True)
    elif downloadType == "v":
        a = yt.filter(only_video=True)
    elif downloadType == "va":
        a=yt.filter(only_audio=False).filter(only_video=False)
    else:
        return
    
    a=a.filter(file_extension='mp4')

    # print streams
    for i in range(len(a)):
        print("#" + str(i)+": "+str(a[i]))
        print('FileSize : ' + str(round(a[i].filesize/(1024*1024))) + 'MB')
        print("----------------------")
    # choose which to download
    choice = int(input("Choose which to download(input number): "))

    try:
        # downloading the video
        print("Downloading. . .")
        a[choice].download(path)
        print("Download Completed!")
    except:
        print("Can't Download!")


# ==========================main==========================
y = askYTLink()
path = askDownloadPath()
downloadYT(y, path)

print('Task Completed!')

input("Press enter to exit.")
