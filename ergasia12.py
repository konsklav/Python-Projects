import json
from urllib.request import Request, urlopen
req = Request('https://drand.cloudflare.com/public/latest', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
data = urlopen(req).read()
data = str(data)
list = []
list = data.split("'")
dictionary = json.loads(list[1])
round = dictionary.get("round")
randomness = dictionary.get("randomness")
randomness = "0x" + randomness[0:]
randomness = int(randomness,16)
randomness = bin(randomness)
total_randomness = randomness
for i in range(99):
    round = round-1
    req = Request('https://drand.cloudflare.com/public/'+str(round), headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
    data = urlopen(req).read()
    data = str(data)
    list = []
    list = data.split("'")
    dictionary = json.loads(list[1])
    randomness = dictionary.get("randomness")
    randomness = "0x" + randomness[0:]
    randomness = int(randomness,16)
    randomness = bin(randomness)
    randomness = randomness[2:]
    total_randomness = total_randomness + randomness
total_randomness = total_randomness[2:]
list_of_bits = []
for i in range(0, len(total_randomness), 1):
    list_of_bits.append(total_randomness[i : i + 1])
length0 = 0
max0 = 0
length1 = 0
max1 = 0
for i in range(len(total_randomness)):
    if int(list_of_bits[i])==0:
        length0+=1
        length1=0
        if length0 > max0:
            max0 = length0
    elif int(list_of_bits[i])==1:
        length1+=1
        length0=0
        if length1 > max1:
            max1 = length1
print("The maximum length of continous zeros is: ", max0)
print("The maximum length of continous ones is: ", max1)