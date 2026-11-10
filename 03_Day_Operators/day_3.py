day 3 : "à days of python programming 
age = 20
taille = 1.73
nombre_complexe = 3 + 2j

hauteur = input("donnez la hauteur " )
print(" elle est de :", hauteur )
base = input("donnez la base ")
print("elle est de : " , base )
aire_du_triangle = 0.5 * int(hauteur) * int(base)
print("l aire est de :", aire_du_triangle)

# PERIMETRE 
a= input("donne le coter a :")
print("a:" , a )
b=input("donne le coter b:")
print("b:",b)
c=input("donne le coter c:")
print("c:" , c)
perimetre = int(a) + int(b) + int(c)
print (" la perimetre est de :" , perimetre)

# rectangle 
longueur= input("donnez votre longueur")
print("longueur:", longueur)
largeur = input("donnez la largeur")
print("elle est de :", largeur)
aire = int(longueur) * int(largeur)
print( "l aire est de :", aire) 
perimetre = 2* (int(longueur) + int(largeur))
print( " le perimetre est de :" , perimetre)

# Cercle
rayon = input("donnez le rayon")
print ("rayon est de :", rayon)
pi=3.14
aire = pi * int(rayon)* int(rayon)
print("aire  est de :", aire)
circonference = 2 * pi * int(rayon)
print("la circonf est de :", circonference)

# pent
def analyser_droite (m,p):
  print(f"la pente de la droite est : y={m}x + {p}")
  pente = m
  print(f" la pente est de :{pente} ")  
  ordonne_origine = p
  print(f"ordonne origine : {ordonne_origine}")
  if m != 0 :
    abscisse_origine = -p/m
    print("abscisse origine = ", {abscisse_origine})
  else: print( "la droite est horizontale sauf si p = 0")
analyser_droite(m =2, p = -2)

# pente 2
def interieur(x1, x2, y1 , y2):
  print(f"la valeur de chaque point : {x1} , {x2} , {y1}, {y2}")
  m = y1-y2/x1-x2
  print(f"la pente est de : {m}")
  distance_eucludienne = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
  print(f"la pente eucludienne : {distance_eucludienne}")
interieur(x1=2, x2=6,y1=2,y2=10)  

pent_exo8 = 2
pente_exo9 = 2
if pent_exo8 > pente_exo9:
  print("celle de l exo 8 est plus grand ")
elif pente_exo9  > pent_exo8:
  print(" celle de 9 est plus grand ")
else : print( "les deux sont les meme")    

x = int(input("donnez une valeur x qui rend y =0 "))
y = (x ** 2) + (6*x )+ 9
print(f" pour x : {x} , alors y est :{y}")
for x in range(-6, 10):
  y = (x**2) + (6*x)+ 9
  print(f"pour x : {x} , alors {y}")

longueur_python = len("python")
longueur_dragon =len("dragon")
print(f"la longueur python : {longueur_python}")
print(f"la longueur dragon  : {longueur_dragon}")
comparaiso = longueur_dragon > longueur_python
print(f"est ce que dragon est plus long que dragon ? {comparaiso}")

print("on" in "python" and "on" in "dragon")
print( "jargon" in "I hope this course is not full of jargon")

longueur_python = len("python")
flotant = float(longueur_python)
print(flotant)
chaine = str(flotant)
print(chaine)

for x in range (0,20 ):
  if x%2 == 0:
    print(f"le nombre x = {x} est paire ")
  else: print(f"le nombre x = {x} est non paire")

valeur_normale = 7//3
print("valeur1 :", valeur_normale)
valeur_test = int(2.3)
print("valeur 2 :",valeur_test)
comparaison = valeur_normale == valeur_test
print(comparaison)

x = 10 
y = '10'
a = type(x)
print(a)
b = type(y)
print(b)
comparaison = a ==b 
print(comparaison)

valeur_a = int(9.8)
valeur_b = 10 
comparaison = valeur_a==valeur_b
print(comparaison)

heure = int(input("donnez la duree"))
taux_horaire = int(input("equivalence: "))
salaire_hebdomadaire = heure*taux_horaire
print("votre salaire est de :",salaire_hebdomadaire)

nombre_annee_vecu = int(input("votre age "))
seconde_vie = nombre_annee_vecu * 365 * 24 * 60 * 60 
print(f"seconde de votre vie est :{seconde_vie} s")

for i in range(1,6):
  print(i,1 , i**2 , i**3, )



