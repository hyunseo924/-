#1
f=open('programming_class.txt',"wt")
f.write(
""",student no.,name,midterm,final,attendance,homework,total sum,grade,,
,87530101,Kim TM,67,70,20,17.5,78.6,,,
,87530102,Ham HC,62,70,20,18.1,77.7,,,
,87530105,Cho HR,47,43,18,17.6,62.6,,,
,87530107,Lee MY,25,18,20,18.4,51.3,,,
,87530108,Kim TY,65,36,20,17.6,67.9,,,
,87530112,Kwon OJ,60,49,20,17.4,70.1,,,
,87530113,Jung JW,0,0,20,4.1,24.1,,,
,87530116,Ha SJ,13,17,18,11.1,38.1,,,
,87530120,Park HM,34,36,20,18.0,59.0,,,
,87530125,Kim BJ,17,15,20,4.1,33.7,,,
,87530127,Kim YJ,83,98,20,18.3,92.6,,,
,87530128,Choi KH,85,81,20,17.4,87.2,,,
,87530129,Park JH,76,61,20,7.8,68.8,,,
,87530130,Park MJ,91,100,20,18.9,96.2,,,
,87530131,Shin BR,47,44,18,18.8,64.1,,,
,87530134,Kim MJ,50,87,20,15.0,76.1,,,
,87530137,Lee WH,92,92,20,17.4,92.6,,,
,87530138,Kwon YH,84,77,20,18.4,86.7,,,
,87530142,Kang C,70,57,20,17.5,75.6,,,
,87530148,Jung YJ,51,27,18,16.4,57.8,,,
,87530149,Park JH,54,40,20,15.9,64.1,,,
,87530150,Kang SJ,77,81,20,18.5,85.9,,,
,88530147,Jung YJ,70,62,20,14.8,74.4,,,
,88530157,Park SH,30,40,20,13.1,54.1,,,""")
f.close()
class Score:      
    def __init__(self,filename):
        self.filename=filename
        self.info={}
        score_list=[]
        f=open(filename)
        # self.info=f.readlines()
        next(f)
        for line in f:
            line_list=line.split(",")
            for i in range(3,8):
                score_list.append(float(line_list[i]))
            self.info[line_list[1], line_list[2]]=score_list
            score_list=[]
        f.close()
            
    
    def grade(self,student_no):
        for i in self.info:
            if str(student_no) == i[0]:
                self.total_sum=self.info[i][4]
        if self.total_sum>=90:
            return 'A'
        elif self.total_sum<90 and self.total_sum>=80:
            return 'B'
        elif self.total_sum<80 and self.total_sum>=70:
            return 'C'
        elif self.total_sum<70 and self.total_sum>=60:
            return 'D'
        else: return 'F'

a=Score("programming_class.txt")

#%%
#2
import json
whole_list=[]
data_dic={}
with open('prob2.dat') as f:
    for line in f:
        whole_list.append(line.rstrip().split())
    for data in whole_list:
        fdata=[
            {
                "time":float(data[1]),
                "energy":float(data[2]),
                "coordinate":{
                    "x":float(data[3]),
                    "y":float(data[4])
                    }
                }
            ]
        if data[0] in data_dic:
            data_dic[data[0]].append(fdata)
        else:
            data_dic[data[0]]=[fdata]
            print("\n")
#Json Module을 이용해 새로운 파일(prob2.json)으로 저장
with open('prob2.json','w') as g:
    json.dump(data_dic,g)
#Json 형식의 prob2.json 파일을 불러와 idNumber가 '133'인 data 5개를 print.
with open('prob2.json') as h:
    data_dic=json.load(h)        
    for i in range(1,6):
        print(data_dic['133'][i])
        


