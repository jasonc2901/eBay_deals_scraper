from bs4 import BeautifulSoup
import requests

def GetDeals():

    print("Getting Todays Deals from eBay...")

    #requests the data from eBay and parses it using BeautifulSoup4
    url = 'https://www.ebay.co.uk/deals?_trkparms=pageci%3Afc480ad1-d01d-11ea-812f-74dbd180e6ef%7Cparentrq%3A90e4c7d71730ad4ea1bd5802ffee3d4c%7Ciid%3A1'
    request = requests.get(url)
    response = BeautifulSoup(request.content, 'html.parser')

    #retrives the deals from the html
    sections_container = response.find_all('div', {'class': 'col'})
    
    deals = []
    #only add the 18 relevant deals to list
    for i in range (0,18):
        deals.append(sections_container[i])
        

    #initialize empty list for all deals
    all_deals = []

    #find the title, price, img and url for each deal
    for deal in deals:
        title = deal.find('h3')
        price = deal.find('span', {'class' : 'first'})
        img_wrapper = deal.find('div', class_='dne-itemtile-imagewrapper')
        img_url = img_wrapper.find('a', {'tabindex' : -1})
        img = img_url.find('img')
        url = str(img).split("src=")
        trimmed = url[1].split("/>")
        final = trimmed[0]

        product_url = deal.find('a')
        product_url_split = str(product_url).split('<a href="')
        final_url = str(product_url_split[1]).split('"')

        #create deal dictionary that can be stored as json format
        deal_object = {
            "deal_title": title.text,
            "deal_price": price.text,
            "deal_img": final.strip().replace('"',""),
            "deal_url": final_url[0].strip()
        }

        #add the dictionary to the all deals list
        all_deals.append(deal_object)

    #return the list
    return all_deals
        