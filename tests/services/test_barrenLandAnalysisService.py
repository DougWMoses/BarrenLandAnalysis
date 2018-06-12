from unittest import TestCase
from unittest.mock import patch

from services.barrenLandAnalysisService import BarrenLandAnalysisService


class TestBarrenLandAnalysisService(TestCase):

    def setUp(self):
        self.blas = BarrenLandAnalysisService()

    @patch.object(BarrenLandAnalysisService, "build_farm_plot_matrix")
    def test_do_farm_analysis_should_call_build_farm_plot_matrix(self, mock_build_farm_plot_matrix):
        mock_build_farm_plot_matrix.return_value = []
        self.blas.do_farm_analysis(1, 2, [])
        mock_build_farm_plot_matrix.assert_called_with(1, 2)

    @patch.object(BarrenLandAnalysisService, "build_farm_plot_matrix")
    @patch.object(BarrenLandAnalysisService, "mark_barren_plots")
    def test_do_farm_analysis_should_call_mark_barren_plots(self, mock_mark_barren_plots, mock_build_farm_plot_matrix):
        mock_mark_barren_plots.return_value = []
        self.blas.do_farm_analysis(1, 2, [])
        mock_mark_barren_plots.assert_called()

    @patch.object(BarrenLandAnalysisService, "build_farm_plot_matrix")
    @patch.object(BarrenLandAnalysisService, "mark_barren_plots")
    @patch.object(BarrenLandAnalysisService, "calculate_fertile_farm")
    def test_do_farm_analysis_should_call_calculate_fertile_farm(self, mock_calculate_fertile_farm, mock_mark_barren_plots, mock_build_farm_plot_matrix):
        mock_calculate_fertile_farm.return_value = []
        self.blas.do_farm_analysis(1, 2, [])
        mock_calculate_fertile_farm.assert_called()

    def test_build_farm_plot_should_create_a_two_dimensional_array_of_farm_plots(self):
        width = 3
        height = 4
        actual = self.blas.build_farm_plot_matrix(width, height)
        self.assertEqual(len(actual), height)
        self.assertEqual(len(actual[0]), width)

    def test_mark_barren_plot_should_set_is_barren_flag_to_true_at_correct_location_of_matrix(self):
        xCoord = 1
        yCoord = 2
        matrix = self.blas.build_farm_plot_matrix(3, 3)
        self.blas.mark_barren_plot(matrix, xCoord, yCoord)
        self.assertTrue(matrix[yCoord][xCoord].isBarren)

    def test_barren_plots_set_to_barren_section_array_should_return_array_of_barren_sections_objects(self):
        barren_plots_set = {"1 2 3 4", "5 6 7 8"}
        barren_sections_array = self.blas.barren_plots_set_to_barren_section_array(barren_plots_set)
        self.assertEqual(len(barren_sections_array), 2)

    def test_mark_barren_plots_should_mark_barren_plots_as_barren(self):
        barren_plots = {"0 0 1 0", "0 0 0 1"}
        matrix = self.blas.build_farm_plot_matrix(3, 3)
        self.blas.mark_barren_plots(matrix, barren_plots)
        self.assertTrue(matrix[0][0].isBarren)
        self.assertTrue(matrix[1][0].isBarren)
        self.assertTrue(matrix[0][1].isBarren)
        self.assertFalse(matrix[1][1].isBarren)
        self.assertFalse(matrix[2][1].isBarren)
        self.assertFalse(matrix[2][0].isBarren)
        self.assertFalse(matrix[1][2].isBarren)
        self.assertFalse(matrix[2][2].isBarren)

