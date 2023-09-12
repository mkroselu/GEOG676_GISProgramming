import arcpy 

# import data 
source = r'C:\\Users\\MEI-KUEI LU\\Downloads\\GEOG676_GIS_Programming\\Lab\\GEOG676_GISProgramming\\Lab07\\Lab07_Data\\'
result = r'C:\\Users\\MEI-KUEI LU\\Downloads\\GEOG676_GIS_Programming\\Lab\\GEOG676_GISProgramming\\Lab07\\Lab07_Result\\'
band1= arcpy.sa.Raster(source + 'LT05_L2SP_026039_20110803_20200820_02_T1_SR_B1.TIF') # blue 
band2= arcpy.sa.Raster(source + 'LT05_L2SP_026039_20110803_20200820_02_T1_SR_B2.TIF') # green 
band3= arcpy.sa.Raster(source + 'LT05_L2SP_026039_20110803_20200820_02_T1_SR_B3.TIF') # red 
band4= arcpy.sa.Raster(source + 'LT05_L2SP_026039_20110803_20200820_02_T1_SR_B4.TIF') # NIR 

# Composite bands 
composite = arcpy.CompositeBands_management([band1, band2, band3, band4], result + 'composite.tif')

# Use DEM to create hillshade 
azimuth = 315 
altitude = 45 
shadows = 'NO_SHADOWS'
z_factor = 1
arcpy.ddd.HillShade(source + r'\\n30_w097_1arc_v3.tif', result + r'\\hillshade.tif', azimuth, altitude, shadows, z_factor)

# Use DEM to create slope image  
output_measurement = 'DEGREE'
z_factor = 1
arcpy.ddd.Slope(source + r'\\n30_w097_1arc_v3.tif', result + r'\\slope.tif', output_measurement, z_factor)

