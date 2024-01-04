#Primeira parte- teste após cálculo das frequências
#No enunciado é dado com x, nomeamos x1 para não haver conflito
x1 = seqsin(440, 0.3, 0, 0.5, 466.164, 0.15)

#Segundo exercício

#Notas musicais
meio_tom = 2**(1/12)
la4 = 440.00
la4_s = la4 * meio_tom
si4 = la4_s* meio_tom
do5 = si4* meio_tom
do4 = do5 / 2
do4_s = do4 * meio_tom
re4 = do4_s * meio_tom
re4_s = re4* meio_tom
mi4 = re4_s * meio_tom
fa4 = mi4 * meio_tom
fa4_s = fa4 * meio_tom
sol4 = fa4_s * meio_tom
sol4_s = sol4 * meio_tom
si3 = si4 / 2
la3 = la4 / 2
mi3 = mi4 / 2
sol3 = sol4 / 2
re3 = re4 /2
fa3_s = fa4_s / 2
samplingrate = 16000
t=timevar(1)
x = seqsin(0, 0.7, sol4, 0.1, fa4_s, 0.1, sol4, 0.2, si4, 0.1, do5, 0.1, si4, 0.8, 0, 0.2, fa4_s, 0.1, sol4, 0.1, fa4_s, 0.2, sol4, 0.1, la4, 0.1, sol4, 0.8, 0, 0.2, fa4_s, 0.1, mi4, 0.1, fa4_s, 0.2, si4, 0.1, do5, 0.1, si4, 0.8, 0, 0.2, fa4_s, 0.1, mi4, 0.1, fa4_s, 1.0, 0, 0.7)

#Extra
y = seqsin(0, 0.5, mi4, 0.2, si3, 0.2, mi4, 0.2, si3, 0.2, mi4, 0.2, si3, 0.2, mi4, 0.2, si3, 0.2, re4, 0.2, si3, 0.2, re4, 0.2, si3, 0.2, re4, 0.2, si3, 0.2, re4, 0.2, si3, 0.2, re4, 0.2, si3, 0.2, re4, 0.2, si3, 0.2, re4, 0.2, si3, 0.2, re4, 0.2, si3, 0.2, re4, 0.2, la3, 0.2, re4, 0.2, la3, 0.2, re4, 0.2, la3, 0.2, re4, 0.2, la3, 0.2, 0, 0.5)   

z = seqsin(0, 0.5, mi3, 0.4, sol3, 0.4, mi3, 0.4, sol3, 0.4, re3, 0.4, sol3, 0.4, re3, 0.4, sol3, 0.4, re3, 0.4, fa3_s , 0.4, re3, 0.4, fa3_s, 0.4, re3, 0.4, fa3_s, 0.4, re3, 0.4, fa3_s, 0.4, 0, 0.5)

play(x)
play(y)
play(z)
play(0.5*x + 0.25*y + 0.25*z)



