from queue import *
from factories.barrenSectionFactory import BarrenSectionFactory
from factories.farmPlotFactory import FarmPlotFactory
from models.farmPlot import FarmPlot


class BarrenLandAnalysisService:

    def __init__(self):
        pass

    def do_farm_analysis(self, farm_width, farm_height, barren_plots):
        farm_plot_matrix = self.build_farm_plot_matrix(farm_width, farm_height)
        self.mark_barren_plots(farm_plot_matrix, barren_plots)
        result = self.calculate_fertile_farm(farm_plot_matrix)

    def build_farm_plot_matrix(self, width, height):
        # create a two dimensional array of FarmPlot objects
        return [[FarmPlotFactory.create_farm_plot(w, h) for h in range(height)] for w in range(width)]

    def mark_barren_plots(self, farm_plot_matrix, barren_plots):
        barren_sections = self.convert_barren_plots_set_to_barren_section_array(barren_plots)
        for barren_section in barren_sections:
            for xCoord in range(barren_section.fromX, barren_section.toX + 1):
                for yCoord in range(barren_section.fromY, barren_section.toY + 1):
                    self.mark_barren_plot(farm_plot_matrix, xCoord, yCoord)

    def mark_barren_plot(self, farm_plot_matrix, x_coord, y_coord):
        farm_plot_matrix[x_coord][y_coord].isBarren = True

    def calculate_fertile_farm(self, farm_plot_matrix):
        fertile_sections = []
        for xCoord in range(len(farm_plot_matrix)):
            for yCoord in range(len(farm_plot_matrix[0])):
                if self.is_fertile(farm_plot_matrix[xCoord][yCoord]):
                    fertile_sections.append(self.get_connected_fertile_plots(farm_plot_matrix,
                                                                             farm_plot_matrix[xCoord][yCoord]))
        return fertile_sections

    def convert_barren_plots_set_to_barren_section_array(self, barren_plots_set):
        barren_sections = []
        for barren_plot in barren_plots_set:
            points = barren_plot.split(" ")
            barren_sections.append(BarrenSectionFactory.create_barren_section(points[0], points[2], points[1], points[3]))
        return barren_sections

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

    def get_left_neighbor(self, farm_plot_matrix, farm_plot: FarmPlot):
        if (farm_plot.xCoord - 1) >= 0:
            return farm_plot_matrix[farm_plot.xCoord - 1][farm_plot.yCoord]
        return None

    def get_right_neighbor(self, farm_plot_matrix, farm_plot: FarmPlot):
        if (farm_plot.xCoord + 1) < len(farm_plot_matrix):
            return farm_plot_matrix[farm_plot.xCoord + 1][farm_plot.yCoord]
        return None

    def get_upper_neighbor(self, farm_plot_matrix, farm_plot: FarmPlot):
        if (farm_plot.yCoord + 1) < len(farm_plot_matrix[0]):
            return farm_plot_matrix[farm_plot.xCoord][farm_plot.yCoord + 1]
        return None

    def get_lower_neighbor(self, farm_plot_matrix, farm_plot: FarmPlot):
        if (farm_plot.yCoord - 1) >= 0:
            return farm_plot_matrix[farm_plot.xCoord][farm_plot.yCoord - 1]
        return None

    def is_fertile(self, farm_plot: FarmPlot):
        return farm_plot and not farm_plot.isBarren and not farm_plot.visited
