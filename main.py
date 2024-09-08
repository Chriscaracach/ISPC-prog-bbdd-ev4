from maquina_cremallera import MaquinaCremallera
import time

maq1 = MaquinaCremallera("Máquina 1")
time.sleep(1)
maq1.tejerCinta(50)
time.sleep(1)
maq1.fabricarCremallera()
time.sleep(1)
maq1.teñir("rojo")
time.sleep(1)
maq1.empaquetar()
time.sleep(1)
maq1.fabricarCremalleraCompleta(20, "azul")
time.sleep(1)
maq1.visualizarDatos()
time.sleep(1)
print(len(maq1))
time.sleep(1)
