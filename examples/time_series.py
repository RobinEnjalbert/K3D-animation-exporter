import k3d
import numpy as np
from k3d_animation_exporter import Plot

np.random.seed(2022)
x = np.random.randn(100, 3).astype(np.float32)

plt_points = k3d.points(x, color=0x528881, point_size=0.2)
plt_points.positions = {str(t): x - t / 5 * x / np.linalg.norm(x, axis=-1)[:, np.newaxis] for t in range(10)}

plot = Plot(grid_visible=False, menu_visibility=False)
plot += plt_points
plot.export_animation(filename='export.html')
