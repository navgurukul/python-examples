# iss example mei hum ek type conversion karenge jo hume aage baar baar karni padegi

# Aage jake bahot baar hume apne users se kuch input leni padegi. Input lene ke liye hum
# python mein `raw_input` ka use karte hain. Jaise
user_input = raw_input("Kuch input daaliye ")

# Jab yeh run hoga, toh python ruk jayegi aur ek cursor dikhayegi.
# Yahan aapko kuch input daalni hogi. Kuch bhi input daal ke `Enter` press kar do.
# Ab jab aap user_input ko `print` kar ke dekhoge, toh aapne jo bhi value daali hai
# woh `user_input` variable ke andar string ke roop mein hogi.
print user_input

# Ek aur raw_input ka example leke isko aur detail mein samajhte hain
number1 = raw_input("Ek number daalo ")

# Yahan dekho ki raw_input ke brackets ke andar humne ek string daala hai.
# Iss string ki value "Ek number daalo" hai. Hum inn brackets ke andar jo bhi
# string daalte hain, woh string python use se input maangne se pehle print
# kar deti hai. Isse user ko kuch hint mil jata hai ki kya input karna hai.
# Jaise upar wale example mein, python input maangne se pehle
# "Ek number daalo" print kar dega. Aur jab user number (input) daal ke enter
# press karega, toh `number1` variable mein woh value chali jayegi.

# Hum jab bhi `raw_input` se kisi variable mein user input lete hain woh string
# type ki form mein hoti hai. Matlab, user jo bhi daalta hai raw_input usko
# string bana deta hai.
number2 = raw_input("Ek number daalo ")

# Yahan `number2` ka data type string hoga. Jab bhi hum kisi variable ki value
# `raw_input` se input lete hain toh woh value string ki roop mein hoti hai.
# Agar user ne number bhi input dala hai toh, woh string ke roop mein hoga.
print type(number2)

# Jaise agar yahan humne 25 enter kia toph `number2` ki value "25" hogi.
# Usko integer mein convert karne ke liye hume `int()` ka use karna padega.
number3 = int(number2)
print type(number3)

# Neeche ek final example hai inn sab cheezon ko ache se samajhne ke liye.
# Yeh example do numbers ko input ko leke unko multiple kar ke print karta hai
number_x = raw_input("Pehla number daaliye ")
number_y = raw_input("Dusra number daaliye")
number_x = int(number_x) # kyunki `raw_input` se hume number_x string type ki form mein mila
number_y = int(number_y) # kyunki `raw_input` se hume number_y string type ki form mein mila
print number_x * number_y # yahan `number_x` aur `number_y` ko multiply kar ke result
                          # print ho raha hai.

# Yahan yeh samajhna bahot zaroori hai ki humne multiply karne se pehle
# `number_x` aur `number_y` ko integer mein convert kiya kyunki `raw_input`
# se hume input humesha string ki form mein milti hai.
