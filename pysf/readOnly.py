# -*- encoding: utf-8 -*-
"""'
english:
    PythonSf pysf/readOnly.py
    https://github.com/lobosKobayashi
    http://lobosKobayashi.github.com/
    
    Copyright 2016, Kenji Kobayashi
    All program codes in this file was designed by kVerifierLab Kenji Kobayashi

    I release souce codes in this file under the GPLv3
    with the exception of my commercial uses.

    2016y 12m 28d Kenji Kokbayashi

japanese:
    PythonSf pysf/readOnly.py
    https://github.com/lobosKobayashi
    http://lobosKobayashi.github.com/

    Copyright 2016, Kenji Kobayashi
    このファイルの全てのプログラム・コードは kVerifierLab 小林憲次が作成しました。
    
    作成者の小林本人に限っては商用利用を許すとの例外条件を追加して、
    このファイルのソースを GPLv3 で公開します。

    2016年 12月 28日 小林憲次
'"""

dctGlb=None
def _getDctGlobals(dctAg):
    global dctGlb;
    dctGlb=dctAg

class RO(object):
    """' Read only variable container class.
         2013.03.01 experimental implementat.
    usages:
    ro=RO(x=1,y=2)

    usages subject to ro=RO()

        You can set new value just only for the _ data member.
    usages.
    ro(_=3); ro(_=RO(_=4)); ro._._ 
    ===============================
    4

    ro(_=3); ro._=RO(_=4); ro._._ 
    ===============================
    4

    (ro(_=3), ro(_=RO(_=4)), ro._._)[-1]
    ===============================
    4
    '"""
    def __init__(self, **dctAg):
        self.__call__(**dctAg)

    def __call__(self, **dctAg):
        global dctGlb
        for k in dctAg:
            if k in self.__dict__ and k != "_":
                assert False, ("You doubly assigned for the variable:" + k
                             + " with a value:" + str(dctAg[k]) + "\n")
            else:
                self.__dict__[k] = dctAg[k]
                assert not(k in dctGlb), ("You cant use the variable name:"+ k
                                          +"."
                                          +" Because there is the variable name already."
                                          )
                dctGlb.update({k:dctAg[k]})

            #return True; # to set sentinel
            # It is not lucid functional programming to use a sentinel

    def __getattr__(self, name):
        print "debug--name:" + str(name)
        assert name in self.__dict__, "There is no read only variable:" + name
        return self.__dict__[name]

    def __setattr__(self, name, ag):
        if name == '_':
            self.__dict__['_'] = ag
        else:
            assert False, ("You can't set value:" + str(ag)
                        + " for read only variable:" + name + "\n")

    def __delattr__(self, name):
        assert False, "Sorry. we don't implement __delattr__()"

    def __del__(self):
    # __del__(self) will cause Exception TypeError: 'NoneType' object is not callable
    # if there is a global RO instance.
    #def delete(self):
        global dctGlb
        for k in self.__dict__:
            assert (k in dctGlb), ("You must have deleted the variable name:"+ k
                                              +"."
                                              )
            del dctGlb[k]

prgn=lambda *tplAg:tplAg[-1]

if dctGlb==None:
    # This codes is for PythonSf one-liner or block.
    import sfFnctns as sf
    dctGlb = sf.__getDctGlobals()

"""' usage
Elisp vs PythonSf block vs PythonSf one-liners

(let* ((x (sin (/ pi 6)))
       (y (+ (* 3 x) 100))
      )
      (+ 1000000 y)
);1000101.5


//@@
from pysf.readOnly import *
print prgn(
   RO(f = lambda x=sin(pi/6):x+x^2+3),  # let sentence
   RO(g = lambda x=   f():3*x+100),     # let sentence

   1000000+   g()
)    

print 'f' in globals()
//@@@
1000111.25
False

from pysf.readOnly import *; prgn( RO(f = lambda x=sin(pi/6):x+x^2+3), RO(g = lambda x=f():3^x+100), 1000000+g())
===============================
1000161.54669

from pysf.readOnly import *; prgn( RO(f = 了 x=sin(pi/6):x+x^2+3), RO(g = 了 x=f():3^x+100), 1000000+g())
===============================
1000161.54669

f=了 x=sin(pi/6):x+x^2+3; g=了 x=f():3^x+100; 1000000+g()
===============================
1000161.54669
'"""
