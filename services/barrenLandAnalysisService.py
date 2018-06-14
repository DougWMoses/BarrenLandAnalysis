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
        result = sorted(fps.calculate_fertile_section_areas(farm_plot_matrix))
        return result



