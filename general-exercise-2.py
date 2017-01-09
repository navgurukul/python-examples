# Yeh exercise hai
# Har line of code se pehle aapko ek line mei comment  mei daal kar likhna hai, ki uss line of code ka matlab kya hai
# Aap jyada comments bhi likh sakte hai, jitne jyada comments likhenge, utna aapkya fayda hoga

# Question 1
# Pehle ke variable_list mein 0 se 100 integers ki list banayein
# Fir aapne iss list pe iterate karte hue 3 nayi list banani hai:
# - Pehli_list naam ki list mein variable_list ke items ko 3 se multiply karke jo result aaya hai, woh hona chaiye
# - Dusri_list naam ki list mein variable_list ke items ko 4 se divide karke jo result aata hai, woh hona chaiye.
#   Iss dusri list mein saari items `float` honi chaiye
# - Teesri_list naam ki list variable_list ke items ko "NavGurukul" string ke saath jodna hai. Jaise:
#   Agar variable_list ka pehla item 0 hai, iss teesri_list ka pehla item "NavGurukul0" hona chaiye
#   Dusra item "NavGurukul1"
#   Teesra item "NavGurukul2"
# Iss program mein bas list banani hai. Kuch print nahi karna.








#Question 2
# - Ek number ka factorial 1 se leke uss number tak ke saare numbers ko ek saath multiply karke nikalta hai.
# Jaise 3 ka factorial 6 hai. Kyunki -
# 1 * 2 * 3 ko calculate karke 6 aata hai
# 4 ka factorial 24 hai. Kyunki -
# 1 * 2 * 3 * 4 ko calculate karke 24 aata hai
# Aise hi 7 ka factorial 5040 hai. Kyunki -
# 1 * 2 * 3 * 4 * 5 * 6 * 7 ko calculate karke 5040 aata hai
# Ab aap ek function likhoge jo ek integer argument lega fir uska factorial return karega.
#function ka naam factorial hona chaiye
# Agar user 3 dalega ko 6 return karega, 7 dalega toh 5040 return karega aur aise hi dusre numbers ke lie.
# Note: Abhi ke liye yeh soch lo ki user sirf positive integers hi dalega. Negative integers kabhi nahi dalega.









# Question 3
# numbers_list naam ki ek list banayein jisme 1 se 100 (das hazar) tak integers hon
# Ab numbers_list ke saare numbers ka sum nikalne ka function likhein.
# function ka naam list_sum hoga jo ek list argument legi
# End mein sum ko return karein









# Question 4
# Socho aapko paas ek list hai jisme kuch values baar baar aa rahi hain.
# Ek aisa code likho jisse aap ek nayi list banayein jisme iss list ki items ek ek baar hi aaye.
# Jaise:
# string_list = ["Rishabh", "Rishabh", "Abhishek", "Rishabh", "Divyashish", "Divyashish"]
# Aapke code ko iss string_list se ek new_list list banai hai jo yeh hogi:
# new_list = ["Rishabh", "Abhishek", "Divyashish"]
# Yeh list dekhiye isme saare naam ek ek baar aa rahe hain. Farak nahi padta ki pichli list mein kitne baar aa rahe the.
# Samajhne ke liye ek aur example padho
# string_list = ["Delhi", "Delhi", "Mumbai", "Mumbai", "Delhi", "Chennai", 'Chennai']
# Isse aapke code ko yeh nayi list banani hogi:
# new_list = ["Delhi", "Mumbai", "Chennai"]
# Iss nayi list mein sirf saare shehron ka naam sirf ek baar aa raha hai.
# Yeh rahi aapki pehli items repeat hone waali list:
string_list = ["Empathy", "Empathy", "Kindness", "Kindness", "Compassion", "Humble", "Humble"]









# Question 5
# Socho aapke paas 2 lists hain. Aapne aisa function likhna hain jisse ek nayi list return ho
# jisme inn dono lists ke woh item hone chaiye ho dono list mein aa rahe hain.
# function ka naam find_common hona chaiye
# function ko 2 list arguments leni chaiye
# Socho aapki do list yeh hain:
# list1 = [1, 342, 75, 23, 98]
# list2 = [75, 23, 98, 12, 78, 10, 1]
# Inn dono list se aapki nayi list yeh banni chaiye:
# new_list = [1, 75, 98]
# Iss nayi list mein sirf 1, 75 aur 98 isliye hain kyunki aur koi bhi items dono lists mein nahi aa rahi.
# Dusri saari items ya toh pehli list mein aa rahi hai ya dusri mein.
# Note: Aapka yeh code kitne bhi items ki list pe kaam karna chaiye.











# Question 6
# Maan li jiye aapke paas yeh kuch english words ki list hai:
#words = ['time',  'person',  'year',  'way',  'day',  'thing',  'man',  'world',  'life',  'hand',  'part',  'child',  'eye',  'woman',  'place', 'case',  'point',  'government']
# Aapne word_count naam ka function likhna hai jo ek list input le aur :
# - Saare unn words ko count karo jinme "e" aata hai
# - Saare unn words ka count karo jinme "i" aata hai
# - Saare unn words ka count karo jinme "e" aur "i" dono aate hain
# - jaise
# 'e' waale words - 6
# 'i' waale words - 3
# 'e' aur 'i' waale words - 2
# function ko inn sab ka sum return karna hai jo ki 11 hai









# Question 7
# - Socho aapke paas do lists hain. Aapko nayi list banani hai jisme dono lists ke elements hone chaiye.
# Lekin yeh dhyan mein rakhna hai ki dono lists ke saare elements sirf ek-ek baar hi hone chaiye.
# Agar humare paas yeh do lists hain:
# list1 = [1, 5, 10, 12, 16, 20]
# list2 = [1, 2, 10, 13, 16]
# Toh humari nayi list yeh hogi:
# new_list = [1, 2, 5, 10, 12, 13, 16, 20]
# - Yahan dekho ki dono lists ke items ek ek baar aa rahe hain.
# - Jaise dono lists mein 1 aa raha tha, lekin nayi list mein ek hi baar aa raha hai.
# - Aise hi 10 aur 16 bhi dono list mein aa raha tha, lekin nayi list mein ek hi baar hai
# - Aur 5, 2, 12, 13 aur 20 mein se kuch pehli list mein the aur kuch dusri mein, lekin
#   sabhi nayi list mein ek ek baar aa rahe hain
# - aapko merge naam ka function banana hai jo do lists argument le
# - yeh function ek nayi list return karga jaise upar samjhaya hai
