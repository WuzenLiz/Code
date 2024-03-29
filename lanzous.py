#coding=utf-8
from bs4 import BeautifulSoup
import requests
import re
import json

#蓝奏云分享文件链接地址
url = 'https://www.lanzous.com/i8nfa7i'

#header头，注意那个referer必须要与上面文件分享地址url相同
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.3',
    'referer': url
}

# 获取分享页面html文件
res = requests.get(url,headers=headers)

# 引入BeautifulSoup库对html进行处理，获取iframe中的出现的js文件
soup = BeautifulSoup(res.text,'html.parser')
url2 = 'https://www.lanzous.com/'+soup.find('iframe')['src']
res2 = requests.get(url2,headers=headers)

# 正则提取请求三个参数
a = re.findall(r'var a = \'([\w]+?)\';',res2.text)
params = re.findall(r'var [\w]{6} = \'([\w]+?)\';',res2.text)

# 请求下载地址
url3 = 'https://www.lanzous.com/ajaxm.php'
data = {
    'action':'down_process',
    'file_id':params[0],
    't':params[1],
    'k':params[2],
}
res3 = requests.post(url3,headers=headers,data=data)
res3 = json.loads(res3.content)

# 请求最终重定向地址
url4 = res3['dom']+'/file/'+res3['url']
headers2 = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
}
res4 = requests.head(url4, headers=headers2)
print(res4.headers['Location'])