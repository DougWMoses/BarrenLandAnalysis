from queue import Queue

from factories.farmPlotFactory import FarmPlotFactory
from models.farmPlot import FarmPlot


class FertilePlotService:

    def __init__(self):
        pass

    # create a two dimensional array of FarmPlot objects
    @staticmethod
    def build_farm_plot_matrix(width, height):
        return [[FarmPlotFactory.create_farm_plot(w, h) for h in range(height)] for w in range(width)]

    def calculate_fertile_section_areas(self, farm_plot_matrix):
        fertile_section_areas = []
        for xCoord in range(len(farm_plot_matrix)):
            for yCoord in range(len(farm_plot_matrix[0])):
                if self.is_fertile(farm_plot_matrix[xCoord][yCoord]):
                    fertile_section_area = len(self.get_connected_fertile_plots(farm_plot_matrix,
                                                                             farm_plot_matrix[xCoord][yCoord]))
                    if fertile_section_area > 0:
                        fertile_section_areas.append(fertile_section_area)
        return fertile_section_areas

    def get_connected_fertile_plots(self, farm_plot_matrix, root_plot):
        fertile_plots = []
        plot_queue = Queue()
        if self.is_fertile(root_plot):
            plot_queue.put(root_plot)
            root_plot.visited = True

        while not plot_queue.empty():
            farm_plot = plot_queue.get()
            fertile_plots.append(farm_plot)
            left_neighbor = self.get_left_neighbor(farm_plot_matrix, farm_plot)
            right_neighbor = self.get_right_neighbor(farm_plot_matrix, farm_plot)
            upper_neighbor = self.get_upper_neighbor(farm_plot_matrix, farm_plot)
            lower_neighbor = self.get_lower_neighbor(farm_plot_matrix, farm_plot)
            if self.is_fertile(left_neighbor):
                plot_queue.put(left_neighbor)
                left_neighbor.visited = True
            if self.is_fertile(right_neighbor):
                plot_queue.put(right_neighbor)
                right_neighbor.visited = True
            if self.is_fertile(upper_neighbor):
                plot_queue.put(upper_neighbor)
                upper_neighbor.visited = True
            if self.is_fertile(lower_neighbor):
                plot_queue.put(lower_neighbor)
                lower_neighbor.visited = True

        return fertile_plots

    @staticmethod
    def get_left_neighbor(farm_plot_matrix, farm_plot: FarmPlot):
        if (farm_plot.xCoord - 1) >= 0:
            return farm_plot_matrix[farm_plot.xCoord - 1][farm_plot.yCoord]
        return None

    @staticmethod
    def get_right_neighbor(farm_plot_matrix, farm_plot: FarmPlot):
        if (farm_plot.xCoord + 1) < len(farm_plot_matrix):
            return farm_plot_matrix[farm_plot.xCoord + 1][farm_plot.yCoord]
        return None

    @staticmethod
    def get_upper_neighbor(farm_plot_matrix, farm_plot: FarmPlot):
        if (farm_plot.yCoord + 1) < len(farm_plot_matrix[0]):
            return farm_plot_matrix[farm_plot.xCoord][farm_plot.yCoord + 1]
        return None

    @staticmethod
    def get_lower_neighbor(farm_plot_matrix, farm_plot: FarmPlot):
        if (farm_plot.yCoord - 1) >= 0:
            return farm_plot_matrix[farm_plot.xCoord][farm_plot.yCoord - 1]
        return None

    @staticmethod
    def is_fertile(farm_plot: FarmPlot):
        return farm_plot and not farm_plot.isBarren and not farm_plot.visited
