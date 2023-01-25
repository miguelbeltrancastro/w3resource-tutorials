import math
import matplotlib.pyplot as plt
import numpy as np

igure, axes = plt.subplots()
Drawing_uncolored_circle = plt.Circle( (0.5, 0.5 ),0.5 ,fill = False )
axes.add_artist( Drawing_uncolored_circle )

x=0

while x <=math.pi*2:
    Drawing_uncolored_circle = plt.Circle( (math.cos(x)+0.5, math.sin(x)+0.5 ),0.5 ,fill = False )
    axes.add_artist( Drawing_uncolored_circle )
    x = x + 0.05

axes.set_aspect( 1 )

plt.title( 'Circle' )
plt.show()