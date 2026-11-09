day 2 : 30 Days of python programming 
prenom = 'Njina'
nom = 'Ravonjihasimbola'
country = 'Madadgacar'
city = 'Antananarivo'
age = 20
annee = 2026
is_married = false 
perso_info = {'prenom':'Njina', 'nom': 'Ravonjihasimbola', 'country':'Madagascar', 'city':'Antananarivo'}
# exo 2

print(type('Njina'))
print(type('Ravonjihasimbola'))
print(type('Madagascar'))
print(type(20))
print(type(2026))
print(type(false))

print(" prenom:" , prenom )
print('longueur_prenom :', len(prenom))
print("nom:" ,nom)
print("longueur_nom:" ,len("nom"))
if len(prenom)> len(nom):
  print(" le prenom est plus long que le nom ")
else : print("le nom est plus long que le prenom " )

num_one =5
num_two = 4
total = int(num_one) + int(num_two)
print ('le somme est de :', total)

diff = int(num_one) - int(num_two)
print ('la difference est de :',diff)

produit= int(num_one) * int(num_two)
print(' le produit est de :', produit)

division =  int(num_one) / int(num_two)
print('la division est de :' , division)
divisions =  int(num_one) // int(num_two)
print('la division est de :' , divisions)

remainder= int(num_one) % int(num_two)
print( "le reste est de :", remainder)

exp= int(num_one) ** int(num_two)
print("la puissance est de:", exp)

rayon=30
area_of_circel = 3.14159 * (rayon**2)
print("l aire du cercle est de :" , area_of_circel)
circum_of_circel= 3.14159 * 2 * rayon
print("la circonference est de: ", circum_of_circel)
rayons =int(input("Donnez la rayon de votre cercle :"))
circel_area =  3.14159 * (rayons**2)
print("votre cercle a pour rayon :", circel_area)




