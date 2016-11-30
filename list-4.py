# Iss example mei RANGE FUNCTION ko use karna seekhenge

# Yeh commands try karo
print range(0)
print range(5)
print range(9)

# Ab yeh commands try karo
print len(range(0))
print len(range(5))
print len(range(9))

# kuch observe kiya?

# range (n) ek n length ki LIST bana dete hai jismei 0 se le kar (n-1) tak numbers hote hai
# range (6) - [0, 1, 2, 3, 4, 5] LIST bana dega

# ab list ko iterate karte hue hum ek simple sa loop likhte hai
for index in range(6):
    print index

# yeh loop bilkul waisa loop jaisa humne pichli assignment mei kiya tha

students_list = ["robin", "anamika", "faisal", "valmiki", "waseem", "amara"]
marks_list = [83, 90, 45, 78, 23, 37]

# yeh lists humne pichli assignment mei use ki thi

for index in range(6):
    print students_list[index], "ke", marks_list[index], "marks hai"

# aisa karke hum do LISTS ko ek saath iterate kar paa rahe hai. yeh karne ke liye hum range(n) LIST ko use kar rahe hai