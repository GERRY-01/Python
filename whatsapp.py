#Sending whatsapp message through python. When you run the code, it will take you to
# whatsapp and your message will take you to whatsapp

import pywhatkit as pwk

phone_number = "+254701266217"
message = "Hey bro, This message is sent using python programming"
pwk.sendwhatmsg(phone_number,message,22,3)
