############################################################################r##############################################################################################################
# AUTHOR: Daniel Genkin                                                                                                                                                                  
# REVISION DATE: 2018/06/07                                                                                                                                              
# PROGRAM NAME: PyFlap                                                                                                                                                      
# PROGRAM DESCRIPTION: Flappy bird re-creation in python for the windows command prompt
##########################################################################################################################################################################################

#used to clear the screen every "frame"
import os
import random

def cls():
     #print ("\n" * 40)# use for idle
     os.system('cls')# use for cmd (works better)

# Code to check if left mouse button was pressed
import win32api
import time
def mouseMonitor(framesMissed, bird1, bird2):
      state_left = win32api.GetKeyState(0x20)

      score = 0
      pipeLoc = 40
      holeLoc = random.randrange(4,20)
      while True:
          a = win32api.GetKeyState(0x20)

          framesMissed+=1
                        
          if a != state_left:#detect space button
              state_left = a
              if a < 0:
                if framesMissed > -15:
                    framesMissed -= 15
                    score +=1
                    ret = render(framesMissed, pipeLoc, score, holeLoc)
                    pipeLoc = ret[1]
                    holeLoc = ret[2]
                    if ret[0] == False:
                        break
                    continue
                    
          ret = render(framesMissed, pipeLoc, score, holeLoc)
          pipeLoc = ret[1]
          holeLoc = ret[2]
          if ret[0] == False:
             break
      #pause in cmd to avoid closing immidietly        
      os.system('pause')
      if str(input("Would you like to try again (Y/N)")).lower() == "y":
          setup()

def setup():
    framesMissed = 0
    bird1 = ' ("<\n / )\n  L' # falling
    bird2 = '\ ("<\n   )\n  L' # flapping
    if countdown(3):
         mouseMonitor(framesMissed, bird1, bird2)

def countdown(timeLeft):
     while timeLeft > 0:
        timeLeft -= 1
        print(" " + str(timeLeft + 1))
        time.sleep(1)
     cls()
     return True

def render(framesMissed, pipeLoc, score, holeLoc):#add if hit pipe (when 1 frame between pipe and bird) loose
        #draw scene
        pipeLoc -= 1
        if pipeLoc < -5:#generate new pipes
           pipeLoc = 40
           holeLoc = random.randrange(4,20)

        scene = ""
        disTop = framesMissed/2
        
        for row in range(0,25):
            for column in range(0,45):#DRAW SCENE
                if row == 0 or row == 24:#if ground or roof, draw
                   scene +="-"
                   continue

                #draw bird
                elif row == disTop and column == 1:
                   scene += '<'

                elif row == disTop + 1 and column == 1:
                   scene += '|'

                elif row == disTop + 2 and column == 1:
                   scene += 'L'

                else:
                   scene += " "
                   
                #draw pipes
                if (row <= (holeLoc - 4) or row >= (holeLoc + 4)) and column == pipeLoc:
                    scene += "[|--|]"
                    break

            scene += "\n"


        print(scene)
                
        #detect loose from ground ADD FROM HITING PIPES
        if disTop >= 22 or disTop <= -5:
           print("YOU LOOSE!! "  + ("Flap harder, you lazy birdy! You fell out of the sky" if(disTop >= 22) else "What are on, steroids? You hit the roof!")+ " \n Your score: " + str(score))
           return False, pipeLoc, holeLoc
        #detect hitting pipes
        elif pipeLoc <= 0 and (disTop >= (holeLoc + 4) or disTop <= (holeLoc - 4)):
           print("YOU LOOSE!! Are you blind. There is clearly a pipe there! \n Your score: " + str(score))
           return False, pipeLoc, holeLoc
        else:
            #clear
            cls()

        return True, pipeLoc, holeLoc

setup()



