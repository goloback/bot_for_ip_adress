import requests
def get_info_by_ip(ip='156.202.176.194'):
    try:
        resours = requests.get(url=f'http://ip-api.com/json/{ip}').json()
        print(resours)
    except requests.exceptions.ConnectionError:
        print('please check your connection')


get_info_by_ip()
get_info_by_ip('154.191.16.63')