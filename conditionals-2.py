# Aayie, hum peechle example ko hum dobara dekhte hai.

day = "Wednesday"

if day == "Monday": # Agar din Monday hai toh
	print "Rajma Chawal"
elif day == "Tuesday": # Agar uppar wali conditions galat hai (Yaani day Monday nahi hai) aur day Tuesday hai toh
	print "Pao Bhaji"
elif day == "Wednesday": # Agar uppar wali conditions galat hai (Yaani day Monday aur Tuesday nahi hai) aur day Wednesday hai toh
	print "Chole Bhature"
elif day == "Thursday": # Agar uppar wali conditions galat hai (Yaani day Monday, Tuesday aur Wednesday nahi hai) aur day Thursday hai toh
	print "Dosa"
elif day == "Friday": # Agar uppar wali conditions galat hai (Yaani day Monday, Tuesday, Wednesday aur Thursday nahi hai) aur day Friday hai toh
	print "Litti Chokha"
elif day == "Saturday": # Agar uppar wali conditions galat hai (Yaani day Monday, Tuesday, Wednesday, Thursday aur Friday nahi hai) aur day Saturday hai toh
	print "Thupka"
else: # Agar uppar wali conditions galat hai (Yaani day Monday, Tuesday, Wednesday, Thursday, Friday aur Saturday nahi hai)
	print "Poha"

print "Khayenge" # Loop ke bahar aa gaye hai. Yeh code hamesha chalega.


# Yaha par hum if, else, or elif ke saath aise expressions daalte hai jinka result Boolean value hota hai - yaani True or False
# Agar value True hoti hai toh aage ka code chalta hai, nahi toh hum next condition check karti hai, jaise

day = "Wednesday"
day == "Monday"
# Iska output false hoga, isliye hum next condition check karenge
day == "Tuesday"
# Iska output false hoga, isliye hum next condition check karenge
day == "Wednesday"
# Iska output True hoga, isliye hum print "Chole Bhature" code chalayenge, aur loop se bahar aa jayenge

# Hum aur complex cheezein kar sakte hai in conditions ke saath, jaise



if day == "Monday" or day == "Wednesday": # Agar din Monday hai toh
	print "Rajma Chawal"
elif day == "Tuesday" or day == "Thursday" or day == "Saturday": # Agar uppar wali conditions galat hai (Yaani day Monday aur Wednesday nahi hai) aur day Tuesday hai toh
	print "Pao Bhaji"
else: # Agar uppar wali conditions galat hai (Yaani day Monday, Tuesday, Wednesday, Thursday aur Saturday nahi hai)
	print "Poha"

print "Khayenge" # Loop ke bahar aa gaye hai. Yeh code hamesha chalega.



