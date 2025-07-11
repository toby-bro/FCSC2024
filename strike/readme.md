# Strike

To reverse engineer this program I used IDA on one side and gdb on the other side (with pwndbg) so i could see what each input would do.

First of all we see that the program expects one argument
Then we realise that the length of the string we pass as argument must be a dividable by two.

From now on we will consider that I am using the program ./strike aabbccddee with aabbccddee a string passed as argument to the program (in gdb)
```gdb
(gdb) set args aabbccddee
(gdb) run
```
Then there is a 'a' function (or so it is named by IDA) that will be called for each of the characters of the input string (here 'aa' then 'bb' then 'cc'...). It checks if each character of this string is in 0-9, or A-Z or a-f.

Just after this function there is a cmp al,23h that will finally check if each input is under 23 in hexadecimal so 00-0f 10-1f 20-23

We furthermore learn that the flag is composed of these characters : abcdefghijklmnopqrstuvwxyz!# $:-(). 

Then we learn that the length of the input must be 0xa2 so the total length of the input must be 81x2 characters long.

Once we got all this we realize that the a function sends back a character for each character of our input. And that once we passed the transformation, our string must have been transformed into '# congratulations! this is a strike :-) you should now see the flag printed ... #'. I did not have the courage of reversing all the maths that transformed our input so I inputed 81x'00' and 81 x '01'. And looked at what was this string transformed into. For the 81 '00' the output was "acegikmoqsuwy! :(.bdfhjlnprtvxz#$-)acegikmoqsuwy! :(.bdfhjlnprtvxz#$-)acegikmoqsu". 

So I wrote a python program that did the opposite of this `attack.py` : 
```python
cible = '# congratulations! this is a strike :-) you should now see the flag printed ... #'

chars = 'abcdefghijklmnopqrstuvwxyz!# $:-().'

num = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '0a', '0b', '0c', '0d', '0e', '0f', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '1a', '1b', '1c', '1d', '1e', '1f', '20', '21', '22', '23']
n = len(chars)
result = ''

def modulo(i):
    while i<0:
        i+=n
    while i>=n:
        i-=n
    return i

def coord(i):
    m = chars.index(cible[i])-2*i%n
    
    return num[modulo(m)]



for i in range(81):
    result += coord(i) 

print(result)
```
And thus I got the flag with ; `./strike $(python attack.py)`
