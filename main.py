from modules.impedances import *
from modules.ybus import functionYbus as fbus
from modules.gs import gaussSeidel as gs

def main():
#VARIABLES OBTENIDAS DE READDDATA.PY
    #Configuraciones
    converge_radius = df_config[5,1]
    iterations_max = df_config[6,1]
    #Bus
    bus_gs = df_bus[:,2:]
    bus_gs[:,3] = (bus_gs[:,3]*np.pi)/180
    #Trx
    print(df_trx)
    trx_gs = df_trx[:,2:]
    

#METODOS DE ESTUDIO
    y_bus = fbus(z_lines,z_sht)
    flow_gs = gaussSeidel(
            converge_radius,
            iterations_max,
            y_bus,
            z_lines,
            trx_gs,
            z_sht
            )


if __name__ == "__main__":
    main()
