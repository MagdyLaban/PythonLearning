import re

email_sender = list()
host = list()
data = open("C:/Users/magdylaban/OneDrive/Desktop/mbox-short.txt")
# extracting email sender
for line in data :
    y = re.findall("^From (\S+@+\S+)", line)
    if len(y) <= 0 :
        continue
    email_sender.append(y)
print(email_sender)
# extracting host names
for email in email_sender :
    host_name = email[0].split("@")
    host.append(host_name[1])
print(host)
