#Script 5
import VisumPy.helpers as VPH
from numpy import *
import pandas as pd

lista_matrices=[405,406,407,408,409,410,411,412]

lista_motivos=["E","Hd","O","P","S","W","FOR","EXT"]



origen=repeat(VPH.GetMulti(Visum.Net.Zones,"No",activeOnly=False),381)
destino=VPH.GetMulti(Visum.Net.Zones,"No",activeOnly=False)*381


vector_od=pd.DataFrame({"Origen":origen,"Destino":destino}, columns=["Origen","Destino"])
    
i=0

for motivo in lista_motivos: 

    matriz= pd.DataFrame(data=VPH.GetODMatrix(Visum,lista_matrices[i]).flatten(),columns=[motivo])
    vector_od=pd.concat([vector_od,matriz],axis=1)
       
    i=i+1
    


vector_od.to_csv("Matrices_motivo_O06.csv", index=True)
