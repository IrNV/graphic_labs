from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *

"""
    trianglesList includes triangles
    quadranglesList includes quadrangle
"""
trianglesList = []
quadranglesList = []
trCoef = [[1, 0, 0], [0, 1, 0], [-1, 0, 0], [0, -1, 0]]


def shiftR():
    for i in range(len(trCoef) - 1):
        trCoef[len(trCoef) - i - 1], trCoef[len(trCoef) - i - 2] = trCoef[len(trCoef) - i - 2]\
            , trCoef[len(trCoef) - i - 1]


def shiftL():
    for i in range(len(trCoef) - 1):
        trCoef[i], trCoef[i + 1] = trCoef[i + 1], trCoef[i]


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Triangle:
    def __init__(self, point1, point2, point3):
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3

    def draw(self):
        glBegin(GL_TRIANGLES)
        glColor3ub(255, 160, 0)
        glVertex2d(self.point1.x, self.point1.y)
        glVertex2d(self.point2.x, self.point2.y)
        glVertex2d(self.point3.x, self.point3.y)
        glEnd()

        self.drawTriangleLine()

    def drawTriangleLine(self):
        """
            Draw triangle border
        """
        glBegin(GL_LINES)
        glColor3ub(0, 0, 0)

        glVertex2d(self.point1.x, self.point1.y)
        glVertex2d(self.point2.x, self.point2.y)

        glVertex2d(self.point2.x, self.point2.y)
        glVertex2d(self.point3.x, self.point3.y)

        glVertex2d(self.point3.x, self.point3.y)
        glVertex2d(self.point1.x, self.point1.y)
        glEnd()


class Quadrangle:
    def __init__(self, point1, point2, point3, point4):
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3
        self.point4 = point4

    def draw(self):
        glBegin(GL_POLYGON)
        glColor3ub(255, 160, 0)
        glVertex2d(self.point1.x, self.point1.y)
        glVertex2d(self.point2.x, self.point2.y)
        glVertex2d(self.point3.x, self.point3.y)
        glVertex2d(self.point4.x, self.point4.y)
        glEnd()

        self.drawQuadrangleLine()

    def drawQuadrangleLine(self):
        """
            Draw polygon border
        """
        glBegin(GL_LINES)
        glColor3ub(0, 0, 0)

        glVertex2d(self.point1.x, self.point1.y)
        glVertex2d(self.point2.x, self.point2.y)

        glVertex2d(self.point2.x, self.point2.y)
        glVertex2d(self.point3.x, self.point3.y)

        glVertex2d(self.point3.x, self.point3.y)
        glVertex2d(self.point4.x, self.point4.y)

        glVertex2d(self.point4.x, self.point4.y)
        glVertex2d(self.point1.x, self.point1.y)
        glEnd()

def initFigure():
    """
        Init Figure witch consists of triangles (tr) and polygons (quard) and
        then we add triangles and polygons to lists
    """
    tr1 = Triangle(Point(0.0, 0.0), Point(2.0, 2.0), Point(2.0, 0.0))
    trianglesList.append(tr1)

    quard1 = Quadrangle(Point(2.0, -1.0), Point(2.0, 2.0),
                     Point(2.0 + sqrt(2), 2 - sqrt(2)), Point(2 + sqrt(2), -1 - sqrt(2)))
    quadranglesList.append(quard1)

    quard2 = Quadrangle(Point(quard1.point1.x - sqrt(2), quard1.point1.y - sqrt(2)),
                     quard1.point1, quard1.point4, Point(quard1.point1.x, quard1.point1.y - 2 * sqrt(2)))
    quadranglesList.append(quard2)

    tr2 = Triangle(quard2.point4, Point(quard2.point4.x + sqrt(7),
                                     2 * quard2.point3.y - quard2.point4.y), Point(quard2.point4.x + 3 * 2, quard2.point4.y))
    trianglesList.append(tr2)

    tr3 = Triangle(tr2.point1, Point(tr2.point1.x + 2 * 2, tr2.point1.y),
                   Point(tr2.point1.x + 2 * 2, tr2.point1.y - 2 * 2))
    trianglesList.append(tr3)

    tr4 = Triangle(Point(tr3.point1.x + sqrt(7), tr3.point3.y + (tr3.point2.y - tr3.point3.y) / (2 * sqrt(2))),
                   Point(2 * tr3.point3.x - sqrt(7) - tr3.point1.x,
                         tr3.point3.y - (tr3.point2.y - tr3.point3.y) / 4),
                   Point(tr3.point1.x + sqrt(7), tr3.point3.y + (tr3.point2.y - tr3.point3.y) / 4 -
                         (tr3.point2.x - tr3.point1.x)))
    trianglesList.append(tr4)

    tr5 = Triangle(Point((tr4.point3.x + tr4.point2.x) / 2 - 2 * sqrt(2),
                         (tr4.point3.y + tr4.point2.y) / 2 - 2),
                   Point((tr4.point3.x + tr4.point2.x) / 2,
                         (tr4.point3.y + tr4.point2.y) / 2),
                   Point((tr4.point3.x + tr4.point2.x) / 2,
                         (tr4.point3.y + tr4.point2.y) / 2 - 2))
    trianglesList.append(tr5)

def initFun():
    #glLoadIdentity()
    gluOrtho2D(-15.0, 15.0, -15.0, 15.0)
    glLineWidth(3);
    initFigure()


def displayFun():

    glClear(GL_COLOR_BUFFER_BIT)


    for figure in range(len(trianglesList)):
        trianglesList[figure].draw()

    for figure in range(len(quadranglesList)):
        quadranglesList[figure].draw()

    glFlush()


def specialKeyboardFun(button, x, y):
    """
        Translate figure
    """
    if button == GLUT_KEY_RIGHT:
        glTranslate(trCoef[0][0], trCoef[0][1], trCoef[0][2])
    if button == GLUT_KEY_UP:
        glTranslate(trCoef[1][0], trCoef[1][1], trCoef[1][2])
    if button == GLUT_KEY_LEFT:
        glTranslate(trCoef[2][0], trCoef[2][1], trCoef[2][2])
    if button == GLUT_KEY_DOWN:
        glTranslate(trCoef[3][0], trCoef[3][1], trCoef[3][2])

    glutPostRedisplay()


def keyboardFun(button, x, y):
    if button == b'-':
        glScale(0.5, 1, 0)
    if button == b'+':
        glScale(2, 1, 0)

    """
        Rotate figure
    """
    if button == b'r':
        glRotate(90, 0, 0, 1)
        shiftR()

    if button == b't':
        glRotate(-90, 0, 0, 1)
        shiftL()

    glutPostRedisplay()


glutInit()
glutInitWindowSize(500, 500)
glutCreateWindow(b"Heron")
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glClearColor(0, 0, 1, 1)
glutDisplayFunc(displayFun)
glutKeyboardFunc(keyboardFun)
glutSpecialFunc(specialKeyboardFun)
initFun()
glutMainLoop()
