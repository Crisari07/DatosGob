import pandas as pd
path=input('¿Qué año desea consultar de 1985 a 2018: ');
datos= pd.read_csv( path + 'Precipo.csv',header=1)
#print(datos)
#[renglones:columnas]
Entidades=datos.iloc[0:32,0:13]
print(Entidades)
print(Entidades['ENTIDAD'])
print('----------------------')
Entidad=int(input('Digite el número del mes que desea consultar: '));
Mes=int(input('Digite el número de la entidad que desea consultar: '));
if Mes==1:
    print("Precipitacion de Enero: "+str(Entidades.iloc[Entidad][Mes]))
elif Mes==2:
    print("Precipitacion de Febrero: "+str(Entidades.iloc[Entidad][Mes]))
elif Mes==3:
    print("Precipitacion de Marzo: "+str(Entidades.iloc[Entidad][Mes]))
elif Mes==4:
    print("Precipitacion de Abril: "+str(Entidades.iloc[Entidad][Mes]))
elif Mes==5:
    print("Precipitacion de Mayo: "+str(Entidades.iloc[Entidad][Mes]))
elif Mes==6:
    print("Precipitacion de Junio: "+str(Entidades.iloc[Entidad][Mes]))
elif Mes==7:
    print("Precipitacion de Julio: "+str(Entidades.iloc[Entidad][Mes]))
elif Mes==8:
    print("Precipitacion de Agosto: "+str(Entidades.iloc[Entidad][Mes]))
elif Mes==9:
    print("Precipitacion de Septiembre: "+str(Entidades.iloc[Entidad][Mes]))
elif Mes==10:
    print("Precipitacion de Octubre: "+str(Entidades.iloc[Entidad][Mes]))
elif Mes==11:
    print("Precipitacion de Noviembre: "+str(Entidades.iloc[Entidad][Mes]))
elif Mes==12:
    print("Precipitacion de Diciembre: "+str(Entidades.iloc[Entidad][Mes]))    

