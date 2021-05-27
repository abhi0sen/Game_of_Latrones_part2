"""Coded By- Abhisar Sen"""
"""Date - 27May 2021"""
"""Version 1"""
import pygame as pg
import math

#Canvas Configuration
pg.display.set_caption('Gaame of Latrones') 
caption  = pg.display.set_caption("Game Of Latrones")
icon = pg.image.load('cons.png')
pg.display.set_icon(icon)
blue = [0, 125, 255]
black =[0,0,0]
pink = [255,160,255]
brown = [125, 0, 0]
coordinate_x = [55, 134, 213,292,371,450,529,608,687,766,845,924]
coordinate_y = [50,110,170,230,290,350,410,470,530]
screen = pg.display.set_mode((1000,600))

class BoardDesign:
    """For designing all the content to be display on canvas screen"""
    def __init__(self, bg_color, grid_color, P1_lat_color, P2_lat_color):
        """To initialize the the class
        
        bg_color = background color of canvas
        grid_color = color of grid
        P1_lat_color = color of king Latrone(player1)
        P2_lat_color = color of king Latrone(player2)
        """
        self._bg_color = bg_color
        self._grid_color = grid_color
        self._P1_lat_color = P1_lat_color
        self._P2_lat_color = P2_lat_color

    def board_config(self):
        """desining board"""
        pg.draw.rect(screen, self._bg_color, pg.Rect(30, 30, 950, 550))

    def grid_config(self):
        """designing grid of board"""
        for i in range (0, 571, 61):
            pg.draw.lines(screen, self._grid_color,False, [(30,i+30),(980, i+30)], 2)
        for j in range(0,975, 79):
            pg.draw.lines(screen, self._grid_color, False,[(30+j, 30),(j+30, 580)], 2)
        
    def player_latrones(self):
        """Placing Latrones and kings of both the players at their respective position"""
        pg.draw.rect(screen, self._P1_lat_color, pg.Rect(443, 100, 45, 45))
        pg.draw.rect(screen, self._P2_lat_color, pg.Rect(522, 465, 45, 45))
        for i in range(len(coordinate_x)):
            latrone_i = pg.image.load('latrone_player1.png')
            screen.blit(latrone_i, (coordinate_x[i],coordinate_y[0]))
        for j in range(len(coordinate_x)):
            latrone_j = pg.image.load('latrone_player2.png')
            screen.blit(latrone_j, (coordinate_x[j]+1,coordinate_y[8]))
        pg.time.delay(100)

crashed = False
while not crashed:  #Make the game functioning
    screen.fill(black)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            crashed = True
            pg.time.delay(100)
        if pg.mouse.get_pressed() == (1,0,0):
            a = pg.mouse.get_pos()
            for new_i in range (len(coordinate_x)):
                for new_j in range(len(coordinate_y)):
                    dist = math.sqrt((pow(a[0]-coordinate_x[new_i],2)+(pow(a[1]-coordinate_y[new_j],2))))//1
                    if dist<=32:
                        x_co = new_i
                        y_co = new_j
                        pg.time.delay(100)
                        done = False
                        
                        while not done:
                            screen.fill(black)
                            print(coordinate_x[x_co], coordinate_y[y_co],a,(new_i, new_j))
                            for event in pg.event.get():
                                if event.type == pg.QUIT:
                                    done = True
                                if event.type == pg.KEYDOWN:
                                    if event.key == pg.K_SPACE:
                                        done = True
                                        
                                    if event.key == pg.K_RIGHT:
                                        coordinate_x[x_co] +=79
                                    if event.key == pg.K_DOWN:   
                                        #if y_co <8:
                                            #y_co +=1
                                        coordinate_y[y_co] +=60
                                    if event.key == pg.K_UP: 
                                        #if y_co>=0:
                                         #   y_co -=1
                                        coordinate_y[y_co]-=60
                                    if event.key == pg.K_LEFT:
                                        coordinate_x[x_co] -=79
                                        
                                    
                                    if coordinate_x[x_co]<0:
                                        coordinate_x[x_co] +=79
                                    if coordinate_y[y_co]<0:
                                        coordinate_y[y_co] +=60
                                    if coordinate_x[x_co]>945:
                                        coordinate_x[x_co] -=79
                                    if coordinate_y[y_co]>545:
                                        coordinate_y[y_co] -=60
                                    Latrones = BoardDesign(blue, brown, pink, black)
                                    Latrones.board_config()
                                    Latrones.grid_config()
                                    Latrones.player_latrones()
                                    pg.display.update()
        
    Latrones = BoardDesign(blue, brown, pink, black)
    Latrones.board_config()
    Latrones.grid_config()
    Latrones.player_latrones()
    pg.display.update()