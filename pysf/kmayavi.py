# -*- encoding: utf-8 -*-
from __future__ import division
"""'
english:
    PythonSf pysf/kmayavi.py
    https://github.com/lobosKobayashi
    http://lobosKobayashi.github.com/
    
    Copyright 2016, Kenji Kobayashi
    All program codes in this file was designed by kVerifierLab Kenji Kobayashi

    I release souce codes in this file under the GPLv3
    with the exception of my commercial uses.

    2016y 12m 28d Kenji Kokbayashi

japanese:
    PythonSf pysf/kmayavi.py
    http://lobosKobayashi.github.com/
    http://lobosKobayashi.github.com/

    Copyright 2016, Kenji Kobayashi
    このファイルの全てのプログラム・コードは kVerifierLab 小林憲次が作成しました。
    
    作成者の小林本人に限っては商用利用を許すとの例外条件を追加して、
    このファイルのソースを GPLv3 で公開します。

    2016年 12月 28日 小林憲次
'"""

import pysf.sfFnctns as sf

def mlb_():
    """'import enthought.mayavi.mlab' takes 2 seconds. It is heavy.
    So we indtroducem mlb() fucntion to imports enthought.mayavi.mlab

    You can call mlb() only again and again.

    e.g.
        mlb_().show()
     alternatively
        import enthought.mayavi.mlab as md
        md.show()
    '"""
    #import enthought.mayavi.mlab as mlb
    import mayavi.mlab as mlb
    sf.__getDctGlobals()['mlb']=mlb
    return mlb

def mlb():
    """'import enthought.mayavi.mlab' takes 2 seconds. It is heavy.
    So we indtroduce mlb() fucntion to imports enthought.mayavi.mlab

    Be Cation! You can call mlb() only once.

    e.g.
        mlb().show()
     alternatively
        import enthought.mayavi.mlab as md
        md.show()
    '"""
    
    return mlb_()

def kmshw(blAxesAg=True):
    """' display mlab graph
        default with axes
    '"""
    if blAxesAg:
        mlb_().axes()
    
    mlb_().show()

def kmsh(ag,**kwargs):
    mtAt=sf.krry(ag)
    shapeAt = mtAt.shape
    if len (shapeAt) == 3:
        mlb_().mesh(mtAt[:,:,0], mtAt[:,:,1], mtAt[:,:,2], **kwargs)
    else:
        assert len(shapeAt) == 2 and len(mtAt[0,0]) == 3
        mtAt2 = sf.kzrs(shapeAt + (3,))
        for j,k in sf.mrng(*shapeAt):
            mtAt2[j,k,:] = mtAt[j,k]
        
        mlb_().mesh(mtAt2[:,:,0], mtAt2[:,:,1], mtAt2[:,:,2], **kwargs)


def kplt3d(ag,**kwargs):
    mtAt=sf.krry(ag)
    if not('color' in kwargs.keys()):
        kwargs.update({'color':(0,1,1)})    # cyan
    mlb_().plot3d(mtAt[:,0], mtAt[:,1], mtAt[:,2], **kwargs)

def kqvr3d(ag,vAg=None, **kwargs):
    """' display vector
        The oder is x,y,z



    ===== value data for the index positions
    --- kqvr3d(valueMatrix)
                    #array or ClTensor with object
                    not tested
                    Is this realy necessary ?

            # N x M x 2 array/ClTensor
            # 2D 
    lst=range(-2,3); ag=[[(x^2,3y) for x in lst] for y in lst]; kqvr3d(ag); kmshw()
            # N x M x 3 array/ClTensor
            #     3d vector on 0 plain
    lst=range(-2,3); ag=[[(x^2,3y,x+y) for x in lst] for y in lst]; kqvr3d(ag); kmshw()

            # N x M x L x 3 array/ClTensor
    lst=range(-2,3);
    ag=[[[(x^2,3y,x+y+z) for x in lst] for y in lst] for z in lst]; kqvr3d(ag); kmshw()


    ===== position data  and  value function
    --- kqvr3d(positionMatrix, valueFunction)
                    #array or ClTensor with object
                    not tested
                    Is this realy necessary ?

                #ag :N x 2 array/ClTensor  and   2d function
    lst=range(-2,3); ag=[(x,y) for x,y in mitr(lst,lst)];kqvr3d(ag,~[`X^2,3`Y]); kmshw()

                #ag :N x 2 array/ClTensor  and   3d function
                #      3D vector on a 0 hight plain
    lst=range(-2,3); ag=[(x,y) for x,y in mitr(lst,lst)]
    kqvr3d(ag,~[`X^2,3`Y,`X+`Y]); kmshw()
 
                    #ag :N x 3 array/ClTensor  and   3d function
    lst=range(-2,3); ag=[(x,y,z) for x,y,z in mitr(lst,lst,lst)];
    kqvr3d(ag,~[`X^2,3`Y,`Z]); kmshw()


                #ag :N x M x 2 array/ClTensor  and  3d function
                #      2D vector on a 0 hight plain
    lst=range(-2,3); ag=[[(x,y) for x in lst] for y in lst];kqvr3d(ag,~[`X^2,3`Y]); kmshw()

                #      3D vector on a 0 hight plain
    lst=range(-2,3); ag=[[(x,y) for x in lst] for y in lst];
    kqvr3d(ag,~[`X^2,3`Y,`X+`Y]); kmshw()

                #ag : N x M x L x 3 array/ClTensor  and  3d function
    lst=range(-2,3);
    ag=[[[(x,y,z) for x in lst] for y in lst] for z in lst];
    kqvr3d(ag,~[`X^2,3`Y,`X+`Y]); kmshw()



    ===== position data  and  value data
    --- kqvr3d(positionMatrix, valueMatrix)
                    #array or ClTensor with object
                    not tested
                    Is this realy necessary ?

                    #ag :N x 2 array/ClTensor      vAg :N x 2 array/ClTensor
    ε=5;lst=klsp(-2.5,2.5,10); ag=list(mitr(lst,lst));
    vAg=~[~[ε (`X-`X^3/3-`Y), `X/ε](x,y) for x,y in ag]
    kqvr3d(ag, vAg); kmshw()

                    #ag :N x 3 array/ClTensor      vAg :N x 3 array/ClTensor
    ε=3;lst=klsp(-2.5,2.5,10); ps=list(mitr(lst,lst,lst));
    vl=~[~[ε (`X-`X^3/3-`Y), `X/ε,`Z](x,y,z) for x,y,z in ag];
    kqvr3d(ag, vl); kmshw()

                #ag :N x M x 2 array/ClTensor  vAg :N x M x 2 array/ClTensor
    lst=range(-2,3); ag=[[(x,y) for x in lst] for y in lst];
    vAg=[[(x^2,3y) for x in lst] for y in lst];
    kqvr3d(ag,vAg); kmshw()

                #ag :N x M x 3 array/ClTensor  vAg :N x M x 3 array/ClTensor
                #                     3d vector on a plain
    lst=range(-2,3); ag=[[(x,y,3) for x in lst] for y in lst];
    vAg=[[(x^2,3y,x+y) for x in lst] for y in lst];
    kqvr3d(ag,vAg); kmshw()

                #ag :NxMxL x 3 array/ClTensor  vAg :NxMxL x 3 array/ClTensor
    lst=range(-2,3); ag=[[[(x,y,z) for x in lst] for y in lst] for z in lst]; 
    vAg=[[[(x^2,3y,x+y) for x in lst] for y in lst] for z in lst];
    kqvr3d(ag,vAg); kmshw()
    '"""
    if vAg == None:
        # The positions of vectors is (0,0,0), (0,0,1) .... (L,M,N)
        if not isinstance( ag, (sf.ClTensor, sf.sc.ndarray) ):
            ag = sf.krry(ag)
        ag=sf.sc.array(ag.view())

        shapeAt = ag.shape
        if ag.dtype == object:
            # You can set a list/tuple/array/ClTensor as an element of matrix
            # e.g.
            # rank 3 array/ClTensor, the length of every elements is 3 
            # [[[(1,2,3), ... , (5,1,2)],
            #  ,[(2,5,0), ... , (6,5,4)],
            #      .       .       .
            #  ,[(0,3,2), ... , (3,5,1)]]], dtype=object
            shapeAt = ag.shape
            assert len(shapeAt) == 3
            assert len(ag[0,0,0]) == 3
            def getTns(ag, xyz):
                return [[[ ag[i,j,k][xyz] for k in range(shapeAt[2])]
                                          for j in range(shapeAt[1])]
                                          for i in range(shapeAt[0])]
                                     
            mlb_().quiver3d(getTns(ag,0),getTns(ag,1),getTns(ag,2), **kwargs)

        elif len(shapeAt) == 3:
            if len(ag[0,0]) == 2:
            # N x M x 2 array/ClTensor
            # 2D 
            #  [[[1,2  ], ... , [5,1  ]],
            #  ,[[2,5  ], ... , [6,5  ]],
            #      .       .       .
            #  ,[[0,3  ], ... , [3,5  ]]]]
                mlb_().quiver3d(ag[:,:,0],ag[:,:,1],sf.kzrs(shapeAt[:2])
                                                                , **kwargs)
            else:
            # N x M x 3 array/ClTensor
            #     3d vector on 0 plain
            #  [[[1,2,3], ... , [5,1,4]],
            #  ,[[2,5,4], ... , [6,5,3]],
            #      .       .       .
            #  ,[[0,3,8], ... , [3,5,1]]]]
                mlb_().quiver3d(ag[:,:,0],ag[:,:,1], ag[:,:,2], **kwargs)
        
        else:
            # N x M x L x 3 array/ClTensor
            # 3D
            # [[[[1,2,3], ... , [5,1,2]],
            #  ,[[2,5,0], ... , [6,5,4]],
            #      .       .       .
            #  ,[[0,3,2], ... , [3,5,1]]]]

            mlb_().quiver3d(ag[:,:,:, 0],ag[:,:,:, 1],ag[:,:,:, 2], **kwargs)
    elif hasattr(vAg, '__call__'):
        # ag is the positions array and vAg is a function that returns a vector

        # mayavi.quiver3d(..) needs a function(sqAgX,sqAgY,sqAgZ) which returns
        # an array of vector elements. The point is a function that treats data
        # quickly in block.
        #
        # But It is difficult to describe a function that treats data in block
        # It is easy to describe a function that treats a each element step by
        # step, althou it may consume CPU time. kqvr3d(..) uses this easy and
        # slot function.
        def get3BulkBlockRtn(sqX, sqY, sqZ):
            #import pdb; pdb.set_trace()
            return sf.sc.array([
                    [vAg(sqX[k],sqY[k],sqZ[k])[0] for k in range(len(sqX))],
                    [vAg(sqX[k],sqY[k],sqZ[k])[1] for k in range(len(sqX))],
                    [vAg(sqX[k],sqY[k],sqZ[k])[2] for k in range(len(sqX))]])

        def get2BulkBlockRtn(sqX, sqY, sqZ):
            return sf.sc.array([
                    [vAg(sqX[k],sqY[k],sqZ[k])[0] for k in range(len(sqX))],
                    [vAg(sqX[k],sqY[k],sqZ[k])[1] for k in range(len(sqX))],
                    [0]*len(sqX)] )


        if not isinstance( ag, (sf.ClTensor, sf.sc.ndarray) ):
            mtAt=sf.krry(ag)    # position
        else:
            mtAt = ag
        mtAt=sf.sc.array(mtAt.view())

        if mtAt.dtype == object:
            shapeAt = mtAt.shape
            if len(shapeAt) == 1:
                # ag:position           vAg(..)
                # [(0.1, 0.3, 0.2)]     
                # [(0.4, 0.0, 0.1)]     
                #        .              
                #        .              
                assert len(mtAt[0]) == 3
                def getTns(ag, xyz):
                    return [ag[i][xyz] for i in range(shapeAt[0])]

                mlb_().quiver3d(getTns(mtAt,0),getTns(mtAt,1),getTns(mtAt,2), 
                           getBulkBlockRtn,
                           **kwargs)

            else:
                #ag :rank 3 array/ClTensor    vAg(..)
                #[[[(1,2,3), ... , (5,1,2)],  
                # ,[(2,5,0), ... , (6,5,4)],  
                #     .       .       .            .       .       .
                # ,[(0,3,2), ... , (3,5,1)]]] 

                assert len(mtAt[ (0,)*len(shapeAt) ]) == 3
                def getTns(ag, xyz):
                    return [[[ ag[i,j,k][xyz] for k in range(shapeAt[2])]
                                              for j in range(shapeAt[1])]
                                              for i in range(shapeAt[0])]
    
                mlb_().quiver3d(getTns(mtAt,0),getTns(mtAt,1),getTns(mtAt,2), 
                           getBulkBlockRtn,
                           **kwargs)
        else:
            shapeAt = mtAt.shape
            if len(shapeAt)==2:
                if len(mtAt[0,:]) == 2:
                    if len(vAg(*mtAt[0,:])) == 2:
                    #ag :N x 2 array/ClTensor  and   2d function
                    # [[ 1,2]                      
                    # ,[ 2,5]                      
                    #     .                            .                       
                    # ,[ 0,3]]                     
                        mlb_().quiver3d(mtAt[:,0], mtAt[:,1], [0]*shapeAt[0], 
                               get2BulkBlockRtn,
                               **kwargs)
                    else:
                    #ag :N x 2 array/ClTensor  and   3d function
                    #      3D vector on a 0 hight plain
                    # [[ 1,2,3]                      
                    # ,[ 2,5,1]                      
                    #     .                            .                       
                    # ,[ 0,3,0]]                     
                        mlb_().quiver3d(mtAt[:,0], mtAt[:,1], [0]*shapeAt[0], 
                               get3BulkBlockRtn,
                               **kwargs)
                else:
                #ag :N x 3 array/ClTensor  and   3d function
                # [[ 1,2,3]                      
                # ,[ 2,5,3]                      
                #     .                            .                       
                # ,[ 0,3,4]]                     
                    mlb_().quiver3d(mtAt[:,0], mtAt[:,1], mtAt[:,2],
                           get3BulkBlockRtn,
                           **kwargs)

            elif len(shapeAt)==3:
                #ag :N x M x 3 array/ClTensor  and  3d function
                # [[[1,2  ], ... , (5,1  ]],   
                # ,[[2,5  ], ... , (6,5  ]],   
                #     .       .       .        
                # ,[[0,3  ], ... , [3,5  ]]]]  
                assert len(mtAt[0,0,:]) == 2
                if len(vAg(*mtAt[0,0])) == 2:
                #      2D vector on a 0 hight plain
                    mlb_().quiver3d(
                           sf.sc.ravel(mtAt[:,:,0]), sf.sc.ravel(mtAt[:,:,1]), sf.sc.ravel(sf.kzrs(shapeAt[:2])),
                           get2BulkBlockRtn,
                           **kwargs)
                else:
                #      3D vector on a 0 hight plain
                    mlb_().quiver3d(
                           sf.sc.ravel(mtAt[:,:,0]), sf.sc.ravel(mtAt[:,:,1]), sf.sc.ravel(sf.kzrs(shapeAt[:2])),
                           get3BulkBlockRtn,
                           **kwargs)

            else:
                #ag : N x M x L x 3 array/ClTensor  and  3d function
                #[[[[1,2,3], ... , [5,1,2]],    ~[`X^2,3`Y,`X+`Y]
                # ,[[2,5,0], ... , [6,5,4]],   
                #     .       .       .        
                # ,[[0,3,2], ... , [3,5,1]]]]  
                assert len(shapeAt) == 4
                mlb_().quiver3d(sf.sc.ravel(mtAt[:,:,:,0]), sf.sc.ravel(mtAt[:,:,:,1]),
                                                 sf.sc.ravel(mtAt[:,:,:,2]), 
                       get3BulkBlockRtn,
                       **kwargs)
    else:
        # ag is the positions array
        #
        if not isinstance( ag, (sf.ClTensor, sf.sc.ndarray) ):
            mtAt=sf.krry(ag)    # position
        else:
            mtAt = ag
        mtAt=sf.sc.array(mtAt.view())

        if not isinstance( vAg, (sf.ClTensor, sf.sc.ndarray) ):
            vMtAt=sf.krry(vAg)  # value
        else:
            vMtAt=vAg
        vMtAt=sf.sc.array(vMtAt.view())

        if mtAt.dtype == object:
            shapeAt = mtAt.shape
            #assert len(shapeAt) == 3
            if len(shapeAt) == 1:
                # ag:position           vAg
                # [(0.1, 0.3, 0.2)]     [(15.3, 0.1, 0.2)]
                # [(0.4, 0.0, 0.1)]     [(10.2, 0.2,   0)]
                #        .                      .
                #        .                      .
                assert len(mtAt[0]) == 3
                def getTns(ag, xyz):
                    return [ag[i][xyz] for i in range(shapeAt[0])]

                mlb_().quiver3d(getTns(mtAt,0),getTns(mtAt,1),getTns(mtAt,2), 
                           getTns(vMtAt,0),getTns(vMtAt,1),getTns(vMtAt,2),
                           **kwargs)

            else:
                #ag :rank 3 array/ClTensor    vAg :rank 3 array/ClTensor
                #[[[(1,2,3), ... , (5,1,2)],  [[[(2.1, .2, 3), ... , (5,1,2)],
                # ,[(2,5,0), ... , (6,5,4)],   ,[(1,5, .0, 3), ... , (6,5,4)],
                #     .       .       .            .       .       .
                # ,[(0,3,2), ... , (3,5,1)]]]  ,[(0.7, .3,2 ), ... , (3,5,1)]]]

                assert len(mtAt[ (0,)*len(shapeAt) ]) == 3
                def getTns(ag, xyz):
                    return [[[ ag[i,j,k][xyz] for k in range(shapeAt[2])]
                                              for j in range(shapeAt[1])]
                                              for i in range(shapeAt[0])]
    
                mlb_().quiver3d(getTns(mtAt,0),getTns(mtAt,1),getTns(mtAt,2), 
                           getTns(vMtAt,0),getTns(vMtAt,1),getTns(vMtAt,2),
                           **kwargs)
        else:
            shapeAt = mtAt.shape
            if len(shapeAt)==2:
                if len(mtAt[0,:]) == 2:
                    #ag :N x 2 array/ClTensor      vAg :N x 2 array/ClTensor
                    # [[ 1,2]                      [[ 2.1, .2]                 
                    # ,[ 2,5]                      ,[ 1,5, .0]                 
                    #     .                            .                       
                    # ,[ 0,3]]                     ,[ 0.7, .3]]                
                    mlb_().quiver3d(mtAt[:,0], mtAt[:,1], [0]*shapeAt[0], 
                           vMtAt[:,0],vMtAt[:,1], [0]*shapeAt[0], **kwargs)
                else:
                    #ag :N x 3 array/ClTensor      vAg :N x 3 array/ClTensor
                    mlb_().quiver3d(mtAt[:,0], mtAt[:,1], mtAt[:,2],
                           vMtAt[:,0],vMtAt[:,1], vMtAt[:,2], **kwargs)
            elif len(shapeAt)==3 and len(vMtAt[0,0,:])==2:
                #ag :N x M x 2 array/ClTensor  vAg :N x M x 2 array/ClTensor
                # [[[1,2  ], ... , (5,1  ]],   [[[2.1, .2   ], ... , [5,1  ]],
                # ,[[2,5  ], ... , (6,5  ]],   ,[[1,5, .0   ], ... , [6,5  ]],
                #     .       .       .            .               .
                # ,[[0,3  ], ... , [3,5  ]]]]  ,[[0.7, .3   ], ... , [3,5  ]]]
                assert len(mtAt[0,0,:]) == 2
                mlb_().quiver3d(mtAt[:,:,0], mtAt[:,:,1], sf.kzrs(shapeAt[:2]),
                       vMtAt[:,:,0],vMtAt[:,:,1],sf.kzrs(shapeAt[:2]),
                       **kwargs)

            elif len(shapeAt)==3:
                #ag :N x M x 3 array/ClTensor  vAg :N x M x 3 array/ClTensor
                #                     3d vector on a plain
                # [[[1,2,3], ... , [5,1,2]],  [[[[2.1, .2, 3], ... , [5,1,2]],
                # ,[[2,5,0], ... , [6,5,4]],   ,[[1,5, .0, 3], ... , [6,5,4]],
                #     .       .       .            .       .       .
                # ,[[0,3,2], ... , (3,5,1)]]]  ,[[0.7, .3,2 ], ... , [3,5,1]]]
                assert len(mtAt[0,0,:]) == 3
                mlb_().quiver3d(mtAt[:,:,0], mtAt[:,:,1], mtAt[:,:,2], 
                       vMtAt[:,:,0],vMtAt[:,:,1],vMtAt[:,:,2], **kwargs)
            else:
                #ag :NxMxL x 3 array/ClTensor  vAg :NxMxL x 3 array/ClTensor
                #[[[[1,2,3], ... , [5,1,2]],  [[[[2.1, .2, 3], ... , [5,1,2]],
                # ,[[2,5,0], ... , [6,5,4]],   ,[[1,5, .0, 3], ... , [6,5,4]],
                #     .       .       .            .       .       .
                # ,[[0,3,2], ... , [3,5,1]]]]  ,[[0.7, .3,2 ], ... , [3,5,1]]]]
                assert len(shapeAt) == 4
                mlb_().quiver3d(mtAt[:,:,:,0], mtAt[:,:,:,1], mtAt[:,:,:,2], 
                       vMtAt[:,:,:,0],vMtAt[:,:,:,1],vMtAt[:,:,:,2], **kwargs)

def kgrd(posAg, valAg=None, color=(0,0,0)):
    """' Display structured 3D grid. 
        Elemnts of posAg must be 3D position vectors
            assert len(posAg.shape) == 3
            assert len(posAg[0,0,0]) == 3
    '"""
    #from enthought.tvtk.api import tvtk
    #from enthought.mayavi.sources.vtk_data_source import VTKDataSource
    from tvtk.api import tvtk
    from mayavi.sources.vtk_data_source import VTKDataSource

    if not isinstance(posAg, (sf.sc.ndarray)):
        posAg = sf.krry(posAg)
    shapeAt = posAg.shape
    sgrid = tvtk.StructuredGrid(dimensions=(shapeAt[0], shapeAt[1], shapeAt[2]))

    lstAt = []
    for idx in sf.mrng(*shapeAt):
        lstAt.append(posAg[idx])
    
    sgrid.points = lstAt
    if valAg == None:
        sgrid.point_data.scalars = range(len(lstAt))
    else:
        sgrid.point_data.scalars = valAg
    
    sgrid.point_data.scalars.name = 'scalars'

    # display 
    engine = mlb_().get_engine()
    fig = mlb_().figure(bgcolor=(1, 1, 1), fgcolor=(0, 0, 0), 
                    name="kgrd")
    #               name=sgrid._get_class_name()[3:])
    #               name=sgrid.class_name[3:])
    src = VTKDataSource(data=sgrid)
    engine.add_source(src) 
    mlb_().pipeline.surface(src, opacity=0.1)
    mlb_().pipeline.surface(mlb_().pipeline.extract_edges(src),
                            color=color )

