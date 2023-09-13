import arcpy 

##### Create a geodatabase (gdb)
folder_path = 'C:\\Users\\MEI-KUEI LU\\Downloads\\GEOG676_GIS_Programming\\Lab\\GEOG676_GISProgramming\\Lab04\\Lab04_Data'
gdb_name = 'Lab04.gdb'
gdb_path = folder_path + '\\' + gdb_name
arcpy.CreateFileGDB_management(folder_path, gdb_name)

###### read csv file of garage, make it a layer and put it to the gdb 
csv = 'C:\\Users\\MEI-KUEI LU\\Downloads\\GEOG676_GIS_Programming\\Lab\\GEOG676_GISProgramming\\Lab04\\Lab04_Data\\garages.csv'
garage_layer_name = 'Garage_Points'
garages = arcpy.MakeXYEventLayer_management(csv, 'X', 'Y', garage_layer_name)

# put garages to gdb 
input_layer = garages
arcpy.FeatureClassToGeodatabase_conversion(input_layer, gdb_path)

# get the Garage_Points layer in gdb
garage_points = gdb_path + '\\' + garage_layer_name

##### Copy the building feature in the Campus.gdb to Lab04.gdb 
campus = 'C:\\Users\\MEI-KUEI LU\\Downloads\\GEOG676_GIS_Programming\\Lab\\GEOG676_GISProgramming\\Lab04\\Lab04_Data\\Campus.gdb'
campus_buildings = campus + '\\Structures' 

# set the destination path for campus_buildings  
buildings = gdb_path + '\\' + 'Buildings'

# Copy 
arcpy.Copy_management(campus_buildings, buildings)

##### Project the Garage_Points layer to the projection of Buildings layer 
spatial_ref = arcpy.Describe(buildings).spatialReference 
arcpy.Project_management(garage_points, gdb_path + '\Garage_Points_reprojected', spatial_ref)

##### Spatial analysis for buildings and garage_points 
# Buffer 
garage_buffer = arcpy.Buffer_analysis(gdb_path + '\Garage_Points_reprojected', gdb_path + '\Garage_Points_buffer', 150)

# Intersect the buffer with the buildings 
arcpy.Intersect_analysis([garage_buffer, buildings], gdb_path + '\Garage_building_intersect', 'ALL')

# Output the info of nearbyBuildings to a csv 
arcpy.TableToTable_conversion(gdb_path + '\Garage_building_intersect.dbf', folder_path, 'nearbyBuilding.csv')

