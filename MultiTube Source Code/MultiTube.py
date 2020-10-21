#https://www.youtube.com/watch?v=4Slcq0Jj4RM https://www.youtube.com/watch?v=4Slcq0Jj4RM https://www.youtube.com/watch?v=o9aaoiyJlcM
#https://youtu.be/yiLI9Upkt_o
import pytube
import speedtest


def progress_function(stream, chunk, bytes_remaining):
    if(round((1-bytes_remaining/video.filesize)*100)%20==0):
        print(round((1-bytes_remaining/video.filesize)*100, 2), '% done...')


try:
    print("\n::::Initializing Bulk Youtube Video Downloader v1.0a (つ▀¯▀)つ >>>>>>>>>>>>>>>>>>>>")
    st = speedtest.Speedtest()
    print("\n>PLEASE BE PATIENT, CHECKING DATA SPEED...")
    speed = st.download() / 1e+6
    print(">DONE.")
    print("========================================---------")
    session = input("\n>NAME THIS SESSION AS : ")
    print(">QUERY OK!")
    print(">FETCHING DATA WAIT...")

    # n = int(input("\nEnter how many videos you want to download in total :"))
    urlist = []
    url = input("\n>ENTER ALL THE URLs (SEPERATED BY SPACE) :> ")
    urlist.append(url.split(' '))
    sizeu = len(url.split(' '))
    print(">TOTAL URLS : ", sizeu)
    print(">All URLS SET!")

    # print("LIST : ",urlist)

    if (input(">SET VIDEO QUALITY >> '1' => 720p -<OR>- '2' => 360p) : ") == "1"):
        TAG = 22
    else:
        TAG = 134

    print("\n>SIT BACK AND RELAX AND LET ME SERVE YOU! ;)")

    print("\n>YOUR INTERNET SPEED :", '%.2f' % (speed), "mbps")

    print("\n\n==============================================<< Active Session:", session,
          " >>========================================================")

    for i in range(0, sizeu):
        youtube = pytube.YouTube(urlist[0][i], on_progress_callback=progress_function)

        video = youtube.streams.get_by_itag(TAG)
        print("\n>DOWNLOADING NOW : VIDEO ID: ", (i + 1), " ------------------------------>")
        try:
            size = video.filesize / 1e+6
            title = youtube.title
            print("\n->Video Url : " + urlist[0][i])
            print("->Video Title : ", title)
            print("->Video Length : ", '%.2f' % (youtube.length / 60), "minutes")
            # print("->Video Description : ", youtube.description)
            print("->Video Size : ", '%.2f' % (size), "MB")
            print("->Estimated Time to Download : ", '%.2f' % (size / (speed / 0.125)), "minutes")

            print("\n>Please Wait...")
            assert video.download('C:\DHAAAGA\\' + session)

            print(
                "\n> ## Video Downloaded Successfully! >> VIDEO SAVED @ " + 'C:\DHAAAGA\\' + session + "\\" + title + ".mp4")
            print("\n\n==================================< YTD >==================================>")


        except Exception as e:
            print("Failed to download Error was > ", e.args)

    print("\n\n>THANK YOU FOR USING ME,MADE BY ARPITM.")
    if (input(">Press Q to quit :") == "Q"):
        print(">BYE.")
    else:
        print(">BYE.")

except Exception as e:
    print(">Error Loading YTD , MAKE SURE YOU HAVE ACTIVE INTERNET :",e)

    if (input(">Press Q to quit :") == "Q"):
        print(">BYE.")
    else:
        print(">BYE.")