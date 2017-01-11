# Yeh exercise hai
# Har line of code se pehle aapko ek line mei comment  mei daal kar likhna hai, ki uss line of code ka matlab kya hai
# Aap jyada comments bhi likh sakte hai, jitne jyada comments likhenge, utna aapkya fayda hoga


# Question 1
# Harshad numbers aise number hote hain jo apni digits ke sum se dhang se divide hote hain.
# Dhang se divide hone ka matlab ki remainder 0 aata hai.
# Jaise 42 ek Harshad number hai kyunki 4 + 2 = 6 aur 42 ko 6 se vidie kar ke remainder aata hai
# Aise hi 18, 21 aur 24 bhi harshad number hai kyunki 1 + 8 = 9 aur 18 ko 9 se divide kar ke remainder 0 hai
# 2 + 1 = 3 aur 21 / 3 ka remainder 0 hai. Aise hi 1, 2, 3, 4, 5, 6, 7, 8, 9 saare harshad number hain kyunki
# inki digits ka sum khud yeh number hain aur yeh apne aap se divide ho jate hain.
# Ek number ke digits nikalne ka code yeh hai:
x = 42
x_digits = list(str(x))
# yahan humne list function mein x ko string mein type cast kar ke de diya. Toh ab yeh har 42 ke alag alag
# number se list bana dega. `x_digits` mein ["4", "2"] list hogi. Iss list mein saare digits string ki
# form mein hogi, aap unko firse integer mein convert kar sakte ho
# Ek function likho "is_harshad_number" jo ek number parameter ki tarah le aur fir agar woh number
# harshad number hai toh ek boolean (True agar harshad number hai, False agar nahi hai toh) return kare
# Fir iss function ka use kar ke 1 se 1000 ke beech mein saare harshad number print karo.


# Question 2
# Python mein hum ek loop ke andar loop bhi chala sakte hain
# Sochiye humare paas ek list hai jisme aur list hain jinme integers hain. Kuch aise:
big_list = [[1,2,3], [5,8,9], [4,3,77,521,31,311]]
# Iss list se agar humne saare numbers ko ek ek kar ke print karna hai toh hum kuch aisa code likh sakte hain
for small_list in big_list:
    for number in small_list:
        print number
    print "-----"
# Iski output kuch aisi aayegi
# 1
# 2
# 3
# -----
# 5
# 8
# 9
# -----
# 4
# 3
# 77
# 521
# 31
# 3111
# Yahan pehle woh `for small_list in big_list` wala loop chala ke uski pehli iteration mein pahunchta hai
# Fir jab small_list ki value mein pehli list, [1,2,3] aati hai uspe pura dusra loop chalta hai
# Dusra loop poora chalne ke baad print "-----" line chalti hai aur fir yeh code pehle loop mein jaata hai
# Fir small_list ki value mein [5,8,9] jaata hai aur fir pura andar waala loop chalta hai.
# Iss code ko python visualizer (www.pythontutor.com) mein chala ke ache se samjho










# Socho aapke paas ek school ki class mein har student ke har subject ke marks hain. Jaise
marks = [[45, 21, 42, 63], [12, 42, 42, 53], [42, 90, 78, 13], [94, 89, 78, 76], [87, 55, 98, 99]]
# Yeh ek list mein andar aur lists hain. Andar waali list mein har bache ke saare subjects mein marks hain
# Ek max_marks naam ka function banao jo ki ek aisi list le aur har students ke maximum marks print kare
# Jaise agar main aapke max_marks function ko upar waali list ke saath call karunga , max_marks(marks)
# toh uski output yeh honi chaiye:
# 63
# 53
# 90
# 94
# 99
# Dekhiye ki har line har student ke maximum marks print hue hain










 
