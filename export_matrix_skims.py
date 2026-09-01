#Script 8
import VisumPy.helpers as VPH
from numpy import *
import pandas as pd

lista_matrices=[1000,1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,1015,1016,1017,1018,1019,1020,1021,1022,1023,1024,1025,1026,1027,1028,1029,1030,1031,1032,1033,1034,1035,1036,1037,1038,1039,1040,1041,1042,1043,1044,1045,1046,1047,1048,1049,1050,1051,1052,1053,1054,1055,1056,1057,1058,1059,1060,1061,1062,1063,1064,1065,1066,1067,1068,1069,1070,1071,1072,1073,1074,1075,1076,1077,1078,1079,1080,1081,1082,1083,1084,1085,1086,1087,1088,1089,1090,1091,1092,1093,1094,1095,1096,1097,1098,1099,1100,1101,1102,1103,1104,1105,1106]

lista_skims=["1000-t0 C ","1001-Direct distance C ","1002-Toll C ","1003-Trip distance C ","1004-Direct distance C 50Km Filter ","1005-User-defined C ","1006-t0 C Penalty ","1007-Access&Egress time B ","1008-Access&Egress time R ","1009-Access&Egress time A ","1010-Access&Egress time S ","1011-In-vehicle time B ","1012-Transfer wait time B ","1013-Access time B ","1014-Egress time B ","1015-Number of transfers B ","1016-Service frequency B ","1017-In-vehicle distance B ","1018-Fare B ","1019-Equivalent journey time B ","1020-In-vehicle time R ","1021-Transfer wait time R ","1022-Access time R ","1023-Egress time R ","1024-Number of transfers R ","1025-Service frequency R ","1026-In-vehicle distance R ","1027-Fare R ","1028-Equivalent journey time R ","1029-In-vehicle time A ","1030-Transfer wait time A ","1031-Access time A ","1032-Egress time A ","1033-Number of transfers A ","1034-Service frequency A ","1035-In-vehicle distance A ","1036-Attribute for path leg skim A ","1037-Equivalent journey time A ","1038-In-vehicle time S ","1039-Transfer wait time S ","1040-Access time S ","1041-Egress time S ","1042-Number of transfers S ","1043-Service frequency S ","1044-In-vehicle distance S ","1045-Attribute for path leg skim S ","1046-Equivalent journey time S ","1047-Access&Egress time B&A ","1048-Fare B&A ","1049-In-vehicle distance B&A ","1050-Service frequency B&A ","1051-Legs Number B&A ","1052-Number of transfers B&A ","1053-Transfer wait time B&A ","1054-In-vehicle time MMA B&A ","1055-In-vehicle time MMR B&A ","1056-In-vehicle time MMS B&A ","1057-Access&Egress time R&A ","1058-Fare R&A ","1059-In-vehicle distance R&A ","1060-Service frequency R&A ","1061-Legs Number R&A ","1062-Number of transfers R&A ","1063-Transfer wait time R&A ","1064-In-vehicle time MMA R&A ","1065-In-vehicle time MMR R&A ","1066-In-vehicle time MMS R&A ","1067-Access&Egress time C&A ","1068-Fare C&A ","1069-In-vehicle distance C&A ","1070-Service frequency C&A ","1071-Legs Number C&A ","1072-Number of transfers C&A ","1073-Transfer wait time C&A ","1074-In-vehicle time MMA C&A ","1075-In-vehicle time MMR C&A ","1076-In-vehicle time MMS C&A ","1077-Access&Egress time C&S ","1078-Fare C&S ","1079-In-vehicle distance C&S ","1080-Service frequency C&S ","1081-Legs Number C&S ","1082-Number of transfers C&S ","1083-Transfer wait time C&S ","1084-In-vehicle time MMA C&S ","1085-In-vehicle time MMR C&S ","1086-In-vehicle time MMS C&S ","1087-Access&Egress time C&R ","1088-Fare C&R ","1089-In-vehicle distance C&R ","1090-Service frequency C&R ","1091-Legs Number C&R ","1092-Number of transfers C&R ","1093-Transfer wait time C&R ","1094-In-vehicle time MMA C&R ","1095-In-vehicle time MMR C&R ","1096-In-vehicle time MMS C&R ","1097-Access&Egress time B&R ","1098-Fare B&R ","1099-In-vehicle distance B&R ","1100-Service frequency B&R ","1101-Legs Number B&R ","1102-Number of transfers B&R ","1103-Transfer wait time B&R ","1104-In-vehicle time MMA B&R ","1105-In-vehicle time MMR B&R","1106-In-vehicle time MMS B&R"]



origen=repeat(VPH.GetMulti(Visum.Net.Zones,"No",activeOnly=False),381)
destino=VPH.GetMulti(Visum.Net.Zones,"No",activeOnly=False)*381


vector_od=pd.DataFrame({"Origen":origen,"Destino":destino}, columns=["Origen","Destino"])
    
i=0

for skim in lista_skims: 

    matriz= pd.DataFrame(data=VPH.GetODMatrix(Visum,lista_matrices[i]).flatten(),columns=[skim])
    vector_od=pd.concat([vector_od,matriz],axis=1)
       
    i=i+1
    


vector_od.to_csv("Skims_O06.csv", index=True)
