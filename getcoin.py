from urllib.request import urlopen
import json
import pandas as pd
import requests

df = pd.read_excel(r'./coins.xlsx')

# file = open(r'./coins.xlsx', 'rb')
# print(file.read().decode('utf8'))

for i, item in df.iterrows():

    print("*")
    print(item['THREAD'])
    print("*")

    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Cookie': 'disqus_unique=6cmcu223okgo89; G_ENABLED_IDPS=google; __hstc=40641725.460571c47275a01dfd57daefaf98b181.1551885197102.1551885197102.1551885197102.1; hubspotutk=460571c47275a01dfd57daefaf98b181; _ga=GA1.2.1525015291.1551885555; intercom-id-x2byp8hg=c381ffed-d67b-40ed-9729-5c98d2ca9b58; csrftoken=TPiPcbzXJpS4hCmY8cItqhKEpfcjr6Eh; __jid=1k3l56envhjip',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Host': 'disqus.com',
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
    }
    #
    #
    # res = requests.get('https://disqus.com/api/3.0/threads/listPostsThreaded?limit=50&thread=%d'
    #                    %item['THREAD']+'&forum=etherscan&order=popular&cursor=1%3A0%3A0&mode=2&api_key=E8Uh5l5fHZ6'
    #                 'gD8U3KycjAIAk46f68Zw7C6eW8WSjZvCLXebZ7p0r1yrYDrLilk2F', headers = header)
    # print(res)

    res = urlopen('https://disqus.com/api/3.0/threads/listPostsThreaded?limit=50'
                  '&thread=%d'%item['THREAD']+'&forum=etherscan&order=popular&cursor=1%3A0%3A0&mode=2&api_key=E8Uh5l5fHZ6'
                  'gD8U3KycjAIAk46f68Zw7C6eW8WSjZvCLXebZ7p0r1yrYDrLilk2F').read().decode('utf-8')
    print(res)

    content = json.loads(res)
    print(content)

    with open("./json/%s.json" %item['COIN'],'w+',encoding='utf-8')as f:
        json.dump(content,f)
