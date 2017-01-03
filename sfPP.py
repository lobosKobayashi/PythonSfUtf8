# -*- encoding: utf-8 -*-
"""'
english:
    PythonSf sfPP.py
    https://github.com/lobosKobayashi
    http://lobosKobayashi.github.com/
    
    Copyright 2016, Kenji Kobayashi
    All program codes in this file was designed by kVerifierLab Kenji Kobayashi

    I release souce codes in this file under the GPLv3
    with the exception of my commercial uses.

    2016y 12m 28d Kenji Kokbayashi

japanese:
    PythonSf sfPP.py
    https://github.com/lobosKobayashi
    http://lobosKobayashi.github.com/

    Copyright 2016, Kenji Kobayashi
    このファイルの全てのプログラム・コードは kVerifierLab 小林憲次が作成しました。
    
    作成者の小林本人に限っては商用利用を許すとの例外条件を追加して、
    このファイルのソースを GPLv3 で公開します。

    2016年 12月 28日 小林憲次
'"""

def whatFileEncoding():
    """'
    return platform.system(): if windows OS then cp932 file else utf-8 file
    return "utf-8"          : utf-8 file
    return "cp932"          : cp932 file
    '"""
    import platform
    return platform.system()

if __name__ == '__main__':
    """'
    '"""
    def gnExec():
        from multiprocessing import Process, Queue
        while True:
            q = Queue()
            p = Process(target=execTempConverted, args=(q,))
            p.start()
            rtnValAt = q.get()

            yield rtnValAt

            del p
            del q

    gnExecGlb=gnExec()

    import pysf.sfPPrcssr
    pysf.sfPPrcssr.gnExecGlb = gnExecGlb
    pysf.sfPPrcssr.start()
