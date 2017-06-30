import requests
import bs4

res = requests.get('http://hzws.selco.info/prototype.php?type=new-arrivals&lib=nor&collect=Bnewnf,Bnewmys,Bnewf,Bnewsf&days=14&key=7a8adfa9aydfa999997af')
res.raise_for_status()

# this specifically parses it as XML
soup = bs4.BeautifulSoup(res.text, "lxml-xml")

# these specify that we want these tags from the xml
img = soup.select('ImageLink') 
link = soup.select('CatalogLink')


# runs a loop to retreive the text needed for img1 and link1
# it either takes the first 14 items from the XML or however 
# many there are if it's fewer
length = min([14, len(img)])
for i in range(length):
    img1 = img[i].getText()
    link1 = link[i].getText()

    # replaces SC.GIF with LC.GIF
    import re
    gifreplace = re.compile(r'SC.GIF')
    img1 = gifreplace.sub('LC.GIF', str(img1))
    # prints the html in the correct format
    if img1 != '' and link1 != '':
        print('<div>' + link1 + img1 + '</a></div>')
        
   
