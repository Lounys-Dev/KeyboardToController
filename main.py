import json

import pygame
import pyautogui

from keyboard_conversion import To, keyboard_conversion

def debug_print(message: str):
    if settings["debug"]:
        print(message)

# Load mapping data from "map.json" and convert keywords to integers.
with open("map.json") as json_file:
    map_controller = json.load(json_file)
    reversed_dict_map_controller = {value: key for key, value in map_controller.items()}

# Load modification data from "modify.json".
with open("modify.json") as json_file:
    modifications = json.load(json_file)

# Load settings from "settings.json".
with open("settings.json") as json_file:
    settings = json.load(json_file)

# Initialize a dictionary to track button press states and associate each button with a False state. This is used for button press tracking.
is_pressed = {i: False for i in range(len(map_controller))}
print(is_pressed)

# Initialize Pygame and joystick support.
pygame.joystick.init()
pygame.init()
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
print("To quit, press ctrl+C")

while True:
    for event in pygame.event.get():
        # Loop through Pygame events.
        if event.type == pygame.QUIT:
            exit()

        if event.type == pygame.JOYBUTTONDOWN:
            for i in range(len(map_controller)):
                debug_print(f"Iteration: {i}")
                if pygame.joystick.Joystick(0).get_button(i):
                    try:
                        modifications[reversed_dict_map_controller[i]]
                    except KeyError:
                        continue
                    else:
                        debug_print("Key Down: Key Passed")
                        is_pressed[i] = True

                    if settings["keyboard"] == "azerty":
                        key = keyboard_conversion(modifications[reversed_dict_map_controller[i]], To.QWERTY)
                    elif settings["keyboard"] == "qwerty":
                        key = modifications[reversed_dict_map_controller[i]]
                    else:
                        raise ValueError(f"{settings['keyboard']} is not included in the list of supported keyboards")
                    debug_print(f"Key Down, original: {modifications[reversed_dict_map_controller[i]]} modified: {key}")
                    pyautogui.keyDown(key)

        if event.type == pygame.JOYBUTTONUP:
            for i in range(len(map_controller)):
                if not pygame.joystick.Joystick(0).get_button(i) and is_pressed[i]:
                    is_pressed[i] = False
                    if settings["keyboard"] == "azerty":
                        key = keyboard_conversion(modifications[reversed_dict_map_controller[i]], To.QWERTY)
                    elif settings["keyboard"] == "qwerty":
                        key = modifications[reversed_dict_map_controller[i]]
                    else:
                        raise ValueError(f"{settings['keyboard']} is not included in the list of supported keyboards")
                    debug_print(f"Key Up, original: {modifications[reversed_dict_map_controller[i]]} modified: {key}")
                    pyautogui.keyUp(key)
