razpolozenje = input('Vnesi svoje razpolozenje: ')

if razpolozenje == 'happy':
    print('It is great to see you happy!')
elif razpolozenje == 'nervous':
    print('Take a deep breath 3 times.')
elif razpolozenje == 'sad':
    print('Do not be sad.')
elif razpolozenje == 'excited':
    print('Super.')
elif razpolozenje == 'relaxed':
    print('Great.')
else:
    print('I do not recognize this mood.')



#Domaca naloga st.:2

secret = 25
guess = int(input('Ugani skrito stevilko: '))
if secret == guess:
    print('Sorry you didnt guess the number,more luck nekt time!')
elif 20 == guess:
    print('Almost there!')
elif 2 == guess:
    print('Bad luck,leave game.')
else:
    print('You guessed the number,congratulations!')




#Domaca naloga st.:3


st1 = int(input('vnesiti prvo stevilko : ' ))
st2 = int(input('vnesiti drugo stevilko : ' ))
operacija = input('vnesite racunsko operacijo : ')

if operacija == '+':
    print(st1 + st2)
elif operacija == '-':
    print(st1 - st2)
elif operacija == '/':
    print(st1 / st2)
elif operacija == '*':
    print(st1 * st2)




