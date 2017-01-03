# -*- encoding: utf-8 -*-
from __future__ import division
"""'
english:
    PythonSf pysfOp/vrfyPySfOp.py
    https://github.com/lobosKobayashi
    http://lobosKobayashi.github.com/
    
    Copyright 2016, Kenji Kobayashi
    All program codes in this file was designed by kVerifierLab Kenji Kobayashi

    I release souce codes in this file under the GPLv3
    with the exception of my commercial uses.

    2016y 12m 28d Kenji Kokbayashi

japanese:
    PythonSf pysfOp/vrfyPySfOp.py
    https://github.com/lobosKobayashi
    http://lobosKobayashi.github.com/

    Copyright 2016, Kenji Kobayashi
    このファイルの全てのプログラム・コードは kVerifierLab 小林憲次が作成しました。
    
    作成者の小林本人に限っては商用利用を許すとの例外条件を追加して、
    このファイルのソースを GPLv3 で公開します。

    2016年 12月 28日 小林憲次
'"""

import sfPPrcssrOp as sP
import sys
# We needs the global kv module name. But we must import after file check
kv = None


blStt       = False     #None  # bool
inStt       = 0         #None  # int, log
scalarStt   = 0+0j      #None  # float, complex
strStt      = ""
strExceptionStt, strPythonAppErrorStt = [None]*2

def __setCalculatedVal(rightSideValueAg):
    #from vrfyPySf import blStt, inStt, scalarStt, strStt, krryStt
    #from vrfyPySf import strExceptionStt, strPythonAppErrorStt
    import sfFnctnsOp as sff
    global blStt, inStt, strStt, scalarStt, strExceptionStt, strPythonAppErrorStt
    blStt = None
    inStt = None
    strStt = None
    scalarStt = None
    strExceptionStt = ""
    strPythonAppErrorStt = None

    #import pdb; pdb.set_trace()
    if isinstance(rightSideValueAg, (bool, sff.np.bool_)):
        blStt = rightSideValueAg
    elif ( isinstance(rightSideValueAg, sff.np.ndarray) 
       and (rightSideValueAg.shape==())
       and isinstance(rightSideValueAg.ravel()[0], sff.np.bool_)
    ):
        # 11.08.03 Python(x,y) ver 2.6.6.2 have changed as that
        # (~[0,1,2]==(0,1,2)).all() return ClTensor, not numpy.bool_
        blStt = rightSideValueAg.ravel()[0]
    elif ( isinstance(rightSideValueAg, (int, sff.np.int32) ) 
      or isinstance(rightSideValueAg, long)
    ):
        inStt = rightSideValueAg
    elif ( isinstance(rightSideValueAg, float) or ( isinstance(rightSideValueAg, complex) ) ):
        scalarStt = rightSideValueAg
    elif isinstance(rightSideValueAg, str):
        strStt = rightSideValueAg

def __calculateLineString(strAg):
    # if exception has occured then upper initilize of blStt, inStt, ... so on
    # are passed. So initilaize below variables in this place too.
    global strExceptionStt, strPythonAppErrorStt

    strExceptionStt = ""
    strPythonAppErrorStt = None

    #import pdb; pdb.set_trace()
    try:
        #__execLine(strAg )
        #sP.execLine(strAg )
        valAt = sP.execLine(strAg)
        __setCalculatedVal(valAt)
        """'
    except sff.ClAppError, valAt:
        strPythonAppErrorStt = str(valAt)

        '"""
    except StandardError, valAt:
        strExceptionStt = str(valAt)
        #clTestGlb.OutError(strExceptionStt );
        #raise SystemExit (str(valAt)
        #                + " at excecuting:" + strExecutingAt)
    except SystemExit, valAt:
        strExceptionStt = str(valAt)
        #clTestGlb.OutError(strExceptionStt );

    #print "debug valAt:",valAt
    #print "type:",type(valAt)

def checkFileNameDoTest():
    global kv
    if not ((sys.argv[1] == "temp.vrf")
            or(sys.argv[1] == "testOp.vrf")
            or(sys.argv[1] == "testSym.vrf")
       ):
        return False

    import kv as md
    kv = md

    global calculateLineString
    global checkResultVal, checkResultArr
    global checkVal, valStt, checkValArr    #, ClTensorD

    import sfFnctnsOp as sff
    import operator as op


    #ClTensorD   = __ClTensorD
    #krryStt     = ClTensorD([0])   # ClTensorD
    strExceptionStt = ""
    strPythonAppErrorStt = ""
    clTestGlb = None

    calculateLineString = __calculateLineString


    def __checkResultVal(strAg):
        global clTestGlb

        #import pdb; pdb.set_trace()
        rsltAt = sff.getSf("_rs")
        if rsltAt == eval(strAg):
            strOKAt = "Checked. Result value == " + strAg
            clTestGlb.OutOK( strOKAt );
        else:
            strErrorAt = "Checked NG.  Result value:"+str(rsltAt)+" != " + strAg
            clTestGlb.OutError(strErrorAt );

    checkResultVal = __checkResultVal


    def __checkResultArr(strAg):
        global clTestGlb
        rsltAt = sff.getSf("_rs")
        strAg = "sff.np.array(" + strAg + ")"
        blAt = reduce( op.mul, sff.np.ravel( abs(rsltAt - eval(strAg))
                              <1e-6) , True )
        if blAt == True:
            strOKAt = "Checked. Array Result value == " + strAg
            clTestGlb.OutOK( strOKAt );
        else:
            strErrorAt = "Checked NG.  Result value:"+str(rsltAt)+" != " + strAg
            clTestGlb.OutError(strErrorAt );

    checkResultArr = __checkResultArr

    def __checkVal(strAg):
        global clTestGlb

        #import pdb; pdb.set_trace()
        blAt = valStt == eval(strAg)
        if isinstance(blAt, sff.np.ndarray):
            blAt = sff.np.alltrue(blAt)
        if blAt:
            strOKAt = "Checked. Result value == " + strAg
            clTestGlb.OutOK( strOKAt );
        else:
            strErrorAt = "Checked NG.  valStt value:"+str(valStt)+" != " + strAg
            clTestGlb.OutError(strErrorAt );

    checkVal = __checkVal

    def __checkValArr(strAg):
        global clTestGlb
        strAg = "sff.np.array(" + strAg + ")"
        blAt = reduce( op.mul, sff.np.ravel( abs(valStt - eval(strAg))
                              <1e-6) , True )
        if blAt == True:
            strOKAt = "Checked. Array valStt value == " + strAg
            clTestGlb.OutOK( strOKAt );
        else:
            strErrorAt = "Checked NG.  valStt value:"+str(valStt)+" != " + strAg
            clTestGlb.OutError(strErrorAt );

    checkValArr = __checkValArr

    def __setOnValStt(valAg):
        global valStt
        valStt = valAg

    setOnValStt = __setOnValStt

    convertFileAndExecute = sP.convertFileAndExecute

    #;;sfIni.py testPyClcLine.vrf
    # ================== kVerifier Test end =======================




    #clTestGlb = kv.ClActnScrpts(globals())
    dctGlbAt=globals()
    dctGlbAt.update(locals())
    clTestGlb = kv.ClActnScrpts(dctGlbAt)

    clTestGlb.rgstVrfyVar( inStt     = ('@kv.a2i',)
        , blStt                 = ('@bool',)
        , scalarStt             = (kv.tolerantType, '@complex')
        , strStt                = ('@str',)
        #, calculateLineString   = (kv.fnType, '@str')
        , calculateLineString   = (kv.fnType, )
        , convertFileAndExecute  = (kv.fnType, '@str')
        , converFileAndStore    = (kv.fnType, '@str')
        #, krryStt               = (kv.arrayType, '@complex')
        #, krryStt               = ('@sff.krry',)
        #, krryStt               = ('@ClTensorD',)
        , strExceptionStt       = ('@str',)
        , strPythonAppErrorStt  = ('@str',)
        , checkResultVal        = (kv.fnType, '@str')
        , checkResultArr        = (kv.fnType, '@str')
        , checkVal              = (kv.fnType, '@str')
        , checkValArr           = (kv.fnType, '@str')
    )

    kv.ClVrfySglt.GetStt().Main(sys.argv[1])

    return True     # sfPPOp.__main__() will call exit(0)


    
