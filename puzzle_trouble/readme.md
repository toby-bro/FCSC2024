# Puzzle Trouble

## Easy
For the first program I started by taking the code from someone on internet who solved the 2023 prechall.
https://kleborgn.github.io/posts/fcsc2023/
But I wanted to swap the pieces one by one interactively so i named each piece and solved it with the swap-easy.sh coordinated with the arrange-easy.py and got output-easy.png
To solve it I used `./swap.sh` and swapped manually all the pieces with there names (by following the state of the puzzle)
```bash
watch 'cat arrange.py | sed -n "13,21p"'
```

## Hard
Before starting the second challenge I sorted all the pieces of this second challenge by hues to facilitate the begining of the challenge. I thus used hues.py to sort all the image and start with a somewhat easier puzzle to solve.

For the second challenge it was far too tedious to search what was each piece's coordinates so i decided to do a python program that would get the coordinates of each piece I wanted to swap, so i only needed to click on two pieces to swap them. But as i had already programmed the swap and the arrange I reused them in a most hedious python program that would call a bash program to swap the image and then call a python program to regenerate the image. 

I thus reprogrammed the swap-easy.sh in simple-swap.sh and only needed the python script exchange.py to exchange all the pieces.

To solve the puzzle thus I only needed to run 
```bash
python exchange.py
```

Thus we get the output and the flag.
