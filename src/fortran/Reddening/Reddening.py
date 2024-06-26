import numpy as np

import matplotlib.pyplot as plt
from   pylab import *

from CAF__LawOPT import caf__lawopt as caf
from CALR_LawOPT import calr_lawopt as cal
from CCMR_LawOPT import ccmr_lawopt as ccm
from CL_R_LawOPT import cl_r_lawopt as clr
from H83gaLawOPT import h83galawopt as h83
from J13__LawOPT import j13__lawopt as j13
from Leitherer02 import leitherer02 as l02
from O_Donnell94 import o_donnell94 as o94
from S79__LawOPT import s79__lawopt as s79

class attenuation(object):
    def __init__( self ):
        print("... Reddening Initiated")
        
    def q( self, l, R_V, law ):

        if law == 'caf':
            q_ = caf( l, R_V )
        if law == 'cal':
            q_ = cal( l, R_V )
        if law == 'ccm':
            q_ = ccm( l, R_V )
        if law == 'clr':
            q_ = clr( l, R_V )
        if law == 'h83':
            q_ = h83( l, R_V )
        if law == 'j13':
            q_ = j13( l, R_V )
        if law == 'l02':
            q_ = l02( l, R_V )
        if law == 'o94':    
            q_ = o94( l, R_V )
        if law == 's79':
            q_ = s79( l, R_V )

        return q_

    def extinct( self, l, f, A_V=1.0, R_V=3.1, law='ccm' ):
        # Attenuation paramaters
        self.A_V = A_V
        self.R_V = R_V
        self.law = law
        
        # SEDs
        self.l = l
        self.f = f
        self.f_ext = np.array(self.f, dtype=float) * 10.0**( -0.4 * A_V * self.q( self.l,R_V,law ) )
        
        return self.f_ext 

# def main():
#     l = np.arange(1.,250001,1.)
#     o = attenuation()

#     #print( o.q.__doc__ )
    
#     rv = 3.1

#     d = { 1: 'cal',
#           2: 'caf',
#           3: 'ccm',
#           4: 'clr',
#           5: 'h83',
#           6: 'j13',
#           7: 'l02',
#           8: 'o94' }

#     # Figure
#     ax1 = subplot2grid( (22,28), (0,0), colspan=28, rowspan=22 )

#     for i,j in d.items():
#         print(i,j)
#         q_ = o.q( l, rv, j )
#         ax1.plot( l,q_,label=j )
        

#     ax1.set_xscale('log')
#     ax1.set_yscale('log')
#     ax1.legend()

#     ax1.set_xlabel(r"Wavelength [$\mu$m]")
#     ax1.set_ylabel(r"$q_{\lambda} = A(\lambda)/A(V)$")
    
#     plt.show()

# if __name__ == "__main__":
#     main()

