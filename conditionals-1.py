# Programming karte hue hume “condition” likhne ki jaroorat padti hai.

# Matlab ek variable ki value ke hisaab se hume alag alag cheezein karni hoti hai.

# Maan lo hume apne hostel ke liye menu banana hai

# Ab yeh example dekhte hai

day = raw_input("Din enter karo\n")

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

# Yaha par teen keywords hai - if, elif, aur else. elif "else if" ki short form hai.

# Hum bina elif ke bhi likh sakte hai
if day == "Monday": # Agar din Monday hai toh
	print "Rajma Chawal"
else: # Agar din Monday nahi hai toh
	print "Poha"
print "Khayenge" # Loop ke bahar aa gaye hai. Yeh code hamesha chalega.

# Yeh simple sa program hai, jisme sirf do hi case hai - ya toh day Monday hai ya nahi


# Hum bina else ke bhi likh sakte hai
if day == "Monday": # Agar din Monday hai toh
	print "Rajma Chawal"

print "Khayenge" # Loop ke bahar aa gaye hai. Yeh code hamesha chalega.

# Yeh aur bhi simple sa program hai, jo sirf yeh Monday hone par kuch kaam karta hai


# Toh aapne dekha hoga ki hum simple ya complex, conditions if-elif-else use karke check kar sakte hai