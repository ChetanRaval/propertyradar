import requests
from bs4 import BeautifulSoup

def scrape_listing(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Scraping the price
    price_span = soup.find('span', class_='property-price property-info__price')
    price = price_span.text.strip() if price_span else 'Price not found'
    
    # Initialize default values
    bedrooms = bathrooms = car_spaces = 'N/A'
    
    # Scraping features
    features_divs = soup.find_all('div', class_='View__PropertyDetail-sc-11ysrk6-0 eSRWKr')
    for feature_div in features_divs:
        feature_label = feature_div.get('aria-label', '').lower()  # Use aria-label to identify the feature type
        feature_value = feature_div.find('p', class_='Text__Typography-sc-vzn7fr-0 kqoxux')
        feature_value = feature_value.text.strip() if feature_value else 'N/A'

        if 'bedroom' in feature_label:
            bedrooms = feature_value
        elif 'bathroom' in feature_label:
            bathrooms = feature_value
        elif 'parking' in feature_label:
            car_spaces = feature_value

    return {
        'price': price,
        'bedrooms': bedrooms,
        'bathrooms': bathrooms,
        'car_spaces': car_spaces
    }


# This can be done at the bottom of your scraper.py for testing purposes
if __name__ == '__main__':
    test_urls = [
        "https://www.realestate.com.au/property-apartment-vic-fitzroy+north-438663632",
        "https://www.realestate.com.au/property-townhouse-qld-mount+gravatt+east-436393092",
    ]
    for url in test_urls:
        data = scrape_listing(url)
        print(data)