from urllib.request import urlopen
import json
import pandas as pd

df = pd.read_excel(r'./coins.xlsx')
for i,item in df.iterrows():
    print(i)
    res = urlopen('https://disqus.com/api/3.0/threads/listPostsThreaded?limit=50'
                  '&thread=%d'%item['thread']+'&forum=etherscan&order=popular&cursor=1%3A0%3A0&mode=2&api_key=E8Uh5l5fHZ6'
                  'gD8U3KycjAIAk46f68Zw7C6eW8WSjZvCLXebZ7p0r1yrYDrLilk2F').read().decode('utf-8')
    content = json.loads(res)
    with open("./json/%s.json"%item['name'],'w',encoding='utf-8')as f:
        json.dump(content,f)
