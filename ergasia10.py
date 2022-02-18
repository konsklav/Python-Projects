file_input = input("Enter ASCII file in txt form: ")
f = open(file_input, 'r')
#f = open('ergasia10.txt', 'r')   #afaireste to sxolio kai prostheste ena stis dyo panw grammes an den douleuei me diko sas arxeio, etsi wste na to trexete me to diko mou (ergasia10.txt)
text = f.read()
text = str(text)
text = text.replace('\n','')
L1 = []
bin_text = bytearray(text, "utf8")
for b in bin_text:
    bin_convertion = bin(b)
    L1.append(bin_convertion[2:])
for i in L1:
    L2=list(i)
    while len(L2)<7: 
        L2.insert(0,'0')
first_and_last_bits_L3 = []
for l in L1:
    L2=l
    i=0
    for j in L2:
        if i==0 or i==1 or i==5 or i==6:
            first_and_last_bits_L3.append(j)
        i+=1
cont_str = ""
for k in first_and_last_bits_L3:
    cont_str+=k
length=len(cont_str)
L4 = []
for i in range (0,length,17):
    L4.append(cont_str[i:i+16])
while len(L4[len(L4)-1])<16:
    L4[len(L4)-1] = '0' + L4[len(L4)-1]
L5 = []
L6 = []
for d in L4:
    L5 = list(d)
    i=0
    de_num=0
    for h in L5:
        h = int(h)
        de_num+=(2^i)* h
        i+=1
    L6.append(de_num)
num_length=float(len(L6))
v1=0
for q1 in L6:
    if q1%2==0:
        v1+=1
percentage1=float(v1)/num_length*100
print("To pososto twn zygwn arithmwn einai:", percentage1, "%")
v2=0
for q2 in L6:
    if q2%3==0:
        v2+=1
percentage2=float(v2)/num_length*100
print("To pososto twn arithmwn pou diairountai me to 3 einai:", percentage2, "%")
v3=0
for q3 in L6:
    if q3%5==0:
        v3+=1
percentage3=float(v3)/num_length*100
print("To pososto twn arithmwn pou diairountai me to 5 einai:", percentage3, "%")
v4=0
for q4 in L6:
    if q4%7==0:
        v4+=1
percentage4=float(v4)/num_length*100
print("To pososto twn arithmwn pou diairountai me to 7 einai:", percentage4, "%")