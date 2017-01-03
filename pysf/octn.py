# -*- encoding: utf-8 -*-
"""'
english:
    PythonSf pysf/octn.py
    https://github.com/lobosKobayashi
    http://lobosKobayashi.github.com/
    
    Copyright 2016, Kenji Kobayashi
    All program codes in this file was designed by kVerifierLab Kenji Kobayashi

    I release souce codes in this file under the GPLv3
    with the exception of my commercial uses.

    2016y 12m 28d Kenji Kokbayashi

japanese:
    PythonSf pysf/octn.py
    http://lobosKobayashi.github.com/
    http://lobosKobayashi.github.com/

    Copyright 2016, Kenji Kobayashi
    このファイルの全てのプログラム・コードは kVerifierLab 小林憲次が作成しました。
    
    作成者の小林本人に限っては商用利用を許すとの例外条件を追加して、
    このファイルのソースを GPLv3 で公開します。

    2016年 12月 28日 小林憲次
'"""

#from __future__ import division 
#:this division results unsupported operand type(s) for /: 'int' and 'BF
import sfFnctns as sf

#Octonion Wiki;;http://en.wikipedia.org/wiki/Octonion
#Octonion;;http://ja.wikipedia.org/wiki/%E5%85%AB%E5%85%83%E6%95%B0

# set Product:multiplication table for dctMtPr to calculate octernion
dctMtPr = {}
for j,x in enumerate(
    [(1,0),( 1,1),( 1,2),( 1,3), ( 1,4),( 1,5),( 1,6),( 1,7)]):dctMtPr[0,j]=x
for j,x in enumerate(
    [(1,1),(-1,0),( 1,3),(-1,2), ( 1,5),(-1,4),(-1,7),( 1,6)]):dctMtPr[1,j]=x
for j,x in enumerate(
    [(1,2),(-1,3),(-1,0),( 1,1), ( 1,6),( 1,7),(-1,4),(-1,5)]):dctMtPr[2,j]=x
for j,x in enumerate(
    [(1,3),( 1,2),(-1,1),(-1,0), ( 1,7),(-1,6),( 1,5),(-1,4)]):dctMtPr[3,j]=x

for j,x in enumerate(
    [(1,4),(-1,5),(-1,6),(-1,7), (-1,0),( 1,1),( 1,2),( 1,3)]):dctMtPr[4,j]=x
for j,x in enumerate(
    [(1,5),( 1,4),(-1,7),( 1,6), (-1,1),(-1,0),(-1,3),( 1,2)]):dctMtPr[5,j]=x
for j,x in enumerate(
    [(1,6),( 1,7),( 1,4),(-1,5), (-1,2),( 1,3),(-1,0),(-1,1)]):dctMtPr[6,j]=x
for j,x in enumerate(
    [(1,7),(-1,6),( 1,5),( 1,4), (-1,3),(-1,2),( 1,1),(-1,0)]):dctMtPr[7,j]=x

class ClOctonion(object):
    """' Octonion class including quaternion, complex, and real numbers
         alias name Oc
        examples: assuming import octn as oc
        declaration of octernion
            oc.Oc([1,2,3,4,5,6,7,8])
            ===============================
            (1, 2, 3, 4, 5, 6, 7, 8)
            
            oc.Oc(1,2,3,4,5,6,7,8)
            ===============================
            (1, 2, 3, 4, 5, 6, 7, 8)
        
        declaration of quaternion
            oc.Oc([1,2,3,4])
            ===============================
            (1, 2, 3, 4)
            
            oc.Oc(1,2,3,4)
            ===============================
            (1, 2, 3, 4)
        
        declaration of complex number
            oc.Oc([1,2])
            ===============================
            (1, 2)
            oc.Oc(1,2)
            ===============================
            (1, 2)
        
        +-*/ ** operations: assuming a = a = oc.Oc(1,2,3,4,5,6,7,8); b = oc.Oc(1,2,3,4)
            a+b
            ===============================
            (2, 4, 6, 8, 5, 6, 7, 8)
            
            a-b
            ===============================
            (0, 0, 0, 0, 5, 6, 7, 8)
            
            a*b
            ===============================
            (-28, 4, 6, 8, 70, -8, 0, -16)
            
            a/b
            ===============================
            (1.0, 0.0, 0.0, -2.7755575615628914e-017, -2.0, 0.66666666666666674, 0.46666666666666662, 1.0666666666666667)
            
            a**3    # power is defined only for integer
            ===============================
            (-272, -148, -768, -1052, -328, -1788, -896, -2020)

            a**-3
            ===============================
            (-0.64705882352941146, 0.76470588235294079, 3.8235294117647052, 4.4117647058823533, 1.7058823529411766, 8.882352941176471, 4.5294117647058822, 10.058823529411764)

    '"""
    # We use self.m_tpl, not self.m_tnsr, because multiply(self,m_tpl, ag) 
    # operation is octonion operation, not tensor operation
    def __init__(self, *tplAg):
        if ( tplAg == () ):
            ag = (0,0,0,0, 0,0,0,0)
        elif( len(tplAg) == 1): # ClOctonion([1,2])
            ag = tplAg[0]
        else:
            ag = tplAg
        
        if isinstance(ag, ClOctonion):
            self.m_tpl = ag.m_tpl
        elif isinstance(ag, int) or isinstance(ag, float):
            self.m_tpl = (ag,0,0,0, 0,0,0,0)
        elif isinstance(ag, int) or isinstance(ag, complex):
            self.m_tpl = (ag.real,ag.imag,0,0, 0,0,0,0)
        else:
            assert 1<= len(ag) <= 8
            if len(ag)<8:
                ag = tuple(ag)+(0,)*(8-len(ag))

            self.m_tpl = tuple(ag)

    def __str__(self):
        if self.m_tpl[1:] == (0,0,0, 0,0,0,0):
            return "Oc("+str(self.m_tpl[0])+")"
        elif self.m_tpl[2:] == (0,0, 0,0,0,0):
            return "Oc"+str(self.m_tpl[0:2])
        elif self.m_tpl[4:] == (0,0,0,0):
            return "Oc"+str(self.m_tpl[0:4])
        else:
            return "Oc"+str(self.m_tpl)

    def __repr__(self):
        # I know __repr__ must reproduce the instane. But I choose __str__ for users.
        return str(self)

    def __add__(self, ag):
        if isinstance(ag, ClOctonion):
            return type(self)([self.m_tpl[i] + ag.m_tpl[i] for i in range(8)])
        elif isinstance(ag, (int, float) ):
            lstAt = list(self.m_tpl)
            lstAt[0] = lstAt[0] + ag
            return type(self)(lstAt)
        elif isinstance(ag, complex):
            lstAt = list(self.m_tpl)
            lstAt[0] = lstAt[0] + ag.real
            lstAt[1] = lstAt[1] + ag.imag
            return type(self)(lstAt)
        elif isinstance(ag, sf.ClFldTns) and (
                (ag.m_type == ClOctonion) or            # Oc element ClFldTns instance
                (ag.m_type.__base__ == ClOctonion)):    # O2 ... O7 element ClFldTns instance
            return ag.__radd__(self)
        elif isinstance(ag, (list,tuple, sf.sc.ndarray, sf.ClFldTns) ):
            assert len(ag) <= 8
            lstAt = list(self.m_tpl)
            for k in range(len(ag)):
                lstAt[k] = lstAt[k] + ag[k]
            return type(self)(lstAt)
        else:
            # date:2011/11/17 (木) time:06:41
            # counter measure for  p=oc.Pl([1,2,3,4], O7); p( oc.Pl([1,2,3],O7) )
            try:
                # 2011.11.05
                # e.g
                # lst,Z3=[0,1,2],oc.Zp(3); f=λ j,k,l,m:oc.Oc(~[j,k,l,m, Z3]); f(0,1,2,3)+Z3(2) 
                lstAt = list(self.m_tpl)
                lstAt[0] = lstAt[0] + ag
                return type(self)(lstAt)
            except:
                return ag.__radd__(self)

    def __radd__(self, ag):
        if isinstance(ag, ClOctonion):
            return type(self)([ag.m_tpl[i] + self.m_tpl[i] for i in range(8)])
        elif isinstance(ag, (int, float) ):
            lstAt = list(self.m_tpl)
            lstAt[0] = ag + lstAt[0]
            return type(self)(lstAt)
        elif isinstance(ag, complex):
            lstAt = list(self.m_tpl)
            lstAt[0] = ag.real + lstAt[0]
            lstAt[1] = ag.imag + lstAt[1]
            return type(self)(lstAt)
        elif isinstance(ag, (list,tuple, sf.sc.ndarray, sf.ClFldTns) ):
            assert len(ag) <= 8
            lstAt = list(self.m_tpl)
            for k in range(len(ag)):
                lstAt[k] = ag[k] + lstAt[k]
            return type(self)(lstAt)
        else:
            # 2011.11.05
            # e.g
            # lst,Z3=[0,1,2],oc.Zp(3); f=λ j,k,l,m:oc.Oc(~[j,k,l,m, Z3]); f(0,1,2,3)+Z3(2) 
            lstAt = list(self.m_tpl)
            lstAt[0] = ag + lstAt[0]
            return type(self)(lstAt)

    def __sub__(self, ag):
        if isinstance(ag, ClOctonion):
            return type(self)([self.m_tpl[i] - ag.m_tpl[i] for i in range(8)])
        elif isinstance(ag, (int, float) ):
            lstAt = list(self.m_tpl)
            lstAt[0] = lstAt[0] - ag
            return type(self)(lstAt)
        elif isinstance(ag, complex):
            lstAt = list(self.m_tpl)
            lstAt[0] = lstAt[0] - ag.real 
            lstAt[1] = lstAt[1] - ag.imag 
            for k in range(2,8):
                lstAt[k] = -lstAt[k]
            return type(self)(lstAt)
        elif isinstance(ag, (list,tuple, sf.sc.ndarray, sf.ClFldTns) ):
            assert len(ag) <= 8
            lstAt = list(self.m_tpl)
            for k in range(len(ag)):
                lstAt[k] = lstAt[k] - ag[k]
            return type(self)(lstAt)
        else:
            # 2011.11.06
            # e.g
            # lst,Z3=[0,1,2],oc.Zp(3); f=λ j,k,l,m:oc.Oc(~[j,k,l,m, Z3]); f(0,1,2,3)-Z3(2) 
            lstAt = list(self.m_tpl)
            lstAt[0] = lstAt[0] - ag
            return type(self)(lstAt)

    def __rsub__(self, ag):
        if isinstance(ag, ClOctonion):
            return type(self)([ag.m_tpl[i]- self.m_tpl[i] for i in range(8)])
        elif isinstance(ag, (int, float) ):
            lstAt = list(self.m_tpl)
            lstAt[0] = ag - lstAt[0]
            for k in range(1,8):
                lstAt[k] = -lstAt[k]
            return type(self)(lstAt)
        elif isinstance(ag, complex):
            lstAt = list(self.m_tpl)
            lstAt[0] = ag.real - lstAt[0]
            lstAt[1] = ag.imag - lstAt[1]
            for k in range(2,8):
                lstAt[k] = -lstAt[k]
            return type(self)(lstAt)
        elif isinstance(ag, (list,tuple, sf.sc.ndarray, sf.ClFldTns) ):
            assert len(ag) <= 8
            lstAt = list(self.m_tpl)
            for k in range(len(ag)):
                lstAt[k] = ag[k] - lstAt[k]
            return type(self)(lstAt)
        else:
            # 2011.11.06
            # e.g
            # lst,Z3=[0,1,2],oc.Zp(3); f=λ j,k,l,m:oc.Oc(~[j,k,l,m, Z3]); Z3(2) - f(1,1,2,3)
            lstAt = list(self.m_tpl)
            lstAt[0] = ag - lstAt[0]
            for k in range(1,8):
                lstAt[k] = -lstAt[k]
            return type(self)(lstAt)

    def __neg__(self):
        lstAt = list(self.m_tpl)
        for k in range(8):
            lstAt[k] = -lstAt[k]
        return type(self)(lstAt)

    def __mul__(self, ag):
        lstAt = [0]*8
        if isinstance(ag, (int, float, complex) ):
            return type(self)([self.m_tpl[j]*ag for j in range(8)])
        elif isinstance(ag, ClOctonion):
            for j in range(8):
                for k in range(8):
                    lstAt[dctMtPr[j,k][1]] += dctMtPr[j,k][0]*self.m_tpl[j]\
                                             *ag.m_tpl[k]
            return type(self)(lstAt)
            
        elif isinstance(ag, (list,tuple) ):
            #assert len(ag) == 8
            assert 1<= len(ag) <= 8
            if len(ag)<8:
                ag = tuple(ag)+(0,)*(8-len(ag))

            for j in range(8):
                for k in range(8):
                    lstAt[dctMtPr[j,k][1]] += dctMtPr[j,k][0]*self.m_tpl[j]\
                                             *ag[k]
        
            return type(self)(lstAt)

        elif isinstance(ag, (sf.sc.ndarray, sf.ClFldTns) ):
            from ptGrp import ClZp
            if(len(ag.shape)==1) and isinstance(ag[0],(int, ClZp)):
                inLen = ag.shape[0]
                assert 1<= inLen <= 8
                if inLen<8:
                    ag = tuple(ag)+(0,)*(8-inLen)

                for j in range(8):
                    for k in range(8):
                        lstAt[dctMtPr[j,k][1]] += dctMtPr[j,k][0]*self.m_tpl[j]\
                                                 *ag[k]
            
                return type(self)(lstAt)
            else:
                return ag.__rmul__(self)

        else:
            # date:2011/11/17 (木) time:06:41
            # counter measure for  p=oc.Pl([1,2,3,4], O7); p( oc.Pl([1,2,3],O7) )
            try:
                # 2011.11.05
                # e.g
                # lst,Z3=[0,1,2],oc.Zp(3); f=λ j,k,l,m:oc.Oc(~[j,k,l,m, Z3]); f(0,1,2,3) Z3(2) 
                lstAt = [self.m_tpl[j] * ag for j in range(8)]
                return type(self)(lstAt)

            except AssertionError, errValAt:
                return ag.__rmul__(self)


    def __rmul__(self, ag):
        lstAt = [0]*8
        if isinstance(ag, (int, float, complex) ):
            return type(self)([ag * self.m_tpl[j] for j in range(8)])
        elif isinstance(ag, ClOctonion):
            for j in range(8):
                for k in range(8):
                    lstAt[dctMtPr[j,k][1]] += dctMtPr[j,k][0]*ag.m_tpl[j]\
                                             *self.m_tpl[k]
            
        elif isinstance(ag, (tuple, list, sf.sc.ndarray, sf.ClFldTns)):
            assert 1<= len(ag) <= 8
            if len(ag)<8:
                ag = tuple(ag)+(0,)*(8-len(ag))
            
            for j in range(8):
                for k in range(8):
                    lstAt[dctMtPr[j,k][1]] += dctMtPr[j,k][0]*ag[j]\
                                             *self.m_tpl[k]
        else:
            # 2011.11.05
            # e.g
            # lst,Z3=[0,1,2],oc.Zp(3); f=λ j,k,l,m:oc.Oc(~[j,k,l,m, Z3]); Z3(2) f(0,1,2,3)
            lstAt = [ag * self.m_tpl[j] for j in range(8)]

        return type(self)(lstAt)

    def square(self):
        return sum([self.m_tpl[j]*self.m_tpl[j] for j in range(8)])

    def abs(self):
        return self.square()**0.5
    def __abs__(self):
        return self.square()**0.5

    def inv(self):
        sqAt = sum(self * self.conj())
        if isinstance(sqAt, (int,long)):
            # if sqAt is int then octAt.m_tpl[j]/sqAt becomes a integer value.
            # then does // operation
            # if sqAt is Zp(N) then can't do float(...) operation.
            sqAt = float(self.square())
        #sqAt = float(self.square())
        if sqAt == 0:
            raise ZeroDivisionError("Square value is 0 at ClOctonion:inv().")
        octAt = type(self)(self)
        octAt = conj(octAt)
        octAt.m_tpl = tuple([octAt.m_tpl[j]/sqAt for j in range(8)])
        return octAt

    def __pow__(self, ag):
        assert isinstance(ag, int)
        if ag == 0:
            return  type(self)([1,0,0,0, 0,0,0,0])
        elif ag > 0:
            octAt = type(self)(self)
            for _ in range(1,ag):
                octAt = octAt * self
            return octAt
        else:
            octAt = type(self)(self)
            rtnAt = octAt = octAt.inv()
            for _ in range(1,-ag):
                rtnAt = rtnAt * octAt
            return rtnAt

    def __div__(self, ag):
        #import pdb; pdb.set_trace()
        if isinstance(ag, int):
            assert ag != 0
            return type(self)([self.m_tpl[j]/float(ag) for j in range(8)])
        elif isinstance(ag, float) or isinstance(ag, complex):
            assert ag != 0
            return type(self)([self.m_tpl[j]/ag for j in range(8)])
        elif isinstance(ag, ClOctonion):
            octAt = type(self)(ag)
            octAt = octAt.inv()
            return self*octAt
        else:
            lstAt = [self.m_tpl[j]/ag for j in range(8)]
            return type(self)(lstAt)

    def __truediv__(self, ag):
        #import pdb; pdb.set_trace()
        if isinstance(ag, int):
            assert ag != 0
            return type(self)([self.m_tpl[j]/float(ag) for j in range(8)])
        elif isinstance(ag, float) or isinstance(ag, complex):
            assert ag != 0
            return type(self)([self.m_tpl[j]/ag for j in range(8)])
        elif isinstance(ag, ClOctonion):
            octAt = type(self)(ag)
            octAt = octAt.inv()
            return self*octAt
        else:
            lstAt = [self.m_tpl[j]/ag for j in range(8)]
            return type(self)(lstAt)

    def __rdiv__(self, ag):
        #import pdb; pdb.set_trace()
        octAt = ClOctonion(self)
        octAt = octAt.inv()
        if isinstance(ag, int):
            return ag*octAt
        elif isinstance(ag, float) or isinstance(ag, complex):
            return ag*octAt
        elif isinstance(ag, ClOctonion):
            return self*octAt
        else:
            return ag*octAt

    def __rtruediv__(self, ag):
        #import pdb; pdb.set_trace()
        octAt = ClOctonion(self)
        octAt = octAt.inv()
        if isinstance(ag, int):
            return ag*octAt
        elif isinstance(ag, float) or isinstance(ag, complex):
            return ag*octAt
        elif isinstance(ag, ClOctonion):
            return self*octAt
        else:
            return ag*octAt

    def __eq__(self, ag):
        if isinstance(ag, ClOctonion):
            return self.m_tpl == ag.m_tpl
        elif isinstance(ag, int) or isinstance(ag, float):
            return (self.m_tpl[1:] == (0,0,0, 0,0,0,0)) and (self.m_tpl[0]==ag)
        elif isinstance(ag, complex):
            return (self.m_tpl[2:] == (0,0, 0,0,0,0))\
                    and (self.m_tpl[0:2]==(ag.real,ag.imag))
        elif isinstance(ag, BF):
            return (self.m_tpl[1:] == (0,0,0, 0,0,0,0)) and (self.m_tpl[0]==ag)
        else:
            from ptGrp import ClZp
            if isinstance(ag, ClZp):
                return (self.m_tpl[1:] == (0,0,0, 0,0,0,0)) and (self.m_tpl[0]==ag)
            else:
                return False
        """'
        elif isinstance(ag, int) or isinstance(ag, float):
            return (self.m_tpl[1:] == (0,0,0, 0,0,0,0)) and (self.m_tpl[0]==ag)
        elif isinstance(ag, int) or isinstance(ag, complex):
            return (self.m_tpl[2:] == (0,0, 0,0,0,0))\
                    and (self.m_tpl[0:2]==(ag.real,ag.imag))
        elif isinstance(ag, (type,type(None)) ):
            # assert isinstance(ag,(int, BF) )
            # at "BF(1) in (bool, int, float) " ag == bool ... and upper error
            return False
        elif not hasattr(ag, '__len__'):
            # append 2011.10.15
            # ag is sclar
            # e.g.
            #   oc.Oc(1,0,0,0, oc.BF) == `1
            if self.m_tpl[0] == ag:
                for elm in self.m_tpl[1:]:
                    if elm != 0:
                        return False

                return True
            else:
                return False
        elif len(ag) == 4:
            return (self.m_tpl[4:] == (0,0,0,0))\
                    and (self.m_tpl[0:4] == tuple(ag))
        else:
            tplAt = tuple(ag)
            lenAt = len(tplAt)
            assert lenAt <= 8
            if len == 8:
                return self.m_tpl == tplAt
            else:
                if (self.m_tpl[:lenAt] == tplAt):
                    return self.m_tpl[lenAt:] == (0,)*(8-lenAt)
                else:
                    return False
        '"""

    def __ne__(self, ag):
        return not(self.__eq__(ag))

    def __lt__(self, ag):
        if isinstance(ag, ClOctonion):
            return self.m_tpl < ag.m_tpl
        elif isinstance(ag, int) or isinstance(ag, float):
            return self.m_tpl[0] < ag
        elif isinstance(ag, complex):
            if ag.imag == 0:
                return self.m_tpl[0] < ag.real
            else:
                assert False, ("You compared complex val:"+ str(ag)
                              +" with ClOctonion instance.")
        else:
            return False
    """'

    '"""

    def __hash__(self):
        """' __hash__(..) is used by set container's methods'"""
        return hash(self.m_tpl)

    def __getitem__(self, *ag):
        return self.m_tpl.__getitem__(*ag)

    #def conj(self, *ag):
    def conj(self):
        lstAt = [0]*8
        lstAt[0] = self.m_tpl[0]
        for j in range(1,8):
            lstAt[j] = -self.m_tpl[j]
        return type(self)(lstAt)

    def __getattr__(self, name):
        if name == "d":
            return self.conj()
        else:
            raise AttributeError
            #assert False,("At ClOcternion instance, you tried to get a unexpected "
            #            + "attribute:" + name)

def conj(octAg):
        assert isinstance(octAg, ClOctonion)
        lstAt = [0]*8
        lstAt[0] = octAg.m_tpl[0]
        for j in range(1,8):
            lstAt[j] = -octAg.m_tpl[j]
        return type(octAg)(lstAt)

Oc =  ClOctonion
"""' Oc is alias name of ClOctonion
'"""

# GF(2^8) Galois Field 
# primitive polynomial  x^8 + x^4 + x^3 + x^2 + 1:0x1d
# used at CD/DVD Reed Solomon Code
class RS(object):
    """' GF(2^8) for primitive polynomial:x^8 + x^4 + x^3 + x^2 + 1:0x1d
    RS.m_lstPwrStt has power values
    e.g;; oc.RS.m_lstPwrStt
    [1, 2, 4, 8, 16, 32, 64, 128, 29, 58, ... 173, 71, 142]

    oc.RS(0x12) + oc.RS(0x43)
    ===============================
    0x51

    oc.RS(0x12) - oc.RS(0x43)
    ===============================
    0x51
 
    oc.RS(24) oc.RS(31)
    ===============================
    0x15

    oc.RS(24)/oc.RS(31)
    ===============================
    0xd7

    oc.RS(2)^8
    ===============================
    0x1d

    oc.RS(2)^-8
    ===============================
    0x83

    ~[ [1,2],[3,4], oc.RS]^-1
    ===============================
    [[0x02 0x01]
     [0x8f 0x8e]]

    oc.RS.m_lstPwrStt.index(24)
    ===============================
    28

    oc.RS.m_lstPwrStt.index(31)
    ===============================
    113

    hex(oc.RS.m_lstPwrStt[28+113])
    ===============================
    0x15
    '"""
    m_lstPwrStt = []
    val = 0x01
    # make the GF(2^8) table at class declaration timing
    #m_lstPwrStt.append(0x00)    # m_lstPwrStt[index] == alpha^index 

    #for damie in range(256-2):
    for damie in range(256-1):
        m_lstPwrStt.append(val)
        val = val << 1
        if val & 0x100 == 0x100:
            val = (val & 0xff) ^ 0x1d

    #print "debug:", m_lstPwrStt
    #print "debug:", [hex(x) for x in m_lstPwrStt]
    def __init__(self, inAg):
        if isinstance(inAg, RS):
            inAg = inAg.m_val
        self.m_val = int(abs(inAg))%256

    def __add__(self, inAg):
        if isinstance(inAg,RS):
            inAg = inAg.m_val
        return RS(self.m_val ^ (inAg % 256))

    def __radd__(self, ag):
        return self.__add__(ag)

    def __sub__(self, ag):
        return self.__add__(ag)

    def __rsub__(self, ag):
        return self.__add__(ag)

    def __neg__(self):
        return RS(self.m_val)

    def __mul__(self, inAg):
        if isinstance(inAg,RS):
            inAg = inAg.m_val
        elif isinstance(inAg, (int, long)):
            pass
        else:
            # inAg may be ClFldTns
            return inAg.__rmul__(self)

        if (inAg % 256 == 0):
            return RS(0)

        if self.m_val == 0:
            return RS(0)

        idxLeftAt = RS.m_lstPwrStt.index(self.m_val)
        idxRightAt = RS.m_lstPwrStt.index(inAg % 256)
        return RS(RS.m_lstPwrStt[(idxLeftAt + idxRightAt)%255])

    def __rmul__(self, ag):
        return self.__mul__(ag)

    def __div__(self, inAg):
        if isinstance(inAg,RS):
            inAg = inAg.m_val

        if (inAg % 256 == 0):
            raise ZeroDivisionError("0 divition at __div__(.)")

        if self.m_val == 0:
            return RS(0)

        idxLeftAt = RS.m_lstPwrStt.index(self.m_val)
        idxRightAt = RS.m_lstPwrStt.index(inAg % 255)
        return RS(RS.m_lstPwrStt[(idxLeftAt - idxRightAt)%255])

    def __truediv__(self, inAg):
        if isinstance(inAg,RS):
            inAg = inAg.m_val

        if (inAg % 256 == 0):
            ZeroDivisionError("0 divition at __div__(.)")

        if self.m_val == 0:
            return RS(0)

        idxLeftAt = RS.m_lstPwrStt.index(self.m_val)
        idxRightAt = RS.m_lstPwrStt.index(inAg % 255)
        return RS(RS.m_lstPwrStt[(idxLeftAt - idxRightAt)%255])

    def __rdiv__(self, ag):
        valAt = RS(self.m_val)
        valAt = valAt.inv()
        if isinstance(ag, int):
            return RS(ag)*valAt
        elif isinstance(ag, RS):
            return ag*valAt
        else:
            assert False, "Not supposed argment at RS:__div__:"+ str(ag)

    def __rtruediv__(self, ag):
        return self.__rdiv__(ag)

    def __pow__(self, ag):
        if isinstance(ag,RS):
            ag = ag.m_val
        else:
            assert isinstance(ag, int)

        if ag == 0:
            return RS(1)
        elif ag > 0:
            rsAt = RS(self)
            for dummy in range(ag - 1):
                rsAt = rsAt * self
            return rsAt
        else:
            # ag < 0
            ag = -ag

            rsAt = self.inv()
            rightAt = RS(rsAt)
            for dummy in range(ag - 1):
                rsAt = rsAt * rightAt
            return rsAt

    def inv(self):
        """' Return inverse instance '"""
        if self.m_val % 256 == 0:
            raise ZeroDivisionError("0 divition at inv(.)")

        idxAt = RS.m_lstPwrStt.index(self.m_val)
        return RS( RS.m_lstPwrStt[(-idxAt) % 255] )
        

    def __eq__(self, ag):
        if isinstance(ag,int):
            return self.m_val == ag
        elif isinstance(ag,RS):
            return self.m_val == ag.m_val
        #elif isinstance(ag,type):
            # compare with type is used in sf.krry([oc.RS(0), oc.RS(1)])
        #    return False
        else:
            # RS(1) == None # NoneType etc.
            return False
    
    def __ne__(self, ag):
        return not(self.__eq__(ag))

    def __repr__(self):
        return "RS(" + str(self) + ")"

    def __str__(self):
        strAt = hex(self.m_val)
        if len(strAt)<4:
            strAt = "0x0"+strAt[-1]
        return strAt

    def __hash__(self):
        """' __hash__(..) is used by set container's methods'"""
        return self.m_val % 256

    def __lt__(self, ag):
        if isinstance(ag, RS):
            return self.m_val < ag.m_val
        elif isinstance(ag, int) or isinstance(ag, float):
            return self.m_val < ag
        elif isinstance(ag, complex):
            if ag.imag == 0:
                return self.m_val < ag.real
            else:
                assert False, ("You compared complex val:"+ str(ag)
                              +" with RS instance.")
        else:
            return False

GF28=RS
"""' Oc is an alias for ClOctoniton '"""

def Zp(N=7):
    """' make prime field class: class factory
        e.g. 
        Z7 = oc.Zp(7); Z7(2) + Z7(5) == 0
    '"""
    class ClZp(object):
        # use static integer m_NStt to be refered by users
        # but only looking at
        assert isinstance(N, (int, long) ) and (int(N) != 0)
        m_NStt = N

        def __init__(self, ag):
            if isinstance(ag, (int,long) ):
                self.m_val = int(ag % N)
            elif isinstance(ag, ClZp):
                self.m_val = int(ag.m_val)%N
            elif hasattr(ag,'__int__') and not isinstance(ag,type):
                # bool type has __int__
                self.m_val = int(ag)%N
            else:
                assert False, ("At __init__ in ClZp, Unexpected argment:"
                              +str(ag) )

        def __add__(self, ag):
            if isinstance(ag, (sf.ClFldTns, ClOctonion)):
                return ag.__radd__(self)
            elif isinstance(ag, (int,long) ):
                return ClZp( (self.m_val + ag)%N)
            elif isinstance(ag, ClZp):
                return ClZp( (self.m_val + ag.m_val)%N)
            else:
                return ClZp( (self.m_val + int(ag))%N)

        def __radd__(self, ag):
            if isinstance(ag, (sf.ClFldTns, ClOctonion)):
                return ag.__add__(self)
            elif isinstance(ag, (int,long) ):
                return ClZp( (self.m_val + ag)%N)
            elif isinstance(ag, ClZp):
                return ClZp( (self.m_val + ag.m_val)%N)
            else:
                return ClZp( (self.m_val + int(ag))%N)

        def __sub__(self, ag):
            if isinstance(ag, (sf.ClFldTns, ClOctonion)):
                return ag.__rsub__(self)
            elif isinstance(ag, (int,long) ):
                return ClZp( (self.m_val - ag)%N)
            elif isinstance(ag, ClZp):
                return ClZp( (self.m_val - ag.m_val)%N)
            else:
                # ClFldTns, ClOctonion, int, ClZp 以外との組み合わせ動作は保障できない
                # 下で動かしておく
                return ClZp( (self.m_val - int(ag))%N)

        def __rsub__(self, ag):
            if isinstance(ag, (sf.ClFldTns, ClOctonion)):
                return ag.__sub__(self)
            elif isinstance(ag, (int,long) ):
                return ClZp( (ag - self.m_val)%N)
            elif isinstance(ag, ClZp):
                return ClZp( (ag.m_val - self.m_val)%N)
            else:
                # ClFldTns, ClOctonion, int, ClZp 以外との組み合わせ動作は保障できない
                # 下で動かしておく
                return ClZp( (int(ag) - self.m_val)%N)

        def __mul__(self, ag):
            if isinstance(ag, sf.ClFldTns):
                return ag.__rmul__(self)
            elif isinstance(ag, (int,long)):
                return ClZp( (self.m_val * ag)%N)
            elif isinstance(ag, ClZp):
                return ClZp( (self.m_val * ag.m_val)%N)
            else:
                return ag.__rmul__(self)
                #assert False

        def __rmul__(self, ag):
            return self.__mul__(ag)

        def __div__(self, ag):
            if isinstance(ag, (sf.ClFldTns, ClOctonion)):
                return ag.__rdiv__(self)
            elif isinstance(ag, (int,long)):
                pass
            elif isinstance(ag,ClZp):
                ag = ag.m_val
            else:
                assert False, "At __div__(.) in ClZp, Unexpected argment:"+str(ag)
    
            if (ag % N == 0):
                raise ZeroDivisionError("0 division at __div__(.)")
    
            #inAt = None
            #for i in range(1,N):
            #    if (ag * i)%N == 1:
            #        inAt = i
            #        break
            #assert not (inAt == None)
            #return ClZp( (self.m_val * inAt)%N)
            
            # x^(N-1) == 1 mod N;;Fermat's Little theorem;;
            return ClZp( self.m_val*(ag**(N-2))%N)

        def __truediv__(self, ag):
            return self.__div__(ag)

        def __rdiv__(self, ag):
            if isinstance(ag, (sf.ClFldTns, ClOctonion)):
                return ag.__div__(self)
            else:
                return ClZp(ag)/self
            #return self.__div__(ag)

        # countermeasure for TypeError: "unsupported operand type(s) 
        # for /: 'int' and 'ClZp'Z=oc.Zp(5);1/Z(2)" 09.01.13
        def __rtruediv__(self, ag):
            return self.__rdiv__(ag)

        def __neg__(self):
            return ClZp(( N-self.m_val)%N )

        def __int__(self):
            return self.m_val

        # array needs __long__ 
        # e.g. ;;mt = kzrs(3,3,int); mt[0,1] = oc.Zp(3)(1);mt
        def __long__(self):
            return self.m_val

        def inv(self):
            if self.m_val % N == 0:
                raise ZeroDivisionError("0 divition at inv(.)")
    
            return ClZp(self.m_val**(N-2)%N)

        def __pow__(self, ag):
            if isinstance(ag,ClZp):
                ag = ag.m_val
            elif isinstance(ag, (int,long) ):
                pass
            else:
                assert False, ("At __pow__(.) in octn.ClZp, "
                                + "Unexpected argment:"+str(ag) )

            if ag == 0:
                return ClZp(1)
            elif ag > 0:
                rsAt = ClZp(self)
                for dummy in range(ag - 1):
                    rsAt = rsAt * self
                return rsAt

            else:
                # ag < 0
                ag = -ag

                rsAt = self.inv()
                rightAt = ClZp(rsAt)
                for dummy in range(ag - 1):
                    rsAt = rsAt * rightAt
                return rsAt

        def __eq__(self, ag):
            if isinstance(ag,int):
                return (self.m_val - ag)% N == 0
            elif isinstance(ag, ClZp):
                return (self.m_val - ag.m_val)% N == 0
            elif hasattr(ag, '__int__') and not isinstance(ag,type):
                return (self.m_val - int(ag))% N == 0
            else:
                #assert False, ("At __eq__(.) in octn.ClZp, "
                #                + "Unexpected argment:"+str(ag) )
                return False

        def __ne__(self, ag):
            return not(self.__eq__(ag))

        def __repr__(self):
            sizeAt = len(str(int(N)))
            strAt = str(self.m_val)
            if len(strAt) < sizeAt:
                strAt = " "*(sizeAt-len(strAt)) + strAt
            return strAt

        def __abs__(self):
            return self.m_val

        def __hash__(self):
            """' __hash__(..) is used by set container's methods'"""
            return self.m_val

    return ClZp


"""' 
We can't use BF(Zp(2)) becuase __add__, __mul__ .. return Zp not BF. 
So we can't pickle a calculation result of BF as BF(1) + BF(1)

class BF_dontUse(Zp(2)):
         Bool Field 
        `1 * `0 = `0   # and
        `1 * `1 = `1
        `0 * `0 = `0

        `1 + `0 = `1   # xor
        `1 + `1 = `0
        `0 + `0 = `0
    def __str__(self):
        if self.m_val == 0:
            return "0"
        else:
            return "1"

    def __repr__(self):
        if self.m_val == 0:
            return "BF(0)"
        else:
            return "BF(1)"
'"""
# Bool Field 
class BF(object):
    """' Bool Field: data member is 1 or 0
        `1 * `0 = `0   # and
        `1 * `1 = `1
        `0 * `0 = `0

        `1 + `0 = `1   # xor
        `1 + `1 = `0
        `0 + `0 = `0
    '"""
    def __init__(self, inAg):
        #if isinstance(inAg,int):
        if hasattr(inAg,'__int__'):
            self.m_val = int(inAg)%2
        elif isinstance(inAg,BF):
            self.m_val = inAg.m_val
        else:
            assert False

    def __int__(self):
        return self.m_val

    # array needs __long__ 
    # e.g. ;;mt = kzrs(3,3,int); mt[0,1] = oc.BF(1);mt
    def __long__(self):
        return self.m_val

    def __add__(self, inAg):
        if isinstance(inAg,(float, int, BF) ):
            return BF(self.m_val + (int(inAg) % 2))
        else:
            return inAg.__radd__(self)

    def __radd__(self, inAg):
        return self.__add__(inAg)

    def __sub__(self, inAg):
        if isinstance(inAg, (bool, int, float)):
            inAg = BF(int(inAg))
        return self.__add__(inAg)

    def __rsub__(self, inAg):
        if isinstance(inAg, (bool, int, float)):
            inAg = BF(int(inAg))
        return self.__add__(inAg)

    def __neg__(self):
        return BF(self)

    def __rmul__(self, inAg):
        return self.__mul__(inAg)

    def __mul__(self, inAg):
        if '__int__' in dir(inAg):
            return BF(self.m_val * int(inAg))
        else:
            return inAg.__rmul__(self)


    def __div__(self, inAg):
        if hasattr(inAg, 'inv'):
            return self * inAg.inv()
        else:
            assert isinstance(inAg,(int, BF) )
            if ( int(inAg) % 2 == 0):
                raise ZeroDivisionError("0 divition at __div__(.)")
            else:
                return BF(self.m_val)

    def __truediv__(self, inAg):
        #return __div__(self, inAg)
        return self.__div__(inAg)

    # After from __future__ import division, __rdiv__(..) is not called
    def __rdiv__(self, inAg):
        #return __div__(self, inAg)
        #return self.__div__(inAg)
        return BF(inAg).__div__(self)
    def __rtruediv__(self, inAg):       #11.02.05 added by kobayashi
        return BF(inAg).__div__(self)

    def inv(self):
        """' inverse BF(1) '"""
        assert self.m_val != 0
        return BF(self)

    def __eq__(self, ag):
        # assert isinstance(ag,(int, BF) )
        # at "BF(1) in (bool, int, float) " ag == bool ... and upper error
        if '__int__' in dir(ag) and not isinstance(ag, type):
            return self.m_val == int(ag)%2
        else:
            return False

    def __ne__(self, ag):
        return not(self.__eq__(ag))

    def __pow__(self, inAg):
        """'
        I had introduced power operator. But there may be no need. I couldn't
        imagine any situation where bool power operator is usefull
        '"""
        assert isinstance(inAg,(int, BF) )
        if int(inAg) != 0:
            return BF(self.m_val)
        else:
            return BF(1)

    def __str__(self):
        if self.m_val == 0:
            return "0"
        else:
            return "1"

    def __repr__(self):
        if self.m_val == 0:
            return "BF(0)"
        else:
            return "BF(1)"

    def __abs__(self):
        return self.m_val

    def __lt__(self, inAg):
        return False

    def __hash__(self):
        """' __hash__(..) is used by set container's methods'"""
        return self.m_val

    def __nonzero__(self):
        return self.m_val == 1

if __name__ == '__main__':
    Z7 = Zp(7)
    print Z7(3) + Z7(5)
    print Z7(3) + 5
    print Z7(3) + 2

if __name__ == "__main__":

    clAt = ClOctonion([0,1,2,3, 4,5,6,7])
    assert (clAt+range(8)) == (0,2,4,6, 8,10,12,14)
    assert clAt * [2,0,0,0, 0,0,0,0] == (0,2,4,6, 8,10,12,14)
    assert clAt *  2                 == (0,2,4,6, 8,10,12,14)
    
    assert ( clAt * conj(clAt) ).m_tpl[0] == clAt.square()
    assert (clAt*clAt**-1).m_tpl[0] == 1
    assert 1/clAt == clAt**-1

    a = ClOctonion(range(8))
    b = ClOctonion(range(2,10))
    # x+y = a
    # x-y = b
    x = (a+b)/2
    y = (a-b)/2
    assert x+y == a
    assert x-y == b

    """'
    print clAt * range(1,9)
    
    clAt = ClOctonion([2,1,0,0, 0,0,0,0])
    print clAt*clAt**-1
    print ClOctonion(range(8))/2
    
    a = ClOctonion(range(8))
    b = ClOctonion(range(2,10))
    # x+y = a
    # x-y = b
    x = (a+b)/2
    y = (a-b)/2
    
    print x+y
    print x-y
    
    c = ClOctonion(range(5,13))
    
    print a*(b*c)
    print (a*b)*c
    print "(e1 e2) e3:",([0,1,0,0, 0,0,0,0]*ClOctonion([0,0,1,0, 0,0,0,0]))*[0,0,0,1, 0,0,0,0]
    print "e1 (e2 e3):",[0,1,0,0, 0,0,0,0]*(ClOctonion([0,0,1,0, 0,0,0,0])*[0,0,0,1, 0,0,0,0])
    '"""

    assert RS(1) + RS(2) == 0x03
    assert RS(1) - RS(2) == 0x03
    assert RS(1) * RS(2) == 0x04
    assert RS(1) / RS(2) == 0x8e


    # test BF bool field
    # constructor
    assert BF(1).m_val == 1
    assert BF(0).m_val == 0
    assert BF(3).m_val == 1
    assert BF(4).m_val == 0

    # add
    assert (BF(1) + 0).m_val == 1
    assert (BF(0) + 0).m_val == 0
    assert (BF(1) + 1).m_val == 0
    assert (BF(0) + BF(1)).m_val == 1
    assert (BF(1) + BF(0)).m_val == 1
    assert (BF(0) + BF(0)).m_val == 0
    assert (BF(1) + BF(1)).m_val == 0
    assert (BF(0) + BF(1)).m_val == 1

    # multiply
    assert (BF(1) * 0).m_val == 0
    assert (BF(0) * 0).m_val == 0
    assert (BF(1) * 1).m_val == 1
    assert (BF(0) * BF(1)).m_val == 0
    assert (BF(1) * BF(0)).m_val == 0
    assert (BF(0) * BF(0)).m_val == 0
    assert (BF(1) * BF(1)).m_val == 1
    assert (BF(0) * BF(1)).m_val == 0

    # devide
    assert (BF(1) / 1).m_val == 1
    assert (BF(1) / BF(1)).m_val == 1
    assert (BF(0) / 1).m_val == 0
    assert (BF(0) * BF(1)).m_val == 0


def Sn(N):
    """' Symmetric group Sn(N) class factory function. 
        Sn(N) return N order Symmetric Group

    Below code is assuming that theere is a line of 'import octn as oc'

        Sn(N) group element is generated with index
        Sn(N) group element has m_idx:index and m_mt:matrix data member
        Sn(N) group element has __mul__(.), inv(), __pow__(.) function
    
    S=oc.Sn(3);S(1,0,2).m_idx,S(1,0,2).m_mt
    ===============================
    ((1, 0, 2), ClTensor([[0, 1, 0],
                          [1, 0, 0],
                          [0, 0, 1]], dtype=int))


    S=oc.Sn(3);s= S(1,0,2) * S(0,2,1); s.m_idx, s.m_mt
    ===============================
    ((1, 2, 0), ClTensor([[0, 1, 0],
                          [0, 0, 1],
                          [1, 0, 0]], dtype=int))

    S=oc.Sn(3);s= S(1,0,2); s* s**-1


        Sn(N).m_tplIdxStt is a list of indices for N order Symmetric Group
        Sn(N).m_dctIdxSgnStt is a dictionary of key:indices and value:sign
    S=oc.Sn(3);S.m_tplIdxStt[0],S.m_tplIdxStt[1]
    ===============================
    ((0, 1, 2), (1, 2, 0))

    S=oc.Sn(3);S.m_dctIdxSgnStt
    ===============================
    {(2, 1, 0): -1, (0, 1, 2): 1, (1, 0, 2): -1, (2, 0, 1): 1
                                        , (0, 2, 1): -1, (1, 2, 0): 1}

    S=oc.Sn(3);[ x for x in S.m_tplIdxStt]
    ===============================
    [(0, 1, 2), (1, 2, 0), (2, 0, 1), (0, 2, 1), (1, 0, 2), (2, 1, 0)]

    '"""
    assert isinstance(N, int)

    class ClSymGrp(object):
        """' closure class for Sn(N) symmetric group class factory function
        '"""
        m_inStt = N # read only
        m_dctIdxSgnStt = dict(sf.permutate(range(N),1))

        # first half has An(N)
        m_tplIdxStt = ( tuple( sorted([idx for idx in m_dctIdxSgnStt.keys()
                                         if m_dctIdxSgnStt[idx] == 1]) )
                       +tuple( sorted([idx for idx in m_dctIdxSgnStt.keys()
                                        if m_dctIdxSgnStt[idx] == -1]) )
                      )
        def __init__(self, *tplAg):
            #if isinstance(tplAg[0], ClSymGrp):
            if isinstance(tplAg[0], Sn.m_dctCashSn[N]):
                ag = tplAg[0]
                self.m_idx = ag.m_idx
                self.m_mt  = ag.m_mt
                return
            else:
                if len(tplAg) == 1:
                    tplAg = tuple(tplAg[0])
                assert len(tplAg) == N

                self.m_idx= tuple(tplAg)
                assert self.m_idx in ClSymGrp.m_tplIdxStt

                self.m_mt=sf.kzrs(N,N,int)
                #self.m_mt=sf.kzrs(N,N, BF)

                for k in range(N):
                    #self.m_mt[k,self.m_idx[k]] = BF(1)
                    self.m_mt[k,self.m_idx[k]] = 1
                    #self.m_mt[self.m_idx[k], k] = 1

                return

        def __mul__(self, ag):
            if isinstance(ag, ClSymGrp):
                assert ag.m_inStt == N
                """'
                print "debug:self.m_mt:\n",self.m_mt
                print "debug:self.ag_mt:\n",ag.m_mt
                print "debug:self.m_mt * ag.m__mt:\n", self.m_mt * ag.m_mt
                '"""
                # I can't understand the below code line.
                #vctAt = self.m_mt * ag.m_mt * range(N)
                vctAt = ag.m_mt * self.m_mt * sf.krry(range(N),int)
                #print "debug vctAt:",vctAt
                return ClSymGrp(tuple(vctAt))
            else:
                ag = tuple(ag)
                assert ag in ClSymGrp.m_tplIdxStt
                return self * ClSymGrp(ag)

        def __call__(self, ag):
            return tuple(self.m_mt * ag)

        def __eq__(self, ag):
            if isinstance(ag, ClSymGrp):
                return self.m_idx == ag.m_idx
            else:
                assert False, ("At __eq__(.) in octn.ClSymGrp, "
                                + "Unexpected argment:"+str(ag))
        def __ne__(self, ag):
            return not(self.__eq__(ag))

        def inv(self):
            #return ClSymGrp(self.m_mt**(-1) * range(N))
            mtAt = sf.kzrs(N,N,int)
            mtAt.r[:] = self.m_mt.inv().r
            return ClSymGrp(mtAt * sf.krry(range(N),int))

        def __pow__(self, ag):
            if isinstance(ag, (int,long) ):
                pass
            else:
                assert False, ("At __pow__(.) in octn.ClSymGrp, "
                                +"Unexpected argment:"+str(ag))

            if ag == 0:
                return ClSymGrp(range(N))
            elif ag > 0:
                rsAt = ClSymGrp(self)
                for dummy in range(ag - 1):
                    rsAt = rsAt * self
                return rsAt

            else:
                # ag < 0
                ag = -ag

                rsAt = self.inv()
                rightAt = ClSymGrp(rsAt)
                for dummy in range(ag - 1):
                    rsAt = rsAt * rightAt
                return rsAt

        def __str__(self):
            return str(self.m_idx)

        def __repr__(self):
            return "Sn(" + str(N) + ")" + str(self)

        def __hash__(self):
            """' __hash__(..) is used by set container's methods'"""
            return hash(self.m_idx)

        def __getitem__(self,ag):
            return self.m_idx[ag]

        def __iter__(self):
            for elmAt in self.m_idx:
                yield elmAt

        @staticmethod
        def iter():
            for tplAt in ClSymGrp.m_tplIdxStt:
                yield ClSymGrp(tplAt)

        """'
        クラス:Sn に Sn[n] や Sn[:N/2] などのインデックス操作をさせられない
        <== sfCrrntIni.py に S3 などの集合を宣言する
        'type' object is unsubscriptable at excecuting:S3[4]
        @staticmethod
        def __getitem__(cls, ag):
            lst=[]
            for tpl in cls.m_tplIdxStt[ag]:
                lst.append(cls(tpl))
            return tuple(lst)

        下のような使い方となり、iter() は冗長
        S3=oc.Sn(3);for x in S3.iter():print x

        @staticmethod
        def iter():
            for tpl in ClSymGrp.m_tplIdxStt:
                yield ClSymGrp(tpl)
        '"""

    if not (N in Sn.m_dctCashSn):
        Sn.m_dctCashSn[N] = ClSymGrp
        # can't use list to used ClSymGrp.setStt.issubset( subsetAg)
        ClSymGrp.setStt = set([ClSymGrp(x) for x in ClSymGrp.m_tplIdxStt])
        

    return Sn.m_dctCashSn[N]
        
    #return ClSymGrp

Sn.m_dctCashSn = {}     # save Class Firm output ClSymGrp for N

import copy

class Pl(object):
    """' polynomial for algebraic coefficients
    
    usages:
        import octn as oc
        oc.Pl(1,2,3,4)                  # a integer coefficient polynomial
        =============================== # int type is estimated from paramters
        1x^3+2x^2+3x+4
    
        lst=[1,2,3,4];oc.Pl(lst)        # can use sequence argment too
        ===============================
        1x^3+2x^2+3x+4

        oc.Pl(1,2,3,4, variable='D')    # assign polynomial variable string
        ===============================
        1D^3+2D^2+3D+4
    
        oc.Pl(1,2,3,4,       oc.BF)     # assgin bool field coefficient
        ===============================
        x^3+x                           # 0 suppressed
    
        oc.Pl(1,2,3,4, dtype=oc.BF)     # assgin bool field coefficient with dtype key word
        ===============================
        x^3+x                           
    
        oc.Pl(1,2,3,`1)                 # assign type estimating from argments
        =============================== # ;;type(sum([1,2,3,`1]))   #== oc.BF
        x^3+x+1

        P=oc.Pl; P([1,2,3,4],Z3)
        ===============================
        Z3(1)x^3+Z3(2)x^2+Z3(1)

        P=oc.Pl; P([5,6,7,8],Z3)
        ===============================
        Z3(2)x^3+Z3(1)x+Z3(2)

        P=oc.Pl; P([1,2,3,4],Z3) + P([5,6,7,8],Z3)  # add
        ===============================
        Z3(2)x^2+Z3(1)x

        P=oc.Pl; P([1,2,3,4],Z3) - P([5,6,7,8],Z3)  # subtract
        ===============================
        Z3(2)x^3+Z3(2)x^2+Z3(2)x+Z3(2)

        P=oc.Pl; P([1,2,3,4],Z3) * P([5,6,7,8],Z3)  # multiply
        ===============================
        Z3(2)x^6+Z3(1)x^5+Z3(1)x^4+Z3(1)x^2+Z3(1)x+Z3(2)

        P=oc.Pl; P([1,2,3,4],Z3) / P([5,6,7,8],Z3)  # divide and (quotient,residual)
        ===============================
        (Pl(Z3(2)), Pl(Z3(2)x^2+Z3(1)x))

        P=oc.Pl; P([1,2,3,4],Z3) % P([5,6,7,8],Z3)  # residual
        ===============================
        Z3(2)x^2+Z3(1)x

        P=oc.Pl; P([1,2,3,4],Z3) // P([5,6,7,8],Z3) # quotient
        ===============================
        Z3(2)

        P=oc.Pl; P([1,2,3,4],Z3)^3                  # power
        ===============================
        Z3(1)x^9+Z3(2)x^6+Z3(1)

        P=oc.Pl; P([1,2,3,4],Z3)(P([5,6,7,8],Z3))   # composition
        ===============================
        Z3(2)x^9+Z3(2)x^6+Z3(2)x^4+Z3(2)x^3+Z3(2)x^2+Z3(2)x+Z3(2)
    '"""
    def __init__(self, *sqAg, **kwDctAg):
        #self.m_type = dtype
        if len(sqAg) == 1:
            sqAg = sqAg[0]
        
        if 'dtype' in kwDctAg:
            self.__dict__['m_type'] = kwDctAg['dtype']
        else:
            # No dtype = mapameter. 
            # sqAg last paramter may have type
            # else then we estimate the type from sqAg
            if isinstance(sqAg, (tuple, list)
                         ) and isinstance(sqAg[-1], type):
                self.__dict__['m_type'] = sqAg[-1]
                sqAg = sqAg[:-1]
                if len(sqAg) == 1:
                    sqAg = sqAg[0]
            elif isinstance(sqAg, sf.sc.poly1d):
                # Enthought2.5 can't use sum for sc.poly1d
                self.__dict__['m_type'] = type(sum(coeffs))
            elif isinstance(sqAg, (Pl, Pm, sf.ClFldTns)):
                self.__dict__['m_type'] = sqAg.m_type
            else:
                # estimate data type from the entities in sqAg
                if hasattr(sqAg, '__iter__'):
                    self.__dict__['m_type'] = type(sum(sqAg))
                else:
                    # sqAg must be solo value
                    self.__dict__['m_type'] = type(sqAg)

        if isinstance(sqAg, sf.sc.poly1d):
            sqAg = sqAg.coeffs
        elif hasattr(sqAg, '__iter__'):
            # [1,2,3], Pl, ClZ
            pass
        else:
            # Pl(1, oc.BF)
            # Use ClTensor(1,dtype=object)
            # Don't use ClTensor(1,dtype=object)
            sqAg = [sqAg]

        if self.m_type == type(None):
            assert False

        lstAt = []
        for elmAt in sqAg:
            lstAt.append(self.m_type(elmAt))
        sqAg = self._getCls().__delUpper0(lstAt)

        if 'variable' in kwDctAg:
            self.m_strVar = kwDctAg['variable']
        else:
            self.m_strVar = 'x'
        self.m_plnml = sf.krry(sqAg, self.m_type)

    
    @staticmethod
    def __delUpper0(sqAg):
        for k,elmAt in enumerate(sqAg):
            if not(elmAt == 0):
                return sqAg[k:]

        return [0]

    def _getCls(self):
        # to use __add__(..) .. etc methods in classes that have inherited Pl 
        return Pl

    def __sub__(self, other):
        if other == 0:
            return self._getCls()(self, self.m_type)

        if isinstance(other, sf.sc.poly1d):
            # list(sc.poly1d) would not return at Enghought 2.4
            lstOtherAt = other.coeffs
        elif hasattr(other, '__iter__'):
            lstOtherAt = list(other)
        else:
            # other must be scalar
            lstOtherAt = [other]

        lenPlnmlAt = len(self.m_plnml)
        lenOtherAt = len(lstOtherAt)
        if lenPlnmlAt >= lenOtherAt:
            lstRtn = [0]*lenPlnmlAt
            lstOtherAt = [0]*(lenPlnmlAt-lenOtherAt) + lstOtherAt
            for k in range(lenPlnmlAt):
                lstRtn[k] = self.m_plnml[k] - lstOtherAt[k]
        else:
            lstRtn = [0]*lenOtherAt
            lstSelfAt = [0]*(lenOtherAt-lenPlnmlAt) + list(self.m_plnml)
            for k in range(lenOtherAt):
                lstRtn[k] = lstSelfAt[k] - lstOtherAt[k]

        lstRtn = self._getCls().__delUpper0(lstRtn)
        return self._getCls()(lstRtn, self.m_type, variable = self.m_strVar)

    def __neg__(self):
        #if other == 0:
        return self._getCls()(-self.m_plnml, self.m_type)

    def __rsub__(self,other):
        if other == 0:
            return self._getCls()(-self.m_plnml, self.m_type)


        if isinstance(other, sf.sc.poly1d):
            # list(sc.poly1d) would not return at Enghought 2.4
            lstOtherAt = other.coeffs
        elif hasattr(other, '__iter__'):
            lstOtherAt = list(other)
        else:
            # other must be scalar
            lstOtherAt = [other]

        plnmlAt = -self.m_plnml
        lenPlnmlAt = len(plnmlAt)
        lenOtherAt = len(lstOtherAt)
        if lenPlnmlAt >= lenOtherAt:
            lstRtn = [0]*lenPlnmlAt
            lstOtherAt = [0]*(lenPlnmlAt-lenOtherAt) + lstOtherAt
            for k in range(lenPlnmlAt):
                lstRtn[k] = plnmlAt[k] + lstOtherAt[k]
        else:
            lstRtn = [0]*lenOtherAt
            lstSelfAt = [0]*(lenOtherAt-lenPlnmlAt) + list(plnmlAt)
            for k in range(lenOtherAt):
                lstRtn[k] = lstSelfAt[k] + lstOtherAt[k]

        lstRtn = self._getCls().__delUpper0(lstRtn)
        return self._getCls()(lstRtn, self.m_type, variable = self.m_strVar)

    def __add__(self, other):
        #import pdb; pdb.set_trace()
        if other == 0:
            return self._getCls()(self, self.m_type)

        if isinstance(other, sf.sc.poly1d):
            # list(sc.poly1d) would not return at Enghought 2.4
            lstOtherAt = other.coeffs
        elif hasattr(other, '__iter__'):
            lstOtherAt = list(other)
        else:
            # other must be scalar
            lstOtherAt = [other]

        lenPlnmlAt = len(self.m_plnml)
        lenOtherAt = len(lstOtherAt)
        if lenPlnmlAt >= lenOtherAt:
            lstRtn = [0]*lenPlnmlAt
            lstOtherAt = [0]*(lenPlnmlAt-lenOtherAt) + lstOtherAt
            for k in range(lenPlnmlAt):
                lstRtn[k] = self.m_plnml[k] + lstOtherAt[k]
        else:
            lstRtn = [0]*lenOtherAt
            lstSelfAt = [0]*(lenOtherAt-lenPlnmlAt) + list(self.m_plnml)
            for k in range(lenOtherAt):
                lstRtn[k] = lstSelfAt[k] + lstOtherAt[k]

        lstRtn = self._getCls().__delUpper0(lstRtn)
        return self._getCls()(lstRtn, self.m_type, variable = self.m_strVar)

    def __radd__(self, other):
        if other == 0:
            return self._getCls()(self, self.m_type)

        if isinstance(other, sf.sc.poly1d):
            # list(sc.poly1d) would not return at Enghought 2.4
            lstOtherAt = other.coeffs
        elif hasattr(other, '__iter__'):
            lstOtherAt = list(other)
        else:
            # other must be scalar
            lstOtherAt = [other]

        lenPlnmlAt = len(self.m_plnml)
        lenOtherAt = len(lstOtherAt)
        if lenPlnmlAt >= lenOtherAt:
            lstRtn = [0]*lenPlnmlAt
            lstOtherAt = [0]*(lenPlnmlAt-lenOtherAt) + lstOtherAt
            for k in range(lenPlnmlAt):
                lstRtn[k] = lstOtherAt[k] + self.m_plnml[k]
        else:
            lstRtn = [0]*lenOtherAt
            lstSelfAt = [0]*(lenOtherAt-lenPlnmlAt) + list(self.m_plnml)
            for k in range(lenOtherAt):
                lstRtn[k] = lstOtherAt[k] + lstSelfAt[k]

        lstRtn = self._getCls().__delUpper0(lstRtn)
        return self._getCls()(lstRtn, self.m_type, variable = self.m_strVar)

    @staticmethod
    def __mul(leftAg,rightAg, tyAg):
        assert isinstance(leftAg, (tuple, list, sf.sc.ndarray, sf.ClFldTns))
        if isinstance(rightAg, (tuple, list, sf.sc.ndarray, sf.ClFldTns)):
            lnLftAt = len(leftAg)
            vctLftAt = sf.krry(leftAg, tyAg)
            lnRgtAt = len(rightAg)
            vctRtn = sf.krry([0]*(lnLftAt+lnRgtAt-1), tyAg)
            #for j in range(lnLftAt):
            for k in range(lnRgtAt):
                vctRtn[k:k+lnLftAt] = vctRtn[k:k+lnLftAt] + vctLftAt*rightAg[k]
            return vctRtn
        else:
            # rightAg must be scalar
            vctRtn = sf.krry(leftAg, tyAg)
            vctRtn = vctRtn*rightAg
            return vctRtn

    @staticmethod
    def __rmul(leftAg,rightAg, tyAg):
        assert isinstance(leftAg, (tuple, list, sf.sc.ndarray, sf.ClFldTns))
        if isinstance(rightAg, (tuple, list, sf.sc.ndarray, sf.ClFldTns)):
            # polynomial multiply
            lnLftAt = len(leftAg)
            vctLftAt = sf.krry(leftAg, tyAg)
            lnRgtAt = len(rightAg)
            vctRtn = sf.krry([0]*(lnLftAt+lnRgtAt-1), tyAg)
            #for j in range(lnLftAt):
            for k in range(lnRgtAt):
                vctRtn[k:k+lnLftAt] += rightAg[k]*vctLftAt
            return vctRtn
        else:
            # rightAgg must be scalar
            """'
            date:2011/11/17 (木) time:13:24
            vctRtn = sf.krry(leftAg, tyAg)
            vctRtn = rightAg*vctRtn
            return vctRtn
            '"""
            lstAt=[ rightAg * elm for elm in leftAg]
            return sf.krry(lstAt, tyAg)

    def __rmul__(self, other):
        if isinstance(other, (Pl, Pm) ):
            return self._getCls()( self._getCls().__mul(other.m_plnml, self.m_plnm,self.m_type)
                        ,dtype = self.m_type
                        ,variable = self.m_strVar)
        else:
            if self.m_type == type(None):
                return self._getCls()( self._getCls().__rmul(self.m_plnml, other,self.m_type )
                        ,dtype = self.m_type
                        ,variable = self.m_strVar)
            else:
                return self._getCls()( self._getCls().__rmul(
                                    self.m_plnml,self.m_type(other),self.m_type )
                        ,dtype = self.m_type
                        ,variable = self.m_strVar)

    def __mul__(self, other):
        if isinstance(other, Pl):
            return self._getCls()( Pl.__mul(self.m_plnml, other.m_plnml, self.m_type)
                        ,dtype = self.m_type
                        ,variable = self.m_strVar)
        elif isinstance(other, (sf.ClFldTns, sf.sc.ndarray) ):
            return other.__rmul__(self)
        else:
            #return Pl( Pl.__mul(self.m_plnml, othe,self.m_typer) )
            #return Pl( Pl.__mul(self.m_plnml, self.m_type(other),self.m_type ) )
            """'
            '"""
            if self.m_type == type(None):
                return self.__class( self.__class.__mul(self.m_plnml, other,self.m_type )
                        ,dtype = self.m_type
                        ,variable = self.m_strVar)
            else:
                return self._getCls()( self._getCls().__mul(
                                    self.m_plnml, self.m_type(other),self.m_type )
                        ,dtype = self.m_type
                        ,variable = self.m_strVar)

    def __pow__(self, inAg):
        if inAg > 0:
            plRtn = [self.m_type(1)]
            for k in range(inAg):
                plRtn = self._getCls().__mul(plRtn, self.m_plnml, self.m_type)

            return self._getCls()(plRtn, dtype=self.m_type, variable=self.m_strVar)
        elif inAg == 0:
            return self._getCls()(self.m_type(1), dtype=self.m_type
                                    , variable=self.m_strVar)
        else:
            assert False, ("You set negative parameter in Pl.__pow__():"
                          +str(inAg) )

    def __truediv__(self, other):
        #import pdb; pdb.set_trace()
        #return self.__div(other)
        if hasattr(other, 'inv'):
            return self * other.inv()
        else:
            if isinstance(other, (sf.sc.poly1d, Pl, Pm) ):
                other = other.coeffs

            if hasattr(other, '__iter__'):
                other = list(other)
                return self.__div__(other)
            else:
                return self._getCls()(self.coeffs/other
                            ,dtype = self.m_type
                            ,variable = self.m_strVar)

    def __rtruediv__(self, other):
        if hasattr(other, 'inv'):
            return self * other.inv()
        else:
            if isinstance(other, (sf.sc.poly1d, Pl, Pm) ):
                other = other.coeffs

            if hasattr(other, '__iter__'):
                other = self._getCls()(other
                        ,dtype = self.m_type
                        , variable = self.m_strVar)
                return other.__div__(self)
            else:
                assert False, ("We dont support '/' operation for "
                              + str(other) + "/" + str(self) )
                """'
                lstAt = []
                for k, elmAt in enumerate(self.m_plnml.coeffs):
                    lstAt = other * elmAt**(-1)
                return self._getCls()(lstAt
                        ,dtype = self.m_type
                        , variable = self.m_strVar)
                '"""

    def __div__(u, v):
        """Computes q and r polynomials so that u(s) = q(s)*v(s) + r(s)
        and deg r < deg v.
        """
        #import pdb; pdb.set_trace()
        if hasattr(v, 'inv'):
            return self * v.inv()
        else:
            if isinstance(v, Pl):
                v = v.m_plnml

            uAt = u
            strVarAt = u.m_strVar
            typeAt = u.m_type
            u = u.m_plnml

            if not(hasattr(u, '__iter__')) and not(hasattr(v, '__iter__')):
                # u and v argments are scalar too
                return self._getCls()(u/v)

            if (hasattr(u, '__iter__')):
                if isinstance(u, sf.sc.poly1d):
                    lstU = u.coeffs
                else:
                    lstU = list(u)
            else:
                lstU = [u]

            if (hasattr(v, '__iter__')):
                if isinstance(v, sf.sc.poly1d):
                    lstV = v.coeffs
                else:
                    lstV = list(v)
            else:
                lstV = [v]

            m = len(lstU) - 1
            n = len(lstV) - 1

            # We must calculate __div__ for monic ring polynomials
            scale = 1/ lstV[0]
            assert lstV[0] == 1/scale, "You set a non field parameter:"+str(lstV)+"at Pl.__div__."
            
            lstQ = [0]*max(m-n+1,1)
            lstR = copy.copy(lstU)

            for k in range(m-n+1):
                d = scale * lstR[k]
                lstQ[k] = d
                for kk in range(k, k+n+1):
                    lstR[kk] = lstR[kk] - d*lstV[kk-k]

            # delete upper 0 terms in remainder
            for k in range(m+1):
                if not (lstR[k] == 0):
                    break
            lstR = lstR[k:]

            #import pdb; pdb.set_trace()
            return (uAt._getCls()(lstQ,dtype = typeAt, variable=strVarAt)
                    , uAt._getCls()(lstR,dtype = typeAt, variable=strVarAt))

    def __floordiv__(u, v):
        return u.__div__(v)[0]

    def __mod__(u, v):
        """Computes modulo for q and r polynomials so that 
                u(s) = some(s)*v(s) + r(s)
                deg r < deg v.
        and return r
        """
        #import pdb; pdb.set_trace()
        if isinstance(v, Pl):
            v = v.m_plnml

        uAt = u
        strVarAt = u.m_strVar
        typeAt = u.m_type
        u = u.m_plnml

        if not(hasattr(u, '__iter__')) and not(hasattr(v, '__iter__')):
            # u and v argments are scalar too
            return self._getCls()(u/v)

        if (hasattr(u, '__iter__')):
            if isinstance(u, sf.sc.poly1d):
                lstU = u.coeffs
            else:
                lstU = list(u)
        else:
            lstU = [u]

        if (hasattr(v, '__iter__')):
            if isinstance(v, sf.sc.poly1d):
                lstV = v.coeffs
            else:
                lstV = list(v)
        else:
            lstV = [v]

        m = len(lstU) - 1
        n = len(lstV) - 1
        scale = 1/ lstV[0]
        lstQ = [0]*max(m-n+1,1)
        lstR = copy.copy(lstU)

        for k in range(m-n+1):
            d = scale * lstR[k]
            lstQ[k] = d
            for kk in range(k, k+n+1):
                lstR[kk] = lstR[kk] - d*lstV[kk-k]

        for k in range(m+1):
            if not (lstR[k] == 0):
                break
        lstR = lstR[k:]
        #import pdb; pdb.set_trace()
        return uAt._getCls()(lstR,dtype = typeAt, variable=strVarAt)

    def __call__(self, ag):
        rtnAt = self.m_type(0)
        orderAt = self.order
        for k,elmAt in enumerate(self.m_plnml):
            at = elmAt*( ag**(orderAt-k) )
            rtnAt = rtnAt + at
        return rtnAt

    def __getattr__(self, name):
        if name == 'coeffs':
            return self.m_plnml
        elif name == 'm_plnml':
            return self.m_plnml
        elif name == 'order':
            return len(self.m_plnml)-1
        elif name == 'variable':
            return self.m_strVar
        else:
            raise AttributeError("There is no attribute in Pl:"+ name)

    def __len__(self):
        """' return polynomial degree
        '"""
        # np.poly1d と同様に -1 したものを length とする。
        #return len(self.m_plnml)
        return len(self.m_plnml) - 1

    def __iter__(self):
        return iter(self.m_plnml)
        #return iter(self.m_plnml)

    def __ne__(self, ag):
        return not(self.__eq__(ag))
    def __eq__(self, ag):
        if ag == 0:
            return len(self.m_plnml)==1 and self.m_plnml[0] == 0
        elif ag == 1:
            return len(self.m_plnml)==1 and self.m_plnml[0] == 1
        else:
            return sf.sc.alltrue(self.coeffs == ag.coeffs)

    def __repr__(self):
        return "Pl(" + self.__str__() + ")"
        """'
        #strAt = (sf.sc.poly1d.__repr__(self.m_plnml)) # poly1d(....)
        strAt = str(self.m_plnml)
        if self.m_type == type(None):
            if sf.sc.isscalar(self.m_plnml[0]):
                return "Pl" + strAt[6:-1]+ ", " + str(
                                    type(self.m_plnml[0]))[7:-2] + ")"
            else:
                return "Pl" + strAt[6:-7]+ ", " + str(
                                    type(self.m_plnml[0]))[8:-2] + ")"

        else:
            return "Pl(" + strAt[8:-(7+9)]+ ","+str(self.m_type)[8:-2] + ")"
        '"""

    def __str__(self):
        orderAt = len(self)
        strAt = ""
        #import pdb; pdb.set_trace()
        for k, elmAt in enumerate(self.coeffs):
            if elmAt == 0:
                continue
            else:
                if strAt != "":
                    strAt += "+"

                if orderAt-k == 0:
                    #strAt += str(elmAt)
                    strTmpAt = str(elmAt)
                    if strTmpAt[0] == '-':
                        strAt += '('+strTmpAt+')'
                    else:
                        strAt += strTmpAt
                else:
                    if self.m_type != BF:
                        #strAt += str(elmAt)
                        strTmpAt = str(elmAt)
                        if strTmpAt[0] == '-':
                            strAt += '('+strTmpAt+')'
                        else:
                            strAt += strTmpAt
                    strAt += self.m_strVar
                    if orderAt-k > 1:
                        strAt += "^" + str(orderAt-k)
            
        if strAt == "":
            return "0"
        else:
            return strAt

    def __hash__(self):
            """' __hash__(..) is used by set container's methods'"""
            return hash(tuple(self.m_plnml))

class Pm(Pl):
    """'
    Pm, Pl を組み合わせた加減乗除算は上手く動作しない

    def __init__(self, *sqAg, **kwDctAg):
        Pl.__init__(self, *sqAg, **kwDctAg)

    '"""

    def _getCls(self):
        return Pm

    def __repr__(self):
        return "Pm(" + self.__str__() + ")"

    def __str__(self):
        orderAt = len(self)
        strAt = ""
        #import pdb; pdb.set_trace()
        for k, elmAt in enumerate(self.coeffs[::-1]):
            if elmAt == 0:
                continue
            else:
                if strAt != "":
                    strAt += "+"

                if k == 0:
                    strAt += str(elmAt)
                else:
                    if self.m_type != BF:
                        strAt += str(elmAt)

                    strAt += self.m_strVar
                    if k > 1:
                        strAt += "^" + str(k)
            
        if strAt == "":
            return "0"
        else:
            return strAt

#z_ = Pm([1,0])

#BF = CZp(2)
#class BF(Zp(2)):pass

#import pprint as pp;pp.pprint( tn.c_.dctMtPr )

#;;octonion.py

def testF():
    return 1/BF(0)
