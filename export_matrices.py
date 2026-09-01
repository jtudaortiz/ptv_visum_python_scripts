
# Salvar matrices de utilidad y exportar a .csv


#Script 1 
import os
Path = Visum.GetPath(69)
SC_CODIGO = Visum.Procedures.OperationVariables.GetOperationVariable("SC_CODIGO").ValueOfVariable


for i in range(58,282):
    M = Visum.Net.Matrices.ItemByKey(i)
    M.Save(Path + "\\" +str(int(M.AttValue("No")))+"-"+M.AttValue("NAME").replace("/","&")+" "+SC_CODIGO,'b')

for i in range(3000,3224):
    M = Visum.Net.Matrices.ItemByKey(i)
    M.Save(Path + "\\" +str(int(M.AttValue("No")))+"-"+M.AttValue("CODE").replace("/","&")+" "+SC_CODIGO,'b')
