# -*- coding: UTF-8 -*-
import requests
import bs4
import codecs

# use this script to write markdown table

oj_url = 'http://www.bjfuacm.com/problem/'
github_url = 'https://github.com/yiran7324/bjfu-data-structure/blob/master/'
Not_Found = 0
Found = 0

"""r = requests.get(oj_url + '204')
just = bs4.BeautifulSoup(r.text, "html.parser")
a = (just.title.text).strip()
print(type(a.encode('utf-8')))
"""

for i in range(204, 304):
    g = requests.get(github_url + str(i) + '.c')
    if (g.headers['Status'] != '404 Not Found'):
        Found += 1
        r = requests.get(oj_url + str(i) + '/')
        html = bs4.BeautifulSoup(r.text, "html.parser")
        a = (html.title.text).strip()
        f = codecs.open('./file.md', 'a')

        # construct string here
        w = '| [{}]({}) | [{}]({}) |\n'.format(str(i), oj_url + str(i) + '/',
                                               a.encode('utf-8'), github_url + str(i) + '.c')
        f.write(w)
        print('success ' + str(Found) + ' No.' + str(i) + '!')
    else:
        Not_Found += 1
        print('not found ' + str(Not_Found) + 'No.' + str(i))
