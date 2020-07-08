import random
tries=5
Win = False
Play = True
while Play == True :
  rand=random.randint(0,10)
  if tries>0:
    guess=input('pick a number between 0 and 10 \n')
    guess=int(guess)
    
    if (guess<0 or guess > 10) :
      print('I am afraid you just lost a turn ')
      tries=tries-1
      break
    else:
      if guess>rand:
        bigger = guess - rand
        print('you are'+ ' '+ str(bigger) + ' ' +'off the correct answer')
        tries=tries-1
      elif guess<rand:
        smaller= rand- guess
        print('you are'+str(smaller) + ' ' +'off the correct answer')
        tries=tries-1
      else:
        print( 'you got the number right')
  else:
    print( 'no more turns')
    Play=False
