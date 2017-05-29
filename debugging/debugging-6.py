##############
# Question 6 #
##############
# Ek cities naam ki list banate hai
cities = ["palampur", "hampi", "kodaikanal", "shillong"]
# Ab hume iss array ko print karna hai reverse (yaani ulte) order mei
for i in range(len(cities)):
    # Yeh karne ke liye hum pehla element print karne ke jagah last element print kar lenge
    print cities[len(cities)-i]
