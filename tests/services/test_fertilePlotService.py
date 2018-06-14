import unittest
from unittest import TestCase

from services.barrenPlotService import BarrenPlotService
from services.fertilePlotService import FertilePlotService


class TestFertilePlotService(TestCase):
    def setUp(self):
        self.fps = FertilePlotService()
        self.bps = BarrenPlotService()

    def test_build_farm_plot_should_create_a_two_dimensional_array_of_farm_plots(self):
        width = 3
        height = 3
        actual = self.fps.build_farm_plot_matrix(width, height)
        self.assertEqual(len(actual), height)
        self.assertEqual(len(actual[0]), width)

    def test_get_left_neighbor_should_return_neighboring_left_x_axis_node(self):
        matrix = self.fps.build_farm_plot_matrix(2, 2)
        result = self.fps.get_left_neighbor(matrix, matrix[1][0])
        self.assertEqual(result.xCoord, 0)
        self.assertEqual(result.yCoord, 0)

    def test_get_left_neighbor_should_return_none_if_no_neighbor_exists(self):
        matrix = self.fps.build_farm_plot_matrix(2, 2)
        result = self.fps.get_left_neighbor(matrix, matrix[0][0])
        self.assertEqual(result, None)

    def test_get_right_neighbor_should_return_neighboring_x_axis_node(self):
        matrix = self.fps.build_farm_plot_matrix(2, 2)
        result = self.fps.get_right_neighbor(matrix, matrix[0][0])
        self.assertEqual(result.xCoord, 1)
        self.assertEqual(result.yCoord, 0)

    def test_get_right_neighbor_should_return_none_if_no_neighbor_exists(self):
        matrix = self.fps.build_farm_plot_matrix(2, 2)
        result = self.fps.get_right_neighbor(matrix, matrix[1][1])
        self.assertEqual(result, None)

    def test_get_upper_neighbor_should_return_neighboring_y_axis_node(self):
        matrix = self.fps.build_farm_plot_matrix(2, 2)
        result = self.fps.get_upper_neighbor(matrix, matrix[0][0])
        self.assertEqual(result.xCoord, 0)
        self.assertEqual(result.yCoord, 1)

    def test_get_upper_neighbor_should_return_none_if_no_neighbor_exists(self):
        matrix = self.fps.build_farm_plot_matrix(2, 2)
        result = self.fps.get_upper_neighbor(matrix, matrix[1][1])
        self.assertEqual(result, None)

    def test_get_lower_neighbor_should_return_neighboring_x_axis_node(self):
        matrix = self.fps.build_farm_plot_matrix(2, 2)
        result = self.fps.get_lower_neighbor(matrix, matrix[0][1])
        self.assertEqual(result.xCoord, 0)
        self.assertEqual(result.yCoord, 0)

    def test_get_lower_neighbor_should_return_none_if_no_neighbor_exists(self):
        matrix = self.fps.build_farm_plot_matrix(2, 2)
        result = self.fps.get_lower_neighbor(matrix, matrix[0][0])
        self.assertEqual(result, None)

    def test_get_connected_fertile_plots_should_return_array_with_fertile_plots_connected_to_root_plot(self):
        barren_plots = {"0 0 1 0", "0 0 0 1"}
        matrix = self.fps.build_farm_plot_matrix(3, 3)
        self.bps.mark_barren_plots(matrix, barren_plots)
        result = self.fps.get_connected_fertile_plots(matrix, matrix[2][0])
        self.assertEqual(len(result), 6)

    def test_calculate_fertile_section_areas_should_return_an_array_connected_fertile_plot_arrays(self):
        barren_plots = {"0 0 1 0", "0 0 0 1"}
        matrix = self.fps.build_farm_plot_matrix(3, 3)
        self.bps.mark_barren_plots(matrix, barren_plots)
        result = self.fps.calculate_fertile_section_areas(matrix)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], 6)

    def test_calculate_fertile_section_areas_should_return_an_array_with_two_sections(self):
        barren_plots = {"0 1 2 1"}
        matrix = self.fps.build_farm_plot_matrix(3, 3)
        self.bps.mark_barren_plots(matrix, barren_plots)
        result = self.fps.calculate_fertile_section_areas(matrix)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0], 3)
        self.assertEqual(result[1], 3)

    def test_calculate_fertile_section_areas_should_return_an_array_four_sections(self):
        barren_plots = {"0 1 2 1", "1 0 1 2"}
        matrix = self.fps.build_farm_plot_matrix(3, 3)
        self.bps.mark_barren_plots(matrix, barren_plots)
        result = self.fps.calculate_fertile_section_areas(matrix)
        self.assertEqual(len(result), 4)
        self.assertEqual(result[0], 1)
        self.assertEqual(result[1], 1)
        self.assertEqual(result[2], 1)
        self.assertEqual(result[3], 1)

    def test_calculate_fertile_section_areas_should_return_an_array_that_includes_an_enclosed_section(self):
        barren_plots = {"1 1 1 3", "1 3 3 3", "1 1 3 1", "3 1 3 3"}
        matrix = self.fps.build_farm_plot_matrix(5, 5)
        self.bps.mark_barren_plots(matrix, barren_plots)
        result = self.fps.calculate_fertile_section_areas(matrix)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0], 16)
        self.assertEqual(result[1], 1)

    @unittest.SkipTest
    def test_calculate_fertile_section_areas_should_return_with_a_large_example(self):
        barren_plots = {"0 292 399 307"}
        matrix = self.fps.build_farm_plot_matrix(400, 600)
        self.bps.mark_barren_plots(matrix, barren_plots)
        result = self.fps.calculate_fertile_section_areas(matrix)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0], 116800)
        self.assertEqual(result[1], 116800)

    @unittest.SkipTest
    def test_calculate_fertile_section_areas_should_return_with_a_large_and_complex_example(self):
        barren_plots = {"48 192 351 207", "48 392 351 407", "120 52 135 547", "260 52 275 547"}
        matrix = self.fps.build_farm_plot_matrix(400, 600)
        self.bps.mark_barren_plots(matrix, barren_plots)
        result = self.fps.calculate_fertile_section_areas(matrix)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0], 192608)
        self.assertEqual(result[1], 22816)
