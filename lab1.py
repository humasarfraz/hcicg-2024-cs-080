import glfw
from OpenGL.GL import *
import sys

def main():
    if not glfw.init():
        print("GLFW initialization failed")
        return

    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    window = glfw.create_window(
        800, 600,
        "HCI & CG Lab 1 - OpenGL Window",
        None, None
    )

    if not window:
        print("Window creation failed. OpenGL 3.3 may not be supported.")
        glfw.terminate()
        return

    glfw.make_context_current(window)

    print("OpenGL Version:", glGetString(GL_VERSION).decode())
    print("Renderer:", glGetString(GL_RENDERER).decode())

    while not glfw.window_should_close(window):
        glClearColor(0.15, 0.10, 0.25, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)

        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()