# Notandi byrjar á reit x=1 og y=1 og þarf svo að velja átt sem hann getur farið í  

# 3x3 reitir og skilyrðin eru eftirfarandi: 
#   (1,1) -> þá geturu bara farið North
#   (1,2) -> þá geturu farið North og East
#   (1,3) -> þá geturu farið East og South
#   (2,3  -> þá geturu farið East og West
#   (3,3) -> þá geturu farið West og South
#   (3,2) -> þá geturu farið North og South
#   (3,1) -> þá geturu farið North 
#   (2,2) -> þá geturu farið West og South
#   (2,1) -> þá geturu farið North

# Þegar notandi hefur komist að gildinu (3,1) = Victory

beginning = (1,1)
print('You can travel: (N)orth.')

while beginning != (3,1):
    if beginning == (1,1):
        direction = input('Direction: ')
        if direction == 'n' or direction == 'N':
            beginning = (1,2)
            print('You can travel: (N)orth or (E)ast or (S)outh.')
            direction = input('Direction: ')
        else:
            print('Not a valid direction!')
            beginning = beginning
    if beginning == (1,2):
        if direction == 'n' or direction =='N':
            beginning = (1,3) 
            print('You can travel: (E)ast or (S)outh.')
            direction = input('Direction: ')
        elif direction == 'E' or direction =='e':
            beginning = (2,2)  
            print('You can travel: (S)outh or (W)est.')
            direction = input('Direction: ')
        elif direction == 's' or direction =='S':
            beginning = (1,1)
            print('You can travel: (N)orth.')
        else:
            print('Not a valid direction!')
            beginning = beginning
            direction = input('Direction: ')
    if beginning == (1,3):
        if direction == 's' or direction == 'S':
            beginning = (1,2)
            print('You can travel: (N)orth or (E)ast or (S)outh.')
            direction = input('Direction: ')
        elif direction == 'e' or direction =='E':
            beginning = (2,3) 
            print('You can travel: (E)ast or (W)est.')
            direction = input('Direction: ')
        else:
            print('Not a valid direction!')
            beginning = beginning
            direction = input('Direction: ')
    if beginning == (2,2):
        if direction == 's' or direction == 'S':
            beginning = (2,1)
            print('You can travel: (N)orth.')
            direction = input('Direction: ')
        elif direction == 'w' or direction == 'W':
            beginning = (1,2)  
            print('You can travel: (N)orth or (E)ast or (S)outh.')
            direction = input('Direction: ')
        else:
            print('Not a valid direction!')
            beginning = beginning
            direction = input('Direction: ')
    if beginning == (2,1):   
        if direction == 'n' or direction =='N':
            beginning = (2,2)  
            print('You can travel: (S)outh or (W)est.')
            direction = input('Direction: ')    
        else:
            print('Not a valid direction!')
            beginning = beginning
            direction = input('Direction: ')
    if beginning == (2,3):       
        if direction == 'e' or direction =='E':
            beginning = (3,3)  
            print('You can travel: (S)outh or (W)est.')
            direction = input('Direction: ')
        elif direction == 'w' or direction =='W':
            beginning = (1,3)
            print('You can travel: (E)ast our (S)outh.')
            direction = input('Direction: ')
        else:
            print('Not a valid direction!')
            beginning = beginning
            direction = input('Direction: ')
    if beginning == (3,3): 
        if direction == 'w' or direction =='W':
            beginning = (2,3)   
            print('You can travel: (E)ast or (W)est.')
            direction = input('Direction: ')
        elif direction == 's' or direction == 'S':
            beginning = (3,2) 
            print('You can travel: (N)orth or (S)outh.')
            direction = input('Direction: ')
        else:
            print('Not a valid direction!')
            beginning = beginning
            direction = input('Direction: ')
    if beginning == (3,2):  
        if direction == 's' or direction == 'S':
            beginning = (3,1) 
        elif direction == 'n' or direction == 'N':
            beginning = (3,3)  
            print('You can travel: (S)outh or (W)est.')
            direction = input('Direction: ')
        else:
            print('Not a valid direction!')
            beginning = beginning
            direction = input('Direction: ')
    if beginning == (3,1):
        print('Victory!')