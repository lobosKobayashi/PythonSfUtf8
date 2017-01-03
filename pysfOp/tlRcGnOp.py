# -*- encoding: utf-8 -*-
from __future__ import division
"""'
english:
    PythonSf pysfOp/tlRcGnOp.py
    https://github.com/lobosKobayashi
    http://lobosKobayashi.github.com/
    
    Copyright 2016, Kenji Kobayashi
    All program codes in this file was designed by kVerifierLab Kenji Kobayashi

    I release souce codes in this file under the GPLv3
    with the exception of my commercial uses.

    2016y 12m 28d Kenji Kokbayashi

japanese:
    PythonSf pysfOp/tlRcGnOp.py
    https://github.com/lobosKobayashi
    http://lobosKobayashi.github.com/

    Copyright 2016, Kenji Kobayashi
    このファイルの全てのプログラム・コードは kVerifierLab 小林憲次が作成しました。
    
    作成者の小林本人に限っては商用利用を許すとの例外条件を追加して、
    このファイルのソースを GPLv3 で公開します。

    2016年 12月 28日 小林憲次
'"""

"""'
extended itertools usages:

tn.count(3)[1:10]
===============================
[4, 5, 6, 7, 8, 9, 10, 11, 12]

(tn.imap(lambda x:x^2, tn.count(10) )[1:10])
===============================
[121, 144, 169, 196, 225, 256, 289, 324, 361]

tn.cycle(xrange(3))[1:10]
===============================
[1, 2, 0, 1, 2, 0, 1, 2, 0]

tn.repeat('s',100)[1:10]
===============================
['s', 's', 's', 's', 's', 's', 's', 's', 's']

tn.repeat(True)[1:10]
===============================
[True, True, True, True, True, True, True, True, True]

tn.repeat(`1)[1:10]
===============================
[BF(1), BF(1), BF(1), BF(1), BF(1), BF(1), BF(1), BF(1), BF(1)]

tn.izip(range(100), xrange(3,100))[1:10]
===============================
[(1, 4), (2, 5), (3, 6), (4, 7), (5, 8), (6, 9), (7, 10), (8, 11), (9, 12)]

tn.izip(range(100), xrange(3,100), tn.count() )[1:10]
===============================
[(1, 4, 1), (2, 5, 2), (3, 6, 3), (4, 7, 4), (5, 8, 5), (6, 9, 6), (7, 10, 7), (8, 11, 8), (9, 12, 9)]

(tn.ifilter(lambda x:x%2==0, tn.count(10) )[1:10])
===============================
[12, 14, 16, 18, 20, 22, 24, 26, 28]

(tn.ifilter(None, tn.count() )[1:10])
===============================
[2, 3, 4, 5, 6, 7, 8, 9, 10]

(tn.ifilterfalse(lambda x:x%2==0, tn.count(10) )[1:10])
===============================
[13, 15, 17, 19, 21, 23, 25, 27, 29]

(tn.ifilterfalse(None, tn.count() )[0])
===============================
0

tn.islice(tn.count(),1,30,3 )[3:10]
===============================
[10, 13, 16, 19, 22, 25, 28]

tn.startmap(lambda *tplAg:sum(tplAg), tn.izip(range(15), range(3,100)) )[1:10]
===============================
[5, 7, 9, 11, 13, 15, 17, 19, 21]
'"""
# ============ decorator closure to make a function or generator fast begin =============
def clrStreamGnGn(fAg):
    """' Closure to make a stackless generators
     faster stackless generator with buffering calculated values.
    '"""
    dctAt = {}
    def innerF(inAg):
        if inAg in dctAt:
            yield EnRtnGnSub, dctAt[inAg]
        else:
            valAt = Start( fAg(inAg) )
            dctAt[inAg] = valAt
            yield EnRtnGnSub, valAt

    return innerF

def clrStreamGn(fAg):
    """' Closure to make a stackless generator's faster one with buffering
        calculated values.
    '"""
    dctAt = {}
    def innerF(inAg):
        if inAg in dctAt:
            yield dctAt[inAg]
        else:
            #valAt = Start( fAg(inAg) )
            valAt = fAg(inAg)
            dctAt[inAg] = valAt
            yield valAt

    return innerF

class ClStreamGn(object):
    """' 
    '"""
    def __init__(self, fnAg):
        self.m_clr = clrStreamGn(fnAg)

    def __iter__(self):
        return self.m_clr()


def clrStream(fAg):
    """' Closure to make a function faster with buffering calculated values.
    '"""
    dctAt = {}
    def innerF(inAg):
        if inAg in dctAt:
            return dctAt[inAg]
        else:
            valAt = fAg(inAg)
            dctAt[inAg] = valAt
            return valAt

    return innerF

def makeSumUpGn(fAg):
    """' make sum up series generator from integer argment function
         ,iterator or generator
    '"""
    sumUpAt = 0
    if ('__iter__' in dir(fAg)):
        for valAt in fAg:
            sumUpAt += valAt
            yield sumUpAt
    else:
        for i in count():
            sumUpAt += fAg(i)
            yield sumUpAt

# ============ closure to make a function or generator fast end =============

# ============ class to make a function or generator fast begin =============
# itertools.islice が返すのはイタレータです。count() などからスライスされたリス
#トを取り出すのに import tlRcGn as tn; list(tn.islice( tn.count() ,0,10)) と記
#述せねばなりません。これを import tlRcGn as tn; tn.idx( tn.count()[:10] と記述
#可能にします。
class ClIndexForDecorator(object):
    """' holding a  generator fucntion and make it enable to use [ : : ] indexing
    '"""
    def __init__(self, gnFnAg):
        self.m_gnFn = gnFnAg
        self.m_gn = None
        self.m_lstYieldedValue = []
    
    def __iter__(self):
        return self

    def next(self):
        valAt = self.m_gn.next()
        self.m_lstYieldedValue.append(valAt)
        return valAt

    def send(self, valAg):
        valAt = self.m_gn.send(valAg)
        self.m_lstYieldedValue.append(valAt)
        return valAt

    def __getitem__(self, sliceAg):
        if isinstance(sliceAg, slice):
            inStartAt = sliceAg.start
            inStopAt = sliceAg.stop
            inStrideAt = sliceAg.step
        else:
            inStartAt = sliceAg
            inStopAt = sliceAg+1
            inStrideAt = 1

        lenAt = len(self.m_lstYieldedValue)
        if lenAt < inStopAt:
            for indexAt in range(lenAt, inStopAt):
                self.m_lstYieldedValue.append(self.m_gn.next())

        return self.m_lstYieldedValue[
                    inStartAt: inStopAt: inStrideAt]

    def __call__(self, *tplAg, **dctAg):
        self.m_gn = self.m_gnFn(*tplAg, **dctAg)
        return self


def indexing(gnAg):     # decorator for generator function
    """' make enable to use [ : : ] indexing for generator fucntion by this decorator
    '"""
    return ClIndexForDecorator(gnAg)

class ClIndex(object):
    """' Holding a generator/iterator and make it enable to use slice indexes
        [...] or [start:stop:step ]
        idx: aliasing name of ClIndex
    '"""
    def __init__(self, gnAg, inMaxIterAg=10**6):
        assert 'next' in dir(gnAg), "You must set generator argment"
        self.m_gn = gnAg
        self.m_lstYieldedValue = []
        self.m_inMaxIter = inMaxIterAg
    
    def __iter__(self):
        self.m_lstYieldedValue = []
        return self

    def __len__(self):
        return len(self.m_lstYieldedValue)

    def next(self):
        if self.m_inMaxIter < len(self):
            raise IndexError

        valAt = self.m_gn.next()
        self.m_lstYieldedValue.append(valAt)
        return valAt

    def send(self, valAg):
        if self.m_inMaxIter < len(self):
            raise IndexError

        valAt = self.m_gn.send(valAg)
        self.m_lstYieldedValue.append(valAt)
        return valAt

    def __getitem__(self, sliceAg):
        if isinstance(sliceAg, slice):
            inStartAt = sliceAg.start
            inStopAt = sliceAg.stop
            inStrideAt = sliceAg.step
            #print "debug inStartAt:", inStartAt, " inStopAt:",inStopAt, " inStrideAt:", inStrideAt
        else:
            inStartAt = sliceAg
            inStopAt = sliceAg+1
            inStrideAt = 1

        lenAt = len(self.m_lstYieldedValue)
        try:
            # tn.idx(ts.count())[10:3:-2] == [9,7,5]
            #;; tn.count()[:10] == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
            #;; tn.count()[:10:2] == [0, 2, 4, 6, 8]
            #;; tn.count()[10::2] AssertionError: At ClIndex, slice stop parameter is None! infinite!
            #;; tn.count()[10::-2] == [9, 7, 5, 3, 1]
            if inStrideAt== None:
                if inStopAt == None:
                    assert False, "At ClIndex, slice stop parameter is None! infinite!"
            elif inStrideAt< 0:
                inStopAt = inStartAt
            elif inStopAt == None:
                assert False, "At ClIndex, slice stop parameter is None! infinite!"
            elif inStartAt > inStopAt:
                inStopAt = inStartAt

            if lenAt < inStopAt:
                for indexAt in range(lenAt, inStopAt):
                    self.next()
                    #self.m_lstYieldedValue.append(self.m_gn.next())
    
        except StopIteration:
            pass

        if isinstance(sliceAg, int):
            return self.m_lstYieldedValue[sliceAg]
        else:
            #return self.m_lstYieldedValue[
            #        inStartAt: inStopAt: inStrideAt]
            return self.m_lstYieldedValue[sliceAg]

    """'
    加減乗除算と べき乗演算を追加することは有用性を大きく広げる。でも次のこと
    まで考えねばならない
        `c ≡ tn.count とする
    嬉しい機能
        ζ(s) ≡ `c(1)^(-s)
        連分数を計算する関数

    注意点
        ・sympy オブジェクトの無限シーケンスも対象に含める
        ・四則演算
            有限シーケンスとの四則演算;;  [1,2,3]*`c(0)
            <== mix iterator との整合性が必要
            scalar        との四則演算;;`1r *`c(), 3 * `c(), `1 `c()

        ・複素有理数 <== 新規に作る必要がある
        ・getDgRspns
          <== getDgImpls も含め既存の関数とは名前を変えて共存させる
    '"""
idx = ClIndex

class ClRcFml(ClIndex):
    def __init__(self, sqInAg, gnAg, inMaxIterAg=10**6):
        def gnAt(x):
            while(True):
                yield gnAg(x)

        ClIndex.__init__(self, gnAt(self), inMaxIterAg)
        self.m_lstYieldedValue = sqInAg

class ClMakeSumUpGn(idx):
    """' Make sum up series class from function or sequence.
        This class has __getitem__(..) method
    e.g.
        ClMakeSumUpGn(lambda x:x )[0:5]
        ===============================
        [0, 1, 3, 6, 10]
        
        ClMakeSumUpGn([0,1,2,3,4,5])[0:5]
        ===============================
        [0, 1, 3, 6, 10]
        

        ClMakeSumUpGn(lambda x:x^2 )[0:5]
        ===============================
        [0, 1, 5, 14, 30]
    
    '"""
    def __init__(self, fAg):
        idx.__init__(self, makeSumUpGn(fAg))

"""'
@indexing
def gnTest(inAg):
    inAt = inAg
    while True:
        inAt += 1
        yield inAt

clAt = gnTest(5)
print clAt[3:4]
print clAt[100]
print clAt[50:60:2]
'"""
# ============ class to make a function or generator fast end =============

# ====================== itertools with __getiterm__ begin =========================
import itertools as it

def count(*tplAg):
    """' itertools.count + [..]:__getitem__(..) function.'"""
    return idx(it.count(*tplAg))

def imap(*tplAg):
    """' itertools.imap + [..]:__getitem__(..) function.'"""
    return idx( it.imap(*tplAg) )
    
def cycle(*tplAg):
    return idx( it.cycle(*tplAg) )
    """' itertools.cycle + [..]:__getitem__(..) function.'"""

def repeat(*tplAg):
    return idx( it.repeat(*tplAg) )
    """' itertools.repeat + [..]:__getitem__(..) function.'"""

def izip(*tplAg):
    """' itertools.izip + [..]:__getitem__(..) function.'"""
    return idx( it.izip(*tplAg) )

def ifilter(*tplAg):
    """' itertools.ifilter + [..]:__getitem__(..) function.'"""
    return idx( it.ifilter(*tplAg) )

def ifilterfalse(*tplAg):
    """' itertools.ifilterfalse + [..]:__getitem__(..) function.'"""
    return idx( it.ifilterfalse(*tplAg) )

def islice(*tplAg):
    """' itertools.islice + [..]:__getitem__(..) function.'"""
    return idx( it.islice(*tplAg) )

def startmap(*tplAg):
    """' itertools.startmap + [..]:__getitem__(..) function.
        extending imap for multi variable
    e.g.
    tn.startmap(λ x,y:(x,y), tn.izip(range(5), range(10,15)) )[:4]
        == [(0, 10), (1, 11), (2, 12), (3, 13)]
    '"""
    return idx( it.starmap(*tplAg) )

def chain(*tplAg):
    """' itertools.chain + [..]:__getitem__(..) function.'"""
    return idx( it.chain(*tplAg) )

def takewhile(*tplAg):
    """' itertools.takewhile + [..]:__getitem__(..) function.'"""
    return idx( it.takewhile(*tplAg) )

def dropwhile(*tplAg):
    """' itertools.dropwhile + [..]:__getitem__(..) function.'"""
    return idx( it.dropwhile(*tplAg) )

def groupby(*tplAg):
    """' itertools.groupby + [..]:__getitem__(..) function.
        may be unusefull
    e.g.
           tn.groupby(tn.count(15), λ x: x %2 == 0 )[0][0] == False
    tn.idx(tn.groupby(tn.count(15), λ x: x %2 == 0 )[0][1])[0] == 15
    tn.idx(tn.groupby(tn.count(15), λ x: x %2 == 0 )[0][1])[1]#list index out of range
    
           tn.groupby(tn.count(15), λ x: x %2 == 0 )[1][0] == True
    tn.idx(tn.groupby(tn.count(15), λ x: x %2 == 0 )[1][1])[0] == 16
    
           tn.groupby(tn.count(15), λ x: x %2 == 0 )[2][0] == False
    tn.idx(tn.groupby(tn.count(15), λ x: x %2 == 0 )[2][1])[0] == 17
    '"""
    return idx( it.groupby(*tplAg) )

def mix(*tplAg):
    """' mix generators
    e.g. 
    tn.mix(tn.repeat(2),tn.count())[:10] == [2, 0, 2, 1, 2, 2, 2, 3, 2, 4]
    '"""
    def gnFnc():
        while True:
            for gnAt in tplAg:
                yield gnAt.next()

    return idx(gnFnc())

"""'
count = it.count
cycle = it.cycle
repeat = it.repeat
izip = it.izip
ifilter = it.ifilter
ifilterfalse = it.ifilterfalse
islice = it.islice
imap = it.imap
starmap = it.starmap
don't use 'tee = it.tee' because thery are copy of iterator and not for slice operator.  chain = it.chain
takewhile = it.takewhile
dropwhile = it.dropwhile
groupby = it.groupby

def slc(gnAg, startAg = None, stopAg = None, stepAg = 1):
    # return sliced tuple by startAg, stopAg, stepAg parameter
    #
    if startAg == None:
        return tuple(pnAg)

    if stopAg == None:
        stopAg = startAg
        startAg = 0

    return tuple( it.islice(gnAg, startAg, stopAg) )
'"""

def mkSrs(fAg):
    """' make infinite seriese of fAg(0), fAg(1), fAg(2), ....  with __getitem__(...)
    '"""
    return imap(fAg, count())

    

# ====================== itertools with __getiterm__ end =========================
