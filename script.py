import os

# Resize a Video to Multiple Resolutions using FFmpeg

def runBash(command):
	os.system(command)

# Create a script which it will invoke FFMPEG to
# create a HLS transport stream container with one
# video you already have
def video_only():
    str = "ffmpeg -i BBB_1920×1080.mp4 -c:v h264 -f hls -hls_time 4 -hls_playlist_type event stream.m3u8"
    print(str)
    runBash(str)


#Download the bento4 tools and use them to create a MPD video file with any encryption you want. You’ll need to fragment, encrypt and dash the file.
def command():
    str = 'mp4info myvideo_1920x1080_frag.mp4'
    print(str)
    runBash(str)

def command2():
    str = 'mp4fragment --fragment-duration 40000 BBB_1920×1080.mp4 myvideo_1920x1080_frag.mp4'
    print(str)
    runBash(str)

def command3():
    str='mp4dash --mpd-name myvideo.mpd myvideo_1920x1080_frag.mp4 '
    print(str)
    runBash(str)

#script to livestream with ffmpeg
def stream_video():
    str = 'ffmpeg -re -i BBB_1920×1080.mp4 -c:v libx264 -f flv rtmp://localhost/show/stream'
    print(str)
    runBash(str)


def print_menu():
    print('''
    Parse the BBB video
                    1) Create a HLS transport stream container
                    2) Create a MPD video file
                    3) Stream Video
            ''')


def main_loop():
    try:
        print_menu()
        choice=int(input())
        if choice == 1:
            try:
                video_only()
                main_loop()
            except:
                print('Enter number, try again')
        if choice == 2:
            try:
                command()
                command2()
                command3()
                main_loop()
            except:
                print('Enter number, try again')
        if choice == 3:
            try:
                stream_video()
                main_loop()
            except:
                print('Enter number, try again')
    except ValueError:
        print("The value introduced is incorrect, enter a digit from 1-3")
        main_loop()
main_loop()
