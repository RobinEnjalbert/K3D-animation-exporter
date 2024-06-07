# K3D-animation-exporter

A small K3D extension to export standalone animations automatically.

## Install

``` bash
$ git clone https://github.com/RobinEnjalbert/K3D-animation-exporter.git
$ cd K3D-animation-exporter

# Option 1 (USERS): install with pip
$ pip 3 install .

# Option 2 (DEVELOPERS): install as editable
$ python3 setu_dev.py

```

## How to use

The main part of your K3D code will remain unchanged as this project only provides an extension to the `Plot` class:

``` python
import k3d
from k3d_animation_exporter import Plot

# Create 3D objects with time series
pcd = k3d.points(...)
pcd.positions = {...}

# Use the extended Plot class to export the animation
plt = Plot(grid_visible=False, menu_visibility=False)
plt += pcd
plt.export_animation(filename='export.html')
```
