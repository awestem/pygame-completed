from pgzhelper import *
WIDTH=600
HEIGHT=400

runner = Actor('run__000')
run_images = ['run__000', 'run__001', 'run__002', 'run__003', 'run__004', 'run__005', 'run__006', 'run__007', 'run__008', 'run__009']
runner.images = run_images
runner.x = 100
runner.y = 200

velocity_y = 0
gravity = 1

obstacles = []
obstacles_timeout = 0

score = 0
game_over = False

def update():
  global velocity_y, obstacles_timeout, score, game_over
  runner.next_image()

  obstacles_timeout += 1
  if obstacles_timeout > 50:
    actor = Actor('cactus')
    actor.x = 650
    actor.y = 230
    obstacles.append(actor)
    obstacles_timeout = 0

  for actor in obstacles:
    actor.x -= 8
    if actor.x < -50 and not game_over:
      obstacles.remove(actor)
      score += 1

  if keyboard.up:
      velocity_y = -15

  runner.y += velocity_y
  velocity_y += gravity
  if runner.y > 200:
    velocity_y = 0
    runner.y = 200
    
  if runner.y < 0:
    velocity_y = 0
    runner.y = 0
    
  if runner.collidelist(obstacles) != -1:
    game_over = True


def draw():
  screen.draw.filled_rect(Rect(0,0,600,200), (163, 232, 254))
  screen.draw.filled_rect(Rect(0,200,600,200), (88, 242, 152))
  screen.draw.text('Score: ' + str(score), (15,10), color=(0,0,0), fontsize=30)
  
  if game_over:
    screen.draw.text('Game Over', centerx=270, centery=70, color=(255,255,255), fontsize=60)
    screen.draw.text('Score: ' + str(score), centerx=270, centery=130, color=(255,255,255), fontsize=60)
  else:
    runner.draw()
    for actor in obstacles:
      actor.draw()
  
