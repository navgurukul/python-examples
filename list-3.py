# Iss example mei hum samjhenge ki LISTS ko kaise ITERATE karte hai

# Class mei teacher ek ek naam bol kar attendance mark karti hai, list of students ki. Iss process ko ITERATION bolte hai. Ek ek karke list ke elements ke saath same action repeat karna.

# jaise yeh example dekho

students_list = ["robin", "anamika", "faisal", "valmiki", "waseem", "amara"]

for student in students_list:
    print student

# ismei kaafi saari cheezein samajhne ke liye important hai

# in general, yeh aise dekha ja sakta hai

# for item in list:
#     <do something with the item>

# iska hindi mei matlab hua -
# list mei rakhe hue item ke liye:
#     <item ke saath jo karna hai karein>

# iska matlab hum list har item ke liye ITERATE karte hue, kuch kaam uss item ke saath kar rahe hai. hum print kar sakte hai, hum item ki length print kar sakte hai, and so on

# doosri important cheez hai : (yaani colon). colon python mei loop ke baad lagaya jata hai. isse python ko pata chal jata hai ki aapne loop ko define kar diya hai

# : (yaani colon) lagane ke baad aap agli line mei likhna shuru karenge, and dhyaan rakhenge ki aapko indentation karni hai apne code ki

# yaani aapko apna code thoda space dekar likhna hai; isse python samajh gaya ki yeh code issi ITERATION ke andar ka code hai

# agar aapko aur code likhna hai issi ITERATION mei toh aap utne hi spaces dekar likhte rahenge

# aur jab aapko iss ITERATION se bahar nikalna hai toh aap woh spaces hata kar bahar likhna shuru kar denge

# jaise yeh example dekho

for student in students_list:
    # student_list mei har ek marks ke liye
    print "hi", student

print "hello", student

# student ek variable ki tarah kaam karta hai jo different values leta hai different points par. jaise

# hum loop mei jayenge
# -- pehle student ki value "robin" hogi and "hi robin" print hoga
# -- phir student ki value "anamika" hogi and "hi anamika" print hoga
# -- phir student ki value "faisal" hogi and "hi faisal" print hoga
# -- phir student ki value "valmiki" hogi and "hi valmiki" print hoga
# -- phir student ki value "waseem" hogi and "hi waseem" print hoga
# -- phir student ki value "amara" hogi and "hello amara" print hoga
# phir hum loop se bahar nikelenge
# par student ki value abhi bhi amara hi set hai, isliye "hello amara" set ho jayega

# socho kya hona chahiye? and phir execute karke dekho kya hota hai? kuch samajh aaya?

#ab yeh example dekho

student_marks = [23, 45, 89, 90, 56, 80]

total_marks = 0
for marks in student_marks:
    #student_marks mei har ek marks ITEM ke liye yeh karein

    # total_marks variable mei marks ko add kar do, jisse total_marks update ho jaye
    total_marks = total_marks + marks
    print "marks of current student", marks, "marks of all students till now", total_marks

print "total marks of all the students are ", total_marks

# socho kya hona chahiye? and phir execute karke dekho kya hota hai? kuch samajh aaya?

# ab yeh example dekho

total_marks = 0
for student in students_list:
    #student_list mei har ek student ke liye yeh karein

    #raw_input use karke sabke marks input karein
    marks_string = raw_input(student+" ke marks enter karo:\n")
    #raw_input se STRING milta hai. usse INTEGER mei type cast karein
    marks_int = int(marks_string)
    total_marks = total_marks + marks_int

print "sab students ke milakar total marks ", total_marks, "hai"

# socho kya hona chahiye? and phir execute karke dekho kya hota hai? kuch samajh aaya?

# dekha hum loops kitne tareeko se use karke unka fayda utha sakte hai

# ek aur example dekhte hai

student_marks = []
for student in students_list:
    #student_list mei har ek student ke liye yeh karein

    #raw_input use karke sabke marks input karein
    marks_string = raw_input(student+" ke marks enter karo:\n")
    #raw_input se STRING milta hai. usse INTEGER mei type cast karein
    marks_int = int(marks_string)
    #jo marks mile hai usse student_marks array mei daal de
    student_marks.append(marks_int)

print "marks ka array hai - ", student_marks

# ek variable banate hai jo kitne students ko marks ke hisaab se improvement ki jaroorat hai woh determine karega
num_students_need_improvement = 0
for student in students_list:
    #student_list mei har ek student ke liye yeh karein

    #raw_input use karke sabke marks input karein
    marks_string = raw_input(student+" ke marks enter karo:\n")
    #raw_input se STRING milta hai. usse INTEGER mei type cast karein
    marks_int = int(marks_string)
    #jo marks mile hai usse student_marks array mei daal de
    if marks_int < 30:
        print "marks less than 30"
        num_students_need_improvement = num_students_need_improvement + 1

print num_students_need_improvement, "students ko apne marks mei improvement ki jaroorat hai"


# Yeh sab examples padhne ke baad aapko yeh sab cheezei pata ache se samajh aa jani chahiye. har example ko 2-3 baar padhiye kyuki yeh examples kaafi jyada important hai

#1 - ITERATION ka matlab kya hota hai
#2 - Kisi LIST mei kaise ITERATE karte hai
#3 - ITERATE karte samay spaces kaise use ki jati hai