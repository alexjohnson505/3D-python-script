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

# start with 'clean slate'
# erases anything on stage creates a new file
newfile = cmds.file(f=True, new=True)

# Set playback options
cmds.playbackOptions( loop='continuous' )
cmds.playbackOptions( minTime='0sec', maxTime='5sec' )

# set initial camera position
# cmds.setAttr('persp.translateX', -15.000)
# cmds.setAttr('persp.translateY', 10.000)
# cmds.setAttr('persp.translateZ', 20.000)

# set initial camera angle
# cmds.setAttr('persp.rotateX', -15.000)
# cmds.setAttr('persp.rotateY', -35.000)
# cmds.setAttr('persp.rotateZ', 0.000)

# set playback options
cmds.playbackOptions( minTime='0sec', maxTime='15sec', ast=0, ps=1.8)

# Create a sphere, with 10 subdivisions in the X direction,
# and 15 subdivisions in the Y direction,
# the radius of the sphere is 20.
# http://download.autodesk.com/us/maya/2010help/CommandsPython/polySphere.html
cmds.polySphere(n='sphere01', sx=15, sy=20, r=1)

# Query the radius of the new sphere
r = cmds.polySphere('sphere01', q=True, sx=True )

# Set sphere's pivot point to the bottom.
# -> Makes scaling the sphere upon collision easier
cmds.move(0, -1, "sphere01.scalePivot","sphere01.rotatePivot", absolute=True)

## Pull Back perspective over 200 frames.
# start perspective change
# cmds.setKeyframe( 'persp', v=-20,      at='translateX', itt='linear', ott='linear', t = 0)
# cmds.setKeyframe( 'persp', v=15,       at='translateY', itt='linear', ott='linear', t = 0)
# cmds.setKeyframe( 'persp', v=25,       at='translateZ', itt='linear', ott='linear', t = 0)

# finish perspective change
# cmds.setKeyframe( 'persp', v=-15,    at='translateX', itt='linear', ott='linear', t = 200)
# cmds.setKeyframe( 'persp', v=10,     at='translateY', itt='linear', ott='linear', t = 200)
# cmds.setKeyframe( 'persp', v=20,     at='translateZ', itt='linear', ott='linear', t = 200)

## Create camera
cameraName = cmds.camera()
cameraShape = cameraName[1]

## Move camera through scene
# Camera Start Position
cmds.setKeyframe(cameraName, v=6.8,       at='translateX', itt='spline', ott='spline', t = 0)
cmds.setKeyframe(cameraName, v=9.5,       at='translateY', itt='spline', ott='spline', t = 0)
cmds.setKeyframe(cameraName, v=15.8,      at='translateZ', itt='spline', ott='spline', t = 0)

cmds.setKeyframe(cameraName, v=-24.3,     at='rotateX', itt='spline', ott='spline', t = 0)
cmds.setKeyframe(cameraName, v=22.7,      at='rotateY', itt='spline', ott='spline', t = 0)
cmds.setKeyframe(cameraName, v=0,         at='rotateZ', itt='spline', ott='spline', t = 0)

# Camera End Position
cmds.setKeyframe(cameraName, v=-3.3,      at='translateX', itt='spline', ott='spline', t = 150)
cmds.setKeyframe(cameraName, v=4.0,       at='translateY', itt='spline', ott='spline', t = 150)
cmds.setKeyframe(cameraName, v=5.6,       at='translateZ', itt='spline', ott='spline', t = 150)

cmds.setKeyframe(cameraName, v=-18.3,     at='rotateX', itt='spline', ott='spline', t = 150)
cmds.setKeyframe(cameraName, v=-34.1,     at='rotateY', itt='spline', ott='spline', t = 150)
cmds.setKeyframe(cameraName, v=0.0,       at='rotateZ', itt='spline', ott='spline', t = 150)

## Animate Sphere over 200 frames

# Translate
cmds.setKeyframe( 'sphere01', v=6.0,     at='translateY', itt='linear', ott='linear', t = 0)
cmds.setKeyframe( 'sphere01', v=1.0,     at='translateY', itt='linear', ott='linear', t = 90)
cmds.setKeyframe( 'sphere01', v=1.0,     at='translateY', itt='linear', ott='linear', t = 110)
cmds.setKeyframe( 'sphere01', v=6.0,     at='translateY', itt='linear', ott='linear', t = 200)

# Scale
cmds.setKeyframe( 'sphere01', v=1.0,     at='scaleY', itt='linear', ott='linear', t = 0)
cmds.setKeyframe( 'sphere01', v=1.0,     at='scaleY', itt='linear', ott='linear', t = 90)
cmds.setKeyframe( 'sphere01', v=0.5,     at='scaleY', itt='linear', ott='linear', t = 100)
cmds.setKeyframe( 'sphere01', v=1.0,     at='scaleY', itt='linear', ott='linear', t = 110)
cmds.setKeyframe( 'sphere01', v=1.0,     at='scaleY', itt='linear', ott='linear', t = 200)


# #move sub
# cmds.setKeyframe( 'moveSub2', v=0.0,         at='translateZ', itt='spline', ott='spline', t = 0)
# cmds.setKeyframe( 'moveSub2', v=0.0,         at='translateZ', itt='spline', ott='spline', t = 100)
# cmds.setKeyframe( 'moveSub2', v=-800.000,    at='translateZ', itt='spline', ott='spline', t = 200)