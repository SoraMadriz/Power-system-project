from modules.readdata import *

#MODELADO DE LÍNEAS
z_lines = df_lines[::,2::]
for i in range(np.shape(df_lines)[0]):
    if df_lines[i,0] == 'OFF':
        z_lines = np.delete(z_lines, i, axis=0)
    else:
        z_lines[i,2] = z_lines[i,2] + z_lines[i,3]*1j
z_lines = np.delete(z_lines,3,axis=1)

#MODELADO DE ELEMENTOS SHUNT
z_sht = df_sht[::,2::]
for i in range(np.shape(df_sht)[0]):
    if df_sht[i,0] == 'OFF':
        z_sht = np.delete(z_sht, i, axis=0)
    else:
        z_sht[i,1] = z_sht[i,1] + z_sht[i,2]*1j
z_sht = z_sht[::,:-1:]
z_sht = np.insert(z_sht,1,0,axis=1)
