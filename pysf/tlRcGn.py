# -*- encoding: utf-8 -*-
from __future__ import division
"""'
english:
    PythonSf pysf/tlRcGn.py
    https://github.com/lobosKobayashi
    http://lobosKobayashi.github.com/
    
    Copyright 2016, Kenji Kobayashi
    All program codes in this file was designed by kVerifierLab Kenji Kobayashi

    I release souce codes in this file under the GPLv3
    with the exception of my commercial uses.

    2016y 12m 28d Kenji Kokbayashi

japanese:
    PythonSf pysf/tlRcGn.py
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

# can be used for python 2.5 or upper
"""'it: aliased name of itertools'"""
import types

EnDormant = 0
EnWait = 1
EnLoopingWait = 2
EnTimeup=3
EnStart =4
EnRestart=5
EnRun = 6
EnLoopRun=7
EnTerminating=8

EnTerminate = 100
EnCallGnSub = 101
EnRtnGnSub = 102
EnTrnstn = 103

EnYield = 300

class ClGenerators(object):
    def __init__(self, gnAg):
        assert isinstance(gnAg, types.GeneratorType)
        # m_returnPrm は yield EnRtnGnSub returnValue で戻された returnValue を
        # 保持する。kYThrd での restart parameter ではない
        self.m_rtrPrmFrmGnSb = None     # return parameter from generator subroutine
        #self.m_generator = gnAg
        self.m_stkGnrtr = [gnAg]
    
    def next(self):
        while True:
            try:
                if  self.m_rtrPrmFrmGnSb == None:
                    tplRtnAt =  self.m_stkGnrtr[-1].next()
                else:
                    tplRtnAt =  self.m_stkGnrtr[-1].send(self.m_rtrPrmFrmGnSb)

            except StopIteration:
                assert False, "Stop Iteration has occured in ClGenerators.next()"
    
            # ===== Now generator executed yield instruction =====

            # process yielded return value
            if isinstance(tplRtnAt, tuple):
                enYieldedAt = tplRtnAt[0]
                objYieldedArgAt = tplRtnAt[1]
            else:
                # EnRtnGnSub は返り値無しで戻ることもある
                assert (tplRtnAt == EnTerminate) or (tplRtnAt == EnRtnGnSub)\
                        , "You have set abnomal YThread yield parameters:"\
                        + str(tplRtnAt)
                enYieldedAt = tplRtnAt
                objYieldedArgAt = None
    
            if (enYieldedAt == EnCallGnSub):
                # executeReadyQue() を経由して generator subroutine の呼び
                # 出しを行わせると# CntxtVfBs の修正が多くなる。C++ との相
                # 違が増えてくるので避ける
                # self.Call(tplRtnAt)
                #import pdb; pdb.set_trace()
                #self.m_stkGnrtr.append(self.m_generator)
                self.m_rtrPrmFrmGnSb = None
                #self.m_generator = objYieldedArgAt
                self.m_stkGnrtr.append(objYieldedArgAt)
                continue
            elif (enYieldedAt == EnTrnstn):
                self.m_rtrPrmFrmGnSb = None
                #self.m_generator = objYieldedArgAt
                self.m_stkGnrtr[-1] = objYieldedArgAt
                continue
            elif (enYieldedAt == EnRtnGnSub):
                #print "to debug objYieldedArgAt:", objYieldedArgAt
                if len(self.m_stkGnrtr) > 1:
                    #self.m_generator = self.m_stkGnrtr.pop()
                    self.m_stkGnrtr.pop()
                    self.m_rtrPrmFrmGnSb = objYieldedArgAt
                    continue
                else:
                    self.m_rtrPrmFrmGnSb = objYieldedArgAt
                    return objYieldedArgAt
            elif (enYieldedAt == EnTerminate):
                return objYieldedArgAt
            else:
                assert False, "You have set unexpected tlRcGn yield parameters:"\
                                      + str(tplRtnAt)

    # same as upper next routine except for send(.) and EnYield
    def Start(self):
        while True:
            try:
                if self.m_rtrPrmFrmGnSb is None:
                # == で比較すると、Rat モジュールなど __corese__ を呼び出してエラーになる
                # ような戻り値を generator routine が戻すことがありうる
                # send の代わりに next を使うと None が返るので、generator subroutine
                # の戻り値が None であっても誤りなく動作する
                #if  self.m_rtrPrmFrmGnSb == None:
                    #tplRtnAt =  self.m_generator.next()
                    tplRtnAt =  self.m_stkGnrtr[-1].next()
                else:
                    #tplRtnAt =  self.m_generator.send(self.m_rtrPrmFrmGnSb)
                    tplRtnAt =  self.m_stkGnrtr[-1].send(self.m_rtrPrmFrmGnSb)

                    #  08.07.07 I ave abandoned to use send because of continuation
                    # which needs itertools that cant use sedn or generator_tools 
                    # that cant use at first restart
                    #tplRtnAt =  self.m_generator.next()
            except StopIteration:
                assert False, "Stop Iteration has occured in ClGenerators.next()"
    
            # ===== Now generator executed yield instruction =====

            # process yielded return value
            if isinstance(tplRtnAt, tuple):
                enYieldedAt = tplRtnAt[0]
                objYieldedArgAt = tplRtnAt[1]
            else:
                # EnRtnGnSub は返り値無しで戻ることもある
                assert (tplRtnAt == EnTerminate) or (tplRtnAt == EnRtnGnSub)\
                        , "You have set abnomal YThread yield parameters:"\
                        + str(tplRtnAt)
                enYieldedAt = tplRtnAt
                objYieldedArgAt = None
    
            if (enYieldedAt == EnCallGnSub):
                # executeReadyQue() を経由して generator subroutine の呼び
                # 出しを行わせると# CntxtVfBs の修正が多くなる。C++ との相
                # 違が増えてくるので避ける
                # self.Call(tplRtnAt)
                #import pdb; pdb.set_trace()
                #self.m_stkGnrtr.append(self.m_generator)
                self.m_rtrPrmFrmGnSb = None
                #self.m_generator = objYieldedArgAt
                self.m_stkGnrtr.append(objYieldedArgAt)
                continue
            elif (enYieldedAt == EnTrnstn):
                self.m_rtrPrmFrmGnSb = None
                #self.m_generator = objYieldedArgAt
                self.m_stkGnrtr[-1] = objYieldedArgAt
                continue
            elif (enYieldedAt == EnRtnGnSub):
                #print "to debug objYieldedArgAt:", objYieldedArgAt
                if len(self.m_stkGnrtr) > 1:
                    #self.m_generator = self.m_stkGnrtr.pop()
                    self.m_stkGnrtr.pop()
                    self.m_rtrPrmFrmGnSb = objYieldedArgAt
                    continue
                else:
                    self.m_rtrPrmFrmGnSb = objYieldedArgAt
                    return objYieldedArgAt
            else:
                assert False, "You have set unexpected tlRcGn yield parameters:"\
                                      + str(tplRtnAt)

# __stkClGeneratorsStt は 
# python 2.4 での Return() 戻り値の取得を ClGenerators instance をユーザーに管理
# させずに行おうとするとき必要になります。下の関数を使います
# def getReturnValue()
#   __stkClGeneratorsStt[-1].m_rtrPrmFrmGnSb
# でも python 2.5 では必要ありません
# 上のコードも python 2.5 向けで send(.) を使っています
# ただし continuation を実装するときにつかえそうなので、残しています
#   generator_tools;;http://pypi.python.org/pypi/generator_tools/0.3.2
# を使った continuation です。でも、これは未だ汚いコードになるので、実験的なものです


__stkClGeneratorsStt = []

def clrStart(gnFnAg):
    def innerF(arg):
        global __stkClGeneratorsStt
        clAt = ClGenerators(gnFnAg(arg))
        # __stkClGeneratorsStt[-1] is "Now executing ClGenerators Instance."
        __stkClGeneratorsStt.append(clAt)

        #return clAt.m_rtrPrmFrmGnSb
        rtnValAt =  clAt.Start()
        __stkClGeneratorsStt.pop()
        return rtnValAt

    return innerF

def Start(gnAg):        # return value
    """' start generator recursive function
        e.g. Start( gnFunction() )
    '"""
    global __stkClGeneratorsStt
    clAt = ClGenerators(gnAg)
    # __stkClGeneratorsStt[-1] is "Now executing ClGenerators Instance."
    __stkClGeneratorsStt.append(clAt)

    #return clAt.m_rtrPrmFrmGnSb
    rtnValAt =  clAt.Start()
    __stkClGeneratorsStt.pop()
    return rtnValAt     # must be the value returned by yield Return(returnValue)

def Call(gnAg):         # return enumerate parameter and generator
    return EnCallGnSub, gnAg

def Transfer(gnAg):     # return generator
    return EnTrnstn, gnAg

def Return(prmAg = None):   # return value
    return EnRtnGnSub, prmAg

def Terminate(prmAg = None):    # return value
    return EnTerminate, prmAg

def Yield(prmAg):       #
    return EnYield, prmAg

"""'
if __name__ == '__main__':
    def fib( n ):
        #print "Now in fib(n), n:", n    # to debug
        if n <= 1:
            yield EnRtnGnSub, n
        else:
            yield EnRtnGnSub, ( (yield EnCallGnSub, fib(n - 1))
                               +(yield EnCallGnSub, fib(n - 2)) )

    #print [ Start(fib(x)) for x in range(10) ] # debug
    assert [ Start(fib(x)) for x in range(10) ] == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

    def fib2( n ):
        #print "Now in fib(n), n:", n    # to debug
        if n <= 1:
            yield Return(n)
        else:
            yield Return(   (  yield Call( fib(n - 1) )  )
                           +(  yield Call( fib(n - 2) )  )
                        )

    #print [ Start(fib2(x)) for x in range(10) ] # debug
    assert [ Start(fib2(x)) for x in range(10) ] == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

'"""


# ============ const bound variable holder begin =============
class ClBoundVar(object):
    """' Bound Variable holder used for constant variables
    Inhibit second assign. Buf forbid changing element in bounded list instance
    '"""
    #class ClDamie(object):
    def __setattr__(my, strAg, valAg):
        if "__" + strAg in my.__dict__:
            if valAg in my.__dict__.values():
                pass
            else:
                raise AttributeError("Already " + strAg
                            + " has been set"+ " in bound variable!")
        else:
            my.__dict__["__"+strAg] = valAg

    def __getattr__(my, strAg):
        if ("__" + strAg in my.__dict__):
            return my.__dict__["__"+strAg]
        else:
            raise AttributeError("There isn't  "+strAg+ " bound variable!")

c_ = ClBoundVar()

"""'
class ClTest(object):
    def __init__(self):
        self.c = ClBoundVar()

clAt = ClTest()
clAt.c.m_in = 3
clAt.c.m_in = 3

clAt.c.m_lst = [1,2,3]
clAt.c.m_lst[0] = 10
print clAt.c.m_lst

del clAt.c.__m_in 
clAt.c.m_in = 4
print clAt.c.m_in
clAt.c.m_in = 5     #AttributeError: Already m_in has been set in bound variable!

'"""

# ============ const bound variable holder end =============

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

def product(*tplAg):
    return idx( it.product(*tplAg) )
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



# ============================ Tail Recursion begin ===========================
#;;http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/496691
def tail_recursion(g):
    '''
    Enable recursibe call without the limit:sy.getrecursionlimit()
    Version of tail_recursion decorator using no stack-frame inspection.    
    e.g.
    @tail_recursion
    def factorial(n, acc=1):
        "calculate a factorial"
        if n == 0:
           return acc
        res = factorial(n-1, n*acc)
        return res

    print factorial(10000)

    '''
    loc_vars ={"in_loop":False,"cnt":0}

    def result(*args, **kwd):
        loc_vars["cnt"]+=1
        if not loc_vars["in_loop"]:
            loc_vars["in_loop"] = True
            while 1:            
                tc = g(*args,**kwd)
                try:                    
                    qual, args, kwd = tc
                    if qual == 'continue':
                        continue
                except (TypeError, ValueError):                    
                    loc_vars["in_loop"] = False
                    return tc                                    
        else:
            if loc_vars["cnt"]%2==0:
                return ('continue',args, kwd)
            else:
                return g(*args,**kwd)
    return result
# ============================ Tail Recursion end ===========================

# ============================ Algebraic Data Type Begin ===========================
#//@@
# elements of algebraic data type
class Any(object):pass      # any type element
class Rcsv(object):pass     # recursive, line Cdr in Lisp
class Type(object):pass     # poly variant element
T = Type

class ClAlgDtElm(object):pass   # root class of algebraic element type

def isMatched(sqDataAg, algDtElmAg):
    #tn.vr.case([1, 2,3, 'a'], (int, float, str) ) dosen't set m_tplTyStt
    #assert 'm_tplTyStt' in dir(algDtElmAg)
    if isinstance(sqDataAg, (tuple, list)):
        if not (len(algDtElmAg.m_tplTyStt) == len(sqDataAg)):
            return False
    
        for i, tyAt in enumerate(algDtElmAg.m_tplTyStt):
            if tyAt in (Any, Rcsv):
                continue
    
            if not isinstance( sqDataAg[i], tyAt):
                return False
    
        return True
    else:
        if isinstance(sqDataAg, algDtElmAg):
            # e.g. isMatched( var.Times('3','4'), var.Times )
            return True
        elif ( len(algDtElmAg.m_tplTyStt)==1 
           and isinstance(sqDataAg, algDtElmAg.m_tplTyStt[0]) ):
            # e.g. isMatched( 3, Leaf1 )  # Leaft1 = (int,)
            return True
        else:
            return False

def init(self,*tplAg):
    assert len(type(self).m_tplTyStt) == len(tplAg)
    for i, elmAt in enumerate(tplAg):
        assert ( (type(self).m_tplTyStt[i] == Any)
              or (type(self).m_tplTyStt[i] == Rcsv)
              or  isinstance(elmAt, type(self).m_tplTyStt[i] )
        )
    self.tpl = tplAg


def isInstanceOfTyLst(sqAg, sqTyAg):    # return bool
    if len(sqTyAg) == 1:
        tyAt = sqTyAg[0]
        if sqAg == tyAt:
            return True
        elif isinstance(tyAt, type) and isinstance(sqAg,  tyAt):
            return True
        elif tyAt == Any:
            return True
        elif tyAt == Rcsv:
            return True
        else:
            return False

    for i, tyAt in enumerate(sqTyAg):
        if sqAg[i] == tyAt:
            continue
        elif isinstance(tyAt, type) and isinstance(sqAg[i],  tyAt):
            continue
        elif tyAt == Any:
            continue
        elif tyAt == Rcsv:
            #assert len(sqTyAg) == i +1 
            # <== error for test2 at Node2 = (Rcsv, Rcsv) 
            continue
        else:
            return False

    return True


class Var(object):
    """' class to save matched result (i.e. after case() ) 
    '"""
    def __init__(self, ag = None):
        if ag == None:
            self.var=[]
            self.m_dctClAlgDtElm={}
        else:
            assert isinstance(ag, Var)
            self.var=[]
            self.m_dctClAlgDtElm=ag.m_dctClAlgDtElm


    def __len__(self):
        return len(self.var)

    def __getitem__(self,i):
        assert i >= 0 and isinstance(i, int)
        assert (i + 1)<= len(self.var)
        
        return self.var[i]

    def mkAlgDT(self, **dctAg):
        """' make algebraic data type
        e.g.
        tyAt = `vr.mkAlgDT(  Leaf1=(int,)           
                             # type elment name = (type0, type1, .... )
                            ,Leaf2=(int,int)
                            ,Node2 = (Rcsv, Rcsv)
                            ,Node3 = (Rcsv, Rcsv, Rcsv)
    
            class Leaf1, Leaf2, Node2, Node3 are generated by type(.., .., ..)
            which are subclass of ClAlgDtElm
    
        Below phenominon is used in function:`vr.case(sqAg, sqTypeAg) 
            assert `vr.m_dctClAlgDtElm['Leaf2'] = Leaf2 # class of (int, int)
    
        self.m_dctClAlgDtElm is  dictionary of {'Leaf2':(int,int),..} classes
            self.Leaf1.m_tplTyStt == (int, int)
                
        '"""
        # initialize a container of element classes
        self.m_dctClAlgDtElm={}
        for key, val in dctAg.items():
            assert isinstance(key, str)
            for tyAt in val:
                assert isinstance(tyAt, type)

            # make element class of alegemeraic Data Type
            self.m_dctClAlgDtElm[key] = type(
                              key, (ClAlgDtElm,), {'m_tplTyStt':tuple(val)
                            , '__init__':init})


    def __getattr__(self, attrAg):
            return self.m_dctClAlgDtElm[attrAg]

    def __call__(self, tyAg):
        """' substitute Type in abstract algebraic data type with tyAg
        '"""
        assert isinstance(tyAg, type)
        dctAt = {}
        for key, val in self.m_dctClAlgDtElm.items():
            assert 'm_tplTyStt' in dir(val)
            lstAt = []
            for tyAt in val.m_tplTyStt:
                if tyAt == Type:
                    lstAt.append(tyAg)
                else:
                    lstAt.append(tyAt)

            dctAt[key] = tuple(lstAt)

        varAt = Var()
        varAt.mkAlgDT(**dctAt)
        return varAt

    def case(self, sqAg, sqTyAg):
        """'
        '"""
        self.var = []
    
        if not isinstance(sqTyAg, (tuple,list)):
            # sqTyAg is only one type, not sequence
            # e.g. case( Plus, Plus(String('2'),String('3')))

            if ClAlgDtElm in sqTyAg.__bases__:
                assert sqTyAg in self.m_dctClAlgDtElm.values()
                if isinstance(sqAg, sqTyAg):
                    #self.var = sqAg.tpl
                    #self.var = tuple(self.var)
                    if isinstance(sqAg, (tuple, list)):
                        self.var = tuple(sqAg)
                    else:
                        if isinstance(sqAg, ClAlgDtElm ):
                            self.var = tuple(sqAg.tpl)
                        else:
                            self.var = (sqAg,)
                    return True
                elif isMatched(sqAg, sqTyAg):
                    #self.var = sqAg.tpl
                    #self.var = tuple(self.var)
                    if isinstance(sqAg, (tuple, list)):
                        self.var = tuple(sqAg)
                    else:
                        if isinstance(sqAg, ClAlgDtElm ):
                            self.var = tuple(sqAg.tpl)
                        else:
                            self.var = (sqAg,)
                        
                    return True
                else:
                    return False
            else:
                # e.g. case( 3, int)
                if isinstance(sqAg, sqTyAg):
                    assert not isinstance(sqAg, (tuple,list))
                    #if isinstance(sqAg, (tuple,list)):
                    #    self.var = tuple(sqAg)
                    #else:
                    self.var = (sqAg,)
                    return True
                else:
                    return False

        # Now sqTyAg is a sequence of type
        for i, tyAt in enumerate(sqTyAg):
            if sqAg[i] == tyAt:
                appendAt = sqAg[i]
            elif isinstance(tyAt, ClAlgDtElm) and isinstance(sqAg[i], tyAt):
                appendAt = sqAg[i]
            elif isinstance(tyAt, type) and isinstance(sqAg[i],  tyAt):
                appendAt = sqAg[i]
            elif tyAt == Any:
                appendAt = sqAg[i]
            elif tyAt == Rcsv:
                # Rcsv type must be in tail
                assert len(sqTyAg) == i +1
                if i == len(sqAg) - 1:
                    appendAt = sqAg[i]
                else:
                    appendAt = sqAg[i:]
            elif '__len__' in dir(tyAt):
                varAt = Var()
                if varAt.case(sqAg[i], tyAt) == False:
                    return False

                appendAt = varAt.var
            elif ( (tyAt in self.m_dctClAlgDtElm.values())
               and isMatched(sqAg[i], tyAt)
            ):
                # e.g. case([3,(4,(5,6)),7 ], [Leaf1, Rcsv], tyAt) 
                appendAt = sqAg[i]
            else:
                #assert False, str(var)    # to debug
                return False

            self.var.append(appendAt)

            if tyAt == Rcsv:
                break

        self.var = tuple(self.var)
        return True

vr = Var()
"""' vr = Var() 
e.g. 
//@@
import tlRcGn as tn
if tn.vr.case([1, 2,3, 'a'], (int, float, str) ):
    print "int:",tn.vr[0], " float:",tn.vr[1], " str:",tn.vr[2]
//@@@
'"""

"""'
if __name__ == "__main__":
    #========== test0 basic ==============================
    assert vr.case(1, int)


    # corresponding O'Caml code
    # type tree = Leaf of int | Node of tree * tree ;;
    # let rec height = function
    #      Leaf _ -> 0
    #    | Node(l, r) -> 1 + max (height l) (height r) ;;
    vr.mkAlgDT(Leaf=(int,), Node=(Rcsv, Rcsv) )
    def hight(sqAg):
        vAt = Var(vr)
        if vAt.case(sqAg, vAt.Leaf):
            return 0
        elif vAt.case(sqAg, vAt.Node):
            return 1+max(hight(vAt[0]), hight(vAt[1]) )

    assert hight( [1, (2,3)] ) == 2

    # corresponding O'Caml code
    # type 'a tree = Leaf of 'a | Node of 'a tree * 'a tree ;;
    # let rec height = function
    #      Leaf _ -> 0
    #    | Node(l, r) -> 1 + max (height l) (height r) ;;
    vr.mkAlgDT(Leaf=(Type,), Node=(Rcsv, Rcsv) )
    def hight(sqAg, tyAg):
        vAt = vr(tyAg)
        if vAt.case(sqAg, vAt.Leaf):
            return 0
        elif vAt.case(sqAg, vAt.Node):
            return 1+max(hight(vAt[0],tyAg), hight(vAt[1],tyAg) )

    assert hight( [1, (2,3)], int ) == 2
    #========== test1 [3,4,5] ==============================
    var = Var()
    assert var.case([3,4,5], [3,4, Any]) 
    assert (     var[0] == 3 
             and var[1] == 4
             and var[2] == 5 )

    #========== test2 [3,(4,(5,6)),7 ], Leaf Node ==========
    var.mkAlgDT(  Leaf1=(int,)
                    ,Leaf2=(int,int)
                    ,Node2 = (Rcsv, Rcsv)
                    ,Node3 = (Rcsv, Rcsv, Rcsv)
           )

    assert var.case([3,(4,(5,6)),7 ], [var.Leaf1, Rcsv]) 
    assert (     var[0] == 3 
             and var[1] == [(4,(5,6)),7]
             and len(var) == 2 )

    assert var.case([3,(4,(5,6)),7 ], [var.Leaf1, var.Node2, var.Leaf1]) 
    assert (     var[0] == 3 
             and var[1] == (4,(5,6))
             and var[2] == 7
             and len(var) == 3 )


    #========== test3 ======================================
    # compare to;;http://www.aclevername.com/projects/splarnektity/
    s = ('quote',
      ('netlist',
        ('namespace', 'connector', ('main-board', 'J2')),
        ('namespace', 'fpga', ('main-board', 'U17')),
        ('net', ('connector', '1'), ('fpga', 'AE12')),
        ('net', ('connector', '2'), ('fpga', 'AA22')),
        ('net', ('connector', '3'), ('connector', '4'), ('fpga', 'B32')) 
      )
    )

    if var.case(s, ['quote', Any]):
        pass
    else:
        assert False

    if var.case(s, ['quote', ('netlist', Rcsv)]):
        #pass
        assert var[1][0] == 'netlist'
        assert var[1][1][0][0] == 'namespace'
        assert var[1][1][0][1] == 'connector'
        assert var[1][1][0][2] == ('main-board', 'J2')
        varAt = var
        var2 = Var()
        if var2.case( var[1][1][0], ('namespace',Any,Any) ):
            assert var2[0] == 'namespace'
            assert var2[1] == 'connector'
            assert var2[2] == ('main-board', 'J2')

        assert var[1][0] == 'netlist'
        assert var[1][1][0][0] == 'namespace'
        assert var[1][1][0][1] == 'connector'
        assert var[1][1][0][2] == ('main-board', 'J2')
    else:
        assert False

    #========== test4: poly variant for abstract algebraic data type ==========
    var.mkAlgDT(  Leaf=(T,T)
                 ,Node = (Rcsv, Rcsv)
           )
    varAt=var(int)
    assert varAt.case([(3,4),((5,6),(7,8))], [varAt.Leaf, Rcsv])
    assert varAt[0] == (3,4)
    assert varAt[1] == ((5,6),(7,8))

    assert not varAt.case([(3,'4'),((5,6),(7,8))], [varAt.Leaf, Rcsv])

    assert varAt.case([(3,4),((5,6),(7,8))], [varAt.Node, Rcsv])
    assert varAt[0] == (3,4)
    assert varAt[1] == ((5,6),(7,8))
    assert varAt.case([(3,'4'),((5,6),(7,8))], [varAt.Node, Rcsv])
    
    #========== test5:  ================
    # compare to;;http://www.ocaml-tutorial.org/ja/data_types_and_matching
    var.mkAlgDT(  String=(str,)
                       , Plus = (Rcsv, Rcsv)
                       , Minus = (Rcsv, Rcsv)
                       , Times = (Rcsv, Rcsv)
                       , Devide = (Rcsv, Rcsv)
               )
    
    def to_string(algExpAg):
        var1 = Var(var)
        if   var1.case(algExpAg, var1.Plus):
            return "("+to_string(var1[0]) + " + " + to_string(var1[1])+")"
        elif var1.case(algExpAg, var1.Minus):
            return "("+to_string(var1[0]) + " - " + to_string(var1[1])+")"
        elif var1.case(algExpAg, var1.Times):
            return "("+to_string(var1[0]) + " * " + to_string(var1[1])+")"
        elif var1.case(algExpAg, var1.Devide):
            return "("+to_string(var1[0]) + " / " + to_string(var1[1])+")"
        elif var1.case(algExpAg, var1.String):
            return var1[0]
        else:
            assert False

    expAt =  var.Times( var.String('5'), var.Plus(var.String('2'),var.String('3')) )
    assert to_string(expAt) == "(5 * (2 + 3))"
    expAt =  var.Times( var.String('x'), var.Plus(var.String('y'),var.String('z')) )
    assert to_string(expAt) == "(x * (y + z))"
    #print Devide(2,3)

    #========== test one liner ===================================
    assert var.case([1,'test', 3.2], [int, str, float])

    var.case([1,(5,6)], [int,Rcsv]); assert var[1] == (5,6)

    print var.Plus
'"""

# ============================ Algebraic Data Type end ===========================


#;;\lng\python25\python -m pdb tlRcGn.py
#;;\lng\python25\python tlRcGn.py
