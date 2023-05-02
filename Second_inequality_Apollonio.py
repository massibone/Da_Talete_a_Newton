'''
La seconda disuguaglianza di Apollonio afferma che, 
dati quattro numeri reali positivi $a$, $b$, $c$ e $d$, 
la seguente disuguaglianza vale:


(a+b+c+d)**2  <= 4(a^2+b^2+c^2+d^2)
'''
a = 2.5
b = 3.8
c = 1.2

left_side = (a + b + c)**2
right_side = 3*(a*b + b*c + c*a)

if left_side >= right_side:
    print("La seconda disuguaglianza di Apollonio è verificata per a = {}, b = {}, c = {}.".format(a, b, c))
else:
    print("La seconda disuguaglianza di Apollonio non è verificata per a = {}, b = {}, c = {}.".format(a, b, c))
