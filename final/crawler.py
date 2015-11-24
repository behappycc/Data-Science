import requests
from bs4 import BeautifulSoup

'''
#taobao
res = requests.get("http://tw.taobao.com/product/%E5%A4%9A%E6%A8%A3%E5%B1%8B-%E8%91%AB%E8%98%86-%E4%BF%9D%E6%BA%AB%E6%9D%AF.htm")
soup = BeautifulSoup(res.text)
for item in soup.select('.item'):
    print item.select('strong')[0].text, item.select('.title')[0].text.strip(), item.select('.J_NickPopup')[0].text
'''

#ptt food
res = requests.get('https://www.ptt.cc/bbs/Food/index.html', verify = False)
soup = BeautifulSoup(res.text)
for entry in soup.select('.r-ent'):
    print  entry.select('.date')[0].text, entry.select('.author')[0].text, entry.select('.title')[0].text

'''
#ptt Gossiping
payload = {
    'from':'/bbs/Gossiping/index.html',
    'yes':'yes'
}

rs = requests.session()
res = rs.post('https://www.ptt.cc/ask/over18', verify = False, data = payload)
res = rs.get('https://www.ptt.cc/bbs/Gossiping/index.html', verify = False)
soup = BeautifulSoup(res.text)
for entry in soup.select('.r-ent'):
    print entry.select('.date')[0].text, entry.select('.author')[0].text, entry.select('.title')[0].text  
'''