import numpy  as np
import pandas as pd                     
from   math   import radians as DegToRad       # Degrees to radians Conversion

from shapely.geometry import Point             # Imported for constraint checking
from shapely.geometry.polygon import Polygon

import warnings
warnings.filterwarnings("ignore")

import csv

def save(file_name,turb_coords):
    #s=input('Give the name of file you want to save as: (ex: Team7_turb_coords_1)  --> :')
    with open(file_name,'a') as csv_file:
        csv_writer=csv.writer(csv_file,delimiter=',')
        #for ii in turb_coords:
        d=[]
        d.append(102415)
        d.append(2048852)
        csv_writer.writerow(d)
    print('file saved succesfully')





def getTurbLoc(turb_loc_file_name):
    """ 
    -**-THIS FUNCTION SHOULD NOT BE MODIFIED-**-
    
    Returns x,y turbine coordinates
    
    :Called from
        main function
    
    :param
        turb_loc_file_name - Turbine Loc csv file location
        
    :return
        2D array
    """
    
    df = pd.read_csv(turb_loc_file_name, sep=',', dtype = np.float32)
    # x=df['x']
    # print(x)
    # df['x']=df['y']
    # df['y']=x
    turb_coords = df.to_numpy(dtype = np.float)
    print(turb_coords)
    print("\n\n$$$$$$$$$$$$$$$\n\n")
    print(turb_coords.shape[0])
    print(turb_coords.shape[1])
    print("\n\n$$$$$$$$$$$$$$$\n\n")
    np.delete(turb_coords,-1,1)
    print(turb_coords)
    print(turb_coords.shape[0])
    print(turb_coords.shape[1])
    return(turb_coords)


if __name__ == "__main__":

    # Turbine Specifications.
    # -**-SHOULD NOT BE MODIFIED-**-
    turb_specs    =  {   
                         'Name': 'Anon Name',
                         'Vendor': 'Anon Vendor',
                         'Type': 'Anon Type',
                         'Dia (m)': 100,
                         'Rotor Area (m2)': 7853,
                         'Hub Height (m)': 100,
                         'Cut-in Wind Speed (m/s)': 3.5,
                         'Cut-out Wind Speed (m/s)': 25,
                         'Rated Wind Speed (m/s)': 15,
                         'Rated Power (MW)': 3
                     }
    turb_diam      =  turb_specs['Dia (m)']
    turb_rad       =  turb_diam/2 


    turb_coords   =  getTurbLoc(r'../Shell_Hackathon Dataset/turbine_loc_test.csv')
    save(r'../Shell_Hackathon Dataset/turbine_loc_test.csv',turb_coords)
    # Turbine x,y coordinate

