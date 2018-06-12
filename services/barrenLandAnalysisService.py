
from factories.barrenSectionFactory import BarrenSectionFactory
from factories.farmPlotFactory import FarmPlotFactory


class BarrenLandAnalysisService:

    def __init__(self):
        pass

    def do_farm_analysis(self, farm_width, farm_height, barren_plots):
        farm_plot_matrix = self.build_farm_plot_matrix(farm_width, farm_height)
        self.mark_barren_plots(farm_plot_matrix, barren_plots)
        result = self.calculate_fertile_farm(farm_plot_matrix)

    def build_farm_plot_matrix(self, width, height):
        # create a two dimensional array of FarmPlot objects
        return [[FarmPlotFactory.create_farm_plot(w, h) for w in range(width)] for h in range(height)]

    def mark_barren_plots(self, farm_plot_matrix, barren_plots):
        barren_sections = self.barren_plots_set_to_barren_section_array(barren_plots)
        for barren_section in barren_sections:
            for yCoord in range(barren_section.fromY, barren_section.toY + 1):
                for xCoord in range(barren_section.fromX, barren_section.toX + 1):
                    self.mark_barren_plot(farm_plot_matrix, xCoord, yCoord)

    def mark_barren_plot(self, farm_plot_matrix, x_coord, y_coord):
        farm_plot_matrix[y_coord][x_coord].isBarren = True

    def calculate_fertile_farm(self, farm_plot_matrix):
        return []

    def barren_plots_set_to_barren_section_array(self, barren_plots_set):
        barren_sections = []
        for barren_plot in barren_plots_set:
            points = barren_plot.split(" ")
            barren_sections.append(BarrenSectionFactory.create_barren_section(points[0], points[2], points[1], points[3]))
        return barren_sections

