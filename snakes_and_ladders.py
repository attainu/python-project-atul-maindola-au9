from random import randint
from time import sleep


class Player:
    def __init__(self, playerNumber):
        self.name=input("enter the name of player {}: ".format(playerNumber))
        self.position=0
        self.finish=False
        self.rank=0

#snake and ladder check function checks if the player has reached the snake's head or bottom of the ladder
def snake_and_ladder_check(player,diceRolls,snakeHead,snakeTail,ladderBottom,ladderTop):
    if player.position+diceRolls<=100:
        if player.position+diceRolls in ladderBottom:
            print("Yay! {} just climbed the ladder on {} and climbs to {}".format(player.name,player.position+diceRolls, ladderTop[ladderBottom.index(player.position+diceRolls)]))
            return ladderTop[ladderBottom.index(player.position+diceRolls)]
        
        elif player.position+diceRolls in snakeHead:
            print("Ouch! {} got bit by Snake on {} and falls back to {} ".format(player.name,player.position+diceRolls,player.position+diceRolls-15))
            return snakeTail[snakeHead.index(player.position+diceRolls)]
        else: 
          return player.position+diceRolls

#dice roll functions rolls the dice and displays the what user got on the dice toll along with the check for 3 consecutive 6's on dice
def dice_roll(playerX):
    print("")
    sleep(0.5)
    choice=input("{}, press 'Enter' to roll the dice :".format(playerX.name))
    sleep(0.5)
    diceRoll1=randint(1,6)
    remaining=100-playerX.position
    if remaining>diceRoll1:
        
        if diceRoll1<6:
            print("{} rolled the dice for {} and moves to {} from {}.".format(playerX.name,diceRoll1,playerX.position+diceRoll1,playerX.position))
            print("")
        
        elif diceRoll1==6:
            print("{} rolled the dice for {} thus {} rolls again..".format(playerX.name,diceRoll1,playerX.name))
            diceRoll2=int(randint(1,6))
            sleep(0.5)
            diceRoll1+=diceRoll2
            if remaining>diceRoll1:
            
                if diceRoll2<6:
                    print("{} rolled the dice for {} and moves {} places to {} from {}.".format(playerX.name,diceRoll2,diceRoll1,playerX.position+diceRoll1,playerX.position))
                    print("")
                else:
                    print("{} rolled the dice for {} thus {} rolls again..".format(playerX.name,diceRoll2,playerX.name))
                    diceRoll3=int(randint(1,6))
                    sleep(0.5)
                    diceRoll1+=diceRoll3
                    if remaining>diceRoll1:
                        
                        if diceRoll3<6:
                            print("{} rolled the dice for {} and moves {} places to {} from {}.".format(playerX.name,diceRoll3,diceRoll1,playerX.position+diceRoll1,playerX.position))
                            print("")
                        else:
                            print("{} rolled the dice for {} again, that's three 6's in a row, thus {} won't move..".format(playerX.name,diceRoll3,playerX.name))
                            print("")
                            diceRoll1=0
                    
                    elif remaining==diceRoll1:
                        print("{} rolled the dice for {} and moves to {} from {}.".format(playerX.name,diceRoll3,playerX.position+diceRoll1,playerX.position))
                        print("")
                    else:
                        print("{} rolled the dice for {} thus can't move, out of bounds!".format(playerX.name,diceRoll3))
                        diceRoll1=0
                        print("")
            
            elif remaining==diceRoll1:
                print("{} rolled the dice for {} and moves {} places to {} from {}.".format(playerX.name,diceRoll2,diceRoll1,playerX.position+diceRoll1,playerX.position))
                print("")
            else:
                print("{} rolled the dice for {} thus can't move, out of bounds!".format(playerX.name,diceRoll2))
                diceRoll1=0
                print("")
    
    elif remaining==diceRoll1:
        print("{} rolled the dice for {} and moves {} places to {} from {}.".format(playerX.name,diceRoll1,diceRoll1,playerX.position+diceRoll1,playerX.position))
        print("")
    else:
        print("{} rolled the dice for {} thus can't move, out of bounds!".format(playerX.name,diceRoll1))
        diceRoll1=0
        print("")
    
    return diceRoll1

#create snakes functions takes the input from user regarding the head and tail of the snake
def create_snakes():
    print("")
    snake=int(input("enter no. of Snakes: "))
    snakeHead=[]
    snakeTail=[]
    
    for i in range(snake):
        snakeHead.append(int(input("enter the snake no. {} head position: ".format(i+1))))
        
        while snakeHead[i]<=1:
            snakeHead[i]=int(input("snakes's head can't be 1 or less than 1...enter again: "))
        
        snakeTail.append(int(input("enter the snake no. {} tail position: ".format(i+1))))
        
        while snakeHead[i]<=snakeTail[i]:
            snakeTail[i]=int(input("tail position should be less than head's position, enter again: "))
    
    return snakeHead,snakeTail

#create ladder function takes the input from user regarding the bottom and top of the ladder and checks if it doesn't concide with the snake's head or tail
def create_ladders(snakeHead,snakeTail):
    print("")
    ladder=int(input("enter no. of Ladders: "))
    ladderBottom=[]
    ladderTop=[]
    for i in range(ladder):
        ladderBottom.append(int(input("enter the ladder no. {}'s bottom position: ".format(i+1))))
        
        while ladderBottom[i]>=100 or ladderBottom[i] in snakeHead or ladderBottom[i] in snakeTail:
          if ladderBottom[i]>=100:
            ladderBottom[i]=int(input("ladder bottom can't be 100 or more...enter again: "))
          if ladderBottom[i] in snakeHead:
            ladderBottom[i]=int(input("ladder bottom can't be at snake's head...enter again: "))
          if ladderBottom[i] in snakeTail:
            ladderBottom[i]=int(input("ladder bottom can't be at snake's Tail...enter again: "))
        
        ladderTop.append(int(input("enter the Ladder no. {}'s Top position: ".format(i+1))))
        
        while ladderBottom[i]>=ladderTop[i] or ladderTop[i] in snakeHead or ladderTop[i] in snakeTail:
          if ladderBottom[i]>=ladderTop[i]:
            ladderTop[i]=int(input("Ladder's top position should be more than ladder's bottom position, enter again: "))
          if ladderTop[i] in snakeHead:
            ladderTop[i]=int(input("ladder's top can't be at snake's head...enter again: "))
          if ladderTop[i] in snakeTail:
            ladderTop[i]=int(input("ladder's top can't be at snake's Tail...enter again: "))
    
    return ladderBottom,ladderTop

#game function basically takes the list of players and create snake and ladders along with running the gameplay and displays result of the game
def game(players):
  snakeHead=[]
  snakeTail=[]
  ladderBottom=[]
  ladderTop=[]
  snakeHead,snakeTail=create_snakes()
  ladderBottom,ladderTop=create_ladders(snakeHead,snakeTail)  
  rank=1
  flag=True
  
  while flag:
    for i in players:
      if rank==len(players) and i.rank==0 and len(players)!=1:
          print("""{} finishes last! 
          
          !!!Game Over!!!""".format(i.name))
          i.finish=True
          flag=False
          break
      
      if i.finish==False:
        sleep(0.5)
        diceRolls=dice_roll(i)
        i.position=snake_and_ladder_check(i,diceRolls,snakeHead,snakeTail,ladderBottom,ladderTop)
        if i.position==100:
          i.finish=True
          if i.rank==0:
            if rank<len(players) or len(players)==1:
              i.rank=rank
              print("{} Wins! finishes with rank {}".format(i.name,i.rank))
              print("")
              rank+=1
              if len(players)!=1:
                choice=input("to continue the game press 'Enter' to end the game press 'Q' :")
                if choice=='q' or choice=='Q':
                    flag=False
                    print("!!! GAME OVER !!!")
                    break
              else:
                  flag=False
          
#main function takes the input from user of no. of players and their names and calls game function      
if __name__ == "__main__":

  print("")
  print("let's play Snakes And Ladders.")
  print("")
  
  p=int(input("enter the number of players:"))
  players=[]
  
  for i in range(p):
    print("")
    player=Player(i+1)
    players.append(player)

  game(players)
