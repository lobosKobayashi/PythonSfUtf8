# -*- encoding: utf-8 -*-
"""'
english:
    PythonSf pysf/kcommon.py
    https://github.com/lobosKobayashi
    http://lobosKobayashi.github.com/
    
    Copyright 2016, Kenji Kobayashi
    All program codes in this file was designed by kVerifierLab Kenji Kobayashi

    I release souce codes in this file under the GPLv3
    with the exception of my commercial uses.

    2016y 12m 28d Kenji Kokbayashi

japanese:
    PythonSf pysf/kcommon.py
    https://github.com/lobosKobayashi
    http://lobosKobayashi.github.com/

    Copyright 2016, Kenji Kobayashi
    このファイルの全てのプログラム・コードは kVerifierLab 小林憲次が作成しました。
    
    作成者の小林本人に限っては商用利用を許すとの例外条件を追加して、
    このファイルのソースを GPLv3 で公開します。

    2016年 12月 28日 小林憲次
'"""

from defines import *    # kcommon.varNameInDefine.py でアクセスさせるため import * を使います



# -------------------- general utility class begin --------------------------------------
def getMax(seqAg, maxAg=0):
    """ 任意 sequence の最大値を求めます。
        maxAg 引数は、行列などのような多重シーケンスの max を求め易くするために設けました
    """
    for elm in seqAg:
        if elm > maxAg:
            maxAg = elm
    return maxAg

def getMin(seqAg, minAg=0):
    """ 任意 sequence の最小値を求めます。
        minAg 引数は、行列などのような多重シーケンスの min を求め易くするために設けました
    """
    for elm in seqAg:
        if elm < minAg:
            minAg = elm
    return minAg

class ClPair:
    """ sort 可能な Pair 構造体
        C++/STL の pair<T1,T2> のようなものが欲しく作りました。left/right のペアで管理する
    データ構造です。sort 動作をさせるときは　left 側のインスタンスは ">" と "<" 演算が可能
    な要素でなければなりません。
    
        三つ以上の要素の構造体を扱いたいときは、このクラスをテンペレートして別にクラスを書
    き下してください。なまじ ClPair を継承すべきではありません。関数プログラミングの技法を
    駆使すれば、複数メンバー向けのクラスを記述できるかもしれません。でも私にはそんな能力も
    ありません。またそこまでする必要もないと考えます。
    """
    def __init__(self, leftAg, rightAg):
        self.left = leftAg
        self.right = rightAg

    def __repr__(self):
        return "(left:"+ str(self.left) + " :: right:" + str(self.right)+')'

    def __cmp__(self, clPairAg):
        if (self.left < clPairAg.left):
            return -1
        elif (self.left > clPairAg.left):
            return 1
        else:
            return 0

class ClError(str):
    def __init__(self, strAg=None):
        str.__init__(strAg)

class kAssertionError:
    def __init__(self, strAg="kAssertionError"):
        self.m_str = strAg
    def __str__(self):
        return self.m_str

def kAssert(blAg, strErrorMessageAg=""):
    """ 戻り値：なし
        たんなる assert では -O オプションを使って最適化したときなくなってしまう。でも
    それではユーザーに情報をエラー情報を与える意味で assert を使いたい時困る。この対策
    として、K.assert(True/False, strErrorMessageAg) を使う。
    """
    if blAg == False:
        raise kAssertionError(strErrorMessageAg)
    else:
        return

class ClEn:
    def __init__(self, inAg=None):
        self.element=inAg
    def __call__(self, inAg):
        self.element = inAg
    def __eq__(self,inAg):
        return self.element == inAg
    def __ne__(self,inAg):
        return self.element != inAg
    def __int__(self):
        return self.element
    def __str__(self):
        return str(self.element)
    

""" usage and test
class EnWeek(ClEn):
    Sun,Mon,Tus,Wed,Thu,Fri,Sat = range(7)
    Sunday,Monday,Tuseday,Wednesday,Thursday,Friday,Saturday = range(7)

enAt = EnWeek()
enAt(EnWeek.Mon)
print enAt == EnWeek.Mon
"""

class ClEnum:
    """ClEnum(strEnumDeclareration) により C 言語での  enum instance を生成します。
    example: enAt = ClEnum('Sun,Mon,Tus,Wed,Thu,Fri,Sat, \
                            Sunday=1,Monday, Tuseday, Wednesday, Thursday, Friday, Saturday')

            enAt('Sun') # enAt = 'Sun' と記述できないのが悔しい。Python の限界
            if enAt == 'Sunday':.....
            inAt = int(enAt)
    self.lstTpl_in_lstStr = strAg : std::list<pair<int, lst<str> > によって enum データ型を管理する
    """
    def __init__(self, arg):
        if isinstance( arg, ClEnum):
            self.strDeclaration = arg.strDeclaration
            self.strAssignedByFunctionalObject = arg.strAssignedByFunctionalObject
            self.lstTpl_in_lstStr = arg.lstTpl_in_lstStr
        elif isinstance( arg, str):
            self.strDeclaration = arg
            self.strAssignedByFunctionalObject = ''
            self.lstTpl_in_lstStr = []

            inEnumFirstValue = 0;
            lstStrAt = [x.strip() for x in arg.split(',')]
            for i, strAt in enumerate(lstStrAt):
                if strAt.find('=') != -1:
                    lstStrAt2 = [x.strip() for x in strAt.split('=')]
                    kAssert(len(lstStrAt2)==2, "Abnormal enum = term:%s" % strAt)
                    inEnumFirstValue = int(lstStrAt2[1])
                    self.lstTpl_in_lstStr.append( (inEnumFirstValue,[]) )
                    strAt=lstStrAt2[0]
                elif i==0:
                    self.lstTpl_in_lstStr.append( (0,[]) )
    
                self.lstTpl_in_lstStr[-1][1].append(strAt)
    
            self.strAssignedByFunctionalObject = self.lstTpl_in_lstStr[0][1][0]
        else:
            assert False, " Abnormal ElEnum __init__  argment:"+ str(arg)
    def __call__(self, strAg):
        for firstValue, lstAt in self.lstTpl_in_lstStr:
            if strAg in lstAt:
                self.strAssignedByFunctionalObject = strAg
                return self
        kAssert(False,"We can't find \"%s\" in declared string list at ClEnum.strDeclaration"% strAg)

    def __eq__(self,strAg):
        if isinstance(strAg, ClEnum):
            return self.__convert2int(self.strAssignedByFunctionalObject)\
                == self.__convert2int(strAg.strAssignedByFunctionalObject)

        if isinstance(strAg, int):
            return self.__convert2int(self.strAssignedByFunctionalObject)\
                == strAg
            
        kAssert(type(strAg) is str,"Abnormal argment:%s at == operator"% strAg\
                + " You must set string argement for ClEnum instace == arigment")
        return self.__convert2int(self.strAssignedByFunctionalObject) == self.__convert2int(strAg)

    def __ne__(self,strAg):
        kAssert(type(strAg) is str,"Abnormal argment:%s at != operator"% strAg\
                + " You must set string argement for ClEnum instace == arigment")
        return self.__convert2int(self.strAssignedByFunctionalObject) != self.__convert2int(strAg)

    def __convert2int(self, strAg):
        """
            ClEnum instance が保存する enum リストから strAg に対応する値をとりだす。
        strAg に対応する文字列が ClEnum instance を保持していないときは assert error にする
        """
        for firstValue, lstStrAt in self.lstTpl_in_lstStr:
            if strAg in lstStrAt:
                for i, strAt in enumerate(lstStrAt):
                    if strAg == strAt:
                        return firstValue + i
        kAssert(False,"We can't find \"%s\" in declared string list at ClEnum.__int__"% strAg)

    def __int__(self):
        return self.__convert2int(self.strAssignedByFunctionalObject)
    def __str__(self):
        return self.strAssignedByFunctionalObject +": " + str(self.lstTpl_in_lstStr)

def sort(lstAg):
    """戻り値 lstAt の sort されたもの
       lstAt.sort() の戻り値は None であり不便なため設ける
    """
    lstAt = lstAg
    lstAt.sort()
    return lstAt
# -------------------- general utility class end --------------------------------------

# -------------------- iterator utility begin --------------------------------------
"""
list.reverse() がある
class ClReverse:
    "" Iterator for looping over a sequence backwards
    ・http://www.python.jp/doc/release/tut/node11.html に機能追加
    ・instanse[...] と [index] でアクセスできるコンテナのみが対象です。hash container 
      には使えません
    ・def __init__(self, data, sztStartAg=len(data) ) とすることも考えましたが
      for x in ClReverse(data[sztStart:]) と記述すれば良いことに気づき止めました
    ""
    def __init__(self, data ):
        self.data = data
        self.index = len(data)
    def __iter__(self):
        return self
    def next(self):
        if self.index == 0:
            raise StopIteration     # StopIteration を投げる事で iterate を終了します
        self.index -= 1
#        print self.index   # to debug
        return self.data[self.index]
"""

# -------------------- iterator utility end --------------------------------------

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
def find(lineAg, strFoundAg, sztStartAg=0):
    """ 戻り値: 
        python の str.find は見つからないとき -1 を返します。これを嫌って npos = 2**30 を
    返す find() 関数を追加します。find_not_of と統一も取れます
    """
    sztAt = lineAg.find(strFoundAg,sztStartAg)
    if sztAt == -1:
        return npos
    else:
        return sztAt

def rfind(lineAg, strFoundAg, sztStartAg=0):
    """ 戻り値: 
        python の str.rfind は見つからないとき -1 を返します。これを嫌って npos = 2**30 を
    返す rfind() 関数を追加します。rfind_not_of と統一も取れます
    """
    sztAt = lineAg.rfind(strFoundAg,sztStartAg)
    if sztAt == -1:
        return npos
    else:
        return sztAt

# 05.10.16 OK
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
        if find_first_not_of(strLineAg,"...") == kcommon.npos : ...
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

def searchPairCh( strAg, strBeginEndAg="()",sztStartAg=0,sztEndAg=npos ):
    """ search 関数の戻り値 (sztStart, sztEnd) 開始記号の位置と終了記号の位置の tuple
    ・'(', ')' などの一組の文字の始まりと終わりをの位置見つけます。
    ・ペアが見つからないときは kAssert エラーにする
    ・クラスにするのは 開始記号／終了記号の位置の解析を何度も続けて行うときのためです。
    // ..[1...[2...]3  ]4   の文字列で chBeginAg=='[', chEndAg==']' とすると
    // [1 に対して ]4 を探し出す。括弧の対応を見つけることができる。
    ・同じ文字のペアのときはネスティングを数えない
    
    """
    assert len(strBeginEndAg)==2, "You must set 2 charactere in strBeginEndAg"
    wdCountBackSlashAt = 0
    wdCountAt = 0
    wdStartAt = 0
    for i, chAt in enumerate(strAg[sztStartAg: sztEndAg]):
        if ( strBeginEndAg[0]==strBeginEndAg[1] and chAt == strBeginEndAg[0]):
            if ( wdCountAt == 0):
                wdStartAt = i + sztStartAg
                wdCountAt = 1
                continue
            else:
                return (wdStartAt, i + sztStartAg)
        
        elif ( strBeginEndAg[0]!=strBeginEndAg[1] and chAt == strBeginEndAg[0]):
            if ( wdCountBackSlashAt % 2 == 0):
                if ( wdCountAt == 0):
                    wdStartAt = i + sztStartAg
                if strBeginEndAg[0] !=  strBeginEndAg[1]:
                    wdCountAt += 1
                
            sztCountBackSlashAt=0
            continue
        elif ( strBeginEndAg[0]!=strBeginEndAg[1] and chAt == strBeginEndAg[1] ):
            if ( wdCountBackSlashAt %2 == 1 ):
                # m_chEnd 文字の直前に奇数個の \ 文字が有る。
                continue
            elif (wdCountAt < 1 ):
                assert False, "Too many End Character:%s" % strBeginEndAg[1]

            elif ( wdCountAt == 1):
                return (wdStartAt, i + sztStartAg)
            
            else:
                if strBeginEndAg[0] !=  strBeginEndAg[1]:
                    wdCountAt -=1;
                continue;
        else:
            if (chAt == '\\' ):
                wdCountBackslashAt+=1;
            else:
                wdCountBackslashAt=0;
            continue;

    if wdCountAt == 0:
        return (npos,npos)
    else:
        return (wdStartAt, npos)

class ClPairedString:
# 05.10.15 OK
    """ search 関数の戻り値 (sztStart, sztEnd) 開始記号の位置と終了記号の位置の tuple
    ・ペアが見つからないときは kAssert エラーにする
       '(', ')' などの一組の文字の始まりと終わりをの位置見つけます。
    ・クラスにするのは 開始記号／終了記号の位置の解析を何度も続けて行うときのためです。
    // ..[1...[2...]3  ]4   の文字列で chBeginAg=='[', chEndAg==']' とすると
    // [1 に対して ]4 を探し出す。括弧の対応を見つけることができる。
    // このようにした弊害として ..."..."... のように同じ文字のペアを見つけ
    // られない。...a..a...b と a で始まり b で終わり、ネスティングの検出を
    // しないときも ClSimplePaired を使う。
    """

    def __init__(self, chBeginAg='(', chEndAg=')' ):
        self.m_wdCount=0
        self.m_chBegin=chBeginAg
        self.m_chEnd=chEndAg
        self.wdStart=0
        self.wdCount=0
        self.m_wdCountBackSlash=0
        assert chBeginAg != chEndAg, (
                "Begin Character & End Character are same %s" % chBeginAg)

    def search(self, strAg, wdStartAg=0,wdEndAg=npos ):
        for i, chAt in enumerate(strAg[wdStartAg: wdEndAg]):
            if ( chAt == self.m_chBegin):
                if ( self.m_wdCountBackSlash % 2 == 0):
                    if ( self.m_wdCount == 0):
                        self.m_wdStart = i + wdStartAg
                    self.m_wdCount+= 1
                self.m_wdCountBackSlash=0
                continue
            elif ( chAt == self.m_chEnd ):
                if ( self.m_wdCountBackSlash %2 == 1 ):
                    # m_chEnd 文字の直前に奇数個の \ 文字が有る。
                    continue
                elif (self.m_wdCount < 1 ):
                    assert False, ("Too many End Character:%s" % self.m_chEnd)   #continue # goto Error
                elif ( self.m_wdCount == 1):
                    return (self.m_wdStart, i + wdStartAg)
                
                else:
                    self.m_wdCount-=1;
                    continue;
            else:
                if (chAt == '\\' ):
                    self.m_wdCountBackslash+=1;
                else:
                    m_inCountBackslash=0;
                continue;
        kAssert(False,"We can't find %s %s matched pair"% ( self.m_chBegin, self.m_chEnd) )

# -------------------- 文字列処理系 utility end --------------------------------------

# pico sec を最小とする時間
# 文字列にするとき下の桁の 0 の具合で pS,nS .... TS まで時間の単位を変更する
class ClTime:
    class EnUnit(ClEn):
        # kVerifier にあわせて k_fS は使っていません
        k_fS,   k_pS, k_nS,k_uS,    k_mS, k_S, k_KS,   k_MS,k_GS,k_TS = range(10)

    def __init__(self, fstAg=0L, sndAg = None):    # inAg に float も入れられる
        if isinstance(fstAg, int) or isinstance(fstAg, long):
            if isinstance(sndAg, str):    
                if sndAg == 'k_pS':
                    self.m_ln = fstAg
                elif sndAg == 'k_nS':
                    self.m_ln = fstAg * 10**3
                elif sndAg == 'k_uS':
                    self.m_ln = fstAg * 10**6
                elif sndAg == 'k_mS':
                    self.m_ln = fstAg * 10**9
                elif sndAg == 'k_S':
                    self.m_ln = fstAg * 10**12
                elif sndAg == 'k_KS':
                    self.m_ln = fstAg * 10**15
                elif sndAg == 'k_MS':
                    self.m_ln = fstAg * 10**18
                elif sndAg == 'k_GS':
                    self.m_ln = fstAg * 10**21
                elif sndAg == 'k_TS':
                    self.m_ln = fstAg * 10**24
                else:
                    assert False, "Abnormal ClTime constructor uint string:"+str(sndAg)
            elif (sndAg == None):    
                self.m_ln = long(fstAg)
            else:
                assert False, "Abnormal ClTime constructor second parameter:"+str(sndAg)
        elif isinstance(fstAg, float):
            self.m_dbObserve = fstAg

            import math
            lngAt = 0L
            dbAt = fstAg - math.fmod(fstAg,1e+6);
            lngAt += int( dbAt*10**(+18-6) ) # dbAt は 10**6 以上の桁のみの数

            fstAg -= dbAt;
            dbAt = fstAg - math.fmod(fstAg,1e-3);
            lngAt += int( dbAt*10**(3+9) )   # dbAt は 10**-3 以上の桁のみの数

            fstAg -= dbAt;                   # inAt は 10**-3 以下の数
            lngAt += int(fstAg*10**12 )       # 
            self.m_ln = lngAt
            
            #print "debug ClTime :", self.m_ln
        elif isinstance(fstAg, ClTime):
            self.m_ln = fstAg.m_ln
        elif (sndAg == None) and isinstance(fstAg, str):
            """ This code is used for time strings and others at the far left 
                in action scripts.
                ----------------- Japanese ----------------------------------
                action scripts の左端に書かれる +10mS などの時刻処理に使います
            """
            fstAg = fstAg.strip()
            assert fstAg[-1] == 'S', "Abnormal ClTime constructor uint string:"+str(fstAg)
            if fstAg[-2] in "pumKMGT":
                strUnitAt = fstAg[-2:]
                strIntAt = fstAg[0:-2]
            else:
                strUnitAt = "S"
                strIntAt = fstAg[0:-1]
            
            strIntAt = strIntAt.strip()
            if strUnitAt == 'pS':
                self.m_ln = long(strIntAt)
            elif strUnitAt == 'nS':
                self.m_ln = long(strIntAt) * 10**3
            elif strUnitAt == 'uS':
                self.m_ln = long(strIntAt) * 10**6
            elif strUnitAt == 'mS':
                self.m_ln = long(strIntAt) * 10**9
            elif strUnitAt == 'S':
                self.m_ln = long(strIntAt) * 10**12
            elif strUnitAt == 'KS':
                self.m_ln = long(strIntAt) * 10**15
            elif strUnitAt == 'MS':
                self.m_ln = long(strIntAt) * 10**18
            elif strUnitAt == 'GS':
                self.m_ln = long(strIntAt) * 10**21
            elif strUnitAt == 'TS':
                self.m_ln = long(strIntAt) * 10**24
            else:
                assert False, "Abnormal ClTime constructor uint string:"+str(fstAg)
        else:
            assert False, str(fstAg) + ": is not integer or float number."

        self.setDouble()

    def SetNextTickTime(self, crTmAg):  # const TyTime& crTmAg
        self.m_ln = crTmAg.m_ln
        self.setDouble()

    def GetTickTime(self):  #return TyTime, const
        return ClTime(self.m_ln)

    def __long__(self):
        return self.m_ln

    def setDouble(self):    # return void
        self.m_dbObserve = 0.0
        # --greater than 1---- less than 1-
        # 999999999,999999,  999 999999999
        inAt    = self.m_ln / 1000000000000   
        inModAt = self.m_ln % 1000000000000
        if ( inAt != 0):
            self.m_dbObserve += inAt

        self.m_dbObserve += float(inModAt)/1000000000000
        

    def GetDouble(self):    # return float
        return self.m_dbObserve;

    def __str__(self):
        #print '__str__ debug:', long(self)
        #print 'debug:', long.__str__(self % 1000)
        # k_fS は long int 部分に割り当ててないので、pS から始まります。
        if (self.m_ln % 1000 != 0):
            return long.__str__(long(self.m_ln))+"pS"
        elif (self.m_ln % 1000**2 != 0):
            # 1000 の次は 1000**2 == 1000000 です
            return long.__str__(long(self.m_ln/1000))+"nS"
        elif (self.m_ln % 1000**3 != 0):
            return long.__str__(long(self.m_ln/1000**2))+"uS"
        elif (self.m_ln % 1000**4 != 0):
            return long.__str__(long(self.m_ln/1000**3))+"mS"
        elif (self.m_ln % 1000**5 != 0):
            return long.__str__(long(self.m_ln/1000**4))+"S"
        elif (self.m_ln % 1000**6 != 0):
            return long.__str__(long(self.m_ln/1000**5))+"KS"
        elif (self.m_ln % 1000**7 != 0):
            return long.__str__(long(self.m_ln/1000**6))+"GS"
        else:
            return long.__str__(long(self.m_ln/1000**7))+"TS"

    def __add__(self, objAg):
        lnAt = self.m_ln
        if isinstance(objAg, ClTime):
            lnAt += objAg.m_ln
        elif isinstance(objAg, int) or isinstance(objAg, long):
            lnAt += objAg
        elif isinstance(objAg, float):
            lnAt += ClTime(objAg).m_ln
        clAt = ClTime(lnAt)
        clAt.setDouble()
        return clAt

    def __eq__(self, objAg):
        if isinstance(objAg, ClTime):
            return self.m_ln == objAg.m_ln
        elif isinstance(objAg, int) or isinstance(objAg, long):
            return self.m_ln == objAg
        elif isinstance(objAg, float):
            return self.GetDouble == objAg
        else:
            assert False, "Abnorma argment at ClTime:__eq__:" + str(objAg)

    def __gt__(self, objAg):
        if isinstance(objAg, ClTime):
            return self.m_ln > objAg.m_ln
        elif isinstance(objAg, int) or isinstance(objAg, long):
            return self.m_ln > objAg
        elif isinstance(objAg, float):
            return self.GetDouble > objAg
        else:
            assert False, "Abnorma argment at ClTime:__gt__:" + str(objAg)

    def __lt__(self, objAg):
        if isinstance(objAg, ClTime):
            return self.m_ln < objAg.m_ln
        elif isinstance(objAg, int) or isinstance(objAg, long):
            return self.m_ln < objAg
        elif isinstance(objAg, float):
            return self.GetDouble < objAg
        else:
            assert False, "Abnorma argment at ClTime:__lt__:" + str(objAg)

    def __le__(self, objAg):
        if isinstance(objAg, ClTime):
            return self.m_ln <= objAg.m_ln
        elif isinstance(objAg, int) or isinstance(objAg, long):
            return self.m_ln <= objAg
        elif isinstance(objAg, float):
            return self.GetDouble <= objAg
        else:
            assert False, "Abnorma argment at ClTime:__le__:" + str(objAg)

# 戻り値は enAg の種類に応じた浮動小数点値
def ConvertEnmTimeToDouble(enAg):   #kc.ClTime.EnUnit タイプの引数
    if (enAg == ClTime.EnUnit.k_pS ):
        return 1.0e-12
    elif (enAg == ClTime.EnUnit.k_nS ):
        return 1.0e-9
    elif (enAg == ClTime.EnUnit.k_uS ):
        return 1.0e-6
    elif (enAg == ClTime.EnUnit.k_mS ):
        return 1.0e-3
    elif (enAg == ClTime.EnUnit.k_S ):
        return 1.0
    elif (enAg == ClTime.EnUnit.k_KS ):
        return 1.0e3
    elif (enAg == ClTime.EnUnit.k_MS ):
        return 1.0e6
    elif (enAg == ClTime.EnUnit.k_GS ):
        return 1.0e9
    elif (enAg == ClTime.EnUnit.k_TS ):
        return 1.0e12;
    else:
        assert False, "Abnormal enum at ConvertEnmTimeToDouble(.)"

""" ConvertEnmTimeToDouble() の test
print ConvertEnmTimeToDouble(ClTime.EnUnit.k_pS)
print ConvertEnmTimeToDouble(ClTime.EnUnit.k_nS)
print ConvertEnmTimeToDouble(ClTime.EnUnit.k_uS)
print ConvertEnmTimeToDouble(ClTime.EnUnit.k_mS)
print ConvertEnmTimeToDouble(ClTime.EnUnit.k_S)
print ConvertEnmTimeToDouble(ClTime.EnUnit.k_KS)
print ConvertEnmTimeToDouble(ClTime.EnUnit.k_MS)
print ConvertEnmTimeToDouble(ClTime.EnUnit.k_GS)
print ConvertEnmTimeToDouble(ClTime.EnUnit.k_TS)
"""

def ConvertEnmTimeTopCh(enAg): # kc.ClTime.EnUnit タイプの引数
    if (enAg == ClTime.EnUnit.k_pS ):
        return "pS"
    elif (enAg == ClTime.EnUnit.k_nS ):
        return "nS"
    elif (enAg == ClTime.EnUnit.k_uS ):
        return "uS"
    elif (enAg == ClTime.EnUnit.k_mS ):
        return "mS"
    elif (enAg == ClTime.EnUnit.k_S ):
        return "S"
    elif (enAg == ClTime.EnUnit.k_KS ):
        return "KS"
    elif (enAg == ClTime.EnUnit.k_MS ):
        return "MS"
    elif (enAg == ClTime.EnUnit.k_GS ):
        return "GS"
    elif (enAg == ClTime.EnUnit.k_TS ):
        return "TS"
    else:
        assert False, "Abnormal enum at ConvertEnmTimeToDouble(.)"

""" ConvertEnmTimeTopCh() の test
print ConvertEnmTimeTopCh(ClTime.EnUnit.k_pS)
print ConvertEnmTimeTopCh(ClTime.EnUnit.k_nS)
print ConvertEnmTimeTopCh(ClTime.EnUnit.k_uS)
print ConvertEnmTimeTopCh(ClTime.EnUnit.k_mS)
print ConvertEnmTimeTopCh(ClTime.EnUnit.k_S)
print ConvertEnmTimeTopCh(ClTime.EnUnit.k_KS)
print ConvertEnmTimeTopCh(ClTime.EnUnit.k_MS)
print ConvertEnmTimeTopCh(ClTime.EnUnit.k_GS)
print ConvertEnmTimeTopCh(ClTime.EnUnit.k_TS)
"""


#06.08.31 python で eof() を使えるようにクラスを設ける
# read only のみを対象とします。
# 注意  open() is an alias for file().

class ClReadFile(file):
    def __init__(self, fileNameAg):
        self.m_blEOF = False
        file.__init__(self, fileNameAg, 'r')

    def readline(self): # return line string
        strAt = file.readline(self)
        if not strAt:
            self.m_blEOF = True
        return strAt

    def eof(self):
        return self.m_blEOF

""" ClReadFile class のテスト
fhAt = ClReadFile('test.txt')
strAt = fhAt.readline()
print strAt
print fhAt.eof()

strAt = fhAt.readline()
print strAt
print fhAt.eof()

strAt = fhAt.readline()
print strAt
print fhAt.eof()

strAt = fhAt.readline()
print strAt
print fhAt.eof()

strAt = fhAt.readline()
print strAt
print fhAt.eof()

strAt = fhAt.readline()
print strAt
print fhAt.eof()
"""

cInMaxGlb = 2147483647
ctmMaxGlb = ClTime(999999999999999999999999999) # kVerifier が扱える最大時刻


# multiple range generator
def mrng(*args):
    head, tail = args[0], args[1:]
    if type(head) in [int, long, float]:
        head = range(head)
    elif isinstance(head, tuple):
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

# 等差数列 を start, size, stride 引数で生成する
# arithmetic sequence is generated with argment start, size, stride
def arSqnc(startOrSizeAg, sizeAg = None, strideAg=1):
    if sizeAg == None:
        return range(startOrSizeAg)
    else:
        tplAt = ()
        for i in range(sizeAg):
            tplAt += (startOrSizeAg + i*strideAg,)
        return tplAt

# 多次元の等差数列を生成する
# generate multiple dimention arithmetic sequence
def masq(*args):
    head, tail = args[0], args[1:]
    if type(head) in [int, long, float]:
        head=range(head)
    elif isinstance(head, tuple) or isinstance(head, list):
        head=arSqnc(*head)
    else:
        kAssert(False, "unexpected argment" + str(args) )

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

# kcommon.dis() を呼び出したモジュール、クラスを逆アッセンブルします
# dis-assemble the module or class which call kcommon.dis(.)
def dis():
    import dis;import inspect as ins;dis.dis(ins.stack()[1][0].f_code)

#07.08.26 modified from;;http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/65207
# Put in const.py...:
class ClConst(object):
    class ConstError(TypeError): pass
    def __setattr__(self,name,value):
        if self.__dict__.has_key(name):
            raise self.ConstError, "Can't rebind const(%s)"%name
        self.__dict__[name]=value

# use const.some = 3    # 2 回目の代入でエラー
const = ClConst()
