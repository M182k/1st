import  requests 
import MySQL.db
from bs4 import Beautifulsoup
import pandas
import argparse
import connect
oyo_url = "https://www.oyorooms.com/hostels-in-bangalore/?page="
page_num_Max=3

db= MySQLdb.connect(hotel address,hotel price, hotel _rating,amenities_list )
cur=db.cursor()
cut.execute("use scraping")

for page_num in range (1,page_num_Max):
req=requests.get(oyo_url)
Content=req.content 

    Soup=Beautifulsoup(content ,"html.parser")
all_hostel = soup.find_all("div", { "class": "listingHotelcardwrapper"} )
scrapped_info_list = [ ]


for hotel in all hostels:
      hotel_name = hotel.find("h3", {"listingHotelDescription_hotelName"}).text
      hotel_address= hotel.find("span",  {" i temprop": " stretAddress"}).text
      hotel_price = hotel.find("span",{ "class ": "listingprice_finalprice"}).text
     try:
     hotel_rating = hotel.find("span",{"class": "hotelrating_ratingsummer"}).text
     except AttributeError:
    pass

parent_amenities_element = hotel.find ("div",{"class": "amentitywarpper"})
amenties_list = [ ]
for amenity in parent_amenities_element. find_all("div",{"class":"amenitywrapper_amenity"}):

scrapped_info_list.append(hotel_dict)

dataframe = pandas. Dataframe(scrapped_info_list)
connect.get_hotel_info(args.dbname)
cur.close( )
db.close( )
