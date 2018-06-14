from services.barrenPlotService import BarrenPlotService
from services.fertilePlotService import FertilePlotService


class BarrenLandAnalysisService:

    def __init__(self):
        pass

    def do_farm_analysis(self, farm_width, farm_height, barren_plots):
        bps = BarrenPlotService()
        fps = FertilePlotService()
        farm_plot_matrix = fps.build_farm_plot_matrix(farm_width, farm_height)
        bps.mark_barren_plots(farm_plot_matrix, barren_plots)
        result = fps.calculate_fertile_section_areas(farm_plot_matrix)
        return self.output_format(result)

    @staticmethod
    def output_format(array_of_int):
        if len(array_of_int) == 0:
            return "No data returned"
        return " ".join(map(str, sorted(array_of_int)))
