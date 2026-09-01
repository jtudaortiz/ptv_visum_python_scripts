#Script 2 
import os
Path = Visum.GetPath(69)
SC_CODIGO = Visum.Procedures.OperationVariables.GetOperationVariable("SC_CODIGO").ValueOfVariable


for M in Visum.Net.Matrices.GetAll:
	if M.AttValue("SAVE")==1:
    		M.Save(Path + "\\" +str(int(M.AttValue("No")))+"-"+M.AttValue("NAME").replace("/","&")+" "+SC_CODIGO,'o')


Path = Visum.GetPath(20)

MatList = Visum.Lists.CreateMatrixList
MatList.OpenLayout("Analisis_Matrices.lla")
MatList.SaveToAttributeFile(Path + "\\Analisis_Matrices_" +SC_CODIGO+".csv",59)

LinkList = Visum.Lists.CreateLinkList
LinkList.OpenLayout("Analisis_Peaje.lla")
LinkList.SaveToAttributeFile(Path + "\\Analisis_Peaje_" +SC_CODIGO+".csv",59)

LineRouteList = Visum.Lists.CreateTimeProfileList
LineRouteList.OpenLayout("Analisis_TPu_Perfil.lla")
LineRouteList.SaveToAttributeFile(Path + "\\Analisis_TPu_Perfil_" +SC_CODIGO+".csv",59)

StopPointsList = Visum.Lists.CreateStopPointBaseList
StopPointsList.OpenLayout("Analisis_TPu_Paradas.lla")
StopPointsList.SaveToAttributeFile(Path + "\\Analisis_TPu_Paradas_" +SC_CODIGO+".csv",59)
