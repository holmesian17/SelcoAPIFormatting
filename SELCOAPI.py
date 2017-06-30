# could python be used to pull the data from the book API
# and then could spit it into the format that I need to
# copy and paste into the book scroll?
# loop string elements [0:14] or however many we're going for
# and have it return the url, img src, and title(as the ID)
# have it format that like we need to paste it into
# the scroll box, then we can just change it out all at once
# -------------------------------------------------------------
# dowload the html for the page
# have it return either top 14 results or the min
# copy the img src results and links and titles into
# the format needed for the book scroll
# copy that to the clipboard

import requests
import sys
import webbrowser
import bs4

res = requests.get('http://hzws.selco.info/prototype.php?type=new-arrivals&lib=nor&collect=Bnewnf,Bnewmys,Bnewf,Bnewsf&days=14&key=7a8adfa9aydfa999997af')
res.raise_for_status()

    # Retrieve top search result links
soup = bs4.BeautifulSoup(res.text, "lxml-xml")

    # Open a browser tab for each result
img = soup.select('ImageLink') 
link = soup.select('CatalogLink')

    #for i in range(13):

length = min([14, len(img)])
for i in range(length):
    img1 = img[i].getText()
    link1 = link[i].getText()

    if img1 != '' and link1 != '':
        print('<div>' + link1 + img1 + '</a></div>')

#TODO: use regular expressions to find and replace the SC.GIF with LC.GIF    
