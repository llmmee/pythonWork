import re
String1="我的邮箱是34161592@qq.com。你可以发送到邮箱15478245@qq.com\
或者34161592@qq.com。这是我的电话18251235874"
strobj=re.search('([a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+)[^a-zA-Z0-9]+([a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+)\
[^a-zA-Z0-9]+([a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+)[^a-zA-Z0-9]+([0-9]+)',String1)
print ("strobj.group(1) : ", strobj.group(1))
print ("strobj.group(2) : ", strobj.group(2))
print ("strobj.group(3) : ", strobj.group(3))
print ("strobj.group(4) : ", strobj.group(4))
