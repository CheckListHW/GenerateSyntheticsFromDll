import os

from utils.synthetic_generator.generator import SyntheticGenerator
from GeosteeringOffice.Autocorrelation.Api import Transfer

from matplotlib import pyplot as plt

if __name__ == '__main__':
    scenario_path = os.getcwd() + '/input.xml'
    scenario = Transfer.Load(scenario_path)

    offset_x = []
    offset_y = []
    for point in scenario.Properties[0].Offset.Points:
        offset_x.append(point.Position)
        offset_y.append(point.Value)

    generator = SyntheticGenerator(scenario_path, offset_x, offset_y)

    top_x = [966.7529628351272, 996.7529628351272]
    top_y = [1921.40443483379, 1926.6005872564963]
    bot_x = [966.7529628351272, 996.7529628351272]
    bot_y = [1926.805672095235, 1932.0018245179413]

    x, y = [], []
    step = 30

    import time
    print(f'start: {time.time() - (start_time := time.time())}')
    curve = generator.generate(top_x, top_y, bot_x, bot_y).Points
    print(f'finish: {round(time.time() - start_time, 8)/1000}ms')

    for point in curve:
        x.append(point.Position)
        y.append(point.Value)
    plt.plot(x, y)
    plt.show()
