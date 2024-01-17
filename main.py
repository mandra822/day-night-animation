import pygame
from numpy import pi, cos, sin
from PIL import Image
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from glfw.GLFW import *

image = None
image2 = None
mat_ambient = [1.0, 1.0, 1.0, 1.0]
mat_diffuse = [1.0, 1.0, 1.0, 1.0]
mat_specular = [1.0, 1.0, 1.0, 1.0]
mat_shininess = 20.0

light_ambient = [0.1, 0.1, 0.0, 1.0]
light_diffuse = [0.8, 0.8, 0.0, 1.0]
light_specular = [1.0, 1.0, 1.0, 1.0]
light_position = [0.0, 0.0, 10.0, 1.0]

att_constant = 1.0
att_linear = 0.05
att_quadratic = 0.001


def startup():
    global image, image2
    glEnable(GL_TEXTURE_2D)
    glEnable(GL_CULL_FACE)
    glTexEnvi(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

    image = Image.open("trawa.tga")
    image2 = Image.open("pien.jpg")

    glMaterialfv(GL_FRONT, GL_AMBIENT, mat_ambient)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
    glMaterialf(GL_FRONT, GL_SHININESS, mat_shininess)

    glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)
    glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular)
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)

    glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, att_constant)
    glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, att_linear)
    glLightf(GL_LIGHT0, GL_QUADRATIC_ATTENUATION, att_quadratic)

    glShadeModel(GL_SMOOTH)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)


def draw_square():
    glTexImage2D(
        GL_TEXTURE_2D, 0, 3, image.size[0], image.size[1], 0,
        GL_RGB, GL_UNSIGNED_BYTE, image.tobytes("raw", "RGB", 0, -1)
    )
    glEnable(GL_TEXTURE_2D)
    glBegin(GL_TRIANGLES)

    glTexCoord2f(0.0, 0.0)
    glVertex3f(-5.0, -1.75, -5.0)

    glTexCoord2f(0.0, 2.0)
    glVertex3f(-5.0, -1.75, 5.0)

    glTexCoord2f(2.0, 2.0)
    glVertex3f(5.0, -1.75, 5.0)

    glTexCoord2f(0.0, 0.0)
    glVertex3f(-5.0, -1.75, -5.0)

    glTexCoord2f(2.0, 2.0)
    glVertex3f(5.0, -1.75, 5.0)

    glTexCoord2f(2.0, 0.0)
    glVertex3f(5.0, -1.75, -5.0)

    glEnd()
    glDisable(GL_TEXTURE_2D)


def sun():
    global light_position, light_diffuse, light_specular, light_ambient, mat_ambient, mat_diffuse, mat_specular
    quad = gluNewQuadric()
    gluQuadricNormals(quad, GLU_SMOOTH)

    glPushMatrix()
    light_diffuse = [1.0, 1.0, 0.0, 1.0]  # Żółte światło dla słońca
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)

    light_specular = [1.0, 1.0, 1.0, 1.0]
    glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular)

    light_ambient = [0.9, 0.5, 0.0, 1.0]
    glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)

    mat_ambient = [1.0, 1.0, 0.0, 1.0]  # Żółty kolor dla materiału
    glMaterialfv(GL_FRONT, GL_AMBIENT, mat_ambient)

    mat_diffuse = [1.0, 1.0, 0.0, 1.0]  # Żółty kolor dla materiału
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)

    mat_specular = [1.0, 1.0, 0.0, 1.0]  # Żółty kolor dla materiału
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)

    glTranslatef(0, 5, -3)
    light_position[1] += 5
    light_position[2] += -3
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)
    gluSphere(quad, 0.9, 32, 32)

    glPopMatrix()


def moon():
    global light_position, light_diffuse, light_specular, light_ambient, mat_ambient, mat_diffuse, mat_specular
    quad = gluNewQuadric()
    gluQuadricNormals(quad, GLU_SMOOTH)

    glPushMatrix()
    light_diffuse = [1.0, 1.0, 0.0, 1.0]
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)

    light_specular = [1.0, 1.0, 1.0, 1.0]
    glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular)

    light_ambient = [0.5, 1.0, 1.0, 1.0]
    glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)

    mat_ambient = [1.0, 1.0, 1.0, 1.0]
    glMaterialfv(GL_FRONT, GL_AMBIENT, mat_ambient)

    mat_diffuse = [1.0, 1.0, 0.0, 1.0]
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)

    mat_specular = [1.0, 1.0, 0.0, 1.0]
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)

    glTranslatef(5, 1, -3)
    light_position[0] += 5
    light_position[1] += 1
    light_position[2] += -3
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)
    gluSphere(quad, 0.9, 32, 32)

    glPopMatrix()


def sphere_tree():
    global light_position, light_diffuse, light_specular, light_ambient, mat_ambient, mat_diffuse, mat_specular
    quad2 = gluNewQuadric()
    gluQuadricNormals(quad2, GLU_SMOOTH)

    glPushMatrix()
    light_diffuse = [1.0, 1.0, 0.0, 1.0]
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)

    light_specular = [1.0, 1.0, 1.0, 1.0]
    glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular)

    light_ambient = [0.0, 0.5, 0.0, 1.0]
    glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)

    mat_ambient = [1.0, 1.0, 0.0, 1.0]
    glMaterialfv(GL_FRONT, GL_AMBIENT, mat_ambient)

    mat_diffuse = [1.0, 1.0, 0.0, 1.0]
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)

    mat_specular = [1.0, 1.0, 0.0, 1.0]
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)

    glTranslatef(0, 0, 0)

    glLightfv(GL_LIGHT0, GL_POSITION, light_position)
    gluSphere(quad2, 0.5, 32, 32)

    glPopMatrix()


def draw_cylinder(radius, height, num_segments):
    glTexImage2D(
        GL_TEXTURE_2D, 0, 3, image2.size[0], image2.size[1], 0,
        GL_RGB, GL_UNSIGNED_BYTE, image2.tobytes("raw", "RGB", 0, -1)
    )
    glEnable(GL_TEXTURE_2D)
    glBegin(GL_QUAD_STRIP)

    for i in range(num_segments + 1):

        theta = (2 * pi * i) / num_segments
        x = radius * cos(theta)
        y = radius * sin(theta)

        u = i / num_segments
        v_bottom = 0.0
        v_top = 1.0

        glTexCoord2f(u, v_bottom)
        glVertex3f(x, -1.75, y)

        glTexCoord2f(u, v_top)
        glVertex3f(x, height - 1.75, y)

    glEnd()
    glDisable(GL_TEXTURE_2D)

    glBegin(GL_TRIANGLE_FAN)
    glVertex3f(0.0, -1.75, 0.0)
    for i in range(num_segments + 1):
        theta = (2 * pi * i) / num_segments
        x = radius * cos(theta)
        y = radius * sin(theta)

        glVertex3f(x, -1.75, y)

    glEnd()

    glBegin(GL_TRIANGLE_FAN)
    glVertex3f(0.0, height - 1.75, 0.0)
    for i in range(num_segments + 1):
        theta = (2 * pi * i) / num_segments
        x = radius * cos(theta)
        y = radius * sin(theta)

        glVertex3f(x, height - 1.75, y)

    glEnd()


def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 100.0)
    glTranslatef(0, 0, -8)
    startup()
    sun_rotation = 0.0
    moon_rotation = 240.0

    zoom_speed = 0.1
    translation_speed = 0.2

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    glTranslatef(0, 0, translation_speed)
                elif event.key == pygame.K_DOWN:
                    glTranslatef(0, 0, -translation_speed)
                elif event.key == pygame.K_LEFT:
                    glTranslatef(-translation_speed, 0, 0)
                elif event.key == pygame.K_RIGHT:
                    glTranslatef(translation_speed, 0, 0)
                elif event.key == pygame.K_PAGEUP:
                    glTranslatef(0, translation_speed, 0)
                elif event.key == pygame.K_PAGEDOWN:
                    glTranslatef(0, -translation_speed, 0)
                elif event.key == pygame.K_PLUS or event.key == pygame.K_KP_PLUS:
                    glTranslatef(0, 0, zoom_speed)
                elif event.key == pygame.K_MINUS or event.key == pygame.K_KP_MINUS:
                    glTranslatef(0, 0, -zoom_speed)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glClearColor(0.7, 0.7, 1.0, 1.0)  # Tło niebieskie

        draw_square()
        draw_cylinder(0.2, 2, 100)
        sphere_tree()

        if sun_rotation < 100 or sun_rotation > 250:
            glPushMatrix()
            glRotatef(sun_rotation, 0, 0, 1)
            sun()
            glPopMatrix()
        else:
            glClearColor(0.0, 0.0, 0.5, 1.0)
            glPushMatrix()
            glRotatef(moon_rotation, 0, 0, 1)
            moon()
            glPopMatrix()

        moon_rotation += 0.5
        sun_rotation += 0.5
        if sun_rotation == 360:
            sun_rotation = 0.0
        if moon_rotation == 110:
            moon_rotation = 250.0

        pygame.display.flip()
        pygame.time.wait(10)


if __name__ == "__main__":
    main()
