import os

from matplotlib import pyplot as plt

from utils.synthetic_generator.generator import SyntheticGenerator

if __name__ == '__main__':
    scenario_path = os.getcwd() + '/input.xml'
    generator = SyntheticGenerator(scenario_path, 120, 25)

    top_x1 = 966.7529628351272
    top_y1 = 1921.40443483379
    top_x2 = 996.7529628351272
    top_y2 = 1926.6005872564963
    bot_x1 = 966.7529628351272
    bot_y1 = 1926.805672095235
    bot_x2 = 996.7529628351272
    bot_y2 = 1932.0018245179413

    x, y = [], []
    y_step = 0
    x_step = 0
    step = 30
    for increment in [0, 1]:
        import time
        start_time = time.time()
        print(f'start: {time.time() - start_time}')
        curves = generator.generate(top_x1 + step * increment, top_y1,
                                    top_x2 + step * increment, top_y2,
                                    bot_x1 + step * increment, bot_y1,
                                    bot_x2 + step * increment, bot_y2)
        print(f'finish: {round(time.time() - start_time, 4)}s synthetics count: {len(curves)}')

        for curve in curves:
            for point in curve.Curve.Points:
                x.append(point.Position + x_step)
                y.append(point.Value + y_step)
            y_step += 15
            plt.plot(x, y)
            x, y = [], []

        x_step += 3000
        y_step = 0
    plt.show()
