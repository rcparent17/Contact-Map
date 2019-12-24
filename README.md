# Contact Map

This is a simple script that maps song lyrics in the form of a contact map (often used in biology to map genomes). This script enables us to see how repetitive different songs are.

## How It Works

Say we have an input string: `"the cat and the dog"`. This script will make a 2D array of pixel data, with both axes being the different words in the string. When both axes match, that pixel in the array will be white. If they don't match, the pixel will be 
black. An example array is below.

```
x=white

       the   cat   and   the   dog


the     x                 x


cat           x


and                 x


the     x                 x


dog                             x

```

At the end, this pixel array is saved in a .png file.

## How to Run The Script
1. Paste song lyrics into `lyrics.txt`
2. Run the script with python 2.7.x

Enjoy!
