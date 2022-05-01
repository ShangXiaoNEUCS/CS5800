'''
ChaCha20 Visualization Module
CS5800, Spring 2022
Professor Jamieson
Nathaniel Webb, Aaron Fihn, Prateep Malyala, Shang Xiao
'''

import time
from graphics import *
from word import Word

class ChaChaViz:
    def __init__(self):
        self.win = GraphWin("ChaCha20", 640, 480)
        self.win.setBackground("white")

    def clear(self):
        for item in self.win.items[:]:
            item.undraw()
        self.win.update()

    def display(self):
        time.sleep(0.5)
        self.clear()

    def end(self):
        self.win.close()
    
    def add(self, start_block, end_block, from_index, to_index):
        self.print_block(start_block, False, from_index, to_index, '+')
        self.print_block(end_block, True, to_index)
        self.display()

    def block(self, block):
        self.print_block(block, False)
        self.display()

    def xor(self, start_block, end_block, from_index, to_index):
        self.print_block(start_block, False, from_index, to_index, '^')
        self.print_block(end_block, True, to_index)
        self.display()

    def lrot(self, start_block, end_block, index):
        self.print_block(start_block, False, index, index, '<')
        self.print_block(end_block, True, index)
        self.display()

    def qround(self, start_block, end_block, indices):
        self.add(start_block, end_block, indices[0], indices[1])

    def print_block(self, block, second_block, index_a = None, index_b = None, operator = None):
        for i in range(16):
            print_color = 'black'
            if (i == index_a):
                print_color = 'blue' if second_block else 'green'
            elif (i == index_b):
                print_color = 'red'

            x_offset = i%4
            y_offset = i//4
            block_offset = 150 if second_block else 0;

            x = 160 + 110 * x_offset
            y = 75 + 30 * y_offset + block_offset

            message = Text(Point(x, y), str(block[i]))
            message.setTextColor(print_color)
            message.draw(self.win)

            if (i == index_b and operator is not None):
                op_message = Text(Point(x - 51, y - 1), operator)
                op_message.draw(self.win)
