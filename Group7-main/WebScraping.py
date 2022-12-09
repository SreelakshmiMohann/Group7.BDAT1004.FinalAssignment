
from urllib.request import urlopen
from bs4 import BeautifulSoup

url='https://www.emeraldwaterways.ca'
page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode("utf-8")
soup = BeautifulSoup(html, 'html.parser')
nooftours = 0


###############Tour title######################
tourtitle = []
text1 =soup.select(".tour-tile__title")
for  text in text1:
    tourtitle.append(text.get_text().strip().replace(',',' '))
    nooftours= nooftours+ 1

#############Tour subtitle####################
toursubtitle = []
text2 =soup.select(".tour-tile__subtitle")
for  text in text2:
    toursubtitle.append(text.get_text().strip().replace(',',' '))


#############Tour offer###################
touroffer = []
text3 =soup.select(".tour-tile__offers")
for  text in text3: 
  touroffer.append(text.get_text().strip().replace(',',' '))
  


#############Tour offer prefix###################
tourofferprefix = []
text4 =soup.select(".tour-tile__offers__prefix")
for  text in text4:
    tourofferprefix.append(text.get_text().strip().replace(',',' '))
  

#############Tour offer title###################
touroffertitle = []
text5 =soup.select(".tour-tile__offers__title")

for  text in text5:
    touroffertitle.append(text.get_text().strip().replace(',',' '))
    

#############Tour offer subtitle###################
touroffersubtitle = []
text6 =soup.select(".tour-tile__offers__subtitle")
for  text in text6:
    touroffersubtitle.append(text.get_text().strip().replace(',',' '))
   

#############Tour offer offers__conditions############
tourofferconditions = []
text7 =soup.select(".tour-tile__offers__conditions")
for  text in text7: 
    tourofferconditions.append(text.get_text().strip().replace(',',' '))

#############Tour offer tile__details###################
tourdurationNumber = []
text8 =soup.select(".tour-tile__duration__number")
for  text in text8:
    tourdurationNumber.append(text.get_text().strip().replace(',',' '))

tourdurationsufix = []
text9 =soup.select(".tour-tile__duration__suffix")
for  text in text9:
    tourdurationsufix.append(text.get_text().strip().replace(',',' '))

tourpriceadjustment = []
text10 =soup.select(".tour-tile__price-adjustment")
for  text in text10:
    tourpriceadjustment.append(text.get_text().strip())

tourprice = []
text10 =soup.select(".tour-tile__price__amount")
for  text in text10:
    tourprice.append(text.get_text().strip().replace('$','')) 
touroffer = []
text11 =soup.select(".tour-tile__offer")
for  text in text11:
    touroffer.append(text.get_text().strip())

f = open("cruise.csv", "w")
Titlestring="Cruise,Destination,Offer,Offer_Availability,Special,Conditions,Period,Time,Special_Price,Full_Price"
f.write(Titlestring+"\n")
for n in range(nooftours-1):
    
    tour = tourtitle[n]+ "," + toursubtitle[n] 
    tour = tour + "," + touroffer[n].replace(',','')
    tour = tour + "," + tourofferprefix[n] + ","  + touroffersubtitle[n]
    tour = tour +  "," + tourofferconditions[n]+ "," + tourdurationNumber[n]
    tour = tour + "," + tourdurationsufix[n]
    tour = tour + "," + tourprice[n].replace(',','')
   ## there are hidden characters and $
    tour = tour + "," + tourpriceadjustment[n][2:].replace(',','')
   
    f.write(tour+"\n")


f.close()
