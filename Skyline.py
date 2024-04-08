import sys
import os

class Building:
    def __init__(self, height, left_coordinate, right_coordinate):
        self.height = height
        self.left_coordinate = left_coordinate
        self.right_coordinate = right_coordinate


class BuildingTuple:
    def __init__(self, height, x_coordinate):
        self.height = height
        self.x_coordinate = x_coordinate

    def __str__(self):
        return f"({self.height},{self.x_coordinate})"


class Skyline:
    @staticmethod
    def recursive_function2( buildings:list):
        if len(buildings) == 1:
            return [BuildingTuple(buildings[0].height, buildings[0].left_coordinate),
                    BuildingTuple(0, buildings[0].right_coordinate)]

        mid = len(buildings) // 2
        left = Skyline.recursive_function2(buildings[:mid])
        right = Skyline.recursive_function2(buildings[mid:])

        return Skyline.merge(left, right)

    @staticmethod
    def merge(left, right):

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

        
def getInputBuildingFiles() -> list:  # pathing in VScode is odd, so this is added to fix it. Shouldn't cause any issues with other IDE's
    path = ''
    if getattr(sys, 'frozen', False):
        path = os.path.dirname(os.path.realpath(sys.executable))
    elif __file__:
        path = os.path.dirname(__file__)

    dirPath = os.path.join(path, 'InputBuildings')
    return [os.path.join(dirPath, file) for file in os.listdir(dirPath) if os.path.isfile(os.path.join(dirPath, file))]

if __name__ == "__main__":
    
    for fullFilePath in getInputBuildingFiles():
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
        print(",".join(str(result) for result in results))


    