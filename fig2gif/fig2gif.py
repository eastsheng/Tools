import imageio

with imageio.get_writer(uri='test.gif', mode='I', fps=12) as writer:
    for i in range(10):
        writer.append_data(imageio.imread('./Visualization/adsorption.0000'+str(i)+'.bmp'))
