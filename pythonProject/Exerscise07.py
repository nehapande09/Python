# =============================================== EXERSCISE 07 ===================================================================
# Healthy Programmer :
"""
9 am - 5pm
water - water.mp3(3.5 litre) - Drank -log
Eyes - Eyes.mp3(30 mins )- EyDone - log
Physical Activity _ physical.mp3- every 45 mins -ExDone -log
pygame module to play audio
"""
from pygame import mixer
mixer.init()
mixer.music.load("C:\Users\DELL\Music\Music\Maroon 5 - Girls Like You ft. Cardi B (Official Music Video)")
mixer.music.set_volume(0.5)
mixer.music.play()
