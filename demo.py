card_no = "5610591081018250"
odd_sum = 0
double_list=[]
number = list(card_no)
for (idx, val) in enumerate(number):
    if idx % 2 !=0:                                   #odd numbers
        odd_sum += int(val)
    else:                                             #even numbers
        double_list.append(int(val)*2)


#convering list to string
double_string = ""
for x in double_list:
    double_list+= str(x)

#conerting string back to list
double_list = list(double_string)


for x in double_list:
    even_sum += int(x)

net_sum = odd_sum + even_sum
if net_sum % 10 ==0:
    print('valid card')
else:
    print('Invalid card')


