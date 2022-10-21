#Importando a biblioteca "math" para usar funções de matemática
from math import *


#Função para coletar o tempo no ar!
def tempoAr(g,vy0,h0,hf):
    #0 = (eixo_y_inicial - eixo_y_final) + vy0*t + (g*(t**2))/2
    a = g/2
    b = vy0
    c = (h0 - hf)
    delta = (b**2) - (4 * a *c)
    t1 = (sqrt(delta) - b) / (2*a)
    t2 = (-b - sqrt(delta)) / (2*a)

    if (t1 > t2):
        tempo_ar = t1
    else:
        tempo_ar = t2

    return tempo_ar

#Função para coletar todos os dados no xmax
def dados_xmax(g,h0,hf,vx0,vy0):
    #Equações base:
    # x = x0 + vx0*t e V = vx0 -> constante

    #tempo no ar: usamos a função tempoAr
    tempo_ar = tempoAr(g,vy0,h0,hf)

    #Distância máxima:
    #xmax = vx0 * tempo_ar
    xmax = vx0 * tempo_ar

    # Velocidades
    # vy_xmax = vy0 + g*tempo_ar = 0
    # vx_xmax = vx0
    # |v|_xmax = sqrt((vy_xmax**2) + (vx_xmax**2))
    vx_xmax = vx0
    vy_xmax = vy0 + g*tempo_ar
    v_modulo_xmax = sqrt( (vx_xmax**2) + (vy_xmax**2))

    #Altura no xmax:
    #h_xmax = eixo_y_inicial + vy0*tempo_ar + (g*(tempo_ar**2))/2
    h_xmax = h0 + vy0*tempo_ar + (g*(tempo_ar**2))/2

    print("Xmax = %f m" % xmax)
    print("Vx_Xmax = %f m/s" %vx_xmax)
    print("Vy_xmax = %f m/s" % vy_xmax)
    print("Modulo da velocidade no Xmax = %f m/s \n" % v_modulo_xmax)
    return tempo_ar, xmax,h_xmax, vx_xmax, vy_xmax, v_modulo_xmax

#Função para coletar todos os dados no hmax
def dados_hmax(g, h0, hf, vx0, vy0):
    #Equações base:
    #posição -> y = eixo_y_inicial + vy0*t + (g * (t**2))/2
    #velocidade -> v = v0y + g*t

    #Tempo que chega no Hmax:
    #0 = vy0 + g*t - > t = -v0y/g
    tempo_hmax = (-vy0)/g

    #Altura maxima -> Usa o tempo_hmax na equação da posição
    #hmax = y = eixo_y_inicial + vy0*tempo_hmax + (g*(tempo_hmax**2))/2
    hmax = h0 + vy0*tempo_hmax + (g*(tempo_hmax**2))/2

    #Velocidades
    #vy_hmax = vy0 + g*tempo_hmax = 0
    #vx_hmax = vx0
    #|v|_hmax = sqrt((vy_hmax**2) + (vx_hmax**2))
    vy_hmax = 0
    vx_hmax = vx0
    modulo_v_hmax = sqrt((vy_hmax**2) + (vx_hmax**2))

    #Posicção x_hmax:
    #x_hmax = vx0*tempo_hmax
    x_hmax = vx0*tempo_hmax

    return tempo_hmax, hmax, x_hmax, vx_hmax, vy_hmax, modulo_v_hmax

#Função para coletar todos os dados no tempo escolhido
def dados_tempoEscolhido(tempo, g, h0, hf, vx0, vy0):

    #Eixo x:

    #S = s0 + vx0*t
    #xt = vx0*tempo
    xt = vx0*tempo

    #Vx->vx = vx0
    vxt = vx0

    #Eixo y:
    #h = h0 + vy0*t + (g*(tempo**2))/2
    ht = h0 + vy0*tempo + (g*(tempo**2))/2

    #vy = vy0 + g*tempo
    vyt = vy0 + g*tempo

    #Modulo velocidade:
    # |v|_tempo = sqrt((vyt**2) + (vxt**2))
    modulo_v_tempo = sqrt((vyt**2) + (vxt**2))

    return xt,ht,vxt,vyt,modulo_v_tempo

#############################################
#############################################
############################################

#Dados de entrada!
g = -9.8
v0 = float(input("Velocidade inicial: "))
angulo = radians(float(input("Angulo inicial: ")))
tempo = float(input("Tempo inicial: "))
h0 = float(input("Altura inicial: "))
hf = float(input("Altura final: "))
vx0 = v0 * cos(angulo)
vy0 = v0 * sin(angulo)

#Chamando as funções
tempo_ar, xmax, y_xmax, vx_xmax, vy_xmax, modulo_v_xmax = dados_xmax(g,h0,hf,vx0,vy0)
tempo_hmax, hmax, x_hmax, vx_hmax, vy_hmax, modulo_v_hmax = dados_hmax(g, h0, hf, vx0, vy0)
xt,yt,vxt,vyt,modulo_v_tempo = dados_tempoEscolhido(tempo, g, h0, hf, vx0, vy0)

print("#######################################")
print("\nDados Iniciais: \n")
print("V0 = %f" %v0)
print("Vx0 = %f" %vx0)
print("Vy0 = %f" %vy0)
print("Gravidade = %f" %g)
print("Angulo = %f" %angulo)
print("Tempo = %f" %tempo)
print("Eixo y Inicial = %f" %h0)
print("Eixo y Final = %f" %hf)
print("#######################################")

print("\n#######################################")
print("Dados no tempo escolhido: %.2lf" %tempo)
print("Posição x(%.2lf): %.2lf m" %(tempo, xt))
print("Posição y(%.2lf): %.2lf m" %(tempo, yt))
print("Velocidade vx(%.2lf): %.2lf m/s" %(tempo, vxt))
print("Velocidade vy(%.2lf): %.2lf m/s" %(tempo, vyt))
print("Módulo da velocidade V(%.2lf): %.2lf m/s" %(tempo, modulo_v_tempo))
print("#######################################")

print("\n#######################################")
print("Dados na Altura máxima")
print("Tempo hmax: %.2f" %(tempo_hmax))
print("Altura máxima: %.2f m" %hmax)
print("Posição x_hmax: %.2lf m" %(x_hmax))
print("Velocidade vx_hmax: %.2lf m/s" %(vx_hmax))
print("Velocidade vy_hmax: %.2lf m/s" %(vy_hmax))
print("Módulo da velocidade na altura máxima: %.2lf m/s" %(modulo_v_hmax))
print("#######################################")

print("\n#######################################")
print("Dados na Distância máxima")
print("Tempo xmax: %.2f" %(tempo_ar))
print("Distância xmax: %.2f m" %xmax)
print("Posição y_xmax: %.2lf m" %(y_xmax))
print("Velocidade vx_xmax: %.2lf m/s" %(vx_xmax))
print("Velocidade vy_xmax: %.2lf m/s" %(vy_xmax))
print("Módulo da velocidade na distância máxima: %.2lf m/s" %(modulo_v_xmax))
print("#######################################")
