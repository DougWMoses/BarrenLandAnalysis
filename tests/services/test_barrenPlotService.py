from unittest import TestCase

from services.barrenPlotService import BarrenPlotService
from services.fertilePlotService import FertilePlotService


class TestBarrenPlotService(TestCase):
    def setUp(self):
        self.bps = BarrenPlotService()
        self.fps = FertilePlotService()

    def test_mark_barren_plot_should_set_is_barren_flag_to_true_at_correct_location_of_matrix(self):
        xCoord = 1
        yCoord = 2
        matrix = self.fps.build_farm_plot_matrix(3, 3)
        self.bps.mark_barren_plot(matrix, xCoord, yCoord)
        self.assertTrue(matrix[xCoord][yCoord].isBarren)

    def test_convert_barren_plots_set_to_barren_section_array_should_return_array_of_barren_sections_objects(self):
        barren_plots_set = {"1 2 3 4", "5 6 7 8"}
        barren_sections_array = self.bps.convert_barren_plots_set_to_barren_section_array(barren_plots_set)
        self.assertEqual(len(barren_sections_array), 2)

    def test_convert_barren_plots_set_to_barren_section_array_should_skip_any_set_that_has_fewer_or_more_than_four_points(self):
        barren_plots_set = {"1 2 3 4 5", "5 6 7"}
        barren_sections_array = self.bps.convert_barren_plots_set_to_barren_section_array(barren_plots_set)
        self.assertEqual(len(barren_sections_array), 0)

    def test_mark_barren_plots_should_mark_barren_plots_as_barren(self):
        barren_plots = {"0 0 1 0", "0 0 0 1"}
        matrix = self.fps.build_farm_plot_matrix(3, 3)
        self.bps.mark_barren_plots(matrix, barren_plots)
        self.assertTrue(matrix[0][0].isBarren)
        self.assertTrue(matrix[1][0].isBarren)
        self.assertTrue(matrix[0][1].isBarren)
        self.assertFalse(matrix[1][1].isBarren)
        self.assertFalse(matrix[2][1].isBarren)
        self.assertFalse(matrix[2][0].isBarren)
        self.assertFalse(matrix[1][2].isBarren)
        self.assertFalse(matrix[2][2].isBarren)

    def test_mark_barren_plots_should_ignore_barren_plots_that_extend_beyond_the_farm(self):
        barren_plots = {"0 0 1 0", "0 1 2 1"}
        matrix = self.fps.build_farm_plot_matrix(2, 2)
        self.bps.mark_barren_plots(matrix, barren_plots)
        self.assertTrue(matrix[0][0].isBarren)
        self.assertTrue(matrix[1][0].isBarren)
        self.assertFalse(matrix[0][1].isBarren)
        self.assertFalse(matrix[1][1].isBarren)

    def test_mark_barren_plots_should_apply_no_barren_values_if_set_is_empty(self):
        barren_plots = {}
        matrix = self.fps.build_farm_plot_matrix(2, 2)
        self.bps.mark_barren_plots(matrix, barren_plots)
        self.assertFalse(matrix[0][0].isBarren)
        self.assertFalse(matrix[1][0].isBarren)
        self.assertFalse(matrix[0][1].isBarren)
        self.assertFalse(matrix[1][1].isBarren)