import pyautogui
import pygame
import keyboard
import time

images = ['final images\Image0.png', 
               'final images\Image1.png', 
               'final images\Image2.png',
               'final images\Image3.png',
               'final images\Image4.png',
               'final images\Image5.png',
               'final images\Image6.png',
               'final images\Image7.png',
               'final images\Image8.png',
               'final images\Image9.png',
               'final images\Image10.png',]

# varibles
sound_to_play = 'sounds\eep-02.wav'
confidence_value = 0.5
check_interval_secs = 1
grey_scale = False

# accuraecy 

def find_image_on_screen(images, sound_path, confidence=confidence_value):
    
    # start mixer module
    pygame.mixer.init()

    # create sound object
    sound = pygame.mixer.Sound(sound_path)

    while True:
        try:    
            for i, image_path in enumerate(images):
                # find image on screen
                location = pyautogui.locateOnScreen(image_path, confidence=confidence, grayscale=grey_scale)

                if location is not None:
                    print(f"Image found at: Location {i} {location}")
                    sound.play()
                # time.sleep(check_interval_secs)
                # print(str(check_interval_secs))
                
        except pyautogui.ImageNotFoundException:
            print("Image not found on screen.")

        if keyboard.is_pressed('pause'):
            print("Stopping script.")
            break
    
# run function
find_image_on_screen(images, sound_to_play)
