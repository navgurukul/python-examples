# Yahan hum ek
number = 200
guess_done = False
attempts = 0
for i in range(10):
    if guess_done == False:
        guessed_number = raw_input("Apna guess enter karo > ")
        guessed_number = int(guessed_number)
        attempts = attempts + 1
        if guessed_number == number:
            guess_done = True
            print "Awesome! Aapne ekdum sahi number guess kara :)"
        elif guessed_number < number:
            print "Aapka number asli number se *chota* hai. Kuch bada guess karo!"
        elif guessed_number > number:
            print "Aapka number asli number se *bada* hai. Kuch chota guess karo!"
    else:
        print "Ab loop chal raha hai, lekin game band ho gayi kyuni aapne guess kar liya."
if guess_done == True:
    print "Aapne", attempts, "attempts mein sahi number guess kar liya."
else:
    print "Aap", attempts, "attempts mein sahi number guess nahi kar paye. Agli baar ke liye Good Luck :)"


# Menu deciding system
"""
1. Weekdays lunch will be Daal - Sabzi - Roti - Chawal
2. Weekdays dinner will be Daal - Sabzi - Roti
3. Tuesdays on lunch we will have Chicken
4. Fridays on dinner we will have Pav Bhaji
5. Weekends we will have Cook Yourself
6. On Sundays on lunch we will cook something new by learning it on Google
"""
day = raw_input("Aaj ka din daaliye (mon/tues/wed/thurs/fri/sat/sun) > ")
time = raw_input("Jis time ka menu chaiye woh daliye > (lunch/dinner) > ")
if day == "tues" and time == "lunch":
    print "Aaj tuesday hai. Chicken khate hain :)"
elif day == "fri" and time == "dinner":
    print "Friday dinner mein toh hum Pav Bhaji khayenge!"
elif day != "sat" and day != "sun" and time == "lunch":
    print "Daal - Sabzi - Roti - Chawal"
elif day != "sat" and day != "sun" and time == "dinner":
    print "Daal - Sabzi - Roti"
elif day == "sun" and time == "lunch":
    print "Aaj hum nayi jagah ki cuisine ke baare mein padh ke banayenge.!"
elif day == "sat" or day == "sun":
    print "Weekeds pe toh hum khud banayenge!"

# Write something in a rectangular frame
words = [
    "NavGurukul",
    "in",
    "a",
    "frame"
]
max_word_length = 0
for word in words:
    word_len = len(word)
    if word_len > max_word_length:
        max_word_length = word_len
frame_width = max_word_length + 4
print "+" * frame_width
for word in words:
    spaces = max_word_length - len(word)
    print "+ " + word + " "*spaces + " +"
print "+" * frame_width


# Cipher wheel with a function for finding an element in a list
def find_in_list(query, mainlist):
    mainlist_len = len(mainlist)
    range_for_loop = range(mainlist_len)
    index = None
    for i in range_for_loop:
        element = mainlist[i]
        if element == query:
            index = i
    return index

chars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
shifted_chars = ['c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b']

def encrypt_message(msg):
    new_msg = ""
    for character in msg:
        if character in chars:
            char_index = find_in_list(character, chars)
            new_char = shifted_chars[char_index]
            new_msg = new_msg + new_char
        else:
            new_msg = new_msg + character
    return new_msg


def decrypt_message(msg):
    new_msg = ""
    for character in msg:
        if character in shifted_chars:
            char_index = find_in_list(character, shifted_chars)
            new_char = chars[char_index]
            new_msg = new_msg + new_char
        else:
            new_msg = new_msg + character
    return new_msg


# Type conversion fuck up
# - Run a loop multiple (as given by user) times to take input from user and then take input from user of student marks. In the loop find the sum of student marks
# - Student name and marks and age in list and we need to compute the student with the largest age
# - Sum up numbers of strings
# - Aam example
