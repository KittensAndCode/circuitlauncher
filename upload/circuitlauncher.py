import os
import sys
import time
import board
import keypad
from ideaboard import IdeaBoard

def parse_programs(text):
    programs_list = text.split(",")
    programs = []
    for program in programs_list:
        parts = program.split(":")
        color = (int(parts[0]), int(parts[1]), int(parts[2]))
        prefix = parts[3]
        program_name = parts[4]
        program_object = {
            "name": program_name,
            "color": color,
            "prefix": prefix
        }
        programs.append(program_object)
    return programs

def getProgram(programs_list, hold_threshold):
    index = 0
    while True:
        ib.pixel = programs_list[index]['color']
        event = switch.events.get()
        if event:
            if event.pressed:
                press_time = time.monotonic()
            elif event.released:
                held_time = time.monotonic() - press_time
                if held_time < hold_threshold:
                    if len(programs_list) == index + 1:
                        index = 0
                    else:
                        index += 1
                    continue
                else:
                    sys.path.append(programs_list[index]['prefix'])
                    return index

ib = IdeaBoard()
pins = (board.IO0,)
switch = keypad.Keys(pins, value_when_pressed=False, pull=True)
HOLD_THRESHOLD = 1.0
press_time = None

programs_raw = os.getenv("PROGRAMS")
programs = parse_programs(programs_raw)

print(programs)

program = getProgram(programs, HOLD_THRESHOLD)
switch.deinit()
ib.deinit()
exec('import ' + programs[program]['name'])