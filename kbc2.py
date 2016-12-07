# Yeh exercise hai
# Har line of code se pehle aapko ek line mei comment mei daal kar likhna hai, ki uss line of code ka matlab kya hai
# Aap jyada comments bhi likh sakte hai, jitne jyada comments likhenge, utna aapkya fayda hoga

# Aap yeh code execute karke dekho

# Ab hum ek flag variable ka use karenge apne program ko control karne ke liye. flag koi bhi normal variable and iska naam kuch bhi rakh sakte ho.

flag=True
for index in range(10):
	# if flag likhne se, jaise hi flag False set ho jayega, toh yeh sab execute nahi hoga
	if flag:
		# Yaha par aap woh saara kaam karenge jo aap chahte hai na ho jab flag False set ho jaye

		# Yeh condition batati hai flag kab False set karna hai. Aap iss condition ke jagah apne hisaab se koi bhi condition likh sakte hai, jab aap chahte ki Flag false set ho jaye
		if index>6:
			flag=False

		print "Yeh flag ke andar hai", index

	# Yeh flag ke bahar hai toh yeh toh execute hoga hi, chahe flag ki value kuch bhi ho
	print "Yeh flag ke bahar hai", index


# Humne toh loop 10 baar chalane ko kaha tha, toh loop sirf 8 baar kyu execute hua?
# Flag variable ke vajah se.

# Issi concept ka use karke apne KBC game ko aise modify karo jisse ki ----
# Agar user galat answer karta hai toh aap wahi par loop se bahar nikal jaye aur print karein - "KBC Khatam. Phir kheliyega!"















# HINT 
# Iske liye aap flag use karoge. Chaliye iss variable ko flagRightAnswer kehte hai
# Galat answer karne par aap flagRightAnswer ko False set kar do
# Loop mei aate hi check karo and dekho agar flagRightAnswer True hai tab hi loop ke andar ka code execute karo


# Ab aap issi program ko aise modify karo ki loop ke bahar aane ke baad bhi jo index ki value hai usse use karke aap user ko batao woh kitne paise jeeta hai. User apne pichle padav ke paise hi jeetega. Toh agar user ne 12th question galat kiya toh aap user ko doosre padaav ke paise doge.



















# User answer mei option dene ki jagah - user quit likh kar game se withdraw bhi kar sakta hai
# But ismei user ko jis question par quit kiya hai, utne paise dene hai
# Socho isse logically kaise karoge. Pehle pen and paper ka use karke sochna. Uske baad karna.
# Jaise humne flag ke baarei mei socha tha, kya aap aisa kuch yaha soch sakte hai?
# Flag ek tareeke se ek temporary variable tha jo kuch information store kar raha tha

# Finally, aapka aisa message print hona chahiye.
# "Aap ne game se quit kar liya hai. Par aaj aap ghar le kar ja rahe hai 320000 rupees." (320000 ko user ki jeeti hue paise se badloge)

















