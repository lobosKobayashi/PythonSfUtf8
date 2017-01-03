# -*- encoding: utf-8 -*-
"""'
english:
    PythonSf pysf/kre.py
    https://github.com/lobosKobayashi
    http://lobosKobayashi.github.com/
    
    Copyright 2016, Kenji Kobayashi
    All program codes in this file was designed by kVerifierLab Kenji Kobayashi

    I release souce codes in this file under the GPLv3
    with the exception of my commercial uses.

    2016y 12m 28d Kenji Kokbayashi

japanese:
    PythonSf pysf/kre.py
    https://github.com/lobosKobayashi
    http://lobosKobayashi.github.com/

    Copyright 2016, Kenji Kobayashi
    このファイルの全てのプログラム・コードは kVerifierLab 小林憲次が作成しました。
    
    作成者の小林本人に限っては商用利用を許すとの例外条件を追加して、
    このファイルのソースを GPLv3 で公開します。

    2016年 12月 28日 小林憲次
'"""

"""' Regular expression  wrapper to make easy using sre regular expression.
    krgl class has both regular expression pattern object and math object
    e.g.
        "abcdefg"/kre.krgl('[c-e]')%0 == 'cde'
'"""
# 08.01.09 
#import sre as se
#09.01.04
import re as se

kre = None

class __ClRglr(object):
    def __init__(self, pattern, flags=0):
        self.m_re = se.compile(pattern, flags=flags)
        self.m_strMatched = ""
        self.m_itr = None
        self.m_posStart = None
        self.m_posEnd = None

        self.m_gn = None

        global kre
        kre = self

    def search(self, strAg = None, posStart = 0, posEnd = None
                , blNext = True):
        """' regular expression search
             Return matched string.

             If you need mached position. then read kre.m_posStart

             If blNext == True and strAg == None:default
           then execute next search cotinuing before search
        '"""
        global kre
        # assign kre as the last operated instance
        kre = self
        if (strAg == None) and (blNext == True):
            if self.m_gn == None:
                raise RuntimeError(
                    "You request next search without first search")
        else:
            self.m_gn = self.finditer(strAg[posStart:posEnd])

        try:
            self.m_gn.next()
        except StopIteration:
            pass

        return self.m_strMatched

    def finditer(self, strAg, blUseZeroLengthMatch = False):
        """' generator to find matching string for this regular
            expression. Don't yield for 0 length match
        '"""
        global kre
        kre = self
        self.m_strMatched = ""
        self.m_itr = None
        self.m_posStart = None
        self.m_posEnd = None
        for itr in self.m_re.finditer(strAg):
            start, end = itr.span()
            # ignore zero length match
            if (start == end) and (blUseZeroLengthMatch == False):
                continue
            else:
                self.m_posStart = start
                self.m_posEnd = end
                self.m_strMatched = itr.group(0)
                self.m_itr = itr
                yield self

    def search0(self, strAg = None, posStart = 0, posEnd = None
                , blNext = False):
        """' 0 length regular expression search
             Return matched string.

             If you need mached position. then read kre.m_posStart

             If blNext == True and strAg == None:default
           then execute next search cotinuing before search
        '"""
        global kre
        kre = self
        if (strAg == None) and (blNext == True):
            if self.m_gn == None:
                raise RuntimeError(
                    "You request next search without first search")
        else:
            self.m_gn = self.finditer0(strAg[posStart:posEnd])

        try:
            self.m_gn.next()
        except StopIteration:
            pass

        return self.m_strMatched

    def finditer0(self, strAg):
        """' generator to find matching string for this regular
            expression. Can yield for 0 length match
        '"""
        global kre
        kre = self
        self.m_strMatched = ""
        self.m_itr = None
        self.m_posStart = None
        self.m_posEnd = None
        for itr in self.m_re.finditer(strAg):
            start, end = itr.span()
            self.m_posStart = start
            self.m_posEnd = end
            self.m_strMatched = itr.group(0)
            self.m_itr = itr
            yield self

    def __rdiv__(self, strAg):     # strAt/reAt    return mathed string
        self.search(strAg)
        return self

    # __rtruediv__ is needed when from __future__ import division is effective
    def __rtruediv__(self, strAg):
        self.search(strAg)
        return self

    def __mod__(self, ag):    # return group string
        """' return grouped sub string.
        '"""
        if self.m_itr == None:
            # If there is no matched string then return "" adn avoid exception
            return ""

        if isinstance(ag, int):
            # numbered sub gourp, regular expression: ...(..)...
            return self.m_itr.group(ag)
        elif isinstance(ag, str):
            # ASCII named gourp (?P<...>regularExpression)
            return self.m_itr.group(ag)
        elif isinstance(ag, unicode):
            # unicode named gourp (?P<...>regularExpression)
            return self.m_itr.group(ag)
        elif ag == ():
            # corresponding to sre.findall(..)
            tplAt = ()
            try:
                k = 0
                while(True):
                    tplAt += (self.m_itr.group(k),)
                    k += 1
            except IndexError:
                return tplAt
        else:
            raise TypeError(
                    "You set abnormal parameter:" + str(ag)+" at __mod__(..)" )

krgl = __ClRglr   # alias name

if __name__ == "__main__":
    assert __ClRglr("abc").search("XabcY") == "abc"
    strAt = "XabcY"/__ClRglr("abc")%0
    assert strAt == "abc"
    assert "XabbbcY"/__ClRglr("a(b*)c")%0 == "abbbc"
    assert kre%1 == "bbb"
    assert "XabbbcY"/__ClRglr("a(b*)c") %1 == "bbb"
    assert "XaxxxcY"/__ClRglr("a(b*)c") %0 == ""
    assert krgl("a(b*)c").search("XaxxxcY") == ""
    assert "AaxxxybbB"/krgl("a(x*y)b")%0 == "axxxyb"
    assert "AaxxxybbB"/krgl("a(x*y)b")%1 == "xxxy"
    assert "AaxxxybbB"/krgl("a(?P<test>x*y)b")%("test") == "xxxy"

    # ignore upper/lowercase
    assert 'abcdefg'/krgl('CD', flags=se.IGNORECASE)%0 == "cd"

    # tests groups() with %(): cation! %() always containns group(0)
    assert 'abccXbbcbXbcbcX'/krgl('a(b*c*)')%() == ('abcc', 'bcc')
    
    # test search
    assert "abcdefg"/krgl("[bc]+")%0 == "bc"
    assert krgl("[bc]+").search("abcdefg") == "bc"
    assert kre.m_posStart == 1

    assert krgl("[bc]+").search("abcdefg",posStart = 1) == "bc"
    assert kre.m_posStart == 0
    # posStart arg is in second
    assert krgl("[bc]+").search("abcdefg", 1) == "bc"

    ## test extreme case
    #   0 length match is omitted
    assert "abcdefg"/krgl("b?")%0 == "b"
    #sre.py cuase 0 length match as below
    #import sre; rgAt = sre.compile('b?'); print rgAt.findall('abcd')
    #['', 'b', '', '', '']


    # test finditer
    strReNumber = r"(\d*[\.]?\d*(e[\+\-]?\d+)?j?)"
    assert [x%0 for x in 
        krgl(strReNumber).finditer(r"1.234 1e6 1e+3 1.3e-3 2.e3  x 1+2j")]\
        == ['1.234', '1e6', '1e+3', '1.3e-3', '2.e3', '1', '2j']

    # test unicode string serced by ASCII reglar expression
    assert u"ab3.14XY"/krgl(r"\d\.?\d+")%0 == u"3.14"
    assert u"ab3.14XY"/krgl(r"\d\.?\d+")%0 ==  "3.14"
    # test ASCII string serced by unicode reglar expression
    assert "ab3.14XY"/krgl(ur"\d\.?\d+")%0 == u"3.14"
    assert "ab3.14XY"/krgl(ur"\d\.?\d+")%0 ==  "3.14"
    
    # test continuing search
    assert u"ab3.14XY123ef45"/krgl(r"\d+")%0 == u"3"
    assert kre.search() == u"14"
    assert kre.search() == u"123"
    assert kre.search() == u"45"
