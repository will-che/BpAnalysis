from data_pipline.plot import Plot

if __name__ == '__main__':
    ph = [130.95091, 116.59857, 130.64807, 130.049, 130.2319, 145.73865, 120.5867]
    rh = [117.0, 120.0, 131.0, 117.0, 111.0, 155.0, 111.0]
    pl = [70, 70, 70, 70, 70, 70, 70]
    rl = [70, 70, 70, 70, 70, 70, 70]
    Plot.plot_diff(ph, rh, pl, rl)