import requests
def get_info_by_ip(ip='156.202.176.194'):
    try:
        resours = requests.get(url=f'http://ip-api.com/json/{ip}').json()
        #print(resours)
        info={
            '[IP]': resours.get('query'),
            '[Int prov]': resours.get('isp'),
            '[Org]': resours.get('org'),
            '[Country]': resours.get('country'),
            '[Region Name]': resours.get('regionName'),
            '[City]': resours.get('city'),
            '[ZIP]': resours.get('zip'),
            '[Lat]': resours.get('lat'),
            '[Lon]': resours.get('lon'),
        }
        for k, v in info.items():
            print(f'{k}: {v}')
    except requests.exceptions.ConnectionError:
        print('please check your connection')


get_info_by_ip()
get_info_by_ip('154.191.16.63')