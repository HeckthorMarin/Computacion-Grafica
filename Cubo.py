import pygame
from pygame.locals import *

import math
import random

ANCHO = 800
ALTO = 600
POSINI = 50
TAMINI = 100

VERDE = (34, 234, 54)
ROJO = (234, 34, 54)
AZUL = (34, 34, 224)
AMARILLO  = (94, 232, 216)
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

COLORES = [ VERDE, ROJO, AZUL, AMARILLO, BLANCO, NEGRO ]


class Cubo:

	def __init__(self, x, y, z):

		x = x
		y = ALTO / 2 - POSINI - y

		self.som = y

		self.ang = math.atan2(x,y)

		self.posx = ANCHO / 2 + x
		self.posy = ALTO / 2 + y
		self.posz = z

		self.xp = self.posx - self.posz*math.sin(self.ang)
		self.yp = self.posy - self.posz*math.cos(self.ang)

		self.m = (self.yp - self.posy) / (self.xp - self.posx)

		y = ALTO / 2 - POSINI
		x = y / self.m

		y += ALTO / 2
		x += ANCHO / 2

		self.tam1 = TAMINI

		self.p = [ x - self.tam1 / 2 , y ]
		self.m = (self.p[1] - ALTO / 2) / (self.p[0] - ANCHO / 2)

		self.pp1 = [ ANCHO / 2 + (self.yp - ALTO / 2) / self.m , self.yp ]

		self.tam1 = math.fabs(self.xp - self.pp1[0]) * 2

		self.pp2 = [ self.pp1[0] + self.tam1 , self.yp ]
		self.pp3 = [ self.pp2[0] , self.yp - self.tam1 ]
		self.pp4 = [ self.pp1[0] , self.pp3[1] ]


		self.xp2 = self.xp + self.tam1 * math.sin(self.ang)
		self.yp2 = self.yp + self.tam1 * math.cos(self.ang)

		self.pf1 = [ ANCHO / 2 + (self.yp2 - ALTO / 2) / self.m , self.yp2 ]

		self.tam2 = math.fabs(self.xp2 - self.pf1[0]) * 2

		self.pf2 = [ self.pf1[0] + self.tam2 , self.yp2 ]
		self.pf3 = [ self.pf2[0] , self.yp2 - self.tam2 ]
		self.pf4 = [ self.pf1[0] , self.pf3[1] ]


	def Puntos(self):
		s = [self.pp1, self.pp2, self.pf2, self.pf1]
		for punto in s:
			punto = [punto[0] , punto[1] + self.som]

		return [[self.pp1, self.pp2, self.pf2, self.pf1],
				[self.pp1, self.pp2, self.pp3, self.pp4],
				[self.pp2, self.pp3, self.pf3, self.pf2],
				[self.pp4, self.pp3, self.pf3, self.pf4],
				[self.pp1, self.pp4, self.pf4, self.pf1],
				[self.pf1, self.pf2, self.pf3, self.pf4],
				s]

	def Mostrar(self, pantalla):

		pygame.draw.polygon(pantalla, COLORES[random.randrange(6)], self.Puntos()[0])
		pygame.draw.polygon(pantalla, COLORES[random.randrange(6)], self.Puntos()[1])
		pygame.draw.polygon(pantalla, COLORES[random.randrange(6)], self.Puntos()[2])
		pygame.draw.polygon(pantalla, COLORES[random.randrange(6)], self.Puntos()[3])
		pygame.draw.polygon(pantalla, COLORES[random.randrange(6)], self.Puntos()[4])
		pygame.draw.polygon(pantalla, COLORES[random.randrange(6)], self.Puntos()[5])
		pygame.draw.polygon(pantalla, NEGRO, self.Puntos()[6])

	def Update(self, z):

		self.posz += z

		self.xp = self.posx + self.posz*math.sin(self.ang)
		self.yp = self.posy + self.posz*math.cos(self.ang)

		self.pp1 = [ ANCHO / 2 + (self.yp - ALTO / 2) / self.m , self.yp ]

		self.tam1 = math.fabs(self.xp - self.pp1[0]) * 2

		self.pp2 = [ self.pp1[0] + self.tam1 , self.yp ]
		self.pp3 = [ self.pp2[0] , self.yp - self.tam1 ]
		self.pp4 = [ self.pp1[0] , self.pp3[1] ]

		self.xp2 = self.xp + self.tam1 * math.sin(self.ang)
		self.yp2 = self.yp + self.tam1 * math.cos(self.ang)

		self.pf1 = [ ANCHO / 2 + (self.yp2 - ALTO / 2) / self.m , self.yp2 ]

		self.tam2 = math.fabs(self.xp2 - self.pf1[0]) * 2

		self.pf2 = [ self.pf1[0] + self.tam2 , self.yp2 ]
		self.pf3 = [ self.pf2[0] , self.yp2 - self.tam2 ]
		self.pf4 = [ self.pf1[0] , self.pf3[1] ]




if __name__ == "__main__":

	pygame.init()
	pantalla = pygame.display.set_mode([ANCHO,ALTO])

	cubos = []
	con = 0

	while con < 10:
		x = random.randrange(-ANCHO/2, ANCHO/2)
		z = random.randrange(-250,250)
		cub1 = Cubo(x, 1, z)
		cubos.append(cub1)
		print "agregado"
		con += 1


	cub1 = Cubo(100, 1, -200)
	#cub2 = Cubo(19, 245, 1)
	#cub3 = Cubo(23, 245, 1)

	cubos.append(cub1)
	#cubos.append(cub2)
	#cubos.append(cub3)

	z = 0.01

	pygame.display.flip()
	fin = False
	reloj = pygame.time.Clock()

	while not fin:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				fin = True

			key = pygame.key.get_pressed()

		pantalla.fill(COLORES[random.randrange(6)])

		if key[pygame.K_UP]:
			z += 0.01

		if key[pygame.K_DOWN]:
			z -= 0.01

		for cubo in cubos:
			cubo.Mostrar(pantalla)
			cubo.Update(z)


		pygame.display.flip()
		reloj.tick(60)
