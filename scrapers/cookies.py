import requests

url = 'https://www.realestate.com.au/property-townhouse-vic-pascoe+vale-426899822'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    # Add any other necessary headers here
}

# cookies = {
#     'name': 'value',
#     # Add your cookies here
# }

response = requests.get(url, headers=headers)
# , cookies=cookies)

print(response)
