import random

aliens = ['./images/broccoli-gf94ba732b_1280.bmp',
          './images/carrot-g4eb2746b4_1280.bmp', './images/eggplant-g318e4a1fd_1280.bmp']

image = aliens[random.randrange(0, len(aliens))]
print(image)
