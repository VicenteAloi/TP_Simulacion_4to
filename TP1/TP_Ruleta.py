import random
import statistics
import math
import matplotlib.pyplot as plt
import sys

if len(sys.argv) != 7 or sys.argv[1] != "-c" or sys.argv[3] != "-n" or sys.argv[5] != "-e":
  print("Uso correcto: py TP_1.1_simulacion.py -c <cant_tiradas> -n <cant_corridas> -e <num_elegido>")
  sys.exit(1)

cant_tiradas = int(sys.argv[2])
cant_corridas = int(sys.argv[4])
num_elegido = int(sys.argv[6])

rdo_tiradas = []
aux_prom_tiradas = []
prom_tiradas = []
frec_abs_elegido = []
frec_rel_elegido = []
var_elegido = []
desv_elegido = []
#[0,1,2,3,.....]
x = list(range(0,cant_tiradas))

for j in range(0,cant_corridas):
  rdo_tiradas.append([0.0])
  prom_tiradas.append([0.0])
  aux_prom_tiradas.append(0)
  frec_abs_elegido.append(0)
  frec_rel_elegido.append([0.0])
  var_elegido.append([0.0])
  desv_elegido.append([0.0])
  
  for i in x:
    #genera num random y lo guarda en el array
    rdo_tiradas[j].append(random.randint(0,36))
    #suma valores al aux promedio
    aux_prom_tiradas[j] += rdo_tiradas[j][i]
    
    #si el resultado es igual al numero elegido, suma refuencia abs del mismo
    if rdo_tiradas[j][i] == num_elegido: 
      frec_abs_elegido[j] += 1
    
    #agrega los valores al final de los arreglos
    if i != 0:
      frec_rel_elegido[j].append(frec_abs_elegido[j]/i)
      prom_tiradas[j].append(aux_prom_tiradas[j]/i)
        # Calcula la varianza para el número elegido
      var_elegido[j].append(statistics.variance(rdo_tiradas[j]))
        # Calcula la desviación estándar para el número elegido
      desv_elegido[j].append(math.sqrt(var_elegido[j][i]))

  

fig, axs1 = plt.subplots(2,2,figsize=(10,6))

axs1[0,0].bar(x,frec_rel_elegido[0],color='blue')
axs1[0,0].set_title('Gráfico 1: Frecuencia relativa respecto a n')
axs1[0,0].set_xlabel('Num tiradas')
axs1[0,0].set_ylabel('frecuencia relativa')

axs1[0,1].plot(x,prom_tiradas[0], color='red')
axs1[0,1].set_title('Gráfico 2: Promedio de las tiradas')
axs1[0,1].set_xlabel('Num tiradas')
axs1[0,1].set_ylabel('Promedio')

axs1[1,0].plot(x,desv_elegido[0], color='green')
axs1[1,0].set_title('Gráfico 3: Desvio del numero elegido')
axs1[1,0].set_xlabel('Num tiradas')
axs1[1,0].set_ylabel('Desvio')

axs1[1,1].plot(x,var_elegido[0], color='black')
axs1[1,1].set_title('Gráfico 4: Varianza del numero elegido')
axs1[1,1].set_xlabel('Num tiradas')
axs1[1,1].set_ylabel('Varianza')

fig2, axs2 = plt.subplots(2,2, figsize=(10,6))
for i in range(0,cant_corridas):
  axs2[0,0].plot(x,frec_rel_elegido[i], color='blue')
  axs2[0,0].axhline(1/37, color='red', linestyle='--', linewidth=1, label='Valor Teórico Esperado')
  axs2[0,0].set_title('Gráfico 1: Frecuencia relativa respecto a n')
  axs2[0,0].set_xlabel('Num tiradas')
  axs2[0,0].set_ylabel('frecuencia relativa')
  
  axs2[0,1].plot(x,prom_tiradas[i], color='red')
  axs2[0,1].axhline(18, color='blue', linestyle='--', linewidth=1, label='Valor Teórico Esperado')
  axs2[0,1].set_title('Gráfico 2: Promedio de las tiradas')
  axs2[0,1].set_xlabel('Num tiradas')
  axs2[0,1].set_ylabel('Promedio')

  axs2[1,0].plot(x,desv_elegido[i], color='green')
  axs2[1,0].axhline(math.sqrt(114), color='red', linestyle='--', linewidth=1, label='Valor Teórico Esperado')
  axs2[1,0].set_title('Gráfico 3: Desvio del numero elegido')
  axs2[1,0].set_xlabel('Num tiradas')
  axs2[1,0].set_ylabel('Desvio')

  axs2[1,1].plot(x,var_elegido[i], color='black')
  axs2[1,1].axhline(114, color='red', linestyle='--', linewidth=1, label='Valor Teórico Esperado')
  axs2[1,1].set_title('Gráfico 4: Varianza del numero elegido')
  axs2[1,1].set_xlabel('Num tiradas')
  axs2[1,1].set_ylabel('Varianza')

plt.tight_layout()

plt.show()

