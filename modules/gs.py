import numpy as np
import pdb

def gaussSeidel(tolerance, max_iter,y_bus,z_line,trx,z_sht,bus_gs):
#VALORES NECESARIOS DEL CALCULO ITERATIVO
    v_i = np.zeros((len(y_bus)),dtype=object)
    error = 0                                           
    p_i = np.squeeze(np.asarray(bus_gs[:,6]))
    q_i = np.squeeze(np.asarray(bus_gs[:,7]))
    v_bar = np.squeeze(np.asarray(bus_gs[:,2]))
    term2 = 0

#METODO DE GAUSS-SEIDEL
    #pdb.set_trace()
    for _ in range(max_iter):
        for i in range(len(y_bus)):
            for j in range(len(y_bus)):
                if i != j:
                    term2 += y_bus[i,j]*v_bar[j]
                else:
                    term2 += 0
            term1 = np.conj((p_i[i] + 1j*q_i[i])/v_bar[i])
            v_i[i] = 1/y_bus[i,i]*(term1 - term2)
        
        error = max(abs(v_i)-abs(v_bar))
        print(error)
        print(tolerance)
        if error < tolerance:
            break
        v_bar = v_i
    print(v_i)
    return v_i
