# mx-finder
### Designed specifically for a game called Total Battle to help find a Mercenary Exchange on the world map.
### Short script that cycles through a list of images and beeps if one of them appears on screen.
### Only works on 1080p resolution due to the specific dimentions of the included images.

# varibles
### sound_to_play = file location of the beep sound
### confidence_value = a float between 0 and 1 used to adjust the accuracy of detecting an image, 1 means 100% match only. requires the Open_CV library.
### check_interval_secs = how often the script will cycle through the image list. Dependant on processing power and internet speed.
### grey_scale = boolean value. if set to True, it will only look for the greyscale version. I had more success with this set to True.

