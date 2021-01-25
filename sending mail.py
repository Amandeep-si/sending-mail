import smtplib

sender_mail = input(str("Please enter your mail : \n"))
reciever_mail = input(str("Please enter mail to whom you want to send : \n"))
sender_password = input(str("Please enter your email password : \n"))
message = input(str("Please enter your message you want to send: \n"))

server = smtplib.SMTP('smtp.gmail.com', 587)#create a server for sending mail using the port number 587
server.starttls()
server.login(sender_mail,sender_password)#login the mail
print("Login is success")
server.sendmail(sender_mail, reciever_mail, message)#send the mail
print("Email has been sent to ", reciever_mail)
server.quit()
'''
For running this code follow the following steps:
Go to your Google Account.
Select Security.
Under "Signing in to Google," select App Passwords. You may need to sign in. If you don’t have this option, it might be because:
2-Step Verification is not set up for your account.
2-Step Verification is only set up for security keys.
Your account is through work, school, or other organization.
You turned on Advanced Protection.
At the bottom, choose Select app and choose the app you using and then Select device and choose the device you’re using and then Generate.
Follow the instructions to enter the App Password. The App Password is the 16-character code in the yellow bar on your device.
Tap Done.
'''