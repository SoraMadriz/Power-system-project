import pandas as pd #Dependencia de lectura y escritura
import numpy as np  #Dependencia de la estructura del programa

document = "data_io" #Hoja de entrada de datos
path = '/home/leonardomadriz/Universidad/Apuntes/TercerAño/CT3233-PotenciaI/proyectoA'

#LECTURA DE LA HOJA DE CONFIGURACION
df_config = np.matrix(pd.read_excel(f'{path}/files/{document}.xlsx', sheet_name="CONFIG"))

#LECTURA DE LA HOJA BUS
df_bus = np.matrix(pd.read_excel(f'{path}/files/{document}.xlsx', sheet_name='BUS'))

#LECTURA DE LA HOJA LINES
df_lines = np.matrix(pd.read_excel(f'{path}/files/{document}.xlsx', sheet_name='LINES'))

#LECTURA DE LA HOJA TRX
df_trx = np.matrix(pd.read_excel(f'{path}/files/{document}.xlsx', sheet_name='TRX'))

#LECTURA DE LA HOJA SHUNT_ELEMENTS
df_sht = np.matrix(pd.read_excel(f'{path}/files/{document}.xlsx', sheet_name='SHUNT_ELEMENTS'))
