from bs4 import BeautifulSoup
import requests

def scrape_listing(html_content):
    response = requests.get(html_content)
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Scraping the price
    price_div = soup.find('div', class_='css-1texeil')
    price = price_div.text.strip() if price_div else 'Price not found'
    
    # Initialize default values
    bedrooms = bathrooms = car_spaces = 'N/A'
    
    # Scraping features
    features_spans = soup.find_all('span', class_='css-1ie6g1l')
    for feature_span in features_spans:
        feature_type = feature_span.find('span', class_='css-9fxapx')
        if feature_type:
            feature_type_text = feature_type.text.lower()
            feature_value = feature_span.find('span', class_='css-lvv8is').text.strip() if feature_span.find('span', class_='css-lvv8is') else 'N/A'
            
            if 'bed' in feature_type_text:
                bedrooms = feature_value
            elif 'bath' in feature_type_text:
                bathrooms = feature_value
            elif 'parking' in feature_type_text:
                car_spaces = feature_value

    # Scraping property type
    property_type_span = soup.find('span', class_='css-in3yi3')
    property_type = property_type_span.text.strip() if property_type_span else 'Property type not found'

    return response.content

    # return {
    #     'price': price,
    #     'bedrooms': bedrooms,
    #     'bathrooms': bathrooms,
    #     'car_spaces': car_spaces,
    #     'property_type': property_type
    # }

# Testing
if __name__ == '__main__':
    test_urls = [
        "https://www.domain.com.au/rh11-11-beesley-street-west-end-qld-4101-16899006",
        "https://www.domain.com.au/rh06-11-beesley-street-west-end-qld-4101-16896666",
    ]
    for url in test_urls:
        data = scrape_listing(url)
        print(data)