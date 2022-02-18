from collections import Counter
import json
file_input = input("Enter ASCII file in txt form: ")
f = open(file_input, 'r')
#f = open('ergasia7.txt', 'r')   #afaireste to sxolio kai prostheste ena stis dyo panw grammes an den douleuei me diko sas arxeio, etsi wste na to trexete me to diko mou (ergasia7.txt)
lines = f.readline()
dictionary = json.loads(lines)
f.close()
keys = dictionary.keys()
options = list(keys)
print(options)
choice = input("Choose a key from the options above: ")
rest_of_dictionaries = []
rof = open(file_input, 'r')
#rof = open('ergasia7.txt', 'r')   #afaireste to sxolio kai prostheste ena sthn apo panw grammi an den douleuei me diko sas arxeio, etsi wste na to trexete me to diko mou (ergasia7.txt)
for l in rof:
    rest_of_dictionaries.append(eval(l))
values = []
for i in rest_of_dictionaries:
    values.append(i[choice])
counter = Counter(values)
print("The most common value of the key you picked is: ", counter.most_common(1), "(the number on the right is the shows of the value)")
print("The maximum value of the key you picked is: ", max(values))
print("The minimum value of the key you picked is: ", min(values))