#Script 6
import VisumPy.helpers as VPH
from numpy import *
import pandas as pd

lista_matrices=[300,301,302,303,304,305,306,307,308,309,310,13,14,15,16,17,18,19,20,21,22,23,24]

lista_modos=["C","B","R","A","S","C/A","B/A","R/A","C/S","B/R","C/R","FOR_C","FOR_B","FOR_R","FOR_A","FOR_S","EXT_C","EXT_B","EXT_R","EXT_A","EXT_S","TRA_C_MOR","TRA_C_POR"]



origen=repeat(VPH.GetMulti(Visum.Net.Zones,"No",activeOnly=False),381)
destino=VPH.GetMulti(Visum.Net.Zones,"No",activeOnly=False)*381


vector_od=pd.DataFrame({"Origen":origen,"Destino":destino}, columns=["Origen","Destino"])
    
i=0

for modo in lista_modos: 

    matriz= pd.DataFrame(data=VPH.GetODMatrix(Visum,lista_matrices[i]).flatten(),columns=[modo])
    vector_od=pd.concat([vector_od,matriz],axis=1)
       
    i=i+1
