import pandas as pd
class Kia:

    def __init__(self, company, model):
        self.company = company
        self.model = model

    def display(self):
        print("Todya's Highlight is " + self.company + self.model)


#method outside class
    def standard_Features(cls):
        common_Features= {"Color": "Steal Gray, Snow White Pearl, Fusion Black, Gravity Gray", "Engine Type": "2.0L 4-Cylinder Engine", "Engine Valve Train":"Dual Overhead Cam (DOHC), 16-valve",
                             "Fuel System":"Multi-Port Gasoline Injection (MPI)",
                             "Horsepower":"147 hp @ 6,200 rpm", "Safety": "Collision Avoidance-Assist with Pedestrian Detection",
                             "Warranty":"Kia 10-year/100,000-mile",
                             "Dimensions": {"Length":"165.2 in.", "Width":"70.9 in.", "Height":"63.0 in."}
                              }
        series1 = pd.Series(common_Features)
        print("Kia Soul Common Features " + series1)


class Soul_S(Kia):
        def __init__(self):
            Kia.__init__(self, "Kia", "Soul S")

# method outside class - cls
        def added_Features(cls):
            newFeatures = {"Color": "Two toned - White / Black & Blue / Black", "Interior": "Black Woven Cloth only",
                       }
            series2 = pd.Series(newFeatures)
            print("Added features to Kia Soul S " + series2)




a = Kia("Kia", "Soul")
a.standard_Features()
a.disply()
b.Soul_S()
b.added_Features()
#Adding this method at runtime to class using classmethod()
Kia.standard_Features = classmethod(standard_Features)
Kia.standard_Features()
#Adding this method at runtime to class using classmethod()
Soul_S.added_Features = classmethod(added_Features)
Soul_S.added_Features()