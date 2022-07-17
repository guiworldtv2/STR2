import glob
import os

path = os.path.dirname(os.path.realpath(__file__))
os.chdir(path)

if os.path.exists("lista2.m3u"):
    os.remove("lista2.m3u")
else:
    print("O ARQUIVO SUMIU")

read_files = glob.glob("*.m3u")

print(read_files)

with open("lista2.m3u", "wb") as outfile:
    for f in read_files:
        i = 0
        line = "\n"
        i += 1
        outfile.write(line.encode('utf-8'))
        
        with open(f, "rb") as infile:
            outfile.write(infile.read())
