import smtplib

my_email = "dingucar@gmail.com"
password = "123456cu"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs="cu20030311@gmail.com", msg="hello")
connection.close()





