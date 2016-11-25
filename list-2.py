# Iss example mei hum samjhenge ki LISTS ko kaise use karte hai

# Jaisa humne dekha LIST mei kaafi values hoti hai

# Toh hume koi tareeka chahiye jisse hum in values ko access kar paye

names_list = ["rahul", "shivam", "kavay", "ashish", "rohit"]

print names_list[1]

'''
Yeh karne se kya hua? "shivam" print hua? Yaha par 1 ko INDEX bolte hai. Kisi item ko access karne ke liye uska INDEX daalte hai. Dekhte hai iss array mei sabka INDEX kya hai

["rahul", "shivam", "kavay", "ashish", "rohit"]

    0        1         2        3         4

Agar aap dhyaan se dekhenge toh aap samjhenge ki INDEX uss ITEM

'''

print names_list[0]

# se "rahul" print hoga

print names_list[4]

# se "rohit" print hoga

print names_list[5]

# se kya hoga? error aayi - list index out of range
# iska matlab simple - jo INDEX aapne diya hai woh INDEX ki range se baahar hai
# simple question - maximum INDEX hum kitna daal sakte hai? 
# answer - INDEX ki length se ek kam
# usse par list index out of range error aayegi

# issi tarah se hum LIST mei ITEMS ko update/change kar sakte hai

names_list[0]="abhishek"
print names_list

# kya dekha aapne?
# jo 0 INDEX par ITEM tha woh change ho kar "abhishek" ho gaya
# issi tarah se

names_list[3]="rishabh"
print names_list

# jo 3 INDEX par ITEM tha woh change ho kar "rishabh" ho gaya
# dhyaan rakhe, ki INDEX item ki position se ek kam hota hai

# aise hi agar aap
names_list[5]="dhruv"
# karenge toh aapko list index out of range error milegi, kyuki 5th index par koi ITEM exist nahi karti

# list ki length check karne ke liye hum len function use kartein hai
print len(names_list)

# agar humne 
# iske liye hume append function use karna padega. functions ke baarein mei hum aage aur details mei padhenge

print names_list
names_list.append("dhruv")
print "length of the list is ", len(names_list)
print names_list

#dobara try karein
names_list.append("alok")
print "length of the list is ", len(names_list)
print names_list

# issi tarah se aap kitne bhi elements add kar sakte hai


# issi tarah, agar hume element remove karne hai

# list se agar aakhiri element hatana ho toh uske liye pop function use karte hai.

print names_list
names_list.pop()
print "length of the list is ", len(names_list)
print names_list
# aap dekhenge ki aakhiri element hat gaya hoga


# dobara try karein
names_list.pop()
print "length of the list is ", len(names_list)
print names_list



# list mei kaafi saari interesting operations kiye ja sakte hai
# unmei se ek operation hai yeh dekhna ki koi particular ITEM LIST mei belong karta hai ya nahi
# jaise

"shivam" in names_list

# True return karega, matlab "shivam" names_list mei hai

"imtiaz" in names_list

# False return karega, matlab "imtiaz" names_list mei nahi hai