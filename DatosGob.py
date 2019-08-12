import pandas as pd
import tkinter as tk
global Entidad
global Mes


path=input('¿Qué año desea consultar de 1985 a 2018: ');
datos= pd.read_csv( path + 'Precip.csv',header=1, encoding="latin-1")
Entidades=datos.iloc[0:32,0:13]
print(Entidades)

def precip():
   
    if Entidad2.get() == 'AGUASCALIENTES':
        Entidad=0
    elif Entidad2.get() == 'BAJA CALIFORNIA':
        Entidad=1
    elif Entidad2.get() == 'BAJA CALIFORNIA SUR':
        Entidad=2
    elif Entidad2.get() == 'CAMPECHE':
        Entidad=3
    elif Entidad2.get() == 'COAHUILA':
        Entidad=4
    elif Entidad2.get() == 'COLIMA':
        Entidad=5
    elif Entidad2.get() == 'CHIAPAS':
        Entidad=6
    elif Entidad2.get() == 'CHIHUAHUA':
        Entidad=7
    elif Entidad2.get() == 'DISTRITO FEDERAL':
        Entidad=8
    elif Entidad2.get() == 'DURANGO':
        Entidad=9
    elif Entidad2.get() == 'GUANAJUATO':
        Entidad=10
    elif Entidad2.get() == 'GUERRERO':
        Entidad=11
    elif Entidad2.get() == 'HIDALGO':
        Entidad=12
    elif Entidad2.get() == 'JALISCO':
        Entidad=13
    elif Entidad2.get() == 'ESTADO DE MÉXICO':
        Entidad=14
    elif Entidad2.get() == 'MICHOACÁN':
        Entidad=15
    elif Entidad2.get() == 'MORELOS':
        Entidad=16
    elif Entidad2.get() == 'NAYARIT':
        Entidad=17
    elif Entidad2.get() == 'NUEVO LEÓN':
        Entidad=18
    elif Entidad2.get() == 'OAXACA':
        Entidad=19
    elif Entidad2.get() == 'PUEBLA':
        Entidad=20
    elif Entidad2.get() == 'QUERÉTARO':
        Entidad=21
    elif Entidad2.get() == 'QUINTANA ROO':
        Entidad=22
    elif Entidad2.get() == 'SAN LUIS POTOSÍ':
        Entidad=23
    elif Entidad2.get() == 'SINALOA':
        Entidad=24
    elif Entidad2.get() == 'SONORA':
        Entidad=25
    elif Entidad2.get() == 'TABASCO':
        Entidad=26
    elif Entidad2.get() == 'TAMAULIPAS':
        Entidad=27
    elif Entidad2.get() == 'TLAXCALA':
        Entidad=28
    elif Entidad2.get() == 'VERACRUZ':
        Entidad=29
    elif Entidad2.get() == 'YUCATÁN':
        Entidad=30        
    elif Entidad2.get() == 'ZACATECAS':
        Entidad=31
    print(Entidad)

    if Mes2.get() == 'Enero':
        Mes=1
    elif Mes2.get() == 'Febrero':
        Mes=2
    elif Mes2.get() == 'Marzo':
        Mes=3
    elif Mes2.get() == 'Abril':
        Mes=4
    elif Mes2.get() == 'Mayo':
        Mes=5
    elif Mes2.get() == 'Junio':
        Mes=6
    elif Mes2.get() == 'Julio':
        Mes=7
    elif Mes2.get() == 'Agosto':
        Mes=8
    elif Mes2.get() == 'Septiembre':
        Mes=9
    elif Mes2.get() == 'Octubre':
        Mes=10
    elif Mes2.get() == 'Noviembre':
        Mes=11
    elif Mes2.get() == 'Diciembre':
        Mes=12

        

    PrecipMes.set(str(Entidades.iloc[Entidad][Mes]))

        
    
    

    if Mes==1:
        print("Precipitacion de Enero: "+(PrecipMes.get()))
    elif Mes==2:
        print("Precipitacion de Febrero: "+(PrecipMes.get()))
    elif Mes==3:
        print("Precipitacion de Marzo: "+(PrecipMes.get()))
    elif Mes==4:
        print("Precipitacion de Abril: "+(PrecipMes.get()))
    elif Mes==5:
        print("Precipitacion de Mayo: "+(PrecipMes.get()))
    elif Mes==6:
        print("Precipitacion de Junio: "+(PrecipMes.get()))
    elif Mes==7:
        print("Precipitacion de Julio: "+(PrecipMes.get()))
    elif Mes==8:
        print("Precipitacion de Agosto: "+(PrecipMes.get()))
    elif Mes==9:
        print("Precipitacion de Septiembre: "+(PrecipMes.get()))
    elif Mes==10:
        print("Precipitacion de Octubre: "+(PrecipMes.get()))
    elif Mes==11:
        print("Precipitacion de Noviembre: "+(PrecipMes.get()))
    elif Mes==12:
        print("Precipitacion de Diciembre: "+(PrecipMes.get()))

    return PrecipMes.get()
    

def cerrar():

    ventana.destroy()
ventana=tk.Tk()
ventana.title("Precipitaciones en las entidades")
ventana.geometry('500x500+600+100')
ventana.configure(background='white')



PrecipMes=tk.StringVar()
print(PrecipMes.get())
#[renglones:columnas]



e1=tk.Label(ventana,text="Seleccione una entidad: ",bg="gray1",fg="white")
e1.pack(padx=5,pady=5,ipadx=5,ipady=5,fill=tk.X)

Entidad2=tk.StringVar(ventana)
Entidad2.set('AGUASCALIENTES')
opciones=['AGUASCALIENTES','BAJA CALIFORNIA','BAJA CALIFORNIA SUR','CAMPECHE','COAHUILA','COLIMA','CHIAPAS','CHIHUAHUA','DISTRITO FEDERAL','DURANGO','GUANAJUATO','GUERRERO','HIDALGO','JALISCO','ESTADO DE MÉXICO','MICHOACÁN','MORELOS','NAYARIT','NUEVO LEÓN','OAXACA,PUEBLA','QUERÉTARO','QUINTANA ROO','SAN LUIS POTOSÍ','SINALOA','SONORA','TABASCO','TAMAULIPAS','TLAXCALA','VERACRUZ','YUCATÁN','ZACATECAS']
opcion=tk.OptionMenu(ventana,Entidad2,*opciones)
opcion.pack(padx=5,pady=5,fill=tk.X)



e2=tk.Label(ventana,text="Seleccione el mes: ",bg="gray1",fg="white")
e2.pack(padx=5,pady=5,ipadx=5,ipady=5,fill=tk.X)

Mes2=tk.StringVar(ventana)
Mes2.set('Enero')
opciones2=['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']
opcion2=tk.OptionMenu(ventana,Mes2,*opciones2)
opcion2.pack(padx=5,pady=5,fill=tk.X)


#color=tk.Label(ventana,bg='green2',textvariable=Entidad, padx=5,pady=5,width=120)
#color.pack()
botonDatos=tk.Button(ventana,text="Dar Datos",fg='blue',command=precip)
botonDatos.pack(side=tk.TOP)

e3=tk.Label(ventana,text="Precitacion: ",bg="gray1",fg="white")
e3.pack(padx=5,pady=5,ipadx=5,ipady=5,fill=tk.X)

precip=tk.Label(ventana,bg='green2',textvariable=PrecipMes, padx=5,pady=5,width=120)
precip.pack()


botonCerrar=tk.Button(ventana,text="Cerrar",fg='blue',command=cerrar)
botonCerrar.pack(side=tk.TOP)

ventana.mainloop()

