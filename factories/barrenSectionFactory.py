from models.barrenSection import BarrenSection


class BarrenSectionFactory:

    @staticmethod
    def create_barren_section(from_x, to_x, from_y, to_y):
        return BarrenSection(int(from_x), int(to_x), int(from_y), int(to_y))
