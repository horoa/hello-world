from math import pi

# https://python.developpez.com/cours/apprendre-python-3/?page=exercices-corriges
#1. Écrire un programme qui, à partir de la saisie d'un rayon et d'une hauteur, calcule le volume d'un cône droit.

def findVolume(radius,height):
    return pi*radius*radius*height/3.0

def exercice1():
    print("radius = " + str(findVolume(float(input("radius?")),float(input("height?")))))
  
#2. Une boucle while : entrez un prix HT (entrez o pour terminer) et affichez sa valeur TTC.

def findPriceTTC():
    prixHT = float(input("Prix HT (0 pour terminer) ?"))
    while prixHT > 0:
        print("Prix TTC : " + str(prixHT * 1.2) + "€\n")
        prixHT = float(input("Prix HT (0 pour terminer) ?"))

def exercice2():
    findPriceTTC()
        
        
#3  Une autre boucle while : calculez la somme d'une suite de nombres positifs ou nuls. Comptez combien il y avait de données et combien étaient supérieures à 100.
#   Entrer un nombre inférieur ou égal à 0 indique la fin de la suite.

def sumOfASerie():
    numberInput = float(input("Number of the serie (0 to end) ?"))
    totalOfNumberHigherThanOneHundred = 0
    totalOfNumber = 0
    sumTotal = 0
       
    while numberInput > 0 :
        if numberInput >= 100 :
            totalOfNumberHigherThanOneHundred +=1
        totalOfNumber +=1
        sumTotal += numberInput
        numberInput = float(input("Number of the serie (0 to end) ?"))
        
    print("The sum total of the serie is " + str(sumTotal) + " there was " + str(totalOfNumber) + " numbers and " + str(totalOfNumberHigherThanOneHundred) + " numbers higher than 100")

def exercice3():
    sumOfASerie()
    
#4 L'utilisateur donne un entier positif n et le programme affiche PAIR s'il est divisible par 2, IMPAIR sinon

def isOddOrEven():
    numberInput = int(input("Take a number"))
    if numberInput%2 == 0 :
        print( str(numberInput) + " is even")
    else :
        print( str(numberInput) + " is odd")

def exercice4():
    isOddOrEven()
    
#5 L'utilisateur donne un entier positif et le programme annonce combien de fois de suite cet entier est divisible par 2.

def numberOfPossibleHalves():
    numberInput = int(input("Take a number"))
    numberOfHalves = 0
    while numberInput != 0 and numberInput%2==0 :
        numberInput/=2
        numberOfHalves+=1
    print("You can divide your number " + str(numberOfHalves) + " times\n")

def exercice5():
    numberOfPossibleHalves()
    
#6 L'utilisateur donne un entier supérieur à 1 et le programme affiche, s'il y en a, tous ses diviseurs propres sans répétition ainsi que leur nombre. S'il n'y en a pas, il indique qu'il est premier.

def findCommonDivisor():
    numberInput = int(input("Take a number"))
    if numberInput == 0 :
        print("0 has all integers other than 0 as a common divisor.\n")
    elif numberInput == 1 :
        print("1 has no common divisor but it isn't a prime number.\n")
    else :
        while numberInput < 2 : 
            numberInput=int(input("please choose a number greater than 1"))
        listOfCommonDivisor = []
        for i in range(2, numberInput) :
            if numberInput%i == 0 :
                listOfCommonDivisor.append(i)
        if len(listOfCommonDivisor) == 0 :
            print( str(numberInput) + " has no common divisor, it's a prime number")
        else :
            print ( str(numberInput) + " has " + str(len(listOfCommonDivisor)) + " common divisor : " + str(listOfCommonDivisor))
            
def exercice6():
    findCommonDivisor()
            
#7 Écrire un programme qui approxime par défaut la valeur de la constante mathématique e, pour n assez grand(56)

def findE():
    numberInput = 0
    while numberInput < 1 :
        numberInput = int(input("Number for the sum"))
    sum = 0
    for i in range(numberInput+1) : 
        sum += 1.0/factoriel(i)
    print("The value e is approximatively equals to " + str(sum))
    
def factoriel(number) :
    if number == 0 : 
        return 1
    return number*factoriel(number-1)

def exercice7():
    findE()

#8  Un gardien de phare va aux toilettes cinq fois par jour. Or les WC sont au rez-de-chaussée…
#   Écrire une procédure (donc sans return) hauteurParcourue qui reçoit deux paramètres, le nombre de marches du phare et la hauteur de chaque marche (en cm), et qui affiche :
#   Pour x marches de y cm, il parcourt z.zz m par semaine.

def hauteurParcourue(nombreMarche, hauteurMarche):
    print("For " + str(nombreMarche) + " steps of " + str(hauteurMarche) + "cm, he walks " + str(nombreMarche*hauteurMarche*2*7*5/100) + "m per week")

def exercice8():
    hauteurParcourue(int(input("number of step?")),float(input("height of the step?")))
   
#9  Un permis de chasse à points remplace désormais le permis de chasse traditionnel. Chaque chasseur possède au départ un capital de 100 points. S'il tue une poule, il perd 1 point, 3 points pour un chien, 5 points pour une vache et 10 points pour un ami. Le permis coûte 200 euros.
#   Écrire une fonction amende qui reçoit le nombre de victimes du chasseur et qui renvoie la somme due.
#   Utilisez cette fonction dans un programme principal qui saisit le nombre de victimes et qui affiche la somme que le chasseur doit débourser.

def calculateFine(countKillChicken, countKillDog, countKillCow, countKillHunter) :
    print(str(((countKillChicken+countKillDog*3+countKillCow*5+countKillHunter*10)//100)*200)+ "€")

def exercice9():
    calculateFine(int(input("Chicken killed?")),int(input("Dog killed?")),int(input("Cow killed?")),int(input("Hunter killed?")))
    
#10 Je suis ligoté sur les rails en gare d'Arras. Écrire un programme qui affiche un tableau me permettant de connaître l'heure à laquelle je serai déchiqueté par le train parti de la gare du Nord à 9 h (il y a 170 km entre la gare du Nord et Arras).
#   Le tableau prédira les différentes heures possibles pour toutes les vitesses de 100 km/h à 300 km/h, par pas de 10 km/h, les résultats étant arrondis à la minute inférieure.
#       Écrire une procédure tchacatchac qui reçoit la vitesse du train et qui affiche l'heure du drame ;
#       Écrire le programme principal qui affiche le tableau demandé.

def tchacatchac(trainSpeed):
    hour = 170//trainSpeed
    min = int(170%trainSpeed*60/trainSpeed)
    minTen = '0' if min<10 else ''
    print (str(trainSpeed) + "km/h => " + str(9+hour) + "h" + minTen + str(min))

def stationTab():
    for vitesse in range(100,310,10):
        tchacatchac(vitesse)
        
def exercice10():
    stationTab()
    

