from bs4 import BeautifulSoup
import requests
import re
headers = {
    'user-aent':'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0'
}
cid = "6204862414620005667"
for i in range(0,100):
    print("第"+str(i+1)+"页的评论")
    pat1 = "'content':'(.*?)"
    url = 'https://video.coral.qq.com/varticle/1622846193/comment/v2?' \
      'callback=_varticle1622846193commentv2&orinum=10&oriorder=o&' \
      'pageflag=1&cursor='+str(cid)+'&scorecursor=0&orirepnum=2&reporder=o&reppageflag=1&source=132&_=1587211708457'

    certfile ="C:\\Users\\10854\Desktop\\2.crt"

    r = requests.get(url, headers=headers, verify=certfile)
    r.raise_for_status()
    r.encoding=r.apparent_encoding
#print(r.text)
    comment = re.compile(pat1, re.S).findall(r)
    for item in comment:
        print(str(item))
        print("------------------")
        pat2 = "'last':(.*?)"
        cid = re.compile(pat2, re.S).findall(r)[0]
