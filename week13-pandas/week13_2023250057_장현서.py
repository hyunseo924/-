import numpy as np
import pandas as pd
#%% problem 1
#1-B
df=pd.read_csv("passenger.csv")
#1-C
df.info()
#1-D
print(f"1-D: \n{df[:10]}\n")
#1-E
print(f"index:{df.index}\n")
print(f"columns:\n{df.columns}\n")
#2-A
df_nw=df.drop("SibSp",axis=1)
df_new=df_nw.drop("Parch",axis=1)
#2-B
df_female=df_new[df_new['Gender'] == 'female']
#2-C
df_surv_wn=df_female[df_female['Survived']==1]
#2-D
ratio1=len(df_surv_wn)/len(df_female)
print("%0.2f of women survived"%ratio1)
#2-E
df_male=df_new[df_new['Gender'] ==  'male']
df_surv_male=df_male[df_male['Survived'] == 1]
ratio2=1-len(df_surv_male)/len(df_male)
print("%0.2f of men could not survive"%ratio2)
#2-F
p1=df[df['Pclass']==1]
p2=df[df['Pclass']==2]
p3=df[df['Pclass']==3]
#2-G
p1=p1.sort_values(by='Age')
p2=p2.sort_values(by='Age')
p3=p3.sort_values(by='Age')

#2-H
print("Average age of grade1: {0:.2f} +/- {1:.2f}".format(p1['Age'].mean(),p1['Age'].std()))
print("Average age of grade2: {0:.2f} +/- {1:.2f}".format(p2['Age'].mean(),p2['Age'].std()))
print("Average age of grade3: {0:.2f} +/- {1:.2f}".format(p3['Age'].mean(),p3['Age'].std()))
#2-I
Age=pd.concat([p1['Age'],p2['Age'],p3['Age']],axis=0).reset_index(drop=True)
Embarked=pd.concat([p1['Embarked'],p2['Embarked'],p3['Embarked']],axis=0).reset_index(drop=True)
d={"Age":Age,"Embarked":Embarked}
Age_Embarked=pd.DataFrame(d)
#Age_Embarked=pd.DataFrame(d),[i for i in range(len(Age))]
#2-J
new_Age_Embarked=Age_Embarked.dropna(subset=['Age'])
print(new_Age_Embarked)
#%%
#3-A
import matplotlib.pyplot as plt
xG=np.array(['female','male'])
yGS=np.array([len(df_surv_wn),len(df_surv_male)])
yGN=np.array([len(df_female)-len(df_surv_wn),len(df_male)-len(df_surv_male)])
plt.figure()
plt.plot(xG,yGS)
plt.plot(xG,yGN);
plt.legend(['Survived','Not Survived']);
plt.title('Survival by Gender')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.show(block=False)
plt.close()
#3-B
xC=np.array(['1','2','3'])
yTS=np.array([len(p1[p1['Survived']==1]),len(p2[p2['Survived']==1]),len(p3[p3['Survived']==1])])
yTN=np.array([len(p1[p1['Survived']==0]),len(p2[p2['Survived']==0]),len(p3[p3['Survived']==0])])
plt.figure()
plt.plot(xC,yTS)
plt.plot(xC,yTN);
plt.legend(['Survived','Not Survived']);
plt.title('Survival by Passenger Class')
plt.xlabel('Ticket Class')
plt.ylabel('Count')
plt.show(block=False)
plt.close()
#%%
#4
new_Age_Embarked.to_excel('result.xlsx')
#%% problem2
#1
df=pd.read_csv('Ba133_for_Ehisto.csv')
#2
df['E']=(7.42344)*(df['X-']+df['X+']+df['Y-']+df['Y+'])-147632.12 
#3
df2=df[(df['E']>0) & (df['E']<10**6)]
#4 
ehist_list=[]
df_int=(df2['E']/1000).round()
for i in range(1001):
    ehist_list.append(len((df_int[df_int.astype(int)==i])))
ehist=pd.Series(ehist_list)
#%%5
plt.figure()
plt.plot(ehist)
plt.xlabel('Energy(KeV)')
plt.ylabel('Counts')
plt.title('Energy Histogram of Ba-133')
plt.show(block=False)
plt.close()