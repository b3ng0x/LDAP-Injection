# LDAP-Injection
Login Bypass


# I should to bypass this
![](https://github.com/b3ng0x/LDAP-Injection/blob/main/1.png?raw=true)
After many try of some sqli payloads,fuzzing and i found nothing so i go to the hacktricks login bypass section and i found a payload that can help me to get the password,is using '*' wildcard
![](https://github.com/b3ng0x/LDAP-Injection/blob/main/3.png)

# How i get the  password
If the password is 'pass' so pass is the same as 'p*' and 'pa*' .... 
And its work with the user Reese gives in a hint
![](https://github.com/b3ng0x/LDAP-Injection/blob/main/4.png?raw=true)
# Solution
So to automate this i write a simple script using python<br>
[Solution](https://github.com/b3ng0x/LDAP-Injection/blob/main/bf.py)
![](https://github.com/b3ng0x/LDAP-Injection/blob/main/5.png?raw=true)
