# -*- encoding: utf-8 -*-
from __future__ import division
"""'
english:
    PythonSf pysfOp/basicFnctnsOp.py
    https://github.com/lobosKobayashi
    http://lobosKobayashi.github.com/
    
    Copyright 2016, Kenji Kobayashi
    All program codes in this file was designed by kVerifierLab Kenji Kobayashi

    I release souce codes in this file under the GPLv3
    with the exception of my commercial uses.

    2016y 12m 28d Kenji Kokbayashi

japanese:
    PythonSf pysfOp/basicFnctnsOp.py
    https://github.com/lobosKobayashi
    http://lobosKobayashi.github.com/

    Copyright 2016, Kenji Kobayashi
    このファイルの全てのプログラム・コードは kVerifierLab 小林憲次が作成しました。
    
    作成者の小林本人に限っては商用利用を許すとの例外条件を追加して、
    このファイルのソースを GPLv3 で公開します。

    2016年 12月 28日 小林憲次
'"""

import sfFnctnsOp as sf
import numpy as sc
import copy
# -------------------- 文字列処理系 utility begin --------------------------------------
""" python での文字列処理で find を失敗した時 -1 を返すのは、list[-1] と矛盾する。たぶん
リストのマイナス インデックスを後で追加したための矛盾でしょう。-1 を返すのを嫌って npos
を定義します。C++ の string::npos と同じように使います。

    sztStartAg などにマイナス値を許せば、find(..) などのままで reverse search にすることも
できます。でも、それは複雑になりすぎます。STL に似せたままのほうが誤りが少ないと考えます。

  ただし、npos に -1 を設定できません。list[beginSzt:-1] の意味になってしまうことがあるか
らです。2**30 とします。このように大きなサイズのシーケンス コンテナを扱うことはないと考え
ます。
"""
npos = 2**30
def rfind_first_not_of(strLineAg, strSetAg, sztStartAg=None ):
    """ find_not_of(strLineAg, strSetAg, sztStartAg=None) で reverse 方向に探します 
        strSegAg の中の文字が見つからないときは npos を返します。
    """
    if ( sztStartAg is None):
        sztStartAg = len(strLineAg)
    for i, chAt in enumerate(strLineAg[:sztStartAg][::-1]):
        if chAt not in strSetAg:
            return sztStartAg - i

    return npos


def find_first_not_of(cntnrAg, elmAg, sztStartAg=0):
    """ 文字列の集合を指定し、その何れか以外が最初に現れる位置を探します。
    最後まで指定した文字ばかりのときは None を返します。
    与えられた strLineAg の最初の文字で不一致文字を見つけたときは 0 を返します。
    一致文字ばかりのときは npos を返します。
        if find_first_not_of(strLineAg,"...") == npos : ...
    で判定ください。== 0 や == None とはしないで下さい。
    """
    if isinstance(cntnrAg,str) or isinstance(cntnrAg,unicode):
        for i, chAt in enumerate(cntnrAg[sztStartAg:]):
            if chAt not in elmAg:
                return i + sztStartAg
    elif isinstance(elmAg,list) or isinstance(elmAg,tuple):
        cntnr = cntnrAg[sztStartAg:]
        for szt, cntnrElm in enumerate(cntnr):
            for elm in elmAg:
                if elm != cntnrElm:
                    return sztStartAg+szt
        return npos
    else:
        cntnr = cntnrAg[sztStartAg:]
        for szt, elm in enumerate(cntnr):
            if elm != elmAg:
                return sztStartAg+szt
        return npos

    return npos

def find_first_of(cntnrAg, elmAg, sztStartAg=0):
    """ 戻り値: elmAg の何れかが cntnrAg から最初に見つかる index 値
        python の list.index は見つからないとき ValueError-1 を throw します。
    tuple では index を使えません。string.find() が見つからないときは -1 を返します。
    これらを統一して stl:find_first_of(.) のように扱います。
      ..見つからないときは npos を返します
      ..[arg:] が定義されているシーケンスコンテナと == が定義されている要素を前提とします
      ..elmAg には list, tuple も認めます
    """
    if isinstance(cntnrAg,str) or isinstance(cntnrAg,unicode):
        for szt, chAt in enumerate(cntnrAg[sztStartAg:]):
            if chAt in elmAg:
                return szt + sztStartAg
        return npos
    elif isinstance(elmAg,list) or isinstance(elmAg,tuple):
        cntnr = cntnrAg[sztStartAg:]
        for szt, cntnrElm in enumerate(cntnr):
            for elm in elmAg:
                if elm == cntnrElm:
                    return sztStartAg+szt
        return npos
    else:
        cntnr = cntnrAg[sztStartAg:]
        for szt, elm in enumerate(cntnr):
            if elm == elmAg:
                return sztStartAg+szt
        return npos

def shftSq(sq, inShift=1, blDeepCopy=False):
    """ shift sequence: tuple, list, scipy.array with 0 supplement 
        return shallow copied sequenc in default, so the returned value type
        is same as parameter sq

        if the sq argment is a instance of ClFldTns, then the filling 0 is 
        the type 0 of the sq argment.
    e.g.
    shftSq( sc.array([1,2,3,4]),-2 )
    ===============================
    [3 4 0 0]

    shftSq( (1,2,3,4), -1 )
    ===============================
    (2, 3, 4, 0)


    shftSq([1,2,3,4], +2)
    ===============================
    [0, 0, 1, 2]


    shftSq(~[1,2,3,4])
    ===============================
    [ 0.  1.  2.  3.]
    ---- ClTensor ----

    shftSq(arange(4*4).reshape(4,4))
    ===============================
    [[ 0  0  0  0]
     [ 0  1  2  3]
     [ 4  5  6  7]
     [ 8  9 10 11]]
    ---- ClTensor ----

    mt=arange(4*4).reshape(4,4);mtr=krry(mt, oc.RS);shftSq(mtr)
    ===============================
    [[0x00 0x00 0x00 0x00]
     [0x00 0x01 0x02 0x03]
     [0x04 0x05 0x06 0x07]
     [0x08 0x09 0x0a 0x0b]]
    ---- ClFldTns:<class 'pysf.octn.RS'> ----

    """
    #import pdb; pdb.set_trace()
    #if isinstance(sq, sf.ClFldTns) and len(sq.shape) >= 2:
    #    # because to shift ClFldTns matrix properly
    #    blDeepCopy = True

    if blDeepCopy == True:
        sqAt = copy.deepcopy(sq)
    else:
        sqAt = copy.copy(sq)

    if isinstance(sq, tuple):
        sqAt = list(sqAt)   # make imutable

    if (inShift > 0):
        #sqAt[inShift:] = sqAt[0:-inShift]
        #11.08.03 counter measure for Python(x,y) ver2.6.6.2
        sqAt[inShift:] = sq[0:-inShift]
        if isinstance(sq,            ):
            shpAt = sq.shape
            if len(shpAt)==1:
                sqAt[0:inShift] = [0]*inShift
            else:
                sqAt[0:inShift] = [sf.kzrs(shpAt[1:])]*inShift
        #elif isinstance(sq, sf.ClFldTns):
        #    shpAt = sq.shape
        #    if len(shpAt)==1:
        #        sqAt[0:inShift] = [sq.m_type(0)]*inShift
        #    else:
        #        sqAt[0:inShift] = [sf.kzrs(shpAt[1:],sq.m_type)]*inShift
        else:
            sqAt[0:inShift] = [0]*inShift
    elif (inShift < 0):
        inShift *= -1
        #sqAt[0:-inShift] = sqAt[inShift:]
        #11.08.03 counter measure for Python(x,y) ver2.6.6.2
        sqAt[0:-inShift] = sq[inShift:]
        #if False:       #isinstance(sq, sf.ClFldTns):
        #    sqAt[-inShift:] = [sq.m_type(0)]*inShift
        #else:
        #    sqAt[-inShift:] = [0]*inShift
        sqAt[-inShift:] = [0]*inShift

    if isinstance(sq, tuple):
        return tuple(sqAt)
    else:
        return sqAt

def rttSq(sq, inShift=1, blDeepCopy=False):
    """ rotate sequence: tuple, list, scipy.array
        return shallow copied sequenc in default, so the returned value type
        is same as parameter sq

    e.g.
    rttSq( sc.array([1,2,3,4]),-2 )
    ===============================
    [3 4 1 2]

    rttSq( (1,2,3,4), -1 )
    ===============================
    (2, 3, 4, 1)

    rttSq([1,2,3,4], +2)
    ===============================
    [3, 4, 1, 2]

    rttSq(~[1,2,3,4])
    ===============================
    [ 4.  1.  2.  3.]
    ---- ClTensor ----
    """
    #if isinstance(sq, sf.ClFldTns):
    #    # because to rotate ClFldTns matrix properly
    #    blDeepCopy = True
        

    if blDeepCopy == True:
        sqAt = copy.deepcopy(sq)
    else:
        sqAt = copy.copy(sq)

    if isinstance(sq, tuple):
        sqAt = list(sqAt)   # make imutable
    

    if (inShift > 0):
        #sqAt[inShift:] = sqAt[0:-inShift]
        #11.08.03 counter measure for Python(x,y) ver2.6.6.2
        sqAt[inShift:] = sq[0:-inShift]
        sqAt[0:inShift] = sq[-inShift:]
    elif (inShift < 0):
        inShift *= -1
        #sqAt[0:-inShift] = sqAt[inShift:]
        #11.08.03 counter measure for Python(x,y) ver2.6.6.2
        sqAt[0:-inShift] = sq[inShift:]
        sqAt[-inShift:] = sq[0:inShift]

    if isinstance(sq, tuple):
        return tuple(sqAt)
    else:
        return sqAt

# multiple range generator
def mrng(*args):
    """' multiple range generator
        list(mrng(2,3))"
        ===============================
        [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2)]

        list(mrng((1,4),(5,7)))
        ===============================
        [(1, 5), (1, 6), (2, 5), (2, 6), (3, 5), (3, 6)]

        list(mrng((1,6,2),(5,9,3)))

        ===============================
        [(1, 5), (1, 8), (3, 5), (3, 8), (5, 5), (5, 8)]

        an example of usage
            dctAt={}
            for i,j in mrng(10,20):
                dctAt[i,j] = i+j
                
    '"""
    head, tail = args[0], args[1:]
    if type(head) in [int, long, float]:
        head = range(int(head))
    elif isinstance(head, tuple) or isinstance(head, list):
        head = range(*head)
    if tail:
        for i in head:
            for j in mrng(*tail):
                if isinstance(j, tuple):
                    yield (i,)+j
                else:
                    yield (i, j)
    else:
        for i in head:
            yield i

def arSqnc(startOrSizeAg, sizeAg = None, strideAg=1):
    """  等差数列タプルを start, size, stride 引数で生成して返す
         return arithmetic sequence generated with argument start, size, stride
      e.g.
        N=10;arsq(1,N, 3)
        ===============================
        (1, 4, 7, 10, 13, 16, 19, 22, 25, 28)
    """
    if sizeAg == None:
        return range(startOrSizeAg)
    else:
        tplAt = ()
        for i in range(sizeAg):
            tplAt += (startOrSizeAg + i*strideAg,)
        return tplAt

arsq = arSqnc   # to truncate

def masq(*args):
    """ 多次元の等差数列を生成するジェネレータ
        generator generating multiple dimention arithmetic sequence
    e.g.
    N=3;list(masq([2, N, 0.5],[3,N,0.5]))
    ===============================
[(2.0, 3.0), (2.0, 3.5), (2.0, 4.0), (2.5, 3.0), (2.5, 3.5), (2.5, 4.0), (3.0, 3.0), (3.0, 3.5), (3.0, 4.0)]

    """
    head, tail = args[0], args[1:]
    if type(head) in [int, long, float]:
        head=range(head)
    elif isinstance(head, tuple) or isinstance(head, list):
        head=arSqnc(*head)
    else:
        assert False, "unexpected argument" + str(args)

    if tail:
        for i in head:
            for j in masq(*tail):
                if isinstance(j, tuple):
                    yield (i,)+j
                else:
                    yield (i, j)
    else:
        for i in head:
            yield i

def enmasq( *args, **kwarg):
    """ 列挙インデックス付きの多次元等差数列
        enumerate index and multiple dimentional arithmetic sequence
    e.g.
N=4;mt=kzrs(N,N);for idx,val in enmasq([0,N,0.1],[1,N,0.1]):mt[idx]=sum(val);mt
    ===============================
    [[ 1.   1.1  1.2  1.3]
     [ 1.1  1.2  1.3  1.4]
     [ 1.2  1.3  1.4  1.5]
     [ 1.3  1.4  1.5  1.6]]
    ---- ClTensor ----
    '"""
    head, tail = args[0], args[1:]
    if type(head) in [int, long, float]:
        head=enumerate(range(head))
    elif isinstance(head, tuple) or isinstance(head, list):
        head=enumerate(arSqnc(*head))
    else:
        assert False, "unexpected argument" + str(args)

    if 'index' in kwarg.keys():
        index = kwarg['index']
    else:
        index = ()

    if tail:
        for idxI, i in head:
            for idxJ, j in enmasq(index=index, *tail):
                if isinstance(j, tuple):
                    yield index+(idxI,)+idxJ, (i,)+j
                else:
                    yield index + (idxI,idxJ),  (i, j)
    else:
        for idxI, i in head:
            yield idxI, i

import itertools as itl;
prdct=itl.product

def mitr(*args):
    """ 多次元の繰り返しを生成するジェネレータ
        generator generating for multiple dimention iterators
    e.g.
    list(mitr(2,3))
    ===============================
    [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2)]

    s=set(['a','b']);list(mitr(s,s))
    ===============================
    [('a', 'a'), ('a', 'b'), ('b', 'a'), ('b', 'b')]

    s=[1,2,3];list(mitr(s,s))
    ===============================
    [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]

    """
#    import itertools as md
#    if len(args)==1 and isinstance(args[0], (int,long,float)):
#        return xrange(int(args[0]))
#    else:
#        return md.product(*
#                   [xrange(int(elm)) if isinstance(elm, (int,long,float)) else elm
#                               for elm in args]
#               )

    head, tail = args[0], args[1:]

    if type(head) in [int, long, float]:
        head = range(int(head))

    if tail:
        if hasattr(head,'next'): # mitr(..) has 'next' attribute
            # to avoid multiple use of one mitr(..) iterator
            idAt=id(head)
            ls=[k for k,elm in enumerate(tail) if idAt == id(elm)]
            if ls:
                tplAt = tuple(head)
                tailAt = list(tail)
                head = tplAt
                for k in ls:
                    tailAt[k] = tplAt
            else:
                tailAt = tail
        else:
            tailAt = tail

        if len(tailAt)==1 and hasattr(tailAt[0],'next'):
            # Counter Measure for X,Y=[4,5],[6,7]; list(mitr([4,5], mitr(Y,Y))): Issue:00021
            # tailAt[0] == mitr(..)
            lstTailAt = list(tailAt[0])
            for i in head:
                for j in lstTailAt:
                    if len(tail) == 1:
                        yield (i, j)
                    else:
                        yield (i,)+j
        else:
            for i in head:
                for j in mitr(*tailAt):
                    if len(tail) == 1:
                        yield (i, j)
                    else:
                        yield (i,)+j
    else:
        for i in head:
            yield i

def enmitr( *args, **kwarg):
    """ 列挙インデックス付きの多次元繰り返しイタレータ
        multiple dimentional iterator with enumerate index
    e.g.
    s=set(['a','b']);list(enmitr(s,s))
    ===============================
    [((0, 0), ('a', 'a')), ((0, 1), ('a', 'b')), ((1, 0), ('b', 'a')), ((1, 1), ('b', 'b'))]

    s=set([1,2]);list(enmitr(s,s,s))
    ===============================
    [((0, 0, 0), (1, 1, 1)), ((0, 0, 1), (1, 1, 2)), ((0, 1, 0), (1, 2, 1)),
     ((0, 1, 1), (1, 2, 2)), ((1, 0, 0), (2, 1, 1)), ((1, 0, 1), (2, 1, 2)),
     ((1, 1, 0), (2, 2, 1)), ((1, 1, 1), (2, 2, 2))]
    '"""
    head, tail = args[0], args[1:]

    if 'index' in kwarg.keys():
        index = kwarg['index']
    else:
        index = ()

    if type(head) in [int, long, float]:
        head = range(int(head))

    if tail:
        if len(tail) == 1 and hasattr(tail[0],'next'):
            # to avoid multiple use of one iterator
            tailAt = (tuple(tail[0]), )
        else:
            tailAt = tail

        for idxI, i in enumerate(head):
            for idxJ, j in enmitr(index=index, *tailAt):
                if len(tail) == 1:
                    yield index + (idxI,idxJ),  (i, j)
                else:
                    yield index+(idxI,)+idxJ, (i,)+j
    else:
        for idxI, i in enumerate(head):
            yield idxI, i

def klsp(*sq, **dct):
    """' return ClTensor of scipy.linspace(...)
    '"""
    return sf.kryO(sc.linspace(*sq, **dct) )


def product(sqAg, first=1):
    """' product up any sequenct as sum
    e.g.
      product([1,2,3,4,5]) == 1200
    '"""
    rtnAt= first
    for elmAt in sqAg:
        rtnAt = rtnAt * elmAt
    
    return rtnAt

def aTrue(sqBlAg):
    """'  make scipy.alltrue short

    and counter mesure for Enthought24 below result
        sc.alltrue([[True,True,True],[True,True,True]])
        ===============================
        [True True True]

    Caution! python 2.5 all can't work for scipy.array matrix
             python 2.6 all can   work for scipy.array matrix
    '""" 
    blAt = sc.alltrue(sqBlAg)
    if hasattr(blAt,'__len__'):
        return aTrue(blAt)
    else:
        return blAt




def combinate(items, n):
    """' Return generator for n combinations of items
    e.g.
    list(combinate(list('abcd'),3))
    ===============================
    [('a', 'b', 'c'), ('a', 'b', 'd'), ('a', 'c', 'd'), ('b', 'c', 'd')]
    
    list(combinate([0,1,2,3],2))
    ===============================
    [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
    '"""
    if isinstance(items,set) and not hasattr(items, '__getitem__'):
        items = tuple(items)

    if n==0: yield ()
    else:
        for i in xrange(len(items)):
            for cc in combinate(items[i+1:],n-1):
                yield (items[i],)+cc

def __permutate(items, n, inSignAg=1):
    if inSignAg == None:
        if n==0:
            #yield [], inSignAg
            yield ()
        else:
            for i in xrange(len(items)):
                for cc in __permutate(items[:i]+items[i+1:],n-1
                                      , None):
                    yield (items[i],)+cc
    else:
        if n==0:
            #yield [], inSignAg
            yield (), inSignAg
        else:
            for i in xrange(len(items)):
                inSignAt = inSignAg * (-1)** i
                for cc, sign in __permutate(items[:i]+items[i+1:],n-1
                                      , inSignAg = inSignAt):
                    #yield [items[i]]+cc, sign
                    yield (items[i],)+cc, sign

def permutate(items, inSignAg=None):
    """'A generator for calculating all the permutations of a sequence
        with sign modified from 
        http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/190465

        permutate given sequece and return the (permutated list,sign)
        inSignAg is initial sign value and changed sign for each exchange

        permutate(.) returns tuple of (tuple,int), not of [list,int] to ease
        make index:sign dictionary from returned value
        e.g.
        tuple(permutate([0,1,2]))
        ===============================
        ((0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0))

        tuple(permutate([2,1,0]))
        ===============================
        ((2, 1, 0), (2, 0, 1), (1, 2, 0), (1, 0, 2), (0, 2, 1), (0, 1, 2))

        tuple(permutate([2,1,0],1))
        ===============================
        (((2, 1, 0), 1), ((2, 0, 1), -1), ((1, 2, 0), -1), ((1, 0, 2), 1)
                , ((0, 2, 1), 1), ((0, 1, 2), -1))

        tuple(permutate([0,1,2],1))
        ===============================
        (((0, 1, 2), 1), ((0, 2, 1), -1), ((1, 0, 2), -1), ((1, 2, 0), 1)
                , ((2, 0, 1), 1), ((2, 1, 0), -1))

        tuple(permutate([0,1,2],-1))
        ===============================
        (((0, 1, 2), -1), ((0, 2, 1), 1), ((1, 0, 2), 1), ((1, 2, 0), -1),
                ((2, 0, 1), -1), ((2, 1, 0), 1))
    '"""
    #return __combinations(items, len(items), inSignAg)
    assert True if inSignAg==None else abs(inSignAg)==1,(
           "permutate( , ) 2nd paramater must be 1 or -1 or None"
           )
    return __permutate(tuple(items), len(items), inSignAg)

def compose(fnLeftAg, fnRightAg):
    """' return composed function: fnLeft(fnRight(x)) 
    e.g.
        compose(sin, cos)(0)
        ===============================
        0.841470984808

        compose(λ x:x^2, λ x:x*2)(3)
        ===============================
        36
    '"""
    return lambda x, fLeft= fnLeftAg, fRight=fnRightAg: fLeft(fRight(x))

# alias function name for compose
cmps =  compose

def bin_(inAg, lenAg = 0):   # return str
    """' convert integer to binary base notation string with '_'
        e.g. bin_(0x15) -->    '0b1_0101'
             bin_(0x15,16) --> '0b0000_0000__0001_0101'
             bin_(0x15,32) --> '0b0000_0000__0000_0000___0000_0000__0001_0101'

        bin_(0x15,32)
        ===============================
        0b0000_0000__0000_0000___0000_0000__0001_0101
    '"""
    inAg = int(inAg)
    strAt = ""
    lenAt = 0
    while( (inAg != 0) or (lenAg > lenAt)):
        if (lenAt % 4 == 0):
            in4At = lenAt/4
            n = 0
            while (2**n <= in4At) and (in4At%(2**n) == 0):
                strAt = '_' + strAt
                n += 1

        remainder = inAg % 2
        if remainder == 0:
            strAt = '0' + strAt
        else:
            strAt = '1' + strAt
        
        #print "debug:",hex(inAg)
        inAg >>= 1
        lenAt += 1

    while( strAt[0] == '_'):
        strAt = strAt[1:]

    return '0b' + strAt

def bin(inAg, lenAg = 0):   # return str 
    """' convert integer to binary base notation string without '_'
        e.g. bin(0x15) -->    '0b10101'
             bin(0x15,16) --> '0b0000000000010101'
             bin(0x15,32) --> '0b000000000000000000000000001_0101'

        bin(0x15,32)
        ===============================
        0b00000000000000000000000000010101
    '"""
    strAt = bin_(inAg, lenAg)
    return ''.join(strAt.split('_'))



def _call(fnAg, *x):
    if isinstance(fnAg, (ClAfOp, ClAFX)):
        return fnAg(*x)
    else:
        return fnAg(x[0])

class ClAF(object):
    """' Algebraic Function Class. Enable to use four operation to functions
    e.g
    f,g=ClAF(sin), ClAF(cos); (2 f + 3 g)(pi/2)
    ===============================
    2.0

    f,g=ClAF(sin), ClAF(cos);  f(3 g)(pi/2)
    ===============================
    1.83690953073e-016

    '"""
    def _getCls(self):
        # to use __add__(..) .. etc methods in classes that have inherited ClAF
        return ClAF

    def __init__(self, ag):
        if hasattr(ag, '__call__'):
            if hasattr(ag, 'is_Atom'):
                import sympy as ts
                if isinstance(fnAg, ts.Basic):
                    raise sf.ClAppError("At ClAF.__init__(..), "
                                    +"you called call sympy object")
            self.m_fn = ag
        else:
            self.m_fn = lambda *x: ag    # constant function


    def __call__(self, *ag):
        assert len(ag) != 0, "In ClAF.__call__(..), you set no argument"

        if hasattr(ag[0], 'is_Atom'):
            #import sympy as ts
            #   If ag has an attribute of 'is_Atom'
            #   then ts() had been executed
            lstGlbAt=_getDctGlobals()
            ts = lstGlbAt['ts']
            agAt=ag[0]
            if isinstance(agAt, ts.Basic):
                if ( hasattr(agAt, 'is_imaginary') 
                 and (agAt.is_imaginary == True)
                ):
                    return self.m_fn(lstGlbAt['Cmplx'](agAt))
                else:
                    return self.m_fn(lstGlbAt['Float'](agAt))
            else:
                assert False, ("Unexpected sympy parameter at "+str(ag)
                              +" ClAF.__call__(..)" )

        elif ( hasattr(ag[0], '__call__')
         

           ):
            # if ag[0] is a class instance which has __call__ method, then ClAF
            #  calcultes self.m_fn(ag[0]) and dosen't ma&e a composed function. 
            import types;
            if not (isinstance(ag[0], ClAF) or isinstance(ag[0], types.FunctionType)):
                return self.m_fn(ag[0])

            ag = ag[0]
            #import pdb; pdb.set_trace()
            # f(g) where g is function. So we make synthesized function
            #return ClAF(lambda *x:self.m_fn(ag(*x)) )
            #return ClAF(lambda x:self.m_fn(ag(x)) )
            def __f(*x):
                #import pdb; pdb.set_trace()
                if len(x)==1 and isinstance(x[0], (tuple,list,dict) ):
                    return self.m_fn(ag(sf.kryO(x[0])))
                else:
                    return self.m_fn(ag(*x))

            return ClAfOp(__f)
        else:
            #return self.m_fn(ag)
            if isinstance(self, (ClAfOp, ClAfxOp)):
                    return self.m_fn(*ag)
            else:
                if len(ag)==1 and isinstance(ag[0], (tuple,list,dict) ):
                    return self.m_fn(sf.kryO(ag[0]))
                else:
                    if isinstance(self.m_fn, (ClAfOp, ClAFX)):
                        return self.m_fn(*ag)
                    else:
                        return self.m_fn(ag[0])

    
    def __add__(self, ag):
        """' Return a function which was synthesized from self+f
        '"""
        if hasattr(ag, '__call__'):
            return ClAfOp(lambda *x: self(*x)
                                           + _call(ag, *x) )
        else:
            return ClAfOp(lambda *x:self(*x) + ag)

    def __radd__(self, ag):
        """' Return a function which was synthesized from f+self
        '"""
        return ClAfOp(lambda *x:ag + self(*x))

    def __sub__(self, ag):
        """' Return a function which was synthesized from self-f
        '"""
        if hasattr(ag, '__call__'):
            return ClAfOp(lambda *x:self(*x)
                                          - _call(ag, *x))
        else:
            return ClAfOp(lambda *x:self(*x)-ag)

    def __rsub__(self, ag):
        """' Return a function which was synthesized from f - self
        '"""
        return ClAfOp(lambda *x:ag - self(*x))

    def __mul__(self, ag):
        """' Return a function which was synthesized from f(x)*g(x)
        '"""
        if hasattr(ag, '__call__'):
            return ClAfOp(lambda *x:self(*x)
                                          * _call(ag, *x))
        else:
            return ClAfOp(lambda *x:(self(*x)*ag))

    def __rmul__(self, ag):
        """' Return a function which was synthesized from f(x)*g(x)
        '"""
        return ClAfOp(lambda *x:ag*self(*x))

    def __div__(self, ag):
        if hasattr(ag, '__call__'):
            return ClAfOp( lambda *x:self(*x)
                                           / _call(ag, *x) )
        else:
            return ClAfOp(lambda *x:self.m_fn(x[0]))
    def __truediv__(self, ag):
        if hasattr(ag, '__call__'):
            return ClAfOp( lambda *x:self(*x)
                                           / _call(ag, *x) )
        else:
            return ClAfOp(lambda *x:self(*x)/ag)

    def __rdiv__(self, ag):
        return ClAfOp(lambda *x:ag/self(*x))
    def __rtruediv__(self, ag):
        return ClAfOp(lambda *x:ag/self(*x))

    def __pow__(self, ag):
        """' return f(x)**ag
             not multple call f^n == f( f(... n ...f(x) ...) )
        '"""
        assert isinstance(ag, (int, float, long, complex)) 
        def __fn(*x):
            assert len(x) >= 1, ("At ClAF.__pow__(..), "
                                        +  "you set no argument")
            at = self(*x)
            if isinstance(at, (tuple,list,dict                          )
                         ):
                for idx in mrng(*at.shape):
                    at[idx] = at[idx]**ag
                return at
            elif isinstance(at, sc.ndarray):
                return at**ag
            else:
                return at**ag

        return ClAfOp(__fn)

    def __neg__(self):
        return ClAfOp(lambda *x:-self(*x))

class ClAfOp(ClAF):
    pass

class ClAFX(ClAF):
    """' Algebraic Function Class for `X
        Enable power calculation for complex
        Enable call for  sym.py variable
    '"""
    def __init__(self, ag, posAg__=0):
        self.m_pos = posAg__
        ClAF.__init__(self,ag)


    def __fnAr(self, agAg):
        if isinstance(agAg, (tuple,list     ) ):
            agAg = sf.kryO(agAg)

        # Calculated results may be complex
        # so we can't decide a matrix type
        dct=sf.np.zeros(agAg.shape) # dct={} open 版の kzrs 関数を作るべき？date:2013/03/30 (土) time:21:46
        for idx in sf.mrng(*agAg.shape):
            dct[idx] = self.m_fn(agAg[idx])

        return sf.kryO(dct)


    def __call__(self, *ag):
        if ( hasattr(ag[0], '__call__')


           ):
            #import pdb; pdb.set_trace()
            if hasattr(ag[0], 'is_Atom'):
                #import sympy as ts
                #   If ag has an attribute of 'is_Atom'
                #   then ts() had been executed
                lstGlbAt=_getDctGlobals()
                ts = lstGlbAt['ts']
                if isinstance(ag[0], ts.Basic):
                    return self.m_fn(ag[0])
                else:
                    assert False, ("Unexpected sympy parameter: "+str(ag[0])
                                  +" at ClAFX.__call__(..)" )
            
            # if ag[0] is a class instance which has __call__ method, then ClAFX
            #  calcultes self.m_fn(ag[0]) and dosen't ma&e a composed function. 
            import types;
            if not (isinstance(ag[0], ClAF) or isinstance(ag[0], types.FunctionType)):
                return self.m_fn(ag[0])

            # f(g) where g is function. So we make synthesized function
            def __f(*x):
                #import pdb; pdb.set_trace()
                if isinstance(ag[0], (ClAfOp, ClAfxOp, ClAFX)):
                    return self.m_fn(ag[0](*x))
                elif isinstance(x[0], (int,list,dict) ):
                    return self.m_fn(ag[0](sf.kryO(x[0])))
                else:
                    return self.m_fn(ag[0](*x))

            return ClAfOp(__f)
        else:
            if len(ag)==1 and isinstance(ag[0],(tuple,list,dict,
                                                                        )):
                return self.__fnAr(ag[0])
            elif len(ag)==1 and isinstance(ag[0], sc.ndarray):
                return self.m_fn(ag[0])
            elif isinstance(self, ClAfxOp):
                return self.m_fn(*ag)
            else:
                assert len(ag) >= self.m_pos+1, ("At ClAFX.__call__(..), "
                                        +  "you set shorter sequence arguments"
                                        + ":"+str(ag) )
                return self.m_fn(ag[self.m_pos])


    def __pow__(self, ag):
        """' return f(x)**ag
             not multple call f^n == f( f(... n ...f(x) ...) )
        '"""
        assert isinstance(ag, (int, float, long, complex)) 
        def __fn(*x):
            assert len(x) >= self.m_pos+1, ("At ClAFX.__pow__(..), "
                                        +  "you set shorter sequence arguments"
                                        + ":"+str(x) )
            at = x[self.m_pos]
            if isinstance(at, (tuple,list,dict                          )
                         ):
                for idx in mrng(*at.shape):
                    at[idx] = at[idx]**ag
                return at
            elif isinstance(at, sc.ndarray):
                return at**ag
            else:
                return at**ag

        return ClAfxOp(__fn)

class ClAfxOp(ClAFX):
    pass

class ClAFXX(ClAF):
    def __call__(self, *ag):
        if ( hasattr(ag[0], '__call__')


           ):
            import types;
            if not (isinstance(ag[0], ClAF) or isinstance(ag[0], types.FunctionType)):
                return self.m_fn(ag[0])
            

            # f(g) where g is function. So we make synthesized function
            def __f(*x):
                return self.m_fn(x[0])

            return ClAFXX(__f)
        else:
            return self.m_fn(ag[0])

    def __add__(self, ag):
        """' Return a function which was synthesized from self+f
        '"""
        if hasattr(ag, '__call__'):
            return ClAFXX(lambda *x: self(*x)
                                           + _call(ag, *x) )
        else:
            return ClAFXX(lambda *x:self(*x) + ag)

    def __radd__(self, ag):
        """' Return a function which was synthesized from f+self
        '"""
        return ClAFXX(lambda *x:ag + self(*x))

    def __sub__(self, ag):
        """' Return a function which was synthesized from self-f
        '"""
        if hasattr(ag, '__call__'):
            return ClAFXX(lambda *x:self(*x)
                                          - _call(ag, *x))
        else:
            return ClAFXX(lambda *x:self(*x)-ag)

    def __rsub__(self, ag):
        """' Return a function which was synthesized from f - self
        '"""
        return ClAFXX(lambda *x:ag - self(*x))

    def __mul__(self, ag):
        """' Return a function which was synthesized from f(x)*g(x)
        '"""
        if hasattr(ag, '__call__'):
            return ClAFXX(lambda *x:self(*x)
                                          * _call(ag, *x))
        else:
            return ClAFXX(lambda *x:(self(*x)*ag))

    def __rmul__(self, ag):
        """' Return a function which was synthesized from f(x)*g(x)
        '"""
        return ClAFXX(lambda *x:ag*self(*x))

    def __div__(self, ag):
        if hasattr(ag, '__call__'):
            return ClAFXX( lambda *x:self(*x)
                                           / _call(ag, *x) )
        else:
            return ClAFXX(lambda *x:self.m_fn(x[0]))
    def __truediv__(self, ag):
        if hasattr(ag, '__call__'):
            return ClAFXX( lambda *x:self(*x)
                                           / _call(ag, *x) )
        else:
            return ClAFXX(lambda *x:self(*x)/ag)

    def __rdiv__(self, ag):
        return ClAFXX(lambda *x:ag/self(*x))
    def __rtruediv__(self, ag):
        return ClAFXX(lambda *x:ag/self(*x))

    def __pow__(self, ag):
        """' return f(x)**ag
             not multple call f^n == f( f(... n ...f(x) ...) )
        '"""
        assert isinstance(ag, (int, float, long, complex)) 
        def __fn(*x):
            assert len(x) >= 1, ("At ClAF.__pow__(..), "
                                        +  "you set no argument")
            at = self(*x)
            return at**ag

        return ClAFXX(__fn)

    def __neg__(self):
        return ClAFXX(lambda *x:-self(*x))


class ClAfNorm(ClAfOp):
    """' Algebraic Function Class for norm
        Enable power calculation for complex
        Disable call for  sym.py variable
    '"""
    def __call__(self, *ag):
        if hasattr(ag[0], '__call__'):
            #import pdb; pdb.set_trace()
            if hasattr(ag[0], 'is_Atom'):
                import sympy
                if isinstance(ag[0], sympy.Rational):
                    #import pdb; pdb.set_trace()
                    if len(ag) > 1:
                        return self.m_fn(*ag)
                    else:
                        return float(abs(ag[0]))
                else:
                    assert False, "ClAfNorm can't treat sympy objects"

            if(isinstance(ag[0],ClAF)



            ):
                # norm(g) where g is function. So we make synthesized function
                def __f(*x):
                    #import pdb; pdb.set_trace()
                    return self.m_fn(ag[0](*x))

                return ClAfOpNorm(__f)
            else:
                return self.m_fn(*ag)

        else:
            return self.m_fn(*ag)


    def __pow__(self, ag):
        """' return norm(x)**ag
        '"""
        assert isinstance(ag, (int, float, long, complex)) 
        def __fn(*x):
            at = self(*x)
            return at**ag

        return ClAfOpNorm(__fn)

class ClAfOpNorm(ClAfNorm):
    pass
