# -*- encoding: utf-8 -*-
"""'
english:
    PythonSf pysf/ptGrp.py
    https://github.com/lobosKobayashi
    http://lobosKobayashi.github.com/
    
    Copyright 2016, Kenji Kobayashi
    All program codes in this file was designed by kVerifierLab Kenji Kobayashi

    I release souce codes in this file under the GPLv3
    with the exception of my commercial uses.

    2016y 12m 28d Kenji Kokbayashi

japanese:
    PythonSf pysf/ptGrp.py
    https://github.com/lobosKobayashi
    http://lobosKobayashi.github.com/

    Copyright 2016, Kenji Kobayashi
    このファイルの全てのプログラム・コードは kVerifierLab 小林憲次が作成しました。
    
    作成者の小林本人に限っては商用利用を許すとの例外条件を追加して、
    このファイルのソースを GPLv3 で公開します。

    2016年 12月 28日 小林憲次
'"""

"""'
 permutation group 
 Sb: Substituting class. In another word, permutation

'"""
import sfFnctns as sf

def gp(blAg = True):
    Sb._blGAPglb = blAg

# permutation group
class Sb(object):
    """' A permutaion group class that is used to substitute
    
    sb= Sb([2,0,3,1])
    assert (sb**3)*(0,1,2,3) == (1, 3, 0, 2)
    assert [sb**k *[0,1,2,3] for k in range(10)][1] ==  (2, 0, 3, 1)
    assert (Sb( [2, 0, 3, 1] )**-1 )((2, 0, 3, 1)) == (0, 1, 2, 3)
    assert (Sb( [2, 0, 3, 1] )**-1 )== (1, 3, 0, 2)
    assert (Sb( [2, 0, 3, 1] )**-2 )((2, 0, 3, 1)) == (1, 3, 0, 2)
    assert  Sb( [2, 0, 3, 1] )(['a','b','c','d'])== ['c', 'a', 'd', 'b']
    assert (Sb( [2, 0, 3, 1] )**-1 )(['a','b','c','d']) == ['b', 'd', 'a', 'c']
    assert  Sb( [2, 0, 3, 1] )(('a','b','c','d'))== ('c', 'a', 'd', 'b')
    assert Cy(1,2,4) * Cy(3,5) == (0, 2, 4, 5, 1, 3)
    assert Cy(3,5) * Cy(1,2,4) == (0, 2, 4, 5, 1, 3)
    assert Cy(0,1) * Cy(0,1,2,3,4,5,6,7) == (0, 2, 3, 4, 5, 6, 7, 1)
    assert (Sb(2, 0, 3, 1)**-1 )((2, 0, 3, 1)) == (0, 1, 2, 3)
    assert Sb(1,0) == (1,0,2,3)
    assert Sb(1,0,2,3) == (1,0)
    assert Sb(0,1) == Sb(0,1,2)

    cycle attribute returns a Cy(...) multiplication string
    Sb(1,2,3,0,4,5,6,7,9,10,11,8,12,13,14,15,16,17,18,19).cyclic
    ===============================
    Cy(0,1,2,3) Cy(8,9,10,11)
    '"""
    _blGAPglb = False
    def __init__(self, *sqAg):
        if len(sqAg) == 1 and hasattr(sqAg[0], '__len__'):
            sqAt = sqAg[0]
        else:
            sqAt = sqAg

        tplAt = tuple(sqAt)
        assert max(tplAt)+1 == len(tplAt)
        assert len(set(tplAt)) == len(tplAt)
        self.m_tpl = tuple(tplAt)

    def __mul__(self, ag):
        # assert len(self) <= len(ag)
        # assert len(self) >=0
        # print Sb._blGAPglb    # to debug
        if Sb._blGAPglb == True:
            if isinstance(ag, kfs):
                return ag.__rmul__(self)

            lstAt = range(max(len(self), len(ag)))
            lstAt[:len(self)] = self
            if len(self) < len(ag):
                lstAt[len(self):] = ag[len(self):]
            for k in range(len(lstAt)):
                if k<len(self) and self[k] < len(ag):
                #if ag[k] < len(self):
                    lstAt[k] = ag[self[k]]
            return Sb(lstAt)
        else:
            if isinstance(ag, kfs):
                return ag.__rmul__(self)

            lstAt = range(max(len(self), len(ag)))
            lstAt[:len(ag)] = ag
            if len(ag) < len(self):
                lstAt[len(ag):] = self[len(ag):]
            for k in range(len(lstAt)):
                if k<len(ag) and ag[k] < len(self):
                #if ag[k] < len(self):
                    lstAt[k] = self[ag[k]]
            return Sb(lstAt)

    def __pow__(self, inAg):
        if inAg > 0:
            tmpAt = self
            for k in range(inAg-1):
                tmpAt = self.__mul__(tmpAt)

            return Sb(tmpAt)
        elif inAg == 0:
            return Sb(range(len(self)))
        else:
            sbAt = Sb( [self.index(k) for k in range(len(self))] )
            tmpAt = sbAt
            inAt = -inAg
            for k in range(inAt-1):
                tmpAt = sbAt.__mul__(tmpAt)

            return Sb(tmpAt)

    def __call__(self, ag):
        if hasattr(ag, "__len__"):
            lstAt = list(ag)
        elif hasattr(ag, "__getitem__"):
            lstAt = list(ag[:])
        else:
            assert False,("At Sb.__call__, we recieved unmanageable "
                         +"argement:"+str(ag)
                         )
        
        for k in range(len(self)):
            if self[k] < len(lstAt):
                lstAt[self[k]] = ag[k]

        if isinstance(ag, sf.ClFldTns):
            return sf.krry(lstAt, ftype=ag.m_type)
        elif isinstance(ag, sf.ClTensor):
            return sf.krry(lstAt, dtype=ag.dtype)
        elif type(ag) == sf.np.ndarray:
            return sf.np.array(lstAt)
        elif type(ag) == str:
            return "".join(lstAt)
        else:
            return type(ag)(lstAt)


    def __len__(self):
        return len(self.m_tpl)

    def __ne__(self, ag):
        if not isinstance(ag,Sb):
            return True
        else:
            return not self.__eq__(ag)

    def __eq__(self, ag):
        if not isinstance(ag,Sb):
            return False

        tplL,tplR = self.m_tpl,ag.m_tpl
        if len(tplL) > len(tplR):
            tplL,tplR = tplR,tplL

        lenL,lenR = len(tplL),len(tplR)

        if tplL != tplR[:lenL]:
            return False

        if tplR[lenL:] == tuple(range(lenL, lenR)):
            return True
        else:
            return False

        #"""'
        #if hasattr(ag, "m_tpl"):
        #    return self.m_tpl == ag.m_tpl
        #elif hasattr(ag, "__len__"):
        #
        #2011/11/20 上の条件を入れると Sb(0,1) == Sb(0,1,2) と言えなくなる
        #m_tpl をは多用されており、ag.m_tpl との比較が正当だとする根拠が薄い
        #'"""
        #if hasattr(ag, "__len__"):
        #    if len(self) > len(ag):
        #        lenAt = len(ag)
        #        if self.m_tpl[lenAt:] != tuple(range(lenAt, len(self.m_tpl))):
        #            return False
        #        else:
        #            return self.m_tpl[:lenAt] == tuple(ag)
        #    elif len(self) == len(ag):
        #        at = tuple(ag)
        #        return self.m_tpl == at
        #    else:
        #        # len(self) < len(ag):
        #        lenAt = len(self.m_tpl)
        #        if tuple(ag[lenAt:]) != tuple(range(lenAt, len(ag))):
        #            return False
        #        else:
        #            return self.m_tpl == tuple(ag)[:lenAt]
        #elif hasattr(ag, "__getitem__"):
        #    ag = ag[:]
        #    if len(self) > len(ag):
        #        lenAt = len(ag)
        #        if self.m_tpl[lenAt:] != tuple(range(lenAt, len(self.m_tpl))):
        #            return False
        #        else:
        #            return self.m_tpl[:lenAt] == tuple(ag)
        #    elif len(self) == len(ag):
        #        at = tuple(ag)
        #        return self.m_tpl == at
        #    else:
        #        # len(self) < len(ag):
        #        lenAt = len(self.m_tpl)
        #        if tuple(ag[lenAt:]) != tuple(range(lenAt, len(ag))):
        #            return False
        #        else:
        #            return self.m_tpl == tuple(ag)[:lenAt]
        #else:
        #    return self.m_tpl == ag

    def __getitem__(self, *ag, **kwAg):
        return self.m_tpl.__getitem__(*ag, **kwAg)

    def index(self, ag):
        return self.m_tpl.index(ag)

    def __str__(self):
        return "Sb"+str(self.m_tpl).replace(" ","")

    def __repr__(self):
        return "Sb"+str(self.m_tpl).replace(" ","")

    def __hash__(self):
        return hash(self.m_tpl)

    def next(self, inAg):
        """' Return next index substituted by a Sb instance:self.m_tpl
        e.g.
        Sb(5, 0, 3, 7, 9, 2, 4, 6, 8, 1).next(0)
        ===============================
        5
        Sb(5, 0, 3, 7, 9, 2, 4, 6, 8, 1).next(1)
        ===============================
        0
        '"""
        assert isinstance(inAg,int)
        if 0<= inAg <len(self.m_tpl):
            return self.m_tpl[inAg] 
        else:
            return inAg 

    """'
    user shuffle
    Sb(shuffle(range(10)))
    ===============================
    Sb(5,2,1,7,6,9,3,4,8,0)

    @statiticmethod
    def random(inSizeAg, inAg=None, lst=[]):
             Return random a permutated tuple. The elements are less than
        inSizeAg and not duplicated. 
        e.g.;; seed(0); Sb.random(10)
        ===============================
        (5, 0, 3, 7, 9, 2, 4, 6, 8, 1)
            
        if inAg == None:
            inAg = sf.randint(inSizeAg)

        if len(lst)>=inSizeAg:
            return Sb( lst )
        elif inAg in lst:
            return Sb.random(inSizeAg, sf.randint(inSizeAg),lst)
        else:
            lst.append(inAg)
            return Sb.random(inSizeAg, sf.randint(inSizeAg),lst)
    '"""

    def __getattr__(self, name):
        def __sign( inSgnAg=1, lstAg=None ):
            if lstAg == None:
               lstAg = list(self.m_tpl) 

            if len(lstAg) == 0:
               return inSgnAg

            lstAt=[]
            inAt, lstAg = lstAg[0], lstAg[1:]
            if len(lstAg) == 0:
                return inSgnAg

            lstAt.append(inAt)
            while(True):
                if inAt == self.m_tpl[inAt]:
                    return __sign(inSgnAg, lstAg)

                inAt = self.m_tpl[inAt]
                if inAt in lstAt:
                    #print lstAt     # debug
                    return __sign(inSgnAg, lstAg)

                inSgnAg *= -1
                lstAt.append(inAt)
                lstAg.remove(inAt)

        def __cyclic( strAg="", lstAg=None ):
            """' Return a string of cyclic discription
            '"""
            if lstAg == None:
               #lstAg = list(self.m_tpl) 
               lstAg = range( len(self.m_tpl) ) 

            if len(lstAg) == 0:
               return strAg

            lstAt = []
            inAt, lstAg = lstAg[0], lstAg[1:]
            if len(lstAg) == 0:
                return strAg

            lstAt.append(inAt)
            while(True):
                if inAt == self.m_tpl[inAt]:
                    return __cyclic(strAg, lstAg)

                inAt = self.m_tpl[inAt]
                if inAt in lstAt:
                    #print lstAt     # debug
                    if strAg == "":
                        return __cyclic("Cy"+ str(tuple(lstAt)).replace(" ",""), lstAg)
                    else:
                        return __cyclic(strAg+ " Cy"+ str(tuple(lstAt)).replace(" ",""), lstAg)

                lstAt.append(inAt)
                lstAg.remove(inAt)

        if name == "sign":
            return __sign()
        elif name == "cyclic":
            return __cyclic()
        else:
            raise AttributeError("There is no attribute in Sb:"+ name)

    def __cmp__(self, ag):
        if isinstance(ag, (int,long,float) ):
            for elm in self.m_tpl:
                if elm == ag:
                    continue
                else:
                    return cmp(elm,ag)

            return 0
        elif hasattr(ag, "m_tpl"):
            if len(self.m_tpl) == len(ag.m_tpl):
                return cmp(self.m_tpl, ag.m_tpl)
            else:
                return cmp(len(self.m_tpl), len(ag.m_tpl))
        if hasattr(ag, "__getitem__"):
            return cmp(self.m_tpl, ag[:])
        else:
            cmp(self.m_tpl, ag)

    def __hash__(self):
        """ Experimental implement 2014.11.13"""
        n=len(self.m_tpl)-1
        tpl=tuple(range(n+1))
        for k in tpl:
            if tpl[n-k] != self.m_tpl[n-k]:
                break

        return hash(self.m_tpl[:n+1-k])

def Cy(*sqAg):
    """' return a cyclic permutaion defined by the argument.
    e.g.
    Cy(2,3)
    ===============================
    Sb(0,1,3,2)

    Cy(2,3,5)
    ===============================
    Sb(0,1,3,5,4,2)
    '"""
    if len(sqAg) == 1 and hasattr(sqAg[0], '__len__'):
        sqAt = sqAg[0]
    else:
        sqAt = sqAg

    lstAt = range(max(sqAt)+1)
    lstAt[sqAt[-1]] = sqAt[0]
    for k in range(1,len(sqAt)):
        lstAt[sqAt[k-1]]=sqAt[k]
        
    return Sb(lstAt)


class kfs(frozenset):
    """' frozenset that has
         +: for a scalar argument; add it for all elements
            for a collection argument; union it for self
         *: for a scalar argument; multiply it for all elements
            for a collection argument; intersect it for self
    e.g.
    kfs([1,2,3])+[10]
    ===============================
    kfs([1, 2, 3, 10])

    kfs([1,2,3])+ 10
    ===============================
    kfs([11, 12, 13])

    kfs([1,2,3])+ [10,20]
    ===============================
    kfs([1, 2, 3, 10, 20])

    kfs([1,2,3])* [2,3,4,5]
    ===============================
    kfs([2, 3])

    kfs(...) instance has sl property which returns sorted a list
    e.g.
    st=kfs([(1,3),(0,2),(1,1), (0,1)]); [x for x in st.sl]
    ===============================
    [(0, 1), (0, 2), (1, 1), (1, 3)]

    st=kfs([(1,3),(0,2),(1,1), (0,1)]); [x for x in st   ]
    ===============================
    [(0, 1), (1, 3), (0, 2), (1, 1)]
    '"""
    def __new__(cls,*sqAg):
        if len(sqAg) == 1:
            if hasattr(sqAg[0], '__iter__'):
                tplAt=sqAg[0]
            else:
                tplAt=(sqAg[0],)
        else:
            tplAt=sqAg

        return frozenset.__new__(cls, tplAt)

    def __getattr__(self, name):
        if name == "oi" or name == "orderedIterator":
            # .oi property is obsolete. Use sl:sortedList.
            def __generator():
                lstAt=sorted(tuple(self))
                for at in lstAt:
                    yield at

            return __generator()
        elif name == "p":
            if "p" in self.__dict__:
                # p attribute is constructed already.
                return self.p
            else:
                # return tuple like as ClTensorInstance.p
                #tplAt = tuple(sorted(tuple(self)))
                #tplAt = tuple(sorted(tuple(self), key=lambda x: tuple(x) if isinstance(x, kfs) else x))    # date:2016/10/08 (土) time:09:06
                tplAt = tuple(sorted(tuple(self), key=lambda x: sorted(tuple(x)) if isinstance(x, kfs) else x))
                self.__dict__.update({"p":tplAt})
                return tplAt

        elif name == "sl" or name == "sortedList":
            # sorted(..) must return list instance
            return list(self.p)

        raise AttributeError("There is no attribute in kfs:"+ name)

    def __mul__(self, ag):
        if isinstance(ag, (frozenset, set, list, tuple, xrange)):
            return kfs(self.intersection(ag))
        else:
            return kfs([at * ag for at in self])

    def __rmul__(self, ag):
        if isinstance(ag, (frozenset, set, list, tuple, xrange)):
            return kfs(self.intersection(ag))
        else:
            return kfs([ag * at for at in self])

    def __add__(self, ag):
        if isinstance(ag, (frozenset, set, list, tuple, xrange)):
            return kfs(self.union(ag))
        else:
            return kfs([at + ag for at in self])

    def __radd__(self, ag):
        if isinstance(ag, (frozenset, set, list, tuple, xrange)):
            return kfs(self.union(ag))
        else:
            return kfs([ag + at for at in self])

    def __div__(self,ag):
        """'If ag is an kfs/frozenset/set/list/tuple/xrange instance
        then return a left quotient ksf instance
        else return a kfs instance that elments are divided by ag
        e.g.
            kfs([1,2,3,4,5])/kfs([2,3,4])
            ===============================
            kfs([1, 5])

            kfs([1,2,3,4,5])/[2,3,4]
            ===============================
            kfs([1, 5])

            kfs([1,2,3,4,5])/2
            ===============================
            kfs([0, 1, 2])

            kfs([1,2,3,4,5])/2.0
            ===============================
            kfs([0.5, 1.0, 1.5, 2.0, 2.5])

        '"""
        if isinstance(ag, (frozenset, set, list, tuple, xrange)):
            if not isinstance(ag, kfs):
                ag = kfs(ag)
            lstAt=[]
            setAt=set([])
            for elmAt in self.sl:
                if elmAt in setAt:
                    continue
                else:
                    lstAt.append(elmAt)
                    #setAt = setAt + elmAt * ag
                    setAt = setAt + ag.__rmul__(elmAt)

            return kfs(lstAt)
        else:
            lstAt = [ elmAt/ag for elmAt in self.sl]
            return kfs(lstAt)

    def __truediv__(self,ag):
        return self.__div__(ag)

    def __str__(self):
        #return ("kfs(" + str([at for at in self.oi]) + ")").replace(" ","")
        #return "kfs(" + str([at for at in self.oi]) + ")"
        try:
            #return "kfs(" + str(self.sl) + ")"
            return "kfs(" + str(self.sl)[1:-1] + ")"
        except TypeError, errValAt:
            return super(kfs, self).__str__()
    def __repr__(self):
        #return "kfs(" + str([at for at in self.oi]) + ")"
        #return "kfs(" + str(self.sl) + ")"
        return self.__str__()

    def preImage(self, f):
        return kfs([elm for elm in self.sl if f(elm)])


    def __getitem__(self, ag):
        return self.p.__getitem__(ag)

    #def __cmp__(self, ag):
    #    if isinstance(ag, kfs):
    #        return cmp(self.p, ag.p)
    #    else:
    #        return cmp(self,ag)

    def __lt__(self,ag):
        """' Return True/False for partial order without ==.
        CATION! if self == ag then __lt__ returns False.

        '"""
        #assert isinstance(ag, (frozenset,set)), "You set a non set parameter:"+str(ag)+ " in kfs.__lt__."
        if not isinstance(ag, (frozenset,set)):
            raise sf.ClAppError("You set a non set parameter:"+str(ag)+ " in kfs.__lt__.")
        return self.issubset(ag) and self!=ag

    def __le__(self,ag):
        """' Return True/False for partial order that contains ==.

        '"""
        #assert isinstance(ag, (frozenset,set)), "You set a non set parameter:"+str(ag)+ " in kfs.__le__."
        if not isinstance(ag, (frozenset,set)):
            raise sf.ClAppError("You set a non set parameter:"+str(ag)+ " in kfs.__le__.")
        return self.issubset(ag)

    def __gt__(self,ag):
        """' Return True/False for partial order without ==.
        CATION! if self == ag then __lt__ returns False.

        '"""
        #assert isinstance(ag, (frozenset,set)), "You set a non set parameter:"+str(ag)+ " in kfs.__gt__."
        if not isinstance(ag, (frozenset,set)):
            raise sf.ClAppError("You set a non set parameter:"+str(ag)+ " in kfs.__gt__.")
        return ag.issubset(self) and self!=ag

    def __ge__(self,ag):
        """' Return True/False for partial order that contains ==.

        '"""
        #assert isinstance(ag, (frozenset,set)), "You set a non set parameter:"+str(ag)+ " in kfs.__ge__."
        if not isinstance(ag, (frozenset,set)):
            raise sf.ClAppError("You set a non set parameter:"+str(ag)+ " in kfs.__ge__.")
        return ag.issubset(self)

"""'
    We should define kft:typed frozen set which is implemented by has a relation ship
to secure being a same type for all elements

class kft(object):
    def __init___(sqAg, dtype=None):
        if dtype==None:
            # guess type froms sqAg[0]
            pass
        self.m_type = dtype
        self.m_kfc = kfc([dtype(elm) for elm in sqAg])

    def __add__(self, ag):
        # if ag type is not the self.m_type then cast it/them
        pass

    def __getattr__(self, name):
        if name in var(kfc).keys():
            self.m_kfc.__dict__[name]
        else:
            assert False, ("...")
        
'"""

def fXY(setAg):
    """'
    setAt = set(setAg)
    x=setAt.copy().pop()

    setAt.add(x*x**-1);
    return frozenset([x* y for x,y in sf.mitr(setAt,setAt)])
    #return frozenset([x* y for x,y in sf.mitr(setAg,setAg)])
    return frozenset([x* y for x,y in sf.mitr(setAg,setAg)]).union(setAg)
    '"""
    return kfs([x* y for x,y in sf.mitr(setAg,setAg)]).union(setAg)

def extend(ag, fnAg=None, newerAg=None, inMaxAg=10000):
    """'Extend a sqeuence:tuple,list,ndarray,set or a iterator to a ksf by 2 term operation:default *.
    fnAg: default grouping method --> if None then use __mul__:*

For example.
extend([Cy(0,1), Sb(0,1,2)])
    '"""
    if newerAg == None:
        # Now is the first time. Align Sb instance length.
        if isinstance(ag, kfs):
            kfsAt = ag
        else:
            kfsAt = kfs(ag)
    else:
        assert isinstance(ag, kfs)
        kfsAt = ag

    inCountAt = 0
    if fnAg==None:
        # lstTmpAt = [ x*y for x in kfsAt for y in kfsAt ] might eats up squared memories.
        kfsTmpAt = kfs()
        for x in kfsAt:
            kfsTmpAt += kfs( x*y for y in kfsAt )
        kfsNewAt = kfsTmpAt - kfsAt
        while True:
            kfsTmpAgNewerAt=kfs()
            for x in kfsNewAt:
                kfsTmpAgNewerAt += x * kfsNewAt

            # lstTmpNewerAgAt = [ x*y for x in kfsNewAt for y in kfsAt ]
            kfsTmpNewerAgAt = kfs()
            for x in kfsNewAt:
                kfsTmpNewerAgAt += x * kfsAt

            # lstTmpNewerNewerAt = [ x*y for x in kfsNewAt for y in kfsNewAt ]
            kfsTmpNewerNewerAt = kfs()
            for x in kfsNewAt:
                kfsTmpNewerNewerAt += x * kfsNewAt

            kfsAt = kfsAt + kfsNewAt

            kfsNewAt = ( kfsTmpAgNewerAt+kfsTmpNewerAgAt+kfsTmpNewerNewerAt ) - kfsAt

            if kfsNewAt == kfs([]):
                return kfsAt

            inCountAt += 1
            assert inCountAt < inMaxAg, ("In extend(..), loop count exeeds max count:inMaxAg:"
                                         + str(inMaxAg))
    else:
        assert hasattr(fnAg, '__call__'), ("You set a non functional parameter fow fnAg"
            + " in extend(..).:"+str(fnAg) )

        # lstTmpAt = [ fnAg(x,y) for x in kfsAt for y in kfsAt ]
        kfsTmpAt = kfs()
        for x in kfsAt:
            kfsTmpAt += kfs( fnAg(x,y) for y in kfsAt )
        kfsNewAt = kfsTmpAt - kfsAt
        while True:
            # lstTmpAgNewerAt = [ fnAg(x,y) for x in kfsAt for y in kfsNewAt ]
            kfsTmpAgNewerAt = kfs()
            for x in kfsAt:
                kfsTmpAgNewerAt += kfs( fnAg(x,y) for y in kfsNewAt )
            
            # lstTmpNewerAgAt = [ fnAg(x,y) for x in kfsNewAt for y in kfsAt ]
            kfsTmpNewerAgAt = kfs()
            for x in kfsNewAt:
                kfsTmpNewerAgAt += kfs( fnAg(x,y) for y in kfsAt )

            # lstTmpNewerNewerAt = [ fnAg(x,y) for x in kfsNewAt for y in kfsNewAt ]
            kfsTmpNewerNewerAt = kfs()
            for x in kfsNewAt:
                kfsTmpNewerNewerAt += kfs( fnAg(x,y) for y in kfsNewAt )

            kfsAt = kfsAt+kfsNewAt

            kfsNewAt = ( kfsTmpAgNewerAt+kfsTmpNewerAgAt+kfsTmpNewerNewerAt ) - kfsAt

            if kfsNewAt == kfs([]):
                return kfsAt

            inCountAt += 1
            assert inCountAt < inMaxAg, ("In extend(..), loop count exeeds max count:inMaxAg:"
                                         + str(inMaxAg))
def group(*sq,**dct):
    """' Obsolete! Use extend(..)
    '"""
    return extend(*sq,**dct)


import octn as oc
class TyZp(type):
    N = 2

    def __new__(cls, name, bases, dict):
        # use static integer m_NStt to be refered by users
        assert isinstance(TyZp.N, (int, long) ) and (int(TyZp.N) != 0)
        dict['m_NStt'] = int(TyZp.N)
        return type.__new__(cls, name, bases, dict)

class ClZp(object):
    __metaclass__ = TyZp

    def __init__(self, ag):
        if isinstance(ag, (int,long) ):
            self.m_val = int(ag % type(self).m_NStt)
        elif isinstance(ag, ClZp):
            self.m_val = int(ag.m_val)%type(self).m_NStt
        elif isinstance(ag, oc.Oc):
            assert isinstance(ag.m_tpl[0], ClZp)
            assert ag.m_tpl[1] == 0

            self.m_val = int(ag.m_tpl[0])%type(self).m_NStt
        elif hasattr(ag,'__int__') and not isinstance(ag,type):
            # bool type has __int__
            self.m_val = int(ag)%type(self).m_NStt
        else:
            assert False, ("At __init__ in ClZp, Unexpected argment:"
                          +str(ag) )

    def __add__(self, ag):
        if isinstance(ag, (sf.ClFldTns, oc.ClOctonion)):
            return ag.__radd__(self)
        elif isinstance(ag, (int,long) ):
            return type(self)( (self.m_val + ag)%type(self).m_NStt)
        elif isinstance(ag, ClZp):
            return type(self)( (self.m_val + ag.m_val)%type(self).m_NStt)
        else:
            # date:2011/11/17 (木) time:06:41
            # counter measure for  p=oc.Pl([1,2,3,4], O7); p( oc.Pl([1,2,3],O7) )
            try:
                return type(self)( (self.m_val + int(ag))%type(self).m_NStt)
            except:
                return ag.__radd__(self)

    def __radd__(self, ag):
        if isinstance(ag, (sf.ClFldTns, oc.ClOctonion)):
            return ag.__add__(self)
        elif isinstance(ag, (int,long) ):
            return type(self)( (self.m_val + ag)%type(self).m_NStt)
        elif isinstance(ag, ClZp):
            return type(self)( (self.m_val + ag.m_val)%type(self).m_NStt)
        else:
            return type(self)( (self.m_val + int(ag))%type(self).m_NStt)

    def __sub__(self, ag):
        if isinstance(ag, (sf.ClFldTns, oc.ClOctonion)):
            return ag.__rsub__(self)
        elif isinstance(ag, (int,long) ):
            return type(self)( (self.m_val - ag)%type(self).m_NStt)
        elif isinstance(ag, ClZp):
            return type(self)( (self.m_val - ag.m_val)%type(self).m_NStt)
        else:
            # ClFldTns, oc.ClOctonion, int, ClZp 以外との組み合わせ動作は保障できない
            # 下で動かしておく
            return type(self)( (self.m_val - int(ag))%type(self).m_NStt)

    def __rsub__(self, ag):
        if isinstance(ag, (sf.ClFldTns, oc.ClOctonion)):
            return ag.__sub__(self)
        elif isinstance(ag, (int,long) ):
            return type(self)( (ag - self.m_val)%type(self).m_NStt)
        elif isinstance(ag, ClZp):
            return type(self)( (ag.m_val - self.m_val)%type(self).m_NStt)
        else:
            # ClFldTns, oc.ClOctonion, int, ClZp 以外との組み合わせ動作は保障できない
            # 下で動かしておく
            return type(self)( (int(ag) - self.m_val)%type(self).m_NStt)

    def __mul__(self, ag):
        if isinstance(ag, sf.ClFldTns):
            return ag.__rmul__(self)
        elif isinstance(ag, (int,long)):
            return type(self)( (self.m_val * ag)%type(self).m_NStt)
        elif isinstance(ag, ClZp):
            return type(self)( (self.m_val * ag.m_val)%type(self).m_NStt)
        else:
            return ag.__rmul__(self)
            #assert False

    def __rmul__(self, ag):
        return self.__mul__(ag)

    def __div__(self, ag):
        if isinstance(ag, (sf.ClFldTns, oc.ClOctonion)):
            return ag.__rdiv__(self)
        elif isinstance(ag, (int,long)):
            pass
        elif isinstance(ag,ClZp):
            ag = ag.m_val
        else:
            return ag.__rdiv(self)
            #assert False, "At __div__(.) in ClZp, Unexpected argment:"+str(ag)

        if (ag % type(self).m_NStt == 0):
            raise ZeroDivisionError("0 division at __div__(.)")

        #inAt = None
        #for i in range(1,N):
        #    if (ag * i)%N == 1:
        #        inAt = i
        #        break
        #assert not (inAt == None)
        #return ClZp( (self.m_val * inAt)%N)
        
        # x^(N-1) == 1 mod N;;Fermat's Little theorem;;
        return type(self)( self.m_val*(ag**(type(self).m_NStt-2))%type(self).m_NStt)

    def __truediv__(self, ag):
        return self.__div__(ag)

    def __rdiv__(self, ag):
        if isinstance(ag, (sf.ClFldTns, oc.ClOctonion)):
            return ag.__div__(self)
        else:
            return type(self)(ag)/self
        #return self.__div__(ag)

    # countermeasure for TypeError: "unsupported operand type(s) 
    # for /: 'int' and 'ClZp'Z=oc.Zp(5);1/Z(2)" 09.01.13
    def __rtruediv__(self, ag):
        return self.__rdiv__(ag)

    def __neg__(self):
        return type(self)(( type(self).m_NStt-self.m_val)%type(self).m_NStt )

    def __int__(self):
        return self.m_val

    # array needs __long__ 
    # e.g. ;;mt = kzrs(3,3,int); mt[0,1] = oc.Zp(3)(1);mt
    def __long__(self):
        return self.m_val

    def inv(self):
        if self.m_val % type(self).m_NStt == 0:
            raise ZeroDivisionError("0 divition at inv(.)")

        return type(self)(self.m_val**(type(self).m_NStt-2)%type(self).m_NStt)

    def __pow__(self, ag):
        if isinstance(ag,ClZp):
            ag = ag.m_val
        elif isinstance(ag, (int,long) ):
            pass
        else:
            assert False, ("At __pow__(.) in octn.ClZp, "
                            + "Unexpected argment:"+str(ag) )

        if ag == 0:
            return type(self)(1)
        elif ag > 0:
            rsAt = type(self)(self)
            for dummy in range(ag - 1):
                rsAt = rsAt * self
            return rsAt

        else:
            # ag < 0
            ag = -ag

            rsAt = self.inv()
            rightAt = type(self)(rsAt)
            for dummy in range(ag - 1):
                rsAt = rsAt * rightAt
            return rsAt

    def __eq__(self, ag):
        if isinstance(ag,int):
            return self.m_val == ag
        elif isinstance(ag, ClZp):
            return self.m_val == ag.m_val
        elif hasattr(ag, '__int__') and not isinstance(ag,type):
            return self.m_val == int(ag)
        else:
            #assert False, ("At __eq__(.) in octn.ClZp, "
            #                + "Unexpected argment:"+str(ag) )
            return False

    def __ne__(self, ag):
        return not(self.__eq__(ag))

    def __str__(self):
        return "Z"+ str(type(self).m_NStt) + "(" + self.__repr__() + ")"

    def __repr__(self):
        sizeAt = len(str(int(type(self).m_NStt)))
        strAt = str(self.m_val)
        if len(strAt) < sizeAt:
            strAt = " "*(sizeAt-len(strAt)) + strAt
        return strAt

    def __abs__(self):
        return self.m_val

    def __hash__(self):
        """' __hash__(..) is used by set container's methods'"""
        return self.m_val

    def __cmp__(self, ag):
        return cmp(self.m_val, int(ag))

class TyNickname(type):
    """' Meta class to generate a nicknamed classe whis is same as the original
    class except for it's name.

    usages:

    TyNickname.__tyBaseStt___ == tuple
    class Pt(object):
        __metaclass__ = TyNickname

    ↑ We strongly request to be Pt class instance should be picklable. So we cant
    use class factory function. We comprommize to use ugle static parameters to
    hand over a inheriting class and a string of nickname.

    __tyBaseStt___ static variables is a parameter to hand over a inherited class.
    __strNameStt___ static variables is a parameter to hand over a nickname string.
    '"""

    __tyBaseStt___  = None
    __strNameStt___ = None

    class ClStr(object):
        def __init__(self, sqAg):
            # this __init__ should be called right just after Cl.__nameStt___= ... 
            self.m_str = TyNickname.__strNameStt___

        def __str__(self):
            return self.m_str
        def __repr__(self):
            return self.m_str

    def __new__(cls, name, bases, dcAg):
        return type.__new__(cls, name, (TyNickname.ClStr, TyNickname.__tyBaseStt___), dcAg)


TyNickname.__tyBaseStt___=tuple
class Pt(object):
    __metaclass__ = TyNickname

def setNicknames(strAg, sqTplAg, tyAg=Pt):
    """' For one-liners, set Pt aliasing name shortly.
    fnPt("abcde",[(0,0),(0,1),(1,0), (2,0),(3,0)]); kfs(a,b,c), kfs(d,e)
    ===============================
    (kfs(a, b, c), kfs(d, e))

    fnPt("p0 p1 p2  p3 p4",[(0,0),(0,1),(1,0), (2,0),(3,0)]); kfs(p0,p1,p2), kfs(p3,p4)
    ===============================
    (kfs(p0, p1, p2), kfs(p3, p4))

    fnPt("p0 p1 p2  p3 p4",[(0,0),(0,1),(1,0), (2,0),(3,0)]); kfs(p0,p1,p2)+ kfs(p3,p4)
    ===============================
    kfs(p0, p1, p2, p3, p4)
    '"""
    import pysf.sfFnctns as sf

    assert isinstance(strAg, str)
    dctGlb=sf.__getDctGlobals()
    if sqTplAg.__len__() == strAg.__len__():
        for strAt, tplAt in zip(strAg, sqTplAg):
            assert strAt in "abcdefghijklmnopqrstrvwxyzABCDEFGHIJKLMNOPQRSTRVWXYZ"
            TyNickname.__strNameStt___ = strAt
            #dctGlb.update({strAt: tyAg(tplAt)})
            dctGlb[strAt] =  tyAg(tplAt)
    else:
        lsAt = strAg.split() 
        assert len(lsAt) == len(sqTplAg)
        for strAt, tplAt in zip(lsAt, sqTplAg):
            assert strAt[0] in "abcdefghijklmnopqrstrvwxyzABCDEFGHIJKLMNOPQRSTRVWXYZ"
            TyNickname.__strNameStt___ = strAt
            dctGlb.update({strAt: tyAg(tplAt)})

# Half way implementing Free Group 
from pysf.ptGrp import TyNickname
from pysf.ptGrp import setNicknames as fnPt
TyNickname.__tyBaseStt___ = str
def __sf__getDctGlobals___(strAg, clAg):
    sf.__getDctGlobals()[strAg] = clAg

class FreeGrp(object):
    __metaclass__ = TyNickname

    """' 大文字・小文字は互いに逆元の関係にあるとする
    単位元はどうする ← z=="":単位元`
    足し算はどうする    とりあえず考えない
    '"""
    def __mul__(self, ag):
        #print "debug ag:",ag, " strAt:",strAt
        if self == '':
            return ag
        elif ag == '':
            return self

        strAt = str(self)+str(ag)
        TyNickname.__tyBaseStt___ = str
        TyNickname.__strNameStt___ = strAt
        clAt = FreeGrp(strAt)
        __sf__getDctGlobals___(strAt, clAt)
        return clAt

    class ClRules(object):
        m_tpFnRules=(lambda x,y: '' if x == swapcase(y) else x+y,
                    )

if __name__ == "__main__":
    #import pysf.sfFnctns as sf
    import sfFnctns as sf
    #assert ( Cy([2,3]) * sf.arange(10) == [0,1,3,2,4,5,6,7,8,9] ).all()
    assert ( Cy([2,3]) * sf.arange(10) == [0,1,3,2,4,5,6,7,8,9] )
    assert Sb([3,0,2,1])*[0,1,2,3] == (3, 0, 2, 1)
    sb= Sb([2,0,3,1])
    assert (sb**3)*(0,1,2,3) == (1, 3, 0, 2)
    assert [sb**k *[0,1,2,3] for k in range(10)][1] ==  (2, 0, 3, 1)
    assert (Sb( [2, 0, 3, 1] )**-1 )((2, 0, 3, 1)) == (0, 1, 2, 3)
    assert (Sb( [2, 0, 3, 1] )**-1 )== (1, 3, 0, 2)
    assert (Sb( [2, 0, 3, 1] )**-2 )((2, 0, 3, 1)) == (1, 3, 0, 2)
    assert  Sb( [2, 0, 3, 1] )(['a','b','c','d'])== ['c', 'a', 'd', 'b']
    assert (Sb( [2, 0, 3, 1] )**-1 )(['a','b','c','d']) == ['b', 'd', 'a', 'c']
    assert  Sb( [2, 0, 3, 1] )(('a','b','c','d'))== ('c', 'a', 'd', 'b')
    assert Cy(1,2,4) * Cy(3,5) == (0, 2, 4, 5, 1, 3)
    assert Cy(3,5) * Cy(1,2,4) == (0, 2, 4, 5, 1, 3)
    assert Cy(0,1) * Cy(0,1,2,3,4,5,6,7) == (0, 2, 3, 4, 5, 6, 7, 1)
    assert (Sb(2, 0, 3, 1)**-1 )((2, 0, 3, 1)) == (0, 1, 2, 3)
    assert Sb(1,0) == (1,0,2,3)
    assert Sb(1,0,2,3) == (1,0)
    assert Sb(0,1) == Sb(0,1,2)
    #assert len( group(set([Cy(0,1), Cy(0,1,2,3)]) )) == 26
    assert len( group(set([Cy(0,1), Cy(0,1,2,3)]) )) == 24 # 11.10.06 group(..) 関数対策の結果
    assert len( group(set([Cy(0,1) *range(4), Cy(0,1,2,3)]) )) == 24

    assert Sb(0,3,1,2) == (0,3,1,2)
    assert Sb(0,3,1,2) == [0,3,1,2]
    assert Sb(0,3,1,2) == sf.krry([0,3,1,2])

    assert (Sb(1,2,0)(sf.np.array([1,2+1j,2-1j])) == [2+1j,2-1j,1]).all()
    assert Sb(0,1,3,2).sign == -1
    assert Sb(0,1,2,3).sign ==  1
    assert Sb(1,2,3,0).sign == -1
    assert Sb(1, 0, 3, 2).cyclic == 'Cy(0,1) Cy(2,3)'
    assert Cy(7) == Sb(0, 1, 2, 3, 4, 5, 6, 7)

    assert str( Sb(0, 3, 1, 2) ) == 'Sb(0,3,1,2)'
    assert str(kfs([Sb(0,1),Cy(2,3)])) == 'kfs([Sb(0,1), Sb(0,1,3,2)])'
    assert str([Sb(0,1),Cy(2,3)]) == '[Sb(0,1), Sb(0,1,3,2)]'
    assert len(group([Cy(0,1), Cy(1,2)])) == 6
    assert (Sb(range(10)))[:4] == (0,1,2,3)

    assert kfs((0,2,3)) * kfs([2,3,4]) == kfs([2, 3])
    assert kfs((0,2,3)) * set([2,3,4]) == kfs([2, 3])
    assert kfs((0,2,3)) *    ([2,3,4]) == kfs([2, 3])
    assert kfs((0,2,3)) *    ( 2,3,4 ) == kfs([2, 3])
    assert kfs((0,2,3)) * xrange(2,5 ) == kfs([2, 3])

    assert kfs((0,2,3)) + kfs([2,3,4]) == kfs([0, 2, 3, 4])
    assert kfs((0,2,3)) + set([2,3,4]) == kfs([0, 2, 3, 4])
    assert kfs((0,2,3)) +    ([2,3,4]) == kfs([0, 2, 3, 4])
    assert kfs((0,2,3)) +    ( 2,3,4 ) == kfs([0, 2, 3, 4])
    assert kfs((0,2,3)) + xrange(2,5 ) == kfs([0, 2, 3, 4])

    assert kfs([1,2,3,4,5])/kfs([2,3,4]) == kfs([1, 5])
    assert kfs([1,2,3,4,5])/set([2,3,4]) == kfs([1, 5])
    assert kfs([1,2,3,4,5])/[2,3,4]      == kfs([1, 5])
    assert kfs([1,2,3,4,5])/(2,3,4)      == kfs([1, 5])
    assert kfs([1,2,3,4,5])/xrange(2,5)  == kfs([1, 5])

    assert kfs([1,2,3,4,5])/2            == kfs([0, 1, 2])
    assert kfs([1,2,3,4,5])/2.0          == kfs([0.5, 1.0, 1.5, 2.0, 2.5])
    assert kfs([1,2,3])+[10]             == kfs([1, 2, 3, 10])
