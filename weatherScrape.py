#June 15,2022
#Author: Andrew N

#Purpose: A program that contains a list of cities that we can abstract data reagrding the weather conditions.
#This data will be saved to CSV files in a directory for each given city
#The intention is for this program to be run continuously with whatever interval the user would like

#Useful tutorials realted to Beautiful Soup:
#tutorial at https://www.geeksforgeeks.org/how-to-extract-weather-data-from-google-in-python/
#https://www.thepythoncode.com/article/extract-weather-data-python

from bs4 import BeautifulSoup as bs
import requests

list=['Olympia,WA','Seattle,WA','Spokane,WA','Kalspell,MT','Shelby,MT','Malta,MT',None,None,None,None,None,None,None,None,None,None,None,None,
'Bangor,ME',None,None,None,None,None,None,'Duluth,MN','Bemidji,MN','Fargo,ND','Bismark,ND','Medora,ND','Miles City,MT','White Sulphur Springs,MT',
'Missoula,MT','Grangerville,ID','Pendleton,OR','Salem,OR','Crescent City,CA','Medford,OR','Lakeview,OR','Boise,ID','Idaho Falls,ID','Cody,WY',
'Buffalo,WY','Rapid City,SD','Wall,SD','Watertown,SD','Minneapolis,MN','Eau Claire,WI','Appleton,WI','Gaylord,MI',None,None,'Watertown,NY',
'Burlington,VT','Manchester,NH','New York,NY','Binghampton,NY','Buffalo,NY','Detroit,MI','Kalamazoo,MI','Rockford,IL','Dubuque,IA','Fort Dodge,IA',
'Sioux City,SD','Valentine,NE','Scottsbluff,NE','Casper,WY','Rockspring,WY','Salt Lake City,UT','Elko,NV','Winnemucca,NV','Redding,CA','Eureka,CA',
'San Fransisco,CA','Sacramento,CA','Fallon Station,NV','Ely,NV','Provo,UT','Grand Junction,CO','Aspen,CO','Sterling,CO','McCook,NE','Lincoln,NE',
'Omaha,NE','Iowa City,IA','Bloomington,IL','Indianapolis,IN','Columbus,OH','Pittsburgh,PA','Baltimore,MD','Philidelphia,PA','Norfolk,VA','Richmond,VA',
'Roanoke,VA','Lexington,KY','Louisville,KY','Saint Louis,MO','Columbia,MO','Kansas City, MO','Wichita,KS','Dodge City,KS','Trinidad,CO',
'Colorado Springs,CO','Durango,CO','Moab,UT','St. George,UT','Las Vegas,NV','Bakersfield,CA','San Luis Obispo,CA','Los Angeles, CA','Lake Havasu City,AZ',
'Flagstaff,AZ','Winslow,AZ','Albuquerque,NM','Santa Fe,NM','Amarillo,TX','Woodward,OK','Oklahoma City,OK','Fayatteville,AR','Branson,MO','Memphis,TN',
'Nashville,TN','Knoxville,TN','Asheville,NC','Durham,NC','Greenville,NC','Charleston,SC','Augusta,GA','Atlanta,GA','Birmingham,AL','Oxford,MS',
'Pine Bluff,AR','Texarkana,TX','Dallas,TX','Wichita Falls,TX','Lubbock,TX','Carlsbad,NM','La Cruces,NM','Tucson,AZ','Phoenix,AZ','San Diego,CA',
'Ciudad Juarez,Mexico','Odessa,TX','Abilene,TX','Waco,TX','Shreveport,LA','Monroe,LA','Jackson,MS','Montgomery,AL','Columbus,GA','Savannah,GA',
'Orlando,FL',None,None,'New Orleans,LA','Lafayette,LA','Houston,TX','Austin,TX','San Antonio,TX','Nuevo Laredo,Mexico','Corpus Christi,TX',
None,None,None,None,None,None,'Miami,FL']

#to find user agent, type 'My User Agent' into Google
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
# US english
LANGUAGE = "en-US,en;q=0.5"

def get_weather_data(city):
    #create sessions
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE
    
    #establish url
    url = "https://www.google.com/search?q="+"weather"+city
    html = session.get(url)
    soup = bs(html.text, "html.parser")

    # results
    result = {}
    #result['day and time'] = soup.find("div", attrs={"id": "wob_dts"}).text
    #dayAndtime = soup.find("div", attrs={"id": "wob_dts"}).text
    #dAtSplit = dayAndtime.split(' ')
    #result['time'] = dAtSplit[1]+dAtSplit[2]
    #result['location'] = soup.find("div", attrs={"id": "wob_loc"}).text
    result['temperature'] = soup.find("span", attrs={"id": "wob_tm"}).text
    #result['humidity'] = soup.find("span", attrs={"id": "wob_hm"}).text
    #result['wind'] = soup.find("span", attrs={"id": "wob_ws"}).text
    #result['precipitation'] = soup.find("span", attrs={"id": "wob_pp"}).text
    #result['sky condition'] = soup.find("span", attrs={"id": "wob_dc"}).text
    return result

temp=[]
for i in range(len(list)):
    if list[i] != None:
        #print(list[i])
        dataNow = get_weather_data(list[i])
        #print(dataNow)
        temp.append(dataNow)
print(temp)
print(len(temp))
print()
