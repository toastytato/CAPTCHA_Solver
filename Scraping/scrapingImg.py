import requests 
from bs4 import BeautifulSoup 
from PIL import Image

def getdata(url): 
    r = requests.get(url) 
    return r.text 
    
htmldata = getdata("https://www.geeksforgeeks.org/") 
soup = BeautifulSoup(htmldata, 'html.parser') 
for item in soup.find_all('img'):    
    if 'png' in item['src'] or 'jpeg' in item['src'] or 'jpg' in item['src']:
        # print(item['src'])  
        im = Image.open(requests.get(item['src'], stream=True).raw)
        #im.show()

