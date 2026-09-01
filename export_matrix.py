#Script 9
import os
Path = Visum.GetPath(69)
SC_CODIGO = Visum.Procedures.OperationVariables.GetOperationVariable("SC_CODIGO").ValueOfVariable


for i in range(1,12):
    M = Visum.Net.Matrices.ItemByKey(i)
    M.Save(Path + "\\" +str(int(M.AttValue("No")))+"-"+M.AttValue("NAME").replace("/","&")+" "+SC_CODIGO,'b')
