import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datetime import datetime
#%%2.A
datas=pd.read_csv('passenger_register.csv')
date_counts=datas['Registered'].value_counts().sort_index() #Registered column의 values의 빈도를 정리
cum_counts=date_counts.cumsum() #cumsum(): 앞 values을 누적하여 반환한다.
dates=[]
for idx in date_counts.index:
    ii=datetime.strptime(idx,'%m-%d-%Y') 
    index=ii.strftime('%Y-%m-%d') #month-date-year을 year=month-date순으로 바꿈. 
    dates.append(index)
plt.style.use('seaborn-v0_8')
f,ax=plt.subplots(2,1)
ax[0].plot(dates,date_counts)
ax[1].plot(dates,cum_counts)
f.autofmt_xdate()
#%%2.B
fdatas=datas[datas['Gender']=='female']['Registered'].value_counts().sort_index()
mdatas=datas[datas['Gender']=='male']['Registered'].value_counts().sort_index()
f,ax=plt.subplots()
ax.plot(dates,fdatas,c='green')
ax.plot(dates,mdatas,c='orange');
ax.legend(['female','male']);
ax.set_xlabel('Dates')
ax.set_ylabel('Counts')
f.autofmt_xdate()
ax.fill_between(dates,fdatas,mdatas,facecolor='blue',alpha=0.1)
plt.show(block=False)
#%%2.C
datas_s=pd.DataFrame(datas['Survived']).value_counts().sort_index() #0=사망, 1=생존
fdatas_s=datas[datas['Gender']=='female']['Survived'].value_counts().sort_index() 
mdatas_s=datas[datas['Gender']=='male']['Survived'].value_counts().sort_index()
x=['female','male']
g,ax=plt.subplots(1,2)
ax[0].bar(['Not Survived','Survived'],[datas_s.iloc[0],datas_s.iloc[1]],color=['red','yellow'])
ax[1].bar(x,[fdatas_s[0],mdatas_s[0]],label='Not Survived',color='red',width=0.5)
ax[1].bar(x,[fdatas_s[1],mdatas_s[1]],bottom=[fdatas_s[0],mdatas_s[0]],label='Survived',color='yellow',width=0.5)
ax[1].legend(loc='best',fontsize=10)
plt.show()
#%% problem 2
import requests
from plotly import offline
url = 'https://api.github.com/search/repositories?q=language:java+created:<2023-01-01&sort=stars'
headers= {'Accept': 'application/vnd.github.v3+json'}
r=requests.get(url,headers=headers)
print(f"Staus code:{r.status_code}")
#
response_dict=r.json()
repo_dicts=response_dict['items'] 
stars, names=[],[]

for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

plt.figure()
g,ax=plt.subplots()
ax.bar(names,stars)
ax.set_xlabel("Stars")
ax.set_ylabel("Repository")
ax.set_title("Most-Starred Java Projects on GitHub")
g.autofmt_xdate()

