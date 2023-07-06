import pyautogui,random,time,keyboard,sys
viewonly=True # Disable only on your risk
if viewonly:
    print('Warning! Disabling viewonly may click on something wrong')
while True:
    time.sleep(random.randint(0,300)*0.01) # Wait
    action = random.randint(1,3) # Pick event bettwen 1 and 3
    if keyboard.is_pressed('p'): # Close program if p is held
        sys.exit()
    x,y = pyautogui.position() # Obantain x,y coordinates of mouse
    if action == 1:
        x1 = random.randint(-50,50)
        y1 = random.randint(-50,50)
        pyautogui.moveTo(x+x1,y+y1,duration=0.2) # Move mouse to random position
    elif action == 2 and not viewonly:
        pyautogui.mouseDown()
        x1 = random.randint(-50,50)
        y1 = random.randint(-50,50)
        pyautogui.moveTo(x+x1,y+y1,duration=0.2) # Move mouse to random position
        pyautogui.mouseUp()
        
    elif action == 2 and viewonly:
        print('Action "click" Is disabled!') # Tell user that click is disabled
