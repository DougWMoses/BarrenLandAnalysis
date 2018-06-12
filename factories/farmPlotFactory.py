from models.farmPlot import FarmPlot


class FarmPlotFactory:

    @staticmethod
    def create_farm_plot(xCoord, yCoord):
        return FarmPlot(xCoord, yCoord)
