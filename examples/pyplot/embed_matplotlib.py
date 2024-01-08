"""Include background images in the rendering scene
(generated by matplotlib)"""
import matplotlib.pyplot as plt
from vedo import *

tmsh = TetMesh(dataurl + "limb.vtu")
msh = tmsh.tomesh().shrink(0.8)

# Create a histogram with matplotlib
fig = plt.figure()
plt.hist(msh.celldata["chem_0"], log=True)
plt.title(r"$\mathrm{Matplotlib\ Histogram\ of\ log(chem_0)}$")

# pic1 = Image(fig).clone2d("top-right", 0.5).alpha(0.8)
pic2 = Image(dataurl + "images/embryo.jpg").clone2d("bottom-right")

show(msh, fig, pic2, __doc__, bg="lightgrey", zoom=1.2, axes=1)
