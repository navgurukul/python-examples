# Yeh exercise hai
# Har line of code se pehle aapko ek line mei comment mei daal kar likhna hai, ki uss line of code ka matlab kya hai
# Aap jyada comments bhi likh sakte hai, jitne jyada comments likhenge, utna aapkya fayda hoga

# calculator naam ka ek function banao jo teen argument leta ho - number_x, number_y, operation.
# number_x aur number_y mein hum humesha do integers denge aur operation mein kaunsa operation karna hai woh denge. Jaise:
# - Agar operation mein "add" diya toh number_x aur number_y ko add kar ke returna karega.
# - Agar operation mein "subtract" diya toh number_x aur number_y ko subtract kar ke return karenge
# - Agar operation mein "multiply" diya toh number_x ko number_y se multiply kar ke returna karega.
# - Agar operation mein "divide" diya toh number_x ko number_y se divide kar ke return karega
# Jaise:
# - calculator(20, 25, "add") call karne pe 45 returna karega. 45 hume 20+25 karne se milega.
# - calculator(40, 3, "subtract") call karne pe 37 return karega. 37 hume 40-3 karne se milega.
# - calculator(10, 4, "multiply") call karne pe 40 return karega. 40 hume 10*4 karne se milega.
# - calculator(40, 4, "divide") call karnse pe 10 return karega. 10 hume 40/3 karne se milega.








# function likhne ke baad, yeh kaam karne ke liye function call karo
# 24 aur 20 ko add karo
# 50 aur 60 ko multiply karo
# 80 aur 120 ko divide karo
# 90 aur 23 ko subtract karo






# Ab raw_input ka use kar ke user se 2 numbers input lo.
# Fir calculator function ko 4 baar call call kar ke inn dono numbers do add, subtract, multiply, divide karo
# aur result ko 4 alag variables mein daalo. Woh variables ka naam yeh hoga:
# *add_result* add operation ka result store karega
# *subtract_result* subtract operation ka result store karega
# *multiply_result* multiple operation ka result store karega
# *divide_result* divide operation ka result store karega
# Fir upar wale chaaron variables ko print karo







# list_change naam ka ekf function ka code likho jo 2 chaar items ki lists arguments ki tarah le aur fir unn lists
# ki woh items so same index number (kram) pe hain unko multiple kar ke ek nayi list return karvaye.
# Aapko multiple karne ke liye *calculator* function ka use karna hai. Normal tareeke se divide nahi kar sakte ho.
# Jaise agar hum function ko aise call karenge toh:
# multiple_list = list_change([5, 10, 50, 20], [2, 20, 3, 5])
# Yahan *multiple_list* ki yeh value honi chaiye:
# [10, 200, 150, 100]
# 10, 5 aur 2 ko multiple kar ke aaya, 200 10 aur 20 ko multiple kar ke, 150 50 aur 3 ko, 100 20 aur 5 ko
# Note: List pe iterate karte hue abhi ke liye aap yeh soch sakte hain ki aapko 4 items ki list hi milegi

# Hint: Neeche diye gaye code mein ek khaali list mein nayi value daalne ka code likha hai.
#       Aapko iski zaroorat padegi nayi list banane ke liye jisko aap aakhir mein return karoge.
integer_list = []
integer_list.append(10) # isse integer_list[0] pe 10 integer ki value chali jayegi
integer_list.append(221) # isse integer_list[1] pe 221 integer ki value chali jayegi
integer_list.append(121) # isse integer_list[2] pe 121 ki integer ki balue chali jayegi
print integer_list # yahan [10, 221, 121] print hoga
