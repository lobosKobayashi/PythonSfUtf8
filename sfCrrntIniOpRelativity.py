# -*- encoding: utf-8 -*-
"""'
english:
    PythonSf sfCrrntIniOpRelativity.py
    https://github.com/lobosKobayashi
    http://lobosKobayashi.github.com/
    
    Copyright 2016, Kenji Kobayashi
    All program codes in this file was designed by kVerifierLab Kenji Kobayashi

    I release souce codes in this file under the GPLv3
    with the exception of my commercial uses.

    2016y 12m 28d Kenji Kokbayashi

japanese:
    PythonSf sfCrrntIniOpRelativity.py
    https://github.com/lobosKobayashi
    http://lobosKobayashi.github.com/

    Copyright 2016, Kenji Kobayashi
    このファイルの全てのプログラム・コードは kVerifierLab 小林憲次が作成しました。
    
    作成者の小林本人に限っては商用利用を許すとの例外条件を追加して、
    このファイルのソースを GPLv3 で公開します。

    2016年 12月 28日 小林憲次
'"""

"""'
    We implemented Natural, modified Natural, Planck and Stoney unit system
according to wikipedia:http://en.wikipedia.org/wiki/Natural_units.

    We implemented Natural/Modified Natural unit systems to deal with relativistic electro-magnetism. Because it is too complex to deal with relativistic electro-magnetism in SI unit system. We implemented Planck/Stoney unit system to clearify relations between unit systems.
'"""

import sympy as sym
import pysf.symIntf as ut
import pysfOp.customizeOp as ct
import pysfOp.sfFnctnsOp as sf

__dctGlb = sf.__getDctGlobals()
_unitConstantGlb=None
class ClLllUnit(ut.Unit):
    def __init__(self, name, abbrev):
        # ut.Unit.__new__(..)  expect only 2 argments:name, abbrev, so we can't
        # pass _unitConstantGlb value through __init__(..) parameters.
        self.m_toSI = _unitConstantGlb



mnk_bq_ = gnk_bq_ =snk_bq_ =eVnk_bq_ =Cnk_bq_ =Nnk_bq_ =Jnk_bq_ =Vnk_bq_ =dVnk_bq_ =e0nk_bq_ =u0nk_bq_ =hnk_bq_____ = 1
pQnk_bq_ =  0.302824523103951
eQnk_bq_ = -0.302824523103951

k_sAlpha_nk_bq_ = 0.0917026917931351

mkk_bq_ = gkk_bq_ =skk_bq_ =eVkk_bq_ =Ckk_bq_ =Nkk_bq_ =Jkk_bq_ =Vkk_bq_ =dVkk_bq_ =pQkk_bq_ =hkk_bq_____ = k_sAlpha_kk_bq_ = 1
eQkk_bq_ = -1

e0kk_bq_ = 10.904805305561
u0kk_bq_ = 0.0917026917931351

# Heaviside-Lorentz units
## *******************************************************************************
## Heaviside-Lorentz for modified natural unit system:pQhk`=Chk`, eQhk`, Vhk`, Thk`
e0kk_bq_= 10.904805305561
u0kk_bq_= 0.0917026917931351

## Heviside-Lorentz no dimensional value for the natural system of units
Ahk_bq_= Chk_bq_= Vhk_bq_= Thk_bq_= 1
pQhk_bq_= 0.302824523103951
eQhk_bq_= -pQhk_bq_

## *******************************************************************************
## Heviside-Lorentz no dimentional value for the modified natural system of unites
pQhkk_bq_= 0.302824523103951
Chkk_bq_= Ahkk_bq_= Vhkk_bq_= Thkk_bq_= 1
eQhkk_bq_= pQhkk_bq_

## *******************************************************************************
## Heviside-Lorentz no dimentional value for the SI
(Alk_bq_, Clk_bq_, Vlk_bq_, Tlk_bq_, pQlk_bq_) = (1,
    1, 1, 1, 5.3844262750599388e-14)

eQlk_bq_= -pQlk_bq_

def tt():
    global _unitConstantGlb

    def toSI(ag):
        ag = 1.0 * ag
        at = 1

        if float(sym.__version__[2:5]) >= 7.1:
            if ag.args == ():
                return ag

            for elm in ag.args:
                if isinstance(elm,(sym.Integer, sym.Float)):
                    at *= elm
                elif elm.is_Pow:
                    if isinstance(elm.args[0], ClLllUnit):
                        at *= elm.args[0].m_toSI ** elm.args[1]
                    else:
                        at *= elm.args[0] ** elm.args[1]
                elif isinstance(elm, ClLllUnit):
                    at *= elm.m_toSI
                else:
                    at *= elm

            return at
        else:
            if isinstance(ag,(int,float,sym.Integer, sym.Real)):
                return float(ag)
            elif isinstance(ag, ClLllUnit):
                return ag.m_toSI

            for elm in ag.args:
                if isinstance(elm,(sym.Integer, sym.Real)):
                    at *= elm
                elif elm.is_Pow:
                    if isinstance(elm.args[0], ClLllUnit):
                        at *= elm.args[0].m_toSI ** elm.args[1]
                    else:
                        at *= elm.args[0] ** elm.args[1]
                elif isinstance(elm, ClLllUnit):
                    at *= elm.m_toSI
                else:
                    at *= elm

            return at

    ct.ts()

    __alpha = __dctGlb['pQk_bq_'] **2/(
                                            4*sf.pi
                                            *__dctGlb['e0k_bq_']
                                            * __dctGlb['hk_bq_k_bq_']
                                            * __dctGlb['ck_bq_']
            ) * __dctGlb['Jk_bq_'] / __dctGlb['sk_bq_'] / __dctGlb['Wk_bq_']

    k_sAlpha_k_bq_ = __alpha

    # *****************************************************************************
    # **** define Natural units in particle physics h``==c`==kB`== eQ` V` == 1 ****
    # *****************************************************************************
    __eV = __dctGlb['pQk_bq_'] * __dctGlb['Vk_bq_'] *(
                __dctGlb['Jk_bq_']/__dctGlb['sk_bq_']/__dctGlb['Wk_bq_'])

    # define length:mn`
    _unitConstantGlb = __dctGlb['ck_bq_'] * __dctGlb['hk_bq_k_bq_']/__eV
    mnk_bq_ = ClLllUnit('meter_n','mn`')

    # define mass:gn`
    _unitConstantGlb = __eV/__dctGlb['ck_bq_'] **2
    gnk_bq_ = ClLllUnit('gram_n','gn`')

    # define time:sn`
    _unitConstantGlb = __dctGlb['hk_bq_k_bq_']/__eV
    snk_bq_ = ClLllUnit('second_n','sn`')

    # define electron volt :eVn`
    _unitConstantGlb = __eV
    eVnk_bq_ = ClLllUnit('electronVolt_n','eVn`')

    # define Lorentz Heaviside electric charge:Cn`
    _unitConstantGlb = __dctGlb['pQk_bq_']/sf.sqrt(4*sf.pi*__alpha)
    k_Cn_bq____ = ClLllUnit('Coulomb_n','Cn`')


    # derived units
    # force Newton
    Nnk_bq_ = 1* gnk_bq_ * mnk_bq_  * snk_bq_ **-2
    # energy Joule
    Jnk_bq_ = 1* gnk_bq_ * mnk_bq_**2  * snk_bq_ **-2
    # Voltage
    Vnk_bq_ = 1* gnk_bq_ * mnk_bq_ **2 * snk_bq_ **-2 * Cnk_bq_**-1 
    dVnk_bq_ = 1* mnk_bq_ **-1 * Cnk_bq_
    # e0` like constant
    e0nk_bq_ = 1* Vnk_bq_**-1 * Cnk_bq_* mnk_bq_**-1

    # mLght:meter of light:unit length of light --- pure imaginary number
    mLnk_bq_ = sym.I * mnk_bq_

    # physical constant
    # light velocity
    cnk_bq_ = 1* mnk_bq_ / snk_bq_
    # h`/(2pi)
    hnk_bq_k_q_ = 1* gnk_bq_ * mnk_bq_ ** 2/ snk_bq_
    # the charge of electron
    pQnk_bq_ =  sym.sqrt(4*sf.pi*__alpha)* Cnk_bq_
    eQnk_bq_ = -sym.sqrt(4*sf.pi*__alpha)* Cnk_bq_

    # Tn` flux Tesra
    Tnk_bq_ = 1* Vnk_bq_ * snk_bq_ / mnk_bq_ **2

    # u0` like constant
    u0nk_bq_ = 1* cnk_bq_**-2 / e0nk_bq_

    k_sAlpha_nk_bq_ = eQnk_bq_**2/(hnk_bq_k_q_ * cnk_bq_)

    # *****************************************************************************
    # **** define modified Natural units. We assigne the unit charge to elementary charge ****
    # **** D == e0k E such that e0k`=10.904805305561*Ck`**2*sk`**2/(gk`*mk`**3)
    # *****************************************************************************
    # define length:mk`
    _unitConstantGlb = __dctGlb['ck_bq_'] * __dctGlb['hk_bq_k_bq_']/__eV
    mkk_bq_ = ClLllUnit('meter_k','mk`')

    # define mass:gk`
    _unitConstantGlb = __eV/__dctGlb['ck_bq_'] **2
    gkk_bq_ = ClLllUnit('gram_k','gk`')

    # define time:sk`
    _unitConstantGlb = __dctGlb['hk_bq_k_bq_']/__eV
    skk_bq_ = ClLllUnit('second_k','sk`')

    # define electron volt :eVn`
    _unitConstantGlb = __eV
    eVkk_bq_ = ClLllUnit('electronVolt_k','eVk`')

    # define electron charge:Ck`
    _unitConstantGlb = __dctGlb['pQk_bq_']
    Ckk_bq_ = ClLllUnit('Coulomb_k','Ck`')


    # derived units
    # force Newton
    Nkk_bq_ = 1* gkk_bq_ * mkk_bq_  * skk_bq_ **-2
    # energy Joule
    Jkk_bq_ = 1* gkk_bq_ * mkk_bq_**2  * skk_bq_ **-2
    # Voltage
    dVkk_bq_ = 1* mkk_bq_ **-1 * Ckk_bq_
    # e0` like constant. hk`` ck` == k_Nk_bq____ * k_mk_bq____**2 
    e0kk_bq_ = 1*Ckk_bq_**2 /(4* sf.pi*k_sAlpha_k_bq_ * Nkk_bq_
                                       * mkk_bq_**2)
    Vkk_bq_ = dVkk_bq_ * Nkk_bq_ * mkk_bq_**2/ Ckk_bq_**2

    # mLght:meter of light:unit length of light --- pure imaginary number
    mLkk_bq_ = sym.I * mkk_bq_

    # physical constant
    # light velocity
    ckk_bq_ = 1* mkk_bq_ / skk_bq_
    # h`/(2pi)
    hkk_bq_k_bq_ = 1* gkk_bq_ * mkk_bq_ ** 2/ skk_bq_
    # the charge of electron
    pQkk_bq_ =  Ckk_bq_
    eQkk_bq_ = -Ckk_bq_

    # Tk` flux Tesra
    Tkk_bq_ = 1* Vkk_bq_ * skk_bq_ / mkk_bq_ **2

    # u0` like constant
    u0kk_bq_ = 1* ckk_bq_**-2 / e0kk_bq_

    k_sAlpha_kk_bq_ = eQkk_bq_**2/(hkk_bq_k_bq_ * ckk_bq_)

    # **********************************************
    # Heaviside-Lorentz pQhk`=Chk`, eQhk`, Vhk`, Thk`
    # **********************************************
    pQhkk_bq_=Chkk_bq_=Ckk_bq_ / sf.sqrt(e0kk_bq_)
    eQhkk_bq_ = -pQhkk_bq_
    Vhkk_bq_=Vkk_bq_ * sf.sqrt(e0kk_bq_)
    Thkk_bq_=Tkk_bq_ / sf.sqrt(u0kk_bq_)

    """' Nature doesn't allow us to difine a ideal natural unit system where a
    unit charge is the elementary charge of one electron.  It is impossible to
    write an ideal natural unit system as described below.

        But I dare to leave the wrong codes. Because It will be usefull if a user
    write test codes and understand unit systems.
    # *****************************************************************************
    # **** define ideal Natural units in particle physics h``==c`==kB`== eQ`== e0` == u0` == 1 ****
    # *****************************************************************************
    # define length:mi`

    __K = 0.0917026917932       # __K == (toSI(Ci`)/toSI(Cn`))^2
    _unitConstantGlb = __K* __dctGlb['ck_bq_'] * __dctGlb['hk_bq_k_bq_']/__eV
    mik_bq_ = ClLllUnit('meter_i','mi`')

    # define mass:gi`
    _unitConstantGlb = __eV/__dctGlb['ck_bq_'] **2 / __K
    gik_bq_ = ClLllUnit('gram_i','gi`')

    # define time:si`
    _unitConstantGlb = __K* __dctGlb['hk_bq_k_bq_']/__eV
    sik_bq_ = ClLllUnit('second_i','si`')

    # define electron charge:Cn`
    _unitConstantGlb = __dctGlb['pQk_bq_']
    Cik_bq_ = ClLllUnit('Coulomb_i','Ci`')


    # force Newton
    Nik_bq_ = 1* gik_bq_ * mik_bq_  * sik_bq_ **-2
    # derived units
    # energy Joule
    Jik_bq_ = 1* gik_bq_ * mik_bq_**2  * sik_bq_ **-2
    # Voltage
    Vik_bq_ = 1* gik_bq_ * mik_bq_ **2 * sik_bq_ **-2 * Cik_bq_**-1 
    dVik_bq_ = 1* mik_bq_ **-1 * Cik_bq_
    # e0` like constant
    e0ik_bq_ = 1* Vik_bq_**-1 * Cik_bq_* mik_bq_**-1

    # mLght:meter of light:unit length of light --- pure imaginary number
    mLik_bq_ = sym.I * mik_bq_

    # physical constant
    # light velocity
    cik_bq_ = 1* mik_bq_ / sik_bq_
    # h`/(2pi)
    hik_bq_k_bq_ = 1* gik_bq_ * mik_bq_ ** 2/ sik_bq_
    # the charge of electron
    eQik_bq_ = Cik_bq_

    # u0` like constant
    u0ik_bq_ = 1* cik_bq_**-2 / e0ik_bq_

    k_sAlpha_ik_bq_ = eQik_bq_**2/(hik_bq_k_bq_ * cik_bq_)
    '"""

    # *****************************************************************************
    # **** define Planck units ****
    # *****************************************************************************
    # define Planc length
    _unitConstantGlb = sf.sqrt(
            __dctGlb['hk_bq_k_bq_'] * __dctGlb['gUk_bq_']
            /__dctGlb['ck_bq_']**3)
    mpk_bq_ = ClLllUnit('meter_p','mp`')

    # Planck time: mp`/c`: sqrt(h`` c`/gU`)
    _unitConstantGlb = mpk_bq_.m_toSI / __dctGlb['ck_bq_']
    spk_bq_ = ClLllUnit('second_p','sp`')

    # Planck mass: sqrt(h`` c`/gU`)
    _unitConstantGlb =  sym.sqrt(
                    __dctGlb['hk_bq_k_bq_']* __dctGlb['ck_bq_']
                    /__dctGlb['gUk_bq_'] )
    gpk_bq_ = ClLllUnit('gram_p','gp`')

    # Planck Charge: eQ`/sqrt(4pi α`)
    _unitConstantGlb =  __dctGlb['pQk_bq_']/sf.sqrt(4* sf.pi * __alpha)
    Cpk_bq_ = ClLllUnit('Coulomb_p','Cp`')

    # **** define `c, h`, eQ`, (eQ`^2/(4pi ε0` h`` c`)):Fine structure constant == 1 ****

    # derived units
    Npk_bq_ = 1* gpk_bq_ * mpk_bq_  * spk_bq_ **-2
    # Vp` Voltage has both of mechanical units and electro-magnetic units
    # Vp` means a potential difference that is the unit energy: m c^2 for the unit charge and mass.
    # <== Charge * Voltage == Energy
    Vpk_bq_ = 1* gpk_bq_ * mpk_bq_ **2 * spk_bq_ **-2 * Cpk_bq_**-1 
    dVpk_bq_ = 1* mpk_bq_ **-1 * Cpk_bq_
    #e0pk_bq_ = 1* Vpk_bq_**-1 * Cpk_bq_* mpk_bq_**-1
    e0pk_bq_ = 1* mpk_bq_**-3 * gpk_bq_**-1 * spk_bq_**2 * Cpk_bq_**2

    # physical constant
    # light velocity
    cpk_bq_ = 1* mpk_bq_ / spk_bq_
    hpk_bq_k_bq_ = 1* gpk_bq_ * mpk_bq_ ** 2/ spk_bq_
    pQpk_bq_ =  sym.sqrt(4*sf.pi*__alpha)* Cpk_bq_
    eQpk_bq_ = -sym.sqrt(4*sf.pi*__alpha)* Cpk_bq_

    # Tp` flux Tesra
    Tpk_bq_ = 1* Vpk_bq_ * spk_bq_ / mpk_bq_ **2

    k_sAlpha_pk_bq_ = eQpk_bq_**2/(hpk_bq_k_bq_ * cpk_bq_)


    # *****************************************************************************
    # **** define Stoney units:http://en.wikipedia.org/wiki/Natural_units ****
    # *****************************************************************************
    # Stoney length: h`^2 (4pi e0`)/(eM` eQ^2)
    _unitConstantGlb = (__dctGlb['Wk_bq_']*__dctGlb['sk_bq_']/__dctGlb['Jk_bq_'] * 
            __dctGlb['hk_bq_k_bq_']**2 * (4*sf.pi* __dctGlb['e0k_bq_'])
            /(__dctGlb['eMk_bq_'] * __dctGlb['pQk_bq_']**2)
            )
    msk_bq_ = ClLllUnit('meter_s','ms`')

    # Stoney time: h``^3 (4pi e0`)^2/eM` eQ^4
    _unitConstantGlb = ((__dctGlb['Wk_bq_']*__dctGlb['sk_bq_']/__dctGlb['Jk_bq_'])**2 * 
            __dctGlb['hk_bq_k_bq_']**3 * (4*sf.pi* __dctGlb['e0k_bq_'])**2
            /(__dctGlb['eMk_bq_'] * __dctGlb['pQk_bq_']**4)
            )
    ssk_bq_ = ClLllUnit('second_s','ss`')

    # Stoney mass: sqrt( e^2/(G 4pi e0)
    _unitConstantGlb = sf.sqrt(
            __dctGlb['pQk_bq_']**2 
            /(__dctGlb['gUk_bq_']* 4*sf.pi* __dctGlb['e0k_bq_'])
            * __dctGlb['Jk_bq_'] / __dctGlb['sk_bq_'] / __dctGlb['Wk_bq_']
            )
    gsk_bq_ = ClLllUnit('gram_s','gs`')

    # Planck Charge: eQ`/sqrt(4pi α`)
    _unitConstantGlb =  __dctGlb['pQk_bq_']
    Csk_bq_ = ClLllUnit('Coulomb_s','Cs`')

    # **** define `c, h`, eQ`, (eQ`^2/(4pi ε0` h`` c`)):Fine structure constant == 1 ****

    # derived units
    Nsk_bq_ = 1* gsk_bq_ * msk_bq_  * ssk_bq_ **-2
    Vsk_bq_ = 1* gsk_bq_ * msk_bq_ **2 * ssk_bq_ **-2 * Csk_bq_**-1 
    dVsk_bq_ = 1* msk_bq_ **-1 * Csk_bq_
    #e0sk_bq_ = 1* Vsk_bq_**-1 * Csk_bq_* msk_bq_**-1
    e0sk_bq_ = 1* msk_bq_**-3 * gsk_bq_**-1 * ssk_bq_**2 * Csk_bq_**2

    # physical constant
    # light velocity
    csk_bq_ = 1* msk_bq_ / ssk_bq_
    hsk_bq_k_bq_ =              gsk_bq_ * msk_bq_ ** 2/ ssk_bq_
    pQsk_bq_ =  Csk_bq_
    eQsk_bq_ = -Csk_bq_

    # Ts` flux Tesra
    Tsk_bq_ = 1* Vsk_bq_ * ssk_bq_ / msk_bq_ **2

    k_sAlpha_sk_bq____ = eQsk_bq_**2/(hsk_bq_k_bq_ * csk_bq_)

    """'
    '"""
    def RttS(theta, axis=[1,1]):
        """' Return a rotating matrix. "axis" parameter defines the reference
        axises for the rotation and also define the matrix size.

        "theta" parameter represents counter clock wise rotation. Complex theta
        means a Lorentz matrix.

            You should set 1 just 2 times in the axis parameter sequence which indicates
        rotating axis

        e.g.
        Rtt(`i pi/3)
        ===============================
        [[ 1.60028686-0.j          0.00000000+1.24936705j]
         [-0.00000000-1.24936705j  1.60028686-0.j        ]]
        ---- ClTensor ----

        Rtt(pi/3, [1,0,0,1])
        ===============================
        [[ 0.5        0.         0.         0.8660254]
         [ 0.         0.         0.         0.       ]
         [ 0.         0.         0.         0.       ]
         [-0.8660254  0.         0.         0.5      ]]
        ---- ClTensor ----
        '"""
        axisAt = list(axis)
        sizeAt = len(axisAt)
        firstIndexAt = axisAt.index(1)
        secondIndexAt = axisAt.index(1, firstIndexAt+1)

        import sympy
        assert sf.__dctGlobals['ts'] == sympy
        r1=sympy.Rational(1)
        mtAt = sf.kzrs(sizeAt, sizeAt, ftype=type(1.0*r1) )

        mtAt[firstIndexAt, firstIndexAt] = sf.cos(theta) * r1
        mtAt[firstIndexAt, secondIndexAt] = sf.sin(theta) * r1
        mtAt[secondIndexAt, firstIndexAt] =-sf.sin(theta) * r1
        mtAt[secondIndexAt, secondIndexAt] = sf.cos(theta) * r1

        return mtAt

    sf.__getDctGlobals().update(locals())

def Rtt(theta, axis=[1,1]):
    axisAt = list(axis)
    sizeAt = len(axisAt)
    firstIndexAt = axisAt.index(1)
    secondIndexAt = axisAt.index(1, firstIndexAt+1)

    import numpy as np
    if np.iscomplex(theta):
        # complex matrix:Lorentz transformation matrix
        mtAt = sf.kzrs(sizeAt, sizeAt, complex)**0
    else:
        # real matrix: normal ratating matrix
        mtAt = sf.kzrs(sizeAt, sizeAt)**0

    mtAt[firstIndexAt, firstIndexAt] = sf.cos(theta)
    mtAt[firstIndexAt, secondIndexAt] = sf.sin(theta)
    mtAt[secondIndexAt, firstIndexAt] =-sf.sin(theta)
    mtAt[secondIndexAt, secondIndexAt] = sf.cos(theta)

    return mtAt

def mnl(v):
    """' Normalize vector v at Minkowski space.
        mnl(.) returns a v direction vector of that product with itself is -1
    example

    mnl([0.8, 0.1, 0.2, `i])
    ===============================
    [ 1.43684242+0.j          0.17960530+0.j          0.35921060+0.j 0.00000000+1.79605302j]
    ---- ClTensor ----
    mnl([0.8, 0.1, 0.2])
    ===============================
    [ 0.+0.96308682j  0.+0.12038585j  0.+0.24077171j]
    ---- ClTensor ----

    '"""
    if not isinstance(v, sf.ClTensor):
        v = sf.krry(v)
    assert v * v < 0, "You set a space like vector:"+str(v)
    return 1j*v/sf.sqrt(v*v)

def Lvv(vcVelocity):
    """' Boost Lorentz transformation for the velocity vector in natural unit
    examples
    Lvv(0.8)
    ===============================
    [[ 1.66666667+0.j          0.00000000-1.33333333j]
     [ 0.00000000+1.33333333j  1.66666667+0.j        ]]
    ---- ClTensor ----

    Lvv([0.8])
    ===============================
    [[ 1.66666667+0.j          0.00000000-1.33333333j]
     [ 0.00000000+1.33333333j  1.66666667+0.j        ]]
    ---- ClTensor ----

    Lvv([0.8,0.1])
    ===============================
    [[ 1.67968838+0.j          0.08496105+0.j          0.00000000-1.35224681j]
     [ 0.08496105+0.j          1.01062013+0.j          0.00000000-0.16903085j]
     [ 0.00000000+1.35224681j  0.00000000+0.16903085j  1.69030851+0.j        ]]
    ---- ClTensor ----

    Lvv([0.8,0.1, 0.2])
    ===============================
    [[ 1.73836802+0.j  0.09229600+0.j  0.18459200+0.j  0.00000000-1.43684242j]
     [ 0.09229600+0.j  1.01153700+0.j  0.02307400+0.j  0.00000000-0.1796053j ]
     [ 0.18459200+0.j  0.02307400+0.j  1.04614800+0.j  0.00000000-0.3592106j ]
     [ 1.43684242j     0.1796053j      0.3592106j      1.79605302+0.j        ]]
    ---- ClTensor ----

    '"""
    """'
    if isinstance(vcVelocity,float):
        vcVelocity = [vcVelocity]
    assert sf.norm(vcVelocity) < 1
    N=len(vcVelocity)
    n2 = sf.normalize(vcVelocity)
    E  = sf.kzrs(N,N)**0
    n1 = sf.kzrs(N)
    n1[0] = 1
    nm = sf.normalize(n1+n2)
    R = (E - 2*n2**n2) * (E-2*nm**nm)
    RR = sf.kzrs(N+1,N+1)**0
    RR[:N, :N] = R
    axis=sf.kzrs(N+1)
    axis[0], axis[-1]=1,1
    return RR* Rtt(sf.arctan(sf.norm(vcVelocity)/1j), axis)* RR**-1
    '"""
    # implementing by diadic
    if isinstance(vcVelocity,float):
        vcVelocity = (vcVelocity,1j)
    else:
        vcVelocity = tuple(vcVelocity)+(1j,)
    assert sf.norm(vcVelocity[:-1]) < 1
    N=len(vcVelocity)

    #n2,n1=mnl(vcVelocity),[0,0,0,1j]
    n2,n1=mnl(vcVelocity),[0]*(N-1)+[1j]
    nm=mnl(n1+n2)
    E=sf.kzrs(N,N)**0;
    return (E+2*n2**n2)*(E+2*nm**nm)

def k__Round_JM___(fnAg, inDim=None, outDim=None):
    """' Jacobian at Minkowski space
    '"""
    clAt = sf.Jc_(fnAg,inDim,outDim)          # ∂J Jacobian

    def __inner(*posAg):
        mtAt = sf.krry(clAt(*posAg), dtype=complex)   
        shapeAt = mtAt.shape
        for indx_1 in sf.mitr(*shapeAt[:-1]):
            for k in range(shapeAt[-1]):
                if isinstance(indx_1,int):
                    mtAt[(indx_1, k )] *=1/(1j)
                else:
                    mtAt[indx_1+(k,)] *=1/(1j)

        return mtAt
    
    return __inner

def k__bq_rotM___(fVct, **kwAg):
    """' rot(..) function at Minkowski space
    '"""
    def __inner(*pos):
        mtAt = k__Round_JM___(fVct,**kwAg)(*pos)     # `rot
        return mtAt - mtAt.T


    return __inner

if __name__ == "__main__":
    tt()
    toSI = sf.__getDctGlobals()['toSI']
    k_m_bq____ = sf.__getDctGlobals()['k_m_bq____']
    assert float((toSI(k_mk_bq____) - 1.97325397334585e-7*k_m_bq____)/k_m_bq____) < 1e-20
    assert float((toSI(1* k_mk_bq____) - 1.97325397334585e-7*k_m_bq____)/k_m_bq____) < 1e-20
    assert float((toSI(2.5* k_mk_bq____) - 2.5*1.97325397334585e-7*k_m_bq____)/k_m_bq____) < 1e-20

