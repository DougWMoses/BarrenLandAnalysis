from utils.utils import input_set_to_actual_set
from services.barrenLandAnalysisService import BarrenLandAnalysisService

FARM_WIDTH = 400
FARM_HEIGHT = 600

if __name__ == "__main__":
    bs = BarrenLandAnalysisService()
    user_input = input("Enter barren sections: ")
    user_input = input_set_to_actual_set(user_input)

    if len(user_input) < 1:
        user_input = {}
    result = bs.do_farm_analysis(FARM_WIDTH, FARM_HEIGHT, user_input)
    print(result)
