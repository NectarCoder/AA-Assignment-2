import sys
import os

# Assignment Two
# Authors: Michael Hayes, Amrutvyasa Ramasamy, Cody Bijeaux
# Date:04/09/2024

#
# Class Name: Building
# Class Variables: 
#    1) [int] self.height: The stored height
#    2) [int] self.left_coordinate: the stored left coordinate
#    3) [int] self.right_coordinate: the stored right coordinate
# Usage: Stores the height and coordinates of buildings
#
class Building:
    #
    # Constructor
    # Formal Parameters:
    #   1) [int]  height: tracks the height of the building
    #   2) [int]  left_coordinate: tracks the left coordinate of the building
    #   3) [int]  right_coordinate: tracks the right coordinate of the building
    #
    def __init__(self, height:int, left_coordinate:int, right_coordinate:int):
        self.height = height
        self.left_coordinate = left_coordinate
        self.right_coordinate = right_coordinate
#
# Class Name: BuildingTuple
# Class Variables:
#       1) [int] self._self.height: the height stored within the object
#       2) [int] self._x_coordinate: the stored X coordinate
# Usage: stores the height and x-coordinate, to which is called by the toString
#
class BuildingTuple:
    #
    # Constructor
    # Formal Parameters:
    #   1) [int]  height: passes the height of the desired building
    #   2) [int]  x_coordinate: passes the x-coordinate of the desired building
    #
    def __init__(self, height:int, x_coordinate:int):
        self.height = height
        self.x_coordinate = x_coordinate
    #
    # Function Name: __str__
    # Formal Parameters: None
    # Return Value:str
    # Usage: prints out the height and x-coordinate of the building as a string
    #
    def __str__(self)-> str:
        return f"({self.height},{self.x_coordinate})"

#
# Class Name: Skyline
# Class Variables: None
# Usage: stores static methods that are used to generate the skyline from a group of buildings
#
class Skyline:

    # ALGORITHM PSEUDOCODE
    #
    # This is the pseudocode for the recursive Skyline Identifier algorithm. The implementation in Python can be found right below the pseudocode.
    # See README.md for execution instructions and test data information.
    # --------------------------------------------------
    #
    # recursiveSkylineFunction(List B of buildings)
    #     If there is only 1 building in B
    #         Return building
    #     Else:
    #         Divide buildings into left list L and right list R
    #         Left buildings = recursiveSkylineFunction(L)
    #         Right buildings = recursiveSkylineFunction(R)
    #
    #     Return mergeSkylineFunction(L, R)
    #
    #
    # mergeSkylineFunction(Left building list L, Right building list R)
    #     Initialize counters i, j = 0
    #     Initialize registers prev_left_height, prev_right_height = 0
    #     Initialize List skyline_list
    #
    #     While i and j haven't reached end of lists L and R respectively
    #         If left building starts before right building (L[i].x-coordinate < R[j].x-coordinate)
    #             Store current left building in prev_left_height
    #             Find max height in this situation (L[i] height vs. prev_right_height) for edge cases
    #             If last point in skyline_list has the same height
    #                 Do not append (no height change)
    #             Increment i
    #         If right building starts before left building (R[i].x-coordinate < L[j].x-coordinate)
    #             Store current right building in prev_right_height
    #             Find max height in this situation (R[i] height vs. prev_left_height) for edge cases
    #             If last point in skyline_list has the same height
    #                 Do not append (no height change)
    #             Increment j
    #
    #     If i didn't reach end of L (left building list)
    #         Append remaining buildings from L to skyline_list
    #     If j didn't reach end of R (right building list)
    #         Append remaining buildings from R to skyline_list
    #
    #     Return skyline_list




    #
    # Function Name: recursive_function2  <STATIC>
    # Formal Parameters:
    #   1) [list] buildings: the lsit of buildings that will be split and used to recall the function until the length of the list has only one building remain.
    # Return Value:list
    # Usage: splits the list of buildings until they are at their indivilual units, then recursively calls the merge function to track points to where the height of the skyline changes
    #
    @staticmethod
    def recursive_function2(buildings:list)->list:
        if len(buildings) == 1:
            return [BuildingTuple(buildings[0].height, buildings[0].left_coordinate),
                    BuildingTuple(0, buildings[0].right_coordinate)]        # if the list has only one element, then its information and another fake building sharing the same right coordinate but a
        mid = len(buildings) // 2                                           # 0 left coordinate are used.
        left = Skyline.recursive_function2(buildings[:mid])                # method recursively called on the left and right side until the base case is found.
        right = Skyline.recursive_function2(buildings[mid:])

        return Skyline.merge(left, right)                                    # method recursively used with the left and the right variables of the stored buildings
    #
    # Function Name: merge  <STATIC>
    # Formal Parameters:
    #   1) [int] left: the left skyline passed into the function to compare with the right coordinate
    #   2) [int]  right: the right skyline passed into the function to compare with the left coordinate
    # Return Value:list
    # Usage: called to compare two buildings and find the change of elevation and collection points to form a skyline of the buildings
    #
    @staticmethod
    def merge(left:int, right:int)->list:

        return_list = []
        i = 0
        j = 0
        previous_left_height = 0
        previous_right_height = 0
        skipAppend = False

        while i < len(left) and j < len(right):

            # When i is less than j, than we are processing based on left buildings position
            # When j is less than i, than we are processing based on right buildings position
            if left[i].x_coordinate < right[j].x_coordinate:
                # By saving the left hight here, we are storing the last iterations left hight. This comes in handy
                # when right[j].x_coordinate < left[i].x_coordinate and we are in the else statement. 
                # When that happens, we will have PREVIOUS iterations left height. We do the same in the else statement
                # by saving right height.
                previous_left_height = left[i].height

                # max_height is the current height compared to the PREVIOUS iterations hight or 0 if the PREVIOUS iteration
                # did not set it. For example, the first iteration, right_height would still be equal to 0.
                # Also, remember that the the hight of the right most position of the building will be 0, so in that case
                # we are: => max(left[i].height = 0, previous_right_height)
                max_height = max(left[i].height, previous_right_height)

                if len(return_list) > 0:
                    if return_list[len(return_list)-1].height == max_height:
                        # We do not want to save this point. 
                        # Examples of when this is true. See arrow. This is why saving the previous_right_height was important!!! 
                        """
                                    __________
                                    |         |
                                ___ |______   |
                                |   |     |   |
                                |   |     |   |
                                |   |  -->|   |
                        """
                        """
                                _________ _________
                                |         |         |
                                |         |         |
                                |         |<--      |
                        """
                        skipAppend = True
                        pass
                
                if skipAppend == False:  
                    #                
                    return_list.append(BuildingTuple(max_height, left[i].x_coordinate))
                else:
                    skipAppend = False #reset

                # Always move the pointer forward once we have processed the current position.
                i += 1
            # All comments made for the if statement above are identical for the else statement. 
            else:
                previous_right_height = right[j].height
                max_height = max(previous_left_height, right[j].height)
                if len(return_list) > 0:
                    if return_list[len(return_list)-1].height == max_height:
                        # We do not want to save this point. 
                        # Examples of when this is true. See arrow. This is why saving the previous_left_hight was important!!! 
                        """
                                _________
                                |    _____|________
                                |   |     |        |
                                |   |<--  |        |
                        """ 
                        """
                                _______________
                                |   _____      |    
                                |  |     |     |
                                |  |<--  |<--  |
                        """
                        """
                                _________ _________
                                |         |         |
                                |         |         |
                                |         |<--      |
                        """
                        skipAppend = True
                        pass
                
                if skipAppend == False:                    
                    return_list.append(BuildingTuple(max_height, right[j].x_coordinate))
                else:
                    skipAppend = False #reset

                j += 1

        # Save any unprocessed buildings. 
        if i < len(left):
            return_list.extend(left[i:])
        if j < len(right):
            return_list.extend(right[j:])

        return return_list

#
# Function Name: getInputBuildingFiles  <STATIC>
# Formal Parameters: None
# Return Value:list
# Usage: gets the pathing for all the input files within the InputBuildings folder
#
def getInputBuildingFiles() -> list:  # pathing in VScode is odd, so this is added to fix it. Shouldn't cause any issues with other IDE's
    path = ''
    if getattr(sys, 'frozen', False):
        path = os.path.dirname(os.path.realpath(sys.executable))
    elif __file__:
        path = os.path.dirname(__file__)

    dirPath = os.path.join(path, 'InputBuildings')
    return [os.path.join(dirPath, file) for file in os.listdir(dirPath) if os.path.isfile(os.path.join(dirPath, file))]

if __name__ == "__main__":
    output=[]
    for fullFilePath in getInputBuildingFiles():
        converted=''
        buildings = []
        with open(fullFilePath, "r") as rawdata:
            data = rawdata.read()
            if data == '':
                break
            compiled = data.split('\n')
            rawdata.close()
        for lines in compiled:
            results = lines.split(",")
            buildings.append(Building(int(results[0].replace(" ","")),int(results[1].replace(" ","")),int(results[2].replace(" ",""))))

        skyline = Skyline()
        results = skyline.recursive_function2(buildings)
        for result in results:
            converted+=str(result)[1:-1]+'\n'
        output.append(converted)
    paths=getInputBuildingFiles()
    for filenumber in range(len(output)):   #used to create the output files
        path=paths[filenumber].replace('InputBuildings','Output').replace('input','Output')  # file path is converted to the output file location
        file=open(path,'w')
        file.write(output[filenumber])
        file.close()                                # file is written and then closed
        print(f'Output File for Skyline {filenumber+1} created Successfully:\n{output[filenumber]}')   #terminal produces successful message of output file being created




