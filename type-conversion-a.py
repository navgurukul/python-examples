# iss example mei hum ek type conversion karenge jo hume aage baar baar karni padegi

# raw_input ek function hai jo user se input leta hai, jo hamesha STRING ki form mei hota hai

# agar user 12 bhi enter karega, raw_input hume '12' dega

# isliye raw_input se INTEGER lene ke liye hume STRING se INT mei type cast karna hoga

# input ek variable hai jo raw_input ka output store karta hai
user_input = raw_input("Enter a number");

# ab ismei user ki side se 12 input karo aur dekh input ka type and value kya hai
print type(user_input)
print user_input

# agar hume 12 number chahiye toh hume isse INTEGER mei cast karna hoga

val = int(user_input)
print type(val)
print val

# PRO TIP
# aap raw_input ki string mei nayi line add karne ke liye \n add kar sakte ho. \n matlab new-line

# jaise
user_input = raw_input("Enter a number:\n")
print "tumne ", int(user_input), "enter kiya"