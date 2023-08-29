"""
The game is played in a zone 16000 units wide by 9000 units high. You control a man named Ash, wielding a gun that lets him kill any zombie within a certain range around him.

Ash works as follows:
Ash can be told to move to any point within the game zone by outputting a coordinate X Y. The top-left point is 0 0.
Each turn, Ash will move exactly 1000 units towards the target coordinate, or onto the target coordinates if he is less than 1000 units away.
If at the end of a turn, a zombie is within 2000 units of Ash, he will shoot that zombie and destroy it. More details on combat further down.

Other humans will be present in the game zone, but will not move. If zombies kill all of them, you lose the game and score 0 points for the current test case.

Zombies are placed around the game zone at the start of the game, they must be destroyed to earn points.

Zombies work as follows:
Each turn, every zombie will target the closest human, including Ash, and step 400 units towards them. If the zombie is less than 400 units away, the human is killed and the zombie moves onto their coordinate.
Two zombies may occupy the same coordinate.

The order in which actions happens in between two rounds is:
Zombies move towards their targets.
Ash moves towards his target.
Any zombie within a 2000 unit range around Ash is destroyed.
Zombies eat any human they share coordinates with.

Killing zombies earns you points. The number of points you get per zombie is subject to a few factors.

Scoring works as follows:
A zombie is worth the number of humans still alive squared x10, not including Ash.
If several zombies are destroyed during on the same round, the nth zombie killed's worth is multiplied by the (n+2)th number of the Fibonnacci sequence (1, 2, 3, 5, 8, and so on). As a consequence, you should kill the maximum amount of zombies during a same turn.
"""
STEP = 400
SHOOT_RANGE = 2000

class Human:
 def __init__(self,id,x,y):
  self.id=id
  self.x=x
  self.y=y
  self.priority=0 # priority of humman, the higher the priority, the more important the humman is (5 is the highest)

 def priority(self):
  return self.priority

 def set_priority(self,priority):
  self.priority+=priority

 def human(self):
  return [self.id,self.x,self.y]

 def debug(self):
  return f"Human {self.id} at ({self.x},{self.y}) with priority {self.priority}"

 def is_safe(self,zombies,ASH):
  # safe if no zombie is within and in Ash's shooting range
  return min([distance((zombie[1],zombie[2]),(self.x,self.y)) for zombie in zombies])>SHOOT_RANGE

# prioritize hummans based on the following criteria:
# human has max priority is 10
# more steps to reach humman, less priority
# needed steps of ash to reach humman > needed steps of zombie to reach humman, less priority
# Case:
## Ash can't reach human before zombie, priority = -1
## Ash can reach human before zombie, priority = +1
## Ash can't reach human before zombie, but can shoot zombie before it touch human, priority = +1
## Ash can reach human before zombie, but humman is too far, priority = +0,5
## Human have zombie in range 400 and Ash can't reach human before zombie, priority = -99
def prioritize(humans, zombies, ASH):
  prioritized_humans = []

  for human in humans:
    # calculate needed steps of ash to reach humman
    ash_steps = distance((ASH[0],ASH[1]),(human.x,human.y))//STEP
    # calculate needed steps of zombie to reach humman
    zombie_steps = min([distance((zombie[1],zombie[2]),(human.x,human.y))//STEP for zombie in zombies])
    # calculate needed steps of ash to reach humman before zombie
    ash_steps_to_reach_human_before_zombie = ash_steps - zombie_steps
    # calculate needed steps of ash to shoot zombie before it touch humman
    ash_steps_to_shoot_zombie_before_it_touch_human = ash_steps - (zombie_steps - 1)
    # calculate priority
    if ash_steps_to_reach_human_before_zombie < 0:
      human.set_priority(-1)
    elif ash_steps_to_reach_human_before_zombie == 0:
      human.set_priority(1)
    elif ash_steps_to_shoot_zombie_before_it_touch_human == 0:
      human.set_priority(1)
    elif ash_steps_to_reach_human_before_zombie > 0:
      human.set_priority(-0.5)
    if not human.is_safe(zombies,ASH):
      human.set_priority(-99)
    prioritized_humans.append(human)
  
  sorted_humans = sorted(prioritized_humans, key=lambda human: human.priority, reverse=True)
  return sorted_humans

def distance(point1, point2):
   return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

if __name__ == '__main__':
 import sys
 x,y=map(int,input().split()) # x,y coor of player (Ash)
 h=int(input()) # number of humans``
 humans=[] # humans[id,x,y]
 for i in range(h):
   humans.append(Human(*list(map(int,input().split(" "))))) # hummans[id,x,y]
 z=int(input()) # number of zombies
 zombies=[] # zombies[id,x,y,xnext,ynext]
 for i in range(z):
   zombies.append(list(map(int,input().split(" "))))
 # find the closest humman are in danger and move to that humman
 # if no humman is in danger, move to the closest humman
 humans=prioritize(humans,zombies,(x,y))
 while True:
  # move to the humman with the highest priority

  print(humans[0].x,humans[0].y)