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
        height = 3
        actual = self.blas.build_farm_plot_matrix(width, height)
        self.assertEqual(len(actual), height)
        self.assertEqual(len(actual[0]), width)

    def test_mark_barren_plot_should_set_is_barren_flag_to_true_at_correct_location_of_matrix(self):
        xCoord = 1
        yCoord = 2
        matrix = self.blas.build_farm_plot_matrix(3, 3)
        self.blas.mark_barren_plot(matrix, xCoord, yCoord)
        self.assertTrue(matrix[xCoord][yCoord].isBarren)

    def test_convert_barren_plots_set_to_barren_section_array_should_return_array_of_barren_sections_objects(self):
        barren_plots_set = {"1 2 3 4", "5 6 7 8"}
        barren_sections_array = self.blas.convert_barren_plots_set_to_barren_section_array(barren_plots_set)
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

    def test_get_left_neighbor_should_return_neighboring_left_x_axis_node(self):
        matrix = self.blas.build_farm_plot_matrix(2, 2)
        result = self.blas.get_left_neighbor(matrix, matrix[1][0])
        self.assertEqual(result.xCoord, 0)
        self.assertEqual(result.yCoord, 0)

    def test_get_left_neighbor_should_return_none_if_no_neighbor_exists(self):
        matrix = self.blas.build_farm_plot_matrix(2, 2)
        result = self.blas.get_left_neighbor(matrix, matrix[0][0])
        self.assertEqual(result, None)

    def test_get_right_neighbor_should_return_neighboring_x_axis_node(self):
        matrix = self.blas.build_farm_plot_matrix(2, 2)
        result = self.blas.get_right_neighbor(matrix, matrix[0][0])
        self.assertEqual(result.xCoord, 1)
        self.assertEqual(result.yCoord, 0)

    def test_get_right_neighbor_should_return_none_if_no_neighbor_exists(self):
        matrix = self.blas.build_farm_plot_matrix(2, 2)
        result = self.blas.get_right_neighbor(matrix, matrix[1][1])
        self.assertEqual(result, None)

    def test_get_upper_neighbor_should_return_neighboring_y_axis_node(self):
        matrix = self.blas.build_farm_plot_matrix(2, 2)
        result = self.blas.get_upper_neighbor(matrix, matrix[0][0])
        self.assertEqual(result.xCoord, 0)
        self.assertEqual(result.yCoord, 1)

    def test_get_upper_neighbor_should_return_none_if_no_neighbor_exists(self):
        matrix = self.blas.build_farm_plot_matrix(2, 2)
        result = self.blas.get_upper_neighbor(matrix, matrix[1][1])
        self.assertEqual(result, None)

    def test_get_lower_neighbor_should_return_neighboring_x_axis_node(self):
        matrix = self.blas.build_farm_plot_matrix(2, 2)
        result = self.blas.get_lower_neighbor(matrix, matrix[0][1])
        self.assertEqual(result.xCoord, 0)
        self.assertEqual(result.yCoord, 0)

    def test_get_lower_neighbor_should_return_none_if_no_neighbor_exists(self):
        matrix = self.blas.build_farm_plot_matrix(2, 2)
        result = self.blas.get_lower_neighbor(matrix, matrix[0][0])
        self.assertEqual(result, None)

    def test_get_connected_fertile_plots_should_return_array_with_fertile_plots_connected_to_root_plot(self):
        barren_plots = {"0 0 1 0", "0 0 0 1"}
        matrix = self.blas.build_farm_plot_matrix(3, 3)
        self.blas.mark_barren_plots(matrix, barren_plots)
        result = self.blas.get_connected_fertile_plots(matrix, matrix[2][0])
        self.assertEqual(len(result), 6)

    def test_calculate_fertile_farm_should_return_an_array_connected_fertile_plot_arrays(self):
        barren_plots = {"0 0 1 0", "0 0 0 1"}
        matrix = self.blas.build_farm_plot_matrix(3, 3)
        self.blas.mark_barren_plots(matrix, barren_plots)
        result = self.blas.calculate_fertile_farm(matrix)
        self.assertEqual(len(result), 1)
        self.assertEqual(len(result[0]), 6)

    def test_calculate_fertile_farm_should_return_an_array_with_two_sections(self):
        barren_plots = {"0 1 2 1"}
        matrix = self.blas.build_farm_plot_matrix(3, 3)
        self.blas.mark_barren_plots(matrix, barren_plots)
        result = self.blas.calculate_fertile_farm(matrix)
        self.assertEqual(len(result), 2)
        self.assertEqual(len(result[0]), 3)
        self.assertEqual(len(result[1]), 3)

    def test_calculate_fertile_farm_should_return_an_array_four_sections(self):
        barren_plots = {"0 1 2 1", "1 0 1 2"}
        matrix = self.blas.build_farm_plot_matrix(3, 3)
        self.blas.mark_barren_plots(matrix, barren_plots)
        result = self.blas.calculate_fertile_farm(matrix)
        self.assertEqual(len(result), 4)
        self.assertEqual(len(result[0]), 1)
        self.assertEqual(len(result[1]), 1)
        self.assertEqual(len(result[2]), 1)
        self.assertEqual(len(result[3]), 1)

    def test_calculate_fertile_farm_should_return_an_array_that_includes_an_enclosed_section(self):
        barren_plots = {"1 1 1 3", "1 3 3 3", "1 1 3 1", "3 1 3 3"}
        matrix = self.blas.build_farm_plot_matrix(5, 5)
        self.blas.mark_barren_plots(matrix, barren_plots)
        result = self.blas.calculate_fertile_farm(matrix)
        self.assertEqual(len(result), 2)
        self.assertEqual(len(result[0]), 16)
        self.assertEqual(len(result[1]), 1)

    def test_calculate_fertile_farm_should_return_with_a_large_example(self):
        barren_plots = {"0 292 399 307"}
        matrix = self.blas.build_farm_plot_matrix(400, 600)
        self.blas.mark_barren_plots(matrix, barren_plots)
        result = self.blas.calculate_fertile_farm(matrix)
        self.assertEqual(len(result), 2)
        self.assertEqual(len(result[0]), 116800)
        self.assertEqual(len(result[1]), 116800)

    def test_calculate_fertile_farm_should_return_with_a_large_and_complex_example(self):
        barren_plots = {"48 192 351 207", "48 392 351 407", "120 52 135 547", "260 52 275 547"}
        matrix = self.blas.build_farm_plot_matrix(400, 600)
        self.blas.mark_barren_plots(matrix, barren_plots)
        result = self.blas.calculate_fertile_farm(matrix)
        self.assertEqual(len(result), 2)
        self.assertEqual(len(result[0]), 192608)
        self.assertEqual(len(result[1]), 22816)
