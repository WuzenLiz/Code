import math

# surface
target_x1, target_y1, target_x2, target_y2 = 0, 0, 0, 0
last_x, last_y = 0, 0
surface_n = int(input())
for i in range(surface_n):
    land_x, land_y = [int(j) for j in input().split()]
    target_x1 = last_x if last_y == land_y else target_x1
    target_y1 = last_y if last_y == land_y else target_y1
    target_x2 = land_x if last_y == land_y else target_x2
    target_y2 = land_y if last_y == land_y else target_y2

STAGE = {
 'initial': 1,
 'mid': 2,
 'slow_down': 3,
 'landing': 4
}
counter = 0
if __name__ == '__main__':
 while True:
  stage = STAGE['initial']
  counter += 1
  # x: x position, y: y position
  x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in input().split()]
  
  if v_speed > 0:
   v_speed *= -1
  
  if h_speed != 0 and v_speed != 0:
   aoa = math.atan2(v_speed, h_speed) # angle of attack
   y0 = y - target_y1  # height from target
   vector_mag = math.hypot(h_speed, v_speed) # magnitude of vector
   theta = aoa # angle of attack
   g = 3.711 # gravity
   distance = ((vector_mag**2 / (2 * g)) * (1 + (1 + ((2 * g * y0) / (vector_mag**2 * math.sin(theta)**2))) ** 0.5)) * (math.sin(2 * theta)) # distance to target
   distance = int(distance) * -1
  
  angle = 0
  # Initial Approach (stage 1): The lander approaches the target area from the left or right. It adjusts the rotation angle and thrust power to maintain a specific horizontal speed range.
  if stage == STAGE['initial']:
   power = 4
   if abs(h_speed) < 40:
    angle = 45 if x < target_x1 else -45
   else:
    stage = STAGE['mid']
  # Mid-Approach (stage 2): After a certain number of turns, the lander switches to a mid-approach stage. It aims to align itself with the target area and control its horizontal speed.
  elif stage == STAGE['mid']:
   angle = 0
   if counter % 20 == 0:
    power = 3
   else:
    power = 4
   if abs(h_speed) < 20:
    stage = STAGE['slow_down']
  # Slow Down (stage 3): The lander starts to slow down as it gets closer to the target. It adjusts its rotation angle based on its vertical and horizontal speeds to control the descent.
  elif stage == STAGE['slow_down']:
   power = 4
   opp_angle = int((math.degrees(aoa) - 90) % 360 - 180)
   if opp_angle >= 70:
    angle = 70
   elif opp_angle <= -70:
    angle = -70
   
   if abs(h_speed) > 1:
     angle = opp_angle
   else:
    angle = 0
    stage = STAGE['landing']
  # Landing (stage 4): In the final stage, the lander prepares for landing by adjusting the thrust power based on its vertical speed. It aims to achieve a safe vertical descent speed.
  elif stage == STAGE['landing']:
   if abs(v_speed) < -30:
    power = 4
   else:
    power = 3
  print(angle, power)