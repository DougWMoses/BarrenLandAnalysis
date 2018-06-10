

class FarmLandUnit:
    def __init__(self, xcoord, ycoord):

        self.xcoord = xcoord
        self.ycoord = ycoord
        self.visited = False
        self.adjacentFarmLandUnits = []