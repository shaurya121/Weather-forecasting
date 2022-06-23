import sys
import requests
#resp=requests.get(f'https://wttr.in/{sys.argv[1].replace(" ", "+")}')
city="Etawah"
url="https://wttr.in/{}".format(city)
res=requests.get(url)
print(res.text)
                
