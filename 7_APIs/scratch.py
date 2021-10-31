
# %%
from stackapi import StackAPI
SITE = StackAPI("stackoverflow")
SITE.page_size = 10
SITE.max_pages = 1
posts = SITE.fetch('posts', fromdate=1633996800, todate=1634083200, sort='votes', order='desc')
posts
for n in range(len(posts['items'])):
    print(posts['items'][n]['score'])
# %%
import requests
from pprint import pprint
data = {
    "site": 'stackoverflow',
    "fromdate": '1633996800',
    "todate": '1634083200',
    "order": 'desc',
    "sort": 'votes',
    "pagesize": '10'
}
url = "http://api.stackexchange.com/2.3/posts"
r = requests.get(url, params=data).json()
pprint(r)
for n in range(len(r['items'])):
    print(f"Post Score: {r['items'][n]['score']}")
# %%
import requests

url = "https://soundcloud.com/morseaudio/morse-mix-023-lund/likes"
r = requests.get(url).content
print(r)
# %%
