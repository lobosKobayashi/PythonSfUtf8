# -*- encoding: utf-8 -*-
from __future__ import division
"""'
english:
    PythonSf pysf/customize.py
    https://github.com/lobosKobayashi
    http://lobosKobayashi.github.com/
    
    Copyright 2016, Kenji Kobayashi
    All program codes in this file was designed by kVerifierLab Kenji Kobayashi

    I release souce codes in this file under the GPLv3
    with the exception of my commercial uses.

    2016y 12m 28d Kenji Kokbayashi

japanese:
    PythonSf pysf/customize.py
    https://github.com/lobosKobayashi
    http://lobosKobayashi.github.com/
    http://lobosKobayashi.github.com/

    Copyright 2016, Kenji Kobayashi
    このファイルの全てのプログラム・コードは kVerifierLab 小林憲次が作成しました。
    
    作成者の小林本人に限っては商用利用を許すとの例外条件を追加して、
    このファイルのソースを GPLv3 で公開します。

    2016年 12月 28日 小林憲次
'"""

from kre import krgl
import kre
import sfFnctns as sf
import tlRcGn as tn
import octn as oc
from pprint import pprint as k__bq_print___          # `print
#import kmayavi as mv
from kmayavi import *

#import pdb; pdb.set_trace()

info=sf.np.info
source=sf.np.source

# `π: 
k__bq__sPi____ = 3.1415926535897931                 #@:`π --> k__bq__sPi_x___
# degree = 2`π/360 and radian
k_degree_bq____ = 0.0174532925199                   #@:degree` --> 
k_rad_bq____ = 1                                    #@:rad` --> 

#=========== Pauli 行列:`σx `σy `σz, Levi-Civitaテンソル `ε begin ========
# `σx: 
k__bq__sSigma_x___ = sf.kzrs([2,2], float) #@:`σx --> k__bq__sSigma_x___
sf.sc.ravel(k__bq__sSigma_x___)[1:3]=[1.0, 1.0]

k__bq__sSigma_y___ = sf.kzrs([2,2], complex) #@:`σy --> k__bq__sSigma_y___
sf.sc.ravel(k__bq__sSigma_y___)[1:3]=[-1j, 1j]

k__bq__sSigma_z___ = sf.kzrs([2,2], float) #@:`σz --> k__bq__sSigma_z___
sf.sc.ravel(k__bq__sSigma_z___)[:]=[1.0, 0.0, 0.0, -1.0]

k__bq__sEpsilon_L___ = sf.kzrs([3,3,3], float) #@:`εL --> k__bq__sEpsilon_L___
k__bq__sEpsilon_L___[0,1,2] =  1
k__bq__sEpsilon_L___[0,2,1] = -1
k__bq__sEpsilon_L___[1,0,2] = -1
k__bq__sEpsilon_L___[1,2,0] =  1
k__bq__sEpsilon_L___[2,0,1] =  1
k__bq__sEpsilon_L___[2,1,0] = -1
#=========== Pauli 行列:`σx `σy `σz, Levi-Civitaテンソル `ε end ========

#=========== 微分 ∂x ∂y ∂z ∂t ∂p ∂p ∂2x ∂2y ∂2z ∂2t=====
#                 `dx `dy `dz `dt         `d2x `d2y `d2z `d2t
#=========== `div, ∇, △ Jacobian:∂J          begin=============
def __k_P0__(fnAg):
    if False:
        pass
    else:
        return sf.P_(0,fnAg)
def __k_P1__(fnAg):
    if False:
        pass
    else:
        return sf.P_(1,fnAg)

def __k_P2__(fnAg):
    if False:
        pass
    else:
        return sf.P_(2,fnAg)

def __k_Pt__(fnAg):
    if False:
        pass
    else:
        return sf.Pt_(fnAg)


def __k_Pp__(fnAg):
    if False:
        pass
    else:
        return sf.P_(0,fnAg)
def __k_Pq__(fnAg):
    if False:
        pass
    else:
        return sf.P_(1,fnAg)



def __k_P20__(fnAg):
    if False:
        pass
    else:
        return sf.P_(0, sf.P_(0,fnAg) )
def __k_P21__(fnAg):
    if False:
        pass
    else:
        return sf.P_(1, sf.P_(1,fnAg) )
def __k_P22__(fnAg):
    if False:
        pass
    else:
        return sf.P_(2, sf.P_(2,fnAg) )


def __k_P2t__(fnAg):
    if False:
        pass
    else:
        return sf.Pt_(sf.Pt_(fnAg) )

def __k_Nabla__(fnAg, **dctAg):
    if False:
        pass
    else:
        return sf.Nl_(fnAg, **dctAg)

k__Nabla____ = __k_Nabla__  # sf.Nl_ or __k_Nabla      # ∇
k__bq_grad___ = __k_Nabla__ # sf.Nl_ or __k_Nabla      # `grad

def __k_div__(fnAg):
        return lambda *posAg:sf.Jc_(fnAg)(*posAg).trace()

k__bq_div___ = __k_div__     # `div


def __k_Laplacian__(fnAg):
    if False:
        pass
    else:
        return sf.Dv_(sf.Nl_(fnAg))

k__Round_x___ = __k_P0__        # ∂x
k__Round_y___ = __k_P1__        # ∂y
k__Round_z___ = __k_P2__        # ∂z
k__Round_t___ = __k_Pt__        # ∂t   differentiate for last argment
k__bq_dx___   = __k_P0__        # `dx
k__bq_dy___   = __k_P1__        # `dy
k__bq_dz___   = __k_P2__        # `dy
k__bq_dt___   = __k_Pt__        # `dt   differentiate for last argment


k__Round_p___ = __k_Pp__        # ∂p
k__Round_q___ = __k_Pq__        # ∂q

k__Round_2x___ = __k_P20__      # ∂2x
k__Round_2y___ = __k_P21__      # ∂2y
k__Round_2z___ = __k_P22__      # ∂2y
k__Round_2t___ = __k_P2t__      # ∂2t  differentiate for last argment
k__bq_d2x___   = __k_P20__      # `d2x
k__bq_d2y___   = __k_P21__      # `d2y
k__bq_d2z___   = __k_P22__      # `d2y
k__bq_d2t___   = __k_P2t__      # `d2t   differentiate for last argment

k__Round_J___ = sf.Jc_          # ∂J Jacobian

k__Laplacian____ = __k_Laplacian__
k__bq_Laplacian___ = __k_Laplacian__

k__bq_rot___ = lambda fVct,**kwAg: (lambda *pos: k__Round_J___(fVct,**kwAg)(*pos)     # `rot
                                        -(k__Round_J___(fVct,**kwAg)(*pos)).T)
#=========== 微分 ∂x ∂y ∂z ∂t ∂p ∂p ∂2x ∂2y ∂2z ∂2t=====
#                 `dx `dy `dz `dt         `d2x `d2y `d2z `d2t
#=========== `div, ∇, △ Jacobian:∂J           end =============

# Can't use x^y-y^x because the priority of operator is ^ < -
k__tilda__UsOp_xor____ = lambda x,y:(x*y) - (y*x)   #  x ~^ y

k__tilda__UsOp_add____ = lambda x,y:x*y/(x + y)     #  x ~+ y
pAdd                    = lambda x,y:x*y/(x + y)     #  x ~+ y
#<== R ~+ 1/(s C) ≡( R ~+ 1)/(s C) になるのならば、無いほうがまし
#   <== 09.11.10 user operator は四則演算・べき乗より優先すると割り切る

def k__bq__lLambda____(*tplVctAg):  #`Λ(v0,v1,v2,..) edge product
    """' return Wedge product tensor for vectors
    '"""
    def getTensor(tplIndex, *tplVctAg):
        kryAt = sf.krry(tplVctAg[tplIndex[0]])
        for i in range(1, len(tplIndex)):
            kryAt = kryAt ^ sf.krry(tplVctAg[tplIndex[i]])
        return kryAt

    n = len(tplVctAg)
    
    # confirm that all elements in tplVctAg are same length vector
    lenAt = len(tplVctAg[0])
    for k in range(n):
        assert lenAt == len(tplVctAg[k])

    krryAt = sf.kzrs(*([len(tplVctAg[0])]*n))
    for index, sign in sf.permutate(range(n),1):
        krryAt = krryAt + sign * getTensor(index, *tplVctAg)

    return krryAt

"""'
`1z: 1/z :== ClRtnl(1,[1,0])    <== use z_ in sf.py
'"""





k__bq_i___ = 1j             # `i: imaginary unit
k__bq_0___ = oc.BF(0)       # Bool 0: `0
k__bq_1___ = oc.BF(1)       # Bool 1: `1











#z_ = oc.Pm([oc.BF(1),oc.BF(0)])
#z_ = oc.Pm([1, 0], variable='z_')
class Z_(oc.Pm):
    """' BF:Bool Field 1/z polynomial '"""
    def __init__(self, *sqAg):
        #oc.Pm.__init__(self, *sqAg, dtype = oc.BF, variable='z_')
        oc.Pm.__init__(self, dtype = oc.BF, variable='z_', *sqAg)

z_ = Z_([1,0])

#class ZZ(oc.Pl):
class PB(oc.Pl):
    """' BF:Bool Field `P polynomial '"""
    def __init__(self, *sqAg):
        oc.Pl.__init__(self, dtype = oc.BF, variable='`P', *sqAg)
        #oc.Pl.__init__(self, dtype = oc.BF, variable='`Z', *sqAg)

k__bq_P___ = PB(1,0)
#k__bq_P___ = ZZ(1,0)
#k__bq_Z___ = ZZ(1,0)


#k__bq_1z___ = sf.ClRtnl(1,[1,0])   # z_ = ClRtnl(1,[1,0]) is defined in sf.py
k__bq_s___ = sf.ClRtnl([1,0],1)     #`s: s of Laplace transformation

# 一次 ClAF 関数 `X:こんな計算を可能にする;; (`X^2+3`X-1)(2) == 9.0
#k__bq_X___   = sf.ClAF(sf.sc.frompyfunc(lambda x:x, 1,1))     # `X
#k__bq_X___   = sf.ClAF(lambda x: x)     # `X
#k__bq_X___   = sf.ClAF(k__bq_s___)     # `X
#k__bq_X___   = sf.ClAF(sf.ClRtnl([1,0],1, variable='x'))     # `X
#k__bq_X___   = sf.ClAFX(sf.ClRtnl([1,0],1, variable='X'))     # `X
#k__bq_Y___   = sf.ClAFX(sf.ClRtnl([1,0],1, variable='Y'),posAg__=1)     # `Y
#k__bq_Z___   = sf.ClAFX(sf.ClRtnl([1,0],1, variable='Z'),posAg__=2)     # `Z
#k__bq_T___   = sf.ClAFX(sf.ClRtnl([1,0],1, variable='T'),posAg__=-1)    # `T
#k__bq_X___   = sf.ClAFX(sf.ClAF(lambda x:x))                            # `X
#k__bq_Y___   = sf.ClAFX(sf.ClAF(lambda y:y),             posAg__=1)     # `Y
#k__bq_Z___   = sf.ClAFX(sf.ClAF(lambda z:z),             posAg__=2)     # `Z
#k__bq_T___   = sf.ClAFX(sf.ClAF(lambda t:t),            posAg__=-1)     # `T
k__bq_X___   = sf.ClAFX(       (lambda x:x))                            # `X
k__bq_Y___   = sf.ClAFX(       (lambda y:y),             posAg__=1)     # `Y
k__bq_Z___   = sf.ClAFX(       (lambda z:z),             posAg__=2)     # `Z
k__bq_T___   = sf.ClAFX(       (lambda t:t),            posAg__=-1)     # `T

XX   = sf.ClAFXX(lambda x:x)                            # XX
#import kmayavi as mv

def ts_():
    import sympy as ts
    import symIntf as ut     # ;;pd sympy.physics.units

    # f`:femto
    k_f_bq____ = ts.Rational(1,1000000000000000)        #@:f` --> 1e-15
    # p`:pico
    k_p_bq____ = ts.Rational(1,1000000000000)           #@:p` --> 1e-12
    # n`:nano                                                       
    k_n_bq____ = ts.Rational(1,1000000000)              #@:n` --> 1e-9
    # `μ:micro                                                     
    k_u_bq____ = ts.Rational(1,1000000)                 #@:u` --> 1e-6
    # mili`:mili
    k_mili_bq____ = ts.Rational(1,1000)                 #@:mili` --> 1e-3
    # `k:kilo
    k_k_bq____ =             1000                       #@:k` --> 1e3
    # M`:Mega                                                       
    k_M_bq____ =             1000000                    #@:M` --> 1e6
    # G`:Giga                                                       
    k_G_bq____ =             1000000000                 #@:G` --> 1e9

    # Time ps`=1e-12, ns`=1e-9, us`=1e-6, ms`=1e-3, minute`=60, hour`=3600
    k_hour_bq____ = 3600*ut.s                           #@:hour` -->
    k_minute_bq____ = 60*ut.s                           #@:minute` -->
    k_s_bq____ = 1*ut.s                                 #@:s` -->
    k_ms_bq____ = ts.Rational(1,1000)*ut.s              #@:ms` --> 1e-3 sec
    k_us_bq____ = ts.Rational(1,1000000)*ut.s           #@:us` --> 1e-6 sec
    k_ns_bq____ = ts.Rational(1,1000000000)* ut.s       #@:ns` --> 1e-9 sec
    k_ps_bq____ = ts.Rational(1,1000000000000)* ut.s    #@:ps` --> 1e-12 sec

    # mass
    k_kg_bq____ = 1 * ut.kg                             #@:kg` -->    1 kg
    k_gram_bq____ = ts.Rational(1,1000)* ut.kg          #@: g` --> 1e-3 gram

    # length nm`=1e-9, um`=1e-6, mm`=1e-3, cm`=1e-2, meter`=1, `km=1e+3
    k_nm_bq____ = ts.Rational(1,1000000000) * ut.m      #@:nm` --> 1e-9: nm
    k_um_bq____ = ts.Rational(1,1000000) * ut.m         #@:um` --> 1e-6: um
    k_mm_bq____ = ts.Rational(1,1000) * ut.m            #@:mm` --> 1e-3: mm
    k_cm_bq____ = ts.Rational(1,100) * ut.m             #@:cm` --> 1e-2: cm
    k_m_bq____ = 1 * ut.m                               #@:m` -->
    k_meter_bq____ = 1 * ut.m                           #@:meter` -->
    k_metre_bq____ = 1 * ut.m                           #@:metre` -->
    k_km_bq____ = 1000                * ut.m            #@:km` --> 1e3
    # 米国単位
    k_inch_bq____ = 0.0254 * ut.m                       #@:inch` -->
    k_feet_bq____ = 0.3048 * ut.m                       #@:feet` -->
    k_mile_bq____ = 1609.3 * ut.m                       #@:mile` -->


    # C`:Coulomb 電荷
    k_C_bq____ = 1 * ut.C                               #@:C` -->

    # A`:ampere 電流
    k_A_bq____ = 1 * ut.A                               #@:A` --> k__bq_A___
    k_mA_bq____ = ts.Rational(1,1000)       * ut.A      #@:mA` --> 1e-3 A
    k_uA_bq____ = ts.Rational(1,1000000)    * ut.A      #@:uA` --> 1e-6 A

    # V`:volt
    k_V_bq____ = 1 * ut.V                               #@:V` --> k__bq_V___
    k_mV_bq____ = ts.Rational(1,1000)       * ut.V      #@:mV` --> 1e-3

    # W`:watt
    k_W_bq____ = 1 * ut.W

    # uH: micro Henry
    k_uH_bq____ = ts.Rational(1,1000000)    * ut.H      #@:uH` --> 1e-6 H

    # F`:Farad
    k_F_bq____ = 1*ut.F                                 #@:F` --> k__bq_F___
    k_uF_bq____ = ts.Rational(1,1000000)    *ut.F       #@:uF` -->1e-6 F
    k_pF_bq____ = ts.Rational(1,1000000000000) * ut.F   #@:pF` -->1e-12 F

    # T`:Tesla
    k_T_bq____ = 1*ut.V*ut.s /ut.m**2

    k__lOmega__bq____ = 1 * ut.ohm                      #@:Ω` -->   1 Ω
    k_k_lOmega__bq____ = 1000               *ut.ohm     #@:kΩ` -->1e3 kΩ
    k_ohm_bq____ = 1*ut.ohm                             #@:ohm` -->  1 ohm


    # Hz`:Herz
    k_Hz_bq____ = 1 / ut.s                              #@:Hz` --> 


    # 力学 N`:newton, dyne`:dyne, J`:Joule
    k_N_bq____ = 1 * ut.N                               #@:N` --> 
    k_J_bq____ = 1 * ut.J                               #@:J` --> 

    # light meter 光メーター 光が 1meter を通過する時間
    k_mLght_bq____ = 1j*ut.m                           #@:mLght` --> 
    # lMeter` は使えない。 3lMeter と書いたとき 3L*Meter:long int 3 * Meter と
    # sfPPrcssr.py が解釈してしまう

    # kelvin unit
    k_K_bq____ = 1 * ut.K                               #@:K`:kelvin --> 

    # J`/s`/W`: unit conversion
    k_jsw_bq____ = k_J_bq____ / k_s_bq____ / k_W_bq____

    #=========== 物理定数 begin ==================================
    # light velosity m/s
    k_c_bq____ = 2.99792458e+8 * ut.m / ut.s            #@:c` --> k__bq__c___

    # プランク定数 h/2π 1.054571628(53)×10-34 J s 
    k_h_bq__bq____ = 1.054571628e-34 * ut.J * ut.s      #@:h`` --> h/(2π)
    k_h_bq____ = 6.62606896e-034 * ut.J * ut.s          #@:h` -->


    #ボルツマン定数   J K^-1。 K は絶対温度の単位です。 Joule/Kelvin
    k_kB_bq____ = 1.380662e-23 * ut.J / ut.K            #@:kB` -->

    #万有引力定数 gU` = 6.67259 ×10-11  N` m`^2 `kg-2 
    k_gU_bq____ = 6.67259e-11 * ut.N * ut.m**2 / ut.kg**2 #@:gU` -->
    #重力加速度 gH`  = 9.80665  m s-2 
    k_gH_bq____ = 9.80665 * ut.m / ut.s**2              #@:gH` -->

    #素電荷 pQ`  = 1.6021892 ×10-19  C, eQ`=-pQ` 
    k_eQ_bq____ = -1.6021892e-19 * ut.C
    k_pQ_bq____ = 1.6021892e-19 * ut.C
    #電子質量 eM`  = 9.10938188 ×10^-31  kg 
    k_eM_bq____ = 9.10938188e-31 * ut.kg
    #陽子質量 pM`  = 1.67262157 ×10^-27  kg 
    k_pM_bq____ = 1.67262157e-27 * ut.kg
    #水素原子質量 HM` = 1.6735 ×10^-27  kg 
    k_HM_bq____ = 1.6735e-27 * ut.kg
    #モル数,Avogadro 数　 NA`  = 6.02214199 ×10^23  mol-1
    k_NA_bq____ = 6.02214199e+23 / ut.mol
    #モル体積 Vm`  = 2.241383 ×10-2  m3mol-1 
    k_Vm_bq____ = 2.241383e-2 * ut.m**3 / ut.mol

    #真空の透磁率 1.2566370614E-06 == 4`π 1e-7, 物理単位 N` A`^-2 == henry/meter == weber/(ampere meter)
    k__sMu_0_bq____ = 1.2566370614e-6 * ut.H/ut.m        #@μ0` -->
    k_u0_bq____ = 1.2566370614e-6 *ut.H/ut.m
    k_U0_bq____ = k_u0_bq____ * k_c_bq____ **2           # U0` ≡ u0` c`^2
    # 真空の誘電率 ε0 == 1/(`c^2 4`π 1e-7)==クーロン**2 / (newton * M ** 2) == farad/meter == coulomb/(volt meter)
    k__sEpsilon_0_bq____ = 8.854187816e-12 * ut.F/ut.m  #@:ε0` -->
    k_e0_bq____ = 8.854187816e-12 * ut.F/ut.m

    #ボルツマン定数   J K^-1 K は絶対温度の単位です。Kg ではありません
    k_kB_bq____  = 1.380662e-23 * ut.J/ut.K     # Joule/ kelvin degree
    #=========== 物理定数 end = ==================================

    #=========== 微分 ∂x ∂y ∂z ∂t ∂p ∂p ∂2x ∂2y ∂2z ∂2t=====
    #                 `dx `dy `dz `dt         `d2x `d2y `d2z `d2t
    #=========== `div, ∇, △ Jacobian:∂J          begin=============
    def __k_P0__(fnAg):
        if (  isinstance(fnAg, ts.Basic)
              or isinstance(fnAg, ts.Add)
              or isinstance(fnAg, ts.Mul)
              or (hasattr(fnAg, 'is_Function') and fnAg.is_Function()) 
              or (hasattr(fnAg, 'is_Pow') and fnAg.is_Pow())
        ):
            return      (ts.diff(fnAg, k__bq_x___))
        else:
            return sf.P_(0,fnAg)
    def __k_P1__(fnAg):
        if ( isinstance(fnAg, ts.Basic)
          or isinstance(fnAg, ts.Add)
          or isinstance(fnAg, ts.Mul)
          or (hasattr(fnAg, 'is_Function') and fnAg.is_Function()) 
          or (hasattr(fnAg, 'is_Pow') and fnAg.is_Pow())
        ):
            return      (ts.diff(fnAg, k__bq_y___))
        else:
            return sf.P_(1,fnAg)

    def __k_P2__(fnAg):
        if ( isinstance(fnAg, ts.Basic)
          or isinstance(fnAg, ts.Add)
          or isinstance(fnAg, ts.Mul)
          or (hasattr(fnAg, 'is_Function') and fnAg.is_Function()) 
          or (hasattr(fnAg, 'is_Pow') and fnAg.is_Pow())
        ):
            return      (ts.diff(fnAg, k__bq_z___))
        else:
            return sf.P_(2,fnAg)

    def __k_Pt__(fnAg):
        if ( isinstance(fnAg, ts.Basic)
          or isinstance(fnAg, ts.Add)
          or isinstance(fnAg, ts.Mul)
          or (hasattr(fnAg, 'is_Function') and fnAg.is_Function()) 
          or (hasattr(fnAg, 'is_Pow') and fnAg.is_Pow())
        ):
            return      (ts.diff(fnAg, k__bq_t___))
        else:
            return sf.Pt_(fnAg)


    def __k_Pp__(fnAg):
        if ( isinstance(fnAg, ts.Basic)
          or isinstance(fnAg, ts.Add)
          or isinstance(fnAg, ts.Mul)
          or (hasattr(fnAg, 'is_Function') and fnAg.is_Function()) 
          or (hasattr(fnAg, 'is_Pow') and fnAg.is_Pow())
        ):
            return      (ts.diff(fnAg, k__bq_p___))
        else:
            return sf.P_(0,fnAg)
    def __k_Pq__(fnAg):
        if ( isinstance(fnAg, ts.Basic)
          or isinstance(fnAg, ts.Add)
          or isinstance(fnAg, ts.Mul)
          or (hasattr(fnAg, 'is_Function') and fnAg.is_Function()) 
          or (hasattr(fnAg, 'is_Pow') and fnAg.is_Pow())
        ):
            return      (ts.diff(fnAg, k__bq_q___))
        else:
            return sf.P_(1,fnAg)



    def __k_P20__(fnAg):
        if ( isinstance(fnAg, ts.Basic)
          or isinstance(fnAg, ts.Add)
          or isinstance(fnAg, ts.Mul)
          or (hasattr(fnAg, 'is_Function') and fnAg.is_Function()) 
          or (hasattr(fnAg, 'is_Pow') and fnAg.is_Pow())
        ):
            return ts.diff( ts.diff(fnAg, k__bq_x___), k__bq_x___ )
        else:
            return sf.P_(0, sf.P_(0,fnAg) )
    def __k_P21__(fnAg):
        if ( isinstance(fnAg, ts.Basic)
          or isinstance(fnAg, ts.Add)
          or isinstance(fnAg, ts.Mul)
          or (hasattr(fnAg, 'is_Function') and fnAg.is_Function()) 
          or (hasattr(fnAg, 'is_Pow') and fnAg.is_Pow())
        ):
            return ts.diff( ts.diff(fnAg, k__bq_y___), k__bq_y___ )
        else:
            return sf.P_(1, sf.P_(1,fnAg) )
    def __k_P22__(fnAg):
        if ( isinstance(fnAg, ts.Basic)
          or isinstance(fnAg, ts.Add)
          or isinstance(fnAg, ts.Mul)
          or ( hasattr(fnAg, 'is_Function') and fnAg.is_Function()) 
          or ( hasattr(fnAg, 'is_Pow') and fnAg.is_Pow())
        ):
            return ts.diff( ts.diff(fnAg, k__bq_z___), k__bq_z___ )
        else:
            return sf.P_(2, sf.P_(2,fnAg) )


    def __k_P2t__(fnAg):
        if ( isinstance(fnAg, ts.Basic)
          or isinstance(fnAg, ts.Add)
          or isinstance(fnAg, ts.Mul)
          or (hasattr(fnAg, 'is_Function') and fnAg.is_Function()) 
          or (hasattr(fnAg, 'is_Pow') and fnAg.is_Pow())
        ):
            return ts.diff( ts.diff(fnAg, k__bq_t___), k__bq_t___ )
        else:
            return sf.Pt_(sf.Pt_(fnAg) )

    def __k_Nabla__(fnAg,**dctAg):
        if ( isinstance(fnAg, ts.Basic)
          or isinstance(fnAg, ts.Add)
          or isinstance(fnAg, ts.Mul)
          or (hasattr(fnAg, 'is_Function') and fnAg.is_Function) 
          or (hasattr(fnAg, 'is_Pow') and fnAg.is_Pow)
        ):
            if fnAg.has_all_symbols(k__bq_x___, k__bq_y___, k__bq_z___):
                return (__k_P0__(fnAg), __k_P1__(fnAg), __k_P2__(fnAg) )
            elif fnAg.has_all_symbols(k__bq_x___, k__bq_y___):
                return (__k_P0__(fnAg), __k_P1__(fnAg))
            elif fnAg.has_all_symbols(k__bq_p___, k__bq_q___):
                return (__k_Pp__(fnAg), __k_Pq__(fnAg))
            else:
                assert False, ("At Nabla, function argments ar not  x,y or,"
                              +" x,y,z :" + str(fnAg) )
        else:
            return sf.nl_(fnag, **dctag)

    k__Nabla____ = __k_Nabla__  # sf.Nl_ or __k_Nabla      # ∇
    k__bq_grad___ = __k_Nabla__ # sf.Nl_ or __k_Nabla      # `grad

    def __k_div__(fnAg):
        assert len(fnAg) == 2 or len(fnAg) == 3,("At div, you set unexpected "
                                            + "argment:" + str(fnAg))
        if ( isinstance(fnAg[0], ts.Basic)
          or isinstance(fnAg[0], ts.Add)
          or isinstance(fnAg[0], ts.Mul)
          or (hasattr(fnAg[0], 'is_Function') and fnAg[0].is_Function()) 
          or (hasattr(fnAg[0], 'is_Pow') and fnAg[0].is_Pow())
        ):
            if len(fnAg) == 3:
                if fnAg[0].has_all_symbols(k__bq_x___, k__bq_y___, k__bq_z___):
                    return __k_P0__(fnAg[0])+ __k_P1__(fnAg[1])+ __k_P2__(fnAg[2])
                else:
                    assert False, ("At div, you set unexpected "
                                            + "argment:" + str(fnAg))
            else:
                if fnAg[0].has_all_symbols(k__bq_x___, k__bq_y___):
                    return __k_P0__(fnAg[0])+ __k_P1__(fnAg[1])
                elif fnAg[0].has_all_symbols(k__bq_p___, k__bq_q___):
                    return __k_Pp__(fnAg[0])+ __k_Pq__(fnAg[1])
                else:
                    assert False, ("At div, you set unexpected "
                                            + "argment:" + str(fnAg))
        else:
            return lambda *posAg:sf.Jc_(fnAg)(*posAg).trace()
            #return sf.Dv_(fnAg)

    k__bq_div___ = __k_div__     # `div

    def __k_Laplacian__(fnAg):
        if ( isinstance(fnAg, ts.Basic)
          or isinstance(fnAg, ts.Add)
          or isinstance(fnAg, ts.Mul)
          or (hasattr(fnAg, 'is_Function') and fnAg.is_Function) 
          or (hasattr(fnAg, 'is_Pow') and fnAg.is_Pow)
        ):
            if fnAg.has_all_symbols(k__bq_x___, k__bq_y___, k__bq_z___):
                #∂x^2(f) + ∂y^2(f) + ∂z^2(f)
                return __k_P20__(fnAg) + __k_P21__(fnAg) + __k_P22__(fnAg)
            elif fnAg.has_all_symbols(k__bq_x___, k__bq_y___):
                #∂x^2(f) + ∂y^2(f)
                return __k_P20__(fnAg) + __k_P21__(fnAg)
            elif fnAg.has_all_symbols(k__bq_p___, k__bq_q___):
                #∂x^2(f) + ∂y^2(f)
                return __k_P2p__(fnAg) + __k_P21__(fnAg)
            else:
                assert False, ("At Laplacian, function argments ar not  x,y or,"
                              +" x,y,z :" + str(fnAg) )
        else:
            return sf.Dv_(sf.Nl_(fnAg))


    k__Round_x___ = __k_P0__        # ∂x
    k__Round_t___ = __k_Pt__        # ∂t   differentiate for last argment
    k__bq_dx___   = __k_P0__        # `dx
    k__bq_dy___   = __k_P1__        # `dy
    k__bq_dz___   = __k_P2__        # `dy
    k__bq_dt___   = __k_Pt__        # `dt   differentiate for last argment


    k__Round_p___ = __k_Pp__        # ∂p
    k__Round_q___ = __k_Pq__        # ∂q

    k__Round_2x___ = __k_P20__      # ∂2x
    k__Round_2y___ = __k_P21__      # ∂2y
    k__Round_2z___ = __k_P22__      # ∂2y
    k__Round_2t___ = __k_P2t__      # ∂2t  differentiate for last argment
    k__bq_d2x___   = __k_P20__      # `d2x
    k__bq_d2y___   = __k_P21__      # `d2y
    k__bq_d2z___   = __k_P22__      # `d2y
    k__bq_d2t___   = __k_P2t__      # `d2t   differentiate for last argment

    k__Round_J___ = sf.Jc_          # ∂J Jacobian

    k__Laplacian____ = __k_Laplacian__
    k__bq_Laplacian___ = __k_Laplacian__


    #=========== 微分 ∂x ∂y ∂z ∂t ∂p ∂p ∂2x ∂2y ∂2z ∂2t=====
    #                 `dx `dy `dz `dt         `d2x `d2y `d2z `d2t
    #=========== `div, ∇, △ Jacobian:∂J           end =============

    #================= sympy related begin ==============================

    k__bq_1r___ = ts.Rational(1)       # `1r ≡ `Rat(1)
    k__bq_Rat___ = ts.Rational  # `Rat(..) rational number

#    k__bq_i___ = 1j             # `i: imaginary unit
#    k__bq_0___ = oc.BF(0)       # Bool 0
#    k__bq_1___ = oc.BF(1)       # Bool 1


    k__bq_x___=ts.Symbol('x')   #`x variale
    k__bq_y___=ts.Symbol('y')   #`y variale
    k__bq_z___=ts.Symbol('z')   #`z variale
    k__bq_n____=ts.Symbol('n')  #`n_ variale

    k__bq_p___=ts.Symbol('p')   #`p variale
    k__bq_q___=ts.Symbol('q')   #`q variale
    k__bq_t___=ts.Symbol('t')   #`t variale

    def Float(*tplAg):
        #import pdb; pdb.set_trace()
        assert len(tplAg) > 0
        if len(tplAg)==1 and isinstance(
                                    tplAg[0], (bool, int, long, float,complex)
        ):
            return tplAg[0]

        assert ( isinstance(tplAg[0], ts.Add) 
              or isinstance(tplAg[0], ts.Mul) 
              or tplAg[0].is_Function 
              or tplAg[0].is_Number
              or tplAg[0].is_Pow )

        fnAt = tplAg[0]
        tplAg = tplAg[1:]
        if len(tplAg)==0 or  not(
                   isinstance(fnAt, ts.Add) or isinstance(fnAt, ts.Mul)
                or (fnAt.is_Function) or (fnAt.is_Pow)
                              ):
            #return float(fnAt)
            if isinstance(fnAt, (ts.Number, ts.Rational) ):
                return float(fnAt)
            else:
                assert isinstance(fnAt, ts.Mul)
                # covert V to m**2*kg/(A*s**3)
                compensatingUnitAt = 1
                for elmAt in fnAt.args:
                    if elmAt == ut.V:
                        compensatingUnitAt =(
                                 compensatingUnitAt*(ut.m**2*ut.kg
                                                        /(ut.A*ut.s**3)
                                                    )/ut.V 
                                            )
                    elif isinstance(elmAt, ts.Pow):
                        if elmAt.args[0] == ut.V:
                            powNumAt = elmAt.args[1]
                            compensatingUnitAt = (compensatingUnitAt
                                     *((ut.m**2*ut.kg/(ut.A*ut.s**3))**powNumAt)
                                     *(ut.V**-powNumAt)
                                                 )
                if compensatingUnitAt == 1:
                    assert False, ("At Float(.), you set physical quantity"
                                  +" parameter"
                                  +",the units of which are not cancelled:"
                                  + str(fnAt)
                                  ) 
                else:
                    valAt = fnAt * compensatingUnitAt
                    assert isinstance(valAt, ts.Number),("At Float(.)"
                                + " you set physical quantity parameter"
                                +",the units of which are not cancelled:"
                                + str(valAt)
                                                        )

                    return float(valAt)

        else:
            varAt=(k__bq_p___, k__bq_q___
                  ,k__bq_t___, k__bq_x___, k__bq_y___, k__bq_z___)

            if len(tplAg)==1:
                for lstElm in sf.combinate(varAt,1):
                    if fnAt.has_any_symbols(lstElm[0]):    # has 'x' name symbol ?
                        if isinstance(fnAt, ts.Mul):
                            # e.g. `x^2/2+`x+1, ....
                            return reduce(lambda a,b:a*b,
                                    [float(elm.subs(lstElm[0], tplAg[0]))
                                            for elm in fnAt._args])

                        else:
                            # e.g. Float(fn(`x), 0.5) or Float(fn(`x/2), 1) , ...
                            return float(fnAt.subs(lstElm[0], tplAg[0]))


                assert False, str(fnAt) + (" dosen't have any symbol:x,y,z,t,p,q,"
                                         + " variable.")

            elif len(tplAg)==2:
                for lstElm in sf.combinate(varAt,2):
                    if ( fnAt.has_any_symbols(lstElm[0]) # has 'x,y' name symbol ?
                     and fnAt.has_any_symbols(lstElm[1])
                       ):
                        if isinstance(fnAt, ts.Mul):
                            # e.g. `x^2/2+`x+1, ....
                            return reduce(lambda a,b:a*b,
                                    [float( elm.subs([(lstElm[0], tplAg[0])
                                                     ,(lstElm[1], tplAg[1])]) )
                                            for elm in fnAt._args])

                        else:
                            # e.g. Float(fn(`x), 0.5) or Float(fn(`x/2), 1) , ...
                            return float(fnAt.subs([(lstElm[0], tplAg[0])
                                                   ,(lstElm[1], tplAg[1])]))


                assert False, str(fnAt) + (" dosen't have any symbol:x,y,z,t,p,q,"
                                         + " variable pair.")

            elif len(tplAg)==3:
                for lstElm in sf.combinate(varAt,3):
                    # has 'x,y,z' name symbol ?
                    if ( fnAt.has_any_symbols(lstElm[0])
                     and fnAt.has_any_symbols(lstElm[1])
                     and fnAt.has_any_symbols(lstElm[2])
                       ):
                        if isinstance(fnAt, ts.Mul):
                            # e.g. `x^2/2+`x+1, ....
                            return reduce(lambda a,b:a*b,
                                    [float( elm.subs([(lstElm[0], tplAg[0])
                                                     ,(lstElm[1], tplAg[1])
                                                     ,(lstElm[2], tplAg[2])]) )
                                            for elm in fnAt._args])

                        else:
                            # e.g. Float(fn(`x), 0.5) or Float(fn(`x/2), 1) , ...
                            return float(fnAt.subs([(lstElm[0], tplAg[0])
                                                   ,(lstElm[1], tplAg[1])
                                                   ,(lstElm[2], tplAg[2])]))


                assert False, str(fnAt) + (" dosen't have any symbol:x,y,z,t,p,q,"
                                         + " variable triple.")

            elif len(tplAg)==4:
                for lstElm in sf.combinate(varAt,4):
                    # has 'x,y,z' name symbol ?
                    if ( fnAt.has_any_symbols(lstElm[0])
                     and fnAt.has_any_symbols(lstElm[1])
                     and fnAt.has_any_symbols(lstElm[2])
                     and fnAt.has_any_symbols(lstElm[3])
                       ):
                        if isinstance(fnAt, ts.Mul):
                            # e.g. `x^2/2+`x+1, ....
                            return reduce(lambda a,b:a*b,
                                    [float( elm.subs([(lstElm[0], tplAg[0])
                                                     ,(lstElm[1], tplAg[1])
                                                     ,(lstElm[2], tplAg[2])
                                                     ,(lstElm[3], tplAg[3])]) )
                                            for elm in fnAt._args])

                        else:
                            # e.g. Float(fn(`x), 0.5) or Float(fn(`x/2), 1) , ...
                            return float(fnAt.subs([(lstElm[0], tplAg[0])
                                                   ,(lstElm[1], tplAg[1])
                                                   ,(lstElm[2], tplAg[2])
                                                   ,(lstElm[3], tplAg[3])]))


                assert False, str(fnAt) + (" dosen't have any symbol:x,y,z,t,p,q,"
                                         + " variable quadruple.")

            elif len(tplAg)==5:
                for lstElm in sf.combinate(varAt,5):
                    # has 'x,y,z' name symbol ?
                    if ( fnAt.has_any_symbols(lstElm[0])
                     and fnAt.has_any_symbols(lstElm[1])
                     and fnAt.has_any_symbols(lstElm[2])
                     and fnAt.has_any_symbols(lstElm[3])
                     and fnAt.has_any_symbols(lstElm[4])
                       ):
                        if isinstance(fnAt, ts.Mul):
                            # e.g. `x^2/2+`x+1, ....
                            return reduce(lambda a,b:a*b,
                                    [float( elm.subs([(lstElm[0], tplAg[0])
                                                     ,(lstElm[1], tplAg[1])
                                                     ,(lstElm[2], tplAg[2])
                                                     ,(lstElm[3], tplAg[3])
                                                     ,(lstElm[4], tplAg[4])]) )
                                            for elm in fnAt._args])

                        else:
                            # e.g. Float(fn(`x), 0.5) or Float(fn(`x/2), 1) , ...
                            return float(fnAt.subs([(lstElm[0], tplAg[0])
                                                   ,(lstElm[1], tplAg[1])
                                                   ,(lstElm[2], tplAg[2])
                                                   ,(lstElm[3], tplAg[3])
                                                   ,(lstElm[4], tplAg[4])]))


                assert False, str(fnAt) + (" dosen't have any symbol:x,y,z,t,p,q,"
                                         + " variable quintuple.")

            elif len(tplAg)==6:
                # has 'p,q, x,y,z' name symbol ?
                if ( fnAt.has_any_symbols(varAt[0])
                 and fnAt.has_any_symbols(varAt[1])
                 and fnAt.has_any_symbols(varAt[2])
                 and fnAt.has_any_symbols(varAt[3])
                 and fnAt.has_any_symbols(varAt[4])
                 and fnAt.has_any_symbols(varAt[5])
                   ):
                    if isinstance(fnAt, ts.Mul):
                        # e.g. `x^2/2+`x+1, ....
                        return reduce(lambda a,b:a*b,
                                [float( elm.subs([(varAt[0], tplAg[0])
                                                 ,(varAt[1], tplAg[1])
                                                 ,(varAt[2], tplAg[2])
                                                 ,(varAt[3], tplAg[3])
                                                 ,(varAt[4], tplAg[4])
                                                 ,(varAt[5], tplAg[5])]) )
                                        for elm in fnAt._args])

                    else:
                        # e.g. Float(fn(`x), 0.5) or Float(fn(`x/2), 1) , ...
                        return float(fnAt.subs([(varAt[0], tplAg[0])
                                               ,(varAt[1], tplAg[1])
                                               ,(varAt[2], tplAg[2])
                                               ,(varAt[3], tplAg[3])
                                               ,(varAt[4], tplAg[4])
                                               ,(varAt[5], tplAg[5])]))


                assert False, str(fnAt) + (" dosen't have any symbol:x,y,z,t,p,q,"
                                     + " variable sextuple.")

            else:
                assert False, str(fnAt) + " too much argments."

    def Cmplx(*tplAg):
        #import pdb; pdb.set_trace()
        assert len(tplAg) > 0
        if len(tplAg)==1:
            if isinstance(tplAg[0], (bool, int, long, float)):
                return float(tplAg[0])
            elif isinstance(tplAg[0], complex):
                raise sf.ClAppError(
                         "You set complex argment in Float(..):"+str(tplAg[0]))

        assert ( isinstance(tplAg[0], ts.Add) 
              or isinstance(tplAg[0], ts.Mul) 
              or tplAg[0].is_Function 
              or tplAg[0].is_Pow 
              or tplAg[0].is_imaginary )

        fnAt = tplAg[0]
        tplAg = tplAg[1:]
        if len(tplAg)==0 or  not(
                   isinstance(fnAt, ts.Add) or isinstance(fnAt, ts.Mul)
                or (fnAt.is_Function) or (fnAt.is_Pow)
                              ):
            return complex(fnAt)
        elif len(tplAg)==1:
            if fnAt.has_any_symbols(k__bq_x___):
                if isinstance(fnAt, ts.Mul):
                    return reduce(lambda a,b:a*b,
                                    [complex(elm.subs(k__bq_x___, tplAg[0]))
                                            for elm in fnAt._args])
                else:
                    return sum([complex(elm.subs(k__bq_x___, tplAg[0]))
                                            for elm in fnAt._args])
            elif fnAt.has_any_symbols(k__bq_y___):
                if isinstance(fnAt, ts.Mul):
                    return reduce(lambda a,b:a*b,
                                    [complex(elm.subs(k__bq_y___, tplAg[0]))
                                            for elm in fnAt._args])
                else:
                    return sum([complex(elm.subs(k__bq_y___, tplAg[0]))
                                            for elm in fnAt._args])
            elif fnAt.has_any_symbols(k__bq_z___):
                if isinstance(fnAt, ts.Mul):
                    return reduce(lambda a,b:a*b,
                                    [complex(elm.subs(k__bq_z___, tplAg[0]))
                                            for elm in fnAt._args])
                else:
                    return sum([complex(elm.subs(k__bq_z___, tplAg[0]))
                                    for elm in fnAt._args])
            elif fnAt.has_any_symbols(k__bq_t___):
                if isinstance(fnAt, ts.Mul):
                    return reduce(lambda a,b:a*b,
                                    [complex(elm.subs(k__bq_t___, tplAg[0]))
                                            for elm in fnAt._args])
                else:
                    return sum([complex(elm.subs(k__bq_t___, tplAg[0]))
                                            for elm in fnAt._args])
            elif fnAt.has_any_symbols(k__bq_p___):
                if isinstance(fnAt, ts.Mul):
                    return reduce(lambda a,b:a*b,
                                    [complex(elm.subs(k__bq_p___, tplAg[0]))
                                            for elm in fnAt._args])
                else:
                    return sum([complex(elm.subs(k__bq_p___, tplAg[0]))
                                            for elm in fnAt._args])
            elif fnAt.has_any_symbols(k__bq_q___):
                if isinstance(fnAt, ts.Mul):
                    return reduce(lambda a,b:a*b,
                                    [complex(elm.subs(k__bq_q___, tplAg[0]))
                                            for elm in fnAt._args])
                else:
                    return sum([complex(elm.subs(k__bq_q___, tplAg[0]))
                                            for elm in fnAt._args])
            else:
                assert False, str(fnAt) + (" dosen't have any symbol:x,y,z,t,p,q,"
                                         + " variable.")
        elif len(tplAg)==2:
            if fnAt.has_any_symbols(k__bq_x___) and fnAt.has_any_symbols(k__bq_y___):
                # fn(`x,`y)
                if isinstance(fnAt, ts.Mul):
                    return reduce(lambda a,b:a*b,
                                    [complex(elm.subs([(k__bq_x___, tplAg[0])
                               , (k__bq_y___, tplAg[1])]) )for elm in fnAt._args])
                else:
                    return sum([complex(elm.subs([(k__bq_x___, tplAg[0])
                               , (k__bq_y___, tplAg[1])]) ) for elm in fnAt._args])
            elif fnAt.has_any_symbols(k__bq_x___) and fnAt.has_any_symbols(k__bq_t___):
                # fn(`x,`t)
                if isinstance(fnAt, ts.Mul):
                    return reduce(lambda a,b:a*b,
                                    [complex(elm.subs([(k__bq_x___, tplAg[0])
                               , (k__bq_t___, tplAg[1])]) )for elm in fnAt._args])
                else:
                    return sum([complex(elm.subs([(k__bq_x___, tplAg[0])
                               , (k__bq_t___, tplAg[1])]) ) for elm in fnAt._args])
            elif fnAt.has_any_symbols(k__bq_p___) and fnAt.has_any_symbols(k__bq_q___):
                # fn(`p,`q)
                if isinstance(fnAt, ts.Mul):
                    return reduce(lambda a,b:a*b,
                                    [complex(elm.subs([(k__bq_p___, tplAg[0])
                               , (k__bq_q___, tplAg[1])]) )for elm in fnAt._args])
                else:
                    return sum([complex(elm.subs([(k__bq_p___, tplAg[0])
                               , (k__bq_q___, tplAg[1])]) ) for elm in fnAt._args])
            elif fnAt.has_any_symbols(k__bq_p___) and fnAt.has_any_symbols(k__bq_t___):
                # fn(`p,`t)
                if isinstance(fnAt, ts.Mul):
                    return reduce(lambda a,b:a*b,
                                    [complex(elm.subs([(k__bq_p___, tplAg[0])
                               , (k__bq_t___, tplAg[1])]) )for elm in fnAt._args])
                else:
                    return sum([complex(elm.subs([(k__bq_p___, tplAg[0])
                               , (k__bq_t___, tplAg[1])]) ) for elm in fnAt._args])
            elif fnAt.has_any_symbols(k__bq_q___) and fnAt.has_any_symbols(k__bq_t___):
                # fn(`q,`t)
                if isinstance(fnAt, ts.Mul):
                    return reduce(lambda a,b:a*b,
                                    [complex(elm.subs([(k__bq_q___, tplAg[0])
                               , (k__bq_t___, tplAg[1])]) )for elm in fnAt._args])
                else:
                    return sum([complex(elm.subs([(k__bq_q___, tplAg[0])
                               , (k__bq_t___, tplAg[1])]) ) for elm in fnAt._args])
            else:
                assert False, str(fnAt) + (" dosen't have two symbols:(x,y), (x,t) "
                                         + ",(p,q), (p,t), (q,t) variables." )

        elif len(tplAg)==3:
            if ( fnAt.has_any_symbols(k__bq_x___)
             and fnAt.has_any_symbols(k__bq_y___)
             and fnAt.has_any_symbols(k__bq_z___)
            ):
                # fn(`x,`y,`z)
                if isinstance(fnAt, ts.Mul):
                    return reduce(lambda a,b:a*b,[complex(elm.subs(
                              [ (k__bq_x___, tplAg[0])
                              , (k__bq_y___, tplAg[1]), (k__bq_z___, tplAg[2])]) )
                                    for elm in fnAt._args])
                else:
                    return sum([complex(elm.subs([ (k__bq_x___, tplAg[0])
                                       , (k__bq_y___, tplAg[1])
                                       , (k__bq_z___, tplAg[2]) ] ) )
                            for elm in fnAt._args])

            elif ( fnAt.has_any_symbols(k__bq_x___)
             and fnAt.has_any_symbols(k__bq_y___)
             and fnAt.has_any_symbols(k__bq_t___)
            ):
                # fn(`x,`y,`t)
                if isinstance(fnAt, ts.Mul):
                    return reduce(lambda a,b:a*b,[complex(elm.subs(
                              [ (k__bq_x___, tplAg[0])
                              , (k__bq_y___, tplAg[1]), (k__bq_t___, tplAg[2])]) )
                                    for elm in fnAt._args])
                else:
                    return sum([complex(elm.subs([ (k__bq_x___, tplAg[0])
                                       , (k__bq_y___, tplAg[1])
                                       , (k__bq_t___, tplAg[2]) ] ) )
                            for elm in fnAt._args])

            elif ( fnAt.has_any_symbols(k__bq_p___)
             and fnAt.has_any_symbols(k__bq_q___)
             and fnAt.has_any_symbols(k__bq_t___)
            ):
                # fn(`p,`q,`t)
                if isinstance(fnAt, ts.Mul):
                    return reduce(lambda a,b:a*b,[complex(elm.subs(
                              [ (k__bq_p___, tplAg[0])
                              , (k__bq_q___, tplAg[1]), (k__bq_t___, tplAg[2])]) )
                                    for elm in fnAt._args])

                else:
                    return sum([complex(elm.subs([ (k__bq_p___, tplAg[0])
                                       , (k__bq_q___, tplAg[1])
                                       , (k__bq_t___, tplAg[2]) ] ) )
                            for elm in fnAt._args])
            else:
                assert False, str(fnAt) + (" dosen't have three symbols:(x,y,z),"
                                         + " (x,y,t), (p,q,t) variables." )
        else:
            assert False

    #================= sympy related end ==============================
    sf.__getDctGlobals().update(locals())
    #localsAt = locals()
    #del localsAt['ts']
    #localsAt['ts_']=ts
    #sf.__getDctGlobals().update(localsAt)

    import platform as md;
    if md.system() == "Windows":
        if ts.__version__ == "0.6.6":
            import sympy.mpmath.calculus as md
            ts.inf = md.inf
        else:
            # inf definition is moved to sympy.mpmath at sympy version 0.6.7 
            import sympy.mpmath as md
            ts.inf = md.inf

        return ts
    else:
        if ts.__version__ == "0.6.6":
            import sympy.mpmath.calculus as md
            ts.inf = md.inf
        elif ts.__version__[:3] == "0.7":
            import mpmath as md
            ts.inf = md.inf
        else:
            # inf definition is moved to sympy.mpmath at sympy version 0.6.7 
            import sympy.mpmath as md
            ts.inf = md.inf

        return ts

def ts():
    # ts_() を呼び出した後なので ts() を呼び出せない。ts_() ならば何度も呼べる。
    # 自動テストのためにも ts_() が必要
    #ts=ts_()
    #sf.__getDctGlobals()['ts']=ts
    #return ts
    return ts_()

def tr():
    # f`:femto
    k_f_bq____ = 1e-15                  #f`:1s.Rational(1,1000000000000000)
    # p`:pico
    k_p_bq____ = 1e-12                  #p`:ts.Rational(1,1000000000000)   
    # n`:nano                                                       
    k_n_bq____ = 1e-9                   #n`:ts.Rational(1,1000000000)      
    # `μ:micro                                                     
    k_u_bq____ = 1e-6                   #ts.Rational(1,1000000)            
    # mili`:mili
    k_mili_bq____ = 1e-3                #mili`:ts.Rational(1,1000)         
    # `k:kilo
    k_k_bq____ =             1000       #k`:ts.Rational(1000,1)            
    # M`:Mega                                                       
    k_M_bq____ =             1000000                    #@:M` --> 1e6
    # G`:Giga                                                       
    k_G_bq____ =             1000000000                 #@:G` --> 1e9
  

    # Time `pS @= 1e-12, `nS @= 1e-9, `uS @= 1e-6, `mS @= 1e-3,  `minute@=60,
    # `hour@=3600
    k_hour_bq____ = 3600                                #@:hour` -->
    k_minute_bq____ = 60                                #@:minute` -->
    k_s_bq____ = 1                                      #@:S` -->
    k_ms_bq____ =1e-3                                   #@:mS` --> 1e-3 sec
    k_us_bq____ =1e-6                                   #@:uS` --> 1e-6 sec
    k_ns_bq____ =1e-9                                   #@:nS` --> 1e-9 sec
    k_ps_bq____ =1e-12                                  #@:pS` --> 1e-12 sec

    # mass
    k_kg_bq____ = 1                                     #@:kg` -->
    k_gram_bq____ = 1e-3                                #@: g` --> 1e-3

    # length nm` @= 1e-9, um` @= 1e-6, mm` @= 1e-3,cm` @= 1e-2, meter` @=1, `km @= 1e+3
    k_nm_bq____ = 1e-9                                  #@:nm` --> 1e-9: nm
    k_um_bq____ = 1e-6                                  #@:um` --> 1e-6: um
    k_mm_bq____ = 1e-3                                  #@:mm` --> 1e-3: mm
    k_cm_bq____ = 1e-2                                  #@:cm` --> 1e-2: cm
    k_m_bq____ = 1                                      #@:m` -->
    k_meter_bq____ = 1                                  #@:meter` -->
    k_metre_bq____ = 1                                  #@:metre` -->
    k_km_bq____ =             1000                      #@:km` --> 1e3
    # 米国単位
    k_inch_bq____ = 0.0254                              #@:inch` -->
    k_feet_bq____ = 0.3048                              #@:feet` -->
    k_mile_bq____ = 1609.3                              #@:mile` -->


    # C`:Coulomb 電荷
    k_C_bq____ = 1                                      #@:C` -->


    # A`:ampere 電流
    k_A_bq____ = 1                                      #@:A` --> k__bq_A___
    k_mA_bq____ = 1e-3                                  #@:mA` --> 1e-3 A
    k_uA_bq____ = 1e-6                                  #@:uA` --> 1e-6 A

    # V`:volt
    k_V_bq____ = 1                                      #@:V` --> k__bq_V___
    k_mV_bq____ = 1e-3                                  #@:uV` --> 

    # W`:watt
    k_W_bq____ = 1

    # uH: micro Henry
    k_uH_bq____ = 1e-6                                  #@:uH` --> 1e-6 H

    # F`:Farad
    k_F_bq____ = 1                                      #@:F` --> k__bq_F___
    k_uF_bq____ = 1e-6                                  #@:uF` -->1e-6 F
    k_pF_bq____ = 1e-12                                 #@:pF` -->1e-12 F

    # T`:Tesla
    k_T_bq____ = 1

    k__lOmega__bq____ = 1                               #@:Ω` -->   1 Ω
    k_k_lOmega__bq____ = 1000                           #@:kΩ` -->1e3 kΩ
    k_ohm_bq____ = 1                                    #@:ohm` -->  1 ohm


    # Hz`:Herz
    k_Hz_bq____ = 1                                     #@:Hz` --> 


    # 力学 N`:newton, dyne`:dyne, J`:Joule
    k_N_bq____ = 1                                      #@:N` --> 
    k_J_bq____ = 1                                      #@:J` --> 

    # light meter 光メーター 光が 1meter を通過する時間
    k_mLght_bq____ = 1j                                #@:mLght` --> 
    # lMeter` は使えない。 3lMeter と書いたとき 3L*Meter と
    # sfPPrcssr.py が解釈してしまう

    # kelvin unit
    k_K_bq____ = 1                                      #@:K`:kelvin --> 

    # J`/s`/W`: unit conversion
    k_jsw_bq____ = 1

    #=========== 物理定数 begin ==================================
    # light velosity m/s
    k_c_bq____ = 2.99792458e+8                          #@:c` --> k__bq__c___

    # プランク定数 h/2π 1.054571628(53)×10-34 J s 
    k_h_bq__bq____ = 1.054571628e-34       #@:h`` --> h/(2π) J` s`
    k_h_bq____ = 6.62606896e-034           #@:h` -->          J` s`


    #ボルツマン定数   J K^-1 K は絶対温度の単位です。kg ではありません Joule/ degree
    k_kB_bq____ = 1.380662e-23             #@:kB` --> * ut.J / ut.K

    #万有引力定数 gU` = 6.67259 ×10-11 N` m`^2 `kg-2 
    k_gU_bq____ = 6.67259e-11              #* ut.N * ut.m**2 / ut.kg**2 #@:gU` -->
    #重力加速度 gH`  = 9.80665 m s-2 
    k_gH_bq____ = 9.80665                  #* ut.m / ut.s**2              #@:gH` -->

    #素電荷 pQ`  = 1.6021892 ×10-19  C, eQ`=-pQ` 
    k_eQ_bq____ = -1.6021892e-19
    k_pQ_bq____ = 1.6021892e-19
    #電子質量 eM`  = 9.10938188 ×10^-31kg 
    k_eM_bq____ = 9.10938188e-31           #* ut.kg
    #陽子質量 pM`  = 1.67262157 ×10^-27  kg 
    k_pM_bq____ = 1.67262157e-27           #* ut.kg
    #水素原子質量 HM` = 1.6735 ×10^-27  kg 
    k_HM_bq____ = 1.6735e-27               #* ut.kg
    #モル数,Avogadro 数　 NA`  = 6.02214199 ×10^23  mol-1
    k_NA_bq____ = 6.02214199e+23           #1/ ut.mol
    #モル体積 Vm`  = 2.241383 ×10-2  m3mol-1 
    k_Vm_bq____ = 2.241383e-2              #* ut.m**3 / ut.mol

    #真空の透磁率 1.2566370614E-06 == 4`π 1e-7, 物理単位 N` A`^-2 == henry/meter == weber/(ampere meter)
    k__sMu_0_bq____ = 1.2566370614e-6      #* ut.H/ut.m        #@μ0` -->
    k_u0_bq____ = 1.2566370614e-6          #*ut.H/ut.m
    k_U0_bq____ = 112940906672.587         # U0` ≡ u0` c`^2
    # 真空の誘電率 ε0 == 1/(`c^2 4`π 1e-7)==クーロン**2 / (newton * M ** 2) == farad/meter == coulomb/(volt meter)
    k__sEpsilon_0_bq____ = 8.854187816e-12 #* ut.F/ut.m  #@:ε0` -->
    k_e0_bq____ = 8.854187816e-12          #* ut.F/ut.m

    #ボルツマン定数   J K^-1 K は絶対温度の単位です。Kg ではありません
    k_kB_bq____  = 1.380662e-23            #* ut.J/ut.K     # Joule/ kelvin degree
    #=========== 物理定数 end = ==================================

    sf.__getDctGlobals().update(locals())

tr()
try:
    from fractions import Fraction
    k__bq_1f___ = Fraction(1,1)             # `1f ≡ Fraction(1,1)
except:
    pass


#k__tilda__UsOp_eq____ = sf.sc.allclose         # ~== : nearly equal
# if you use allclose, then (4.7pF`) ~== (100pF) become True
k__tilda__UsOp_eq____ = sf.nearlyEq         # ~== : nearly equal

#def __clearBF___(self):
#    sf.__getDctGlobals()['k__bq_B___']=self   # clear and regist global Bf

def BF(**dctAg):
    clAt = BG(**dctAg)
    sf.__getDctGlobals()['k__bq_B___']=clAt   # clear and regist global Bf
    return clAt.m_dctReadOnly[sorted(dctAg)[-1]]


class BG(object):
    """' date:2014/05/25 Constructor holds read-only variable and __call__ holds
        instantanious variable. We implemented this class for one-liners to hold
        temporal variables.
    '"""
    def __init__(self, **dctAg):
        # Don't use self.m_dctReadOnly = ... or self.m_dctBuffer = ... ,
        # because they call for __setattr__(..)
        if dctAg == {}:
            #self.m_dctReadOnly = {}
            self.__dict__["m_dctReadOnly"] = {}
        else:
            # m_dctReadOnly is set at just only __init__()
            #self.m_dctReadOnly = dctAg
            self.__dict__["m_dctReadOnly"] = dctAg

        #self.m_dctBuffer={}
        self.__dict__["m_dctBuffer"] = {}
        #__clearBF___(self)

    def __call__(self, **dctAg):
        """' Set (key:value) pair for imutable m_dctBuffer.
        Return last value. 
        '"""
        for k in dctAg:
            if k in self.m_dctReadOnly:
                assert False, ("You assigned a keyward argument:"+str({k:dctAg[k]})
                              +" for already exising in a read only BF instance") 

            else:
                for k in dctAg:
                    self.m_dctBuffer[k] = dctAg[k]

            #return True; # to set sentinel
            # It is not lucid functional programming to use a sentinel

            # return value to use in comprehension operations
            # an example;;[ bf.x for v in mitr(*[range(3)]*4) if bf(x=O3(v)) bf.x.conj() == 0]
            #return self.m_dctBuffer[sorted(self.m_dctBuffer)[-1]]
            return self.m_dctBuffer[sorted(dctAg)[-1]]

    def __getattr__(self, name):
        #print "debug--name:" + str(name)
        if name in self.m_dctReadOnly:
            return self.m_dctReadOnly[name]
        # yet implemented for _._. .. read only hierarchy
        elif name in self.m_dctBuffer:
            return self.m_dctBuffer[name]
        else:
            assert False, "In ClBuffer, there is no variable:" + name
        return self.__dict__[name]

    def __setattr__(self, name, value):

        assert False , ("Don't assign for ClBuffer members. " + name
                      + " = " + str(value) )

    #def pop(self, ag=None):
    #    """' default:None pop '_' (key:value) pair first from m_dctBuffer,
    #    second from m_dctReadOnly.
    #    '"""
    #    if ag==None:
    #        ag = '_'

    #    if ag in self.m_dctBuffer:
    #        self.m_dctBuffer.pop(ag)
    #    elif ag in self.m_dctReadOnly:
    #        self.m_dctBuffer.pop(ag)
    #    else:
    #        import exceptions as md
    #        raise md.KeyError(ag)

    """'
    '"""

Bf = k__bq_B___ = BG() 


