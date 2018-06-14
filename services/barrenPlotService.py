from factories.barrenSectionFactory import BarrenSectionFactory
from models.barrenSection import BarrenSection


class BarrenPlotService:

    def __init__(self):
        pass

    def mark_barren_plots(self, farm_plot_matrix, barren_plots):
        barren_sections = self.convert_barren_plots_set_to_barren_section_array(barren_plots)
        for barren_section in barren_sections:
            if self.section_out_of_bounds(barren_section, farm_plot_matrix):
                continue

            for xCoord in range(barren_section.fromX, barren_section.toX + 1):
                for yCoord in range(barren_section.fromY, barren_section.toY + 1):
                    self.mark_barren_plot(farm_plot_matrix, xCoord, yCoord)

    @staticmethod
    def mark_barren_plot(farm_plot_matrix, x_coord, y_coord):
        farm_plot_matrix[x_coord][y_coord].isBarren = True

    @staticmethod
    def convert_barren_plots_set_to_barren_section_array(barren_plots_set):
        barren_sections = []
        for barren_plot in barren_plots_set:
            points = barren_plot.split(" ")
            if len(points) == 4:
                barren_sections.append(BarrenSectionFactory.create_barren_section(points[0], points[2], points[1], points[3]))
        return barren_sections

    @staticmethod
    def section_out_of_bounds(section: BarrenSection, farm_plot_matrix):
        return section.fromX < 0 or section.toX >= len(farm_plot_matrix) \
               or section.fromY < 0 or section.toY >= len(farm_plot_matrix[0])