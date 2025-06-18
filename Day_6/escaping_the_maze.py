"""Escape the maze"""

from random import randint


def turn_left():
    """Turn left"""
    print("Turning left")


def front_is_clear():
    """Check if front is clear"""
    print("Front is clear")


def at_goal():
    """Check if at goal"""
    print("At goal")


def move():
    """Move"""
    print("Moving")


def turn_right():
    """Turn right"""
    turn_left()
    turn_left()
    turn_left()


while not at_goal():
    if front_is_clear():
        move()
    if randint(0, 2) == 1:
        turn_right()
    else:
        turn_left()
