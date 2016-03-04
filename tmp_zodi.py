import numpy as np
from scipy.interpolate import interp1d
import sys

def interpfile(the_file, norm = False, bounds_error = False):
    data = np.loadtxt(the_file)
    if norm:
        data[:,1] /= data[:,1].max()
    return interp1d(data[:,0], data[:,1], kind = 'linear', fill_value = 0., bounds_error = bounds_error)

def flamb_to_photons_per_wave(flamb, meters2, waves, dwaves):
    erg_per_cm2 = 5.03411701e21 # meters^-3
    return meters2*flamb*erg_per_cm2*(waves/1.e10) * dwaves

def get_zodi_per_filter(filt_fl, pixel_scale = 0.11):
    waves = np.arange(6000., 22000., 10.)
    dwaves = 10.

    meters2_fn = interpfile(filt_fl)
    log10zodi_fn = interpfile("input/aldering.txt")
    zodi_fn = lambda x: 10.**(log10zodi_fn(x))

    print sum(flamb_to_photons_per_wave(zodi_fn(waves), meters2_fn(waves), waves, dwaves))*pixel_scale**2.

    
if __name__ == "__main__":
    get_zodi_per_filter(sys.argv[1])
    


