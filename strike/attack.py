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
