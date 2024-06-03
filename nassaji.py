T = "tedad taar"
t1 = "toole parche/metr"
t1 = 1
tp = "tarakom pood"
tp = 25.4
T = ((t1)* 100) * tp
print("tedad taar=", T)

P = "tedad pood"
p1 = "arze parche/metr"
p1 = 1.6
tt = "tarakom taar"
tt = 28.2
P = ((p1)*100) * tt
print("tedad pood",P)
tt = "tarakom taar"
tt = 28.2
t1 = "toole parche/metr"
t1=1
x = "darsad jam shodegi nakh taar"
x= 0.07
t2 = "tool asli nakh taar/metr"
t2 = t1 + x*(t1)
print("tool asli nakh taar/metr=", t2)

p1 = "arze parche/metr"
p1 = 1.6
y ="darsad jam shodegi nakh pood"
y = 0.14
p2 = "tool asli nakh pood/metr"
p2 = p1 + y*(p1)
print("tool asli nakh pood/metr",p2)

tex1="nomre nakh taar"
tex1=35
tex2="nomre nakh pood"
tex2=35

A = "vazne kol nakh pood"
B = "vazne kol nakh taar"
A=((p2*tex1)/1000)*T
print("vazne kol nakh pood",A)
B=(t2*tex2)/1000*P
print("vazne kol nakh taar",B)
z = "vazne kol parche"
z = A+B
print("vazne kol parche=====",z)