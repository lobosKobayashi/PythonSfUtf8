# -*- encoding: utf-8 -*-
from __future__ import division
"""'
english:
    PythonSf pysf/symIntr.py
    https://github.com/lobosKobayashi
    http://lobosKobayashi.github.com/
    
    Copyright 2016, Kenji Kobayashi
    All program codes in this file was designed by kVerifierLab Kenji Kobayashi

    I release souce codes in this file under the GPLv3
    with the exception of my commercial uses.

    2016y 12m 28d Kenji Kokbayashi

japanese:
    PythonSf pysf/symIntr.py
    https://github.com/lobosKobayashi
    http://lobosKobayashi.github.com/

    Copyright 2016, Kenji Kobayashi
    このファイルの全てのプログラム・コードは kVerifierLab 小林憲次が作成しました。
    
    作成者の小林本人に限っては商用利用を許すとの例外条件を追加して、
    このファイルのソースを GPLv3 で公開します。

    2016年 12月 28日 小林憲次
'"""

"""
Physical units and dimensions.

The base class is Unit, where all here defined units (~200) inherit from.
"""

import sympy as ts
if float(ts.__version__[2:5]) >= 7.1:
    from sympy import Rational, pi
    from sympy.core import AtomicExpr

    class Unit(AtomicExpr):
        """
        Base class for all physical units.

        Create own units like:
        m = Unit("meter", "m")
        """
        is_positive = True    # make (m**2)**Rational(1,2) --> m
        is_commutative = True

        __slots__ = ["name", "abbrev"]

        def __new__(cls, name, abbrev, **assumptions):
            obj = AtomicExpr.__new__(cls, **assumptions)
            assert isinstance(name, str),repr(type(name))
            assert isinstance(abbrev, str),repr(type(abbrev))
            obj.name = name
            obj.abbrev = abbrev
            return obj

        def __getnewargs__(self):
            return (self.name, self.abbrev)

        def __eq__(self, other):
            return isinstance(other, Unit) and self.name == other.name

        def __hash__(self):
            return super(Unit, self).__hash__()

        def _hashable_content(self):
            return (self.name,self.abbrev)


    # Delete this so it doesn't pollute the namespace
    #del AtomicExpr

    def defunit(value, *names):
        # define other unit label in symIntf global name space
        u = value
        g = globals()
        for name in names:
            g[name] = u


    # Dimensionless

    percent = percents = Rational(1,100)
    permille = permille = Rational(1,1000)

    ten = Rational(10)

    yotta = ten**24
    zetta = ten**21
    exa   = ten**18
    peta  = ten**15
    tera  = ten**12
    giga  = ten**9
    mega  = ten**6
    kilo  = ten**3
    deca  = ten**1
    deci  = ten**-1
    centi = ten**-2
    milli = ten**-3
    micro = ten**-6
    nano  = ten**-9
    pico  = ten**-12
    femto = ten**-15
    atto  = ten**-18
    zepto = ten**-21
    yocto = ten**-24

    rad = radian = radians = 1
    deg = degree = degrees = pi/180


    # Base units

    defunit(Unit('meter', 'm`'), 'm', 'meter', 'meters')
    defunit(Unit('kilogram', 'kg`'), 'kg', 'kilogram', 'kilograms')
    defunit(Unit('second', 's`'), 's', 'second', 'seconds')
    defunit(Unit('ampere', 'A`'), 'A', 'ampere', 'amperes')
    defunit(Unit('kelvin', 'K`'), 'K', 'kelvin', 'kelvins')
    defunit(Unit('mole', 'mol`'), 'mol', 'mole', 'moles')
    defunit(Unit('candela', 'cd`'), 'cd', 'candela', 'candelas')
    defunit(Unit('volt', 'V`'),   'V', 'volt',  'volts')


    # Derived units

    defunit(1/s, 'Hz', 'hz', 'hertz')
    defunit(m*kg/s**2, 'N', 'newton', 'newtons')
    defunit(N*m, 'J', 'joule', 'joules')
    #defunit(J/s, 'W', 'watt', 'watts')
    defunit(V*A, 'W', 'watt', 'watts')
    defunit(N/m**2, 'Pa', 'pa', 'pascal', 'pascals')
    defunit(s*A, 'C', 'coulomb', 'coulombs')
    defunit(V/A, 'ohm', 'ohms')
    defunit(A/V, 'S', 'siemens', 'mho', 'mhos')
    defunit(C/V, 'F', 'farad', 'farads')
    defunit(J/A, 'Wb', 'wb', 'weber', 'webers')
    defunit(V*s/m**2, 'T', 'tesla', 'teslas')
    defunit(V*s/A, 'H', 'henry', 'henrys')

else:
    from sympy import Rational, pi
    from sympy.core.basic import Basic, Atom

    class Unit(Atom):
        """
        Base class for all physical units.

        Create own units like:
        m = Unit("meter", "m")
        """
        is_positive = True    # make (m**2)**Rational(1,2) --> m
        is_commutative = True

        __slots__ = ["name", "abbrev"]

        def __new__(cls, name, abbrev, **assumptions):
            #import pdb; pdb.set_trace()
            obj = Basic.__new__(cls, **assumptions)
            assert isinstance(name, str),`type(name)`
            assert isinstance(abbrev, str),`type(abbrev)`
            obj.name = name
            obj.abbrev = abbrev
            return obj

        def __eq__(self, other):
            return isinstance(other, Unit) and self.name == other.name

        def _hashable_content(self):
            return (self.name,self.abbrev)

        """
        # compare dosen't work for <:StrictInequality(
        def __cmp__(self, other):
            return 1
        """

    # Delete this so it doesn't pollute the namespace
    del Atom

    def defunit(value, *names):
        u = value
        g = globals()
        for name in names:
            g[name] = u


    # Dimensionless

    percent = percents = Rational(1,100)
    permille = permille = Rational(1,1000)

    ten = Rational(10)

    yotta = ten**24
    zetta = ten**21
    exa   = ten**18
    peta  = ten**15
    tera  = ten**12
    giga  = ten**9
    mega  = ten**6
    kilo  = ten**3
    deca  = ten**1
    deci  = ten**-1
    centi = ten**-2
    milli = ten**-3
    micro = ten**-6
    nano  = ten**-9
    pico  = ten**-12
    femto = ten**-15
    atto  = ten**-18
    zepto = ten**-21
    yocto = ten**-24

    rad = radian = radians = 1
    deg = degree = degrees = pi/180


    # Base units

    defunit(Unit('meter', 'm`'), 'm', 'meter', 'meters')
    defunit(Unit('kilogram', 'kg`'), 'kg', 'kilogram', 'kilograms')
    defunit(Unit('second', 's`'), 's', 'second', 'seconds')
    defunit(Unit('ampere', 'A`'), 'A', 'ampere', 'amperes')
    defunit(Unit('kelvin', 'K`'), 'K', 'kelvin', 'kelvins')
    defunit(Unit('mole', 'mol`'), 'mol', 'mole', 'moles')
    defunit(Unit('candela', 'cd`'), 'cd', 'candela', 'candelas')
    defunit(Unit('volt', 'V`'),   'V', 'volt',  'volts')


    # Derived units

    defunit(1/s, 'Hz', 'hz', 'hertz')
    defunit(m*kg/s**2, 'N', 'newton', 'newtons')
    defunit(N*m, 'J', 'joule', 'joules')
    #defunit(J/s, 'W', 'watt', 'watts')
    defunit(V*A, 'W', 'watt', 'watts')
    defunit(N/m**2, 'Pa', 'pa', 'pascal', 'pascals')
    defunit(s*A, 'C', 'coulomb', 'coulombs')
    defunit(V/A, 'ohm', 'ohms')
    defunit(A/V, 'S', 'siemens', 'mho', 'mhos')
    defunit(C/V, 'F', 'farad', 'farads')
    defunit(J/A, 'Wb', 'wb', 'weber', 'webers')
    defunit(V*s/m**2, 'T', 'tesla', 'teslas')
    defunit(V*s/A, 'H', 'henry', 'henrys')


"""'
# Float(..) is merged into the sfpy.customize.py file
def Float(physicalValAg):
    if isinstance(physicalValAg, ts.Number):
        return float(physicalValAg)
    else:
        assert isinstance(physicalValAg, ts.Mul)
        # covert V to m**2*kg/(A*s**3)
        compensatingUnitAt = 1
        for elmAt in physicalValAg.args:
            if elmAt == V:
                compensatingUnitAt = compensatingUnitAt*(m**2*kg/(A*s**3))/V
            elif isinstance(elmAt, ts.Pow):
                if elmAt.args[0] == V:
                    powNumAt = elmAt.args[1]
                    compensatingUnitAt = (compensatingUnitAt
                                         *((m**2*kg/(A*s**3))**powNumAt)
                                         *(V**-powNumAt)
                                         )
        if compensatingUnitAt == 1:
            assert False, ("At Float(.), you set physical quantity parameter"
                          +",the unit of which is not cancelled:"
                          + str(physicalValAg)
                          ) 
        else:
            valAt = physicalValAg * compensatingUnitAt
            assert isinstance(valAt, ts.Number),("At Floa(.)"
                        + " you set physical quantity parameter"
                        +",the unit of which is not cancelled:"
                        + str(valAt)
                                                )

            return float(valAt)


if __name__ == "__main__":
    print 1* W
    print 1* V
    print 1* ohm
    print 1* ohm *(1*A)

    print 1.5* W
    print 1.5* V
    print 1.5* ohm
    print 1.5* ohm *(1*A)

    print 1*W/(10*V *(5*A))
    print 1*W/(10*J/s)
    print 3.3*F
    print 1*F *(1*V)/(2*C)

    print "========== Float ============="
    print Float(1.5*s *(1.1/s) )
    print Float(1*s/s)
    print Float(1.5*V*A /(1.1*W) )
    print Float(1.5*W*s /(1.1*N*m) )
    print Float(1.5* m**2*kg/(A*s**3)/(1.1*V) )

    import math
    import scipy
    print math.sin(Float(1.5*V*A /(1.1*W) ))
    print scipy.sin(Float(1.5*V*A /(1.1*W) ))
    print ts.sin(Float(1*V*A /W ))
'"""
