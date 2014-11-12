# Alex Johnson
# CS 4300 - Computer Graphics
# Assignment 06 - 3D Animation
# Part I : Scripting

# Initial source code from '3D_Scripting_Mac/CS4800/simple_animation.py'
# These scripts have been included in the .zip file, and can be
# found in the '/Example Scripts folder'.


# Python commands can be read from Autodesks's support site:
# http://download.autodesk.com/us/maya/2010help/CommandsPython/index_all.html

import maya.cmds as cmds
import random

# set initial camera position
cmds.setAttr('persp.translateX', -15.000)
cmds.setAttr('persp.translateY', 10.000)
cmds.setAttr('persp.translateZ', 20.000)

# set initial camera angle
cmds.setAttr('persp.rotateX', -15.000)
cmds.setAttr('persp.rotateY', -35.000)
cmds.setAttr('persp.rotateZ', 0.000)

# set playback options
cmds.playbackOptions( minTime='0sec', maxTime='15sec', ast=0, ps=1.8)

# Create a sphere, with 10 subdivisions in the X direction,
# and 15 subdivisions in the Y direction,
# the radius of the sphere is 20.
# http://download.autodesk.com/us/maya/2010help/CommandsPython/polySphere.html
cmds.polySphere(n='sphere01', sx=15, sy=20, r=1)

# Query the radius of the new sphere
r = cmds.polySphere('sphere01', q=True, sx=True )

#start camera change (wait 48 frames = 2 secs)
cmds.setKeyframe( 'persp', v=-15,    at='translateX', itt='linear', ott='linear', t = 0)
cmds.setKeyframe( 'persp', v=10,    at='translateY', itt='linear', ott='linear', t = 0)
cmds.setKeyframe( 'persp', v=20,   at='translateZ', itt='linear', ott='linear', t = 0)

# cmds.setKeyframe( 'persp', v=-25.538,   at='rotateX',    itt='linear', ott='linear', t = 48)
# cmds.setKeyframe( 'persp', v=31.000,    at='rotateY',    itt='linear', ott='linear', t = 48)
# cmds.setKeyframe( 'persp', v=0.000,     at='rotateZ',    itt='linear', ott='linear', t = 48)

#finish camera change (wait 48 frames = 2 secs)
cmds.setKeyframe( 'persp', v=-20,      at='translateX', itt='linear', ott='linear', t = 96)
cmds.setKeyframe( 'persp', v=15,       at='translateY', itt='linear', ott='linear', t = 96)
cmds.setKeyframe( 'persp', v=25,     at='translateZ', itt='linear', ott='linear', t = 96)

# cmds.setKeyframe( 'persp', v=-38.138,       at='rotateX',    itt='linear', ott='linear', t = 96)
# cmds.setKeyframe( 'persp', v=128.600,       at='rotateY',    itt='linear', ott='linear', t = 96)
# cmds.setKeyframe( 'persp', v=0.000,         at='rotateZ',    itt='linear', ott='linear', t = 96)


# # SPIN PROP
# cmds.setKeyframe( 'propel', v=0,     at='rotateZ', itt='linear', ott='linear', t = 0)
# cmds.setKeyframe( 'propel', v=-2160, at='rotateZ', itt='linear', ott='linear', t = 240)


# #move sub
# cmds.setKeyframe( 'moveSub2', v=0.0,         at='translateZ', itt='spline', ott='spline', t = 0)
# cmds.setKeyframe( 'moveSub2', v=0.0,         at='translateZ', itt='spline', ott='spline', t = 100)
# cmds.setKeyframe( 'moveSub2', v=-800.000,    at='translateZ', itt='spline', ott='spline', t = 200)