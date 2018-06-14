
from services.barrenLandAnalysisService import BarrenLandAnalysisService

FARM_WIDTH = 400
FARM_HEIGHT = 600

if __name__ == "__main__":
    bs = BarrenLandAnalysisService()
    user_input = input("Enter barren sections: ")
    user_input = user_input.replace("{", "").replace("}", "").replace('"', '').replace(", ", ",").split(',')

    if len(user_input) < 1:
        user_input = {}
    result = bs.do_farm_analysis(FARM_WIDTH, FARM_HEIGHT, user_input)
    print(result)
