# -*- encoding: utf-8 -*-
from __future__ import division
"""'
english:
    PythonSf pysf/rational.py
    https://github.com/lobosKobayashi
    http://lobosKobayashi.github.com/
    
    Copyright 2016, Kenji Kobayashi
    All program codes in this file was designed by kVerifierLab Kenji Kobayashi

    I release souce codes in this file under the GPLv3
    with the exception of my commercial uses.

    2016y 12m 28d Kenji Kokbayashi

japanese:
    PythonSf pysf/rational.py
    https://github.com/lobosKobayashi
    http://lobosKobayashi.github.com/

    Copyright 2016, Kenji Kobayashi
    このファイルの全てのプログラム・コードは kVerifierLab 小林憲次が作成しました。
    
    作成者の小林本人に限っては商用利用を許すとの例外条件を追加して、
    このファイルのソースを GPLv3 で公開します。

    2016年 12月 28日 小林憲次
'"""

import numpy as sc
import sfFnctns as sf
import copy

# Below poly1d is needed to avoid sc.poly1d([1,2,3])/3
# unsupported operand type(s) for /: 'poly1d' and 'int' at excecuting:sc.poly1d([1,3,2])/3

# at from __future__ import division
class poly1d(sc.poly1d):
    def __init__(self, sqAg, **dctAg):
        #assert not sc.iscomplexobj(sqAg)
        if not 'variable' in dctAg:
            dctAg['variable']='s'

        if isinstance(sqAg, sf.ClTensor):
            sqAg = sc.array(sqAg)

        sc.poly1d.__init__(self, sqAg, **dctAg)

    def __truediv__(self, other):
        #return self.__div(other)
        if sc.isscalar(other):
            return poly1d(self.coeffs/other, variable='s')
        else:
            other = sc.poly1d(other, variable='s')
            tplAt =  sc.polydiv(self, other)
            return (poly1d(tplAt[0]), poly1d(tplAt[1]))

    def __rtruediv__(self, other):
        #return "XXX"
        #return self.__div__(a)
        if sc.isscalar(other):
            return sc.poly1d(other/self.coeffs, variable='s')
        else:
            other = sc.poly1d(other, variable='s')
            tplAt =  sc.polydiv(other, self)
            return (poly1d(tplAt[0]), poly1d(tplAt[1]))

    def getGCD(self, other):
        if isinstance(other, (int, float, complex)):
            return poly1d([1])

        if not isinstance(other, poly1d):
            other = poly1d(other)

        if len(self)==0 or len(other)==0:
            return poly1d([1])

        numerAt,denomAt = self, other
        if len(denomAt) > len(numerAt):
            numerAt,denomAt = denomAt, numerAt

        while True:
            assert denomAt.coeffs[0] != 0
            denomAt = denomAt/denomAt.coeffs[0]

            #import pdb; pdb.set_trace()
            residualAt = (numerAt/denomAt)[1]
            if residualAt == poly1d([0]):
                return poly1d(denomAt)

            if len(residualAt) == 0:
                return poly1d([1])

            numerAt,denomAt = denomAt, residualAt


def plotBode(fAg, lowerFreq, higherFreq = None):
    """'  plot Bode diagram using matplotlib
        Default frequency width is 3 decades
    '"""
    import pylab as py
    #import pdb; pdb.set_trace()
    if ( higherFreq == None):
        rangeAt = 1000.0  # 3 decade
    else:
        assert higherFreq > lowerFreq
        rangeAt = float(higherFreq)/lowerFreq

    N = 128
    lstScannAngFreqAt = [2*sc.pi*1j*lowerFreq*sc.exp(
                                                sc.log(rangeAt)*float(k)/N)
                                for k in range(N)]

    t              = [        lowerFreq*sc.exp(sc.log(rangeAt)*float(k)/N)
                                for k in range(N)]

    py.subplot(211)
    py.loglog( t, [(abs(fAg(x))) for x in lstScannAngFreqAt]  )
    py.ylabel('gain')
    py.grid(True)

    py.subplot(212)
    py.semilogx( t, [sc.arctan2(fAg(zz).imag, fAg(zz).real)
                        for zz in lstScannAngFreqAt])
    py.ylabel('phase')
    py.grid(True)
    py.gca().xaxis.grid(True, which='minor')  # minor grid on too
    py.show()


class ClRtnl(object):
    """' Ratianal Function class
        The highest coefficient of demoninator is always 1
    '"""
    def __init__(self, numerAg, denomAg = 1, variable='s'):
        #import pdb;pdb.set_trace()
        if isinstance(numerAg, ClRtnl):
            assert denomAg == 1
            self.m_plNumer = copy.copy(numerAg.m_plNumer)
            self.m_plDenom = copy.copy(numerAg.m_plDenom)
        elif sc.isscalar(numerAg):
            self.m_plNumer = poly1d(numerAg, variable=variable)
            self.m_plDenom = poly1d(denomAg, variable=variable)
        else:
            # cation! list(numerAg) may cause infinite loop between
            #poly1d.__setitem__(..) and poly1d.__getitem__(..)

            # ClRtntnl coefficients must be float or complex
            if isinstance(numerAg, sc.poly1d):
                lstAt = list(numerAg.coeffs)
            else:
                lstAt = numerAg

            if isinstance(lstAt[0],int):
                lstAt[0] = float(lstAt[0])
            self.m_plNumer = poly1d(lstAt, variable=variable)


            if isinstance(denomAg, poly1d):
                lstAt = list(denomAg.coeffs)
            else:
                lstAt = denomAg

            if sc.isscalar(lstAt):
                self.m_plDenom = poly1d(lstAt, variable=variable)
            else:
                if isinstance(lstAt[0],int):
                    lstAt[0] = float(lstAt[0])
                self.m_plDenom = poly1d(lstAt, variable=variable)

        # normalize
        valAt = self.m_plDenom.coeffs[0]
        #self.m_plNumer /= valAt
        #self.m_plDenom /= valAt
        self.m_plNumer = poly1d(self.m_plNumer/valAt, variable=variable)
        self.m_plDenom = poly1d(self.m_plDenom /valAt, variable=variable)

        self.__elmntNmDn()
        if self.m_plNumer.variable != variable:
            self.m_plNumer = poly1d(self.m_plNumer/valAt, variable=variable)
        if self.m_plDenom.variable != variable:
            self.m_plDenom = poly1d(self.m_plDenom /valAt, variable=variable)

    def __repr__(self):
        #import pdb;pdb.set_trace()
        return "ClRtnl(%s,%s)" % (repr(self.m_plNumer.coeffs)[6:-1]
                                , repr(self.m_plDenom.coeffs)[6:-1] )
    def __str__(self):
        lstStr = [0]*4
        lstStrAt = str(self.m_plNumer).split("\n")
        #import pdb;pdb.set_trace()
        if len(lstStrAt) > 2:
            # if len(str(poly1d instrance)) > 72 then the polynomial strings
            # become to consists of 2*N multiple lines
            assert len(lstStrAt)%2 == 0

            # make length ofupper and lower strings same 10.03.17
            for k in range(0,len(lstStrAt),2):
                inDffAt = len(lstStrAt[k]) - len(lstStrAt[k+1])
                if inDffAt > 0:
                    lstStrAt[k+1] += " " * inDffAt
            lstStrAt = [''.join(lstStrAt[0::2]), ''.join(lstStrAt[1::2])]

        if len(lstStrAt) == 2:
            lstStr[0] = lstStrAt[0]
            lstStr[1] = lstStrAt[1]
        else:
            assert len(lstStrAt) == 1
            lstStr[0] = '\n'
            lstStr[1] = lstStrAt[0]

        lstStrAt = str(self.m_plDenom).split("\n")
        if len(lstStrAt) == 2:
            lstStr[2] = lstStrAt[0]
            lstStr[3] = lstStrAt[1]
        elif len(lstStrAt) == 1:
            lstStr[2] = '\n'
            lstStr[3] = lstStrAt[0]
        else:
            lenAt =  len(lstStrAt)
            assert lenAt % 2== 0

            # make length ofupper and lower strings same 10.03.17
            for k in range(0,len(lstStrAt),2):
                inDffAt = len(lstStrAt[k]) - len(lstStrAt[k+1])
                if inDffAt > 0:
                    lstStrAt[k+1] += " " * inDffAt

            lstStr[2] = ''.join(lstStrAt[0:lenAt:2])
            lstStr[3] = ''.join(lstStrAt[1:lenAt:2])


        if lstStr[3] == "1":
            return str(self.m_plNumer)
            lstStr[2] = lstStrAt[0:lenAt:2]

        #import pdb;pdb.set_trace()
        assert lstStr[3][0:2] == "1 "
        lstStr[2] = lstStr[2][2:]
        lstStr[3] = lstStr[3][2:]

        if lstStr[2] == "":
            lstStr[2] = lstStr[3]
            lstStr[3] = ""
            inDiffAt = len(lstStr[1]) - len(lstStr[2])
        else:
            inDiffAt = len(lstStr[1]) - len(lstStr[3])

        if (inDiffAt > 0):
            strSp = " " * int(inDiffAt/2)
            if lstStr[3]=="":
                lstStr[2] = strSp + lstStr[2]
                lenAt = int(inDiffAt/2) + len(lstStr[2])
            else:
                lstStr[2] = strSp + lstStr[2]
                lstStr[3] = strSp + lstStr[3]
                lenAt = int(inDiffAt/2) + len(lstStr[3])
        elif (inDiffAt < 0):
            inDiffAt *= -1
            strSp = " " * int(inDiffAt/2)
            lstStr[0] = strSp + lstStr[0]
            lstStr[1] = strSp + lstStr[1]
            lenAt = int(inDiffAt/2) + len(lstStr[1])
        else:
            lenAt = len(lstStr[1])

        lstStr.insert(2, "-"*lenAt)
        return "\n".join(lstStr)

    def getRtnlOfRtnl(self, rtnlAg):
        """' get Rational function of Rational function
        e.g.
//@@
# 07.12.26 test getRtnlOfRtnl
import sf
cl = sf.ClRtnl(1,[1,2,3])
print cl
print cl.getRtnlOfRtnl([1,0,0])
print cl.getRtnlOfRtnl([1,0,3])
print cl.getRtnlOfRtnl(sf.ClRtnl([1,2],[1,0,3]) )

cl = sf.ClRtnl([2,7],[1,2,3])
print cl
print cl.getRtnlOfRtnl(sf.ClRtnl([1,2],[1,0,3]) )
//@@@

     1
-----------
 2
x + 2 x + 3

     1
-----------
 4     2
x + 2 x + 3

     1
-----------
 4     2
x + 8 x + 18
                       6     4     2
               0.3333 x + 3 x + 9 x + 9
------------------------------------------------------
 6          5         4         3         2
x + 0.6667 x + 10.67 x + 5.333 x + 37.33 x + 10 x + 43

  2 x + 7
-----------
 2
x + 2 x + 3
       8          7         6     5       4      3       2
2.333 x + 0.6667 x + 29.33 x + 6 x + 138 x + 18 x + 288 x + 18 x + 225
----------------------------------------------------------------------
 8          7         6         5         4      3       2
x + 0.6667 x + 13.67 x + 7.333 x + 69.33 x + 26 x + 155 x + 30 x + 129

        '"""
        rtAt = ClRtnl(rtnlAg)

        lstAt = list(self.m_plNumer.coeffs)
        lstAt.reverse()
        rtNumerAt = sum([e*rtAt**k for k,e in enumerate(lstAt)] )

        lstAt = list(self.m_plDenom.coeffs)
        lstAt.reverse()
        rtDenomAt = sum([e*rtAt**k for k,e in enumerate(lstAt)] )
        return (rtNumerAt/rtDenomAt).__elmntNmDn()

    def __elmntNmDn(self):
        """' eliminate 0 term that exists both of the numerator and denominator
        '"""
        # len(plGcdAt) >= 1 then plGcdAt == poly1d([1] become vector
        plNumerAt = self.m_plNumer
        plDenomAt = self.m_plDenom
        if len(plNumerAt)==0 and plNumerAt == poly1d([0]):
            self.m_plNumer = poly1d([0])
            self.m_plDenom = poly1d([1])
            return self

        plGcdAt = plNumerAt.getGCD(plDenomAt)
        if len(plGcdAt)==0 and plGcdAt == poly1d([1]):
            # No common factor
            return self

        plNumerAt = (plNumerAt/plGcdAt)[0]
        plDenomAt = (plDenomAt/plGcdAt)[0]
        valAt = plDenomAt.coeffs[0]
        assert valAt != 0
        self.m_plNumer = plNumerAt/valAt
        self.m_plDenom = plDenomAt/valAt

        return self

    def __call__(self, val):
        if isinstance(val, (tuple, list, sf.ClTensor)):
            return sf.krry([self(x) for x in val])
        else:
            return self.m_plNumer(val)/self.m_plDenom(val)

    def __mul__(self, other):
        if isinstance(other, sf.ClFldTns):
            return other.__rmul__(self)

        if self == 0 or other == 0:
            # ClRtnl([0],[1]) * polynomial or rational == ClRtnl([0],[1])
            # 上を保たずに ClRtnl([0],polynomial)とすると、回路など係数の仮数部
            # が大きく異なる多項式の加減算で計算誤差が入り込む
            return ClRtnl([0],[1])

        if sc.isscalar(other):
            return ClRtnl(self.m_plNumer * other, self.m_plDenom)
        else:
            clRtn = ClRtnl(self)
            other = ClRtnl(other)

            plDenomAt = clRtn.m_plDenom
            plNumerAt = other.m_plNumer
            plGcdAt = plNumerAt.getGCD(plDenomAt)
            if len(plGcdAt)==0 and plGcdAt == poly1d([1]):
                pass
            else:
                clRtn.m_plDenom = (plDenomAt/plGcdAt)[0]
                other.m_plNumer = (plNumerAt/plGcdAt)[0]

            plDenomAt = other.m_plDenom
            plNumerAt = clRtn.m_plNumer
            plGcdAt = plNumerAt.getGCD(plDenomAt)
            if len(plGcdAt)==0 and plGcdAt == poly1d([1]):
                pass
            else:
                other.m_plDenom = (plDenomAt/plGcdAt)[0]
                clRtn.m_plNumer = (plNumerAt/plGcdAt)[0]

            clRtn.m_plNumer = clRtn.m_plNumer * other.m_plNumer
            clRtn.m_plDenom = clRtn.m_plDenom * other.m_plDenom
            valAt = self.m_plDenom.coeffs[0]
            #clRtn.m_plNumer /= valAt
            #clRtn.m_plDenom /= valAt
            self.m_plNumer = poly1d(self.m_plNumer/valAt)
            self.m_plDenom = poly1d(self.m_plDenom /valAt)
            clRtn.m_plNumer = poly1d(clRtn.m_plNumer)
            clRtn.m_plDenom = poly1d(clRtn.m_plDenom)
            return clRtn.__elmntNmDn()

    def __rmul__(self, other):
        return ClRtnl.__mul__(self,other)

    def __add__(self, other):
        other = ClRtnl(other)
        clRtn = ClRtnl(self)
        plGcdAt = self.m_plDenom.getGCD(other.m_plDenom)

        # len(plGcdAt) >= 1 then plGcdAt == poly1d([1] become vector
        if len(plGcdAt)==0 and plGcdAt == poly1d([1]):
            clRtn.m_plNumer = clRtn.m_plNumer * other.m_plDenom\
                            + clRtn.m_plDenom * other.m_plNumer
            clRtn.m_plDenom = clRtn.m_plDenom * other.m_plDenom
        else:
            selfDenomQuotientAt = (self.m_plDenom/plGcdAt)[0]
            otherDenomQuotientAt = (other.m_plDenom/plGcdAt)[0]

            clRtn.m_plNumer = ( clRtn.m_plNumer * otherDenomQuotientAt
                              + selfDenomQuotientAt * other.m_plNumer)
            clRtn.m_plDenom = ( selfDenomQuotientAt * otherDenomQuotientAt
                              * plGcdAt)

        valAt = clRtn.m_plDenom.coeffs[0]
        #clRtn.m_plNumer /= valAt
        #clRtn.m_plDenom /= valAt
        self.m_plNumer = poly1d(self.m_plNumer/valAt)
        self.m_plDenom = poly1d(self.m_plDenom /valAt)
        clRtn.m_plNumer = poly1d(clRtn.m_plNumer)
        clRtn.m_plDenom = poly1d(clRtn.m_plDenom)
        return clRtn.__elmntNmDn()

    def __radd__(self, other):
        return ClRtnl.__add__(self,other).__elmntNmDn()

    def __pow__(self, val):
        if not sc.isscalar(val) or int(val) != val :
            raise ValueError, "In ClRtnl, a parameter at power operation must be integer:"+str(val)

        clRtn = ClRtnl([1])
        if (val < 0):
            val = -int(val)
            for i in range(val):
                clRtn.m_plNumer *= self.m_plDenom
                clRtn.m_plDenom *= self.m_plNumer
        else:
            for i in range(val):
                clRtn.m_plNumer *= self.m_plNumer
                clRtn.m_plDenom *= self.m_plDenom

        valAt = clRtn.m_plDenom.coeffs[0]
        #clRtn.m_plNumer /= valAt
        #clRtn.m_plDenom /= valAt
        self.m_plNumer = poly1d(self.m_plNumer/valAt)
        self.m_plDenom = poly1d(self.m_plDenom /valAt)
        clRtn.m_plNumer = poly1d(clRtn.m_plNumer)
        clRtn.m_plDenom = poly1d(clRtn.m_plDenom)
        return clRtn.__elmntNmDn()

    def __sub__(self, other):
        return self.__add__(-1*other)

    def __rsub__(self, other):
        return (-1*self).__add__(other)

    def __truediv__(self, other):
        return self.__div__(other)
    def __div__(self, other):
        otherAt = ClRtnl(other)
        assert otherAt.m_plNumer != poly1d([0])
        otherAt.m_plNumer, otherAt.m_plDenom = (
                                        otherAt.m_plDenom, otherAt.m_plNumer)
        return self.__mul__(otherAt)


    def __rtruediv__(self, other):
        return self.__rdiv__(other)
    def __rdiv__(self, other):
        clRtn = ClRtnl(other)
        clAt = ClRtnl(self)
        assert clAt.m_plNumer != poly1d([0])
        clAt.m_plNumer, clAt.m_plDenom = clAt.m_plDenom, clAt.m_plNumer
        return clRtn.__mul__(clAt)

    def __eq__(self, other):
        if isinstance(other, (int, float, complex)):
            # ClRtnl([0],[1])==0 --> True を返さねばならない
            otherAt = ClRtnl([other])
        elif not(isinstance(other, poly1d) or isinstance(other, ClRtnl)):
            return False
        else:
            otherAt = ClRtnl(other)
        return self.m_plNumer*otherAt.m_plDenom\
            == self.m_plDenom* otherAt.m_plNumer

    def __ne__(self, other):
        if not(isinstance(other, poly1d) or isinstance(other, ClRtnl)):
            return True
        otherAt = ClRtnl(other)
        return self.m_plNumer*otherAt.m_plDenom\
            != self.m_plDenom* otherAt.m_plNumer

    def __neg__(self):
        clRtn = ClRtnl(self)
        clRtn.m_plNumer = poly1d(-sf.krry(clRtn.m_plNumer.coeffs))
        return clRtn

    def deriv(self):
        """Return the derivative of this rational funciton.
        """
        return ClRtnl( self.m_plNumer.deriv() * self.m_plDenom
                            + self.m_plDenom.deriv()
                    ,  self.m_plDenom * self.m_plDenom )

    def getAnImpls(self, time, dataN = 128):
        """' Get Analog Impulse from Ratianal Function
        '"""
        #assert self.m_plNumer.order < self.m_plDenom.order
        denominatorAt = self.m_plDenom.coeffs[1:]
        denominatorAt = -denominatorAt
        denominatorAt = list(denominatorAt) # change to list to reverse
        denominatorAt.reverse()

        numeratorAt = list(self.m_plNumer.coeffs)
        numeratorAt.reverse()

        N = len(denominatorAt)      # order
        assert len(numeratorAt) <= N, \
            "numerator order must be bigger than demoninator order"

        lenAt = len(numeratorAt)
        C = numeratorAt + [0]*(N-lenAt)
        B = sc.zeros(N)
        B[-1] = 1

        A = sc.zeros([N,N])
        A[-1,:] = denominatorAt
        sc.ravel(A)[1:N*(N-1):N+1] = [1]*(N-1)

        def func(x,t):
            return sc.dot(A,x)

        import scipy.integrate as si
        arrX = si.odeint( func, sf.krry( [0]*(N-1)+[1] )
                , sf.arSqnc(0,dataN, float(time)/dataN) )

        #print arrX
        #print arrX[3,:]
        # 12.12.13 return sc.dot(arrX, C)
        return sf.krry__(sc.dot(arrX, C).view())

    def getAnRspns(self, time, input = sf.arsq(1, 128, 0.0) ):
        """' Get Analog Responce determined by the rational function.
             Default inputs wave form is step function.
              if a input vector or list is given, then simulation step time
             deltaT will be determined as deltaT = time/len(imput)
        '"""
        #assert self.m_plNumer.order <= self.m_plDenom.order
        denominatorAt = self.m_plDenom.coeffs[1:]
        denominatorAt = -denominatorAt
        denominatorAt = list(denominatorAt) # change to list to reverse
        denominatorAt.reverse()

        numeratorAt = list(self.m_plNumer.coeffs)
        numeratorAt.reverse()

        N = len(denominatorAt)      # order, m_plDenominator list is truncated
        assert len(numeratorAt) <= N+1, \
            "numerator order must be bigger than equal demoninator order"

        if ( len(numeratorAt) == N+1):
            D = numeratorAt[-1]
            numeratorAt = list(
                    # 上で denominatorAt の符号は既に反転させている
                    sf.krry(numeratorAt[0:-1]) + D*sf.krry(denominatorAt) )
        elif ( len(numeratorAt) > N+1):
            assert False, \
                "numerator order must be bigger than equal demoninator order"
        else:
            D = 0

        lenAt = len(numeratorAt)
        C = numeratorAt + [0]*(N-lenAt)
        B = sc.zeros(N)
        B[-1] = 1

        A = sc.zeros([N,N])
        A[-1,:] = denominatorAt
        sc.ravel(A)[1:N*(N-1):N+1] = [1]*(N-1)
        dataN = len(input)

        """'
        def func(x,t):
            if ( int(dataN*t/time) >= dataN ):
                #import pdb; pdb.set_trace()
                return sc.dot(A,x)
            else:
                return sc.dot(A,x) + input[int(dataN*t/time)]*B

        import scipy.integrate as si
        arrX = si.odeint( func, sc.zeros(N)
                , sf.arSqnc(0,dataN, float(time)/dataN) )

        #print arrX
        #print arrX[3,:]
        return sc.dot(arrX, C)+D*sf.krry(input)
        '"""

        lsX=[sc.zeros(N)]
        import scipy.integrate as si
        for inpAt in input:
            def func(x,t):
                return sc.dot(A,x) + inpAt*B

            lsX.append( si.odeint(func, lsX[-1], [0,float(time)/dataN])[-1] )

        return sc.dot(lsX[:-1], C)+D*sf.krry(input)


    def getDgImpls(self, dataN = 128):
        """' Get Digital Impulse from Ratianal Function
        '"""
        # cl=rt.ClRtnl([6,7,8,9],[2,3,4,5,6])
        # dx/dt = A x + B u
        #     v = C x + D u

        # A:    [[ 0. ,  1. ,  0. ,  0. ],
        #        [ 0. ,  0. ,  1. ,  0. ],
        #        [ 0. ,  0. ,  0. ,  1. ],
        #        [-3. , -2.5, -2. , -1.5]]

        # B:    [ 0.,  0.,  0.,  1.]

        # C:    [4.5, 4.0, 3.5, 3.0]

        # D:    0

        #assert self.m_plNumer.order < self.m_plDenom.order
        denominatorAt = self.m_plDenom.coeffs[1:]
        denominatorAt = -denominatorAt
        denominatorAt = list(denominatorAt) # change to list to reverse
        denominatorAt.reverse()

        numeratorAt = list(self.m_plNumer.coeffs)
        numeratorAt.reverse()

        N = len(denominatorAt)      # order
        assert len(numeratorAt) <= N+1, \
            "numerator order must be bigger equal than demoninator order"

        if ( len(numeratorAt) == N+1):
            D = numeratorAt[-1]
            numeratorAt = list(
                    # 上で denominatorAt の符号は既に反転させている
                    sf.krry(numeratorAt[0:-1]) + D*sf.krry(denominatorAt) )
        elif ( len(numeratorAt) > N+1):
            assert False, \
                "numerator order must be bigger than equal demoninator order"
        else:
            D = 0

        lenAt = len(numeratorAt)
        C = numeratorAt + [0]*(N-lenAt)
        B = sc.zeros(N)
        B[-1] = 1

        A = sc.zeros([N,N])
        A[-1,:] = denominatorAt
        sc.ravel(A)[1:N*(N-1):N+1] = [1]*(N-1)
        #vctY = sc.zeros(dataN)
        vctY = sf.kzrs(dataN)

        def func(x):
            return sc.dot(A,x)

        # if D == 0 then output:vctY[0] == 0
        vctY[0] = D
        arState = sc.array( [0]*(N-1)+[1] )
        for k in range(1,dataN):
            vctY[k] = sum(arState * C)
            arState = func(arState)

        return vctY

    def getDgRspns(self, input = sf.arsq(1, 128, 0) ):
        """' Get Analog Responce from Ratianal Function
             Default inputs wave forme is step function.
        '"""
        #assert self.m_plNumer.order <= self.m_plDenom.order
        denominatorAt = self.m_plDenom.coeffs[1:]
        denominatorAt = -denominatorAt
        denominatorAt = list(denominatorAt) # change to list to reverse
        denominatorAt.reverse()

        numeratorAt = list(self.m_plNumer.coeffs)
        numeratorAt.reverse()

        N = len(denominatorAt)      # order, m_plDenominator list is truncated
        assert len(numeratorAt) <= N+1, \
            "numerator order must be bigger than equal demoninator order"

        if ( len(numeratorAt) == N+1):
            D = numeratorAt[-1]
            numeratorAt = list(
                    #vctr(numeratorAt[0:-1]) - D*vctr(denominatorAt) )
                    # denominatorAt の符号は上で反転されている
                    sf.krry(numeratorAt[0:-1]) + D*sf.krry(denominatorAt) )
        elif ( len(numeratorAt) > N+1):
            assert False, \
                "numerator order must be bigger than equal demoninator order"
        else:
            D = 0

        lenAt = len(numeratorAt)
        """'11.05.14 modify to spped up
        C = numeratorAt + [0]*(N-lenAt)
        B = sc.zeros(N)
        B[-1] = 1

        A = sc.zeros([N,N])
        A[-1,:] = denominatorAt
        sc.ravel(A)[1:N*(N-1):N+1] = [1]*(N-1)
        arState = sc.array( [0]*N )
        dataN= len(input)
        #vctY = sc.zeros(dataN)
        vctY = sf.kzrs(dataN)

        def func(x, u):
            return sc.dot(A,x) + u*B

        for k in range(dataN):
            vctY[k] = sum(arState * C)+ D*input[k]
            arState = func(arState, input[k])

        return vctY
        '"""
        C = numeratorAt + [0]*(N-lenAt)
        A = sc.array(denominatorAt)
        arState = sc.array( [0.]*N )
        dataN= len(input)
        #12.12.13 vctY = sc.zeros(dataN)
        vctY = sf.kzrs(dataN)

        for k in range(dataN):
            vctY[k] = sc.dot(arState, C)+ D*input[k]
            valAt = sc.dot(A, arState)+ input[k]
            arState = sc.roll(arState, -1)
            arState[-1] = valAt

        return vctY

    def plotBode(self, lowerFreq, higherFreq = None):
        """'  plot Bode diagram using matplotlib
            Default frequency width is 3 decades
        '"""
        import pylab as py
        #import pdb; pdb.set_trace()
        if ( higherFreq == None):
            rangeAt = 1000.0  # 3 decade
        else:
            assert higherFreq > lowerFreq
            rangeAt = float(higherFreq)/lowerFreq

        N = 128
        lstScannAngFreqAt = [2*sc.pi*1j*lowerFreq*sc.exp(
                                                  sc.log(rangeAt)*float(k)/N)
                                    for k in range(N)]

        t              = [        lowerFreq*sc.exp(sc.log(rangeAt)*float(k)/N)
                                    for k in range(N)]

        py.subplot(211)
        py.loglog( t, (abs(self(lstScannAngFreqAt)))  )
        py.ylabel('gain')
        py.grid(True)

        py.subplot(212)
        py.semilogx( t, [sc.arctan2(zz.imag, zz.real)
                            for zz in self(lstScannAngFreqAt)])
        py.ylabel('phase')
        py.grid(True)
        py.gca().xaxis.grid(True, which='minor')  # minor grid on too
        py.show()

    def plotDgGnPh(self, higherFrqAg = 0.5, lowerFrqAg = -0.5):
        """'  plot Gain/Phase diagram of discrete system using matplotlib
            The angular at the right side is pi
            Drawing Gain/Phase plot by H(z) ==> H(epx(j ω))
            Default angular width is 3 decades
            Frequencey Range: [lowerFrqAg , higherFrqAg]
        '"""
        import pylab as py
        N = 128

        lstThetaAt = [sc.exp( 2*sc.pi*1j*(lowerFrqAg
                    + (higherFrqAg-lowerFrqAg) *float(k)/N) )    for k in range(N)]

        t          = [lowerFrqAg+ (higherFrqAg-lowerFrqAg) *float(k)/N
                                    for k in range(N)]

        py.subplot(211)
        py.plot( t, abs(self(lstThetaAt))  )
        py.ylabel('gain')
        py.grid(True)

        py.subplot(212)
        py.plot( t, [sc.arctan2(zz.imag, zz.real)
                            for zz in self(lstThetaAt)])
        py.ylabel('phase')
        py.grid(True)
        py.gca().xaxis.grid(True, which='minor')  # minor grid on too
        py.show()

    def plotAnRspns(self, time, input = sf.arsq(1, 128, 0.0), color=(0,1,1) ):
        """' Plot Analog Responce determined by the rational function.
             Default inputs wave form is step function.
              if a input vector or list is given, then simulation step time
             deltaT will be determined as deltaT = time/len(imput)

         2010,05,18
         This code is a test implementation and may be changed.
        '"""
        #assert self.m_plNumer.order <= self.m_plDenom.order
        denominatorAt = self.m_plDenom.coeffs[1:]
        denominatorAt = -denominatorAt
        denominatorAt = list(denominatorAt) # change to list to reverse
        denominatorAt.reverse()

        numeratorAt = list(self.m_plNumer.coeffs)
        numeratorAt.reverse()

        N = len(denominatorAt)      # order, m_plDenominator list is truncated
        assert len(numeratorAt) <= N+1, \
            "numerator order must be bigger than equal demoninator order"

        if ( len(numeratorAt) == N+1):
            D = numeratorAt[-1]
            numeratorAt = list(
                    # 上で denominatorAt の符号は既に反転させている
                    sf.krry(numeratorAt[0:-1]) + D*sf.krry(denominatorAt) )
        elif ( len(numeratorAt) > N+1):
            assert False, \
                "numerator order must be bigger than equal demoninator order"
        else:
            D = 0

        lenAt = len(numeratorAt)
        C = numeratorAt + [0]*(N-lenAt)
        B = sc.zeros(N)
        B[-1] = 1

        A = sc.zeros([N,N])
        A[-1,:] = denominatorAt
        sc.ravel(A)[1:N*(N-1):N+1] = [1]*(N-1)
        dataN = len(input)

        lsX=[sc.zeros(N)]
        import scipy.integrate as si
        for inpAt in input:
            def func(x,t):
                return sc.dot(A,x) + inpAt*B

            lsX.append( si.odeint(func, lsX[-1], [0,float(time)/dataN])[-1] )

        #import pdb; pdb.set_trace()
        # upper code is same in getAnRspns
        vs=sf.vs_()
        N = len(input)
        vc = sf.arsq(0,N, time/N)
        #R=1/vc[-1] *(len(vc))
        R=(1-1e-10)/vc[-1] *(len(vc))
        # don't use lsX[1:] becuase visual.graph(..) needs (0,0) first data.
        # if not (0,0) then horizontal axis become wider if the span is us` order.
        vsVal = sc.dot(lsX[:-1], C)+D*sf.krry(input)
        #import pdb; pdb.set_trace()
        def f(x):
            inAt = int(R*x)
            return vsVal[inAt]
        return sf.plotGr(f, vc, color=color)

#z_ = ClRtnl(1,[1,0])


def plotBode(clRtnlAg, lowerFreq, higherFreq = None):
    """' Not member function in ClRtnl '"""
    assert isinstance(clRtnlAg, ClRtnl)
    clRtnlAg.plotBode(lowerFreq, higherFreq)

def plotDgGnPh(clRtnlAg, higherFreq = 1, lowerFreq = 0):
    """' Not member function in ClRtnl '"""
    assert isinstance(clRtnlAg, ClRtnl)
    clRtnlAg.plotDgGnPh(lowerFreq, higherFreq)

