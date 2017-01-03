# -*- encoding: utf-8 -*-
from __future__ import division
"""'
english:
    PythonSf pysf/vsGraph.py
    https://github.com/lobosKobayashi
    http://lobosKobayashi.github.com/
    
    Copyright 2016, Kenji Kobayashi
    All program codes in this file was designed by kVerifierLab Kenji Kobayashi

    I release souce codes in this file under the GPLv3
    with the exception of my commercial uses.

    2016y 12m 28d Kenji Kokbayashi

japanese:
    PythonSf pysf/vsGraph.py
    https://github.com/lobosKobayashi
    http://lobosKobayashi.github.com/

    Copyright 2016, Kenji Kobayashi
    このファイルの全てのプログラム・コードは kVerifierLab 小林憲次が作成しました。
    
    作成者の小林本人に限っては商用利用を許すとの例外条件を追加して、
    このファイルのソースを GPLv3 で公開します。

    2016年 12月 28日 小林憲次
'"""


#from sfFnctns import *
import sfFnctns as sf

# 07.10.19

# if Image/real ratio of a complex number is greater than cDbBoundaryTanStt
# then we treat the complex number as on the image axis and put a rgb color of image axis

class ClCplxColor:
    """ Mapp complex number to RGB color like below.

                            \ Red and Green arear
          Red and Blue arear \_____________
                            / 
                           /  Blue and Green arear
                    

    def __init__(self, dbBoundary=1.0, dbLimit=10.0, dbGamma = 1.0):
        dbBoundary > abs(z)           ==> analog RGB mix
        dbLimit > abs(z) > abBoundary ==> Yeloo, Green, Cyan, Magenta
        abs(z) > dbLimit              ==> White
        
        see http://www.nasuinfo.or.jp/FreeSpace/kenji/sf/kkRGB/rgb.htm

    """
    __cDbRoot3 = 1.732050807568877;
    __cDbBoundaryTanStt = 100000;
    def __init__(self, dbBoundary=1.0, dbLimit=10.0, dbGamma = 1.0):
        self.m_dbCplx = 0+0j
        self.m_dbBoundary = dbBoundary
        self.m_dbLimit = dbLimit
        self.m_dbGamma = dbGamma


    def setGamma(self, dbAg):    # return void
        self.m_dbGamma = dbAt

    #if 1:
        self.m_inRed = int( 255* (self.m_inRed/255.0)**(1.0/self.m_dbGamma) )
        self.m_inGreen = int( 255* (self.m_inGreen/255.0)**(1.0/self.m_dbGamma) )
        self.m_inBlue = int(255* (self.m_inBlue/255.0)**(1.0/self.m_dbGamma) )
        """
    #else
        double Y = 0.299 * m_inRed + 0.587 * m_inGreen + 0.114 * m_inBlue;
        double U = -0.169* m_inRed - 0.332 * m_inGreen + 0.500 * m_inBlue;
        double V = +0.500* m_inRed - 0.419 * m_inGreen - 0.081 * m_inBlue;
    
        Y = 255* pow(Y/255.0, 1/self.m_dbGamma);
        m_inRed   = int( 1.0    * Y     -0.00092642    *U     +1.40169   *V);
        m_inGreen = int(0.999656* Y       -0.343577    *U     -0.713924  *V);
        m_inBlue  = int( 1.00177* Y       +1.77155     *U    -0.000274967*V);
    #endif
        """
        if ( self.m_inRed > 255 ):
            self.m_inRed = 255
        if ( self.m_inGreen > 255 ):
            self.m_inGreen = 255
        if ( self.m_inBlue > 255 ):
            self.m_inBlue = 255

    def __setColor(self, cplxAg): # return void
        """ comvert self.m_dbCplx to self.m_inRd, self.m_inGreen, self.m_inBlue
        """
        """'
        import fpconst as fc
        self.m_dbCplx = cplxAg
        if ( fc.isInf(cplxAg.real)
          or fc.isNaN(cplxAg.real)
          or fc.isInf(cplxAg.imag)
          or fc.isNaN(cplxAg.imag)
        ):
        '"""
        import math as mt
        self.m_dbCplx = cplxAg
        if ( sf.sc.isinf(cplxAg.real)
          or sf.sc.isnan(cplxAg.real)
          or sf.sc.isinf(cplxAg.imag)
          or sf.sc.isnan(cplxAg.imag)
        ):
            self.m_inRed = 0
            self.m_inGreen = 0
            self.m_inBlue = 0
            return

        # dbNormAt, dbImageAt, dbRealAt are normalized
        dbNormAt = abs(self.m_dbCplx) / self.m_dbBoundary
        dbImageAt = self.m_dbCplx.imag / self.m_dbBoundary
        dbRealAt = self.m_dbCplx.real / self.m_dbBoundary
        
        self.m_inRed=0
        self.m_inGreen=0
        self.m_inBlue=0
        if ( abs(self.m_dbCplx) > self.m_dbLimit ):
            self.m_inRed=255
            self.m_inGreen=255
            self.m_inBlue=255
            return
        elif (dbNormAt > 1 ):
            if ( dbRealAt >= 0):
                if ( dbImageAt >= 0):
                    self.m_inRed=255
                    self.m_inGreen=255
                else:
                    self.m_inBlue=255
                    self.m_inRed=255
            else:
                if ( dbImageAt >= 0):
                    self.m_inGreen=255
                    self.m_inBlue=120
                    self.m_inRed=120
                else:
                    self.m_inGreen=255
                    self.m_inBlue=255
            return
        elif ( dbRealAt == 0):
            if ( dbImageAt > 0):
                self.m_inGreen = int( 255* dbNormAt * mt.sin( mt.pi*3/8 ) )
                self.m_inRed = int( 255*dbNormAt * mt.cos( mt.pi*3/8 ) )
            elif ( dbImageAt < 0):
                self.m_inRed = int( 255*dbNormAt * mt.cos( mt.pi*3/8 ) )
                self.m_inBlue = int( 255*dbNormAt * mt.sin( mt.pi*3/8 ) )
        else:
            self.m_inRed=0
            self.m_inGreen=0
            self.m_inBlue=0
            dbThetaAt=0;
            if ( (dbImageAt > 0)  and ( dbImageAt >= -ClCplxColor.__cDbRoot3*dbRealAt) ):
                #! Red and Green arear
                if ( (dbRealAt == 0) 
                  or(
                       ( (dbImageAt / dbRealAt) > ClCplxColor.__cDbBoundaryTanStt )
                   and ( (dbImageAt / dbRealAt) < -ClCplxColor.__cDbBoundaryTanStt )
                    )
                ):
                    dbThetaAt = mt.pi/2;
                elif ( dbRealAt > 0 ):
                    dbThetaAt = mt.atan( dbImageAt / dbRealAt)
                elif ( dbRealAt < 0 ):
                    dbThetaAt = mt.pi - mt.atan( -dbImageAt / dbRealAt)

                dbThetaAt *= 3.0/4.0
                self.m_inRed = int ( 255 * dbNormAt * mt.cos(dbThetaAt) )
                self.m_inGreen = int ( 255 * dbNormAt * mt.sin(dbThetaAt) )
            elif ( (dbImageAt<=0) and (dbImageAt<=ClCplxColor.__cDbRoot3*dbRealAt)
            ):
                # Blue and Red arear
                if ( (dbRealAt == 0)
                  or ( ( (dbImageAt / dbRealAt) > ClCplxColor.__cDbBoundaryTanStt )
                   and ( (dbImageAt / dbRealAt) < -ClCplxColor.__cDbBoundaryTanStt )
                     )
                ):
                     dbThetaAt = mt.pi/2;
                elif ( dbRealAt > 0 ):
                     dbThetaAt = mt.atan(-dbImageAt/dbRealAt)
                elif (dbRealAt < 0):
                     dbThetaAt = mt.pi - mt.atan(-dbImageAt/-dbRealAt)

                dbThetaAt *= 3.0/4.0
                self.m_inRed = int ( 255 * dbNormAt * mt.cos(dbThetaAt) )
                self.m_inBlue = int ( 255 * dbNormAt * mt.sin(dbThetaAt) )
            else:
                #! Green and Blue arear
                #assert(dbRealAt < -0.00000001);
                #some function parameters make dbRealAt <0
                if (dbRealAt > 0):
                    dbRealAt = 0
                if ( ( (dbImageAt / dbRealAt) > ClCplxColor.__cDbBoundaryTanStt )
                 and ( (dbImageAt / dbRealAt) < -ClCplxColor.__cDbBoundaryTanStt )
                ):
                    assert false
                    #dbThetaAt = mt.pi / 3;
                elif ( dbImageAt > 0 ):
                    dbThetaAt = mt.pi/3 - sf.sc.arctan2(  dbImageAt,-dbRealAt )
                elif ( dbImageAt < 0 ):
                    dbThetaAt = mt.pi/3 + sf.sc.arctan2( -dbImageAt,-dbRealAt )
                else:
                    # minus number on real axis
                    dbThetaAt = (mt.pi/4.0)*4.0/3.0
                if ( dbThetaAt < 3.142/10000 ):
                    self.m_inRed = 255
                    self.m_inBlue = 255
                dbThetaAt *= 3.0/4.0;
                self.m_inGreen = int ( 255 * dbNormAt * mt.cos(dbThetaAt) )
                self.m_inBlue = int ( 255 * dbNormAt * mt.sin(dbThetaAt) )
                #m_inRed = 255;
                #m_inBlue = 255;

    def GetFltColor(self, cplxAg):
        self.__setColor(cplxAg)
        return ( self.m_inRed/255.0, self.m_inGreen/255.0, self.m_inBlue/255.0 )

    def GetIntColor(self, cplxAg):
        self.__setColor(cplxAg)
        return ( self.m_inRed, self.m_inGreen, self.m_inBlue )

"""'
N = 300
if __name__ == "__main__":
    import Image as Im

    imAt = Im.new('RGB', (N,N))

    clAt = sf.ClCplxColor(dbBoundary =  0.6, dbLimit = 1.5)

    for  index, tplZ in zip(sf.mrng(N,N), sf.masq([-1.0, N, 2.0/N],[-1.0, N, 2.0/N]) ):
        i,j = index
        dbCplxAt = tplZ[0]+tplZ[1]*1.0j
        imAt.putpixel( (i,j), clAt.GetIntColor(dbCplxAt) )

    imAt.save('test.jpg')
'"""
__clStt = ClCplxColor()
def cplx2RGB(cplxAg):
    """' convert complex value to kkRGB tuple
        if cplxAg == 0 then retunr (0,0,0)
    '"""
    # added 11y06m14d
    absAt = abs(cplxAg)
    if absAt == 0:
        return (0,0,0)
    return __clStt.GetFltColor(0.9999999*cplxAg/absAt)

def render2dRGB(mtrxAg, boundary=1.0, limit=None, blReverse=False, blBoth=False
    , fileName="kkRGB", blDisplay=True, blMax=False):
    """' Render a complex value distribution with kkRGB color for matrix argument
rendered figure is saved at kkRGB.jpg file as a default
    if limit == None:default value then we set limit = 10*boundary.

    e.g.
vc=klsp(-3,3,300); f=`X^3+`X^2+`X+1; dct={};for idx,(x,y) in enmitr(vc,vc):dct[idx]=f(x+`i y); render2dRGB(dct)
    '"""
    vs = sf.vs_()

    if isinstance(mtrxAg, dict):
        lstAt = mtrxAg.keys()
        lstAt.sort()
        shapeAt = lstAt[-1]
        shapeAt = (shapeAt[0]+1, shapeAt[1]+1)
        assert shapeAt[0]*shapeAt[1] == len(lstAt),\
            "dictionary mtrxAg index is not alined" + str(objarAg)

    else:
        #if isinstance(mtrxAg, (list, tuple)) or hasattr(mtrxAg, '__iter__'):
        # We don't support krry(multipleIterator) yet
        if isinstance(mtrxAg, (list, tuple)):
            mtrxAg = sf.krry(mtrxAg)

        shapeAt = vs.shape(mtrxAg)
        assert len(shapeAt) > 0, \
                "render2dRGB(mtrxAg,..) argements error." + str(mtrxAg)

    if limit == None:
        limit = 10*boundary

    clAt = ClCplxColor(dbBoundary = float(boundary), dbLimit = float(limit) )
    clReverseAt = ClCplxColor(dbBoundary = 1/float(limit), dbLimit = 1/float(boundary) )

    if blBoth == True:
        blReverse = True
    
    shapeAt = list(shapeAt)
    shapeAt.reverse()

    import platform as md;
    if md.system() == "Windows":
        import Image as Im
    else:
        from PIL import Image as Im
    imAt = Im.new('RGB', shapeAt)
    if blReverse == True:
        imReverseAt = Im.new('RGB', shapeAt)
        
    indxMax = None
    flMax = 0.0
    cplxMax = 0+0j

    #dbgLst = [200,200]
    for  index in sf.mrng(*shapeAt):
        #if index == tuple(dbgLst):
        #    import pdb; pdb.set_trace()
        # same distribution with renderMtCmplx(..)
        z=mtrxAg[index[0],index[1]]
        flAt = abs(z)
        if ( flAt > flMax ):
            flMax = flAt
            indxMax = index
            cplxMax = z
        
        imAt.putpixel( index, clAt.GetIntColor(z) )
        if blReverse == True:
            if z != 0:
                imReverseAt.putpixel( index, clReverseAt.GetIntColor(1.0/z) )

    if blMax == True:
        print "max index:", indxMax
        print "max value:", cplxMax

    if not('.' in fileName):
        fileName += ".jpg"
        
    imAt.save(fileName)
    if blReverse == True:
        imReverseAt.save("r"+fileName)

    if blDisplay==True:
        import os   # OK
        if ( blReverse == False) or (blBoth == True):
            os.system("start "+fileName)
        if blReverse == True:
            os.system("start "+ "r"+fileName)


def drawAxis( len=1.0, pos = (0,0,0) ):
    """' draw x,y,z axis with red, green blue arrows '"""
    vs = sf.vs_()

    vs.curve( pos=[pos, (len,0,0)]
            ,  color=(1,0,0)
            , radius = 0.05*len )
    vs.curve( pos=[pos, (0,len,0)]
            ,  color=(0,1,0)
            , radius = 0.05*len )
    vs.curve( pos=[pos, (0,0,len)]
            ,  color=(0,1,1)
            , radius = 0.05*len )

    """'
    vs.arrow(pos=pos, axis=(len,0,0), shaftwidth=0.1*len, color=red)
    vs.arrow(pos=pos, axis=(0,len,0), shaftwidth=0.1*len, color=green)
    vs.arrow(pos=pos, axis=(0,0,len), shaftwidth=0.1*len, color=blue)
    '"""

__tplLstMinMax_renderMtCplx=([],[])
def renderMtCplx(mtCplxAg, blMesh = False, blAxes=True, meshColor = sf.white
        , blDisplayMinMaxLabel = False, xyRatio = 1.0, blDirection = True):

    vs = sf.vs_()

    if isinstance(mtCplxAg, (list,tuple) ):
        assert sf.sc.iscomplexobj(mtCplxAg)
        mtCplxAg = sf.ClTensor(mtCplxAg, dtype=complex)

    if isinstance(mtCplxAg, dict):
        lstAt = mtCplxAg.keys()
        lstAt.sort()
        shapeAt = lstAt[-1]
        shapeAt = (shapeAt[0]+1, shapeAt[1]+1)
        assert shapeAt[0]*shapeAt[1] == len(lstAt),\
            "dictionary mtCplxAg index is not alined" + str(mtCplxAg)
        assert sf.sc.iscomplexobj(mtCplxAg.values()),\
             "Not complex matrix at renderMtCplxWithRGB(.)"

    else:
        shapeAt = vs.shape(mtCplxAg)
        assert len(shapeAt) > 0, \
            "renderMtCplx(mtCplxAg,..) argements error." + str(mtCplxAg)
        assert sf.sc.iscomplexobj(mtCplxAg),\
             "Not complex matrix at renderMtCplx(.)"

    rwLenAt = shapeAt[1]
    clLenAt = shapeAt[0]
    rwfLenAt = shapeAt[1]*1.0   # make float to avoid warning
    clfLenAt = shapeAt[0]*float(xyRatio)

    clAt = ClCplxColor()
    dctAt = {}
    for i,j in sf.mrng(clLenAt, rwLenAt):
        cplxAt = mtCplxAg[i,j]
        if cplxAt == 0+0j:
            phaseAt = 0+0j
        else:
            # use 0.999 to avoid abs(pahseAt) == dbBoundary
            phaseAt = 0.999*cplxAt/abs(cplxAt) 

        dctAt[i,j] = [ (i/clfLenAt,j/rwfLenAt, abs(cplxAt) )
                         , clAt.GetFltColor(phaseAt) ]

    #sf.putPv(dctAt,'dctAt') # to debug

    radiusAt = 1.0/140.0
    if blAxes == True:
        a = vs.curve( pos=[(0,0,0), (1,0,0)],  color=vs.crayola.red
                , radius = radiusAt*1.1 )
        b = vs.curve( pos=[(0,0,0), (0,1,0)],  color=vs.crayola.green
                , radius = radiusAt*1.1 )

    minAt = dctAt[0,0][0][2]
    minIndexAt = (0,0)
    maxAt = dctAt[0,0][0][2]
    maxIndexAt = (0,0)
    for index in sf.mrng( shapeAt[0],shapeAt[1]):
        valAt = dctAt[index][0][2]
        if minAt > valAt:
            minAt = valAt
            minIndexAt = index
        if maxAt < valAt:
            maxAt = valAt
            maxIndexAt = index

    print "index:"+str(
            maxIndexAt) + "  max:"+'% 6g  :'%maxAt,mtCplxAg[maxIndexAt]
    print "index:"+str(
            minIndexAt) + "  min:"+'% 6g  :'%minAt,mtCplxAg[minIndexAt]

    if __tplLstMinMax_renderMtCplx[0]==[]:
        __tplLstMinMax_renderMtCplx[0].append(minAt)
        __tplLstMinMax_renderMtCplx[1].append(maxAt)
        minAt = min(__tplLstMinMax_renderMtCplx[0])
        maxAt = max(__tplLstMinMax_renderMtCplx[1])
    else:
        vs.scene.autoscale = False
        minAt = __tplLstMinMax_renderMtCplx[0][0]
        maxAt = __tplLstMinMax_renderMtCplx[1][0]

    #import pdb; pdb.set_trace()
    if (maxAt >0) and (minAt < 0):
        hRateAt = 1.0/(maxAt - minAt)
        centerHightAt = hRateAt*(maxAt + minAt)/2.0
    elif (maxAt >0) and (minAt >= 0):
        hRateAt = 1.0/maxAt
        centerHightAt = hRateAt*(maxAt)/2
        minAt = 0
    elif minAt < 0:
        hRateAt = 1.0/(-minAt)
        centerHightAt = hRateAt*(minAt)/2
        maxAt = 0
    else:
        assert minAt == maxAt == 0
        hRateAt = 1.0
        centerHightAt = 1.0

    vs.scene.up=(0,0,1)
    #vs.scene.center = [1.0/2.0,                1.0/2.0, centerHightAt]
    vs.scene.center = [1.0/2.0, (rwLenAt/clfLenAt)/2.0, centerHightAt]
    vs.scene.forward=(-1,+1,-1)
    vs.scene.up=(0,0,1)

    if blAxes == True:
        c = vs.curve( pos=[(0,0,minAt*hRateAt), (0,0,maxAt*hRateAt)]
                ,  color=(0,1,1)
                , radius = radiusAt*1.1 )

    if blMesh:
        lstCurveY = [vs.curve(pos =[], color=meshColor)
                for y in range(shapeAt[0]) ]
        lstCurveX = [vs.curve( pos =[], color=meshColor)
                for x in range(shapeAt[1]) ]
        for inY in range(shapeAt[0]):
            for inX in range(shapeAt[1]):
                #lstCurveY[inY].append(dctAt[inY,inX][0])
                tplAt = ( dctAt[inY,inX][0][0], dctAt[inY,inX][0][1]
                        , dctAt[inY,inX][0][2]*hRateAt )
                lstCurveY[inY].append(tplAt)

        for inX in range(shapeAt[1]):
            #import pdb; pdb.set_trace()
            for inY in range(shapeAt[0]):
                #lstCurveX[inX].append(dctAt[inY,inX][0])
                tplAt = ( dctAt[inY,inX][0][0], dctAt[inY,inX][0][1]
                        , dctAt[inY,inX][0][2]*hRateAt )
                lstCurveX[inX].append(tplAt)

    vs.sphere(pos = (maxIndexAt[0]/clfLenAt, maxIndexAt[1]/rwfLenAt
                    ,  maxAt*hRateAt)
            , radius = 0.018, color = vs.color.red)
    vs.sphere(pos = (minIndexAt[0]/clfLenAt, minIndexAt[1]/rwfLenAt
                    , minAt*hRateAt)
            , radius = 0.018, color = vs.color.green)
    if blDisplayMinMaxLabel == True:
        vs.label(pos=(maxIndexAt[0]/clfLenAt, maxIndexAt[1]/rwfLenAt
                     ,  maxAt*hRateAt)
                , text='max:'+ '%6g'%maxAt, xoffset=0, yoffset=20
                , height=20, border=5)
        vs.label(pos=(minIndexAt[0]/clfLenAt, minIndexAt[1]/rwfLenAt
                    , minAt*hRateAt)
                , text='min:'+ '%6g'%minAt, xoffset=-20, yoffset=-20
                , height=20, border=5)

    # clLenAt-1,rwLenAt-1 は両端を除くこと
    # (clLenAt-1)*2
    # (rwLenAt-1)の後の *2 は三角形が裏面にも作られること
    # 最後の *3 は三角形の三つの頂点を意味します
    modelAt = vs.faces(
        pos = vs.zeros( ( (clLenAt-1)*2*(rwLenAt-1)*2*3,3 ), sf.vs_Float ))
    modelAt.normal = [ [0,0,0] ]*len(modelAt.pos)
    modelAt.color = [ [0,0,0] ]* len(modelAt.pos)
    for colAt in range(clLenAt-1):
        for rowAt in range(rwLenAt-1):
            # [col,row]+(0,0), (0,1), (1,1) の三角形の位置を指定します
            modelAt.pos[colAt*2*(rwLenAt-1)*2*3 + 2*2*3*rowAt     ,0:3] = [
                    dctAt[colAt, rowAt][0][0], dctAt[colAt, rowAt][0][1],
                    dctAt[colAt, rowAt][0][2]*hRateAt ]
            modelAt.pos[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt +  1,0:3] = [
                    dctAt[colAt,rowAt+1][0][0], dctAt[colAt,rowAt+1][0][1],
                    dctAt[colAt,rowAt+1][0][2]*hRateAt ]
            modelAt.pos[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt +  2,0:3] = [
                    dctAt[colAt+1,rowAt+1][0][0],dctAt[colAt+1,rowAt+1][0][1],
                    dctAt[colAt+1,rowAt+1][0][2]*hRateAt ]

            # [col,row]+(0,0), (0,1), (1,1) の三角形の色を指定します
            modelAt.color[colAt*2*(rwLenAt-1)*2*3 + 2*2*3*rowAt     ,0:3] = [
                    dctAt[colAt, rowAt][1][0], dctAt[colAt, rowAt][1][1],
                    dctAt[colAt, rowAt][1][2] ]
            modelAt.color[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt +  1,0:3]=[
                    dctAt[colAt,rowAt+1][1][0], dctAt[colAt,rowAt+1][1][1],
                    dctAt[colAt,rowAt+1][1][2] ]
            modelAt.color[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt +  2,0:3]=[
                    dctAt[colAt+1,rowAt+1][1][0],dctAt[colAt+1,rowAt+1][1][1],
                    dctAt[colAt+1,rowAt+1][1][2] ]

            if blDirection == True:
                dbDirection = -1.0
            else:
                dbDirection = +1.0
            
            """'
            # this continuous normal vector results slightly spoted areas
            modelAt.normal[colAt*2*(shapeAt[1]-1)*2*3
                         + 2*2*3*rowAt:colAt*2*(shapeAt[1]-1)*2*3
                         + 2*2*3*rowAt+3, 0:3] = dbDirection*vs.norm(vs.cross( 
                                    vs.array(dctAt[colAt+1,rowAt+1][0]) 
                                            - vs.array(dctAt[colAt,rowAt][0]),
                                    vs.array(dctAt[colAt  ,rowAt+1][0]) 
                                            - vs.array(dctAt[colAt,rowAt][0])
                                             ))
            '"""
            modelAt.normal[colAt*2*(shapeAt[1]-1)*2*3
                         + 2*2*3*rowAt:colAt*2*(shapeAt[1]-1)*2*3
                         + 2*2*3*rowAt+3, 0:3] = [
                                    [dbDirection,dbDirection,dbDirection]]*3

            """'
            # to debug
            if colAt == 10:
                print               dbDirection*vs.norm(vs.cross( 
                                    vs.array(dctAt[colAt+1,rowAt+1][0]) 
                                            - vs.array(dctAt[colAt,rowAt][0]),
                                    vs.array(dctAt[colAt  ,rowAt+1][0]) 
                                            - vs.array(dctAt[colAt,rowAt][0])
                                             ))
            '"""


            # [col,row]+(0,0), (1,1), (1,0) の三角形の位置を指定します
            modelAt.pos[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt +  3, 0:3] =[
                    dctAt[colAt, rowAt][0][0],dctAt[colAt, rowAt][0][1],
                    dctAt[colAt, rowAt][0][2]*hRateAt ]
            modelAt.pos[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt +  4, 0:3] =[
                    dctAt[colAt+1,rowAt+1][0][0], dctAt[colAt+1,rowAt+1][0][1],
                    dctAt[colAt+1,rowAt+1][0][2]*hRateAt ]
            modelAt.pos[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt +  5, 0:3] =[
                     dctAt[colAt+1,rowAt][0][0], dctAt[colAt+1,rowAt][0][1],
                     dctAt[colAt+1,rowAt][0][2]*hRateAt ]

            # [col,row]+(0,0), (1,1), (1,0) の三角形の色を指定します
            modelAt.color[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt + 3, 0:3]=[
                    dctAt[colAt, rowAt][1][0],dctAt[colAt, rowAt][1][1],
                    dctAt[colAt, rowAt][1][2] ]
            modelAt.color[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt + 4, 0:3]=[
                    dctAt[colAt+1,rowAt+1][1][0], dctAt[colAt+1,rowAt+1][1][1],
                    dctAt[colAt+1,rowAt+1][1][2] ]
            modelAt.color[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt + 5, 0:3]=[
                     dctAt[colAt+1,rowAt][1][0], dctAt[colAt+1,rowAt][1][1],
                     dctAt[colAt+1,rowAt][1][2] ]

            """'
            modelAt.normal[colAt*2*(shapeAt[1]-1)*2*3 +2*2*3*rowAt+3:colAt*2*(
                    shapeAt[1]-1)*2*3\
                    + 2*2*3*rowAt+6, 0:3] =  dbDirection*vs.cross( 
                                    vs.array(dctAt[colAt+1  ,rowAt][0])
                                            - vs.array(dctAt[colAt,rowAt][0]),
                                    vs.array(dctAt[colAt+1,rowAt+1][0]) 
                                            - vs.array(dctAt[colAt,rowAt][0]) 
                                             )
            '"""
            modelAt.normal[colAt*2*(shapeAt[1]-1)*2*3 +2*2*3*rowAt+3:colAt*2*(
                    shapeAt[1]-1)*2*3\
                    + 2*2*3*rowAt+6, 0:3] =  [
                                    [dbDirection,dbDirection,dbDirection]]*3



            #if colAt==15 and rowAt == 3:    # to debug
            #    import pdb; pdb.set_trace()

            # print back surface 裏側の三角形を張り合わせないと、反対面の表示を
            # しなくなる。ただし反対面なので [col,row]+(0,0), (1,1), (0,1) の順
            # 序です
            modelAt.pos[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt +  6,0:3] = [
                    dctAt[colAt, rowAt][0][0], dctAt[colAt, rowAt][0][1],
                    dctAt[colAt, rowAt][0][2]*hRateAt ]
            modelAt.pos[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt +  7,0:3] = [
                    dctAt[colAt+1,rowAt+1][0][0], dctAt[colAt+1,rowAt+1][0][1],
                    dctAt[colAt+1,rowAt+1][0][2]*hRateAt ]
            modelAt.pos[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt +  8,0:3] = [
                    dctAt[colAt,rowAt+1][0][0], dctAt[colAt,rowAt+1][0][1],
                    dctAt[colAt,rowAt+1][0][2]*hRateAt ]

            modelAt.color[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt + 6,0:3] =[
                    dctAt[colAt, rowAt][1][0], dctAt[colAt, rowAt][1][1],
                    dctAt[colAt, rowAt][1][2] ]
            modelAt.color[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt + 7,0:3] =[
                    dctAt[colAt+1,rowAt+1][1][0], dctAt[colAt+1,rowAt+1][1][1],
                    dctAt[colAt+1,rowAt+1][1][2] ]
            modelAt.color[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt + 8,0:3] =[
                    dctAt[colAt,rowAt+1][1][0], dctAt[colAt,rowAt+1][1][1],
                    dctAt[colAt,rowAt+1][1][2] ]

            """'
            modelAt.normal[colAt*2*(shapeAt[1]-1)*2*3 +2*2*3*rowAt+6:colAt*2*(
                    shapeAt[1]-1)*2*3\
                    + 2*2*3*rowAt+9, 0:3] = vc= dbDirection*vs.norm(vs.cross( 
                                    vs.array(dctAt[colAt  ,rowAt+1][0])
                                            - vs.array(dctAt[colAt,rowAt][0]),
                                    vs.array(dctAt[colAt+1,rowAt+1][0])
                                            - vs.array(dctAt[colAt,rowAt][0])
                                             ))
            # to debug
            #if colAt in (14,15,16) and rowAt in (2,3,4):
            #    print "colAt,rowAt:",(colAt,rowAt)
            #    print vc
            '"""

            modelAt.normal[colAt*2*(shapeAt[1]-1)*2*3 +2*2*3*rowAt+6:colAt*2*(
                    shapeAt[1]-1)*2*3\
                    + 2*2*3*rowAt+9, 0:3] =  [
                                    [-dbDirection,-dbDirection,-dbDirection]]*3


            # ただし反対面なので [col,row]+(0,0), (1,0), (1,1) の順序です
            # 位置
            modelAt.pos[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt +  9, 0:3] =[
                    dctAt[colAt, rowAt][0][0], dctAt[colAt, rowAt][0][1],
                    dctAt[colAt, rowAt][0][2]*hRateAt ]
            modelAt.pos[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt + 10, 0:3] =[
                    dctAt[colAt+1,rowAt][0][0], dctAt[colAt+1,rowAt][0][1],
                    dctAt[colAt+1,rowAt][0][2]*hRateAt ]
            modelAt.pos[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt + 11, 0:3] =[
                    dctAt[colAt+1,rowAt+1][0][0], dctAt[colAt+1,rowAt+1][0][1],
                    dctAt[colAt+1,rowAt+1][0][2]*hRateAt ]

            # 色
            modelAt.color[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt + 9, 0:3]=[
                    dctAt[colAt, rowAt][1][0], dctAt[colAt, rowAt][1][1],
                    dctAt[colAt, rowAt][1][2] ]
            modelAt.color[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt +10, 0:3]=[
                    dctAt[colAt+1,rowAt][1][0], dctAt[colAt+1,rowAt][1][1],
                    dctAt[colAt+1,rowAt][1][2] ]
            modelAt.color[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt +11, 0:3]=[
                    dctAt[colAt+1,rowAt+1][1][0], dctAt[colAt+1,rowAt+1][1][1],
                    dctAt[colAt+1,rowAt+1][1][2] ]

            """'
            modelAt.normal[colAt*2*(shapeAt[1]-1)*2*3 +2*2*3*rowAt+9:colAt*2*(
                    shapeAt[1]-1)*2*3\
                    + 2*2*3*rowAt+12, 0:3] =  dbDirection*vs.cross( 
                                vs.array(dctAt[colAt+1,rowAt+1][0]) 
                                        - vs.array(dctAt[colAt,rowAt][0]),
                                vs.array(dctAt[colAt+1,rowAt  ][0])
                                        - vs.array(dctAt[colAt,rowAt][0])
                                              )
            '"""
            modelAt.normal[colAt*2*(shapeAt[1]-1)*2*3 +2*2*3*rowAt+9:colAt*2*(
                    shapeAt[1]-1)*2*3\
                    + 2*2*3*rowAt+12, 0:3] =  [
                                [-dbDirection,-dbDirection,-dbDirection]]*3
    return modelAt

"""'

'"""

def renderMtCplxWithRGB(mtCplxAg, blMesh = False, meshColor = sf.white
            , frame = None, blDirection = True):
    """This cods is obsolete. use the renderMtCplx(..)

        Render Commplex Matrix with RGB
    argument obArAg must be 2 dimention array or dictionary array
    with complex value
    
    mtCplxAg[i,j] 要素は 複素数値です

    return visual python object that is rendered as surface

    Use as renderMtCplxWithRGB( mtAg, True)

    We assumed that mtCplxAg is dict or numarray.array which index is aligned
    from 0 to maximum index number.
            
    """
    vs = sf.vs_()

    if isinstance(mtCplxAg, (list,tuple) ):
        assert sf.sc.iscomplexobj(mtCplxAg)
        mtCplxAg = sf.ClTensor(mtCplxAg, dtype=complex)

    if isinstance(mtCplxAg, dict):
        lstAt = mtCplxAg.keys()
        lstAt.sort()
        shapeAt = lstAt[-1]
        shapeAt = (shapeAt[0]+1, shapeAt[1]+1)
        assert shapeAt[0]*shapeAt[1] == len(lstAt),\
            "dictionary mtCplxAg index is not alined" + str(mtCplxAg)
        assert sf.sc.iscomplexobj(mtCplxAg.values()),\
             "Not complex matrix at renderMtCplxWithRGB(.)"

    else:
        shapeAt = vs.shape(mtCplxAg)
        assert len(shapeAt) > 0, \
            "renderMtCplxWithRGB(mtCplxAg,..) argements error." + str(mtCplxAg)
        assert sf.sc.iscomplexobj(mtCplxAg),\
             "Not complex matrix at renderMtCplxWithRGB(.)"

    #print "debug shapeAt:",shapeAt
    rwLenAt = shapeAt[1]
    clLenAt = shapeAt[0]
    rwfLenAt = shapeAt[1]*1.0   # make float to avoid warning
    clfLenAt = shapeAt[0]*1.0
    
    assert( len(shapeAt) == 2)

    clAt = ClCplxColor()
    dctAt = {}
    for i,j in sf.mrng(clLenAt, rwLenAt):
        cplxAt = mtCplxAg[i,j]
        if cplxAt == 0+0j:
            phaseAt = 0+0j
        else:
            # use 0.999 to avoid abs(pahseAt) == dbBoundary
            phaseAt = 0.999*cplxAt/abs(cplxAt) 

        dctAt[i,j] = [ (i/clfLenAt,j/rwfLenAt, abs(cplxAt) )
                         , clAt.GetFltColor(phaseAt) ]

    minAt = dctAt[0,0][0][2]
    minIndexAt = (0,0)
    maxAt = dctAt[0,0][0][2]
    maxIndexAt = (0,0)
    for index in sf.mrng( shapeAt[0],shapeAt[1]):
        valAt = dctAt[index][0][2]
        if minAt > valAt:
            minAt = valAt
            minIndexAt = index
        if maxAt < valAt:
            maxAt = valAt
            maxIndexAt = index

    print "index:"+str(
            maxIndexAt) + "  max:"+'% 6g  :'%maxAt,mtCplxAg[maxIndexAt]
    print "index:"+str(
            minIndexAt) + "  min:"+'% 6g  :'%minAt,mtCplxAg[minIndexAt]

    """'
    __tplLstMinMax_plot3dRowCol[0].append(minAt)
    __tplLstMinMax_plot3dRowCol[1].append(maxAt)
    minAt = min(__tplLstMinMax_plot3dRowCol[0])
    maxAt = max(__tplLstMinMax_plot3dRowCol[1])
    '"""
    
    #import pdb; pdb.set_trace()
    if (maxAt >0) and (minAt < 0):
        hRateAt = 1.0/(maxAt - minAt)
        centerHightAt = hRateAt*(maxAt + minAt)/2.0
    elif (maxAt >0) and (minAt >= 0):
        hRateAt = 1.0/maxAt
        centerHightAt = hRateAt*(maxAt)/2
        minAt = 0
    elif minAt < 0:
        hRateAt = 1.0/(-minAt)
        centerHightAt = hRateAt*(minAt)/2
        maxAt = 0
    else:
        assert minAt == maxAt == 0
        hRateAt = 1.0
        centerHightAt = 1.0

    vs.scene.forward=(-1,+1,-1)
    vs.scene.up=(0,0,1)
    #vs.scene.center = [1.0/2.0, (rwLenAt/clfLenAt)/2.0, centerHightAt]
    vs.scene.center = [1.0/2.0,                1.0/2.0, centerHightAt]

    if blMesh:
        lstCurveY = [vs.curve(frame = frame, pos =[], color=meshColor)
                for y in range(shapeAt[0]) ]
        lstCurveX = [vs.curve(frame = frame, pos =[], color=meshColor)
                for x in range(shapeAt[1]) ]
        for inY in range(shapeAt[0]):
            for inX in range(shapeAt[1]):
                #lstCurveY[inY].append(dctAt[inY,inX][0])
                tplAt = ( dctAt[inY,inX][0][0], dctAt[inY,inX][0][1]
                        , dctAt[inY,inX][0][2]*hRateAt )
                lstCurveY[inY].append(tplAt)

        for inX in range(shapeAt[1]):
            #import pdb; pdb.set_trace()
            for inY in range(shapeAt[0]):
                #lstCurveX[inX].append(dctAt[inY,inX][0])
                tplAt = ( dctAt[inY,inX][0][0], dctAt[inY,inX][0][1]
                        , dctAt[inY,inX][0][2]*hRateAt )
                lstCurveX[inX].append(tplAt)


    modelAt = vs.faces( frame = frame
            , pos = vs.zeros( ( (clLenAt-1)*2*(rwLenAt-1)*2*3,3 ), sf.vs_Float ))
    modelAt.normal = [ [0,0,0] ]*len(modelAt.pos)
    modelAt.color = [ [0,0,0] ]* len(modelAt.pos)
    for colAt in range(clLenAt-1):
        for rowAt in range(rwLenAt-1):
            # [col,row]+(0,0), (0,1), (1,1) の三角形の位置を指定します
            modelAt.pos[colAt*2*(rwLenAt-1)*2*3 + 2*2*3*rowAt     ,0:3] = [
                    dctAt[colAt, rowAt][0][0], dctAt[colAt, rowAt][0][1],
                    dctAt[colAt, rowAt][0][2]*hRateAt ]
            modelAt.pos[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt +  1,0:3] = [
                    dctAt[colAt,rowAt+1][0][0], dctAt[colAt,rowAt+1][0][1],
                    dctAt[colAt,rowAt+1][0][2]*hRateAt ]
            modelAt.pos[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt +  2,0:3] = [
                    dctAt[colAt+1,rowAt+1][0][0],dctAt[colAt+1,rowAt+1][0][1],
                    dctAt[colAt+1,rowAt+1][0][2]*hRateAt ]

            # [col,row]+(0,0), (0,1), (1,1) の三角形の色を指定します
            modelAt.color[colAt*2*(rwLenAt-1)*2*3 + 2*2*3*rowAt     ,0:3] = [
                    dctAt[colAt, rowAt][1][0], dctAt[colAt, rowAt][1][1],
                    dctAt[colAt, rowAt][1][2] ]
            modelAt.color[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt +  1,0:3] = [
                    dctAt[colAt,rowAt+1][1][0], dctAt[colAt,rowAt+1][1][1],
                    dctAt[colAt,rowAt+1][1][2] ]
            modelAt.color[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt +  2,0:3] = [
                    dctAt[colAt+1,rowAt+1][1][0],dctAt[colAt+1,rowAt+1][1][1],
                    dctAt[colAt+1,rowAt+1][1][2] ]

            #import pdb; pdb.set_trace()
            #print "colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt:", colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt
            #modelAt.normal[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt:colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt+12, 0:3] = [ [[1,1,1]]*3 ]*12
            #import pdb; pdb.set_trace()
            if blDirection == True:
                dbDirection = -1.0
            else:
                dbDirection = +1.0
            
            modelAt.normal[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt:colAt*2*(shapeAt[1]-1)*2*3\
                     + 2*2*3*rowAt+3, 0:3] = dbDirection*vs.cross( 
                                    vs.array(dctAt[colAt+1,rowAt+1][0]) 
                                            - vs.array(dctAt[colAt,rowAt][0]),
                                    vs.array(dctAt[colAt  ,rowAt+1][0]) 
                                            - vs.array(dctAt[colAt,rowAt][0])
                                             )


            # [col,row]+(0,0), (1,1), (1,0) の三角形の位置を指定します
            modelAt.pos[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt +  3, 0:3] = [
                    dctAt[colAt, rowAt][0][0],dctAt[colAt, rowAt][0][1],
                    dctAt[colAt, rowAt][0][2]*hRateAt ]
            modelAt.pos[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt +  4, 0:3] = [
                    dctAt[colAt+1,rowAt+1][0][0], dctAt[colAt+1,rowAt+1][0][1],
                    dctAt[colAt+1,rowAt+1][0][2]*hRateAt ]
            modelAt.pos[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt +  5, 0:3] = [
                     dctAt[colAt+1,rowAt][0][0], dctAt[colAt+1,rowAt][0][1],
                     dctAt[colAt+1,rowAt][0][2]*hRateAt ]

            # [col,row]+(0,0), (1,1), (1,0) の三角形の色を指定します
            modelAt.color[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt +  3, 0:3]= [
                    dctAt[colAt, rowAt][1][0],dctAt[colAt, rowAt][1][1],
                    dctAt[colAt, rowAt][1][2] ]
            modelAt.color[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt +  4, 0:3]= [
                    dctAt[colAt+1,rowAt+1][1][0], dctAt[colAt+1,rowAt+1][1][1],
                    dctAt[colAt+1,rowAt+1][1][2] ]
            modelAt.color[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt +  5, 0:3]= [
                     dctAt[colAt+1,rowAt][1][0], dctAt[colAt+1,rowAt][1][1],
                     dctAt[colAt+1,rowAt][1][2] ]

            modelAt.normal[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt+3:colAt*2*(
                    shapeAt[1]-1)*2*3\
                    + 2*2*3*rowAt+6, 0:3] =  dbDirection*vs.cross( 
                                    vs.array(dctAt[colAt+1  ,rowAt][0])
                                            - vs.array(dctAt[colAt,rowAt][0]),
                                    vs.array(dctAt[colAt+1,rowAt+1][0]) 
                                            - vs.array(dctAt[colAt,rowAt][0]) 
                                             )



            # print back surface 裏側の三角形を張り合わせないと、反対面の表示を
            # しなくなる。ただし反対面なので [col,row]+(0,0), (1,1), (0,1) の順序です
            modelAt.pos[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt +  6,0:3] = [
                    dctAt[colAt, rowAt][0][0], dctAt[colAt, rowAt][0][1],
                    dctAt[colAt, rowAt][0][2]*hRateAt ]
            modelAt.pos[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt +  7,0:3] = [
                    dctAt[colAt+1,rowAt+1][0][0], dctAt[colAt+1,rowAt+1][0][1],
                    dctAt[colAt+1,rowAt+1][0][2]*hRateAt ]
            modelAt.pos[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt +  8,0:3] = [
                    dctAt[colAt,rowAt+1][0][0], dctAt[colAt,rowAt+1][0][1],
                    dctAt[colAt,rowAt+1][0][2]*hRateAt ]

            modelAt.color[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt +  6,0:3] = [
                    dctAt[colAt, rowAt][1][0], dctAt[colAt, rowAt][1][1],
                    dctAt[colAt, rowAt][1][2] ]
            modelAt.color[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt +  7,0:3] = [
                    dctAt[colAt+1,rowAt+1][1][0], dctAt[colAt+1,rowAt+1][1][1],
                    dctAt[colAt+1,rowAt+1][1][2] ]
            modelAt.color[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt +  8,0:3] = [
                    dctAt[colAt,rowAt+1][1][0], dctAt[colAt,rowAt+1][1][1],
                    dctAt[colAt,rowAt+1][1][2] ]

            modelAt.normal[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt+6:colAt*2*(
                    shapeAt[1]-1)*2*3\
                    + 2*2*3*rowAt+9, 0:3] =  dbDirection*vs.cross( 
                                    vs.array(dctAt[colAt  ,rowAt+1][0])
                                            - vs.array(dctAt[colAt,rowAt][0]),
                                    vs.array(dctAt[colAt+1,rowAt+1][0])
                                            - vs.array(dctAt[colAt,rowAt][0])
                                             )


            # ただし反対面なので [col,row]+(0,0), (1,0), (1,1) の順序です
            # 位置
            modelAt.pos[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt +  9, 0:3] = [
                    dctAt[colAt, rowAt][0][0], dctAt[colAt, rowAt][0][1],
                    dctAt[colAt, rowAt][0][2]*hRateAt ]
            modelAt.pos[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt + 10, 0:3] = [
                    dctAt[colAt+1,rowAt][0][0], dctAt[colAt+1,rowAt][0][1],
                    dctAt[colAt+1,rowAt][0][2]*hRateAt ]
            modelAt.pos[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt + 11, 0:3] = [
                    dctAt[colAt+1,rowAt+1][0][0], dctAt[colAt+1,rowAt+1][0][1],
                    dctAt[colAt+1,rowAt+1][0][2]*hRateAt ]

            # 色
            modelAt.color[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt +  9, 0:3] = [
                    dctAt[colAt, rowAt][1][0], dctAt[colAt, rowAt][1][1],
                    dctAt[colAt, rowAt][1][2] ]
            modelAt.color[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt + 10, 0:3] = [
                    dctAt[colAt+1,rowAt][1][0], dctAt[colAt+1,rowAt][1][1],
                    dctAt[colAt+1,rowAt][1][2] ]
            modelAt.color[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt + 11, 0:3] = [
                    dctAt[colAt+1,rowAt+1][1][0], dctAt[colAt+1,rowAt+1][1][1],
                    dctAt[colAt+1,rowAt+1][1][2] ]

            modelAt.normal[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt+9:colAt*2*(
                    shapeAt[1]-1)*2*3\
                    + 2*2*3*rowAt+12, 0:3] =  dbDirection*vs.cross( 
                                vs.array(dctAt[colAt+1,rowAt+1][0]) 
                                        - vs.array(dctAt[colAt,rowAt][0]),
                                vs.array(dctAt[colAt+1,rowAt  ][0])
                                        - vs.array(dctAt[colAt,rowAt][0])
                                              )
    return modelAt


def renderFacesWithRGB(obarAg, blMesh = False, meshColor = sf.white
            , frame = None, blDirection = True):
    """argument obArAg must be 2 dimention object array or dictionary array
    with value:obArAg[col,row] == [xPos,yPos,zPos]
    
    obarAg[i,j] の値は [sqPos, sqColor] のような position sequence と color sequence 
    二つの要素からなる sequence とする。0 番目の要素が position とする
    
    return visual python object that is rendered as surface

    Use as renderFacesWithRGB( objArAg, True)

    We assumed that obarAg is dict or numarray.ObjectArray which index is aligned
    from 0 to maximum index number.
            
    """

    vs = sf.vs_()

    if isinstance(obarAg, dict):
        lstAt = obarAg.keys()
        lstAt.sort()
        shapeAt = lstAt[-1]
        shapeAt = (shapeAt[0]+1, shapeAt[1]+1)
        assert shapeAt[0]*shapeAt[1] == len(lstAt),\
            "dictionary obarAg index is not alined" + str(obarAg)

    else:
        shapeAt = vs.shape(obarAg)
        assert len(shapeAt) > 0, \
                "renderFacesWithRGB(obarAg,..) argements error." + str(obarAg)

    rwLenAt = shapeAt[1]
    clLenAt = shapeAt[0]
    rwfLenAt = shapeAt[1]*1.0   # make float to avoid warning
    clfLenAt = shapeAt[0]*1.0
    
    assert( len(shapeAt) == 2)


    vs.scene.forward=(-1,+1,-1)
    vs.scene.up=(0,0,1)
    if blMesh:
        lstCurveY = [vs.curve(frame = frame, pos =[], color=meshColor)
                for y in range(shapeAt[0]) ]
        lstCurveX = [vs.curve(frame = frame, pos =[], color=meshColor)
                for x in range(shapeAt[1]) ]
        for inY in range(shapeAt[0]):
            for inX in range(shapeAt[1]):
                lstCurveY[inY].append(obarAg[inY,inX][0])

        for inX in range(shapeAt[1]):
            #import pdb; pdb.set_trace()
            for inY in range(shapeAt[0]):
                lstCurveX[inX].append(obarAg[inY,inX][0])

    modelAt = vs.faces( frame = frame
            , pos = vs.zeros( ( (clLenAt-1)*2*(rwLenAt-1)*2*3,3 ), sf.vs_Float ))
    modelAt.normal = [ [0,0,0] ]*len(modelAt.pos)
    modelAt.color = [ [0,0,0] ]* len(modelAt.pos)
    for colAt in range(clLenAt-1):
        for rowAt in range(rwLenAt-1):
            # [col,row]+(0,0), (0,1), (1,1) の三角形の位置を指定します
            modelAt.pos[colAt*2*(rwLenAt-1)*2*3 + 2*2*3*rowAt     ,0:3] = [
                    obarAg[colAt, rowAt][0][0], obarAg[colAt, rowAt][0][1],
                    obarAg[colAt, rowAt][0][2] ]
            modelAt.pos[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt +  1,0:3] = [
                    obarAg[colAt,rowAt+1][0][0], obarAg[colAt,rowAt+1][0][1],
                    obarAg[colAt,rowAt+1][0][2] ]
            modelAt.pos[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt +  2,0:3] = [
                    obarAg[colAt+1,rowAt+1][0][0],obarAg[colAt+1,rowAt+1][0][1],
                    obarAg[colAt+1,rowAt+1][0][2] ]

            # [col,row]+(0,0), (0,1), (1,1) の三角形の色を指定します
            modelAt.color[colAt*2*(rwLenAt-1)*2*3 + 2*2*3*rowAt     ,0:3] = [
                    obarAg[colAt, rowAt][1][0], obarAg[colAt, rowAt][1][1],
                    obarAg[colAt, rowAt][1][2] ]
            modelAt.color[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt +  1,0:3] = [
                    obarAg[colAt,rowAt+1][1][0], obarAg[colAt,rowAt+1][1][1],
                    obarAg[colAt,rowAt+1][1][2] ]
            modelAt.color[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt +  2,0:3] = [
                    obarAg[colAt+1,rowAt+1][1][0],obarAg[colAt+1,rowAt+1][1][1],
                    obarAg[colAt+1,rowAt+1][1][2] ]

            #import pdb; pdb.set_trace()
            #print "colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt:", colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt
            #modelAt.normal[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt:colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt+12, 0:3] = [ [[1,1,1]]*3 ]*12
            #import pdb; pdb.set_trace()
            if blDirection == True:
                dbDirection = 1.0
            else:
                dbDirection = -1.0
            
            modelAt.normal[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt:colAt*2*(shapeAt[1]-1)*2*3\
                     + 2*2*3*rowAt+3, 0:3] = dbDirection*vs.cross( 
                        vs.array(obarAg[colAt+1,rowAt+1][0]) - vs.array(obarAg[colAt,rowAt][0]),
                        vs.array(obarAg[colAt  ,rowAt+1][0]) - vs.array(obarAg[colAt,rowAt][0]))


            # [col,row]+(0,0), (1,1), (1,0) の三角形の位置を指定します
            modelAt.pos[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt +  3, 0:3] = [
                    obarAg[colAt, rowAt][0][0],obarAg[colAt, rowAt][0][1],
                    obarAg[colAt, rowAt][0][2] ]
            modelAt.pos[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt +  4, 0:3] = [
                    obarAg[colAt+1,rowAt+1][0][0], obarAg[colAt+1,rowAt+1][0][1],
                    obarAg[colAt+1,rowAt+1][0][2] ]
            modelAt.pos[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt +  5, 0:3] = [
                     obarAg[colAt+1,rowAt][0][0], obarAg[colAt+1,rowAt][0][1],
                     obarAg[colAt+1,rowAt][0][2] ]

            # [col,row]+(0,0), (1,1), (1,0) の三角形の色を指定します
            modelAt.color[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt +  3, 0:3] = [
                    obarAg[colAt, rowAt][1][0],obarAg[colAt, rowAt][1][1],
                    obarAg[colAt, rowAt][1][2] ]
            modelAt.color[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt +  4, 0:3] = [
                    obarAg[colAt+1,rowAt+1][1][0], obarAg[colAt+1,rowAt+1][1][1],
                    obarAg[colAt+1,rowAt+1][1][2] ]
            modelAt.color[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt +  5, 0:3] = [
                     obarAg[colAt+1,rowAt][1][0], obarAg[colAt+1,rowAt][1][1],
                     obarAg[colAt+1,rowAt][1][2] ]

            modelAt.normal[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt+3:colAt*2*(shapeAt[1]-1)*2*3\
                     + 2*2*3*rowAt+6, 0:3] =  dbDirection*vs.cross( 
                        vs.array(obarAg[colAt+1  ,rowAt][0]) - vs.array(obarAg[colAt,rowAt][0]),
                        vs.array(obarAg[colAt+1,rowAt+1][0]) - vs.array(obarAg[colAt,rowAt][0]) )



            # print back surface 裏側の三角形を張り合わせないと、反対面の表示をしなくなる
            # ただし反対面なので [col,row]+(0,0), (1,1), (0,1) の順序です
            modelAt.pos[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt +  6,0:3] = [
                    obarAg[colAt, rowAt][0][0], obarAg[colAt, rowAt][0][1],
                    obarAg[colAt, rowAt][0][2] ]
            modelAt.pos[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt +  7,0:3] = [
                    obarAg[colAt+1,rowAt+1][0][0], obarAg[colAt+1,rowAt+1][0][1],
                    obarAg[colAt+1,rowAt+1][0][2] ]
            modelAt.pos[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt +  8,0:3] = [
                    obarAg[colAt,rowAt+1][0][0], obarAg[colAt,rowAt+1][0][1],
                    obarAg[colAt,rowAt+1][0][2] ]

            modelAt.color[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt +  6,0:3] = [
                    obarAg[colAt, rowAt][1][0], obarAg[colAt, rowAt][1][1],
                    obarAg[colAt, rowAt][1][2] ]
            modelAt.color[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt +  7,0:3] = [
                    obarAg[colAt+1,rowAt+1][1][0], obarAg[colAt+1,rowAt+1][1][1],
                    obarAg[colAt+1,rowAt+1][1][2] ]
            modelAt.color[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt +  8,0:3] = [
                    obarAg[colAt,rowAt+1][1][0], obarAg[colAt,rowAt+1][1][1],
                    obarAg[colAt,rowAt+1][1][2] ]

            modelAt.normal[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt+6:colAt*2*(shapeAt[1]-1)*2*3\
                     + 2*2*3*rowAt+9, 0:3] =  dbDirection*vs.cross( 
                        vs.array(obarAg[colAt  ,rowAt+1][0]) - vs.array(obarAg[colAt,rowAt][0]),
                        vs.array(obarAg[colAt+1,rowAt+1][0]) - vs.array(obarAg[colAt,rowAt][0]))


            # ただし反対面なので [col,row]+(0,0), (1,0), (1,1) の順序です
            # 位置
            modelAt.pos[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt +  9, 0:3] = [
                    obarAg[colAt, rowAt][0][0], obarAg[colAt, rowAt][0][1],
                    obarAg[colAt, rowAt][0][2] ]
            modelAt.pos[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt + 10, 0:3] = [
                    obarAg[colAt+1,rowAt][0][0], obarAg[colAt+1,rowAt][0][1],
                    obarAg[colAt+1,rowAt][0][2] ]
            modelAt.pos[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt + 11, 0:3] = [
                    obarAg[colAt+1,rowAt+1][0][0], obarAg[colAt+1,rowAt+1][0][1],
                    obarAg[colAt+1,rowAt+1][0][2] ]

            # 色
            modelAt.color[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt +  9, 0:3] = [
                    obarAg[colAt, rowAt][1][0], obarAg[colAt, rowAt][1][1],
                    obarAg[colAt, rowAt][1][2] ]
            modelAt.color[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt + 10, 0:3] = [
                    obarAg[colAt+1,rowAt][1][0], obarAg[colAt+1,rowAt][1][1],
                    obarAg[colAt+1,rowAt][1][2] ]
            modelAt.color[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt + 11, 0:3] = [
                    obarAg[colAt+1,rowAt+1][1][0], obarAg[colAt+1,rowAt+1][1][1],
                    obarAg[colAt+1,rowAt+1][1][2] ]

            modelAt.normal[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt+9:colAt*2*(shapeAt[1]-1)*2*3\
                     + 2*2*3*rowAt+12, 0:3] =  dbDirection*vs.cross( 
                        vs.array(obarAg[colAt+1,rowAt+1][0]) - vs.array(obarAg[colAt,rowAt][0]),
                        vs.array(obarAg[colAt+1,rowAt  ][0]) - vs.array(obarAg[colAt,rowAt][0]))
    return modelAt


__tplLstMinMax_renderFaces=([],[])
def renderFaces(obarAg, blMesh = False, colorFace = sf.green,
                 blMeshOnly = False,
                 meshColor = sf.white, frame = None, blDirection = True):
    """argument obarAg must be 2 dimention object array or dictionary array
       in which each elements is a 3D position sequence

        e.g. assert obarAg[0,1] == (xPos, yPos, valueAt_x_y)
    
    return visual python object that is rendered as surface

    Use as renderFaces( obarAg, True, colorFace = vs.colore.blue)

    We assumed that obarAg is dict or numarray.ObjectArray which index is aligned
    from 0 to maximum index number.
            
    """

    vs = sf.vs_()

    if isinstance(obarAg, dict):
        lstAt = obarAg.keys()
        lstAt.sort()
        shapeAt = lstAt[-1]
        shapeAt = (shapeAt[0]+1, shapeAt[1]+1)
        assert shapeAt[0]*shapeAt[1] == len(lstAt),\
            "dictionary mtrxAg index is not alined" + str(obarAg)
        """'
        assert (shapeAt[0]+1)*(shapeAt[1]+1) == len(lstAt),\
            "dictionary obarAg index is not alined" + str(obarAg)
        '"""
    else:
        shapeAt = vs.shape(obarAg)
        assert len(shapeAt) > 0, \
                "makeFaces(obarAg,..) argements error." + str(obarAg)

    rwLenAt = shapeAt[1]
    clLenAt = shapeAt[0]
    
    assert( len(shapeAt) == 2)

    minAt = min(obarAg[0,0])
    minIndexAt = (0,0)
    maxAt = max(obarAg[0,0])
    maxIndexAt = (0,0)
    for index in sf.mrng( shapeAt[0],shapeAt[1]):
        valAt = min(obarAg[index])
        if minAt > valAt:
            minAt = valAt
            minIndexAt = index
        valAt = max(obarAg[index])
        if maxAt < valAt:
            maxAt = valAt
            maxIndexAt = index

    print "index:"+str(
            maxIndexAt) + "  max:"+'% 6g  :'%maxAt,obarAg[maxIndexAt]
    print "index:"+str(
            minIndexAt) + "  min:"+'% 6g  :'%minAt,obarAg[minIndexAt]


    vs.range = max( abs(maxAt), abs(minAt) )
    vs.scene.forward=(-1,+1,-1)
    vs.scene.up=(0,0,1)
    if (blMeshOnly == True):
        blMesh = True

    if blMesh:
        lstCurveY = [vs.curve(frame = frame, pos =[], color=meshColor)
                for y in range(shapeAt[0]) ]
        lstCurveX = [vs.curve(frame = frame, pos =[], color=meshColor)
                for x in range(shapeAt[1]) ]
        for inY in range(shapeAt[0]):
            for inX in range(shapeAt[1]):
                lstCurveY[inY].append(obarAg[inY,inX])

        for inX in range(shapeAt[1]):
            #import pdb; pdb.set_trace()
            for inY in range(shapeAt[0]):
                lstCurveX[inX].append(obarAg[inY,inX])

    if (blMeshOnly == True):
        return

    modelAt = vs.faces( frame = frame
            , pos = vs.zeros( ( (clLenAt-1)*2*(rwLenAt-1)*2*3,3 ), sf.vs_Float ))
    modelAt.normal = [ [0,0,0] ]*len(modelAt.pos)
    modelAt.color = [ colorFace ]* len(modelAt.pos)
    for colAt in range(clLenAt-1):
        for rowAt in range(rwLenAt-1):
            # [col,row]+(0,0), (0,1), (1,1) の三角形の位置を指定します
            modelAt.pos[colAt*2*(rwLenAt-1)*2*3 + 2*2*3*rowAt     ,0:3] = [
                    obarAg[colAt, rowAt][0], obarAg[colAt, rowAt][1],
                    obarAg[colAt, rowAt][2] ]
            modelAt.pos[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt +  1,0:3] = [
                    obarAg[colAt,rowAt+1][0], obarAg[colAt,rowAt+1][1],
                    obarAg[colAt,rowAt+1][2] ]
            modelAt.pos[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt +  2,0:3] = [
                    obarAg[colAt+1,rowAt+1][0],obarAg[colAt+1,rowAt+1][1],
                    obarAg[colAt+1,rowAt+1][2] ]

            #import pdb; pdb.set_trace()
            #print "colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt:", colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt
            #modelAt.normal[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt:colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt+12, 0:3] = [ [[1,1,1]]*3 ]*12
            #import pdb; pdb.set_trace()
            if blDirection == True:
                dbDirection = -1.0
            else:
                dbDirection =  1.0

            modelAt.normal[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt:colAt*2*(shapeAt[1]-1)*2*3\
                     + 2*2*3*rowAt+3, 0:3] = dbDirection*vs.cross( 
                        vs.array(obarAg[colAt+1,rowAt+1]) - vs.array(obarAg[colAt,rowAt]),
                        vs.array(obarAg[colAt  ,rowAt+1]) - vs.array(obarAg[colAt,rowAt]))

            modelAt.pos[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt +  3, 0:3] = [
                    obarAg[colAt, rowAt][0],obarAg[colAt, rowAt][1],
                    obarAg[colAt, rowAt][2] ]
            modelAt.pos[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt +  4, 0:3] = [
                    obarAg[colAt+1,rowAt+1][0], obarAg[colAt+1,rowAt+1][1],
                    obarAg[colAt+1,rowAt+1][2] ]
            modelAt.pos[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt +  5, 0:3] = [
                     obarAg[colAt+1,rowAt][0], obarAg[colAt+1,rowAt][1],
                     obarAg[colAt+1,rowAt][2] ]

            modelAt.normal[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt+3:colAt*2*(shapeAt[1]-1)*2*3\
                     + 2*2*3*rowAt+6, 0:3] =  dbDirection*vs.cross( 
                        vs.array(obarAg[colAt+1  ,rowAt]) - vs.array(obarAg[colAt,rowAt]),
                        vs.array(obarAg[colAt+1,rowAt+1]) - vs.array(obarAg[colAt,rowAt]) )


            # print back surface
            modelAt.pos[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt +  6,0:3] = [
                    obarAg[colAt, rowAt][0], obarAg[colAt, rowAt][1],
                    obarAg[colAt, rowAt][2] ]
            modelAt.pos[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt +  7,0:3] = [
                    obarAg[colAt+1,rowAt+1][0], obarAg[colAt+1,rowAt+1][1],
                    obarAg[colAt+1,rowAt+1][2] ]
            modelAt.pos[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt +  8,0:3] = [
                    obarAg[colAt,rowAt+1][0], obarAg[colAt,rowAt+1][1],
                    obarAg[colAt,rowAt+1][2] ]

            modelAt.normal[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt+6:colAt*2*(shapeAt[1]-1)*2*3\
                     + 2*2*3*rowAt+9, 0:3] =  dbDirection*vs.cross( 
                        vs.array(obarAg[colAt  ,rowAt+1]) - vs.array(obarAg[colAt,rowAt]),
                        vs.array(obarAg[colAt+1,rowAt+1]) - vs.array(obarAg[colAt,rowAt]))


            modelAt.pos[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt +  9, 0:3] = [
                    obarAg[colAt, rowAt][0], obarAg[colAt, rowAt][1],
                    obarAg[colAt, rowAt][2] ]
            modelAt.pos[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt + 10, 0:3] = [
                    obarAg[colAt+1,rowAt][0], obarAg[colAt+1,rowAt][1],
                    obarAg[colAt+1,rowAt][2] ]
            modelAt.pos[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt + 11, 0:3] = [
                    obarAg[colAt+1,rowAt+1][0], obarAg[colAt+1,rowAt+1][1],
                    obarAg[colAt+1,rowAt+1][2] ]

            modelAt.normal[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt+9:colAt*2*(shapeAt[1]-1)*2*3\
                     + 2*2*3*rowAt+12, 0:3] =  dbDirection*vs.cross( 
                        vs.array(obarAg[colAt+1,rowAt+1]) - vs.array(obarAg[colAt,rowAt]),
                        vs.array(obarAg[colAt+1,rowAt  ]) - vs.array(obarAg[colAt,rowAt]))

    return modelAt

__tplLstMinMax_plot3dRowCol=([],[])
def plot3dRowCol(mtrxAg, blMesh = True, blAxes = True, color = sf.blue
        , blDisplayMinMaxLabel = False, xyRatio = 1.0):

    """ obsolete! use plot3dGr(..)
    argument mtrxAg must be 2 dimention array or dictionary


       returned visual object is normalized for axis x:[0,1], axis y:[0,1],
       axis z:[min(mtrxAg)/hRate, max(mtrxAg)/hRate] with hRate = max - min
    """

    vs = sf.vs_()

    if isinstance(mtrxAg, (list,tuple) ):
        assert sf.sc.isrealobj(mtrxAg)
        mtrxAg = sf.ClTensor(mtrxAg, dtype=float)

    if isinstance(mtrxAg, dict):
        lstAt = mtrxAg.keys()
        lstAt.sort()
        shapeAt = lstAt[-1]
        shapeAt = (shapeAt[0]+1, shapeAt[1]+1)
        assert shapeAt[0]*shapeAt[1] == len(lstAt),\
            "dictionary mtrxAg index is not alined" + str(mtrxAg)

        #assert (shapeAt[0]+1)*(shapeAt[1]+1) == len(lstAt),\
        #    "dictionary mtrxAg index is not alined" + str(mtrxAg)
        #"""'
        #'"""

    else:
        shapeAt = vs.shape(mtrxAg)
        assert len(shapeAt) > 0, \
                "plot3dRosCol(mtrxAg,..) argements error." + str(mtrxAg)

    rwLenAt = shapeAt[1]
    clLenAt = shapeAt[0]
    # make float to avoid warning こっちにすると正方形になる
    #rwfLenAt = shapeAt[1]*1.0
    rwfLenAt = shapeAt[0]*1.0   # make float to avoid warning
    clfLenAt = shapeAt[0]*float(xyRatio)
    
    assert( len(shapeAt) == 2)


    radiusAt = 1.0/140.0
    if blAxes == True:
        a = vs.curve( pos=[(0,0,0), (1,0,0)],  color=vs.crayola.red
                , radius = radiusAt*1.1 )
        b = vs.curve( pos=[(0,0,0), (0,1,0)],  color=vs.crayola.green
                , radius = radiusAt*1.1 )

    minAt = mtrxAg[0,0]
    minIndexAt = (0,0)
    maxAt = mtrxAg[0,0]
    maxIndexAt = (0,0)
    for index in sf.mrng( shapeAt[0],shapeAt[1]):
        valAt = mtrxAg[index]
        if minAt > valAt:
            minAt = valAt
            minIndexAt = index
        if maxAt < valAt:
            maxAt = valAt
            maxIndexAt = index

    print "index:"+str(maxIndexAt) + "  max:"+'% 6g'%maxAt
    print "index:"+str(minIndexAt) + "  min:"+'% 6g'%minAt

    # 下は少し変なコードだ。しかし最初に表示したスケールで二回目以降も表示する
    # コードになっている
    # Below is bit weird but it shows a graph with the first scale
    if __tplLstMinMax_plot3dRowCol[0]==[]:
        __tplLstMinMax_plot3dRowCol[0].append(minAt)
        __tplLstMinMax_plot3dRowCol[1].append(maxAt)
        minAt = min(__tplLstMinMax_plot3dRowCol[0])
        maxAt = max(__tplLstMinMax_plot3dRowCol[1])
    else:
        vs.scene.autoscale = False
        minAt = __tplLstMinMax_plot3dRowCol[0][0]
        maxAt = __tplLstMinMax_plot3dRowCol[1][0]

    #import pdb; pdb.set_trace()
    if (maxAt >0) and (minAt < 0):
        hRateAt = 1.0/(maxAt - minAt)
        centerHightAt = hRateAt*(maxAt + minAt)/2.0
    elif (maxAt >0) and (minAt >= 0):
        hRateAt = 1.0/maxAt
        centerHightAt = hRateAt*(maxAt)/2
        minAt = 0
    elif minAt < 0:
        hRateAt = 1.0/(-minAt)
        centerHightAt = hRateAt*(minAt)/2
        maxAt = 0
    else:
        assert minAt == maxAt == 0
        hRateAt = 1.0
        centerHightAt = 1.0

    #vs.scene.center = [1.0/2.0, r1.0/2.0, centerHightAt]
    vs.scene.center = [1.0/2.0, (rwLenAt/clfLenAt)/2.0, centerHightAt]
    vs.scene.forward=(-1,+1,-1)
    vs.scene.up=(0,0,1)

    if blAxes == True:
        c = vs.curve( pos=[(0,0,minAt*hRateAt), (0,0,maxAt*hRateAt)]
                ,  color=(0,1,1)
                , radius = radiusAt*1.1 )

    if blMesh:
        lstCurveY = [vs.curve(pos =[], radius = radiusAt)
                for y in range(shapeAt[0]) ]
        lstCurveX = [vs.curve(pos =[], radius = radiusAt)
                for x in range(shapeAt[1]) ]
        for inY in range(shapeAt[0]):
            for inX in range(shapeAt[1]):
                #import pdb; pdb.set_trace()
                tplAt= (inY/clfLenAt, inX/rwfLenAt, mtrxAg[inY,inX]*hRateAt)
                lstCurveY[inY].append(tplAt)

        for inX in range(shapeAt[1]):
            #import pdb; pdb.set_trace()
            for inY in range(shapeAt[0]):
                tplAt=(inY/clfLenAt, inX/rwfLenAt, mtrxAg[inY,inX]*hRateAt)
                lstCurveX[inX].append(tplAt)

    vs.sphere(pos = (maxIndexAt[0]/clfLenAt, maxIndexAt[1]/rwfLenAt
                    ,  maxAt*hRateAt)
            , radius = 0.018, color = vs.color.red)
    vs.sphere(pos = (minIndexAt[0]/clfLenAt, minIndexAt[1]/rwfLenAt
                    , minAt*hRateAt)
            , radius = 0.018, color = vs.color.green)
    if blDisplayMinMaxLabel == True:
        vs.label(pos=(maxIndexAt[0]/clfLenAt, maxIndexAt[1]/rwfLenAt
                     ,  maxAt*hRateAt)
                , text='max:'+ '%6g'%maxAt, xoffset=0, yoffset=20
                , height=20, border=5)
        vs.label(pos=(minIndexAt[0]/clfLenAt, minIndexAt[1]/rwfLenAt
                    , minAt*hRateAt)
                , text='min:'+ '%6g'%minAt, xoffset=-20, yoffset=-20
                , height=20, border=5)

    # clLenAt-1,rwLenAt-1 は両端を除くこと
    # (clLenAt-1)*2
    # (rwLenAt-1)の後の *2 は三角形が裏面にも作られること
    # 最後の *3 は三角形の三つの頂点を意味します
    modelAt = vs.faces(
        pos = vs.zeros( ( (clLenAt-1)*2*(rwLenAt-1) *2*3,3 ), sf.vs_Float ))
    modelAt.normal = [ [0,0,0] ]*len(modelAt.pos)
    modelAt.color = [ color ]* len(modelAt.pos)
    for colAt in range(clLenAt-1):
        for rowAt in range(rwLenAt-1):
            modelAt.pos[colAt*2*(rwLenAt-1)*2*3 + 2*2*3*rowAt     ,0:3] = [
                    colAt/clfLenAt, rowAt/rwfLenAt
                    , mtrxAg[colAt,rowAt]*hRateAt ]
            modelAt.pos[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt +  2,0:3] = [
                    colAt/clfLenAt, (rowAt+1)/rwfLenAt
                    ,mtrxAg[colAt,rowAt+1]*hRateAt ]
            modelAt.pos[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt +  1,0:3] = [
                    (colAt+1)/clfLenAt, (rowAt+1)/rwfLenAt
                    ,mtrxAg[colAt+1,rowAt+1]*hRateAt ]

            modelAt.normal[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt
                          :colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt+6, 0:3] =[
                          [1,1,1] ]*6

            modelAt.pos[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt +  4, 0:3] =[
                    colAt/clfLenAt, rowAt/rwfLenAt
                    , mtrxAg[colAt, rowAt]*hRateAt ]
            modelAt.pos[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt +  3, 0:3] =[
                    (colAt+1)/clfLenAt, (rowAt+1)/rwfLenAt
                    , mtrxAg[colAt+1,rowAt+1]*hRateAt ]
            modelAt.pos[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt +  5, 0:3] =[
                    (colAt+1)/clfLenAt, rowAt/rwfLenAt
                    , mtrxAg[colAt+1,rowAt]*hRateAt ]


            modelAt.pos[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt +  6,0:3] = [
                    colAt/clfLenAt, rowAt/rwfLenAt
                    , mtrxAg[colAt, rowAt]*hRateAt ]
            modelAt.pos[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt +  8,0:3] = [
                    (colAt+1)/clfLenAt, (rowAt+1)/rwfLenAt
                    , mtrxAg[colAt+1,rowAt+1]*hRateAt ]
            modelAt.pos[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt +  7,0:3] = [
                    colAt/clfLenAt, (rowAt+1)/rwfLenAt
                    , mtrxAg[colAt,rowAt+1]*hRateAt ]

            modelAt.pos[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt +  9, 0:3] =[
                    colAt/clfLenAt, rowAt/rwfLenAt
                    , mtrxAg[colAt, rowAt]*hRateAt ]
            modelAt.pos[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt + 11, 0:3] =[
                    (colAt+1)/clfLenAt, rowAt/rwfLenAt
                    , mtrxAg[colAt+1,rowAt]*hRateAt ]
            modelAt.pos[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt + 10, 0:3] =[
                    (colAt+1)/clfLenAt, (rowAt+1)/rwfLenAt
                    , mtrxAg[colAt+1,rowAt+1]*hRateAt ]

    return modelAt



__tplLstMinMax_plot3d=([],[])
def plot3d(mtrxAg, blMesh = True, blAxes = True, color = sf.blue
        , blDisplayMinMaxLabel = False, xyRatio = 1.0):

    """ obsolete! use plot3dGr(..)
       argument mtrxAg must be 2 dimention array or dictionary

       returned visual object is normalized for axis x:[0,1], axis y:[0,1],
       axis z:[min(mtrxAg)/hRate, max(mtrxAg)/hRate] with hRate = max - min
    """

    vs = sf.vs_()

    if isinstance(mtrxAg, (list,tuple) ):
        assert sf.sc.isrealobj(mtrxAg)
        mtrxAg = sf.ClTensor(mtrxAg, dtype=float)

    if isinstance(mtrxAg, dict):
        lstAt = mtrxAg.keys()
        lstAt.sort()
        shapeAt = lstAt[-1]
        shapeAt = (shapeAt[0]+1, shapeAt[1]+1)
        assert shapeAt[0]*shapeAt[1] == len(lstAt),\
            "dictionary mtrxAg index is not alined" + str(mtrxAg)

        #assert (shapeAt[0]+1)*(shapeAt[1]+1) == len(lstAt),\
        #    "dictionary mtrxAg index is not alined" + str(mtrxAg)
        #"""'
        #'"""

    else:
        shapeAt = vs.shape(mtrxAg)
        assert len(shapeAt) > 0, \
                "plot3d(mtrxAg,..) argements error." + str(mtrxAg)

    rwLenAt = shapeAt[1]
    clLenAt = shapeAt[0]
    #rwfLenAt = shapeAt[1]*1.0   # make float to avoid warning
    rwfLenAt = shapeAt[0]*float(xyRatio)
    clfLenAt = shapeAt[0]*1.0
    
    assert( len(shapeAt) == 2)


    radiusAt = 1.0/140.0
    if blAxes == True:
        a = vs.curve( pos=[(0,0,0), (1,0,0)],  color=vs.crayola.red
                , radius = radiusAt*1.1 )
        b = vs.curve( pos=[(0,0,0), (0,1,0)],  color=vs.crayola.green
                , radius = radiusAt*1.1 )

    minAt = mtrxAg[0,0]
    minIndexAt = (0,0)
    maxAt = mtrxAg[0,0]
    maxIndexAt = (0,0)
    for index in sf.mrng( shapeAt[0],shapeAt[1]):
        valAt = mtrxAg[index]
        if minAt > valAt:
            minAt = valAt
            minIndexAt = index
        if maxAt < valAt:
            maxAt = valAt
            maxIndexAt = index

    print "index:"+str(maxIndexAt) + "  max:"+'% 6g'%maxAt
    print "index:"+str(minIndexAt) + "  min:"+'% 6g'%minAt

    #import pdb; pdb.set_trace()
    if (maxAt >0) and (minAt < 0):
        hRateAt = 1.0/(maxAt - minAt)
        centerHightAt = hRateAt*(maxAt + minAt)/2.0
    elif (maxAt >0) and (minAt >= 0):
        hRateAt = 1.0/maxAt
        centerHightAt = hRateAt*(maxAt)/2
        minAt = 0
    elif minAt < 0:
        hRateAt = 1.0/(-minAt)
        centerHightAt = hRateAt*(minAt)/2
        maxAt = 0
    else:
        assert minAt == maxAt == 0
        hRateAt = 1.0
        centerHightAt = 1.0

    if __tplLstMinMax_plot3d[0] == []:
        __tplLstMinMax_plot3d[0].append(minAt)
        __tplLstMinMax_plot3d[1].append(maxAt)
        minAt = min(__tplLstMinMax_plot3d[0])
        maxAt = max(__tplLstMinMax_plot3d[1])
    else:
        vs.scene.autoscale = False
        minAt = __tplLstMinMax_plot3d[0][0]
        maxAt = __tplLstMinMax_plot3d[1][0]

    #vs.scene.center = [1.0/2.0, 1.0/2.0, centerHightAt]
    vs.scene.center = [(rwLenAt/clfLenAt)/2.0, 1.0/2.0, centerHightAt]
    vs.scene.forward=(-1,+1,-1)
    vs.scene.up=(0,0,1)

    if blAxes == True:
        c = vs.curve( pos=[(0,0,minAt*hRateAt), (0,0,maxAt*hRateAt)]
                ,  color=(0,1,1)
                , radius = radiusAt*1.1 )

    if blMesh:
        lstCurveY = [vs.curve(pos =[], radius = radiusAt) for y in range(shapeAt[0]) ]
        lstCurveX = [vs.curve(pos =[], radius = radiusAt) for x in range(shapeAt[1]) ]
        for inY in range(shapeAt[0]):
            for inX in range(shapeAt[1]):
                #import pdb; pdb.set_trace()
                lstCurveY[inY].append([inX/rwfLenAt, inY/clfLenAt, mtrxAg[inY,inX]*hRateAt])

        for inX in range(shapeAt[1]):
            #import pdb; pdb.set_trace()
            for inY in range(shapeAt[0]):
                lstCurveX[inX].append([inX/rwfLenAt, inY/clfLenAt, mtrxAg[inY,inX]*hRateAt])

    vs.sphere(pos = (maxIndexAt[1]/rwfLenAt, maxIndexAt[0]/clfLenAt, maxAt*hRateAt)
            , radius = 0.018, color = vs.color.red)

    vs.sphere(pos = (minIndexAt[1]/rwfLenAt, minIndexAt[0]/clfLenAt, minAt*hRateAt)
            , radius = 0.018, color = vs.color.green)
    if blDisplayMinMaxLabel == True:
        vs.label(pos=(maxIndexAt[1]/rwfLenAt,  maxIndexAt[0]/clfLenAt
                    , maxAt*hRateAt)
                , text='max:'+ '%6g'%maxAt, xoffset=0, yoffset=20
                , height=20, border=5)
        vs.label(pos=(minIndexAt[1]/rwfLenAt, minIndexAt[0]/clfLenAt
                , minAt*hRateAt)
                , text='min:'+ '%6g'%minAt, xoffset=-20, yoffset=-20
                , height=20, border=5)
        

    modelAt = vs.faces(
        pos = vs.zeros( ( (clLenAt-1)*2*(rwLenAt-1)*2*3,3 ), sf.vs_Float ))
    modelAt.normal = [ [0,0,0] ]*len(modelAt.pos)
    modelAt.color = [ color ]* len(modelAt.pos)
    for colAt in range(clLenAt-1):
        for rowAt in range(rwLenAt-1):
            modelAt.pos[colAt*2*(rwLenAt-1)*2*3 + 2*2*3*rowAt     ,0:3] = [
                    rowAt/rwfLenAt, colAt/clfLenAt,mtrxAg[colAt,
                    rowAt]*hRateAt ]
            modelAt.pos[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt +  1,0:3] = [
                    (rowAt+1)/rwfLenAt, colAt/clfLenAt,
                    mtrxAg[colAt,rowAt+1]*hRateAt ]
            modelAt.pos[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt +  2,0:3] = [
                    (rowAt+1)/rwfLenAt, (colAt+1)/clfLenAt,
                    mtrxAg[colAt+1,rowAt+1]*hRateAt ]

            #import pdb; pdb.set_trace()
            #print "colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt:",
            # colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt
            #modelAt.normal[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt:
            #   colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt+12, 0:3] = [
            #                                                [[1,1,1]]*3 ]*12
            modelAt.normal[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt
                          :colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt+6, 0:3] =[
                          [1,1,1] ]*6

            modelAt.pos[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt +  3, 0:3] =[
                    rowAt/rwfLenAt, colAt/clfLenAt, mtrxAg[colAt
                    , rowAt]*hRateAt ]
            modelAt.pos[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt +  4, 0:3] =[
                    (rowAt+1)/rwfLenAt, (colAt+1)/clfLenAt
                    , mtrxAg[colAt+1,rowAt+1]*hRateAt ]
            modelAt.pos[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt +  5, 0:3] =[
                    rowAt/rwfLenAt, (colAt+1)/clfLenAt
                    , mtrxAg[colAt+1,rowAt]*hRateAt ]


            modelAt.pos[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt +  6,0:3] = [
                    rowAt/rwfLenAt, colAt/clfLenAt, mtrxAg[colAt
                    , rowAt]*hRateAt ]
            modelAt.pos[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt +  7,0:3] = [
                    (rowAt+1)/rwfLenAt, (colAt+1)/clfLenAt
                    , mtrxAg[colAt+1,rowAt+1]*hRateAt ]
            modelAt.pos[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt +  8,0:3] = [
                    (rowAt+1)/rwfLenAt, colAt/clfLenAt
                    , mtrxAg[colAt,rowAt+1]*hRateAt ]

            modelAt.pos[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt +  9, 0:3] =[
                    rowAt/rwfLenAt, colAt/clfLenAt, mtrxAg[colAt
                    , rowAt]*hRateAt ]
            modelAt.pos[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt + 10, 0:3] =[
                    rowAt/rwfLenAt, (colAt+1)/clfLenAt
                    , mtrxAg[colAt+1,rowAt]*hRateAt ]
            modelAt.pos[colAt*2*(shapeAt[1]-1)*2*3 + 2*2*3*rowAt + 11, 0:3] =[
                    (rowAt+1)/rwfLenAt, (colAt+1)/clfLenAt
                    , mtrxAg[colAt+1,rowAt+1]*hRateAt ]

    return modelAt

__objScatteringDisplayGeneratedStt = None   # to enable overlap plot
def plotPt(sqAg,  color = sf.cyan, orgn=(), ends=()):
    """' plot scattered point graph for vector argument data
        If you call scattertGr(..) a number of times, then the graphs
        were plotted in piles.

        You can set orgh/ends pair for the displaying area
        By default, the displaying arear is determined by minimum/maxmum values.
        
        if you want to vanish the graph then do as below
            objAt=scatterGr(..)
                .
                .
            objAt.visible = None
    '"""

    vs = sf.vs_()

    global __objScatteringDisplayGeneratedStt
    color = tuple(color)   # color argment may be list/vector
    assert hasattr(sqAg, '__len__'),(
        "You set not 2D or 3D data in scatterGr(..):"+str(sqAg))
    lenAt = len(sqAg)
    assert hasattr(sqAg[0], '__len__'),(
        "You set not 2D or 3D data in scatterGr(..):"+str(sqAg))
    dimAt = len(sqAg[0])
    
    if __objScatteringDisplayGeneratedStt == None:
        if dimAt == 2:
            import visual.graph as vg
            __objScatteringDisplayGeneratedStt = vg.gdisplay(width=600
                                                            ,height=600)
        elif dimAt == 3:
            __objScatteringDisplayGeneratedStt = vs.curve( color = color )
        else:
            assert False, ("You set not 2D or 3D data in scatterGr(..):"
                          +str(sqAg) )

    if dimAt == 2:
        lstX = [x[0] for x in sqAg]
        lstY = [x[1] for x in sqAg]
        lstX_rangeAt = [min(lstX), max(lstX)]
        lstY_rangeAt = [min(lstY), max(lstY)]
        if orgn != ():
            lstX_rangeAt[0] = orgh[0]
            lstY_rangeAt[0] = orgh[1]
        if ends != ():
            lstX_rangeAt[1] = ends[0]
            lstY_rangeAt[1] = ends[1]

        delta = min( lstX_rangeAt[1]-lstX_rangeAt[0]
#                   , lstY_rangeAt[1]-lstY_rangeAt[0] )/(2*50.)
                   , lstY_rangeAt[1]-lstY_rangeAt[0] )/(2*50.)
        import visual.graph as vg
        def drawRectangular(pos):
            grphAt = vg.gcurve( color = color)
            grphAt.plot(pos = (pos[0]- delta, pos[1] + delta) )
            grphAt.plot(pos = (pos[0]- delta, pos[1] - delta) )
            grphAt.plot(pos = (pos[0]+ delta, pos[1] - delta) )
            grphAt.plot(pos = (pos[0]+ delta, pos[1] + delta) )
            grphAt.plot(pos = (pos[0]- delta, pos[1] + delta) )

        for elm in sqAg:
            drawRectangular(elm)
        return __objScatteringDisplayGeneratedStt
    else:
        #assert False, "Not implemented!" 
        lstX = [x[0] for x in sqAg]
        lstY = [x[1] for x in sqAg]
        lstZ = [x[2] for x in sqAg]
        lstX_rangeAt = (min(lstX), max(lstX))
        lstY_rangeAt = (min(lstY), max(lstY))
        lstZ_rangeAt = (min(lstZ), max(lstZ))
        if orgn != ():
            lstX_rangeAt[0] = orgh[0]
            lstY_rangeAt[0] = orgh[1]
            lstZ_rangeAt[0] = orgh[2]
        if ends != ():
            lstX_rangeAt[1] = ends[0]
            lstY_rangeAt[1] = ends[1]
            lstY_rangeAt[1] = ends[3]


        delta = min( lstX_rangeAt[1]-lstX_rangeAt[0]
                   , lstY_rangeAt[1]-lstY_rangeAt[0]
                   , lstZ_rangeAt[1]-lstZ_rangeAt[0] )/(2*50.)

        import visual as vs
        for elm in sqAg:
            vs.sphere(pos = elm, radius = delta, color = color)

        return __objScatteringDisplayGeneratedStt




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
        from octn import ClOctonion
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

plot2d = plotGr # plot2d must be perged lately

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


def plotTmCh(vctMtrxAg):
    """' plot time chart for vector,array or matrix dictionary data
    '"""
    import pylab as pb
    def __plotTmChX(vctMtrxAg):
        n = len(vctMtrxAg)
        lstYAt = [None]*(2*n)
        lstYAt[0::2] = vctMtrxAg
        lstYAt[1::2] = vctMtrxAg
        lstYAt = [vctMtrxAg[0]]+lstYAt+[vctMtrxAg[-1]]

        lstXAt = [None]*(2*(n+1))
        lstXAt[0::2] = range(n+1)
        lstXAt[1::2] = range(n+1)

        maxAt = max(vctMtrxAg)
        minAt = min(vctMtrxAg)
        pb.plot(lstXAt, lstYAt)

        if maxAt != minAt:
            lstAxisAt = list(pb.axis())
            meanAt = float(maxAt + minAt)/2
            lstAxisAt[2] = minAt + (minAt - meanAt)*0.2 # set Y axis min
            lstAxisAt[3] = maxAt + (maxAt - meanAt)*0.2 # set Y axis max
            pb.axis(lstAxisAt)

    assert '__getitem__' in dir(vctMtrxAg)
    if isinstance(vctMtrxAg, dict) or '__len__' in dir(vctMtrxAg[0]):
        if isinstance(vctMtrxAg, list):
            assert not('__getitem__' in dir(vctMtrxAg[0][0]))
            colSizeAt = len(vctMtrxAg)
        elif isinstance(vctMtrxAg, dict):
            lstAt = vctMtrxAg.keys()
            lstAt.sort()
            shapeAt = lstAt[-1]
            shapeAt = (shapeAt[0]+1, shapeAt[1]+1)
            assert shapeAt[0]*shapeAt[1] == len(lstAt),\
                "dictionary vctMtrxAg index is not alined" + str(objarAg)

            krAt = sf.kzrs(shapeAt)
            for index in sf.mrng(*shapeAt):
                krAt[index] = vctMtrxAg[index]

            vctMtrxAg = krAt
            colSizeAt = shapeAt[0]
        else:
            assert isinstance(vctMtrxAg, sf.sc.ndarray)
            assert len( vctMtrxAg.shape ) == 2

            colSizeAt = vctMtrxAg.shape[0]

        for i, elmAt in enumerate(vctMtrxAg):
            # don't use subplot(,,0) not to shift upper
            pb.subplot(colSizeAt, 1, i+1) 
            __plotTmChX(elmAt)
    else:
        __plotTmChX(vctMtrxAg)

    pb.show()


renderMtrx = plot3dRowCol
"""' renderMtrx(..) is a aliaing name of the plot3dRowCol(..)
    Because if a user uses renderMtCplxWithRGB(..) then the user want to
    use the name of renderMtrx(..) substituting plot3dRowCol(..)
'"""

def plot3dGr(f, rangeX=[0,1], rangeY=None, blLabel=False, color=sf.blue):
    """' render f(x,y) for x in rangeX and for y in rangeY
    まだ、複数グラフ表示は rageX,rangeY が同じときに限る
    '"""
    if isinstance(f,(dict,list,tuple)):
        mtAt = sf.krry(f)
    elif isinstance(f, sf.np.ndarray):
        mtAt = f
    else:
        assert hasattr(f,'__call__')

        if rangeY==None:
            rangeY = rangeX

        if len(rangeX)==2:
            rangeX = sf.klsp(*rangeX)
        if len(rangeY)==2:
            rangeY = sf.klsp(*rangeY)

        dctAt={}
        if sf.sc.iscomplexobj(rangeX) or sf.sc.iscomplexobj(rangeY):
            for j,x in sf.enmitr(rangeX):
                for k,y in sf.enmitr(rangeY):
                    dctAt[j,k]=f(x+y)
        else:
            for j,x in sf.enmitr(rangeX):
                for k,y in sf.enmitr(rangeY):
                    dctAt[j,k]=f(x,y)

        mtAt = sf.krry(dctAt)
    if sf.sc.iscomplexobj(mtAt):
        #sf.renderMtCplxWithRGB(mtAt)
        sf.renderMtCplx(mtAt, blDisplayMinMaxLabel = blLabel)
        #sf.renderMtCplx(mtAt, blDisplayMinMaxLabel = blLabel, blDirection=False)
    else:
        sf.renderMtrx(mtAt, blDisplayMinMaxLabel = blLabel, color=color)

    if blLabel != False:
        vs = sf.vs_()
        val = rangeX[0]
        if isinstance(val,complex) and val.imag != 0:
            strAt = ( '%6g'%(val.real)+'+%6g'%val.imag+'i'
                      if val.imag >= 0 else
                      '%6g'%(val.real)+'%6g'%val.imag+'i'
                    )
            vs.label(pos=(0, 0, 0)
                    , text=strAt
                    , xoffset=-20, yoffset=0
                    , height=10, border=5)
        else:
            if isinstance(val,complex):
                val = val.real
            vs.label(pos=(0, 0, 0)
                    , text='%6g'%(rangeX[0]), xoffset=-20, yoffset=0
                    , height=10, border=5)

        val = rangeX[-1]
        if isinstance(val,complex) and val.imag != 0:
            strAt = ('%6g'%(val.real)+'+%6g'%val.imag+'i'
                      if val.imag >= 0 else
                      '%6g'%(val.real)+'%6g'%val.imag+'i'
                    )
            vs.label(pos=(1, 0, 0)
                    , text=strAt
                    , xoffset=-20, yoffset=0
                    , height=10, border=5)
        else:
            if isinstance(val,complex):
                val = val.real
            vs.label(pos=(1, 0, 0)
                    , text='%6g'%(rangeX[-1]), xoffset=-20, yoffset=0
                    , height=10, border=5)
        
        val = rangeY[0]
        if isinstance(val,complex) and val.imag != 0:
            strAt = ( '%6g'%(val.real)+'+%6g'%val.imag+'i'
                       if val.imag >= 0 else
                      '%6g'%(val.real)+'%6g'%val.imag+'i'
                    )
            vs.label(pos=(0, 0, 0)
                    , text=strAt
                    , xoffset=  0, yoffset=-20
                    , height=10, border=5)
        else:
            if isinstance(val,complex):
                val = val.real

            vs.label(pos=(0, 0, 0)
                    , text='%6g'%(rangeY[0]), xoffset=  0, yoffset=-20
                    , height=10, border=5)

        val = rangeY[-1]
        if isinstance(val,complex) and val.imag != 0:
            strAt = ( '%6g'%(val.real)+'+%6g'%val.imag+'i' 
                      if val.imag >= 0 else
                      '%6g'%(val.real)+'%6g'%val.imag+'i'
                    )
            vs.label(pos=(0, 1, 0)
                    , text=strAt
                    , xoffset=  0, yoffset=+60
                    , height=10, border=5)
        else:
            if isinstance(val,complex):
                val = val.real
            vs.label(pos=(0, 1, 0)
                    , text='%6g'%(rangeY[-1]), xoffset=  0, yoffset=+60
                    , height=10, border=5)

#import visual as vs
class ClPlane(object):
    def __init__(self, pos=[0,0,0], axis = [0,1,0], size = 1.0):
        """' display plane made of vpyhon ellipsoids
            Inputs:
              axis --- dirction of the body
              pos ---- the position of the body
              size --- the body size
        '"""
        vs = sf.vs_()
        self.m_frm = vs.frame()
        self.m_frm.up = [0,0,1]
    
        vs.ellipsoid(frame = self.m_frm, pos = pos, axis=[size, 0, 0]    # 胴体
                , width=size/3.0, height=size/3.0 )
        vs.ellipsoid(frame = self.m_frm, pos = [size*0.2/3+pos[0], pos[1], pos[2]], axis=[0,0,size*5/3.0]
                , width=size* 0.9/3, height=size* 0.1/3, color = vs.color.red) # 主翼
        vs.ellipsoid(frame = self.m_frm, pos = [-size/3.0+pos[0], pos[1], pos[2]], axis=[0,0,size*2/3.0]
                , width =size*0.5/3, height=size*0.1/3, color = vs.color.red) #水平尾翼
        vs.ellipsoid(frame = self.m_frm, pos = [-size/3.0+pos[0], 0.3*size/3+pos[1], pos[2]], axis=[0, size/3.0, 0]
                , width=0.1*size/3, height=0.5*size/3, color = vs.color.green)   # 垂直尾翼
    

