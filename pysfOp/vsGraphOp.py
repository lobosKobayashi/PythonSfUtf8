# -*- encoding: utf-8 -*-
from __future__ import division
"""'
english:
    PythonSf pysfOp/vsGraphOp.py
    https://github.com/lobosKobayashi
    http://lobosKobayashi.github.com/
    
    Copyright 2016, Kenji Kobayashi
    All program codes in this file was designed by kVerifierLab Kenji Kobayashi

    I release souce codes in this file under the GPLv3
    with the exception of my commercial uses.

    2016y 12m 28d Kenji Kokbayashi

japanese:
    PythonSf pysfOp/vsGraphOp.py
    https://github.com/lobosKobayashi
    http://lobosKobayashi.github.com/

    Copyright 2016, Kenji Kobayashi
    このファイルの全てのプログラム・コードは kVerifierLab 小林憲次が作成しました。
    
    作成者の小林本人に限っては商用利用を許すとの例外条件を追加して、
    このファイルのソースを GPLv3 で公開します。

    2016年 12月 28日 小林憲次
'"""

import sfFnctnsOp as sf

__obj2dDisplayGeneratedStt = None   # to enable overlap plot
def plotTrajectory(arg, color = sf.cyan, xyRate=True, radiusRate = 80.0
                      , blAxes = True):
    """' plot 2D/3D trajectory. You can hand over list of length 2 element at 2D 
        or length 3 element at 3D.
         The line radius is 1/200 for max display size. The line radius can be
        changed by radiusRate.
         If blAxes = False then the RGB axis is not displayed.
        
         At 2D plot, if xyRage == False then plot in a same hight/width square
    '"""
    if not(hasattr(arg, '__getitem__')) and hasattr(arg, '__iter__'):
        arg = list(arg)

    vs = sf.vs_()

    color = tuple(color)   # color argment may be list/vector
    if isinstance(arg,list) or isinstance(arg,tuple) or isinstance(
                                                    arg,type(sf.sc.array([0,]))):
        from octnOp import ClOctonion
        if not(hasattr(arg[0],'__len__')) and isinstance(arg[0], complex):
            arg = [ (x.real, x.imag) for x in arg]
        elif not(hasattr(arg[0],'__len__')) and isinstance(arg[0], ClOctonion):
            arg = [ x[1:4] for x in arg]

        if len(arg[0])==2:
            import visual.graph as vg
            global __obj2dDisplayGeneratedStt

            maxX = max([abs(elm[0]) for elm in arg])
            maxY = max([abs(elm[1]) for elm in arg])

            print "maxX:",maxX, "  maxY:",maxY

            if (__obj2dDisplayGeneratedStt == None):
                if xyRate == True:  # 11.01.16 to 
                    maxAt = max(maxX, maxY)
                    __obj2dDisplayGeneratedStt = vg.gdisplay(
                                    width=600*maxX/maxAt,height=600*maxY/maxAt)
                else:
                    __obj2dDisplayGeneratedStt = vg.gdisplay(
                                                    width=600,height=600)
                #__bl2dDisplayGeneratedStt = True
            grphAt = vg.gcurve(color = color)
            for i in range(len(arg)):
                assert len(arg[i])==2, "unexpeted length data:"+str(arg[i])
                grphAt.plot(pos = arg[i])

            #return __obj2dDisplayGeneratedStt
            #import pdb; pdb.set_trace()
            #print "debug:",grphAt.gcurve.pos

            # plot start mark
            grphSqAt = vg.gcurve(color = color)
            pos0At = grphAt.gcurve.pos[0,:][:2]
            rateAt = 50
            for x,y in sf.mitr([-maxX/rateAt, maxX/rateAt]
                             , [-maxY/rateAt, maxY/rateAt]):
                grphSqAt.plot(pos = pos0At+[x,y])
            
            grphSqAt.plot(pos = pos0At+[-maxX/rateAt,-maxY/rateAt])

            return grphAt   # 09.02.04 to animate graph
        elif len(arg[0])==3:
            vs.scene.forward=(-1,+1,-1)
            vs.scene.up=(0,0,1)

            c = vs.curve( color = color )

            maxX, maxY, maxZ = 0,0,0
            for i in range(len(arg)):
                if maxX < abs(arg[i][0]):
                    maxX = abs(arg[i][0])
                if maxY < abs(arg[i][1]):
                    maxY = abs(arg[i][1])
                if maxZ < abs(arg[i][2]):
                    maxZ = abs(arg[i][2])
                c.append( arg[i] )
            #print c.pos
            print "maxX:",maxX, "  maxY:",maxY, "  maxZ:",maxZ
            maxAt = max(maxX,maxY,maxZ)
            c.radius = maxAt/radiusRate

            vs.sphere(pos = arg[0], radius = 3*c.radius, color = color)

            if blAxes == True:
                # draw axise
                vs.curve( pos=[(0,0,0), (maxAt,0,0)]
                        ,  color=(1,0,0)
                        , radius = maxAt/100 )
                vs.curve( pos=[(0,0,0), (0,maxAt,0)]
                        ,  color=(0,1,0)
                        , radius = maxAt/100 )
                vs.curve( pos=[(0,0,0), (0,0,maxAt)]
                        ,  color=(0,1,1)
                        , radius = maxAt/100 )
            #return vs.scene
            return c    # 09.02.04 to animate graph
    else:
        assert False,"unexpeted data:"+str(arg)


__objGrDisplayGeneratedStt = None   # to enable overlap plot
def plotGr(vctAg, start=(), end=None, N=50, color = sf.cyan):
    """' plot graph for a function or vector data
        If you call plotGr(..) a number of times, then the graphs were plotted
        in piles.

        start,end are domain parameters, which are used if vctAg type is 
        function

        if you want to vanish the graph then do as below
            objAt=plotGr(..)
                .
                .
            objAt.visible = None

    usage:
        plotGr(sin) # plot sin graph in a range from 0 to 1
        
        plotGr(sin,-3,3) #plot sin in a range from -3 to 3

        plotGr(sin,[-3,-2,0,1]) 
        # plot sequential line graph by
        #                       [(-3,sin(-3),(-2,sin(-2),(0,sin(0),(1,sin(1)]

        plotGr([sin(x) for x in klsp(-3,3)]) # plot a sequence data
    '"""
    if not(hasattr(vctAg, '__getitem__')) and hasattr(vctAg, '__iter__'):
        vctAg = list(vctAg)

    vs = sf.vs_()

    global __objGrDisplayGeneratedStt
    color = tuple(color)   # color argment may be list/vector
    import visual.graph as vg
    if __objGrDisplayGeneratedStt == None:
        __objGrDisplayGeneratedStt = vg.gdisplay()
    grphAt = vg.gcurve( color = color)
    #grphAt = vg.gcurve(gdisplay=dspAt, color = color)
    #import pdb; pdb.set_trace()
    if '__call__' in dir(vctAg):
        # vctAg is function
        if start != () and end == None and hasattr(start, '__iter__'):
            for x in start:
                grphAt.plot(pos = [x, float(vctAg(x))] )
        else:
            if start == ():
                start = 0
            if end == None:
                end = 1

            assert start != end
            if start > end:
                start, end = end, start

            #assert start != end
            """'
            for x in arsq(start, N, float(end-start)/N):
                # 08.10.27 add float(..) cast to avoid below error 
                # "No registered converter was able to produce a C++ rvalue"
                # at ;;n=64;plotGr([sf.sc.comb(n,i) for i in range(n)])
                grphAt.plot(pos = [x, float(vctAg(x))] )
            '"""
            for x in sf.klsp(start, end, N):
                # 09.12.03 to display end and avoid 0
                grphAt.plot(pos = [x, float(vctAg(x))] )

        #return grphAt
        return __objGrDisplayGeneratedStt
    else:
        if (start != ()) or (end != None):
            #import pdb; pdb.set_trace()
            if start == ():
                start = 0
            if end == None:
                end = 1

            assert start != end
            if start > end:
                start, end = end, start

            N = len(vctAg)
            for i, x in enmasq([start, N, (end - start)/N]):
                grphAt.plot(pos = [x, float(vctAg[i])] )
        else:
            for i in range(len(vctAg)):
                grphAt.plot(pos = [i, float(vctAg[i])] )
        #return grphAt
        return __objGrDisplayGeneratedStt

def plotDbl(sq0,sq1, region=None, N=50):
    if isinstance(sq0, (tuple, list, sf.np.ndarray)):
        sf.plotGr(sq0)
        return sf.plotGr(sq1,color=sf.red)
    else:
        assert hasattr(sq0,'__call__'), "at plotDbl(..), you set parameter sq0 that is not function"
        assert hasattr(sq1,'__call__'), "at plotDbl(..), you set parameter sq1 that is not function"

        if region==None:
            region = [-1,1]
        assert(isinstance(region,(tuple, list, sf.np.ndarray)) and len(region)==2)
        sf.plotGr(sq0,region[0],region[1],N=N)
        return sf.plotGr(sq1, region[0], region[1], N=N, color=sf.red)


