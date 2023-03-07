import libs.greek_lib as greeklib

word = 'rẽma'
word = 'angelos'
word = 'anastasis'
word = 'afẽmi'
word = 'baile'
word = 'reir'
word = 'oir'
word = 'bautismo'
word = 'fluctuar'

print("----------------------------------------------")
print("*        TRASLITERACIÓN ESPAÑOL GRIEGO       *")
print("----------------------------------------------")
print("Palabra (Español): "+word)
print("----------------------------------------------")
greek = ""
details = []
for char in word:
    for equiv in greeklib.equivalencies_without_sigma():
        if char.lower() in equiv:
            details.append([char, equiv[1], equiv[5]])
            if equiv[1].lower() == 's':
                chars_s = equiv[1].split(',')
                greek = greek + chars_s[0]; 
            else:
                greek = greek + equiv[1]

print("----------------------------------------------")
print("Detalles: ")
print("----------------------------------------------")
result = greeklib.sigma_case(word, greek, details)

for val in result[1]:
    print(val[0]+' : '+val[1]+' : '+val[2])
print("----------------------------------------------")

print("----------------------------------------------")
print("Palabra (Griego Koiné): "+result[0])
print("----------------------------------------------")