from typing import List

from GeosteeringOffice.Autocorrelation.Api import Transfer
from AutoCorrelation import GenerateSyntheticsFromSurface


class SyntheticGenerator:
    def __init__(self, scenario_path, offset_x: List[float] = None, offset_y: List[float] = None):
        scenario = Transfer.Load(scenario_path)
        offset_curve = GenerateSyntheticsFromSurface.CreateCurve(offset_x, offset_y)
        self.Generator = GenerateSyntheticsFromSurface(scenario, offset_curve)

    def generate(self, top_x: List[float], top_y: List[float], bot_x: List[float], bot_y: List[float]):
        return self.Generator.GenerateSyntheticsFromList(top_x, top_y, bot_x, bot_y)
