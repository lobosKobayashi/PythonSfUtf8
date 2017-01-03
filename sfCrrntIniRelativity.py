# -*- encoding: utf-8 -*-
"""'
english:
    PythonSf sfCrrntIniRelativity.py
    https://github.com/lobosKobayashi
    http://lobosKobayashi.github.com/
    
    Copyright 2016, Kenji Kobayashi
    All program codes in this file was designed by kVerifierLab Kenji Kobayashi

    I release souce codes in this file under the GPLv3
    with the exception of my commercial uses.

    2016y 12m 28d Kenji Kokbayashi

japanese:
    PythonSf sfCrrntIniRelativity.py
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
import pysf.customize as ct
import pysf.sfFnctns as sf

__dctGlb = sf.__getDctGlobals()
_unitConstantGlb=None
class ClLllUnit(ut.Unit):
    def __init__(self, name, abbrev):
        # ut.Unit.__new__(..)  expect only 2 argments:name, abbrev, so we can't
        # pass _unitConstantGlb value through __init__(..) parameters.
        self.m_toSI = _unitConstantGlb



k_mn_bq____ = k_gn_bq____ =k_sn_bq____ =k_eVn_bq____ =k_Cn_bq____ =k_Nn_bq____ =k_Jn_bq____ =k_Vn_bq____ =k_dVn_bq____ =k_e0n_bq____ =k_u0n_bq____ =k_hn_bq__bq____ = k_cn_bq____  = k_Tn_bq____= 1
k_pQn_bq____ =  0.302824523103951
k_eQn_bq____ = -0.302824523103951

k__sAlpha_n_bq____ = 0.0917026917931351

k_mk_bq____ = k_gk_bq____ =k_sk_bq____ =k_eVk_bq____ =k_Ck_bq____ =k_Nk_bq____ =k_Jk_bq____ =k_Vk_bq____ =k_dVk_bq____ =k_pQk_bq____ =k_hk_bq__bq____ = k__sAlpha_k_bq____ = k_ck_bq____ = k_Tk_bq____ = 1
k_eQk_bq____ = -1

# *******************************************************************************
# Heaviside-Lorentz for modified natural unit system:pQhk`=Chk`, eQhk`, Vhk`, Thk`
# *******************************************************************************
k_e0k_bq____ = 10.904805305561
k_u0k_bq____ = 0.0917026917931351

k_pQhk_bq____ = k_Chk_bq____=0.302824523103951
k_eQhk_bq____ = -0.302824523103951
k_Vhk_bq____ = k_Thk_bq____ =3.30224246619792


k_mLn_bq____ = k_mLk_bq____ =  1j

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

    __alpha = __dctGlb['k_pQ_bq____'] **2/(
                                            4*sf.pi
                                            *__dctGlb['k_e0_bq____']
                                            * __dctGlb['k_h_bq__bq____']
                                            * __dctGlb['k_c_bq____']
            ) * __dctGlb['k_J_bq____'] / __dctGlb['k_s_bq____'] / __dctGlb['k_W_bq____']

    k__sAlpha__bq____ = __alpha

    # *****************************************************************************
    # **** define Natural units in particle physics h``==c`==kB`== eQ` V` == 1 ****
    # *****************************************************************************
    __eV = __dctGlb['k_pQ_bq____'] * __dctGlb['k_V_bq____'] *(
                __dctGlb['k_J_bq____']/__dctGlb['k_s_bq____']/__dctGlb['k_W_bq____'])

    # define length:mn`
    _unitConstantGlb = __dctGlb['k_c_bq____'] * __dctGlb['k_h_bq__bq____']/__eV
    k_mn_bq____ = ClLllUnit('meter_n','mn`')

    # define mass:gn`
    _unitConstantGlb = __eV/__dctGlb['k_c_bq____'] **2
    k_gn_bq____ = ClLllUnit('gram_n','gn`')

    # define time:sn`
    _unitConstantGlb = __dctGlb['k_h_bq__bq____']/__eV
    k_sn_bq____ = ClLllUnit('second_n','sn`')

    # define electron volt :eVn`
    _unitConstantGlb = __eV
    k_eVn_bq____ = ClLllUnit('electronVolt_n','eVn`')

    # define natural unit charge:Cn`
    _unitConstantGlb = __dctGlb['k_pQ_bq____']/sf.sqrt(4*sf.pi*__alpha)
    k_Cn_bq____ = ClLllUnit('Coulomb_n','Cn`')


    # derived units
    # force Newton
    k_Nn_bq____ = 1* k_gn_bq____ * k_mn_bq____  * k_sn_bq____ **-2
    # energy Joule
    k_Jn_bq____ = 1* k_gn_bq____ * k_mn_bq____**2  * k_sn_bq____ **-2
    # Voltage
    k_Vn_bq____ = 1* k_gn_bq____ * k_mn_bq____ **2 * k_sn_bq____ **-2 * k_Cn_bq____**-1 
    k_dVn_bq____ = 1* k_mn_bq____ **-1 * k_Cn_bq____
    # e0` like constant
    k_e0n_bq____ = 1* k_Vn_bq____**-1 * k_Cn_bq____* k_mn_bq____**-1

    # mLght:meter of light:unit length of light --- pure imaginary number
    k_mLn_bq____ = sym.I * k_mn_bq____

    # physical constant
    # light velocity
    k_cn_bq____ = 1* k_mn_bq____ / k_sn_bq____
    # h`/(2pi)
    k_hn_bq__bq____ = 1* k_gn_bq____ * k_mn_bq____ ** 2/ k_sn_bq____
    # the charge of electron
    k_eQn_bq____ = -sym.sqrt(4*sf.pi*__alpha)* k_Cn_bq____
    k_pQn_bq____ =  sym.sqrt(4*sf.pi*__alpha)* k_Cn_bq____

    # Tn` flux Tesra
    k_Tn_bq____ = 1* k_Vn_bq____* k_sn_bq____ / k_mn_bq____ **2

    # u0` like constant
    k_u0n_bq____ = 1* k_cn_bq____**-2 / k_e0n_bq____

    k__sAlpha_n_bq____ = k_eQn_bq____**2/(k_hn_bq__bq____ * k_cn_bq____)

    # *****************************************************************************
    # **** define modified Natural an unit charge assigned to elementary charge ****
    # **** D == e0k E such that e0k`=10.904805305561*Ck`**2*sk`**2/(gk`*mk`**3)
    # *****************************************************************************
    # define length:mk`
    _unitConstantGlb = __dctGlb['k_c_bq____'] * __dctGlb['k_h_bq__bq____']/__eV
    k_mk_bq____ = ClLllUnit('meter_k','mk`')

    # define mass:gk`
    _unitConstantGlb = __eV/__dctGlb['k_c_bq____'] **2
    k_gk_bq____ = ClLllUnit('gram_k','gk`')

    # define time:sk`
    _unitConstantGlb = __dctGlb['k_h_bq__bq____']/__eV
    k_sk_bq____ = ClLllUnit('second_k','sk`')

    # define electron volt :eVn`
    _unitConstantGlb = __eV
    k_eVk_bq____ = ClLllUnit('electronVolt_k','eVk`')

    # define electron charge:Ck`
    _unitConstantGlb = __dctGlb['k_pQ_bq____']
    k_Ck_bq____ = ClLllUnit('Coulomb_k','Ck`')


    # derived units
    # force Newton
    k_Nk_bq____ = 1* k_gk_bq____ * k_mk_bq____  * k_sk_bq____ **-2
    # energy Joule
    k_Jk_bq____ = 1* k_gk_bq____ * k_mk_bq____**2  * k_sk_bq____ **-2
    # Voltage
    #k_dVk_bq____ = 1* k_gk_bq____ * k_mk_bq____ **2 * k_sk_bq____ **-2 * k_Ck_bq____**-1 
    k_dVk_bq____ = 1* k_mk_bq____ **-1 * k_Ck_bq____
    # e0` like constant. hk`` ck` == k_Nk_bq____ * k_mk_bq____**2 
    k_e0k_bq____ = 1*k_Ck_bq____**2 /(4* sf.pi*k__sAlpha__bq____ * k_Nk_bq____
                                       * k_mk_bq____**2)
    #k_Vk_bq____ = k_dVk_bq____ / k_e0k_bq____  2012.10.12
    k_Vk_bq____ = k_dVk_bq____ * k_Nk_bq____ * k_mk_bq____**2/ k_Ck_bq____**2

    # mLght:meter of light:unit length of light --- pure imaginary number
    k_mLk_bq____ = sym.I * k_mk_bq____

    # physical constant
    # light velocity
    k_ck_bq____ = 1* k_mk_bq____ / k_sk_bq____
    # h`/(2pi)
    k_hk_bq__bq____ = 1* k_gk_bq____ * k_mk_bq____ ** 2/ k_sk_bq____
    # the charge of electron
    k_eQk_bq____ = -k_Ck_bq____
    k_pQk_bq____ =  k_Ck_bq____

    # Tn` flux Tesra
    k_Tk_bq____ = 1* k_Vk_bq____* k_sk_bq____ / k_mk_bq____ **2

    # u0` like constant
    k_u0k_bq____ = 1* k_ck_bq____**-2 / k_e0k_bq____

    k__sAlpha_k_bq____ = k_eQk_bq____**2/(k_hk_bq__bq____ * k_ck_bq____)


    # **********************************************
    # Heaviside-Lorentz pQhk`=Chk`, eQhk`, Vhk`, Thk`
    # **********************************************
    k_pQhk_bq____=k_Chk_bq____=k_Ck_bq____ / sf.sqrt(k_e0k_bq____)
    k_eQhk_bq____ = -k_pQhk_bq____
    k_Vhk_bq____=k_Vk_bq____ * sf.sqrt(k_e0k_bq____)
    k_Thk_bq____=k_Tk_bq____ / sf.sqrt(k_u0k_bq____)

    
    """' Nature doesn't allow us to difine a ideal natural unit system where a
    unit charge is the elementary charge of one electron.  It is impossible to
    write an ideal natural unit system as described below.

        But I dare to leave the wrong codes. Because It will be usefull if a user
    write test codes and understand unit systems.
    # *****************************************************************************
    # **** define ideal Natural units in particle physics h``==c`==kB`== eQ`== e0` == u0` == 1 ****
    # *****************************************************************************
    # define length:mi`

    __K = 0.0917026917932       #;; __K == (toSI(Ci`)/toSI(Cn`))^2 == 4pi α`
    _unitConstantGlb = __K**-1 * __dctGlb['k_c_bq____'] * __dctGlb['k_h_bq__bq____']/__eV
    k_mi_bq____ = ClLllUnit('meter_i','mi`')

    # define mass:gi`
    _unitConstantGlb = __K**2 * __eV/__dctGlb['k_c_bq____'] **2
    k_gi_bq____ = ClLllUnit('gram_i','gi`')

    # define time:si`
    _unitConstantGlb = __K**-1 * __dctGlb['k_h_bq__bq____']/__eV
    k_si_bq____ = ClLllUnit('second_i','si`')

    # define electron charge:Cn`
    _unitConstantGlb = __dctGlb['k_pQ_bq____']
    k_Ci_bq____ = ClLllUnit('Coulomb_i','Ci`')


    # force Newton
    k_Ni_bq____ = 1* k_gi_bq____ * k_mi_bq____  * k_si_bq____ **-2
    # derived units
    # energy Joule
    k_Ji_bq____ = 1* k_gi_bq____ * k_mi_bq____**2  * k_si_bq____ **-2
    # Voltage
    k_Vi_bq____ = 1* k_gi_bq____ * k_mi_bq____ **2 * k_si_bq____ **-2 * k_Ci_bq____**-1 
    k_dVi_bq____ = 1* k_mi_bq____ **-1 * k_Ci_bq____
    # e0` like constant
    #k_e0i_bq____ = 1* k_Vi_bq____**-1 * k_Ci_bq____* k_mi_bq____**-1
    k_e0i_bq____ = 1* k_mi_bq____**-3 * k_gi_bq____**-1 * k_si_bq____**2 * k_Ci_bq____**2
    #k_e0i_bq____ = 1* k_mi_bq____**-3 * k_gi_bq____**+1 * k_si_bq____**2 * k_Ci_bq____**2

    # mLght:meter of light:unit length of light --- pure imaginary number
    k_mLi_bq____ = sym.I * k_mi_bq____

    # physical constant
    # light velocity
    k_ci_bq____ = 1* k_mi_bq____ / k_si_bq____
    # h`/(2pi)
    k_hi_bq__bq____ = 1* k_gi_bq____ * k_mi_bq____ ** 2/ k_si_bq____
    # the charge of electron
    k_eQi_bq____ = k_Ci_bq____

    # u0` like constant
    k_u0i_bq____ = 1* k_ci_bq____**-2 / k_e0i_bq____

    k__sAlpha_i_bq____ = k_eQi_bq____**2/(k_hi_bq__bq____ * k_ci_bq____)
    '"""

    # *****************************************************************************
    # **** define Planck units ****
    # *****************************************************************************
    # define Planc length
    _unitConstantGlb = sf.sqrt(
            __dctGlb['k_h_bq__bq____'] * __dctGlb['k_gU_bq____']
            /__dctGlb['k_c_bq____']**3)
    k_mp_bq____ = ClLllUnit('meter_p','mp`')

    # Planck time: mp`/c`: sqrt(h`` c`/gU`)
    _unitConstantGlb = k_mp_bq____.m_toSI / __dctGlb['k_c_bq____']
    k_sp_bq____ = ClLllUnit('second_p','sp`')

    # Planck mass: sqrt(h`` c`/gU`)
    _unitConstantGlb =  sym.sqrt(
                    __dctGlb['k_h_bq__bq____']* __dctGlb['k_c_bq____']
                    /__dctGlb['k_gU_bq____'] )
    k_gp_bq____ = ClLllUnit('gram_p','gp`')

    # Planck Charge: eQ`/sqrt(4pi α`)
    _unitConstantGlb =  __dctGlb['k_pQ_bq____']/sf.sqrt(4* sf.pi * __alpha)
    k_Cp_bq____ = ClLllUnit('Coulomb_p','Cp`')

    # **** define `c, h`, eQ`, (eQ`^2/(4pi ε0` h`` c`)):Fine structure constant == 1 ****

    # derived units
    k_Np_bq____ = 1* k_gp_bq____ * k_mp_bq____  * k_sp_bq____ **-2
    # Vp` Voltage has both of mechanical units and electro-magnetic units
    # Vp` means a potential difference that is the unit energy: m c^2 for the unit charge and mass.
    # <== Charge * Voltage == Energy
    k_Vp_bq____ = 1* k_gp_bq____ * k_mp_bq____ **2 * k_sp_bq____ **-2 * k_Cp_bq____**-1 
    k_dVp_bq____ = 1* k_mp_bq____ **-1 * k_Cp_bq____
    # e0` like constant
    #k_e0p_bq____ = 1* k_Vp_bq____**-1 * k_Cp_bq____* k_mp_bq____**-1
    k_e0p_bq____ = 1* k_mp_bq____**-3 * k_gp_bq____**-1 * k_sp_bq____**2 * k_Cp_bq____**2

    # physical constant
    # light velocity
    k_cp_bq____ = 1* k_mp_bq____ / k_sp_bq____
    k_hp_bq__bq____ = 1* k_gp_bq____ * k_mp_bq____ ** 2/ k_sp_bq____
    k_eQp_bq____ = -sym.sqrt(4*sf.pi*__alpha)* k_Cp_bq____
    k_pQp_bq____ =  sym.sqrt(4*sf.pi*__alpha)* k_Cp_bq____

    # Tp` flux Tesra
    k_Tp_bq____ = 1* k_Vp_bq____* k_sp_bq____ / k_mp_bq____ **2

    k__sAlpha_p_bq____ = k_eQp_bq____**2/(k_hp_bq__bq____ * k_cp_bq____)


    # *****************************************************************************
    # **** define Stoney units:http://en.wikipedia.org/wiki/Natural_units ****
    # *****************************************************************************
    # Stoney length: h`^2 (4pi e0`)/(eM` eQ^2)
    _unitConstantGlb = (__dctGlb['k_W_bq____']*__dctGlb['k_s_bq____']/__dctGlb['k_J_bq____'] * 
            __dctGlb['k_h_bq__bq____']**2 * (4*sf.pi* __dctGlb['k_e0_bq____'])
            /(__dctGlb['k_eM_bq____'] * __dctGlb['k_pQ_bq____']**2)
            )
    k_ms_bq____ = ClLllUnit('meter_s','ms`')

    # Stoney time: h``^3 (4pi e0`)^2/eM` eQ^4
    _unitConstantGlb = ((__dctGlb['k_W_bq____']*__dctGlb['k_s_bq____']/__dctGlb['k_J_bq____'])**2 * 
            __dctGlb['k_h_bq__bq____']**3 * (4*sf.pi* __dctGlb['k_e0_bq____'])**2
            /(__dctGlb['k_eM_bq____'] * __dctGlb['k_pQ_bq____']**4)
            )
    k_ss_bq____ = ClLllUnit('second_s','ss`')

    # Stoney mass: eM`
    _unitConstantGlb = __dctGlb['k_eM_bq____']
    k_gs_bq____ = ClLllUnit('gram_s','gs`')

    # Stoney Charge: eQ`
    _unitConstantGlb =  __dctGlb['k_pQ_bq____']
    k_Cs_bq____ = ClLllUnit('Coulomb_s','Cs`')

    # **** define `c, h`, eQ`, (eQ`^2/(4pi ε0` h`` c`)):Fine structure constant == 1 ****

    # derived units
    k_Ns_bq____ = 1* k_gs_bq____ * k_ms_bq____  * k_ss_bq____ **-2
    k_Vs_bq____ = 1* k_gs_bq____ * k_ms_bq____ **2 * k_ss_bq____ **-2 * k_Cs_bq____**-1 
    k_dVs_bq____ = 1* k_ms_bq____ **-1 * k_Cs_bq____
    # e0` like constant
    #k_e0s_bq____ = 1* k_Vs_bq____**-1 * k_Cs_bq____* k_ms_bq____**-1
    k_e0s_bq____ = 1* k_ms_bq____**-3 * k_gs_bq____**-1 * k_ss_bq____**2 * k_Cs_bq____**2

    # physical constant
    # light velocity
    k_cs_bq____ = 1* k_ms_bq____ / k_ss_bq____
    k_hs_bq__bq____ =              k_gs_bq____ * k_ms_bq____ ** 2/ k_ss_bq____
    k_eQs_bq____ = -k_Cs_bq____
    k_pQs_bq____ =  k_Cs_bq____

    # Ts` flux Tesra
    k_Ts_bq____ = 1* k_Vs_bq____* k_ss_bq____ / k_ms_bq____ **2

    k__sAlpha_s_bq____ = k_eQs_bq____**2/(k_hs_bq__bq____ * k_cs_bq____)

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
    #assert v * v < 0, "You set a space like vector:"+str(v)
    return 1j*v/sf.sqrt(v*v)

def Lvv(vcVelocity):
    """' Boost Lorentz transformation at Minkowski space for the velocity vector in natural unit
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
    if isinstance(vcVelocity,(int,float)):
        vcVelocity = (vcVelocity,1j)
    else:
        vcVelocity = tuple(vcVelocity)+(1j,)
    #assert sf.norm(vcVelocity[:-1]) < 1
    N=len(vcVelocity)

    #n2,n1=mnl(vcVelocity),[0,0,0,1j]
    n2,n1=mnl(vcVelocity),[0]*(N-1)+[1j]
    nm=mnl(n1+n2)
    E=sf.kzrs(N,N)**0;
    #return (E+2*n2**n2)*(E+2*nm**nm)
    lenAt=sf.norm(vcVelocity[:-1]+(0,))
    # bug: signs of imaginary part were flipped 2013.10.30 
    #print "lenAt:",lenAt
    if lenAt == 1:
        assert False,("You set light velocity for the parameter:"
                     +str(vcVelocity[:-1]+(0,)))
    else:
        return (E+2*nm**nm)*(E+2*n2**n2)

def Lvn(vcVelocity):
    """' Return normal Lorentz boost tensor. not Minkowski space
    '"""
    # implementing by diadic
    if isinstance(vcVelocity,(int,float)):
        vcVelocity = (vcVelocity,1j)
    else:
        vcVelocity = tuple(vcVelocity)+(1j,)
    #assert sf.norm(vcVelocity[:-1]) < 1
    N=len(vcVelocity)

    n2,n1=mnl(vcVelocity),[0]*(N-1)+[1j]
    nm=mnl(n1+n2)
    E=sf.kzrs(N,N)**0;
    mt=(E+2*nm**nm)*(E+2*n2**n2)
    dg=sf.diag([1]*(N-1)+[1j])
    lenAt=sf.norm(vcVelocity[:-1]+(0,))
    #print "lenAt:",lenAt
    if lenAt < 1:
        return (dg.d*mt*dg).real
    elif lenAt > 1:
        return (dg.d*mt*dg)
    else:
        assert False,("You set light velocity for the parameter:"
                     +str(vcVelocity[:-1]+(0,)))

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
