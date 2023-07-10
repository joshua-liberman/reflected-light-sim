import astropy.io.fits as fits
import glob
import os
import fnmatch

class Spectrum():
    '''
    A class for spectra manipulation (based on PSI Sim's spectrum.py class).

    The main properties will be: 
    wvs    - sampled wavelengths (np.array of floats, in microns)
    spectrum    - current flux values of the spectrum (np.array of floats, [photons/s/cm^2/A])
    R   - spectral resolution (float)

    The main functions will be: 
    load_phoenix_model      - load a PHOENIX model 
    calculate_reflected_light  -calculate the reflected light from a planet


    '''

    def __init__(self, wvs, spectrum, R):

        self.wvs = wvs
        self.spectrum = spectrum
        self.R = R

        return
    
    # def load_phoenix_model(self, )
        

    def load_phoenix_model(path=None, lambda_start, lambda_end):
        '''
        Read in a phoenix spectrum
        '''
       
        # Prompt the user to specify a path if none is given
        if path is None:
            path = input('Specify a path to your PHOENIX model (directory containing wavels + fluxes): \n')

        hdulist = fits.open(path + 'lte*.fits')
        spec = f[0].data / (1e8) # ergs/s/cm2/cm to ergs/s/cm2/Angstrom for conversion
        f.close()
        
        path = path.split('/')
        f = fits.open(path + 'WAVE_PHOENIX-ACES-AGSS-COND-2011.fits')
        lam = f[0].data # angstroms
        f.close()
        
        # Convert
        conversion_factor = 5.03*10**7 * lam #lam in angstrom here
        spec *= conversion_factor # phot/cm2/s/angstrom
        
        # Take subarray requested
        isub = np.where( (lam > wav_start*10.0) & (lam < wav_end*10.0))[0]

        # Convert 
        return lam[isub]/10.0,spec[isub] * 10 * 100**2 #nm, phot/m2/s/nm

        