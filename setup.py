import os
import time
question = input("Are you install android package for using android_payload.py?[Y/N]: ")
if question == "Y":
    os.system("sudo apt install apktool apksigner zipalign")
    time.sleep(3)
    print("Now you use android_payload.py")
    time.sleep(3)
    os.system("clear")
else:
    print("ERROR!!!")