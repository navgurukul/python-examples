# Iss example mein hum FUNCTION ARGUEMNTS aur PARAMETERS ke baare mein padhenge

# FUNCTION ARGUMENTS ka pehla example
# Neeche diye gaye code ko chala ke dekho aur ek baar socho ki kya ho raha hai

def say_hello(name):
    print "Hello ", name
    print "Aap kaise ho?"
say_hello("Aatif")

# Yahan humne function ko ussi tareeke se define kiya hai jaise pichle examples mein kiya tha
# Lekin dhyan se dekho toh "def say_hello" ke baad brackets mein humne *name* likha hai aur, aur neeche ek *name* variable ko print command ke saath use kar rahe hain.
# Yahan name ko parameter kehte hain jiski value hum function call karne ke time de sakte hain.
# Aakhri line mein function call karte vakt humne brackets ke andar "Aatif" likha hai. Function call karte vakt hum jo parameters ko value dete hain, unko arguments kehte hain.
# Toh basically humne iss example mein yeh kiya aur seekha:
# - say_hello naam ka ek function define kiya jo ek name naam ka parameter leta hai aur uska use kar ke kuch print karta hai
# - fir humne function call kiya aur function call karne ke time ek argument diya jiski value "Aatif" thi
# - jab yeh function call hota hai toh jo humne string "Aatif" argument diya hai. Yahan uski value name parameter mein jaati hai aur. Jab yeh value
#   name parameter mein jaati hai, toh woh function ke andar same naam ke variable mein use kar sakte hain. Humne iss variable ka naam use kar ke print command likhi hai.
# Note: Yeh thoda sa mushkil concept, agar bahot ache se samajh nahi aaya, toh ek aur baar padh ke aur dusre examples dekh ke zaroor samajh aa jayega ;-)

# Ek aur FUNCTION ARGUMENTS ka basic example.

 def say_bye(name):
     print "Bye bye ", name
     print "Aapko mil ke acha laga"
say_bye("Drishti")
print "Yahan hum functions seekh rahe hain."
string_name = "Rishabh"
say_bye(string_name)
# Yahan humne pichle example ki tarah ek function "say_bye" define kiya jo ek name parameter leta hai
# Iske baad humne "say_bye" function ko call kiya aur argument mein ek string, "Drishti" diya. Jab function call karte hain iss argument ki value function ke name parameter mein chali jati hai.
#   Iss tareeke se woh same naam. Hum jis naam se function parameters likhte hain, ussi naam se hum unki value function ke andar se same naam ke variable
#   Iss tareeke se yeh value function ke andar same parameter vale naam ke variable se use kar sakte hain.
#   Jaise yahan *name* wale parameter ki value name variable mein hai jo humne print command ke saath use kiya hai.
# Fir humne print command ka use kar ke ek string print kiya hai
# Fir humne ek variable string_name declare kiya jiski value ek string, "Rishabh" hai.
# Iske baad humne ek "say_bye" function call kiya aur usko ek argument diya jo ki string_name naam ka ek variable hai.
# Yahan gaur dijiye ki hum function ko kisi bhi tareeke se parameters de sakte hain, jaise variables ka use kar ke jo ki humne say_bye(string_name) mein kiya ya directly value deke jo humne say_bye("Drishti") mein kiya.


# 2 ARGUMENTS ke saath FUNCTION ka example

def add_numbers(number1, number2):
    print "Main do numbers ko add karunga."
    print number1 + number2
add_numbers(120, 50)
num_x = 134
num_y = 22
add_numbers(num_x, num_y)

# Yahan humne ek add_numbers naam ka function define kara hai. Lekin dekho ki bracket mein humne 2 parameter likhe hain. Ek sa jyada argument lene ke liye arguments ke baad comma laga dete hain
# Humne add_numbers(120, 50) likh ke function call karte samay do integer parameter diye hai. Yahan parameters ka kram / order important hai. Iss function call mein yeh hota hai:
# - 120 ki value "pehle" parameter number1 mein jaati hai jo ki function ke andar same naam ke variable number1 mein hai
# - 50 ki value "dusre" parameter number2 mein jaati hai jo ki function ke andar same naam ke variable number2 mein hai
# Baad mein humne do variable define kare hain, num_x and num_y aur fir add_numbers ko num1 aur num2 arguments deke call kiya hai. Yahan bhi:
# - num_x ki value 134 pehle parameter number1 mein jaati hai aur num_y ki value 22 dusre parameter number2 mein jaati hai

# 2 ARGUMENTS ke saath ek aur example
# Hum yahan ek function banayenge jo aapke pasand ki language mein hello print karega.

def say_hello_language(name, language):
    if language == "hindi":
        print "Namaste ", name
        print "Aap kaise ho?"
    elif language == "punjabi":
        print "Sat sri akaal ", name
        print "Tuhada ki haal hai?"
    else:
        print "Hello ", name
        print "How are you?"
say_hello_language("Rishabh", "punjabi")
say_hello_language("Armaan", "english")
say_hello_language("Abhishek", "french")
say_hello_language("Kavay", "hindi")

# Yeh function do parameter leta hai, name aur language aur aise kaam karta hai:
# - Agar language "hindi" di hai, toh hindi mein kuch print karega
# - Agar language "punjabi" di hai, toh punjabi mein kuch print karega
# - Agar "hindi" aur "punjabi" ke ilava koi bhi language di hai toh punjabi mein karega
# Yeh karne ke liye humne ek function define kiya jo do arguments leta hai, *name* aur *language*.
# Hum jab say_hello_language("Rishabh", "punjabi") call karte hain toh yeh hota hai:
# - pehle parameter, *name* mein "Rishabh" string jata hai aur dusre parameter, *language* mein punjabi jaata hai.
# - fir humara program if-elif-else ka use kar ke dekhta hai language ki value kya hai aur uske hisaab se sahi language mein print kar deta hai
# Isi tareeke se upar likhi hui saari function calls mein yeh hi hota hai


# 4 ARGUMENTS ke saath ek aur FUNCTION ka example
# Chalane se pehle isko padh ke output ko sochne ki koshish karo. Fir chala ke dekho ki aapne sahi output sochi thi ya nahi

def say_hello_people(name_x, name_y, name_z, name_a):
    print "Namaste ", name_x # hindi mein
    print "Alah hafiz ", name_y # urdu mein
    print "Bonjour ", name_z # french mein
    print "Hello ", name_a # english mein
say_hello_people("Imitiyaz", "Rishabh", "Rahul", "Vidya")
say_hello_people("Steve", "Saswata", "Shakrundin", "Rajeev")

# Iss function mein dekho ki yeh 4 argument leta hai, name_x, name_y, name_z, name_a.
# def waali pehli line mein humne 4 parameter ka naam comma (,) laga laga ke likhe hain
# Function call karte samay jis kram / order mein humne parameters likhe hain def waali line mein, wahi kram / order mein arguments ki value parameters mein jaati hai.
# say_hello_people("Imitiyaz", "Rishabh", "Rahul", "Vidya") mein parameters ki value iss hisaab se jaati hain:
# - "Imtiyaz" ki value pehle parameter name_x mein jaati hai
# - "Rishabh" ki value dusre parameter name_y mein jaati hai
# - "Rahul" ki value teesre parameter name_z mein jaati hai
# - "Vidya" ki value teesre parameter name_a mein jaati hai
