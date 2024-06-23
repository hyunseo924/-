def order_pizza(factor, *toppings):
    pizza_dic={}
    for i in toppings:
        pizza_dic[i]=factor
    return pizza_dic

def change_order(pizza, **toppings):
    for key in toppings.keys():
        pizza[key]=toppings[key]
        
def change_name(patients):
    import copy
    new_name=''
    new_patients=copy.deepcopy(patients)
    for patient in new_patients:
        new_name=patient[2][:3]+'_'+patient[2][0]
        patient[2]=new_name
    print(new_patients)
        
def change_otype(patients):
    import copy
    new_patients=copy.deepcopy(patients)
    change_lam= lambda: (patient[3][0]+patient[3][1])/2
    for patient in new_patients:
        if patient[4] == 'O':
            patient.append(change_lam())
    print(new_patients)
    
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