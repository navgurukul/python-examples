# Question 6 #
# Iss program ko run karo aur dekho ki num_list aur num_list_20 ki value same aa rahi.
# Iss code ko ais chane karo jisse hume num_list ki intial value bhi mil jaye.

def numbers_greater_than_twenty(list):
  for item in list:
    if item > 20:
      list.remove(item)
  return list


num_list = [12, 312, 42, 123, 5, 12, 53, 75, 123, 62, 9]

num_list_20 = numbers_greater_than_twenty(num_list)

print "Initial list", num_list
print "List that doesn't contain numbers greate than 20", new_list