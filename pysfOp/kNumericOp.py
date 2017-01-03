# -*- encoding: utf-8 -*-
from __future__ import division
"""'
english:
    PythonSf pysfOp/kNumericOp.py
    https://github.com/lobosKobayashi
    http://lobosKobayashi.github.com/
    
    Copyright 2016, Kenji Kobayashi
    All program codes in this file was designed by kVerifierLab Kenji Kobayashi

    I release souce codes in this file under the GPLv3
    with the exception of my commercial uses.

    2016y 12m 28d Kenji Kokbayashi

japanese:
    PythonSf pysfOp/kNumericOp.py
    https://github.com/lobosKobayashi
    http://lobosKobayashi.github.com/

    Copyright 2016, Kenji Kobayashi
    このファイルの全てのプログラム・コードは kVerifierLab 小林憲次が作成しました。
    
    作成者の小林本人に限っては商用利用を許すとの例外条件を追加して、
    このファイルのソースを GPLv3 で公開します。

    2016年 12月 28日 小林憲次
'"""

import sfFnctnsOp as sf
import numpy as np
pi = np.pi
arange = np.arange
#exp, sin = np.exp, np.sin
#cos, tan, sinh = np.cos, np.tan, np.sinh
#cosh, tanh = np.cosh, np.tanh
#arctan = np.arctan

def __absF(ag):
    if hasattr(ag, 'is_Atom') and ( (ag < 0) == True):
        return -ag
    else:
        return abs(ag)

absF = sf.ClAFX(__absF)  # We can't use abs(..) because it will calle __abs__(..)__.

exp, sin =sf.ClAF(np.exp), sf.sf.ClAF(np.sin)
cos, tan, sinh = sf.ClAF(np.cos),sf.ClAF(np.tan),sf.ClAF(np.sinh)
cosh, tanh, = sf.ClAF(np.cosh),sf.ClAF(np.tanh)
arctan = sf.ClAF(np.arctan)

def __log(ag):
    """' use scipy.log becuase np.log(-1) == nan
    '"""
    import scipy as sy
    return sy.log(ag)

log = sf.ClAF(__log)

def __log10(ag):
    """' use scipy.log10 becuase np.log10(-1) == nan
    '"""
    import scipy as sy
    return sy.log10(ag)

log10 = sf.ClAF(__log10)

def __sqrt(ag):
    if hasattr(ag, 'is_Atom'):
        lstGlbAt=sf.__getDctGlobals()
        ts = lstGlbAt['ts']
        return ts.sqrt(ag)
    elif (isinstance(ag, (int, float)) and ag < 0):
        return  np.sqrt(complex(ag))
    elif ( isinstance(ag, np.ndarray) ):
        # 2011.7.21 counter mesure for ag==[1,1,-1]
        # <== numpy.sqrt(-1) == NaN
        import scipy
        return scipy.sqrt(ag)
    else:
        return np.sqrt(ag)

sqrt = sf.ClAFX(__sqrt) # 2012.11.04 (sqrt^2)(4) == 4

def __arcsin(ag):
    """' use scipy.arcsin becuase arcsin(2) == nan
    '"""
    import scipy as sy
    return sy.arcsin(ag)

def __arccos(ag):
    """' use scipy.arcsin becuase arccos(2) == nan
    '"""
    import scipy as sy
    return sy.arccos(ag)

arcsin = sf.ClAF(__arcsin)
arccos = sf.ClAF(__arccos)

from numpy.fft import fftshift, ifftshift

def fft(sqAg, n=None, axis = -1):
    """' reverse Fasst Fourier Transform
         return ClTensor array
    '"""
    import numpy.fft as fp
    return sf.kryO(fp.fft(sqAg, n, axis))

def ifft(sqAg, n=None, axis = -1):
    """' reverse fft.
         return ClTensor array
    '"""
    import numpy.fft as fp
    return sf.kryO(fp.ifft(sqAg, n, axis))

def nft(sqAg, n=None, axis = -1):
    """' reverse Fasst Fourier Transform
        Cation!:sf's nft is unitary transformation
                and return ClTensor array
    '"""
    #import scipy.fftpack as fp
    import numpy.fft as fp
    #return sf.kryO(fp.fft(sqAg, n, axis)/sqrt(2))
    return sf.kryO(fp.fft(sqAg, n, axis))/sqrt(len(sqAg))

def inft(sqAg, n=None, axis = -1):
    """' reverse fft.
        Cation!:sf's ifft is unitary transformation
                and return ClTensor array
    '"""
    #import scipy.fftpack as fp
    import numpy.fft as fp
    #return sf.kryO(sqrt(2)*fp.ifft(sqAg, n, axis))
    return sf.kryO(fp.ifft(sqAg, n, axis))*sqrt(len(sqAg))

diag = lambda x,k=0:sf.kryO(np.diag(x,k))

def eig(a, b=None, left=False, right=True, overwrite_a=False
                                            , overwrite_b=False):
    import numpy.linalg as sl
    tplAt = sl.eig(a)

    return (sf.kryO(tplAt[0]), sf.kryO(tplAt[1]))

def eigvals(a):
    import numpy.linalg as sl
    return sf.krr(Osl.eigvals(a))

def eigh(a, lower='L'):
    import numpy.linalg as sl
    tplAt = sl.eigh(a, lower)
    return (sf.krr(OtplAt[0]), sf.kryO(tplAt[1]))

def eigvalsh(a, lower='L'):
    import numpy.linalg as sl
    return sf.krr(Osl.eigvalsh(a, lower))

def expm(mtAg):
    """' return kryO matrix exponential value
    '"""
    #import numpy.linalg as sl  # there is no expm in numpy.linalg
    import scipy.linalg as sl
    return sf.kryO(sl.expm(mtAg))

def logm(mtAg):
    """' return kryO matrix logarithm value
    '"""
    #import numpy.linalg as sl  # there is no logm in numpy.linalg
    import scipy.linalg as sl
    return sf.kryO(sl.logm(mtAg))

def sqrtm(mtAg):
    """' return kryO matrix square root value
    '"""
    # 11y06m22d append
    import scipy.linalg as sl
    return sf.kryO(sl.sqrtm(mtAg))



class D_(object):
    """' derivative object  of single variable function
    '"""
    def __init__(self, fnAg):
        self.m_fn = fnAg

    def __call__(self, x, dx=0.000001):
        return np.derivative(self.m_fn, x, dx=dx)

class P_(object):
    """' return partial differential function
    '"""
    def __init__(self, inPos, fnAg):
        self.m_fn = fnAg
        self.m_inPos = inPos
        assert isinstance(inPos, int)
        assert inPos >= 0

    def __call__(self, *tplAg, **kwAg):
        """' Calculate derivative value. with dx=0.000001
            If you want to change dx , you can use key word argument dx.

            ussage:
             P_(0,func)(1,2,3)  # orignal function has 3 argument
             P_(0,func)(1,2,3, dx=0.00001)
            e.g.
             x=1;y=2; P_(0,arctan2)(x,y)
             x=1;y=2; P_(1,arctan2)(x,y)
        '"""
        assert self.m_inPos < len(tplAg)

        x = tplAg[self.m_inPos]
        restBefore = tplAg[0:self.m_inPos]
        restAfter = tplAg[self.m_inPos+1:]

        def innerF(x):
            return self.m_fn(\
                *(restBefore + (x,) + restAfter) )

        import scipy as sci
        return sci.derivative(innerF, x
                                #, dx=kwAg.get('dx',0.000001) )
                                #, dx=kwAg.get('dx',0.00001) )
                                , dx=kwAg.get('dx',0.0001) )
                                #, dx=kwAg.get('dx',0.001) )
        """'
        default dx = 0.0001 is selected from below numeric experiments
        x=arcsin(1);P_(0,P_(0,sin))(x)  #('dx',0.000001) ):-0.99997787828
        x=arcsin(1);P_(0,P_(0,sin))(x)  #('dx',0.00001 ) ):-1.00000008274
        x=arcsin(1);P_(0,P_(0,sin))(x)  #('dx',0.0001  ) ):-0.999999993923
        x=arcsin(1);P_(0,P_(0,sin))(x)  #('dx',0.001   ) ):-0.999999666684
        '"""

class Pt_(object):
    """' return partial differential function for last variable
    '"""
    def __init__(self, fnAg):
        self.m_fn = fnAg

    def __call__(self, *tplAg, **kwAg):
        x = tplAg[-1]
        restX = tplAg[0:-1]

        def innerF(x, *tplAg):
            return self.m_fn( *(restX+ (x,)) )

        import scipy as sci
        return sci.derivative(innerF, x
                                , dx=kwAg.get('dx',0.0001) )


class Nl_(object):  # Nabla
    """' container of Nabla functions for N argument:dim scalar function
    '"""
    def __init__(self, fnAg, dim = None):
        """' If parmeter dim == None,then we determine the fnAg's parameter
        count from fnAg.func_code.co_argcount
        '"""
        if dim == None:
            if 'func_code' in dir(fnAg):
                dim = fnAg.func_code.co_argcount
            elif hasattr(fnAg, '__call__'):
                dim = fnAg.__call__.func_code.co_argcount - 1
            else:
                print ("Function parameter must be a built in or dll"
                      +" function. We can't draw out argument count."
                      +" You must set a count of parameters, that the"
                      +" function have, at 'dim' key word argument")
                raise AttributeError
        self.m_arP_ = np.array([P_(k,fnAg) for k in range(dim)])
        self.shape = self.m_arP_.shape
        self.m_inDim = dim

    def __call__(self, *sqAg):
        return sf.kryO([fnAt(*sqAg) for fnAt in self.m_arP_])

    """
    def __len__(self):
        return len(m_arP_)

    def __getitem__(self,ag):
        return self.m_arP_[ag]

    def __iter__(self):
        return iter(self.m_arP_)
    """

class Dv_(object):  # Divergence
    """' This function is obsolete. Use Jacobina:Jc_ alternatively.
     contaner of divegence functions for vector function array
    If you want div(..) for not sequence function then use Jc_ as below
        Jc_(f)(x,y,z).trace()
    '"""
    def __init__(self, *sqFnAg):
        if isinstance(sqFnAg[0], Nl_):
            sqFnAg = sqFnAg[0].m_arP_
        elif ( isinstance(sqFnAg[0], tuple) or isinstance(sqFnAg[0], list)
            or isinstance( sqFnAg[0], type( np.array([1.0, 2]) ) )  ):
            sqFnAg = sqFnAg[0]

        self.m_arP_ = np.array([P_(k, sqFnAg[k]) for k in range(len(sqFnAg))])

    def __call__(self, *sqAg):
        return sum([fnAt(*sqAg) for fnAt in self.m_arP_])

# You must fix using krry(dictionary)
#class Jc_(object):
#    """' class to calculate Jacobian
#    '"""
#    def __init__(self, fnAg, inDim = None, outDim = None):
#        #import pdb; pdb.set_trace()
#        if ( inDim==None
#         and isinstance(fnAg,sf.ClFldTns)
#         and issubclass(fnAg.m_type, sf.ClAF)
#        ):
#            # Jc_([`X+`Y, `X `Y]) --> inDim==2
#            # because sqare matrix is used in many cases.
#            inDim = fnAg.m_tnsr.shape[0]
#
#        if isinstance(fnAg,(tuple, list, dict, sc.ndarray, sf.ClFldTns) ):
#            fnAg = sf.ClTensor(fnAg,dtype=object)
#
#        if inDim == None:
#            def getElm(sqAg):
#                if hasattr(sqAg, '__len__'):
#                    return getElm(sqAg[0])
#                else:
#                    return sqAg
#
#            fnAt = getElm(fnAg)
#            if hasattr(fnAt, 'm_inDim'):
#                # fnAg may be Nl_/Jc_ instance
#                inDim = fnAt.m_inDim
#            elif hasattr(fnAt, 'func_code'):
#                inDim = fnAt.func_code.co_argcount
#            elif hasattr(fnAt, '__call__'):
#                inDim = fnAt.__call__.func_code.co_argcount -1
#                assert inDim >= 1
#            else:
#                print ("At sf.Jc_.__int,"
#                      +" function parameter must be a built in or dll"
#                      +" function. We can't draw out argument count."
#                      +" You must set a count of parameters, that the"
#                      +" function have, at 'inDim' key word argument")
#                raise AttributeError
#
#
#        if outDim == None:
#            if isinstance(fnAg, sf.ClTensor):
#                outDim = fnAg.shape
#            else:
#                # use (1/3,)*inDim input parameter to avoid 0 division error
#                tplArgAt = (1/3,)*inDim
#                valAt = fnAg(*tplArgAt)
#                if isinstance(valAt, sc.ndarray):
#                    outDim = valAt.shape
#                elif hasattr(valAt, '__len__'):
#                    outDim = len(fnAg(*tplArgAt))
#                else:
#                    outDim =(1,)
#
#        if not hasattr(outDim, '__len__'):
#            outDim = (outDim,)
#
#
#
#        dctAt = {}
#
#        if isinstance(fnAg, sf.ClTensor):
#            for idx in sf.mrng(*outDim):
#                if isinstance(idx, int):
#                    idx = (idx,)
#
#                for k in range(inDim):
#                    dctAt[idx+(k,)] = P_(k, fnAg[idx])
#        else:
#            def makeFnSq(idxAg):
#                def innerF(*ag):
#                    return fnAg(*ag)[idxAg]
#
#                return innerF
#
#            for idx in sf.mrng(*outDim):
#                if isinstance(idx, int):
#                    idx = (idx,)
#                for k in range(inDim):
#                    #import pdb; pdb.set_trace()
#                    #the below code changes last but one P_(..) to 0 function
#                    #I can't understand the reason. But closure works well.
#                    #dctAt[idx+(k,)] = P_(k, makeFnSq(idx))
#                    if outDim == (1,):
#                        dctAt[k] = P_(k, fnAg)
#                    else:
#                        dctAt[idx+(k,)] = P_(k, makeFnSq(idx))
#
#        self.m_mtP_ = sf.ClTensor(dctAt, dtype=object)
#        self.shape = self.m_mtP_.shape
#        self.m_inDim = inDim
#
#    def __call__(self, *sqAg):
#        #import pdb; pdb.set_trace()
#        dctAt = {}
#        for idx in sf.mrng(*self.m_mtP_.shape):
#            dctAt[idx] = self.m_mtP_[idx](*sqAg)
#
#        elmAt = dctAt[idx]
#        if isinstance(elmAt, sf.ClTensor):
#            dctDctAt = {}
#            for idx in sf.mrng(*self.m_mtP_.shape):
#                for iidx in sf.mrng(*elmAt.shape):
#                    if isinstance(iidx,int):
#                        if isinstance(idx,int):
#                            # e.g. Jc_(λ x:~[x])
#                            dctDctAt[(idx,) +(iidx,)] = dctAt[idx][iidx]
#                        else:
#                            dctDctAt[idx +(iidx,)] = dctAt[idx][iidx]
#                    else:
#                        if isinstance(idx,int):
#                            dctDctAt[(idx,) +iidx] = dctAt[idx][iidx]
#                        else:
#                            dctDctAt[idx +iidx] = dctAt[idx][iidx]
#
#            return sf.kryO(dctDctAt)
#        else:
#            return sf.kryO(dctAt)



def quadAn(fAn, sqPath):
    """' line integral on complex plane and analytical function
    fAn :complex analytical function
    sqPath:sequence of integrating path with which elments are complex nummber
    return: tuple of ( integrated complex an real accuracy, an image accuracy)

    e.g.
    quadAn(lambda z: 1, [0+1j, 1+1j])
    ===============================
    ((1+0j), 1.1102230246251565e-014, 0.0)
             read accuracy            image accuracy

    quadAn(lambda z: z**2, [0+1j, 1+1j, 1, 0, 0+1j])
    ===============================
    (0j, 2.2204460492503131e-014, 2.2204460492503131e-014)


    You must be carefull for beeing that analitical functions may be multiple
    value functions

    quadAn(log, [1+`i,1-`i, -1-`i,-1+`i,1+`i])
    ===============================
    (6.2831853071795862j, 3.23830369214736e-09, 3.2383033509434062e-09)
    '"""
    sf.sy_()

    #  ret arg
    def re_re_fAn(reX):
        reY = imA + (imB-imA)*(reX-reA)/(reB-reA)
        return complex(fAn(reX + reY*1j)).real

    def im_re_fAn(reX):
        imY = imA + (imB-imA)*(reX-reA)/(reB-reA)
        return complex(fAn(reX + imY*1j)).imag

    def im_im_fAn(imY):
        reX = reA + (reB-reA)*(imY-imA)/(imB-imA)
        return complex(fAn(reX + imY*1j)).imag

    def re_im_fAn(imY):
        reX = reA + (reB-reA)*(imY-imA)/(imB-imA)
        return complex(fAn(reX + imY*1j)).real

    re, im, reError, imError = 0,0,0,0
    for i in range(len(sqPath)-1):
        a = complex(sqPath[i])
        b = complex(sqPath[i+1])
        reA = a.real
        reB = b.real
        imA = a.imag
        imB = b.imag

        if (reA != reB):
            re += sf.si_().quad(re_re_fAn, reA,reB)[0]
            reError += sf.si_().quad(re_re_fAn, reA,reB)[1]
            im += sf.si_().quad(im_re_fAn, reA,reB)[0]
            imError += sf.si_().quad(im_re_fAn, reA,reB)[1]
        if (imA != imB):
            re -= sf.si_().quad(im_im_fAn, imA,imB)[0]
            reError += sf.si_().quad(im_im_fAn, imA,imB)[1]
            im += sf.si_().quad(re_im_fAn, imA,imB)[0]
            imError += sf.si_().quad(re_im_fAn, imA,imB)[1]

    return re + im*1.0j, reError, imError
"""' test
print quadAn(lambda z: 1, [0+1j, 1+1j]) #((1+0j), 1.1102230246251565e-014, 0.0)
print quadAn(lambda z: 1, [1+1j, 1+0j]) #(-1j, 0.0, 1.1102230246251565e-014)
print quadAn(lambda z: 1, [1+0j, 0+0j]) #((-1+0j), 1.1102230246251565e-014, 0.0)
print quadAn(lambda z: 1, [0+0j, 0+1j]) #(1j, 0.0, 1.1102230246251565e-014)
print quadAn(lambda z: z**2, [0+1j, 1+1j, 1, 0, 0+1j]) #(0j, 2.2204460492503131e-014, 2.2204460492503131e-014)
'"""

def quadR(*sqAg, **dctAg):
    """' quadR and qdrt are very same. use quadR(..). qdrt(..) is obsolete.
    integrate by scipy.integrate.quad ignoreing tolerance
    e.g
    quadR(cos, 0,pi)
    ===============================
    4.92255263497e-17

    '"""
    #sf.sy_()
    return sf.si_().quad(*sqAg, **dctAg)[0]

def nearlyEq(lftAg, rhtAg, tolerance=1e-6):
    """' Obsolete! We alterntively use numpy.allclose.
        compare with small tolerance to test float/complex values which may
    contain a tolerance. In many cases, if the first 6 digits of two terms
    are same, then we can see them as same. In that cases, nearlyEq(..)
    function is usefull.

    Subtrac:'lftAg - rhtAg' must have a value

    If lftAg is tuple or list or dict, we convert it to a ClTensor instance and
    enabel to subtract.

    usage:
        nearlyEq(3, 3.0000000001)               # return True
        nearlyEq(3, 3.01)                       # return False
        nearlyEq(~[3,4], [3.0000000001, 4])     # return True
        nearlyEq( [3,4], [3.0000000001, 4])     # return True
        nearlyEq( [3,4], [3.01        , 4])     # return False

        nearlyEq([3,3.00000001], 3) # True, ~[,3.00000001] - 3 has a value

    '"""
    if isinstance(lftAg,(tuple,list,dict)):
        lftAg = sf.kryO(lftAg)

    return norm(lftAg-rhtAg) <= max(norm(lftAg), norm(rhtAg))*tolerance

def nearlyIn(elmAg, sqAg, tolerance=1e-6):
    """' Chdek elmAg is in sqAg allowing tollerence
    e.g.
        nearlyIn(3, [1, 5, 3.000000001])
        ===============================
        True

        nearlyIn(3, [1, 5, 3.000001])
        ===============================
        True

        nearlyIn(3, [1, 5, 3.00001])
        ===============================
        False
    '"""

    for elmAt in sqAg:
        if nearlyEq(elmAg, elmAt, tolerance):
            return True

    return False

def normalize(vct, type=float):
    """' return a ClTensor which absolute length is 1

    normalize([1,2,3])
    ===============================
    [ 0.26726124  0.53452248  0.80178373]
    ---- ClTensor ----

    normalize(`σx)
    ===============================
    [[ 0.          0.70710678]
     [ 0.70710678  0.        ]]
    ---- ClTensor ----

    normalize(`εL)
    ===============================
    [[[ 0.          0.          0.        ]
      [ 0.          0.          0.40824829]
      [ 0.         -0.40824829  0.        ]]

     [[ 0.          0.         -0.40824829]
      [ 0.          0.          0.        ]
      [ 0.40824829  0.          0.        ]]

     [[ 0.          0.40824829  0.        ]
      [-0.40824829  0.          0.        ]
      [ 0.          0.          0.        ]]]
    ---- ClTensor ----

    norm(normalize(`εL))
    ===============================
    1.0

    '"""
    #arAt = sc.array(vct, type)
    arAt = sf.kryO(vct, type)
    arAt /= norm(arAt)
    return arAt

def __norm(*sqAg):
    """' Calculate a norm of the sequence argment, Usually the results are same
    for scipy.linalg.norm(.). We are sure to return float value, not integer

        But we calculate a norm as far as possible. Althour elments of the
    sequence are not int, float, or complex. If they have a method of __abs__
    or  __int__ then we calculate norm.

        We don't calculate norm of dict
      e.g.
        norm( 1, 1, 0, 0, 1, 1 ) #--> 2.0
        norm([1, 1, 0, 0, 1, 1]) #--> 2.0
        norm((1, 1, 0, 0, 1, 1)) #--> 2.0
        norm(`1,`1,`0,`0,`1,`1 ) #--> 2.0

        norm([1,[2,3]])             #--> 3.74165738677   not aligned sequence
        norm(oc.ClOctonion(1,2,3))  #--> 3.74165738677   __abs__
        norm({1,2,3})               #--> 3.74165738677   set
        dctMt={};dctMt[0,0]=1;dctMt[1,0]=2;norm(dctMt) #--> 2.2360679775:values

        norm(dict([(0, 1.2),(1, 5)]))
        ===============================
        5.14198405287

        norm(`σx)
        ===============================
        1.41421356237

        norm(`εL)
        ===============================
        2.44948974278
        norm(set([1,2,3]))
        ===============================
        3.74165738677
    '"""
    if len(sqAg) == 1:
        elm = sqAg[0]
        if ( not hasattr(elm, '__iter__') and not hasattr(elm, '__len__')
         and not hasattr(elm, '__getitem__') ):
            if hasattr(elm, '__abs__'):
                return float(abs(elm))     # don't return integer
            elif hasattr(elm, '__float__'):
                valAt = float(elm)
                return (valAt * valAt)**0.5
            elif hasattr(elm, '__int__'):
                valAt = int(elm)
                #return float(sqrt(valAt * valAt))
                return (valAt * valAt)**0.5
            else:
                raise sf.ClAppError("At sf.norm(..), we can't get calculate"
                               + " abs()/float()/int() for " + str(elm) )
        elif not hasattr(elm, '__iter__') and hasattr(elm, '__getitem__'):
            try:
                sqAg = elm[:]
            except IndexError:
                # numpy.int32 has __getitem__ 
                # but index operation causes Index Error
                pass
        else:
            sqAg = elm

    if isinstance( sqAg, np.ndarray) and sqAg.shape==():
        sqAg = np.ravel(sqAg)
        #return sl.norm(sqAg)
        #raise sf.ClAppError("At sf.norm(..), we detect 0 dimentional array"
        #                   + " that are not supported." )

    elif isinstance(sqAg, dict):
        sqAg = sqAg.values()


    flRtn = 0
    for elm in sqAg:
        """
        #Can't use this for norm(~[1,2])
        elm = norm(*elm)
        """
        if isinstance(elm, (bool, int,long,float)):
            pass
        elif hasattr(elm, '__len__'):
            elm = norm(*elm)
        elif hasattr(elm, '__iter__'):
            elm = norm(*tuple(elm) )
        elif hasattr(elm, '__abs__'):
            elm = abs(elm)
        elif hasattr(elm, '__float__'):
            elm = float(elm)
        elif hasattr(elm, '__int__'):
            elm = int(elm)
        else:
            raise sf.ClAppError("At sf.norm(..), we can't get scalar value "
                           + "for elment:" + str(elm) )

        flRtn += elm * elm

    # **0.5 return float. sqrt return integer depending on the situations
    # <== at sympy Rat **0.5 reutrns <class 'sympy.core.numbers.Real'>
    return float(flRtn**0.5)

# norm(oc.Pl(1,2,3)) が scalar を返さねばならない。
#     ClAfNorm を作らないと、上の式が関数合成になる
# 「normAF is an Arithmitic Function of norm」 を追加して設ける
# normF(..) を使わせることで、危なっかしい計算を始めている注意信号の意味も
# 持たせられる
norm = sf.ClAfNorm(__norm)
#norm =            (__norm)
#norm = sf.ClAF(__norm)


def normSq(*sqAg):
    """' return square:**2 of vector length
    e.g.
        nearlyEq(normSq([1,2,3]), 14)
        ===============================
        True
        nearlyEq(normSq(dict([(0, 1.2),(1, 5)])), 26.44)
        ===============================
        True
        nearlyEq(normSq(`σx), 2)
        ===============================
        True
        nearlyEq(normSq(`εL), 6)
        ===============================
        True
        normSq([2^30]) == 2^60
        ===============================
        True
        normSq([2^1000]) == 2^2000
        ===============================
        True
    '"""
    #return norm(*sqAg)**2
    if len(sqAg) == 1:
        elm = sqAg[0]
        if ( not hasattr(elm, '__iter__') and not hasattr(elm, '__len__')
         and not hasattr(elm, '__getitem__') ):
            if hasattr(elm, '__abs__'):
                return float(abs(elm))     # don't return integer
            elif hasattr(elm, '__float__'):
                valAt = float(elm)
                return (valAt * valAt)**0.5
            elif hasattr(elm, '__int__'):
                valAt = int(elm)
                #return float(sqrt(valAt * valAt))
                return (valAt * valAt)**0.5
            else:
                raise sf.ClAppError("At sf.norm(..), we can't get calculate"
                               + " abs()/float()/int() for " + str(elm) )
        elif not hasattr(elm, '__iter__') and hasattr(elm, '__getitem__'):
            try:
                sqAg = elm[:]
            except IndexError:
                # numpy.int32 has __getitem__ 
                # but index operation causes Index Error
                pass

        else:
            sqAg = elm

    if isinstance( sqAg, np.ndarray) and sqAg.shape==():
        sqAg = np.ravel(sqAg)
        #return sl.norm(sqAg)
        #raise sf.ClAppError("At sf.norm(..), we detect 0 dimentional array"
        #                   + " that are not supported." )

    elif isinstance(sqAg, dict):
        sqAg = sqAg.values()


    flRtn = 0
    for elm in sqAg:
        """
        #Can't use this for norm(~[1,2])
        elm = norm(*elm)
        """
        if isinstance(elm, (bool, int,long,float)):
            pass
        elif hasattr(elm, '__len__'):
            elm = norm(*elm)
        elif hasattr(elm, '__iter__'):
            elm = norm(*tuple(elm) )
        elif hasattr(elm, '__abs__'):
            elm = abs(elm)
        elif hasattr(elm, '__float__'):
            elm = float(elm)
        elif hasattr(elm, '__int__'):
            elm = int(elm)
        else:
            raise sf.ClAppError("At sf.norm(..), we can't get scalar value "
                           + "for elment:" + str(elm) )

        flRtn += elm * elm

    # **0.5 return float. sqrt return integer depending on the situations
    # <== at sympy Rat **0.5 reutrns <class 'sympy.core.numbers.Real'>
    return flRtn

def quadGN(fN, sqXN):
    """' line integral of N dimensional vector function  along with N
    dimentioanl path using Gaussiann quadrature untill 50 points.

    fAn :N dimentioanal vector function
    sqPath:sequence of integrating path which elments are N dimentional vector

    e.g.
    vctE = λ vctP:vctP/norm(vctP);quadGN(vctE, ([1,1,1],[1,2,3]) )
    ===============================
    (2.0096065781679306, 7.8044882778627311e-009)

    vctE = λ vctP:vctP/norm(vctP);quadGN(vctE, ([1,1,0],[1,-1,0],[-1,-1,0],[-1,1,0],[1,1,0]) )
    ===============================
    (0.0, 0.0)

    '"""
    #sf.sy_()
    N = len(sqXN[0])

    flIntegrated = 0.0
    flError = 0.0

    for i in range(len(sqXN)-1):
        def elmntF(x, n, arA, arB):
            lenAt = len(x)
            if isinstance(x[0], complex):
                rtnAr=np.zeros(lenAt, complex)
            else:
                rtnAr=np.zeros(lenAt, float)

            for i in range(len(x)):
                xx = x[i]
                rtnAr[i] = fN( arA + (arB-arA)*(xx-arA[n])/(arB[n]-arA[n]) )[n]

            return rtnAr

        arA = np.array(sqXN[i])
        arB = np.array(sqXN[i+1])
        for k in range(N):
            if ( arA[k] != arB[k]):
                tplAt = sf.si_().quadrature(elmntF, arA[k], arB[k], args = (k,arA,arB) )
                flIntegrated += tplAt[0]
                flError += tplAt[1]

    return flIntegrated, flError

def quadN(fN, sqXN):
    """' line integral of inner product which caculated from N dimensional
    vector function  and N dimentioanl integrating path using scipy.quad(..)

    fAn :N dimentioanal vector function
    sqPath:sequence of integrating path which elments are N dimentional vector
    return: integrated float number

    e.g.
    vctE = λ vctP:vctP/norm(vctP);quadN(vctE, ([1,1,1],[1,2,3]) )
    ===============================
    (2.0096065792050641, 2.2311114946716608e-014)

    vctE = λ vctP:vctP/norm(vctP);quadN(vctE, ([1,1,0],[1,-1,0],[-1,-1,0],[-1,1,0],[1,1,0]) )
    ===============================
    (2.8130846960094083e-017, 3.6623805685846749e-014)
    '"""
    #sf.sy_()
    N = len(sqXN[0])

    flIntegrated = 0.0
    flError = 0.0

    for i in range(len(sqXN)-1):# sqXN[i], sqXN[i+1] の両方を扱いたいので range(..) を使う
        def elmntF(x, n, arA, arB):
            return fN( arA + (arB-arA)*(x-arA[n])/(arB[n]-arA[n]) )[n]

        arA = np.array(sqXN[i])
        arB = np.array(sqXN[i+1])
        for k in range(N):
            if ( arA[k] != arB[k]):
                tplAt = sf.si_().quad(
                                elmntF, arA[k], arB[k], args = (k,arA,arB) )
                flIntegrated += tplAt[0]
                flError += tplAt[1]

    return flIntegrated, flError

def quadVctN(fN, sqXN, usrAg=None, bl3arg=False, bl_fixed_quad = False, inOrder=5):
    """' line integral of N dimensional vector function  along with N dimentioanl path
         fAn :N dimentioanal vector function
         sqPath:sequence of integrating path which elments are N dimentional vector
         bl3arg: True:  fN(x, vctA, vctB, ...)
                 False: fn(vct, ... )
         bl_fiexed_quad: True: use fixed_quad to improve calculating time
                         False: use quad for aculate calculation results.
            inOrder: oder argument for fixed_quad
         return: integrated vactor
    '"""
    def elmntF(x, n, arA, vctNormalizedAg, usrAg):
        if usrAg == None:
            return fN( arA + x*vctNormalizedAg )[n]
        else:
            return fN( arA + x*vctNormalizedAg, *usrAg )[n]

    def elmnt3argF(x, n, arA, arB, usrAg):
        if usrAg == None:
            return fN(x, arA, arB)[n]
        else:
            return fN(x, arA, arB, *usrAg)[n]

    def elmnt3argFixed(x, n, arA, arB, usrAg):
        # x must be array
        if usrAg == None:
            return [fN(xx, arA, arB)[n] for xx in x]
        else:
            return [fN(xx, arA, arB, *usrAg)[n] for xx in x]


    N = len(sqXN[0])

    flIntegrated = np.zeros(N)
    flError = np.zeros(N)

    for i in range(len(sqXN)-1):
        arA = np.array(sqXN[i])
        arB = np.array(sqXN[i+1])
        for k in range(N):
            vctNormalizedAt = normalize(arB-arA)
            if (bl_fixed_quad == True):
                if bl3arg == False:
                    # 後回し
                    tplAt = sf.si_().quad(elmntF, 0, norm(arB - arA)
                                  , args = (k, arA, vctNormalizedAt, usrAg) )
                else:
                    tplAt = sf.si_().fixed_quad(
                                          elmnt3argFixed, 0, norm(arB - arA)
                                        , args = (k,arA,arB, usrAg), n=inOrder )
                flError[k] = 0
            else:
                if bl3arg == False:
                    tplAt = sf.si_().quad(elmntF, 0, norm(arB - arA)
                                  , args = (k, arA, vctNormalizedAt, usrAg) )
                else:
                    tplAt = sf.si_().quad(elmnt3argF, 0, norm(arB - arA)
                    , args = (k,arA,arB, usrAg) )
                flError[k] += tplAt[1]
            flIntegrated[k] += tplAt[0]

    return flIntegrated, flError

# 07.11.10 test complex ODE
#from scipy.integrate import odeint
def cplx2real(vct):
    """ convert complex or compolex array to real pair(s)"""
    if isinstance(vct, int) or isinstance(vct, float):
        return sf.kryO(vct, 0)
    elif vct is complex:
        return sf.kryO(vct.real, vct.imag)
    else:
        vctAt = np.zeros(2*len(vct))
        for i in range(len(vct)):
            valAt = vct[i]
            if isinstance(valAt, int) or isinstance(valAt, float):
                vctAt[2*i]=valAt
                vctAt[2*i+1]=0.0
            elif isinstance(valAt, complex) or isinstance(valAt[0], complex):
                vctAt[2*i]=valAt.real
                vctAt[2*i+1]=valAt.imag
            else:
                vctAt[2*i]=valAt
                vctAt[2*i+1]=0.0
        return vctAt

def real2cplx(vct):
    """ convert real pair(s) to complex or compolex array """
    if isinstance(vct,int) or isinstance(vct, float):
        return vct+0j

    vctAt = np.zeros(len(vct)/2, complex)
    for i in range(len(vctAt)):
        vctAt[i]=vct[2*i]+1j*vct[2*i+1]
    return vctAt

class __ClInterim:
    def __init__(self, fnAg, args=()):
        self.m_fn = fnAg
        self.m_ag = args

    def __call__(self,y,t):
        if self.m_ag == ():
            rtAt = self.m_fn(real2cplx(y), t)
        else:
            rtAt = self.m_fn(real2cplx(y), t, self.m_ag)
        return cplx2real(rtAt)

def cOdeInt(fncAg, y0, t, args=() ):
    """ extended from scipy.integrate.odeint to complex odeint
    usage:
    import sf
    #mtBA = sc.zeros(2,2, complex)
    mtBA=-1j
    def func(psi,t):
        return mtBA* psi

    N = 30
    #y = sf.si_().odeint( func, [1+0j,0+0j], sf.arSqnc(0,N,5.0/N) )
    y = sf.codeint( func, 1, sf.arSqnc(0,N,5.0/N) )

    or
    import sf
    mtBA = sf.sc.zeros(2,2, complex)
    mtBA[0,0]=-1+0j
    def func(psi,t):
        return sc.dot(mtBA, psi)

    N = 30
    #y = sf.si.odeint( func, [1+0j,0+0j], sf.arSqnc(0,N,5.0/N) )
    #y = sf.codeint( func, [1, 0+0j], sf.arSqnc(0,N,5.0/N) )
    #y = sf.codeint( func, [1, 0], sf.arSqnc(0,N,5.0/N) )
    y = sf.codeint( func, [1+0j, 0], sf.arSqnc(0,N,5.0/N) )
    """
    #sf.sy_()
    clAt = __ClInterim(fncAg, args)
    y0At = cplx2real(y0)
    rtAt = sf.si_().odeint(clAt, y0At, t, args)
    cplxRtAt = np.zeros([len(rtAt), len(rtAt[0])/2], complex)
    for i,val in  enumerate(rtAt):
        cplxRtAt[i] = real2cplx(val)
    return cplxRtAt

def solvePDE(dctBoundary, fncRecurring, inIteration=64, dfltValue = 0
        , blInterpolation = True, arRslt=None):
    """'solve partial differential equation by user defined recurring function.

        dctBoudary argument: dictionary
            dctBoudary[i,j, .. , k] = True or False or Initial value
                True: call fncRecurring function which will be called for user
                      with dctRslt and index argument
                False:dctRslt[i,j, .. ,k] == dfltValue, not calculating area

        fncRecurring: function defined by user
            argument fncRecurring(dctRslt, index)

        inIteration: number of iteration times
        dfltValue: defualt value at dctBoundary[index] == True or False
        blInterpolation: True: enable linear interpolation at mesh edge
        arRslt: Use user defined mesh matrix/tensor
        return: matrix or tensor dictionary with float value
    '"""
    #dctBoundary = copy.deepcopy(dctBoundary)    # we change dctBoundary free mesh to None

    # estimate index
    if isinstance(dctBoundary, dict):
        lstAt = dctBoundary.keys()
        #lstAt.sort()
        #shapeAt = list(lstAt[-1])
        shapeAt = list(max(lstAt))

        for i in range(len(shapeAt)):
            shapeAt[i] += 1
        assert reduce(int.__mul__, shapeAt) == len(lstAt),\
            "dictionary dctBoundary index is not alined" + str(shapeAt)
    elif isinstance(dctBoundary, np.ndarray):
        shapeAt = dctBoundary.shape
    else:
        assert False, "dctBoundary argument is not dictionary:"+str(dctBoundary)

    #initialize dctRslt
    if arRslt == None:
        dctRslt = {}
    else:
        dctRslt = arRslt

    if ( isinstance(dfltValue,int) ):
        dfltValue = float(dfltValue)

    # set default value and initial value
    for index in sf.mrng(*shapeAt):
        if ( ( dctBoundary[index] is True)
          or ( dctBoundary[index] is False)
          or isinstance(dctBoundary[index], str) ):
            if ( isinstance(dfltValue,float)
              or isinstance(dfltValue,complex) ):
                dctRslt[index] = dfltValue
            else:
                dctRslt[index] = copy.deepcopy(dfltValue)
        else:
            dctRslt[index] = sf.copy.deepcopy(dctBoundary[index])

    # make interpolation dictionary for free edge
    dctInterpolateAt = {}
    lenAt = len(shapeAt)
    if blInterpolation == True:
        for index in sf.mrng(*shapeAt):
            if not(dctBoundary[index] is True):
                continue
            lstIndex1 = [0,]*lenAt
            lstIndex2 = [0,]*lenAt
            blSentinel = False
            for i in range(lenAt):
                if index[i] == 0:
                    lstIndex1[i]=1
                    lstIndex2[i]=2
                    blSentinel = True
                elif index[i] == shapeAt[i]-1:
                    lstIndex1[i]=shapeAt[i]-2
                    lstIndex2[i]=shapeAt[i]-3
                    blSentinel = True
                else:
                    lstIndex1[i]=index[i]
                    lstIndex2[i]=index[i]

            if ( blSentinel == True):
                dctBoundary[index] = None
                dctInterpolateAt[index] = ( tuple(lstIndex1),tuple(lstIndex2) )

    # calculate
    lstAt = [ 1, 3] # to debug
    for i in range(inIteration):
        for index in sf.mrng(*shapeAt):
            """'
            print "index:",index
            if index == tuple(lstAt):                          # to debug
                #lstAt2= [dctRslt[n,17] for n in range(30)]# to debug
                import pdb; pdb.set_trace()
                #print lstAt2

            '"""
            if ( dctBoundary[index] is True) or isinstance(dctBoundary[index],str):
                fncRecurring(dctRslt, index)
            elif ( dctBoundary[index] is None ):
                sqAt = dctInterpolateAt[index]
                dctRslt[index] = 2*dctRslt[ sqAt[0] ] - dctRslt[ sqAt[1] ]
            else:
                continue
    return dctRslt


def solveLaplacian(dctBoundary, inIteration=64):
    """'solve partial differential equation

        dctBoudary argument: dictionary
            dctBoudary[i,j, .. , k] = True or False or Character
                True: calculate recurrence formula for Laplacian with dctRslt
                False:dctRslt[i,j, .. ,k] == 0, not calculating area
                Character: user extension <== don't use fo solveLaplacian
        inIteration argemnt: number of iteration times

        return: tensor dictionary with float value
    '"""
    def itrF(index):
        for j in range( len(index) ):
            for k in sf.arSqnc(-1,2,2):
                indexAt = list(index)
                indexAt[j] = indexAt[j]+k
                yield tuple(indexAt)

    def fncPDE(dctRslt, index):
        dctRslt[index] = 1.0/(2*len(index))*sum(
                            [dctRslt[indexAt] for indexAt in itrF(index)]
                         )
    return solvePDE(dctBoundary, fncPDE, inIteration)

def itrSlvPDE(dctBoundary, inIteration=64, dfltValue = 0
        , blInterpolation = True, arRslt=None):
    """'generatro function iterating for solving partial differential equation:

        dctBoudary argument: dictionary
            dctBoudary[i,j, .. , k] = True or False or Initial value
                True: yield with dctRslt and index argument
                False:dctRslt[i,j, .. ,k] == dfltValue, not calculating area
        inIteration: number of iteration times
        dfltValue: defualt value at dctBoundary[index] == True or False
        blInterpolation: True: enable linear interpolation at mesh edge
        arRslt: Use user defined mesh matrix/tensor

        yield dctRslt, index, boundaryValue
    '"""
    #dctBoundary = copy.deepcopy(dctBoundary)    # we change dctBoundary free mesh to None

    # estimate index
    if isinstance(dctBoundary, dict):
        lstAt = dctBoundary.keys()
        #lstAt.sort()
        #shapeAt = list(lstAt[-1])
        shapeAt = list(max(lstAt))

        for i in range(len(shapeAt)):
            shapeAt[i] += 1
        assert reduce(int.__mul__, shapeAt) == len(lstAt),("dictionary "
                                + "dctBoundary index is not alined. Shape:"
                                + str(shapeAt) + "  len:"+str(len(lstAt)) )

    elif isinstance(dctBoundary, np.ndarray):
        shapeAt = dctBoundary.shape
    else:
        assert False, ("dctBoundary argument is not dictionary:"
                       +str(dctBoundary))

    #initialize dctRslt
    if arRslt == None:
        dctRslt = {}
    else:
        dctRslt = arRslt

    # set default value and initial value
    for index in sf.mrng(*shapeAt):
        if ( ( dctBoundary[index] is True)
          or ( dctBoundary[index] is False)
          or isinstance(dctBoundary[index], str) ):
            if ( isinstance(dfltValue,float)
              or isinstance(dfltValue,complex) ):
                dctRslt[index] = dfltValue
            else:
                dctRslt[index] = sf.copy.deepcopy(dfltValue)
        else:
            dctRslt[index] = sf.copy.deepcopy(dctBoundary[index])

    # make interpolation dictionary for free edge
    dctInterpolateAt = {}
    lenAt = len(shapeAt)
    if blInterpolation == True:
        for index in sf.mrng(*shapeAt):
            if not(dctBoundary[index] is True):
                continue
            lstIndex1 = [0,]*lenAt
            lstIndex2 = [0,]*lenAt
            blSentinel = False
            for i in range(lenAt):
                if index[i] == 0:
                    lstIndex1[i]=1
                    lstIndex2[i]=2
                    blSentinel = True
                elif index[i] == shapeAt[i]-1:
                    lstIndex1[i]=shapeAt[i]-2
                    lstIndex2[i]=shapeAt[i]-3
                    blSentinel = True
                else:
                    lstIndex1[i]=index[i]
                    lstIndex2[i]=index[i]

            if ( blSentinel == True):
                dctBoundary[index] = None
                dctInterpolateAt[index] = ( tuple(lstIndex1),tuple(lstIndex2) )

    # calculate
    lstDbg = [ 0, 3, 3] # to debug
    for i in range(inIteration):
        for index in sf.mrng(*shapeAt):
            """'
            print "index:",index
            if index == tuple(lstDbg):                          # to debug
                #lstAt2= [dctRslt[n,17] for n in range(30)]# to debug
                import pdb; pdb.set_trace()
                #print lstAt2

            '"""
            if ( dctBoundary[index] is True) or isinstance(dctBoundary[index], str):
                yield (dctRslt, index)
            elif (blInterpolation == True) and ( dctBoundary[index] is None ):
                sqAt = dctInterpolateAt[index]
                dctRslt[index] = 2*dctRslt[ sqAt[0] ] - dctRslt[ sqAt[1] ]
            else:
                continue


def dct2(sqAg):
    """' Type2 Discrete Cosine Transformation for sequence argment
        return kryO vector with same norm size for argment sequence.
    e.g.
    dct2([0.7, 0.6, 0.95, 0.85,  0.55, 0.1, 0.68, 0.43])
    ===============================
    [ 1.71826948  0.36452813 -0.08071514 -0.38011727  0.07071068  0.32186722
     -0.15790841  0.2548168 ]
    ---- ClTensor ----

    dct2(range(32))
    ===============================
    [  8.76812409e+01  -5.18555951e+01  -2.04281037e-14  -5.74305749e+00
      -5.32907052e-15  -2.05378057e+00   0.00000000e+00  -1.03699056e+00
      -1.15463195e-14  -6.18143249e-01   8.88178420e-16  -4.05658019e-01
       2.13162821e-14  -2.82932996e-01  -9.76996262e-15  -2.05367296e-01
       8.43769499e-14  -1.52902657e-01   3.64153152e-14  -1.15420131e-01
       1.42108547e-14  -8.73494434e-02  -4.39648318e-14  -6.53996651e-02
       1.02140518e-14  -4.75025193e-02  -3.28626015e-14  -3.22782075e-02
      -6.43929354e-15  -1.87448835e-02  -8.65973959e-15  -6.14826207e-03]
    ---- ClTensor ----

    '"""
    """'
    Too slow for 1000 length sequece data!

    ret=[0]*len(sqAg)
    a=2*len(sqAg)
    d=sqrt(2.0 / len(sqAg))
    for k in range(len(sqAg)):
        b=k*pi
        ret[k]=0.0
        for n in range(len(sqAg)):
            ret[k] += sqAg[n] * cos(((2*n+1)*b)/a)

        ret[k] *= d
        if k==0:
            ret[k] /= sqrt(2)
    return sf.kryO(ret)
    '"""

    if isinstance(sqAg, list) and isinstance(sqAg[0],int):
        sqAg[0] = float(sqAg[0])
    elif isinstance(sqAg, np.ndarray) and (
            sqAg.dtype in (np.int32,np.int16,np.int64)):
        sqAg = np.array(sqAg,dtype=float)

    import scipy.fftpack as md
    return sf.kryO(md.dct(sqAg, type=2, norm='ortho'))

def idct2(sqAg):
    """' inverse dct2:Type3 Discrete Cosine Transformation for sequence argment
        return kryO vector with same norm size for argment sequence.
    '"""
    if isinstance(sqAg, list) and isinstance(sqAg[0],int):
        sqAg[0] = float(sqAg[0])
    elif isinstance(sqAg, np.ndarray) and (
            sqAg.dtype in (np.int32,np.int16,np.int64)):
        sqAg = np.array(sqAg,dtype=float)

    import scipy.fftpack as md
    return sf.kryO(md.dct(sqAg, type=3, norm='ortho'))

def quadC(*sqAg, **dctAg):
    """' inteegrate a function returning complex value in a real domain
    by scipy.integrate.quad ignoreing tolerance

    e.g.
    quadC(exp(`i `X), 0,1)
    ===============================
    (0.841470984808+0.459697694132j)

    f=0.1;quadC(λ x   :exp(-x^2) exp(2 pi `i x f), -np.inf, np.inf)
    ===============================
    (1.60587519197+0j)

    Fourier transformed function with a parameter f
    (λ f:(quadC( λ t,f:exp(-t^2) exp(2 pi `i f t), -np.inf, np.inf,args=(f,))))(0.1)
    ===============================
    (1.60587519197+0j)

    '"""
    def getRealImagFn(fnAg, blReal_ImagAg=True):
        def innerF(*sAg):
            valueAt = fnAg(*sAg)
            if blReal_ImagAg == True:
                if isinstance(valueAt,complex):
                    return valueAt.real
                else:
                    return valueAt
            else:
                if isinstance(valueAt,complex):
                    return valueAt.imag
                else:
                    return 0

        return innerF

    fnAt = sqAg[0]
    return ( sf.si_().quad(*((getRealImagFn(fnAt, True),)
                              +sqAg[1:]
                            ), **dctAg
                      )[0]
           + 1j*sf.si_().quad(*((getRealImagFn(fnAt,False),)+sqAg[1:]),
                            **dctAg)[0])

# Don't use qdrtC any more. Obsolete! Only for backward compatibility
qdrtC = quadC
qdrt = quadR    # 後で quadR を関数名に修正する

class ClODE(object):
    def __init__(self, f, x0, t0=0):
        import scipy.integrate as si

        self.m_ode = si.ode(f)
        # explicit runge-kutta method of order (4)5
        # 10.12.12 pyxy package doesn't have dopri5
        import sys
        if sys.version[7:7+3] == 'EPD':
            self.m_ode.set_integrator('dopri5')
        self.m_ode.set_initial_value(sf.kryO(x0))
        self.m_x0 = x0
        self.m_lenX0 = len(x0)
        self.m_t0=None

    def __call__(self, t, N=50, t0=None):
        if t0==None and self.m_t0==None:
            self.m_t0=0

        deltaT= 1.0*(t - self.m_t0)/N
        lstRtn=[self.m_x0]
        for k in range(N):
            self.m_ode.integrate(self.m_t0+(k+1)*deltaT)
            lstRtn.append(self.m_ode.y)

        self.m_x0  = lstRtn[-1]
        self.m_t0 += t
        if self.m_lenX0 == 1:
            return sf.kryO(lstRtn)[:,0]
        else:
            return sf.kryO(lstRtn)

def odeint(f, x0, N=50., t0=0):
    """' This odeint(..) is obsolete. Don't use odeint(..). Use kOde(..)
    time independent Runge Kutta integral by scipy.integrate.ode.
    f don't include t term

    e.g.

    odeint(~[-2 `X `Y, -`X], [1,2])(2,10)
    ===============================
    [[  4.63620997e-01   1.86108060e+00]
     [  2.23487176e-01   1.79540724e+00]
     [  1.09764092e-01   1.76345232e+00]
     [  5.44058566e-02   1.74768585e+00]
     [  2.70894588e-02   1.73985328e+00]
     [  1.35187020e-02   1.73594893e+00]
     [  6.75396145e-03   1.73399941e+00]
     [  3.37618618e-03   1.73302515e+00]
     [  1.68817038e-03   1.73253807e+00]
     [  8.44242482e-04   1.73229450e+00]]
    ---- ClTensor ----

    odeint(lambda x,y:[y,1-y-26x], [0,0])(2,10)
    ===============================
    [[ 0.          0.        ]
     [ 0.01718359  0.15146262]
     [ 0.04963093  0.14464541]
     [ 0.06654912  0.01412796]
     [ 0.0561402  -0.10493355]
     [ 0.03234834 -0.11177757]
     [ 0.01814943 -0.02083425]
     [ 0.02406873  0.0716192 ]
     [ 0.04134668  0.08545331]
     [ 0.05300066  0.02297031]
     [ 0.04998411 -0.04802681]]
    ---- ClTensor ----

    odeint(lambda *sq:[sq[1],1-sq[1]-26sq[0]], [0,0])(2,10)
    ===============================
    [[ 0.          0.        ]
     [ 0.01718359  0.15146262]
     [ 0.04963093  0.14464541]
     [ 0.06654912  0.01412796]
     [ 0.0561402  -0.10493355]
     [ 0.03234834 -0.11177757]
     [ 0.01814943 -0.02083425]
     [ 0.02406873  0.0716192 ]
     [ 0.04134668  0.08545331]
     [ 0.05300066  0.02297031]
     [ 0.04998411 -0.04802681]]
    ---- ClTensor ----


    odeint(~[`Y, 1-`Y-26`X], [0,0])(2,10)
    ===============================
    [[ 0.          0.        ]
     [ 0.01718359  0.15146262]
     [ 0.04963093  0.14464541]
     [ 0.06654912  0.01412796]
     [ 0.0561402  -0.10493355]
     [ 0.03234834 -0.11177757]
     [ 0.01814943 -0.02083425]
     [ 0.02406873  0.0716192 ]
     [ 0.04134668  0.08545331]
     [ 0.05300066  0.02297031]
     [ 0.04998411 -0.04802681]]
    ---- ClTensor ----

    # x'' = 1 - x' - 26x --- 10second, 256 point graph
    plotGr( odeint(~[`Y, 1-`Y-26`X], [0,0])(10s`, 256)[:,0])

    '"""
    if isinstance(f, sf.ClAF):
        return ClODE(lambda t, x:f(x), [x0], t0)
    elif hasattr(x0, '__len__'):
        return ClODE(lambda t, y:f(*y), x0, t0)
    else:
        return ClODE(lambda t,x:f(x), x0, t0)

def kOde(f, x0, t, N=50):
    """' time independent Runge Kutta integral by scipy.integrate.ode.

  kOde(f, x0, t, N=50)
    f:a dynamic equation that may return a vector or list
    x0: a initial codition value that may be a scalar,vector or list
    t: integrating time [0,t]
    N: returning data size

    f doesn't include t term unlike scpy.integrate.ode(..)

    e.g.

    kOde(~[-2 `X `Y, -`X], [1,2], 2s`,10)
    ===============================
    [[  4.63620997e-01   1.86108060e+00]
     [  2.23487176e-01   1.79540724e+00]
     [  1.09764092e-01   1.76345232e+00]
     [  5.44058566e-02   1.74768585e+00]
     [  2.70894588e-02   1.73985328e+00]
     [  1.35187020e-02   1.73594893e+00]
     [  6.75396145e-03   1.73399941e+00]
     [  3.37618618e-03   1.73302515e+00]
     [  1.68817038e-03   1.73253807e+00]
     [  8.44242482e-04   1.73229450e+00]]
    ---- ClTensor ----

    kOde(lambda x,y:[y,1-y-26x], [0,0],2s`,10)
    ===============================
    [[ 0.          0.        ]
     [ 0.01718359  0.15146262]
     [ 0.04963093  0.14464541]
     [ 0.06654912  0.01412796]
     [ 0.0561402  -0.10493355]
     [ 0.03234834 -0.11177757]
     [ 0.01814943 -0.02083425]
     [ 0.02406873  0.0716192 ]
     [ 0.04134668  0.08545331]
     [ 0.05300066  0.02297031]
     [ 0.04998411 -0.04802681]]
    ---- ClTensor ----

    kOde(lambda *sq:[sq[1],1-sq[1]-26sq[0]], [0,0],2s`,10)
    ===============================
    [[ 0.          0.        ]
     [ 0.01718359  0.15146262]
     [ 0.04963093  0.14464541]
     [ 0.06654912  0.01412796]
     [ 0.0561402  -0.10493355]
     [ 0.03234834 -0.11177757]
     [ 0.01814943 -0.02083425]
     [ 0.02406873  0.0716192 ]
     [ 0.04134668  0.08545331]
     [ 0.05300066  0.02297031]
     [ 0.04998411 -0.04802681]]
    ---- ClTensor ----


    kOde(~[`Y, 1-`Y-26`X], [0,0],2s`,10)
    ===============================
    [[ 0.          0.        ]
     [ 0.01718359  0.15146262]
     [ 0.04963093  0.14464541]
     [ 0.06654912  0.01412796]
     [ 0.0561402  -0.10493355]
     [ 0.03234834 -0.11177757]
     [ 0.01814943 -0.02083425]
     [ 0.02406873  0.0716192 ]
     [ 0.04134668  0.08545331]
     [ 0.05300066  0.02297031]
     [ 0.04998411 -0.04802681]]
    ---- ClTensor ----

    # x'' = 1 - x' - 26x --- 10second, 256 point graph
    plotGr( kOde(~[`Y, 1-`Y-26`X], [0,0], 10s`, 256)[:,0])

    '"""
    class _ClODE(object):
        def __init__(self,fAg):
            import scipy.integrate as si

            self.m_ode = si.ode(fAg)
            # explicit runge-kutta method of order (4)5
            # 10.12.12 pyxy package doesn't have dopri5
            import sys
            if sys.version[7:7+3] == 'EPD':
                self.m_ode.set_integrator('dopri5')

            self.m_ode.set_initial_value(sf.kryO(x0))
            self.m_x0 = x0
            self.m_lenX0 = len(x0)
            self.m_t0=0.0

        def __call__(self, t):
            deltaT= 1.0*(t - self.m_t0)/N
            lstRtn = [self.m_x0]

            for k in range(N):
                self.m_ode.integrate(self.m_t0+(k+1)*deltaT)
                lstRtn.append(list(self.m_ode.y))

            self.m_x0  = lstRtn[-1]
            self.m_t0 += t
            #import pdb; pdb.set_trace()
            if self.m_lenX0 == 1:
                return np.array(lstRtn)[:,0]
            else:
                return np.array(lstRtn)

    if not hasattr(x0, '__len__'):
        # 11.01.12 kOde(`X, 1, 10s`) を扱えるようにする
        x0 = [x0]

    if isinstance(f, sf.ClAF):
        return _ClODE(lambda t, x:f(x))(t)
    elif hasattr(x0, '__len__'):
        return _ClODE(lambda t, y:f(*y))(t)
    else:
        return _ClODE(lambda t,x:f(x))(t)


def seed(ag):
    sf.sc.random.seed(ag)

seed.__doc__ = sf.sc.random.seed.__doc__

def rand(*sqAg):
    if len(sqAg) == 0:
        return        (sf.sc.random.rand(*sqAg))
    else:
        return sf.kryO(sf.sc.random.rand(*sqAg))

rand.__doc__ = sf.sc.random.rand.__doc__

def randint(*sqAg, **dctAg):
    return  sf.sc.random.randint(*sqAg, **dctAg)

randint.__doc__ = sf.sc.random.randint.__doc__

def randi(*sq, **dct):
    """' usage
    seed(0); randi(10)
    ===============================
    5

    # 5<= x <10 random integer
    seed(0); randi(5,10)
    ===============================
    9

    # x<10 random integer: length 5 vector
    seed(0); randi(10, [5])
    ===============================
    [5 0 3 3 7]

    # 5<=x<10 random integer: length 5 vector
    seed(0); randi(5,10, [5])
    ===============================
    [9 5 8 8 8]

    ## 5<=x<10 random integer: length 6 vector
    ↑ but randi(5,10, [6]) indicate size by [6]
    seed(0); randi(5,10, 6)
    ===============================
    [9 5 8 8 8 6]

    # x<10 random integer: length 3x5 matrix
    seed(0); randi(10, [3,5])
    ===============================
    [[5 0 3 3 7]
     [9 3 5 2 4]
     [7 6 8 8 1]]

    # 5<=x<10 random integer: length 3x5 matrix
    seed(0); randi(5,10, [3,5])
    ===============================
    [[9 5 8 8 8]
     [6 8 7 9 5]
     [5 9 7 6 5]]

    # 5<=x<10 random integer: length 3x5 matrix <== randint like
    seed(0); randi(5,10, size=[3,5])
    Warning! Don't use a assignment sentence in end.
    ===============================
    [[9 5 8 8 8]
     [6 8 7 9 5]
     [5 9 7 6 5]]
    '"""
    if len(dct) != 0:
        return randint(*sq,**dct)

    assert dct=={}
    if len(sq) == 1:
        return randint(sq[0])
    elif len(sq) == 2:
        if hasattr(sq[1], '__getitem__'):
            return randint(sq[0],size=sq[1])
        else:
            return randint(*sq)
    elif len(sq) == 3:
        if hasattr(sq[2], '__getitem__'):
            return randint(sq[0],sq[1], size=sq[2])
        else:
            return randint(*sq)
    else:
        assert False, "At randi(..), you set unexpected parameters: "+str(sq)

def randn(*sqAg):
    if len(sqAg) == 0:
        return        (sf.sc.random.randn(*sqAg))
    else:
        return sf.kryO(sf.sc.random.randn(*sqAg))

randn.__doc__ = sf.sc.random.randn.__doc__

def shuffle(sqAg):
    sf.sc.random.shuffle(sqAg)
    return sqAg

shuffle.__doc__ = sf.sc.random.shuffle.__doc__


def pp(mtAg):
    """' pretty print for matrix, tensor data with 6 digit accuracy. 
       Especially effective for complex number data.
    '"""

    assert isinstance(mtAg, (sf.sc.ndarray,))
    shapeAt = mtAg.shape
    mtInLenAt = sf.sc.zeros(shapeAt, int)
    mtStrAt   = sf.sc.zeros(shapeAt, object)
    if sf.sc.iscomplexobj(mtAg) or sf.sc.isrealobj(mtAg):
        def getStr(valAg):
            valAt = valAg
            if abs(valAt) < sf.nearlyZero:
                if uppIdx==():
                    mtInLenAt[k] = 1
                    mtStrAt[k] = '0'
                else:
                    mtInLenAt[uppIdx+(k,)] = 1
                    mtStrAt[uppIdx+(k,)] = '0'
            if sf.sc.iscomplexobj(valAt):
                valRealAt = valAt.real
                valImageAt = valAt.imag
            else:
                valRealAt = valAt
                valImageAt = 0

            if abs(valRealAt) < sf.nearlyZero:
                strAt = ""
            else:
                strAt = "%1.6g"%valRealAt

            if abs(valImageAt) < sf.nearlyZero:
                if strAt == "":
                    strAt = "0"
            else:
                # image number
                if strAt == "":
                    strAt = "%1.6g"%valImageAt+ "j"
                elif valImageAt < 0:
                    strAt += "%1.6g"%valImageAt+ "j"
                else:
                    strAt += "+" + "%1.6g"%valImageAt+ "j"
            return strAt
        
        if len(shapeAt) >= 2:
            for uppIdx in sf.mrng(*shapeAt[:-1]):
                if not isinstance(uppIdx, tuple):
                    uppIdx = (uppIdx,)
                for k in range(shapeAt[-1]):
                    strAt = getStr( mtAg[uppIdx+(k,)])
    
                    mtStrAt[uppIdx+(k,)] = strAt
                    mtInLenAt[uppIdx+(k,)] = len(strAt)
        else:
            # Now vector
            #assert False, "You set vector"
            uppIdx = ()
            for k in range(shapeAt[-1]):
                strAt = getStr( mtAg[k])
    
                mtStrAt[k] = strAt
                mtInLenAt[k] = len(strAt)
    
    else:
        assert False


    inSizeAt = reduce(int.__mul__, shapeAt)
    #inSkipAt = inSizeAt/shapeAt[-1]
    inSkipAt = shapeAt[-1]
    lstMaxAt = []
    if len(shapeAt) >= 2:
        for k in range(shapeAt[-1]):
            lstMaxAt.append(max(mtInLenAt.ravel()[slice(k, inSizeAt, inSkipAt)]))
    else:
        lstMaxAt = [max(mtInLenAt)]

    #print lstMaxAt
    #print
    def pLine(posAg=0, idxAg=(), strAg = ""):
        strAt = sf.copy.deepcopy(strAg)
        if posAg >= len(shapeAt)-1:
            for k in range(shapeAt[-1]):
                if k == 0:
                    if len(idxAg) == 0 or idxAg[-1] == 0:
                        strAt += "["
                    else:
                        strAt = " "*(len(strAt)-1)+",["
                    
                if idxAg ==():
                    strAt += " "*(1+(lstMaxAt[0]-mtInLenAt[k]))
                    strAt += mtStrAt[k]
                else:
                    strAt += " "*(1+(lstMaxAt[k]-mtInLenAt[idxAg+(k,)]))
                    strAt += mtStrAt[idxAg+(k,)]
                
                if k >= shapeAt[-1]-1:
                    strAt += "]"
                else:
                    strAt += ","

            return strAt +"\n"

        else:
            strRtn = ""
            for i in range(shapeAt[posAg]):
                if i == 0:
                    if  strAt == "" or idxAg[-1] == 0 and strAt[-1] == '[':
                        strAt = strAt+'['
                    else:
                        strAt = strAt[:-1]+",["
                        #strAt = " "*(len(strAt)-1)+",["
                else:
                    strAt = ' ' * (len(strAg) + 1)
                
                strRtn += pLine(posAg+1, idxAg+(i,), strAt)

            strRtn = strRtn[:-1]+']\n'
        return strRtn

    print pLine()[:-1]
    print "-------- pp --"


