# Script 9 
# -*- coding: utf-8 -*-
import os

# Get current Visum path
Path = Visum.GetPath(59)

# Read operation variable "ScenNo"
myScenNo = Visum.Procedures.OperationVariables.GetOperationVariable("ScenNo")
# Convert scenario number to string
scen_no = str(myScenNo.ValueOfVariable)

# Create link list
LinkList = Visum.Lists.CreateLinkList
LinkList.OpenLayout("Links-ROD.llax")
# Build output file path
out_links = os.path.join(Path, "Links_" + scen_no + ".csv")
# Save link list to attribute file
LinkList.SaveToAttributeFile(out_links, 44)

#Create Lineroutes list
LineRouteList = Visum.Workbench.Lists.CreateLineRouteList
LineRouteList.OpenLayout("Lineroutes.llax")
# Build output file path
out_lineroutes = os.path.join(Path, "Lineroutes_" + scen_no + ".csv")
# Save link list to attribute file
LineRouteList.SaveToAttributeFile(out_lineroutes, 44)

#Create Stoppoints list
StopPointsList = Visum.Workbench.Lists.CreateStopPointBaseList
StopPointsList.OpenLayout("Stoppoints.llax")
# Build output file path
out_stoppoint = os.path.join(Path, "Stoppoint_" + scen_no + ".csv")
# Save link list to attribute file
StopPointsList.SaveToAttributeFile(out_stoppoint, 44)

#Create PuTPathLegs list
PuTPathlegList = Visum.Workbench.Lists.CreatePuTPathLegList
PuTPathlegList.OpenLayout("PuTPathlegs-ROD_Metro.llax")
# Build output file path
out_pathlegs = os.path.join(Path, "PuTpathlegs_Metro_" + scen_no + ".sqlite3")
# Save link list to attribute file
PuTPathlegList.SaveToAttributeFile(out_pathlegs, 44)

#Create PuTPathLegs list
PuTPathlegList = Visum.Workbench.Lists.CreatePuTPathLegList
PuTPathlegList.OpenLayout("PuTPathlegs-ROD_NoMetro.llax")
# Build output file path
out_pathlegs = os.path.join(Path, "PuTpathlegs_NoMetro_" + scen_no + ".sqlite3")
# Save link list to attribute file
PuTPathlegList.SaveToAttributeFile(out_pathlegs, 44)
