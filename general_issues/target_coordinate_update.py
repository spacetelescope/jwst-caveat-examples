"""
TARG_RA and TARG_DEC in FITS primary header are not at 
the epoch of the JWST exposure. This can cause the 1D 
spectral extraction aperture to be offset from the target 
location in the 2D extracted spectrum image
"""
from astropy.coordinates import SkyCoord
from astropy.io.fits import open as fits_open
from astropy.time import Time
from astropy.units import arcsec, deg, pc, yr
 
def fix_radec(path, distance=1000*pc):
    '''Fix TARG_RA and TARG_DEC in primary FITS header.'''
    with fits_open(path, 'update') as hdulist:
        header = hdulist['primary'].header
        prop_ra = header['prop_ra'] * deg
        prop_dec = header['prop_dec'] * deg
        mu_epoch = Time(header['mu_epoch'])
        mu_ra = header['mu_ra'] * arcsec / yr
        mu_dec = header['mu_dec'] * arcsec / yr
        expmid = Time(header['expmid'], format='mjd')
        apt = SkyCoord(
            prop_ra, prop_dec, distance=distance,
            pm_ra_cosdec=mu_ra, pm_dec=mu_dec, obstime=mu_epoch,
            equinox='J2000', frame='icrs')
        targ = apt.apply_space_motion(expmid)
        header['targ_ra'] = targ.ra.value
        header['targ_dec'] = targ.dec.value

    