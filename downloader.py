
import pafy
import progressbar
import urllib.request

class MyProgressBar():
    def __init__(self):
        self.pbar = None

    def __call__(self, block_num, block_size, total_size):
        if not self.pbar:
            self.pbar=progressbar.ProgressBar(maxval=total_size)
        downloaded = block_num * block_size
        self.pbar.start()
        if downloaded < total_size:
            self.pbar.update(downloaded)
        else:
            self.pbar.finish()


def download(y_url, file_name="temp/tempfile.webm"):
    vid = pafy.new(y_url)
    aud = min(vid.audiostreams, key=lambda s: s.get_filesize())
    # aud.download()
    url = aud.url
    try:
        urllib.request.urlretrieve(url, file_name, MyProgressBar())
    except:
        urllib.request.urlretrieve(url, file_name)

def getFileSize(vidID):
    "min file size in MB for a videoID"
    f = 10**-6
    return round(f*min(s.get_filesize() for s in pafy.new(vidID).audiostreams), 3)

if __name__=='__main__':
    download("https://youtube.com/watch?v=RzoO756PvL8")
