from PIL import Image
import time
import pyautogui
import os
keep_track = "D:/upload yt/badascii/tracker.txt"
with open(keep_track, 'r') as file:
    i = int(file.read())
#with open(keep_track, 'r') as file:
    #i = file.read()
totalimage=13147;
while (i<totalimage):
    frame_number_str = f"{i:05d}"
    output_file_path = f"D:/upload yt/badascii/0{frame_number_str}.txt"
    
    with open(keep_track, 'w') as file:
        file.write(str(i));
    with open(output_file_path, 'r') as file:
        file_content = file.read()
        print(file_content)
            #print(file)
            #for line in file:
                #print(line.strip())
    
    time.sleep(1)
    screenshot = pyautogui.screenshot()
    filename = f"0{frame_number_str}.png"
    folder_path = "D:/upload yt/badss"
    full_path = os.path.join(folder_path, filename)
    screenshot.save(full_path)
    i+=1;