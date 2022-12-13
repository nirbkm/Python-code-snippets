import winsound
from playsound import playsound


sounds_path = (
    "C:\\Nir_PC\\Nir\\Programming\\Python\\Projects\\Graphenea_chipTester_v2\\"
)


# try:
# while True:
# x = input()
# winsound.PlaySound(sounds_path + "ok.wav", winsound.SND_NOWAIT)
# except KeyboardInterrupt:
# print("interrupted!")


for x in range(100):
    input()
    # winsound.PlaySound(sounds_path + "beep.wav", winsound.SND_NOSTOP)
    playsound(sounds_path + "beep.wav")
