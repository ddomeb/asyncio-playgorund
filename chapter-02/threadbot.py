import threading
import sys
# from typing import Self
from queue import Queue
from time import sleep
from random import randint

class Cutlery:
    def __init__(self, knives=0, forks=0) -> None:
        self.knives = knives
        self.forks = forks
        self.lock = threading.Lock()

    def give(self, to, knives, forks):
        self.change(-knives, -forks)
        to.change(knives, forks)

    def change(self, knives, forks):
        # self.knives += knives
        # self.forks += forks
        # simply adding knives and forks didn't really break the code
        # probably too fast, so I added some calculation overhead
        with self.lock:
            self.knives += knives + (randint(1, 1000) * 0)
            self.forks += forks + (randint(1, 1000) * 0)
    
    def __repr__(self) -> str:
        return f'knives: {self.knives}, forks: {self.forks}'

kitchen = Cutlery(knives=100, forks=100)

class ThreadBot(threading.Thread):
    def __init__(self):
        super().__init__(target=self.manage_table)
        self.cutlery = Cutlery()
        self.tasks = Queue()


    def manage_table(self):
        while True:
            task = self.tasks.get()
            if task == 'prepare table':
                kitchen.give(to=self.cutlery, knives=4, forks=4)
            elif task == 'clear table':
                self.cutlery.give(to=kitchen, knives=4, forks=4)
            elif task == 'shutdown':
                return

bots = [ThreadBot() for _ in range(10)]

if __name__ == '__main__':
    for bot in bots:
        for i in range(int(sys.argv[1])):
            bot.tasks.put('prepare table')
            bot.tasks.put('clear table')
        bot.tasks.put('shutdown')

    print('Kitchen inventory before service:', kitchen)

    for bot in bots:
        bot.start()

    for bot in bots:
        bot.join()
    print('Kitchen inventory after service:', kitchen)


