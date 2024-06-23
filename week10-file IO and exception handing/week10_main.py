from week10_prob1 import Score
class instance:
    def __init__(self,filename):
        self.filename=filename
        O=Score(filename)
        
        g=open('programming_grade.txt','wt')
        g.write("student no. \t\t name \t\t midterm \t\t final\t\t\tattendance\t\thomework\t\ttotal sum\t\tgrade \n")
        for i in O.info:
            g.write("{0:<8} \t\t {1:<8} \t\t {2:<8} \t\t {3:<8} \t\t {4:<8} \t\t {5:<8} \t\t {6:<8} \t\t {7:<8}\n".format(i[0],i[1],O.info[i][0],O.info[i][1],O.info[i][2],O.info[i][3],O.info[i][4],O.grade(i[0])))
        g.close()
        
A=instance('programming_class.txt')
#%%
