import sounddevice as sd
from scipy.io.wavfile import write
import time

freq = 44100
duration = float(input("Enter the length that you want to be duration of your record: "))
x = 3
while x >= 0:
    print('\x08' * 100, f"{x} seconds left to start", end='' ,flush= True)
    time.sleep(0.25)
    x -= 0.25
print('\n' "Recording...")

print(f"{round(duration , 2)} seconds left\r")
rec = sd.rec(int(duration * freq), samplerate = freq , channels = 2)

while duration > 0:
    if duration > 1:
        time.sleep(1)
        duration = duration - 1
        print(f"{round(duration , 2)} seconds left")
    else:
        time.sleep(0.25)
        duration = duration - 0.25
        print(f"{round(duration, 2)} seconds left\r")
print("The record has been successfully saved !!! ")

write("ax.wav", freq, rec)

