#Script 7
import VisumPy.helpers as VPH
from numpy import *
import pandas as pd

lista_matrices=[1,2,3,4,5]

lista_modos=["C","B","R","A","S"]



origen=repeat(VPH.GetMulti(Visum.Net.Zones,"No",activeOnly=False),381)
destino=VPH.GetMulti(Visum.Net.Zones,"No",activeOnly=False)*381


vector_od=pd.DataFrame({"Origen":origen,"Destino":destino}, columns=["Origen","Destino"])
    
i=0

for modo in lista_modos: 

    matriz= pd.DataFrame(data=VPH.GetODMatrix(Visum,lista_matrices[i]).flatten(),columns=[modo])
    vector_od=pd.concat([vector_od,matriz],axis=1)
       
    i=i+1
    


vector_od.to_csv("Matrices_etapas_modo_O06.csv", index=True)
