
import search
import downloader
import subprocess
import store
import sys

while True:
    query = input("\n\nWhat do you want to listen to today. Type 'done' if you are done\n")
    if query in ['done', 'Done', 'DONE', '-1']:
        break

    results = store.history(query)
    if len(results)>0:
        print("\n\nWe already have %s downloaded files similar to that\n" %len(results))
        for i, title in enumerate(results):
            print("[%s] %s" %(i, title))
        print("\nChoose which one you want to listen to. Type -1 to reject all and search on YT\n")
        choice = int(input())
        if choice!=-1:
            subprocess.call(["mplayer", "temp/"+results[choice]])
            continue

    results = search.request(query)
    print("\n\nHere is what came up\n\n\n")
    print("____________________TITLE___________________:__SIZE__\n")
    # print(results)
    for i, (vid, title) in enumerate(results.items()):
        print("[%s] %s: %s MB" %(i, title, downloader.getFileSize(vid)))
    print("\nChoose which one you want to download (a number from 0 to 9). Choose -1 to skip\n")
    choice = int(input())
    if choice==-1:
        continue

    vidID =list(results.keys())[choice]
    downloader.download("http://youtube.com/watch?v="+vidID)
    subprocess.call(["mplayer", "temp/tempfile.webm"])
    print("Do you want to save this\n")
    if input() in ["Y", "yes", "1", "ok", "YES"]:
        subprocess.run(["mv", "temp/tempfile.webm", "temp/"+list(results.values())[choice]+".webm"])

sys.exit("Thank You!!")
