#%%
#1번
def order_pizza(factor, *toppings):
    pizza_dic={}
    for i in toppings:
        pizza_dic[i]=factor
    return pizza_dic

def change_order(pizza, **toppings):
    for key in toppings.keys():
        pizza[key]=toppings[key]
#%%
#2번
import copy
patients = [[176, 75,'Moebius', (0.8, 1.0), 'A', 39],
 [185, 80,'Riemann', (0.2, 0.3), 'B', 39],
 [176, 72,'Maxwell', (0.9, 1.0), 'O', 38],
 [178, 72,'Lagrange', (0.5, 0.6), 'AB', 37],
 [175, 67,'Laplace', (1.0, 1.1), 'O', 36]]
def change_name(patients):
    new_name=''
    new_patients=copy.deepcopy(patients)
    for patient in new_patients:
        new_name=patient[2][:3]+'_'+patient[2][0]
        patient[2]=new_name
    print(new_patients)
        
def change_otype(patients):
    new_patients=copy.deepcopy(patients)
    change_lam= lambda: (patient[3][0]+patient[3][1])/2
    for patient in new_patients:
        if patient[4] == 'O':
            patient.append(change_lam())
    print(new_patients)
#%% coordinates[column][row]
#3번
coordinates=[[0, 0, 0, 0],
[0, 0, 0, 0],
[0, 0, 0, 0],
[0, 0, 0, 0]]
def print_coordinates(coordinates):
    for i in range(4):
        print(f"{coordinates[i]}")
def move_robot(coordinates,coord,*move):
    row=coord[0]
    column=coord[1]
    for move_num in move:
        if move_num == 0:
            if column-1 in [0,1,2,3]:
                column -= 1
                coordinates[column][row] += 1
        elif move_num == 1:
            if row+1 in [0,1,2,3]:
                row += 1
                coordinates[column][row] += 1
        elif move_num == 2:
            if column+1 in [0,1,2,3]:
                column += 1
                coordinates[column][row] += 1
        elif move_num == 3:
            if row-1 in [0,1,2,3]:
                row -= 1
                coordinates[column][row] += 1
        else:
            coordinates[column][row] += move_num
    print_coordinates(coordinates)
#%%
#4번
import week07_package as w7

'''order_pizza를 이용하여 새로운 pizza를 만들고 
두 개 이상의 topping 개수를 변경하여 출력하시오.'''
pizza1=w7.order_pizza(4, 'tomato','shrimp','cheese','salame')
w7.change_order(pizza1, shrimp=6,cheese=2)
print(pizza1)

'''change_name(patients), change_otype(patients)를 수행하고 
patients를 출력하시오.'''
patients = [[176, 75,'Moebius', (0.8, 1.0), 'A', 39],
 [185, 80,'Riemann', (0.2, 0.3), 'B', 39],
 [176, 72,'Maxwell', (0.9, 1.0), 'O', 38],
 [178, 72,'Lagrange', (0.5, 0.6), 'AB', 37],
 [175, 67,'Laplace', (1.0, 1.1), 'O', 36]]
w7.change_name(patients)
w7.change_otype(patients)


'''move_robot(coordinates, (1,1), 1,5,3,2,1,4,0,0,2) 의 결과를 출력하시오.'''
coordinates=[[0, 0, 0, 0], 
[0, 0, 0, 0],
[0, 0, 0, 0],
[0, 0, 0, 0]]

w7.move_robot(coordinates, (1,1), 1,5,3,2,1,4,0,0,2)


