import config
import requests
def abusedb(ip = '',code = '',comm = ''):
    # Defining the api-endpoint
    print('ip: ' + ip + ' code=' + code + ' comm: ' + comm )
    url = 'https://api.abuseipdb.com/api/v2/report'

    # String holding parameters to pass in json format
    params = {
        'ip': ip,
        'categories': code,
        'comment': comm
    }

    headers = {
        'Accept': 'application/json',
        'Key': config.abusekey
    }

    response = requests.request(method='POST', url=url, headers=headers, params=params)
    for responsee in response:
        print(responsee)
