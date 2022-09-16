from GeosteeringOffice.Autocorrelation.Api import Transfer
from AutoCorrelation import GenerateSynthetics


class SyntheticGenerator:
    def __init__(self, scenario_path, angle: int = 120, synthetic_count: int = 50):
        self.Scenario = Transfer.Load(scenario_path)
        self.Generator = GenerateSynthetics()
        self.Generator.Angle = angle
        self.Generator.SyntheticCountOnStep = synthetic_count

    def generate(self, top_x1, top_y1, top_x2, top_y2, bot_x1, bot_y1, bot_x2, bot_y2):
        self.Generator.FirstPointTopX = top_x1
        self.Generator.FirstPointTopY = top_y1
        self.Generator.SecondPointTopX = top_x2
        self.Generator.SecondPointTopY = top_y2

        self.Generator.FirstPointBottomX = bot_x1
        self.Generator.FirstPointBottomY = bot_y1
        self.Generator.SecondPointBottomX = bot_x2
        self.Generator.SecondPointBottomY = bot_y2

        return self.Generator.Generate(self.Scenario)
