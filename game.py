import pyglet, random, math
from pyglet.gl import *
from game import enemy,load,physicalobject,player,resources
from pyglet.window import mouse
from RL_brain import DeepQNetwork
from pyglet.window import key
import numpy as np

action_space=[dict(left=True, right=False,up=False, down=False),
              dict(left=False, right=True, up=False, down=False),
              dict(left=False, right=False, up=True, down=False),
              dict(left=False, right=False, up=False, down=True)]
n_actions=len(action_space)
n_features=5
RL = DeepQNetwork(n_actions, n_features,
                  learning_rate=0.01,
                  reward_decay=0.9,
                  e_greedy=0.9,
                  replace_target_iter=200,
                  memory_size=2000,
                  # output_graph=True
                  )

# Set up a window
game_window = pyglet.window.Window(1500, 800)
glClear(GL_COLOR_BUFFER_BIT)
def Reverse(tuples):
    new_tup = tuples[::-1]
    return new_tup

# reward=

wallVertex=()
# wallVertex+=Reverse((421, 45))
# wallVertex+=Reverse((1079, 81))
# wallVertex+=Reverse((977, 289))
# wallVertex+=Reverse((1315, 295))
# wallVertex+=Reverse((1300, 779))
# wallVertex+=Reverse((1000, 5951))
# wallVertex+=Reverse((229, 365))
# wallVertex+=Reverse((277, 193))

wallVertex+=(421, 45)
wallVertex+=(1079, 81)
wallVertex+=(977, 289)
wallVertex+=(1315, 295)
wallVertex+=(1300, 779)
wallVertex+=(1000, 595)
wallVertex+=(265, 793)
wallVertex+=(229, 365)
wallVertex+=(277, 193)

wallVertex2=()
wallVertex2+=(497, 157)
wallVertex2+=(873, 189)
wallVertex2+=(831, 391)
wallVertex2+=(1165, 391)
wallVertex2+=(1181, 555)
wallVertex2+=(1119, 433)
wallVertex2+=(377, 647)
wallVertex2+=(381, 349)


wallArr = []
pointCount=0
lastX=0
lastY=0
for i in range(0,len(wallVertex),2):
    pointCount+=1
    if i>0:
        wallArr.append((lastX,lastY,wallVertex[i], wallVertex[i+1]))
    lastX=wallVertex[i]
    lastY=wallVertex[i+1]

pointCount=0
lastX=0
lastY=0
for i in range(0,len(wallVertex2),2):
    pointCount+=1
    if i>0:
        wallArr.append((lastX,lastY,wallVertex2[i], wallVertex2[i+1]))
    lastX=wallVertex2[i]
    lastY=wallVertex2[i+1]


main_batch = pyglet.graphics.Batch()

# Set up the two top labels
# score_label = pyglet.text.Label(text="Score: 0", x=10, y=575, batch=main_batch)
# generation_label = pyglet.text.Label(text="Generation: 0", x=10, y=555, batch=main_batch)
# max_fitness_label = pyglet.text.Label(text="Max Fitness: 0", x=20, y=340)
# avg_fitness = pyglet.text.Label(text="Avg Fitness: 0", x=20, y=340)
# alive_label = pyglet.text.Label(text="Alive gamers: 0", x=20, y=360)
game_over_label = pyglet.text.Label(text="GAME OVER",
                                    x=250, y=-300, anchor_x='center', 
                                    batch=main_batch, font_size=48)


# bg = pyglet.sprite.Sprite(resources.road_image)
# bg.scale=0.7
# bg.x = 250
# bg.y = 300


PLAYER_SIZE = 100
score = 1
game_objects = []
gamers = []
# blocks = []

car_ship = player.Player(x=309, y=379 , batch=main_batch)
# replaced name of asteroids by blocks
blocks = [] #load.gen_enemies(3,batch= main_batch)
# print("length at start of block is "+str(len(blocks)))

# # Store all objects that update each frame in a list
blocks = [car_ship] + blocks

# # Tell the main window that the player object responds to events
game_window.push_handlers(car_ship)

rewardArr=[]
rewardArr.append((235,446,389,421,1))
rewardArr.append((229,478,411,459,0))
rewardArr.append((229,518,388,497,0))
rewardArr.append((236,558,400,534,0))
rewardArr.append((231,614,395,561,0))
rewardArr.append((239,690,392,620,0))
rewardArr.append((252,784,400,623,0))
rewardArr.append((355,784,412,630,0))
rewardArr.append((476,730,449,620,0))
rewardArr.append((563,718,519,596,0))
rewardArr.append((615,707,573,581,0))
rewardArr.append((679,696,628,559,0))
rewardArr.append((736,680,701,550,0))
rewardArr.append((800,663,748,536,0))
rewardArr.append((857,646,812,528,0))

rewardArr.append((859,639,825,509,0))
rewardArr.append((897,636,858,499,0))
rewardArr.append((910,622,880,496,0))
rewardArr.append((966,619,921,482,0))
rewardArr.append((979,619,983,457,0))
rewardArr.append((978,614,1072,436,0))
rewardArr.append((1040,638,1141,425,0))
rewardArr.append((1059,688,1160,502,0))
rewardArr.append((1142,706,1172,537,0))
rewardArr.append((1230,755,1173,543,0))
rewardArr.append((1292,738,1172,537,0))
rewardArr.append((1307,651,1169,517,0))
rewardArr.append((1312,539,1162,501,0))
rewardArr.append((1318,478,1166,465,0))
rewardArr.append((1326,435,1160,432,0))
rewardArr.append((1347,379,1141,423,0))
rewardArr.append((1327,314,1131,401,0))
rewardArr.append((1327,276,1107,400,0))
rewardArr.append((1195,279,1093,395,0))
rewardArr.append((1112,283,1049,417,0))
rewardArr.append((1070,259,1009,408,0))
rewardArr.append((1042,283,934,421,0))
rewardArr.append((1014,276,848,400,0))
rewardArr.append((1012,277,816,342,0))
rewardArr.append((1024,245,839,276,0))
rewardArr.append((1027,219,855,228,0))
rewardArr.append((1064,173,874,203,0))
rewardArr.append((1073,119,860,195,0))
rewardArr.append((1080,64,846,190,0))
rewardArr.append((906,68,795,197,0))
rewardArr.append((805,52,746,200,0))
rewardArr.append((722,47,711,202,0))
rewardArr.append((665,41,655,181,0))
rewardArr.append((590,28,585,163,0))
rewardArr.append((535,34,538,180,0))
rewardArr.append((437,27,500,170,0))
rewardArr.append((372,73,487,184,0))
rewardArr.append((319,134,462,229,0))
rewardArr.append((277,172,450,243,0))
rewardArr.append((239,231,438,287,0))
rewardArr.append((240,284,432,318,0))
rewardArr.append((214,319,411,346,0))
rewardArr.append((216,362,411,352,0))

currentTargetRewardIdx=0

generation_counter=0

rewardTuple = ()
for i in range(len(rewardArr)):
    rewardTuple += rewardArr[i]

# print(rewardTuple)

# lastX=0
# lastY=0
# totalCount=0
# @game_window.event
# def on_mouse_press(x,y, button, modifier):
#
#     if button == mouse.LEFT:
#         print("The Left Mouse Was Pressed:"+str(x)+" "+str(y))
#         global rewardArr
#         global lastX
#         global lastY
#         global totalCount
#         totalCount+=1
#
#         if(totalCount%2==0):
#             rewardArr.append((lastX, lastY, x, y))
#             print("Append")
#
#         lastX=x
#         lastY=y
#     elif button == mouse.RIGHT:
#         print("Right Mouse Was Pressed")
#         reset_one_game()

        # for i in range(len(rewardArr)):
        #     print("rewardArr+=(" +str(rewardArr[i][0]) +","+str(rewardArr[i][1])+ ")")

def reset_one_game():
    global car_ship,currentTargetRewardIdx
    car_ship.reset()
    currentTargetRewardIdx = 0

@game_window.event
def on_draw():
    game_window.clear()
    # bg.draw

    main_batch.draw()
    # glBegin(GL_LINE_LOOP)


    # for wall in wallVertex:
        # pyglet.graphics.draw(2, pyglet.gl.GL_LINE_LOOP,('c[34]B', (wall[0], wall[1], wall[2], wall[3])))
        # vertex_list = pyglet.graphics.vertex_list(4,
        #                                           ('v2f', (x, y, x + w, y, x + w, y + h, x, y + h)),
        #                                           ('c3B', (255, 0, 0, 255, 0, 0, 255, 0, 0, 255, 0, 0))
        #                                           )
    vertex_list = pyglet.graphics.vertex_list(int(len(wallVertex)/2),
                                                  ('v2f', wallVertex)
                                              # ,
                                              #     ('c3B', (255, 0, 0, 255, 0, 0, 255, 0, 0, 255, 0, 0))
                                                  )
    vertex_list.draw(gl.GL_LINE_LOOP)
    vertex_list2 = pyglet.graphics.vertex_list(int(len(wallVertex2) / 2),
                                              ('v2f', wallVertex2)
                                              # ,
                                              #     ('c3B', (255, 0, 0, 255, 0, 0, 255, 0, 0, 255, 0, 0))
                                              )
    vertex_list2.draw(gl.GL_LINE_LOOP)

    global rewardArr
    reward_batch = pyglet.graphics.Batch()
    t=rewardArr[currentTargetRewardIdx]

    # for i in range(len(rewardArr)):
    #     t=rewardArr[i]
    #     if rewardArr[i][4]==1:
    reward_batch.add(2, gl.GL_LINES, None,
                   ('v2f', (t[0], t[1], t[2], t[3])),
                   ('c3B', (255, 0, 0, 0, 255, 0)))
    reward_batch.draw()

# glVertex2f(wall[0],wall[1])
    # glEnd

learning_materials=[]

frame_counter=0
def update(dt):
    
    global blocks, game_objects, car_ship,currentTargetRewardIdx
    # if len(blocks) < 3:
    #     try:
    #         blocks.extend(load.gen_enemies(3-len(blocks), blocks[-1].y, batch=main_batch))
    #     except IndexError:
    #         blocks = load.gen_enemies(3, 200, batch=main_batch)

    # removal = []

    #AI Decision
    observation=np.array(car_ship.get_state_arr())
    action = RL.choose_action(observation)

    car_ship.keys=action_space[action]
    #model update
    for obj in blocks:
        obj.update(dt)
        # if obj.dead:
        #     removal.append(obj)
    observation_ = np.array(car_ship.get_state_arr())

    # Get rid of dead objects
    # for block in removal:
    #     blocks.remove(block)
    #     block.delete()

    # if not car_ship.dead:
    #     car_ship.update(dt)

    for block in blocks:
        if block.collides_with(car_ship):
            car_ship.dead = True

    learn=0

    rewardLine=rewardArr[currentTargetRewardIdx]
    global generation_counter
    if car_ship.collides_line_circle(rewardLine[0],rewardLine[1],rewardLine[2],rewardLine[3],10):
        print("Reward!")
        currentTargetRewardIdx=(currentTargetRewardIdx+1)%len(rewardArr)
        learn=1

    for wall in wallArr:
        if car_ship.collides_line_circle(wall[0],wall[1],wall[2],wall[3],10):
            print("Hit the wall!");
            learn=-1

    global learning_materials, frame_counter

    if(frame_counter>=100):
        learn=-1

    if learn==1:
        tf_learn(1);
        learning_materials = []
        frame_counter=0
    elif learn==-1:
        tf_learn(-1);
        generation_counter+=1
        print("generation_counter: " + str(generation_counter))
        learning_materials=[]
        frame_counter=0
        reset_one_game()
    else:
        learning_materials.append((observation,action,observation_)); #important
        frame_counter+=1

    if generation_counter%10==0:
        RL.persist()

def tf_learn( reward):
    global learning_materials
    for i in range(len(learning_materials)):
        learning_material=learning_materials[i]
        RL.store_transition(learning_material[0], learning_material[1], reward, learning_material[2])
    RL.learn()


    # if car_ship.dead:
    #     game_over_label.y = 300

    # global score
    # score += 10 * dt
    # score_label.text = "Score: {}".format(int(score))


if __name__ == "__main__":
    # Update the game 120 times per second
    pyglet.clock.schedule_interval(update, 1/9999999999.0)
    
    # Tell pyglet to do its thing
    pyglet.app.run()

