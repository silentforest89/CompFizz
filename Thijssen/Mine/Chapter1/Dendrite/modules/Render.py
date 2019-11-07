import numpy as np
import matplotlib.pyplot as plt
import os

def render_image(grid,count):

    grid_size = len(grid.grid[:,0])
    mask = (grid.grid != 0).astype(int)*1000000

    fig, ax = plt.subplots()
    ax.imshow(grid.grid+mask,cmap='gray',interpolation='hamming')

    for axis in ['top','bottom','left','right']:
      ax.spines[axis].set_linewidth(1.5)

    ax.minorticks_on()
    ax.tick_params(which='both', width=1)
    ax.tick_params(which='major', length=5)
    ax.tick_params(which='minor', length=3, color='k')

    ax.set_xlabel('X-coord',labelpad=4,fontweight='normal',
              fontsize='large')
    ax.set_ylabel('Y-coord',labelpad=4,fontweight='normal',
              fontsize='large')

    fig.suptitle('N = {}, Grid = {}x{}'.format(count,grid_size,grid_size),y=0.94,
        fontsize='x-large',fontweight='bold')

    plt.savefig('images/image{:06d}.png'.format(count),
            format='png',dpi=300,bbox_inches='tight')
    
    fig.clear()
    plt.close(fig)

def render_movie():
    """
    Maybe should replace this with a better python script or something ... I dunno.
    """
    if os.path.exists('growth.mp4'):
        os.remove('growth.mp4')

    print('\n\nRENDERING MOVIE!\n\n')

    os.system('ffmpeg -f image2 -r 48 -i images/image%06d.png -vcodec mpeg4 -y growth.mp4')

    print('\n\n')

