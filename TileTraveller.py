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