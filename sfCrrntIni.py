# -*- encoding: utf-8 -*-
"""'
english:
    PythonSf sfCrrntIni.py
    https://github.com/lobosKobayashi
    http://lobosKobayashi.github.com/
    
    Copyright 2016, Kenji Kobayashi
    All program codes in this file was designed by kVerifierLab Kenji Kobayashi

    I release souce codes in this file under the GPLv3
    with the exception of my commercial uses.

    2016y 12m 28d Kenji Kokbayashi

japanese:
    PythonSf sfCrrntIni.py
    https://github.com/lobosKobayashi
    http://lobosKobayashi.github.com/

    Copyright 2016, Kenji Kobayashi
    このファイルの全てのプログラム・コードは kVerifierLab 小林憲次が作成しました。
    
    作成者の小林本人に限っては商用利用を許すとの例外条件を追加して、
    このファイルのソースを GPLv3 で公開します。

    2016年 12月 28日 小林憲次
'"""

"""'
python では、戻り値を tuple にできるので、複数の値を返すことができる
type を返すような関数は扱わないものとする
<== instance list/tuple で戻り値の type としているときを扱えるようにするため。
    <== tuple 値を返す category function の戻り値を一つの関数でチェックすることもある
        <== m_outType の length で確認できる
<== type parameter として None を与えたときは don&t care を意味する
    <== None 事態であることを示したいときは集合 {None} を使う
<== collection type を指定するときは set/frozense で引き渡すことにする
    <== 入力が {1,2,3} のタイプであることは 1 or 2 or 3 の値しか与えないことを意味する
        <== CT クラス内部では frozense にしてやり、変更しないことを明記する
    <== その順序に意味がないことを強制する
    <== 目視で python sf 式上で　collection type を指定していることを明示できる
    <== list/tuple は複数の入力引数／tuple 戻り値であることを意味させる
        <== 一つの type list で一つの入力引数／一つの戻り値であることを明記することも許す
        <== 一つの関数で複数の入力／出力タイプチェックをすることも可能にする
    <== CT([1,2,3],[0,1]) のような instance sequence での入出力型指定は許さない
        <== z,a,b,c=0,1,2,3; CT([a,b,c],[z,a]) と書いたとき、式だけからでは
            [a,b,c] が type 指定か instance 指定か見分けられないからです
            <== z,a,b,c=0,1,2,3; CT({a,b,c},{z,a}) と書くことで instance 指定を明確化します
            <== これならば、CT({int,int},{0,1}) などと型自体を instance として渡すこともできます
<== category だけではなく、一般の python 関数でも使えるように配慮する
    <== キー･ワード引数の型はどうする
        <== 当面は詰めない
        <== いっぺんに そこまで考えきれない
        <== 後々らくにするための考慮だけはしておくべき
        <== CT に渡す段階でキー･ワードまで決まることになる
            <== CT の段階ではキー･ワード引数に型を渡しておく
            <== キー･ワード引数の文字列も含めた型付けとなる
                <== キー･ワード引数の文字列も含めた型付けが嫌なときは複数の CT instace を作る
            <==
<== def f(*.sqAg):... であり かつ関数による型チェックならば、可変長引数であっても型チェックを続けられる
<== 戻り側の値の複数型チェックは、戻り値が tuple のときのみ行う
    <== category theory では、複数の型のデータを戻すという考えがない
        <== プログラムを作る上では欲しい
        <== 逆に一つの tuple を返すプログラムを扱えなくなる
            <== list を返すことで多くの場合は逃げられる
<== もともと collection type は集合を前提としているコードに見える

注意：class CT における、input,outpu 引数のタイプ・チェックが本当に正しいか、注意深い検討が必要です
<== metaclass type は types module に入っていません
    <==でも右の式が通っています;; ηx1= fCT(λ x,y:(Z3(1), y),[Z3,Z3],[Z3,Z3]); ηx1(Z3(0),Z3(2))
            if all([type(x) in (types.TypeType, types.ClassType,
                                types.FunctionType,
                                set, frozenset)
                 or isinstance(x, CT)
                 or hasattr(x, '__call__')
                 or isinstance(x, (sf.sc.ndarray, sf.ClTensor, sf.ClFldTns))
                    for x in inputTypeOrSqTypeAg]):

                self.m_tplInType = tuple(inputTypeOrSqTypeAg)

多変数戻り値で許されるのは、戻り値の型が __len__ method を備えたものだけです。
    例：,tuple, list, ndarray, ClTensor, ClFldTns のときまでです
'"""

"""'
CT; category theory class
    input/output type checking
    ct=CT([int,float],complex); f,g=ct(λ x,y:x+y `i),ct(λ x,y: x y `i); f(3,4.0),g(3, 4.0)
    ===============================
    ((3+4j), 12j)

    ct=CT([int,float],complex); f,g=ct(λ x,y:x+y `i),ct(λ x,y: x y `i); f(3.1,4.0)
    Traceback (most recent call last):
        snipped
    pysf.sfFnctns.ClAppError: Error at CT:__call__(..) input type check:3.1

    CT:__call__(self, fnAg)
        Currying

usage:
    Currying
    ct=CT([Z5,Z5],Z3);f=ct(λ x,y:Z3(x+y)).fst(Z5(3)); f(Z5(1))
    ===============================
    Z3(1)
    f=fCT(λ x,y:Z3(x+y), [Z5,Z5],Z3).fst(Z5(3)); f(Z5(2))
    ===============================
    Z3(0)

'"""
import pysf.sfFnctns as sf
#import pysf.octn as oc


def Assert(ag, strAg="at Assert(..)"):
    if ag == False:
        # print strAg   # debug
        raise sf.ClAppError(strAg)
    else:
        return True

import types

class CT(object):
    """' class for typed function and Currying
    ----------------------------------------
    --- Input/Output type check function ---
    ----------------------------------------
                fn:int→float   fn     int→float
    usage:;; ct=CT(int, float); f=ct(λ x: 2.5*x); f(3)
             ct=CT(int, float); f=ct(λ x: 2.5*x); f(3.1)   # AssertError
             ct=CT(int, float); f=ct(λ x: 2  *x); f(3  )   # AssertError

        type check for collection type
             f:{0,1,2} --> {0,1,2,3,4,5,6,7,8,9,0}
             ct=CT({0,1,2}, {0,1,2,3,4,5,6,7,8,9,0}); f=ct(λ x: ... )
          collection type(set type in other words) was indicated
        only by a set/frozenset/kfs. You can&t use a tuple or a list.

             ct=CT({0,1,2}, set(range(10))); f=ct(λ x: 2  *x); f(2)
             ct=CT({0,1,2}, set(range(10))); f=ct(λ x: 2  *x); f(3) # input type error
             ct=CT({0,1,2}, set(range(10))); f=ct(λ x: 6  *x); f(2) # output type error

    -------------------------------------------------
    --- Currying functions for first/last argment ---
    -------------------------------------------------
      e.g.
    f=CT()(λ x,y:x+2y).fst(3); f(1),f(2),f(3)
    ===============================
    (5, 7, 9)

    You can use Currying functions without type checks.
    f=CT()(λ x,y:x+y).fst(3); f(1),f(2),f(3)
    ===============================
    (4, 5, 6)
    f=CT()(λ x,y:x+2y).lst(3); f(1),f(2),f(3)
    ===============================
    (7, 8, 9)

    '"""
    def __init__(self, inputTypeOrSqTypeAg=None, outTypeAg=None):
        from pysf.ptGrp import kfs
        if inputTypeOrSqTypeAg == None:
            self.m_tplInType = None
        elif isinstance(inputTypeOrSqTypeAg, (tuple, list)):
            # New Type Class:types.TypeType
            # Classical Class:types.ClassType
            if all([type(x) in (types.TypeType, types.ClassType,
                                types.FunctionType,
                                types.NoneType,     # add 2011.11.23
                                set, frozenset, kfs) # add kfs 2016.01.11
                 or isinstance(x, CT)
                 or hasattr(x, '__call__')
                 or isinstance(x, (sf.sc.ndarray, sf.ClTensor, sf.ClFldTns))
                    for x in inputTypeOrSqTypeAg]):

                self.m_tplInType = tuple(inputTypeOrSqTypeAg)
            else:
                self.m_tplInType = (tuple(inputTypeOrSqTypeAg), )
        elif isinstance(inputTypeOrSqTypeAg, set):
            self.m_tplInType = (frozenset(inputTypeOrSqTypeAg),)
        else:
            self.m_tplInType = (inputTypeOrSqTypeAg,)
            #self.m_tplInType = inputTypeOrSqTypeAg

        if outTypeAg == None:
            self.m_outType = None
        elif isinstance(outTypeAg, (tuple, list)):
            assert all([type(x) in (types.TypeType, types.ClassType,
                                types.FunctionType,
                                types.NoneType,     # add 2011.11.23
                                set, frozenset, kfs)  # add kfs 2016.01.11  
                 or isinstance(x, CT)
                 or hasattr(x, '__call__')
                 or isinstance(x, (sf.sc.ndarray, sf.ClTensor, sf.ClFldTns))
                                                   for x in outTypeAg])
            self.m_outType = tuple(outTypeAg)
        elif isinstance(outTypeAg, set):
            self.m_outType = (frozenset(outTypeAg),)
        else:
            self.m_outType = (outTypeAg,)
        """'
        if outTypeAg == None:
            self.m_outType = None
        elif isinstance(outTypeAg, (tuple,list)):
            self.m_outType = ( tuple(outTypeAg), )
        else:
            self.m_outType = ( outTypeAg, )
        '"""

    def isType(self, x, tyAg):
        """' Check x is in tyAg. tyAg may be
                a set,list or tuple or
                a function that takes one argment and return a bool value or
                a type e.g. int, float, ... , class or
                any instance that can check == for x
        '"""
        if isinstance(tyAg,  types.NoneType):   # add 2011.11.23
            return True
        elif isinstance(tyAg, (set,sf.sc.ndarray, sf.ClTensor, sf.ClFldTns)):
            # tuple, lst, set
            return x in tyAg
        elif isinstance(tyAg, CT):
                assert hasattr(x,'func_name')
                assert hasattr(x,'dom')
                assert hasattr(x,'cod')
                assert x.dom == tyAg.m_tplInType
                assert x.cod == tyAg.m_outType
                return True
        elif type(tyAg) == types.FunctionType:
        #elif hasattr(tyAg,'func_name'):
            # typAg is a function that takes one argment and return a bool value
            return tyAg(x)
        elif type(tyAg) == type or isinstance(tyAg, type):
            # tyAg is a type e.g. int, float, ... , class
            return isinstance(x,tyAg)
        elif isinstance(tyAg, frozenset):
            return x in tyAg
        elif x == tyAg:
            # tyAg is a instance that can check == for x
            return True
        else:
            assert False, ("In isType(..) we have encountered unexpected"
                         + " Object: "+str(tyAg)
                          )

    def __call__(self, fAg):
        """' Instantiate typed function from non typed fAg
            not function composition
        '"""
        def _(*sqAg):
            """' _ is an actual function that checks in/out types
            '"""
            if _.dom == None:
                pass
            elif len(_.dom)==1 and isinstance(_.dom[0], types.FunctionType):
                Assert(_.dom[0](*sqAg),
                        "Error at CT:__call__(..) input type check:"
                        + str(sqAg)
                      )
            elif len(_.dom)==1 and isinstance(_.dom[0], (set, frozenset)):
                    # h=fCT(λ x:x[0],{(1,5),(2,5)}, int); h((1,5)) == 1
                    #  h=fCT(λ x,y:x,{(1,5),(2,5)}, int); h(1,5) これは assert error.
                    #  <== {(1,5),(2,5)} に属することで型を確認しており、入力は一変数関数
                    Assert(sqAg[0] in _.dom[0],
                            "Error at CT:__call__(..) input type check by set:"
                            + str(sqAg)
                          )
            else:
                assert len(sqAg) == len(_.dom)

                for k in range(len(sqAg)):
                    Assert(self.isType(sqAg[k], _.dom[k]),
                            "Error at CT:__call__(..) input type check:"
                            + str(sqAg[k])
                          )

            valAt = fAg(*sqAg)
            if (_.cod)==None:
                pass
            elif isinstance(valAt, tuple):
            #elif hasattr(valAt, "__len__"):
                if len(_.cod)==1 and isinstance(_.cod[0], types.FunctionType):
                    Assert(_.cod[0](*sqAg),
                            "Error at CT:__call__(..) output type check by function:"
                            + str(valAt)
                          )
                elif len(_.cod)==1 and isinstance(_.cod[0], (set, frozenset)):
                    # h=fCT(λ x:(2,5),int,{(1,5),(2,5)}); h(10) == (2,5)
                    Assert(valAt in _.cod[0],
                            "Error at CT:__call__(..) output type check by set:"
                            + str(valAt)
                          )
                else:
                    assert len(valAt) == len(_.cod)

                    for k in range(len(valAt)):
                        Assert(self.isType(valAt[k], _.cod[k]),
                                "Error at CT:__call__(..) output type check:"
                                + str(valAt[k])
                              )

            else:
                assert len(_.cod) == 1
                Assert(self.isType(valAt, _.cod[0]),
                      "Error at CT:__call__(..) output type check:"
                      + str(valAt)
                      )

            return valAt

        def fst(ag):
            def __(*sqAg):
                return _(*((ag,)+sqAg))

            if _.dom == None:
                return CT()(__)
            else:
                ctAt = CT(_.dom[1:], _.cod)
                return ctAt(__)

        def lst(ag):
            def __(*sqAg):
                return _(*(sqAg+(ag,)))

            if _.dom == None:
                return CT()(__)
            else:
                ctAt = CT(_.dom[:-1], _.cod)
                return ctAt(__)

        _.dom = self.m_tplInType
        _.cod = self.m_outType

        if _.dom == None:
            #if fAg.func_code.co_argcount >= 2:
            #Can't use the upper condition because
            #   (lambda *s:sum(s)).func_code.co_argcount == 0
                _.fst = fst
                _.lst = lst
        elif len(_.dom) >= 2:
            _.fst = fst
            _.lst = lst

        _.f, _.l=fst,lst
        return _

def fCT(f, inputTypeOrSqTypeAg=None, outTypeAg=None):
    # "input/outputTypeorSqTypeAg == None" means "Don't care"
    import copy
    inputTypeOrSqTypeAg = copy.deepcopy(inputTypeOrSqTypeAg)
    outTypeAg = copy.deepcopy(outTypeAg)

    ctAt = CT(inputTypeOrSqTypeAg, outTypeAg)
    return ctAt(f)

def isIF(x):
    return isinstance(x, (int,float))

isN = isIF  # obsolete

def f2CT(f, ty=None, tyOut=None):
    # comment
    if ty==None and tyOut==None:
        return fCT(f,[None,None],tyOut)
    elif ty!=None and tyOut==None:
        return fCT(f, [ty,ty], ty)
    else:
        # ty!=None and tyOut!=None:
        return fCT(f, [ty,ty], tyOut)

def cmps(f,g):
    """' composition of typed functions:f ~* g. f's argemnt must be only 1.
    '"""
    if hasattr(g, '__call__'):
        pass
    else:
        assert hasattr(g, 'func_code') and g.func_code.co_argcount == 1

    if ( hasattr(f, 'dom') and hasattr(g, 'cod')
     and not ((f.dom == None) or (f.dom == (None,))) and not (g.dom == None)
    ):
        assert f.dom == g.cod

        def _(*sqAg):
            if f.func_code.co_argcount > 1:
                return f(*g(*sqAg))
            else:
                return f(g(*sqAg))

        #_.dom = g.dom
        #_.cod = f.cod
        ctAt = CT(g.dom, f.cod)
        return ctAt(_)
    else:
        return lambda *x:f(g(*x))

#k__tilda__UsOp_mul____ = cmps
#k__tilda__UsOp_xor____ = cmps # a ~^ b
k__tilda__UsOp_mod____ = cmps # a ~% b

import pysf.octn as oc
# ~* Z5 octonion multiply
Oc = oc.Oc
k__tilda__UsOp_mul____ = lambda x,y:Oc(sf.krry((Oc(x) * Oc(y)).m_tpl, Z5)) # ~*

fAd=flAd=f2CT(lambda x,y:x+y)
fMl=flMl=f2CT(lambda x,y:x*y)

# using algebra related ones
# kfs;  sorted frozenset
# Sb:   substituting Symmetric Group class
# Cy:   make Symmetric Group instance from a cyclic parameter
# extend;make a symmetric group from a set of symmetric group instances or kfs families
# ClZp: Zp(N) class
# TyZp; metaclass for the ClZp to make a pickable Zp(N) instances.
from pysf.ptGrp import kfs, Cy, extend, group, Sb, TyZp, ClZp, gp
TyZp.N = 2
class Z2(ClZp): pass
TyZp.N = 3
class Z3(ClZp): pass
TyZp.N = 4
class Z4(ClZp): pass
TyZp.N = 5
class Z5(ClZp): pass
TyZp.N = 6
class Z6(ClZp): pass
TyZp.N = 7
class Z7(ClZp): pass

TyZp.N = 127
class Z127(ClZp): pass
Zb=Z127

isMtZ5=fCT(lambda x,tpl: isinstance(x, sf.ClFldTns) and x.m_type==Z5 and x.shape==tpl)

class O2(Oc):
    def __init__(self, *sqAg):
        if len(sqAg) == 1:
            if hasattr(sqAg[0], '__len__'):
                tplAt = tuple(sqAg[0])
            elif hasattr(sqAg[0], '__getitem__'):
                tplAt = tuple(sqAg[0][:])
            else:
                tplAt = (sqAg[0],)
        else:
            tplAt = tuple(sqAg)

        Oc.__init__(self, sf.krry(tplAt, ftype=Z2))

    def __str__(self):
        return "O2" + super(O2, self).__str__()[2:]

class O3(Oc):
    def __init__(self, *sqAg):
        if len(sqAg) == 1:
            if hasattr(sqAg[0], '__len__'):
                tplAt = tuple(sqAg[0])
            elif hasattr(sqAg[0], '__getitem__'):
                tplAt = tuple(sqAg[0][:])
            else:
                tplAt = (sqAg[0],)
        else:
            tplAt = tuple(sqAg)

        Oc.__init__(self, sf.krry(tplAt, ftype=Z3))

    def __str__(self):
        return "O3" + super(O3, self).__str__()[2:]

class O4(Oc):
    def __init__(self, *sqAg):
        if len(sqAg) == 1:
            if hasattr(sqAg[0], '__len__'):
                tplAt = tuple(sqAg[0])
            elif hasattr(sqAg[0], '__getitem__'):
                tplAt = tuple(sqAg[0][:])
            else:
                tplAt = (sqAg[0],)
        else:
            tplAt = tuple(sqAg)

        Oc.__init__(self, sf.krry(tplAt, ftype=Z4))

    def __str__(self):
        return "O4" + super(O4, self).__str__()[2:]

class O5(Oc):
    def __init__(self, *sqAg):
        if len(sqAg) == 1:
            if hasattr(sqAg[0], '__len__'):
                tplAt = tuple(sqAg[0])
            elif hasattr(sqAg[0], '__getitem__'):
                tplAt = tuple(sqAg[0][:])
            else:
                tplAt = (sqAg[0],)
        else:
            tplAt = tuple(sqAg)

        Oc.__init__(self, sf.krry(tplAt, ftype=Z5))

    def __str__(self):
        return "O5" + super(O5, self).__str__()[2:]

class O6(Oc):
    def __init__(self, *sqAg):
        if len(sqAg) == 1:
            if hasattr(sqAg[0], '__len__'):
                tplAt = tuple(sqAg[0])
            elif hasattr(sqAg[0], '__getitem__'):
                tplAt = tuple(sqAg[0][:])
            else:
                tplAt = (sqAg[0],)
        else:
            tplAt = tuple(sqAg)

        Oc.__init__(self, sf.krry(tplAt, ftype=Z6))

    def __str__(self):
        return "O6" + super(O6, self).__str__()[2:]

class O7(Oc):
    def __init__(self, *sqAg):
        if len(sqAg) == 1:
            if hasattr(sqAg[0], '__len__'):
                tplAt = tuple(sqAg[0])
            elif hasattr(sqAg[0], '__getitem__'):
                tplAt = tuple(sqAg[0][:])
            else:
                tplAt = (sqAg[0],)
        else:
            tplAt = tuple(sqAg)

        Oc.__init__(self, sf.krry(tplAt, ftype=Z7))

    def __str__(self):
        return "O7" + super(O7, self).__str__()[2:]

class Ob(Oc):
    def __init__(self, *sqAg):
        if len(sqAg) == 1:
            if hasattr(sqAg[0], '__len__'):
                tplAt = tuple(sqAg[0])
            elif hasattr(sqAg[0], '__getitem__'):
                tplAt = tuple(sqAg[0][:])
            else:
                tplAt = (sqAg[0],)
        else:
            tplAt = tuple(sqAg)

        Oc.__init__(self, sf.krry(tplAt, ftype=Z127))

    def __str__(self):
        return "Ob" + super(Ob, self).__str__()[2:]

O127=Ob

if __name__ == "__main__":
    #ct=CT(float,float);f=ct(λ x:3+x); g=ct(λ x:4x); (f~^g)(5.)
    ct=CT(float,float)
    f=ct(lambda x:3+x)
    g=ct(lambda x:4*x)
    assert cmps(f,g)(5.) == 23

    #ct=CT([float,float],float);fm=ct(λ x,y:x*y);(fm.fst(3.) ~^ fm.fst(4.))(5.)
    ct=CT([float,float],float)
    fm=ct(lambda x,y:x*y)
    assert cmps(fm.fst(3.),  fm.fst(4.))(5.) == 60.0

    f=fCT(lambda x,y:x+y, [float,float],float)
    assert f(3., 4.) == 7.0

    f=cmps(lambda x:x+1, lambda x:x*2)
    assert f(1) == 3

    assert flAd.fst(3)(4) == 7
    assert flAd.lst(3)(4) == 7

    assert flMl.fst(3)(4) == 12
    assert flMl.lst(3)(4) == 12

    #f=CT()(λ x,y:x+y)
    f=CT()(lambda x,y:x+y)
    assert f.fst(3)(4) == 7
    assert f.lst(3)(4) == 7

    f=isMtZ5.lst((3,))
    assert isMtZ5.lst((3,))(sf.krry(1,2,3,Z5)) # assert shape==(3,) Z5 vector

    innrP3=fCT(lambda x,y:x*y, [f,f],Z5)
    assert innrP3(sf.krry([1,2,3,Z5]),sf.krry([4,5,6,Z5])) == 2

    f=fCT(lambda x,y:x+y, [set([1,2,3]),set([4,5,6])],set(range(9)))
    assert f(2,4) == 6
    assert f(2,5) == 7
    assert f(3,5) == 8


    try:
        ct=CT(int, float)
        f=ct(lambda x: 2.5*x)
        assert f(3) == 7.5
        f(3.1)   # AssertError
    except sf.ClAppError, valAt: pass
    assert str(valAt) == 'Error at CT:__call__(..) input type check:3.1'
    try:
        f=ct(lambda x: 2 *x)
        f(3)
    except sf.ClAppError, valAt: pass
    assert str(valAt) == 'Error at CT:__call__(..) output type check:6'

    try:
        ct=CT(set([0,1,2]), set(range(10)))
        f=ct(lambda x: 2 *x)
        assert f(2) == 4
        f(3)
    except sf.ClAppError, valAt: pass
    assert str(valAt) == 'Error at CT:__call__(..) input type check:3'
    try:
        f=ct(lambda x: 6 *x)
        f(2) # output type error
    except sf.ClAppError, valAt: pass
    assert str(valAt) == 'Error at CT:__call__(..) output type check:12'

    # check undefinite input length using type check function
    try:
        ct=CT(lambda *sq:all([isinstance(elm,int) for elm in sq]))
        f=ct(lambda x,y: x+y)
        assert f(3,4) == 7

        f(3.1,4)
    except sf.ClAppError, valAt: pass
    assert str(valAt) == 'Error at CT:__call__(..) input type check:(3.1, 4)'

    assert O3(1,2,3) == (1,2)
    assert O3([1]) == 1
    assert O3(4) == 1
    assert O3([4,3,2]) == (1,0,2)
    assert O3(4,3,2) == (1,0,2)

    # date:2011/11/11 (金) time:08:23 戻り値が lsit, ndarray, ClFldTns のとき飛んでいた
    #testF = fCT(lambda x:  [Z5(1),Z5(2)], Z5,[Z5,Z5])
    testF = fCT(lambda x:  (Z5(1),Z5(2)), Z5,[Z5,Z5])
    assert testF(Z5(4))[1] == 2
    """'
    date:2011/11/17 (木) time:22:50
    ベクトルやリストを返す関数は、他変数戻り値の関数とは看做さない。
    ベクトルやリストの戻り値は、一つのリストまたはベクトルを返しているはず。
    プログラム・コードとしても複数の戻り値を表現するのにリストやベクトルを使うのは誤り。
    testF = fCT(lambda x:  sf.krry([Z5(1),Z5(2)], dtype=object), Z5,[Z5,Z5])
    assert testF(Z5(4))[1] == 2
    testF = fCT(lambda x: sf.krry([Z5(1),Z5(2)]), Z5,[Z5,Z5])
    assert testF(Z5(4))[1] == 2
    testF = fCT(lambda x: [Z5(1),O5(2)], Z5,[Z5,O5])
    assert testF(Z5(4))[1] == 2
    '"""

    # date:2011/11/12 (土) OcOctonion で O2,O3, .. O7 の加減乗除算が OcOctonion を返していた
    # O2,O3, ... O7 を返すように type(self)(...) を返すコードにした
    f=f2CT(lambda x,y:x*y, lambda x:isinstance(x,O5) and x[2:]==(0,)*6)
    assert f(O5(2,3), O5(1,2)) == (1,2)

    # date:2011/11/12 ptGrp.ClZp に __cmp__(...) を追加して
    # [Z5(k)<Z5(k+1) for k in range(4)] の値が
    # [False, True, False, True] ではなく [True, True, True True] になるようにした
    assert all( [Z5(k)<Z5(k+1) for k in range(4)] )

    # 2011.11.22 出力が None:don&t care のときを追加した
    f=fCT(lambda x:x+1,None, [None])
    assert f(3) == 4

    f=fCT(lambda x:(x,x+1),None, [None,int])
    assert f(3) == (3,4)

    # 下で AssertError になっていた
    ct=CT([None,None])
    f=ct(lambda x,y:x+y)
    assert f(3,4) == 7

    f=fCT(lambda x,y: 1.1*x*y,[int,int])
    assert abs(f(3,4) - 13.2) <1e-10

    f=fCT(lambda x,y: 1.1*x*y,[int,int],float)
    assert abs(f(3,4) - 13.2) <1e-10

    f=f2CT(lambda x,y: 1.1*x*y,int,float)
    assert abs(f(3,4) - 13.2) <1e-10
    f=f2CT(lambda x,y: 1.1*x*y,None,float)
    assert abs(f(3,4.) - 13.2) <1e-10

# Fp, Fs make a Laplace operator matrix for two-terminal network.
# Fp:Lapalace operator matrix for a parallel element
# Fs:Lapalace operator matrix for a serial element
# e.g.;; R=1k` ohm`; Fp(R)
# ===============================
#  [[ClRtnl([ 1.],[ 1.]), ClRtnl([-0.001],[ 1.])],
#   [ClRtnl([ 0.],[1]), ClRtnl([ 1.],[ 1.])]]
# ---- ClFldTns:<class 'pysf.rational.ClRtnl'> ----
# e.g.;; R=1k` ohm`; Fs(R)
# ===============================
#  [[ClRtnl([ 1.],[ 1.]), ClRtnl([ 0.],[1])],
#   [ClRtnl([-1000.],[ 1.]), ClRtnl([ 1.],[ 1.])]]
#  ---- ClFldTns:<class 'pysf.rational.ClRtnl'> ----
Fp = lambda Z:sf.krry__(*[[1.0,-1.0/Z],[0.0,1.0], sf.ClRtnl])
Fs = lambda Z:sf.krry__(*[[1.0,0.0],[-Z*1.0,1.0], sf.ClRtnl])

import wave as wv
import numpy as sc
#import pysf.sfFnctns as sf
#(nchannels, sampwidth, framerate, nframes, comptype, compname)
wavePrmsStt = None
def readWv(strFileAg):
    global wavePrmsStt

    if not( len(strFileAg)>=4 and strFileAg[-4:].upper()=='.WAV'):
        strFileAg = strFileAg + ".wav"

    fileAt = wv.open(strFileAg)
    wavePrmsStt = fileAt.getparams()
    strAt = fileAt.readframes(wavePrmsStt[3])
    #dataAt = sf.krry(sc.fromstring(strAt, sc.int16), int)
    # More frequently we use sc.array multiply for audio data
    #than inner product
    dataAt = (sc.fromstring(strAt, sc.int16)     )
    return dataAt

def writeWv(vctAg, strFileAg='_tmp.wav'):
    prmAt=wavePrmsStt
    if not( len(strFileAg)>=4 and strFileAg[-4:].upper()=='.WAV'):
        strFileAg = strFileAg + ".wav"

    fileAt=wv.Wave_write(strFileAg)
    if prmAt == None:
        fileAt.setparams(
                (1, 2, 16000, 32000, 'NONE', 'not compressed'))
    elif isinstance(prmAt, int):
        fileAt.setparams(
                (1, 2, prmAt, 2*pmmAt, 'NONE', 'not compressed'))
    else:
        fileAt.setparams(prmAt)

    if isinstance(vctAg, sc.ndarray) and vctAg.dtype==sc.int16:
        pass
    else:
        vctAg = sc.array(vctAg, dtype=sc.int16)

    fileAt.writeframes(vctAg.tostring())

def kqvr2d(ag,vag=True, blShow=True, **kwargs):
    """' An experimental implement of 2-dimmentional vector distribution plot.
    Yet we have not implemented plots when position parameter matrix is given.
    Yet we have not implemented color and log compression
    '"""
    import pylab as pb

    pb.figure()
    if vag in (True,False):
        blShow = vag
        vag=None

    if vag == None:
        # matrix (column,row) corresponds each position of arrow vector.
        if not isinstance( ag, (sf.ClTensor, sf.sc.ndarray) ):
            ag = sf.krry(ag)
        # [::-1,:] reverse columns because pb.quiver display [0,0] at the lower left
        #ag=sf.sc.array(ag.view())
        #ag=sf.sc.array(ag.view())#[:,::-1]
        #ag=sf.sc.array(ag.view()).T[::-1,:]

        shapeat = ag.shape
        if ag.dtype == object:
        #if ag.dtype in (object, np.dtype('int32'), np.dtype('float64')) :
            # you can set a list/tuple/array/ClTensor as an element of matrix
            # e.g.
            # ag is rank 2 of tuple,array/cltensor elements, the length of every elements is 2 
            #  [[(1,2), ... , (5,1)],
            #  ,[(2,5), ... , (6,5)],
            #      .     .       .
            #  ,[(0,3), ... , (3,5)], dtype=object]
            shapeat = ag.shape
            assert len(shapeat) >= 2
            assert len(ag[0,0]) == 2
            def gettns(ag, xy):
                return [[ ag[i,j][xy] for j in range(shapeat[0])]
                                      for i in range(shapeat[1])]
                                     
            
            #ag=ag[::-1,:]      # 要素ベクトルの向きはグラフ座標だから、行列の colmn だけを変えてもあかん
            #ag=ag[::-1,::-1]    # 見た目が行列とグラフでは、column が反転するから
            #ag=ag.T[::-1,::-1]    # 見た目が行列とグラフでは、column が反転するから
            #ag=ag.T[::-1,::-1].T    # 見た目が行列とグラフでは、column が反転するから
            #ag=ag.T[::-1,::-1].T[::-1,::-1]    # 見た目が行列とグラフでは、column が反転するから
            #ag=ag[::-1,::-1].T    # 見た目が行列とグラフでは、column が反転するから
            ag=ag[::-1,:].T[:,::-1]
            pb.quiver(gettns(ag,0),gettns(ag,1), **kwargs)
            #pb.quiver(gettns(ag,1),gettns(ag,0), **kwargs)

        elif len(shapeat) == 3:
            # n x m x 2 array/ClTensor
            # 2d 
            #  [[[1,2], ... , [5,1]],
            #  ,[[2,5], ... , [6,5]],
            #      .     .       .
            #  ,[[0,3], ... , [3,5]]]]
            #pb.quiver(ag[:,:,1],ag[:,:,0], **kwargs)
            #ag=ag[::-1,::-1]
            #ag=ag[::-1,::-1].T[::-1,::-1]
            #ag=ag[::-1,::-1].T[::-1,:]
            #ag=ag[::-1,::-1].T[:,::-1]
            #pb.quiver(ag.b[:,:,0],ag.b[:,:,1], **kwargs)
            if isinstance(ag, sf.ClTensor):
                # ClTensor では not alined になる
                ag = ag.b
            ag=ag[::-1,::-1]
            pb.quiver(ag[:,:,1],ag[:,:,0], **kwargs)
            #ag=ag[::-1,:].T
            #pb.quiver(ag[:,:,0],ag[:,:,1], **kwargs)
        else:
            assert False, "unexpected parameter:"+str(ag)
        """'
            if len(ag[0,0]) == 2:
            # n x m x 2 array/ClTensor
            # 2d 
            #  [[[1,2  ], ... , [5,1  ]],
            #  ,[[2,5  ], ... , [6,5  ]],
            #      .       .       .
            #  ,[[0,3  ], ... , [3,5  ]]]]
                mlb_().quiver3d(ag[:,:,0],ag[:,:,1],sf.kzrs(shapeat[:2])
                                                                , **kwargs)
            #else:
            # n x m x 3 array/ClTensor
            #     3d vector on 0 plain
            #  [[[1,2,3], ... , [5,1,4]],
            #  ,[[2,5,4], ... , [6,5,3]],
            #      .       .       .
            #  ,[[0,3,8], ... , [3,5,1]]]]
                mlb_().quiver3d(ag[:,:,0],ag[:,:,1], ag[:,:,2], **kwargs)
        
        else:
            # n x m x l x 3 array/ClTensor by mgrid(..)
            # 3d
            # [[[[1,2,3], ... , [5,1,2]],
            #  ,[[2,5,0], ... , [6,5,4]],
            #      .       .       .
            #  ,[[0,3,2], ... , [3,5,1]]]]

            mlb_().quiver3d(ag[:,:,:, 0],ag[:,:,:, 1],ag[:,:,:, 2], **kwargs)
        '"""

    if blShow:
        pb.show()

"""'
if __name__ == "__main__":
    #f = ClWave(r'D:\work\alice\segment\goverment.wav')
    #f = ClWave(r'c:\work\alice\segment\goverment.wav')
    dataAt =  readWv(r'\work\alice\segment\goverment.wav')
    print dataAt.shape

    writeWv(sc.r_[dataAt,dataAt])
'"""

class ClDoubleEndedArray(sc.ndarray):
    """' Experimental implementation of double ended array for the 2d discrete Mikusinski operator.
    We dare to avoid default double because ?
    '"""
    def __new__(subtype, data, lft=None, dtype=float, copy=True):
        """'lft:left index
        '"""
        #import pdb; pdb.set_trace()
        if lft!=None and isinstance(lft, type(object)):
            # You can set below PythonSf one-liner
            # ;;drry(range(10),int)
            dtype=lft
            lft=None

        if isinstance(data, sc.ndarray):
            None
        else:
            data=sc.array(data)
        shapeAt=data.shape
        if len(shapeAt)==0:
            data = sc.array([data])
            shapeAt=(1,)

        if lft==None:
            # default center
            tplInLeftAt = tuple(-(x//2) for x in shapeAt)
            tplInRightAt= tuple(x+tplInLeftAt[k] for k,x in enumerate(shapeAt))
        else:
            if isinstance(lft, int):
                lft=(lft,)
            tplInLeftAt = tuple(lft)
            tplInRightAt= tuple(x+tplInLeftAt[k] for k,x in enumerate(shapeAt))

        if dtype == object:
            arAt=sc.ndarray.__new__(subtype, data,dtype=dtype)
        else:
            if sc.iscomplexobj(data) and dtype in (bool, int, long, float):
                arAt=sc.ndarray.__new__(subtype, shapeAt,dtype=complex)
            else:
                arAt=sc.ndarray.__new__(subtype, shapeAt,dtype=dtype)
        
        arAt.ravel()[:] = data.ravel()
        arAt.m_tplInLeft = tplInLeftAt
        arAt.m_tplInRight = tplInRightAt

        # Return the newly created object:
        return arAt

drry = ClDoubleEndedArray

def url2str(strAg):
    """'usage:
    url2str(u'https://ja.wikipedia.org/wiki/%E3%83%A6%E3%83%BC%E3%82%AF%E3%83%AA%E3%83%83%E3%83%89%E5%8E%9F%E8%AB%96')
    ===============================
    https://ja.wikipedia.org/wiki/ユークリッド原論
    
    Cation! You must set a unicode string: u'...'. 
    If you set a ordinary ascii string, the PythonSf will return Traceback error as below.
    lurl2str('https://ja.wikipedia.org/wiki/%E3%83%A6%E3%83%BC%E3%82%AF%E3%83%AA%E3%83%83%E3%83%89%E5%8E%9F%E8%AB%96')
    '"""
    import urllib2 as md

    return md.unquote(strAg).encode('raw_unicode_escape').decode('utf-8').encode('utf-8')

# 下のコードは github に出すときは comment out する 
#import rpy2.robjects as robjects
#ro=robjects.r
#rof=robjects.FloatVector

# run R code from python
# example: pr();pR('sapply(1:5, function(x){2+x})')
def pr():
    import pyper as pr
    pR = pr.R(use_pandas='True')
    sf.__getDctGlobals()['pR']=pR
    sf.__getDctGlobals()['pr']=pr

    return pR

def XyMt(strAg):
    strHead=(
    r"""\documentclass{jarticle}
    \usepackage[all]{xy}
    \usepackage{BOONDOX-ds, BOONDOX-frak, amsmath, amssymb, mathrsfs}
    \usepackage{fancybox}
    \begin{document}
    \[\xymatrix{
    """
    )
    # 2016.12.21 set back {fancybox} lines to make orthogonal to LaTeX(..), XyXy(..)

    strTail=(r"""
    }\]
    \end{document}"""
    )

    fl=open('temp.tex','w')
    fl.write(strHead + strAg + strTail)
    fl.close()

    import os
    #os.system("platex temp.tex")
    if 0 != os.system("platex -halt-on-error temp.tex"):
        return
    #os.system("start temp.dvi")
    os.system("dvipdfmx temp.dvi")
    os.system("atril temp.pdf&")

XyPic =  XyMt   # Obsolete! Use XyMt date:2016/08/31

def XyXy(strAg):
    strHead=(
    r"""\documentclass{jarticle}
    \usepackage[all]{xy}
    \usepackage{BOONDOX-ds, BOONDOX-frak, amsmath, amssymb, mathrsfs}
    \usepackage{fancybox}
    \begin{document}
    \begin{xy}
    """
    )

    strTail=(r"""
    \end{xy}
    \end{document}"""
    )

    fl=open('temp.tex','w')
    fl.write(strHead + strAg + strTail)
    fl.close()

    import os
    #os.system("platex temp.tex")
    if 0 != os.system("platex -halt-on-error temp.tex"):
        return
    #os.system("start temp.dvi")
    os.system("dvipdfmx temp.dvi")
    os.system("atril temp.pdf&")

def LaTeX(strAg):
    strHead=(
    r"""\documentclass{jarticle}
    \usepackage{BOONDOX-ds, BOONDOX-frak, amsmath, amssymb, mathrsfs}
    \usepackage{fancybox}
    \begin{document}
    """
    )

    strTail=(r"""
    \end{document}"""
    )

    fl=open('temp.tex','w')
    fl.write(strHead + '$$' + strAg +'$$' + strTail)
    fl.close()

    import os
    #os.system("platex -halt-on-error `temp.tex")
    if 0 != os.system("platex -halt-on-error temp.tex"):
        return
    #os.system("start temp.dvi")
    os.system("dvipdfmx temp.dvi")
    os.system("atril temp.pdf&")

def Circuit(*sqStrAg):
    strHead=(
    r"""\documentclass{jarticle}
    \usepackage[dvipdfmx]{graphicx}
    \usepackage{circuitikz}
    \begin{document}
    \begin{circuitikz}
    """
    )

    strTail=(r"""
    \end{circuitikz}
    \end{document}"""
    )

    fl=open('temp.tex','w')

    strAt = strHead;
    for strX in sqStrAg:
        strAt += '\draw '+ strX +';'
    strAt += strTail

    fl.write(strAt)
    fl.close()

    import os
    #os.system("platex -halt-on-error `temp.tex")
    if 0 != os.system("platex -halt-on-error temp.tex"):
        return
    if 0 != os.system("dvipdfmx temp.dvi"):
        return
    os.system("gvfs-open temp.pdf&")

def svg():
    import svgwrite as svg

    dwg=svG = svg.Drawing(filename='test.svg')
    svG.viewbox(width=1000, height=1000)
    # viewBox を大きくすることで、web 表示領域に合わせて自動的に svg 表示が拡大されるのを防ぐ

    sf.__getDctGlobals()['svg']=svg
    sf.__getDctGlobals()['svG']=svG
    sf.__getDctGlobals()['dwg']=dwg

    def show():
        """'save and start'"""
        import os
        svG.save()
        os.system("start test.svg")

    sf.__getDctGlobals()['show']=show
    sf.__getDctGlobals()['shwSvg']=show

    return svG

# Comment out "ksv shwSvg jctx" because they request to install non
# essential package:svgwrite and PyV8
#
#from pysf.kSvgTxt import ksv
#from pysf.kSvgTxt import show as shwSvg
#
def jctx():
    # Make java script context and change jctx from function to module.
    import PyV8 as md
    jctx=md.JSContext()
    jctx.enter()
    sf.__getDctGlobals()['jctx']=jctx
    return 

def ejr(strAg):
    import os
    strAt = r'grep -n -i "'+strAg+r'" ~/utl/eij/EIJIRO52.txt'
    os.system(strAt)
#

from pysf.ptGrp import setNicknames as fnPt
from pysf.ptGrp import FreeGrp as St

# experimental implementation of neighborhood norm date:2016/11/04
normZn=lambda x: sum(min(int(x[k]), int(-x[k])) for k in range(8 if isinstance(x,Oc) else len(x)))

def tdSb(sbAg):
    # teardown Sb
    kfsPairAt = kfs(zip(range(sbAg.__len__()), sbAg.m_tpl))
    lsRtn=[]
    while kfsPairAt != kfs():   # kfsPairAt != φ
        # get first pair
        nAt = kfsPairAt[0][0]
        dctKfsPairAt = dict(kfsPairAt)
        lsNAt=[]
        dctPairAt={}
        # get a chain of pairs begininng by n
        while nAt not in lsNAt:
            lsNAt.append(nAt)
            nextAt = dctKfsPairAt[nAt]
            dctPairAt.update({nAt:nextAt})
            nAt = nextAt
        
        # print dctPairAt # to debug

        kfAt = kfs(dctPairAt.items())
        lsRtn.append(kfAt)
        kfsPairAt -= kfAt
        
    return lsRtn
        
def nrmSb(sbAg):
    lsKfsAt = tdSb(sbAg)
    #print lsKfsAt  # to debug

    return sum(kf.__len__()-1 for kf in lsKfsAt)

