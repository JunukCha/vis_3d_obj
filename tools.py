import os
import glob

for ply in glob.glob("data/*/*.ply"):
    os.remove(ply)

for obj in glob.glob("data/*/*.obj"):
    os.remove(obj)