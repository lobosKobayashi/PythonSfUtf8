# -*- encoding: utf-8 -*-
"""'
english:
    PythonSf pysfOp/sfFnctnsOp.py
    https://github.com/lobosKobayashi
    http://lobosKobayashi.github.com/
    
    Copyright 2016, Kenji Kobayashi
    All program codes in this file was designed by kVerifierLab Kenji Kobayashi

    I release souce codes in this file under the GPLv3
    with the exception of my commercial uses.

    2016y 12m 28d Kenji Kokbayashi

japanese:
    PythonSf pysfOp/sfFnctnsOp.py
    https://github.com/lobosKobayashi
    http://lobosKobayashi.github.com/

    Copyright 2016, Kenji Kobayashi
    このファイルの全てのプログラム・コードは kVerifierLab 小林憲次が作成しました。
    
    作成者の小林本人に限っては商用利用を許すとの例外条件を追加して、
    このファイルのソースを GPLv3 で公開します。

    2016年 12月 28日 小林憲次
'"""

import numpy as np
import os

red =     (1, 0, 0)
black =   (0, 0, 0)
white =   (1, 1, 1)
red =     (1, 0, 0)
green =   (0, 1, 0)
blue =    (0, 0, 1)
yellow =  (1, 1, 0)
cyan =    (0, 1, 1)
magenta = (1, 0, 1)
orange =  (1, 0.6, 0)
green =   (0, 1, 0)

vs_Float = float
def vs_():
    global __dctGlobals, vs_Float

    import visual as vs
    #if __dctGlobals == None:
    #    __dctGlobals = globals()

    __dctGlobals.update({'vs':vs})
    # visual については 「import visual as vs」だけでは足りない。 vs_Float の
    # 設定が必要になる。そのため、このモジュールでの vs ラベルを追加する。

    if hasattr(vs, 'Float'):
        vs_Float = vs.Float
    else:
        vs_Float = float
    #__dctGlobals.update({'vs_Float':vs_Float})

    return vs

def vs():
    return vs_()

nearlyZero = 1e-6

#print "At sfFnctns just before from basicFnctns import*"
from basicFnctnsOp import *
from kNumericOp import *
from vsGraphOp import *
from rationalOp import *

__dctGlobals=globals()
def setDctGlobals(dctGlobalsAg):
    global __dctGlobals
    __dctGlobals = dctGlobalsAg

def __getDctGlobals():
    return __dctGlobals

def sy_():
    global __dctGlobals
    #if __dctGlobals == None:
    #    __dctGlobals = globals()
    import scipy as sy
    __dctGlobals.update({'sy':sy})

    so_()
    si_()
    sl_()
    ss_()
    sg_()

    return sy

def sy():
    return sy_()

def so_():
    global __dctGlobals
    import scipy.optimize as so
    __dctGlobals.update({'so':so})
    return so

def si_():
    global __dctGlobals
    import scipy.integrate as si
    __dctGlobals.update({'si':si})
    return si

def sl_():
    global __dctGlobals
    import scipy.linalg as sl
    __dctGlobals.update({'sl':sl})
    return sl

def ss_():
    global __dctGlobals
    import scipy.special as ss
    __dctGlobals.update({'ss':ss})
    return ss

def sg_():
    global __dctGlobals
    import scipy.signal as sg
    __dctGlobals.update({'sg':sg})
    return sg

def sumUpArry(arAg):
    #import pdb; pdb.set_trace()
    if isinstance( arAg, (tuple, list       ) ):
        arAg = np.array(arAg, dtype = object)
    else:
        assert isinstance( arAg, (sc.ndarray           ) )
        if arAg.dtype == object:
            return object

    return sum(sc.ravel(arAg))

def kryO(*ag, **dctAg):
    """' return a np.ndarray instance
    e.g.
    '"""
    typeAt = 0  # None is used as an alternative for np.array estimation
    blFldTnsAt = False  # if blLdTnsAt become True then make ClFldTns
    if len(dctAg)==0:
        # there is a no key word:type specification
        dctAt ={}
        if ( len(ag) == 1 ):
            # e.g. kryO([1,0,3,2]) or krry([[1,2],[3,4]])
            #   or kryO([1,0,3,2, complex]) or krry([[1,2],[3,4], int])
            #   or kryO([ [0,1],[1,0], Z2])
            #   or kryO([ [Z2(0),1],[1,0], Z3])
            #   or kryO({(0,0):1, (0,1):2, (1,0):3, (1,1):4})
            #   or kryO([[0, 1.0],[1,0], Z3])
            #   or kryO(3)
            elmAt = ag[0]
            if isinstance(elmAt,( tuple,list, dict , np.ndarray) ):
                pass
            else:
                elmAt = [elmAt]

            if isinstance(elmAt, dict):
                sumValAt = sumUpArry(elmAt)
                # type(sumValAt) might be numpy.float64, numpy.complex28
                if isinstance(sumValAt, (bool, int)):
                    typeAt = float
                elif isinstance(sumValAt, float):
                    typeAt = float
                elif isinstance(sumValAt, complex):
                    typeAt = complex
                elif isinstance(sumValAt, (np.ndarray          )):
                    typeAt = object
                else:
                    typeAt = type(sumValAt)

                elmAt = np.array(elmAt)     # elmAt = ClTensor(elmAt)
            elif isinstance(elmAt, np.ndarray ):
                pass
            elif isinstance(elmAt, (tuple,list) ):
                if isinstance(elmAt[-1], type):
                    typeAt = elmAt[-1]
                    elmAt = elmAt[:-1]
                    if len(elmAt) == 1:
                        elmAt = elmAt[0]

                    """'
                    '"""
                    if not hasattr(elmAt, '__len__'):
                        # e.g [1, complex] --> elmAt == 1
                        elmAt = [elmAt]

                    elmAt = np.array(elmAt, dtype=object)
                    assert len(elmAt) >= 1
                elif elmAt[-1] is None:
                    raise ClAppError("You use None in sf.kryO(..) paramere:"
                                   + str(elmAt))
            else:
                # krry(3)
                elmAt = np.array([elmAt],dtype=object)

            if typeAt is 0:
                # type estimation to decide ClTensor or ClFldTns
                sumAt = sumUpArry(elmAt)
                if isinstance(sumAt, (bool,int,long,float)):
                    typeAt = float
                elif isinstance(sumAt, complex):
                    typeAt = complex
                # sumAt == object では 10.03.15 krry([z_,z_] で Pl と object を
                # 比較しようとしてエラーになる
                # sumUpArry(..) は引数が ndarray or ClFldTns のときは
                # ag.dtype を返す
                #elif sumAt == object:
                elif sumAt is object:
                    typeAt = object
                else:
                    typeAt = type(sumAt)
                    blFldTnsAt = True
            else:
                if not(typeAt in [None, bool, int, float, complex, object]):
                    blFldTnsAt = True
        else:
            # e.g. krry(1j,2,3,4)
            #      krry(1j,2,3,4, int)
            #      krry([1., 2.], Z3)
            #      krry({(0,0):1,(0,1):0,(1,0):0,(1,1):1}, int)
            #assert False, "Yet not implemented!"
            if  isinstance(ag[-1], type):
                # krry( ......, type )
                typeAt = ag[-1]
                elmAt = ag[:-1]
                if len(elmAt) == 1 and isinstance(
                                    elmAt[0],(list,tuple, np.ndarray)):
                    elmAt = np.array(elmAt[0], dtype=object)
                elif len(elmAt) == 1 and isinstance(elmAt[0],dict):
                    elmAt = np.array(elmAt[0], dtype=object)
                else:
                    elmAt = np.array(elmAt, dtype =object)

                assert len(elmAt) >= 1
            elif  (ag[-1] is None):
                raise ClAppError("You use None in sf.kryO(..) paramere:"
                               + str(ag))
            else:
                # krry(1,2,3,4)
                elmAt = ag

                if isinstance(elmAt, dict):
                    elmAt = ClTens(elmAt)
                elif isinstance(elmAt, np.ndarray ):
                    pass
                elif isinstance(elmAt, (tuple,list) ):
                    if isinstance(elmAt[-1], type):
                        typeAt = elmAt[-1]
                        elmAt = np.array(elmAt[:-1], dtype=object)
                    else:
                        elmAt = np.array(elmAt, dtype=object)
                        # sumUpArry(elmAt は object を返してしまう
                        vct=elmAt.ravel()
                        val=vct[0]
                        for k in range(1,len(vct)):
                            val = val+vct[k]
                        typeAt = type(val)
                        # float is added to avoid numpy.float64
                        if isinstance(val,(bool, int, long, float) ):
                            typeAt = float  # default float
                        elif isinstance(val,complex ):
                            typeAt = complex  # default float
                    assert len(elmAt) >= 1
                else:
                    assert False

            if typeAt is 0:
                # type estimation
                sumAt = sumUpArry(elmAt)
                if isinstance(sumAt, (bool,int,long,float)):
                    typeAt = float
                elif isinstance(sumAt, complex):
                    typeAt = complex
                else:
                    typeAt = type(sumAt)
                    blFldTnsAt = True

            if not(typeAt in [None, bool,int,float,long, complex, object]):
                blFldTnsAt = True
    else:
        # krry(....., dtype = ...)
        assert False, "Yet not implemented!"

    if blFldTnsAt == True:
        elmAt = [ typeAt(x) for x in elmAt]
        return np.array(elmAt, dtype = typeAt)

        #cast(np.ravel(elmAt))
        #import pdb; pdb.set_trace()
        #assert not(typeAt == None) and not(typeAt is 0)
        #krry([`Rat(3),`Rat(0)],ftype=`Rat) で
        #  typeAt == <class 'sympy.core.numbers.Rational'>
        #となる。この typeAt は == None を行うと飛ぶ

    else:
        assert not(typeAt is 0)
        return np.array(elmAt, dtype = typeAt)

class ClAppError(StandardError):
    """' sf.py, octn.py, tlRcGn.py, ... application Error
        This error will be catched and the throwned string is stored in
        strPythonAppErrorStt. And the strPythonAppErrorStt may be check
        by kVerifier action scripts

        e.g.
            raise ClAppError("Application Erron in" + .... )
    '"""
    pass

