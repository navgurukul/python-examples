# encrypt function ek message input leta hai aur firr uss message ko encrypt karta hai
# Encrypt karne ke liye yeh har character ko 3 character aage wale character se change kar deta hai.
# Aisa karne ke liye yeh har character ki ascii value ko 3 se increase kar deta hai.
# Jaise,
#   v ki ascii value 118 hai, agar hum isse 3 se increase kar de tab yeh 121 ho jayegi. Jo ki 'y' ki ascii value hai.
#   ascii value nikalne ke liye hum ord() ka use karte hai.
#   aur ascii value ko string mei convert karne ke liye chr function ka.
#   Jaise,
#   ascii_value = ord(v) # 118
#   string_value = str(ascii_value) # v
# decrypt function encrypt function ka ultaa hai. Yeh value ko 3 se incresae karne ki jagah 3 se kam kar deta hai.
def encrypt():
  message = raw_input("Enter the message you want to encrypt")
  ascii_message = [ord(char)+3 for char in message]
  encrypt_message = [ chr(char) for char in ascii_message]  
  print ''.join(encrypt_message)

  
def decrypt():
  message = raw_input("Enter the message you want to decrypt")
  ascii_message = [ord(char) for char in message]
  decrypt_message = [ chr(char) for char in ascii_message]  
  print ''.join(decrypt_message)

flag = True
while flag == True
choice = raw_input("What do you want to do? 1. Encrypt a message 2. Decrypt a message         Enter E or D respectively!")
if choice = 'e':
encrypt() 
els choice = 'd':
  decrypt()    
else
    play_again = raw_input("Do you want to try agian or Do you want to exit? (Y/N)")
    if play_again == 'Y'
        continue
    elif play_again == 'N':
        break
