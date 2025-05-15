from PIL import Image
filename = "D:/1KKRX17/UserData/chara/female/1dump/Altvir.png"
im = Image.open(filename)
im.load()
print(im.info)
