import pygame
from numpy import pi, cos, sin
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

vertexes = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
)

edges = (
    (0, 1),
    (0, 3),
    (0, 4),
    (2, 1),
    (2, 3),
    (2, 7),
    (6, 3),
    (6, 4),
    (6, 7),
    (5, 1),
    (5, 4),
    (5, 7)
)

surfaces = (
    (0, 1, 2, 3),
    (3, 2, 7, 6),
    (6, 7, 5, 4),
    (4, 5, 1, 0),
    (1, 5, 7, 2),
    (4, 0, 3, 6)
)


def cube():
    glBegin(GL_QUADS)
    for surface in surfaces:
        for vertex in surface:
            glVertex3fv(vertexes[vertex])
    glEnd()

    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertexes[vertex])
    glEnd()


def draw_rectangle():
    glBegin(GL_QUADS)
    glColor3f(0.0, 0.4, 0.0)  # Kolor czerwony
    glVertex3f(2.5, -1.75, -2.5)
    glVertex3f(2.5, -1.75, 2.5)
    glVertex3f(-2.5, -1.75, 2.5)
    glVertex3f(-2.5, -1.75, -2.5)
    glEnd()


def sphere():
    quad = gluNewQuadric()
    gluQuadricNormals(quad, GLU_SMOOTH)
    gluQuadricTexture(quad, GL_TRUE)

    glPushMatrix()
    glColor3f(1.0, 1.0, 0.0)  # Kolor kuli
    glTranslatef(0, 0, -3)  # Przesunięcie kuli w przestrzeni
    gluSphere(quad, 0.9, 32, 32)  # Rysowanie kuli
    glPopMatrix()

def sphere_tree():
    quad = gluNewQuadric()
    gluQuadricNormals(quad, GLU_SMOOTH)
    gluQuadricTexture(quad, GL_TRUE)

    glPushMatrix()
    glColor3f(0.0, 0.4, 0.0)  # Kolor kuli
    glTranslatef(0, 0, 0)  # Przesunięcie kuli w przestrzeni
    gluSphere(quad, 0.5, 32, 32)  # Rysowanie kuli
    glPopMatrix()

def draw_cylinder(radius, height, num_segments):
    glBegin(GL_QUAD_STRIP)

    for i in range(num_segments + 1):
        glColor3f(0.6, 0.4, 0.2)
        theta = (2 * pi * i) / num_segments
        x = radius * cos(theta)
        y = radius * sin(theta)

        glVertex3f(x, -1.75, y)
        glVertex3f(x, height-1.75, y)

    glEnd()

    # Draw the bottom circle
    glBegin(GL_TRIANGLE_FAN)
    glVertex3f(0.0, -1.75, 0.0)  # Center of bottom circle
    for i in range(num_segments + 1):
        glColor3f(0.6, 0.4, 0.2)
        theta = (2 * pi * i) / num_segments
        x = radius * cos(theta)
        y = radius * sin(theta)

        glVertex3f(x, -1.75, y)

    glEnd()

    # Draw the top circle
    glBegin(GL_TRIANGLE_FAN)
    glVertex3f(0.0, height-1.75, 0.0)  # Center of top circle
    for i in range(num_segments + 1):
        glColor3f(0.6, 0.4, 0.2)
        theta = (2 * pi * i) / num_segments
        x = radius * cos(theta)
        y = radius * sin(theta)

        glVertex3f(x, height-1.75, y)

    glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0, 0, -8)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(0.5, 0, 1, 0)  # 1szy argument to predkosc
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glClearColor(0.7, 0.7, 1.0, 1.0)  # Tło niebieskie
        # cube()
        sphere()
        draw_rectangle()
        draw_cylinder(0.2, 2, 100)
        sphere_tree()

        pygame.display.flip()
        pygame.time.wait(10)


if __name__ == "__main__":
    main()
