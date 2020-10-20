import smtplib
msmtpUser = 'testeraccforbianca@gmail.com'
msmtpPass = 'thisismytestermail'

toAdd = 'naidubianca@gmail.com'
fromAdd = msmtpUser

subject = 'Python test' 
header = 'To: '+toAdd+'\n'+'From: '+fromAdd+'\n'+'Subject: '+subject
body = 'From within a python script'

print (header+'\n'+body)

s = smtplib.SMTP('smtp.gmail.com',587)

s.ehlo()
s.starttls()
s.ehlo()

s.login(msmtpUser, msmtpPass)
s.sendmail(fromAdd, toAdd, header +'\n\n' +body)

s.quit()
