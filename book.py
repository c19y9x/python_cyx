import requests, os,bs4,re

bookFile = open('nitian.txt','w',encoding='utf-8') # 打开txt文件
url = 'https://www.nitianxieshen.com/wangushendi/' # 目录页
link_list = requests.get(url)
link_list.encoding='utf-8'
soup = bs4.BeautifulSoup(link_list.text,features='html.parser')
zjms = soup.select('.line3 a')

for zjm in zjms:
    print('正在下载%s...'%(zjm.get('title')))
    link = requests.get('https://www.nitianxieshen.com'+zjm.get('href'))
    link.encoding='utf-8'
    link.raise_for_status()
    soup1 = bs4.BeautifulSoup(link.text,features='html.parser')
    title =  soup1.select('h1')
    content = soup1.select('#content p')
    bookFile.write(title[0].text+'\n')
    for p1 in content[1:]:   
        p11 = re.sub('<p>','    ',str(p1))
        p11 = re.sub('</p>','\n',p11)
        bookFile.write(p11)
bookFile.close()
