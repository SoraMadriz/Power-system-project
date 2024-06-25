import numpy as np
import pdb
def functionYbus(z_lines,z_sht):

#DIMENSIONAMIENTO DE LA MATRIX DE INCIDENCIA
    num_bar = int(max(np.max(z_lines[:,0]),np.max(z_lines[:,1]))) #Num. barras
    num_nexos = int(np.shape(z_lines)[0] + np.shape(z_sht)[0])    #Num. nexos
    a_pr = np.zeros((num_nexos,num_bar))                          #Mat. incidencia

#CONSTRUCCION DE LA MATRIZ DE ADMITANCIA
    super_matrix=np.concatenate((z_lines[:,:-1],z_sht),0)
    for nexus,arista in enumerate(super_matrix[:,:-1].tolist()):
        #vertices de entrada y salida
        vertex_out = int(arista[0] -1)
        vertex_in = int((arista[1]-1) if arista[1]!=0 else arista[1])
        #actualización de la matriz de incidencia
        a_pr[nexus,vertex_in] = ((-1) if vertex_in!=0 else 0)
        a_pr[nexus,vertex_out] = 1

#CONSTRUCCION DE LA MATRIZ IMPEDANCIA DE RAMA --> ADMITANCIA DE RAMA
    z_rama = np.diagflat(super_matrix[:,-1]).astype(complex)
    y_rama = np.linalg.inv(z_rama)

#CALCULO DE YBUS
    a_pr_trans = np.transpose(a_pr)
    y_bus = (a_pr_trans)@(y_rama)@(a_pr)
    print(y_bus)

    

    return 0
