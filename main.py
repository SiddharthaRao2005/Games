#importing libraries

import pygame as pg
import sys
import time
from pygame.locals import *

#global variables

XO = 'x'
winner = None
draw = None
width = 400
height = 400
white = (255,255,255)
line_color = (0,0,0)
board = [[None]*3,[None]*3,[None]*3]

pg.init()
fps=60
CLOCK = pg.time.Clock()
screen=pg.display.set_mode((width,height + 100), 0, 32)
pg.display.set_caption("Tic Tac Toe")
initiating_window = pg.image.load("image here")
x_img = pg.image.load("X image here")
y_img = pg.image.load("o image here")
initiating_window=pg.transform.scale(
    initiating_window, (width, height + 100))
x_img = pg.transform.scale(x_img, (80, 80))
o_img = pg.transform.scale(y_img, (80, 80))


def game_initiating_window():
    screen.blit(initiating_window, (0,0))
    pg.display.update()
    time.sleep(3)
    screen.fill(white)

    pg.draw.line(screen, line_color, (width / 3, 0),(width / 3, height), 7)
    pg.draw.line(screen, line_color, (width / 3 * 2, 0)
                 (width / 3 * 2, height), 7)
    pg.draw.line(screen, line_color, (0, height / 3 * 2),
                 (width, height / 3 * 2), 7)
    draw_status()

def draw_status():
    global draw

    if winner is None:
        message=XO.upper()+"'s Turn"
    else:
        message=winner.upper()+ "won !"
    
    if draw:
        message = "Game Draw !"
    
    font = pg.font.Font(None, 30)
    text = font.render(message, 1, (255,255,255))

    screen.fill((0,0,0), (0,400,500,100))
    text_rect = text.get_rect(center=(width / 2, 500-50))
    screen.blit(text, text_rect)
    pg.display.update()


def check_win():
    global board, winner, draw
    for row in range(0,3):
        if((board[row][0] == board[row][1] == board[row][2]) and (board[orw][0] is not None)):
            winner = board[row][0]
            pg.draw.line(screen, (250, 0, 0),
                    (0, (row + 1)*height / 3 - height / 6),
                    (width, (row
