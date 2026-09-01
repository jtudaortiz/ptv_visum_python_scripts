#Script 4

import VisumPy.helpers as VPH
from numpy import *
import pandas as pd

lista_matrices=[401,402,403,404,411,412]

lista_usuarios=["W","S","R","O","FOR","EXT"]



origen=repeat(VPH.GetMulti(Visum.Net.Zones,"No",activeOnly=False),381)
destino=VPH.GetMulti(Visum.Net.Zones,"No",activeOnly=False)*381


vector_od=pd.DataFrame({"Origen":origen,"Destino":destino}, columns=["Origen","Destino"])
    
i=0

for usuario in lista_usuarios: 

    matriz= pd.DataFrame(data=VPH.GetODMatrix(Visum,lista_matrices[i]).flatten(),columns=[usuario])
    vector_od=pd.concat([vector_od,matriz],axis=1)
       
    i=i+1
    


vector_od.to_csv("Matrices_tipo_usuario_O06.csv", index=True)
