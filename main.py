
import pandas as pd

class kia:
    # class variable
    # used in class methods
    #kia_Model = "Kia Soul"
    # constructor to create and properly initialize objects of this class later
    def __init__(self, model):
        self.model = model  # instance variable
        self.list_Of_Specs = { }
    #Common in all soul trims/standard features
    def standard_Features(self, list):
       self.list_Of_Specs.append(list)
        #pandas series organizes dictionary values into columns
       series1 = pd.Series(self.list_Of_Specs)
       print(series1)



        # create class object
highlights = kia("Soul")
highlights.standard_Features({"Engine Type": "2.0L 4-Cylinder Engine", "Engine Valve Train":"Dual Overhead Cam (DOHC), 16-valve",
                             "Fuel System":"Multi-Port Gasoline Injection (MPI)",
                             "Horsepower":"147 hp @ 6,200 rpm", "Safety": "Collision Avoidance-Assist with Pedestrian Detection",
                             "Warranty":"Kia 10-year/100,000-mile",
                             "Dimensions": {"Length":"165.2 in.", "Width":"70.9 in.", "Height":"63.0 in."}
                              })
highlights.list_Of_Specs


#"Color": ["Steal Gray", "Snow White Pearl", "Fusion Black", "Gravity Gray"],

# Command to check for main function
# If main function is found go to it
#if __name__ == "__main__":
        #main()











