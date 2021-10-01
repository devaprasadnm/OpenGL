import glfw
from OpenGL.GL import *
import numpy as np

glfw.init()

window = glfw.create_window(800,600,"PyOpenGL Triangle", None, None)
glfw.set_window_pos(window,400,200)
glfw.make_context_current(window)

vertices = [-0.5, -0.5, 0.0,
             0.5, -0.5,0.0,
             0.0, 0.5, 0.0]

v = np.array(vertices,dtype=np.float32)

glEnableClientState(GL_VERTEX_ARRAY)
glVertexPointer(3, GL_FLOAT,0,v)

glClearColor(0,0,0,0)

while not glfw.window_should_close(window):

glfw.poll_events()
glClear(GL_COLOR_BUFFER_BIT)

glDrawArrays(GL_TRIANGLES,0,3)
glfw.swap_buffers(window)

glfw.terminate()
