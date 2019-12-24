from PIL import Image

words = []
white = (255,255,255)
black = (0,0,0)

with open("lyrics.txt") as ly:
    content = ly.readlines()
    content = [x.strip() for x in content]
    for line in content:
        lwords = line.split(" ")
        for word in lwords:
            words.append(word)

size = len(words)
pixels = [[black for x in range(size)] for y in range(size)]
for r in range(size):
    for c in range(size):
        if words[r]==words[c]:
            print(words[r] + "\t" + words[c])
            pixels[r][c] = white

im = Image.new('RGB', (size, size))

pixelStream = []
for row in pixels:
    pixelStream.extend(row)

im.putdata(pixelStream)
im.save('output.png')
