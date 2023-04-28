try:
    import sim
except:
    print("Não foi possível importar a biblioteca sim!")

import time
import math

print ('Programa iniciado')
sim.simxFinish(-1) 
clientID=sim.simxStart('127.0.0.1',19999,True,True,5000,5) 

if clientID!=-1:
    print ('Conectado ao servidor API remoto')
    sim.simxAddStatusbarMessage(clientID, "Conectado com sucesso!!", sim.simx_opmode_oneshot_wait)
    pi = math.pi
    angulo= float(input("angulo da junta 1"))   
    "juntaperna"
    [er,j] = sim.simxGetObjectHandle(clientID, 'j', sim.simx_opmode_oneshot_wait)
    sim.simxSetJointTargetPosition(clientID, j,angulo*pi/180, sim.simx_opmode_oneshot_wait)
    sim.simxSetJointTargetVelocity(clientID, j,3, sim.simx_opmode_oneshot_wait)
    time.sleep(2)
    
    sim.simxAddStatusbarMessage(clientID, "feito!", sim.simx_opmode_oneshot_wait)
else:
    print ('Conexão com o servidor API remoto falhou')
print ('Programa finalizado')






