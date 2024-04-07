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
        if len(left) > 0 and len(right) == 0:
            return left
        elif len(left) == 0 and len(right) > 0:
            return right

        return_list = []
        i = 0
        j = 0
        left_height = 0
        right_height = 0
        temp = None

        while i < len(left) and j < len(right):
            if left[i].x_coordinate < right[j].x_coordinate or left[i].height > right[j].height:
                left_height = left_height if left[i].height == 0 else left[i].height
                if temp is not None:
                    return_list.append(BuildingTuple(temp.height, temp.x_coordinate))
                    temp = None
                elif left_height > right_height:
                    return_list.append(BuildingTuple(left[i].height, left[i].x_coordinate))
                else:
                    return_list.append(BuildingTuple(right[j].height, right[j].x_coordinate))
                    j += 1
                i += 1
            elif left[i].x_coordinate > right[j].x_coordinate:
                right_height = right_height if right[j].height == 0 else right[j].height
                temp = None
                if left_height > right_height:
                    temp = BuildingTuple(right_height, left[-1].x_coordinate)
                elif left_height < right_height and right[j].height > 0:
                    return_list.append(BuildingTuple(right_height, right[j].x_coordinate))
                else:
                    return_list.append(BuildingTuple(left_height, right[j].x_coordinate))
                j += 1

        if i < len(left):
            return_list.extend(left[i:])
        if j < len(right):
            return_list.extend(right[j:])

        return return_list


if __name__ == "__main__":
    buildings = [
        Building(4, 4, 9),
        Building(2, 7, 12)
    ]

    skyline = Skyline()
    results = skyline.recursive_function2(buildings)
    print(results)