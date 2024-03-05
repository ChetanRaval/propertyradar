import requests
from bs4 import BeautifulSoup

def scrape_listing(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Scraping the address
    address_h1 = soup.find('h1', class_='property-info-address')
    address = address_h1.text.strip() if address_h1 else 'Address not found'
    
    # Scraping the price
    price_span = soup.find('span', class_='property-price property-info__price')
    price = price_span.text.strip() if price_span else 'Price not found'
    
    # Initialize default values for features
    bedrooms = bathrooms = car_spaces = 'N/A'
    
    # Scraping features
    features_divs = soup.find_all('div', class_='View__PropertyDetail-sc-11ysrk6-0 eSRWKr')
    for feature_div in features_divs:
        feature_label = feature_div.get('aria-label', '').lower()
        feature_value = feature_div.find('p', class_='Text__Typography-sc-vzn7fr-0 kqoxux')
        feature_value_text = feature_value.text.strip() if feature_value else 'N/A'

        if 'bedroom' in feature_label:
            bedrooms = feature_value_text
        elif 'bathroom' in feature_label:
            bathrooms = feature_value_text
        elif 'parking space' in feature_label:
            car_spaces = feature_value_text


    return response.content
    # return {
    #     'address': address,
    #     'price': price,
    #     'bedrooms': bedrooms,
    #     'bathrooms': bathrooms,
    #     'car_spaces': car_spaces
    # }




# Testing
if __name__ == '__main__':
    test_urls = [
        "https://www.realestate.com.au/property-apartment-vic-fitzroy+north-438663632",
        "https://www.realestate.com.au/property-townhouse-qld-mount+gravatt+east-436393092",
    ]
    for url in test_urls:
        data = scrape_listing(url)
        print(data)