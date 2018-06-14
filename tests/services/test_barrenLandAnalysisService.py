from unittest import TestCase
from unittest.mock import patch

from services.barrenLandAnalysisService import BarrenLandAnalysisService
from services.barrenPlotService import BarrenPlotService
from services.fertilePlotService import FertilePlotService


class TestBarrenLandAnalysisService(TestCase):

    def setUp(self):
        self.blas = BarrenLandAnalysisService()

    @patch.object(FertilePlotService, "build_farm_plot_matrix")
    def test_do_farm_analysis_should_call_build_farm_plot_matrix(self, mock_build_farm_plot_matrix):
        mock_build_farm_plot_matrix.return_value = []
        self.blas.do_farm_analysis(1, 2, [])
        mock_build_farm_plot_matrix.assert_called_with(1, 2)

    @patch.object(FertilePlotService, "build_farm_plot_matrix")
    @patch.object(BarrenPlotService, "mark_barren_plots")
    def test_do_farm_analysis_should_call_mark_barren_plots(self, mock_mark_barren_plots, mock_build_farm_plot_matrix):
        mock_mark_barren_plots.return_value = []
        self.blas.do_farm_analysis(1, 2, [])
        mock_mark_barren_plots.assert_called()

    @patch.object(FertilePlotService, "build_farm_plot_matrix")
    @patch.object(BarrenPlotService, "mark_barren_plots")
    @patch.object(FertilePlotService, "calculate_fertile_section_areas")
    def test_do_farm_analysis_should_call_calculate_fertile_farm(self, mock_calculate_fertile_section_areas, mock_mark_barren_plots, mock_build_farm_plot_matrix):
        mock_calculate_fertile_section_areas.return_value = []
        self.blas.do_farm_analysis(1, 2, [])
        mock_calculate_fertile_section_areas.assert_called()

    @patch.object(FertilePlotService, "build_farm_plot_matrix")
    @patch.object(BarrenPlotService, "mark_barren_plots")
    @patch.object(FertilePlotService, "calculate_fertile_section_areas")
    @patch.object(BarrenLandAnalysisService, "output_format")
    def test_do_farm_analysis_should_call_output_format(self, mock_output_format, mock_calculate_fertile_section_areas, mock_mark_barren_plots, mock_build_farm_plot_matrix):
        mock_calculate_fertile_section_areas.return_value = [5, 3, 6, 1]
        result = self.blas.do_farm_analysis(1, 2, [])
        mock_output_format.assert_called_with([5, 3, 6, 1])

    def test_output_format_should_convert_array_of_integers_to_space_delimited_string(self):
        test_array = [5, 3, 6, 1]
        expected = "1 3 5 6"
        actual = self.blas.output_format(test_array)
        self.assertEqual(expected, actual)

    def test_output_format_should_convert_empty_array(self):
        test_array = []
        expected = "No data returned"
        actual = self.blas.output_format(test_array)
        self.assertEqual(expected, actual)
