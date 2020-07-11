import random


def write_file(route,text):
    with open(route,'a') as file:
        file.write(text)


def get_random_line(route):
    with open(route,'r') as file:
        lines = file.readlines()
        text = random.choice(lines).replace('\n','')
        return text