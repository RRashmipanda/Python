# you are given two list and you need to find total of each list
def calculate_total(exp): # <-- exp -argument
    total = 0
    for item in exp:
        total = total+item
    return total    # return value

tom_exp_list = [3000,2000,1000]
jerry_exp_list = [700,200,100]

toms_total = calculate_total(tom_exp_list)
jerryss_total = calculate_total(jerry_exp_list)

print("Toms total exp is", toms_total)
print("jerrys total exp is", jerryss_total)

