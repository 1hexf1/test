import requests
from bs4 import BeautifulSoup
import pandas as pd
url = "https://iftp.chinamoney.com.cn/english/bdInfo/"
response = requests.get(url)
web_content = response.text
soup = BeautifulSoup(web_content, 'html.parser')
table = soup.find('table')
headers = [header.text for header in table.find_all('th')]
rows = table.find_all('tr')

data = []
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele])
df = pd.DataFrame(data, columns=headers)

filtered_df = df[(df['Bond Type'] == 'Treasury Bond') & (df['Issue Date'].str.contains('2023'))]
filtered_df.to_csv('file.csv', index=False)
