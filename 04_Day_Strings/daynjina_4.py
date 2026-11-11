#concactation 
mot1 = "thirty"
mot2 = "days"
mot3 = "of"
mot="python"
total = '{} {} {} {}'.format(mot1,mot2,mot3,mot)
print(total)
ph1= "coding"
ph2= "for"
ph3 = "all"
tout = f"{'coding'} {'for'}  {'all'}"
print(tout)
company= tout
print(len(company))
transfo = company.upper()
print(transfo)
transfo= company.lower()
print(transfo)
transfo=company.title()
print(transfo)
transfo=company.capitalize()
print(transfo)
transfo=company.swapcase()
print(transfo)

ph = " coding for all"
decoupe = ph[0:7]
print(decoupe)
print(ph.index('coding'))
print(ph.find('coding'))
print(ph.rindex('coding'))
print(ph.rfind('coding'))
new = ph.replace("coding","python")
print(new)
mot = "python for everyone"
print(mot.replace("everyone","all"))

mot = "coding for all"
print(mot.split())
entreprise = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
tous_entreprise =print(entreprise.split(", "))
premier_lettre = mot[0]
print(premier_lettre)
dernier_indice = len(mot) - 1 
print(dernier_indice)
ten = mot[10]
print(ten)

mot = "coding for all"
mot2 = "coding for all people"
decoupe = mot.split()
acro = decoupe[0][0] + decoupe[1][0] + decoupe[2][0]
capital = acro.upper()
print(capital)
po1 = mot.index('c')
print(po1)
po2 = mot.index('f')
print(po2)
po3 = mot2.rfind('l')
print(po3)

ph = "You cannot end a sentence with because because because is a conjunction"
po = ph.find("because")
print(po)
po1 = ph.rfind("because")
print(po)
decoupe = ph[31:55]
print(decoupe)

mot = "coding for all"
si = mot.startswith("coding")
print(si)
non = mot.endswith("coding")
print(non)
original = '&nbsp;&nbsp; Coding For All &nbsp;&nbsp;&nbsp; &nbsp;'
new = original.strip("&nbsp;&nbsp;&nbsp; &nbsp;")
print(new)
accept = "30DaysOfPython"
accept2 = "thirty_days_of_python"
print(accept.isidentifier())
print(accept2.isidentifier())

liste = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
decoupe = "# ".join(liste)
print(decoupe)
nom = "I am enjoying this challenge.\n I just wonder what is next."
print(nom)

print("name \t age \t country\tcity")
print("Njina \t 250 \t Mada  \t Tana")
radius = 10
pi = 3.14
area = 2 * radius * pi 
print("the circle with %d and %f  have a aera %s "%(radius,pi,area))
a=8
b=6
print("{} + {}={}".format(a,b,a+b))
print("{} - {}={}".format(a,b,a-b))
print("{} * {}={}".format(a,b,a*b))
print("{} / {}={}".format(a,b,a/b))
print("{} % {}={}".format(a,b,a%b))
print("{} // {}={}".format(a,b,a//b))
print("{} ** {}={}".format(a,b,a**b))

