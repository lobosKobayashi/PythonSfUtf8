# -*- encoding: utf-8 -*-
from __future__ import division
"""'
english:
    PythonSf pysfOp/sfPPrcssrOp.py
    https://github.com/lobosKobayashi
    http://lobosKobayashi.github.com/
    
    Copyright 2016, Kenji Kobayashi
    All program codes in this file was designed by kVerifierLab Kenji Kobayashi

    I release souce codes in this file under the GPLv3
    with the exception of my commercial uses.

    2016y 12m 28d Kenji Kokbayashi

japanese:
    PythonSf pysfOp/sfPPrcssrOp.py
    https://github.com/lobosKobayashi
    http://lobosKobayashi.github.com/

    Copyright 2016, Kenji Kobayashi
    このファイルの全てのプログラム・コードは kVerifierLab 小林憲次が作成しました。
    
    作成者の小林本人に限っては商用利用を許すとの例外条件を追加して、
    このファイルのソースを GPLv3 で公開します。

    2016年 12月 28日 小林憲次
'"""

strFileEncodeGlb="utf-8"
__all__ = ["execLine"]

def convertGreekLetters(ustrAg):
    dctCnvrtngTbl={     # converting table of Greek Kanji letter to ASCII
            # Larage Greek Letters
            u"Α":"k_lAlpha_"
          , u"Β":"k_lBeta_"
          , u"Γ":"k_lGamma_"
          , u"Δ":"k_lDelta_"
          , u"Ε":"k_lEpsilon_"
          , u"Ζ":"k_lOZeta_"
          , u"Η":"k_lEta_"
          , u"Θ":"k_lTheta_"
          , u"Ι":"k_lIota_"
          , u"Κ":"k_lKappa_"
          , u"Λ":"k_lLambda_"
          , u"Μ":"k_lMu_"
          , u"Ν":"k_lNu_"
          , u"Ξ":"k_lXi_"
          , u"Ο":"k_lOmicron_"
          , u"Π":"k_lPi_"
          , u"Ρ":"k_lRho_"
          , u"Σ":"k_lSigma_"
          , u"Τ":"k_lTau_"
          , u"Υ":"k_lUpsilon_"
          , u"Φ":"k_lPhi_"
          , u"Χ":"k_lChi_"
          , u"Ψ":"k_lPsi_"
          , u"Ω":"k_lOmega_"
    
            # Smallk Greek Letters
          , u"α":"k_sAlpha_"
          , u"β":"k_sBeta_"
          , u"γ":"k_sGamma_"
          , u"δ":"k_sDelta_"
          , u"ε":"k_sEpsilon_"
          , u"ζ":"k_sZeta_"
          , u"η":"k_sEta_"
          , u"θ":"k_sTheta_"
          , u"ι":"k_sIota_"
          , u"κ":"k_sKappa_"

          , u"λ":"lambda"

          , u"μ":"k_sMu_"
          , u"ν":"k_sNu_"
          , u"ξ":"k_sXi_"
          , u"ο":"k_sOmicron_"
          , u"π":"k_sPi_"
          , u"ρ":"k_sRho_"
          , u"σ":"k_sSigma_"
          , u"τ":"k_sTau_"
          , u"υ":"k_sUpsilon_"
          , u"φ":"k_sPhi_"
          , u"χ":"k_sChi_"
          , u"ψ":"k_sPsi_"
          , u"ω":"k_sOmega_"

          , u"`" :"k_bq_"      # back quote
    }

    lstGreekAt = dctCnvrtngTbl.keys()
    ustrAt = u""
    for ch in ustrAg:
        if ch in lstGreekAt:
            ustrAt += dctCnvrtngTbl[ch]
        else:
            ustrAt += ch

    return ustrAt

def convertCaret2Star(ustrAg):
    ustrAt = ustrAg
    # convert ^ to **
    sztAt=0
    while(True):
        sztAt = ustrAt.find('^', sztAt)
        if sztAt == -1: 
            break

        if sztAt>=1 and ustrAt[sztAt-1]=='\\':
            sztAt = sztAt + 1
        else:
            ustrAt = ustrAt[:sztAt]+"**"+ustrAt[sztAt+1:]
            sztAt = sztAt + 2
       
    # convert "\^" to "^"
    sztAt=0
    while(True):
        sztAt = ustrAt.find('^', sztAt)
        if sztAt == -1: 
            return ustrAt
        blAt = (sztAt>=1) and (ustrAt[sztAt-1]=='\\') 
        #if blAt:
        if True:
            ustrAt = ustrAt[:sztAt-1]+"^"+ustrAt[sztAt+1:]            
            sztAt = sztAt
        else:
            sztAt = sztAt + 1

        if sztAt>len(ustrAt):
            assert False

rightSideValueGlb__ = None
def execLine(strAg):
    global rightSideValueGlb__
    try:
        ustrAt = strAg.decode(strFileEncodeGlb)
        ustrAt = convertCaret2Star(ustrAt)
        lstStrAt = ustrAt.split(';')
        wFileAt = open('_tmC.py', 'w')
        usConvertedAt = u""
        usConvertedAt += "# -*- encoding: "+strFileEncodeGlb+" -*-\n"
        usConvertedAt += "from __future__ import division\n"
        usConvertedAt += "from pysfOp.sfFnctnsOp import *\n"
        usConvertedAt += "setDctGlobals(globals())\n"
        usConvertedAt += "from pysfOp.customizeOp import *\n"
        usConvertedAt += "if os.path.exists('./sfCrrntIniOp.py'):\n"
        usConvertedAt += "    from sfCrrntIniOp import *\n"

        #import pdb; pdb.set_trace()
        strLastAt, lstStrAt = lstStrAt[-1], lstStrAt[0:-1]
        for strAt in lstStrAt:
            usConvertedAt += convertGreekLetters(strAt.strip())+"\n"

        strLastAt = strLastAt.strip()
        if "==" in strLastAt:
            pass
        elif "!=" in strLastAt:
            pass
        elif "=" in strLastAt:
            print "Warning! Don't use a assignment sentence in end."
            #strLastAt = strLastAt[strLastAt.rfind('='):]


        if strLastAt == "":
            usConvertedAt += "rightSideValueGlb__ = None\n"
        else:
            usConvertedAt += "rightSideValueGlb__ = "\
                           + convertGreekLetters(strLastAt)+"\n"
            usConvertedAt += 'print "==============================="\n'
            usConvertedAt += "print rightSideValueGlb__"

        usConvertedAt = usConvertedAt.encode(strFileEncodeGlb)
        wFileAt.write(usConvertedAt)
        wFileAt.close()

        exec(usConvertedAt, globals())
        #print "==============================="
        #print rightSideValueGlb__

    except IOError, errValAt:
        import traceback
        print traceback.format_exc()
        raise SystemExit( "IOError:You may use nonexistent variable name:"
                          +str(errValAt) )

    except ValueError, valAt:
        import traceback
        print traceback.format_exc()
        raise SystemExit (str(valAt) )

    except TypeError, valAt:
        import traceback
        print traceback.format_exc()
        raise SystemExit (str(valAt) )

    except NameError, valAt:
        import traceback
        print traceback.format_exc()
        raise SystemExit (str(valAt) )

    except SyntaxError, valAt:
        import traceback
        print traceback.format_exc()
        raise SystemExit (str(valAt) )

    except RuntimeError, valAt:
        import traceback
        print traceback.format_exc()
        raise SystemExit (str(valAt) )

    """'
    #except valAt:
    except Exception, valAt:
        if blVrfyAg == True:
            rightSideValueGlb__ =valAt
        else:
            raise SystemExit (str(valAt) )

    '"""
    return rightSideValueGlb__  # vrfyPySfOp.py: __calculateLineString() uses this returned value

def convertFileAndExecute(fileNameAg):
    wFileAt = open('_tmC.py', 'w')
    usConvertedAt = u""
    usConvertedAt += "# -*- encoding: "+strFileEncodeGlb+" -*-\n"
    usConvertedAt += "from __future__ import division\n"
    usConvertedAt += "from pysfOp.sfFnctnsOp import *\n"
    usConvertedAt += "setDctGlobals(globals())\n"
    usConvertedAt += "from pysfOp.customizeOp import *\n"
    usConvertedAt += "if os.path.exists('./sfCrrntIniOp.py'):\n"
    usConvertedAt += "    from sfCrrntIniOp import *\n"

    lstLineAt = open(fileNameAg, 'r').readlines()
    for strAt in lstLineAt:
        strAt = convertCaret2Star(strAt)
        usConvertedAt += convertGreekLetters(strAt.rstrip())+"\n"

    wFileAt.write(usConvertedAt.encode(strFileEncodeGlb))
    wFileAt.close()

    exec(usConvertedAt.encode(strFileEncodeGlb), globals())

"""'
sfPPOp.py "f=λ x:x+1; f(1)"

'"""
