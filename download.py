from tqdm import tqdm #this is the module which creates the progress bar.
import requests #install requests using pip3
import time #use time so you watch the progress take place.

#define the chunk size you want to download at a time.
chunk_size=1024

#url from which you want to download from.
url="http://www.pdf995.com/samples/pdf.pdf"

r=requests.get(url,stream=True)

#define total size which will be the content length
total_size=int(r.headers['content-length'])

#create a file where to save the download
with open('python.pdf','wb') as f:
    #loop to get the download using tqdm. remember this will only work in python3.
    for data in tqdm(iterable=r.iter_content(chunk_size=chunk_size),total=total_size/chunk_size, unit ='KB'):
        f.write(data)
        time.sleep(0.01)

print('Download complete')


