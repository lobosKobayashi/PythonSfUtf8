# -*- encoding: utf-8 -*-
"""'
english:
    PythonSf sfPPOp.py
    https://github.com/lobosKobayashi
    http://lobosKobayashi.github.com/
    
    Copyright 2016, Kenji Kobayashi
    All program codes in this file was designed by kVerifierLab Kenji Kobayashi

    I release souce codes in this file under the GPLv3
    with the exception of my commercial uses.

    2016y 12m 28d Kenji Kokbayashi

japanese:
    PythonSf sfPPOp.py
    https://github.com/lobosKobayashi
    http://lobosKobayashi.github.com/

    Copyright 2016, Kenji Kobayashi
    このファイルの全てのプログラム・コードは kVerifierLab 小林憲次が作成しました。
    
    作成者の小林本人に限っては商用利用を許すとの例外条件を追加して、
    このファイルのソースを GPLv3 で公開します。

    2016年 12月 28日 小林憲次
'"""

if __name__ == '__main__':
    """'
    '"""
    import sys
    #import pdb; pdb.set_trace()
    # print "Now in __main__"   # to dubug
    if ( (len(sys.argv) == 1)
      or (sys.argv[1] == "-h")
      or (sys.argv[1] == "/?")
    ):
        # command line help
        print (
""" PythonSf pre-processr
-h: help: this message
-fl: execute Python one-liner file specified by an argment with PythonSf
   pre-processing.
     There is the converted Python codes in  _tmC.py at the current
   directory.
-f:  execute Python block codes file specified by an argment with PythonSf
   pre-processing
     There is the converted Python codes in  _tmC.py at the current
   directory.

default: no option and an expression string
"""     )
        exit()

    import pysfOp.vrfyPySfOp as md
    # if argv[1] == "temp.vrf" for "testOp.vrf" the do kVerifier test and return True
    # else return False
    if md.checkFileNameDoTest():
        exit()

    # It is not requested to verify PythonSf actions.
    # Now we parse and calculate a given expression.
    import pysfOp.sfPPrcssrOp as md
    if ( sys.argv[1] == '-f'):
        #md.converFileAndExecute( sys.argv[2], sys.argv[1] )
        md.convertFileAndExecute( sys.argv[2])
    elif (sys.argv[1] == '-fl'):
        lstLineAt = open(sys.argv[2], 'r').readlines()
        #print "debug lstLineAt:", lstLineAt
        assert len(lstLineAt) == 1, ("You set a file that is not an one-liner:"
                                    + sys.argv[2]
                                    + ":"
                                    + lstLineAt
                                    + "\n"
                                    )
        md.execLine( lstLineAt[0].strip() )
    else:
        #__execLine( (" ".join(sys.argv[1:])).strip() )
        md.execLine( (" ".join(sys.argv[1:])).strip() )

