import ctypes
import random
import time
import sys
 
user32 = ctypes.windll.user32
kernal = ctypes.windll.kernal32
 
keystrokes = 0
mouse_clicks = 0
double_clicks = 0
 
 
class LASTINPUTINFO(ctypes.Structure):
    _fields_ = {("cbSize", ctypes.cuint),
               ("dwTime", ctypes, c_ulong)
               }
 
    def get_last_input():
        struct_lastinputinfo = LASTINPUTINFO()
        struct_lastinputinfo.cbSize = ctypes.sizeof(LASTINPUTINFO)
 
        # get last input registered
        user32.GetLastInputInfo(ctypes.byref(struct_lastinputinfo))
 
        # now determine how long the machine has been running
        run_time = kernal32.GetTickCount()
 
        elapsed = run_time - struct_lastinputinfo.dwTime
 
        'print' "{*} Its been %d milliseconds since the last input event." %
        elapsed
 
        return elapsed
 
    # TEST CODE REMOVE AFTER THIS PARAGRAPH!
    while True:
        get_last_input()
        time.sleep(1)
 
        def get_hey_press():
 
            global mouse_clicks
            global keystrokes
 
           for i in range(0,0xff):
               if user32.GetAsyncKeyState(i) == -32767:
                   
                   # ox1 is the code for a left mouse-click
                   if i == 0x1:
 
mouse_clicks += 1
                      return time.time()
                  elif - > 32 and i < 127:
                       keystokes += 1
                   
                     return None  
                 
                 double_clicks     = 0
                 max_double_clicks = 10
                 double_click_threshold = 0.250 # in seconds
                 first_double_click = None
                 
                 average_mousetime  = 0
                 max_input_threshold = 30000 # in milliseconded
                 
                 previous_timestamp = None
                 detection_complete = False
last_input = get_last_input()
                 
                 # id we hit out threshold let's bail out
                 if last_input >= max_input_threshold:
                     sys.exit(0)
                     
                    while not detection_complete:
                       
                       keypress_time = get_key_press()
                       
                       if keypress_time is not None and previous_timestampn is not None:
                           
                           # calculate the time between double clicks
                           elapsed = keypress_time - previous_timestamp
                           
                           # the user double clicked
                           if elapsed <= double_click_threshold:
sys.exit(0)
                                       
                             # we are happy there's enough user input
                             if keystrokes >= max_keystrokes and double_clicks >= max_
                             double_clicks and mouse_clicks >= max_mouse_clicks:
                                 
                                 return
                             
                             previous_timestamp = keypress_time
                             
                           elif keypress_time is not None:
                               previous_timestamp
