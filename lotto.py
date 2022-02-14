import random

def gen_irish():
   return random.randint(1, 47)
    
def gen_euro():
    return random.randint(1, 50)

def irish_lotto():
    irishLotto = []

    count = 0
    
    while True:
        if len(irishLotto) < 6:
            number = gen_irish()
            while number in irishLotto:
                number = gen_irish()     
            irishLotto.append(number)
            count += 1

        elif count == 6:
            irishLotto.sort()
            count = 0
            break    
    result = str(irishLotto)
    return result
    

def euromillions():
    euroMillions = []
    luckyStars = []
    count = 0
       
    while True:
        if len(euroMillions) < 5:
            number = gen_euro()
            while number in euroMillions:
                number = gen_euro()     
            euroMillions.append(number)
            count += 1
           
        elif count == 5:
            euroMillions.sort()
            count = 0
            break  

    while True:
        if len(luckyStars) < 2:
            number = gen_euro()
            while number in luckyStars or number > 12:
                number = gen_euro()     
            luckyStars.append(number)
            count += 1   

        elif count == 2:
            luckyStars.sort()
            count = 0
            break    
    result = str(euroMillions) + " Lucky Stars: " + str(luckyStars)
   
    return result