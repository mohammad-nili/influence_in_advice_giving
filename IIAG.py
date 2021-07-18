#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.0),
    on July 15, 2021, at 18:16
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.0'
expName = 'flankerText'  # from the Builder filename that created this script
expInfo = {'participant': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' %(expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\nili\\Desktop\\cog\\nili_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1366, 768], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color='white', colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "inst1"
inst1Clock = core.Clock()
instrText_2 = visual.TextStim(win=win, name='instrText_2',
    text='Zero sum game with 3 subject \n(1 client & 2 adviser)',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
image_3 = visual.ImageStim(
    win=win,
    name='image_3', 
    image='client.png', mask=None,
    ori=0.0, pos=(-.75, 0), size=(0.25, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
image_4 = visual.ImageStim(
    win=win,
    name='image_4', 
    image='blue.png', mask=None,
    ori=0.0, pos=(.75, .25), size=(0.25, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
image_5 = visual.ImageStim(
    win=win,
    name='image_5', 
    image='red.png', mask=None,
    ori=0.0, pos=(.75, -0.25), size=(0.25, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
text_3 = visual.TextStim(win=win, name='text_3',
    text='(press "space" key to next)',
    font='Open Sans',
    pos=(0, -.75), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
key_resp = keyboard.Keyboard()
title = visual.TextStim(win=win, name='title',
    text='Influence in advice giving',
    font='Open Sans',
    pos=(0, .75), height=0.15, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
details = visual.TextStim(win=win, name='details',
    text='experiment run in 20 trials',
    font='Open Sans',
    pos=(0, -.25), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
warn = visual.TextStim(win=win, name='warn',
    text="warning : don't use right side numbers on your keyboard",
    font='Open Sans',
    pos=(0, -.9), height=0.05, wrapWidth=None, ori=0.0, 
    color='red', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);

# Initialize components for Routine "inst2"
inst2Clock = core.Clock()
instrText_3 = visual.TextStim(win=win, name='instrText_3',
    text="When it is the client's turn, client must choose one adviser In this way : ",
    font='Arial',
    pos=[0, .75], height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
image_6 = visual.ImageStim(
    win=win,
    name='image_6', 
    image='client.png', mask=None,
    ori=0.0, pos=(-.75, 0), size=(0.25, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
text_L = visual.TextStim(win=win, name='text_L',
    text='press "←" key to choose red adviser\n',
    font='Open Sans',
    pos=(0, .25), height=0.1, wrapWidth=None, ori=0.0, 
    color='red', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
text_or = visual.TextStim(win=win, name='text_or',
    text='or ',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
text_r = visual.TextStim(win=win, name='text_r',
    text='press  "→" key to choose blue adviser',
    font='Open Sans',
    pos=(0, -.25), height=0.1, wrapWidth=None, ori=0.0, 
    color='blue', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
text_space = visual.TextStim(win=win, name='text_space',
    text='(press "space" key to next)',
    font='Open Sans',
    pos=(0, -.75), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "inst3"
inst3Clock = core.Clock()
instrText_4 = visual.TextStim(win=win, name='instrText_4',
    text="When it is the adviser's turn:\n the client must go out \n\nthe advicers must individually :\ngive adviced lottery color & \nthe degree of confidence they have .",
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
image_10 = visual.ImageStim(
    win=win,
    name='image_10', 
    image='blue.png', mask=None,
    ori=0.0, pos=(.75, .25), size=(0.25, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
image_11 = visual.ImageStim(
    win=win,
    name='image_11', 
    image='red.png', mask=None,
    ori=0.0, pos=(.75, -0.25), size=(0.25, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
text_4 = visual.TextStim(win=win, name='text_4',
    text='(press "space" key to next)',
    font='Open Sans',
    pos=(0, -.75), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
key_resp_3 = keyboard.Keyboard()

# Initialize components for Routine "client_turn_begin"
client_turn_beginClock = core.Clock()
instrText = visual.TextStim(win=win, name='instrText',
    text="client's turn.\n\n(you've 5 sec to choose your adviser)",
    font='Arial',
    pos=[0, .75], height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
instrEnd = keyboard.Keyboard()
image_7 = visual.ImageStim(
    win=win,
    name='image_7', 
    image='client.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.25, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
text_5 = visual.TextStim(win=win, name='text_5',
    text='press "space" key to start when you was ready',
    font='Open Sans',
    pos=(0, -.75), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "client"
clientClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
resp = keyboard.Keyboard()
image = visual.ImageStim(
    win=win,
    name='image', 
    image='red.png', mask=None,
    ori=0.0, pos=(-.75, 0), size=(0.25, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
image_2 = visual.ImageStim(
    win=win,
    name='image_2', 
    image='blue.png', mask=None,
    ori=0.0, pos=(.75, 0), size=(0.25, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)

# Initialize components for Routine "adviser_r"
adviser_rClock = core.Clock()
massage = visual.TextStim(win=win, name='massage',
    text='',
    font='Arial',
    pos=[0,0.75] , height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text_10 = visual.TextStim(win=win, name='text_10',
    text="you've :\n(1.4 sec to see Evidence grid)\n(4.5 sec to suggest lottery color)\n(4.5 sec to give your confidence)\n",
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
key_resp_4 = keyboard.Keyboard()
image_12 = visual.ImageStim(
    win=win,
    name='image_12', 
    image='red.png', mask=None,
    ori=0.0, pos=(-.75, 0), size=(0.25, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
text_11 = visual.TextStim(win=win, name='text_11',
    text='press "space" key to start when you was ready',
    font='Open Sans',
    pos=(0, -.75), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
text_15 = visual.TextStim(win=win, name='text_15',
    text="red adviser's turn",
    font='Open Sans',
    pos=(-.75, .5), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);

# Initialize components for Routine "grid"
gridClock = core.Clock()
advicer_turn = visual.TextStim(win=win, name='advicer_turn',
    text='',
    font='Open Sans',
    pos=(0, .5), height=0.2, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
show_image_to_advicer = visual.ImageStim(
    win=win,
    name='show_image_to_advicer', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(1, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)

# Initialize components for Routine "suggestion"
suggestionClock = core.Clock()
text_8 = visual.TextStim(win=win, name='text_8',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
resp_2 = keyboard.Keyboard()

# Initialize components for Routine "conf"
confClock = core.Clock()
text_9 = visual.TextStim(win=win, name='text_9',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
resp_3 = keyboard.Keyboard()
image_8 = visual.ImageStim(
    win=win,
    name='image_8', 
    image='conf.png', mask=None,
    ori=0.0, pos=(0, -.75), size=(0.6, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)

# Initialize components for Routine "adviser_b"
adviser_bClock = core.Clock()
massage_2 = visual.TextStim(win=win, name='massage_2',
    text='',
    font='Arial',
    pos=[0, .75], height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text_12 = visual.TextStim(win=win, name='text_12',
    text="you've :\n(1.4 sec to see Evidence grid)\n(4.5 sec to suggest lottery color)\n(4.5 sec to give your confidence)\n",
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
key_resp_5 = keyboard.Keyboard()
image_13 = visual.ImageStim(
    win=win,
    name='image_13', 
    image='blue.png', mask=None,
    ori=0.0, pos=(.75, 0), size=(0.25, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
text_13 = visual.TextStim(win=win, name='text_13',
    text='press "space" key to start when you was ready',
    font='Open Sans',
    pos=(0, -.75), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
text_16 = visual.TextStim(win=win, name='text_16',
    text="blue adviser's turn",
    font='Open Sans',
    pos=(.75, .5), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);

# Initialize components for Routine "grid"
gridClock = core.Clock()
advicer_turn = visual.TextStim(win=win, name='advicer_turn',
    text='',
    font='Open Sans',
    pos=(0, .5), height=0.2, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
show_image_to_advicer = visual.ImageStim(
    win=win,
    name='show_image_to_advicer', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(1, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)

# Initialize components for Routine "suggestion_2"
suggestion_2Clock = core.Clock()
text_14 = visual.TextStim(win=win, name='text_14',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
resp_4 = keyboard.Keyboard()

# Initialize components for Routine "conf_2"
conf_2Clock = core.Clock()
text_17 = visual.TextStim(win=win, name='text_17',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
resp_5 = keyboard.Keyboard()
image_9 = visual.ImageStim(
    win=win,
    name='image_9', 
    image='conf.png', mask=None,
    ori=0.0, pos=(0, -.75), size=(0.6, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)

# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
key_resp_7 = keyboard.Keyboard()
msg_c = visual.TextStim(win=win, name='msg_c',
    text='',
    font='Arial',
    pos=[0, 0], height=0.07, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
image_c = visual.ImageStim(
    win=win,
    name='image_c', 
    image='client.png', mask=None,
    ori=0.0, pos=(0, .5), size=(0.25, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
client_turn = visual.TextStim(win=win, name='client_turn',
    text="client's turn  (trial's result)",
    font='Open Sans',
    pos=(0, .8), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
image_r = visual.ImageStim(
    win=win,
    name='image_r', 
    image='red.png', mask=None,
    ori=0.0, pos=(-.75, .25), size=(0.25, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
image_b = visual.ImageStim(
    win=win,
    name='image_b', 
    image='blue.png', mask=None,
    ori=0.0, pos=(.75, .25), size=(0.25, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
key_resp_8 = keyboard.Keyboard()
text_2 = visual.TextStim(win=win, name='text_2',
    text='(press "space" key to next trial)',
    font='Open Sans',
    pos=(0, -.75), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);
msg_r = visual.TextStim(win=win, name='msg_r',
    text='',
    font='Arial',
    pos=[-.75, 0], height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);
msg_b = visual.TextStim(win=win, name='msg_b',
    text='',
    font='Arial',
    pos=[.75, 0], height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-10.0);

# Initialize components for Routine "thanks"
thanksClock = core.Clock()
thanksText = visual.TextStim(win=win, name='thanksText',
    text=' Thank you :)',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "inst1"-------
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
inst1Components = [instrText_2, image_3, image_4, image_5, text_3, key_resp, title, details, warn]
for thisComponent in inst1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
inst1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "inst1"-------
while continueRoutine:
    # get current time
    t = inst1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=inst1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instrText_2* updates
    if instrText_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instrText_2.frameNStart = frameN  # exact frame index
        instrText_2.tStart = t  # local t and not account for scr refresh
        instrText_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instrText_2, 'tStartRefresh')  # time at next scr refresh
        instrText_2.setAutoDraw(True)
    
    # *image_3* updates
    if image_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_3.frameNStart = frameN  # exact frame index
        image_3.tStart = t  # local t and not account for scr refresh
        image_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_3, 'tStartRefresh')  # time at next scr refresh
        image_3.setAutoDraw(True)
    
    # *image_4* updates
    if image_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_4.frameNStart = frameN  # exact frame index
        image_4.tStart = t  # local t and not account for scr refresh
        image_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_4, 'tStartRefresh')  # time at next scr refresh
        image_4.setAutoDraw(True)
    
    # *image_5* updates
    if image_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_5.frameNStart = frameN  # exact frame index
        image_5.tStart = t  # local t and not account for scr refresh
        image_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_5, 'tStartRefresh')  # time at next scr refresh
        image_5.setAutoDraw(True)
    
    # *text_3* updates
    if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_3.frameNStart = frameN  # exact frame index
        text_3.tStart = t  # local t and not account for scr refresh
        text_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
        text_3.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *title* updates
    if title.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        title.frameNStart = frameN  # exact frame index
        title.tStart = t  # local t and not account for scr refresh
        title.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(title, 'tStartRefresh')  # time at next scr refresh
        title.setAutoDraw(True)
    
    # *details* updates
    if details.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        details.frameNStart = frameN  # exact frame index
        details.tStart = t  # local t and not account for scr refresh
        details.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(details, 'tStartRefresh')  # time at next scr refresh
        details.setAutoDraw(True)
    
    # *warn* updates
    if warn.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        warn.frameNStart = frameN  # exact frame index
        warn.tStart = t  # local t and not account for scr refresh
        warn.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(warn, 'tStartRefresh')  # time at next scr refresh
        warn.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in inst1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "inst1"-------
for thisComponent in inst1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instrText_2.started', instrText_2.tStartRefresh)
thisExp.addData('instrText_2.stopped', instrText_2.tStopRefresh)
thisExp.addData('warn.started', warn.tStartRefresh)
thisExp.addData('warn.stopped', warn.tStopRefresh)
# the Routine "inst1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "inst2"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
inst2Components = [instrText_3, image_6, text_L, text_or, text_r, text_space, key_resp_2]
for thisComponent in inst2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
inst2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "inst2"-------
while continueRoutine:
    # get current time
    t = inst2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=inst2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instrText_3* updates
    if instrText_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instrText_3.frameNStart = frameN  # exact frame index
        instrText_3.tStart = t  # local t and not account for scr refresh
        instrText_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instrText_3, 'tStartRefresh')  # time at next scr refresh
        instrText_3.setAutoDraw(True)
    
    # *image_6* updates
    if image_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_6.frameNStart = frameN  # exact frame index
        image_6.tStart = t  # local t and not account for scr refresh
        image_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_6, 'tStartRefresh')  # time at next scr refresh
        image_6.setAutoDraw(True)
    
    # *text_L* updates
    if text_L.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_L.frameNStart = frameN  # exact frame index
        text_L.tStart = t  # local t and not account for scr refresh
        text_L.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_L, 'tStartRefresh')  # time at next scr refresh
        text_L.setAutoDraw(True)
    
    # *text_or* updates
    if text_or.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_or.frameNStart = frameN  # exact frame index
        text_or.tStart = t  # local t and not account for scr refresh
        text_or.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_or, 'tStartRefresh')  # time at next scr refresh
        text_or.setAutoDraw(True)
    
    # *text_r* updates
    if text_r.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_r.frameNStart = frameN  # exact frame index
        text_r.tStart = t  # local t and not account for scr refresh
        text_r.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_r, 'tStartRefresh')  # time at next scr refresh
        text_r.setAutoDraw(True)
    
    # *text_space* updates
    if text_space.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_space.frameNStart = frameN  # exact frame index
        text_space.tStart = t  # local t and not account for scr refresh
        text_space.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_space, 'tStartRefresh')  # time at next scr refresh
        text_space.setAutoDraw(True)
    
    # *key_resp_2* updates
    waitOnFlip = False
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_2_allKeys.extend(theseKeys)
        if len(_key_resp_2_allKeys):
            key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
            key_resp_2.rt = _key_resp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in inst2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "inst2"-------
for thisComponent in inst2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "inst2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "inst3"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_3.keys = []
key_resp_3.rt = []
_key_resp_3_allKeys = []
# keep track of which components have finished
inst3Components = [instrText_4, image_10, image_11, text_4, key_resp_3]
for thisComponent in inst3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
inst3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "inst3"-------
while continueRoutine:
    # get current time
    t = inst3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=inst3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instrText_4* updates
    if instrText_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instrText_4.frameNStart = frameN  # exact frame index
        instrText_4.tStart = t  # local t and not account for scr refresh
        instrText_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instrText_4, 'tStartRefresh')  # time at next scr refresh
        instrText_4.setAutoDraw(True)
    
    # *image_10* updates
    if image_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_10.frameNStart = frameN  # exact frame index
        image_10.tStart = t  # local t and not account for scr refresh
        image_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_10, 'tStartRefresh')  # time at next scr refresh
        image_10.setAutoDraw(True)
    
    # *image_11* updates
    if image_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_11.frameNStart = frameN  # exact frame index
        image_11.tStart = t  # local t and not account for scr refresh
        image_11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_11, 'tStartRefresh')  # time at next scr refresh
        image_11.setAutoDraw(True)
    
    # *text_4* updates
    if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_4.frameNStart = frameN  # exact frame index
        text_4.tStart = t  # local t and not account for scr refresh
        text_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
        text_4.setAutoDraw(True)
    
    # *key_resp_3* updates
    waitOnFlip = False
    if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.tStart = t  # local t and not account for scr refresh
        key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_3.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_3.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_3_allKeys.extend(theseKeys)
        if len(_key_resp_3_allKeys):
            key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
            key_resp_3.rt = _key_resp_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in inst3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "inst3"-------
for thisComponent in inst3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "inst3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('dataframe.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "client_turn_begin"-------
    continueRoutine = True
    # update component parameters for each repeat
    instrEnd.keys = []
    instrEnd.rt = []
    _instrEnd_allKeys = []
    # keep track of which components have finished
    client_turn_beginComponents = [instrText, instrEnd, image_7, text_5]
    for thisComponent in client_turn_beginComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    client_turn_beginClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "client_turn_begin"-------
    while continueRoutine:
        # get current time
        t = client_turn_beginClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=client_turn_beginClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instrText* updates
        if instrText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instrText.frameNStart = frameN  # exact frame index
            instrText.tStart = t  # local t and not account for scr refresh
            instrText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instrText, 'tStartRefresh')  # time at next scr refresh
            instrText.setAutoDraw(True)
        
        # *instrEnd* updates
        waitOnFlip = False
        if instrEnd.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instrEnd.frameNStart = frameN  # exact frame index
            instrEnd.tStart = t  # local t and not account for scr refresh
            instrEnd.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instrEnd, 'tStartRefresh')  # time at next scr refresh
            instrEnd.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(instrEnd.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(instrEnd.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if instrEnd.status == STARTED and not waitOnFlip:
            theseKeys = instrEnd.getKeys(keyList=['space'], waitRelease=False)
            _instrEnd_allKeys.extend(theseKeys)
            if len(_instrEnd_allKeys):
                instrEnd.keys = _instrEnd_allKeys[-1].name  # just the last key pressed
                instrEnd.rt = _instrEnd_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *image_7* updates
        if image_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_7.frameNStart = frameN  # exact frame index
            image_7.tStart = t  # local t and not account for scr refresh
            image_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_7, 'tStartRefresh')  # time at next scr refresh
            image_7.setAutoDraw(True)
        
        # *text_5* updates
        if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_5.frameNStart = frameN  # exact frame index
            text_5.tStart = t  # local t and not account for scr refresh
            text_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
            text_5.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in client_turn_beginComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "client_turn_begin"-------
    for thisComponent in client_turn_beginComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "client_turn_begin" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "client"-------
    continueRoutine = True
    routineTimer.add(9.500000)
    # update component parameters for each repeat
    text.setText('choose  one adviser :\n(← red , blue→)\n\n\n')
    resp.keys = []
    resp.rt = []
    _resp_allKeys = []
    # keep track of which components have finished
    clientComponents = [text, resp, image, image_2]
    for thisComponent in clientComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    clientClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "client"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = clientClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=clientClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
                text.setAutoDraw(False)
        
        # *resp* updates
        waitOnFlip = False
        if resp.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            resp.frameNStart = frameN  # exact frame index
            resp.tStart = t  # local t and not account for scr refresh
            resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(resp, 'tStartRefresh')  # time at next scr refresh
            resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(resp.clock.reset)  # t=0 on next screen flip
        if resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > resp.tStartRefresh + 9.5-frameTolerance:
                # keep track of stop time/frame for later
                resp.tStop = t  # not accounting for scr refresh
                resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(resp, 'tStopRefresh')  # time at next scr refresh
                resp.status = FINISHED
        if resp.status == STARTED and not waitOnFlip:
            theseKeys = resp.getKeys(keyList=['right', 'left'], waitRelease=False)
            _resp_allKeys.extend(theseKeys)
            if len(_resp_allKeys):
                resp.keys = [key.name for key in _resp_allKeys]  # storing all keys
                resp.rt = [key.rt for key in _resp_allKeys]
                # a response ends the routine
                continueRoutine = False
        
        # *image* updates
        if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image.frameNStart = frameN  # exact frame index
            image.tStart = t  # local t and not account for scr refresh
            image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
            image.setAutoDraw(True)
        if image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                image.tStop = t  # not accounting for scr refresh
                image.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image, 'tStopRefresh')  # time at next scr refresh
                image.setAutoDraw(False)
        
        # *image_2* updates
        if image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_2.frameNStart = frameN  # exact frame index
            image_2.tStart = t  # local t and not account for scr refresh
            image_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_2, 'tStartRefresh')  # time at next scr refresh
            image_2.setAutoDraw(True)
        if image_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_2.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                image_2.tStop = t  # not accounting for scr refresh
                image_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_2, 'tStopRefresh')  # time at next scr refresh
                image_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in clientComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "client"-------
    for thisComponent in clientComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if resp.keys in ['', [], None]:  # No response was made
        resp.keys = None
    trials.addData('resp.keys',resp.keys)
    if resp.keys != None:  # we had a response
        trials.addData('resp.rt', resp.rt)
    trials.addData('resp.started', resp.tStartRefresh)
    trials.addData('resp.stopped', resp.tStopRefresh)
    
    # ------Prepare to start Routine "adviser_r"-------
    continueRoutine = True
    # update component parameters for each repeat
    mykey = event.getKeys()
    mykey = mykey[len(mykey)-1:]
    if mykey[0] == 'left':
        msg = "you selected you to advice"
    else:
        msg = "you doesn't select"
    massage.setText(msg)
    key_resp_4.keys = []
    key_resp_4.rt = []
    _key_resp_4_allKeys = []
    # keep track of which components have finished
    adviser_rComponents = [massage, text_10, key_resp_4, image_12, text_11, text_15]
    for thisComponent in adviser_rComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    adviser_rClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "adviser_r"-------
    while continueRoutine:
        # get current time
        t = adviser_rClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=adviser_rClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *massage* updates
        if massage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            massage.frameNStart = frameN  # exact frame index
            massage.tStart = t  # local t and not account for scr refresh
            massage.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(massage, 'tStartRefresh')  # time at next scr refresh
            massage.setAutoDraw(True)
        
        # *text_10* updates
        if text_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_10.frameNStart = frameN  # exact frame index
            text_10.tStart = t  # local t and not account for scr refresh
            text_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_10, 'tStartRefresh')  # time at next scr refresh
            text_10.setAutoDraw(True)
        
        # *key_resp_4* updates
        waitOnFlip = False
        if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_4.frameNStart = frameN  # exact frame index
            key_resp_4.tStart = t  # local t and not account for scr refresh
            key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
            key_resp_4.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_4.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_4.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_4_allKeys.extend(theseKeys)
            if len(_key_resp_4_allKeys):
                key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
                key_resp_4.rt = _key_resp_4_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *image_12* updates
        if image_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_12.frameNStart = frameN  # exact frame index
            image_12.tStart = t  # local t and not account for scr refresh
            image_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_12, 'tStartRefresh')  # time at next scr refresh
            image_12.setAutoDraw(True)
        
        # *text_11* updates
        if text_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_11.frameNStart = frameN  # exact frame index
            text_11.tStart = t  # local t and not account for scr refresh
            text_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_11, 'tStartRefresh')  # time at next scr refresh
            text_11.setAutoDraw(True)
        
        # *text_15* updates
        if text_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_15.frameNStart = frameN  # exact frame index
            text_15.tStart = t  # local t and not account for scr refresh
            text_15.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_15, 'tStartRefresh')  # time at next scr refresh
            text_15.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in adviser_rComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "adviser_r"-------
    for thisComponent in adviser_rComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "adviser_r" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "grid"-------
    continueRoutine = True
    routineTimer.add(1.400000)
    # update component parameters for each repeat
    advicer_turn.setText('Evidence grid\n\n\n')
    show_image_to_advicer.setImage(url)
    # keep track of which components have finished
    gridComponents = [advicer_turn, show_image_to_advicer]
    for thisComponent in gridComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    gridClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "grid"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = gridClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=gridClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *advicer_turn* updates
        if advicer_turn.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            advicer_turn.frameNStart = frameN  # exact frame index
            advicer_turn.tStart = t  # local t and not account for scr refresh
            advicer_turn.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(advicer_turn, 'tStartRefresh')  # time at next scr refresh
            advicer_turn.setAutoDraw(True)
        if advicer_turn.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > advicer_turn.tStartRefresh + 1.4-frameTolerance:
                # keep track of stop time/frame for later
                advicer_turn.tStop = t  # not accounting for scr refresh
                advicer_turn.frameNStop = frameN  # exact frame index
                win.timeOnFlip(advicer_turn, 'tStopRefresh')  # time at next scr refresh
                advicer_turn.setAutoDraw(False)
        
        # *show_image_to_advicer* updates
        if show_image_to_advicer.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            show_image_to_advicer.frameNStart = frameN  # exact frame index
            show_image_to_advicer.tStart = t  # local t and not account for scr refresh
            show_image_to_advicer.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(show_image_to_advicer, 'tStartRefresh')  # time at next scr refresh
            show_image_to_advicer.setAutoDraw(True)
        if show_image_to_advicer.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > show_image_to_advicer.tStartRefresh + 1.4-frameTolerance:
                # keep track of stop time/frame for later
                show_image_to_advicer.tStop = t  # not accounting for scr refresh
                show_image_to_advicer.frameNStop = frameN  # exact frame index
                win.timeOnFlip(show_image_to_advicer, 'tStopRefresh')  # time at next scr refresh
                show_image_to_advicer.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in gridComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "grid"-------
    for thisComponent in gridComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('show_image_to_advicer.started', show_image_to_advicer.tStartRefresh)
    trials.addData('show_image_to_advicer.stopped', show_image_to_advicer.tStopRefresh)
    
    # ------Prepare to start Routine "suggestion"-------
    continueRoutine = True
    routineTimer.add(5.000000)
    # update component parameters for each repeat
    text_8.setText('What is your suggested color?\n\n( "w" : white  ,  "b" : black )')
    resp_2.keys = []
    resp_2.rt = []
    _resp_2_allKeys = []
    # keep track of which components have finished
    suggestionComponents = [text_8, resp_2]
    for thisComponent in suggestionComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    suggestionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "suggestion"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = suggestionClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=suggestionClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_8* updates
        if text_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_8.frameNStart = frameN  # exact frame index
            text_8.tStart = t  # local t and not account for scr refresh
            text_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_8, 'tStartRefresh')  # time at next scr refresh
            text_8.setAutoDraw(True)
        if text_8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_8.tStartRefresh + 4.5-frameTolerance:
                # keep track of stop time/frame for later
                text_8.tStop = t  # not accounting for scr refresh
                text_8.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_8, 'tStopRefresh')  # time at next scr refresh
                text_8.setAutoDraw(False)
        
        # *resp_2* updates
        waitOnFlip = False
        if resp_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            resp_2.frameNStart = frameN  # exact frame index
            resp_2.tStart = t  # local t and not account for scr refresh
            resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(resp_2, 'tStartRefresh')  # time at next scr refresh
            resp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(resp_2.clock.reset)  # t=0 on next screen flip
        if resp_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > resp_2.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                resp_2.tStop = t  # not accounting for scr refresh
                resp_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(resp_2, 'tStopRefresh')  # time at next scr refresh
                resp_2.status = FINISHED
        if resp_2.status == STARTED and not waitOnFlip:
            theseKeys = resp_2.getKeys(keyList=['w', 'b'], waitRelease=False)
            _resp_2_allKeys.extend(theseKeys)
            if len(_resp_2_allKeys):
                resp_2.keys = [key.name for key in _resp_2_allKeys]  # storing all keys
                resp_2.rt = [key.rt for key in _resp_2_allKeys]
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in suggestionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "suggestion"-------
    for thisComponent in suggestionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if resp_2.keys in ['', [], None]:  # No response was made
        resp_2.keys = None
    trials.addData('resp_2.keys',resp_2.keys)
    if resp_2.keys != None:  # we had a response
        trials.addData('resp_2.rt', resp_2.rt)
    trials.addData('resp_2.started', resp_2.tStartRefresh)
    trials.addData('resp_2.stopped', resp_2.tStopRefresh)
    
    # ------Prepare to start Routine "conf"-------
    continueRoutine = True
    routineTimer.add(5.000000)
    # update component parameters for each repeat
    text_9.setText('What is confidence rate?\n\n(0 , 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , space)')
    resp_3.keys = []
    resp_3.rt = []
    _resp_3_allKeys = []
    # keep track of which components have finished
    confComponents = [text_9, resp_3, image_8]
    for thisComponent in confComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    confClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "conf"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = confClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=confClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_9* updates
        if text_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_9.frameNStart = frameN  # exact frame index
            text_9.tStart = t  # local t and not account for scr refresh
            text_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_9, 'tStartRefresh')  # time at next scr refresh
            text_9.setAutoDraw(True)
        if text_9.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_9.tStartRefresh + 4.5-frameTolerance:
                # keep track of stop time/frame for later
                text_9.tStop = t  # not accounting for scr refresh
                text_9.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_9, 'tStopRefresh')  # time at next scr refresh
                text_9.setAutoDraw(False)
        
        # *resp_3* updates
        waitOnFlip = False
        if resp_3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            resp_3.frameNStart = frameN  # exact frame index
            resp_3.tStart = t  # local t and not account for scr refresh
            resp_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(resp_3, 'tStartRefresh')  # time at next scr refresh
            resp_3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(resp_3.clock.reset)  # t=0 on next screen flip
        if resp_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > resp_3.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                resp_3.tStop = t  # not accounting for scr refresh
                resp_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(resp_3, 'tStopRefresh')  # time at next scr refresh
                resp_3.status = FINISHED
        if resp_3.status == STARTED and not waitOnFlip:
            theseKeys = resp_3.getKeys(keyList=['space', '9', '8', '7', '6', '5', '4', '3', '2', '1', '0'], waitRelease=False)
            _resp_3_allKeys.extend(theseKeys)
            if len(_resp_3_allKeys):
                resp_3.keys = [key.name for key in _resp_3_allKeys]  # storing all keys
                resp_3.rt = [key.rt for key in _resp_3_allKeys]
                # a response ends the routine
                continueRoutine = False
        
        # *image_8* updates
        if image_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_8.frameNStart = frameN  # exact frame index
            image_8.tStart = t  # local t and not account for scr refresh
            image_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_8, 'tStartRefresh')  # time at next scr refresh
            image_8.setAutoDraw(True)
        if image_8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_8.tStartRefresh + 4.5-frameTolerance:
                # keep track of stop time/frame for later
                image_8.tStop = t  # not accounting for scr refresh
                image_8.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_8, 'tStopRefresh')  # time at next scr refresh
                image_8.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in confComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "conf"-------
    for thisComponent in confComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if resp_3.keys in ['', [], None]:  # No response was made
        resp_3.keys = None
    trials.addData('resp_3.keys',resp_3.keys)
    if resp_3.keys != None:  # we had a response
        trials.addData('resp_3.rt', resp_3.rt)
    trials.addData('resp_3.started', resp_3.tStartRefresh)
    trials.addData('resp_3.stopped', resp_3.tStopRefresh)
    trials.addData('image_8.started', image_8.tStartRefresh)
    trials.addData('image_8.stopped', image_8.tStopRefresh)
    
    # ------Prepare to start Routine "adviser_b"-------
    continueRoutine = True
    # update component parameters for each repeat
    mykey = mykey+event.getKeys()[1:]
    
    if mykey[0] == 'right':
        msg = "you selected you to advice"
    else:
        msg = "you doesn't select"
    
    massage_2.setText(msg)
    key_resp_5.keys = []
    key_resp_5.rt = []
    _key_resp_5_allKeys = []
    # keep track of which components have finished
    adviser_bComponents = [massage_2, text_12, key_resp_5, image_13, text_13, text_16]
    for thisComponent in adviser_bComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    adviser_bClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "adviser_b"-------
    while continueRoutine:
        # get current time
        t = adviser_bClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=adviser_bClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *massage_2* updates
        if massage_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            massage_2.frameNStart = frameN  # exact frame index
            massage_2.tStart = t  # local t and not account for scr refresh
            massage_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(massage_2, 'tStartRefresh')  # time at next scr refresh
            massage_2.setAutoDraw(True)
        
        # *text_12* updates
        if text_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_12.frameNStart = frameN  # exact frame index
            text_12.tStart = t  # local t and not account for scr refresh
            text_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_12, 'tStartRefresh')  # time at next scr refresh
            text_12.setAutoDraw(True)
        
        # *key_resp_5* updates
        waitOnFlip = False
        if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_5.frameNStart = frameN  # exact frame index
            key_resp_5.tStart = t  # local t and not account for scr refresh
            key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
            key_resp_5.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_5.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_5.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_5_allKeys.extend(theseKeys)
            if len(_key_resp_5_allKeys):
                key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
                key_resp_5.rt = _key_resp_5_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *image_13* updates
        if image_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_13.frameNStart = frameN  # exact frame index
            image_13.tStart = t  # local t and not account for scr refresh
            image_13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_13, 'tStartRefresh')  # time at next scr refresh
            image_13.setAutoDraw(True)
        
        # *text_13* updates
        if text_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_13.frameNStart = frameN  # exact frame index
            text_13.tStart = t  # local t and not account for scr refresh
            text_13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_13, 'tStartRefresh')  # time at next scr refresh
            text_13.setAutoDraw(True)
        
        # *text_16* updates
        if text_16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_16.frameNStart = frameN  # exact frame index
            text_16.tStart = t  # local t and not account for scr refresh
            text_16.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_16, 'tStartRefresh')  # time at next scr refresh
            text_16.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in adviser_bComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "adviser_b"-------
    for thisComponent in adviser_bComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "adviser_b" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "grid"-------
    continueRoutine = True
    routineTimer.add(1.400000)
    # update component parameters for each repeat
    advicer_turn.setText('Evidence grid\n\n\n')
    show_image_to_advicer.setImage(url)
    # keep track of which components have finished
    gridComponents = [advicer_turn, show_image_to_advicer]
    for thisComponent in gridComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    gridClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "grid"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = gridClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=gridClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *advicer_turn* updates
        if advicer_turn.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            advicer_turn.frameNStart = frameN  # exact frame index
            advicer_turn.tStart = t  # local t and not account for scr refresh
            advicer_turn.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(advicer_turn, 'tStartRefresh')  # time at next scr refresh
            advicer_turn.setAutoDraw(True)
        if advicer_turn.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > advicer_turn.tStartRefresh + 1.4-frameTolerance:
                # keep track of stop time/frame for later
                advicer_turn.tStop = t  # not accounting for scr refresh
                advicer_turn.frameNStop = frameN  # exact frame index
                win.timeOnFlip(advicer_turn, 'tStopRefresh')  # time at next scr refresh
                advicer_turn.setAutoDraw(False)
        
        # *show_image_to_advicer* updates
        if show_image_to_advicer.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            show_image_to_advicer.frameNStart = frameN  # exact frame index
            show_image_to_advicer.tStart = t  # local t and not account for scr refresh
            show_image_to_advicer.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(show_image_to_advicer, 'tStartRefresh')  # time at next scr refresh
            show_image_to_advicer.setAutoDraw(True)
        if show_image_to_advicer.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > show_image_to_advicer.tStartRefresh + 1.4-frameTolerance:
                # keep track of stop time/frame for later
                show_image_to_advicer.tStop = t  # not accounting for scr refresh
                show_image_to_advicer.frameNStop = frameN  # exact frame index
                win.timeOnFlip(show_image_to_advicer, 'tStopRefresh')  # time at next scr refresh
                show_image_to_advicer.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in gridComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "grid"-------
    for thisComponent in gridComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('show_image_to_advicer.started', show_image_to_advicer.tStartRefresh)
    trials.addData('show_image_to_advicer.stopped', show_image_to_advicer.tStopRefresh)
    
    # ------Prepare to start Routine "suggestion_2"-------
    continueRoutine = True
    routineTimer.add(5.000000)
    # update component parameters for each repeat
    text_14.setText('What is your suggested color?\n\n( "w" : white  ,  "b" : black )')
    resp_4.keys = []
    resp_4.rt = []
    _resp_4_allKeys = []
    # keep track of which components have finished
    suggestion_2Components = [text_14, resp_4]
    for thisComponent in suggestion_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    suggestion_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "suggestion_2"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = suggestion_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=suggestion_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_14* updates
        if text_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_14.frameNStart = frameN  # exact frame index
            text_14.tStart = t  # local t and not account for scr refresh
            text_14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_14, 'tStartRefresh')  # time at next scr refresh
            text_14.setAutoDraw(True)
        if text_14.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_14.tStartRefresh + 4.5-frameTolerance:
                # keep track of stop time/frame for later
                text_14.tStop = t  # not accounting for scr refresh
                text_14.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_14, 'tStopRefresh')  # time at next scr refresh
                text_14.setAutoDraw(False)
        
        # *resp_4* updates
        waitOnFlip = False
        if resp_4.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            resp_4.frameNStart = frameN  # exact frame index
            resp_4.tStart = t  # local t and not account for scr refresh
            resp_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(resp_4, 'tStartRefresh')  # time at next scr refresh
            resp_4.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(resp_4.clock.reset)  # t=0 on next screen flip
        if resp_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > resp_4.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                resp_4.tStop = t  # not accounting for scr refresh
                resp_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(resp_4, 'tStopRefresh')  # time at next scr refresh
                resp_4.status = FINISHED
        if resp_4.status == STARTED and not waitOnFlip:
            theseKeys = resp_4.getKeys(keyList=['w', 'b'], waitRelease=False)
            _resp_4_allKeys.extend(theseKeys)
            if len(_resp_4_allKeys):
                resp_4.keys = [key.name for key in _resp_4_allKeys]  # storing all keys
                resp_4.rt = [key.rt for key in _resp_4_allKeys]
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in suggestion_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "suggestion_2"-------
    for thisComponent in suggestion_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if resp_4.keys in ['', [], None]:  # No response was made
        resp_4.keys = None
    trials.addData('resp_4.keys',resp_4.keys)
    if resp_4.keys != None:  # we had a response
        trials.addData('resp_4.rt', resp_4.rt)
    trials.addData('resp_4.started', resp_4.tStartRefresh)
    trials.addData('resp_4.stopped', resp_4.tStopRefresh)
    
    # ------Prepare to start Routine "conf_2"-------
    continueRoutine = True
    routineTimer.add(5.000000)
    # update component parameters for each repeat
    text_17.setText('What is confidence rate?\n\n(0 , 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , space)')
    resp_5.keys = []
    resp_5.rt = []
    _resp_5_allKeys = []
    # keep track of which components have finished
    conf_2Components = [text_17, resp_5, image_9]
    for thisComponent in conf_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    conf_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "conf_2"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = conf_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=conf_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_17* updates
        if text_17.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_17.frameNStart = frameN  # exact frame index
            text_17.tStart = t  # local t and not account for scr refresh
            text_17.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_17, 'tStartRefresh')  # time at next scr refresh
            text_17.setAutoDraw(True)
        if text_17.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_17.tStartRefresh + 4.5-frameTolerance:
                # keep track of stop time/frame for later
                text_17.tStop = t  # not accounting for scr refresh
                text_17.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_17, 'tStopRefresh')  # time at next scr refresh
                text_17.setAutoDraw(False)
        
        # *resp_5* updates
        waitOnFlip = False
        if resp_5.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            resp_5.frameNStart = frameN  # exact frame index
            resp_5.tStart = t  # local t and not account for scr refresh
            resp_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(resp_5, 'tStartRefresh')  # time at next scr refresh
            resp_5.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(resp_5.clock.reset)  # t=0 on next screen flip
        if resp_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > resp_5.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                resp_5.tStop = t  # not accounting for scr refresh
                resp_5.frameNStop = frameN  # exact frame index
                win.timeOnFlip(resp_5, 'tStopRefresh')  # time at next scr refresh
                resp_5.status = FINISHED
        if resp_5.status == STARTED and not waitOnFlip:
            theseKeys = resp_5.getKeys(keyList=['space', '9', '8', '7', '6', '5', '4', '3', '2', '1', '0'], waitRelease=False)
            _resp_5_allKeys.extend(theseKeys)
            if len(_resp_5_allKeys):
                resp_5.keys = [key.name for key in _resp_5_allKeys]  # storing all keys
                resp_5.rt = [key.rt for key in _resp_5_allKeys]
                # a response ends the routine
                continueRoutine = False
        
        # *image_9* updates
        if image_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_9.frameNStart = frameN  # exact frame index
            image_9.tStart = t  # local t and not account for scr refresh
            image_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_9, 'tStartRefresh')  # time at next scr refresh
            image_9.setAutoDraw(True)
        if image_9.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_9.tStartRefresh + 4.5-frameTolerance:
                # keep track of stop time/frame for later
                image_9.tStop = t  # not accounting for scr refresh
                image_9.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_9, 'tStopRefresh')  # time at next scr refresh
                image_9.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in conf_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "conf_2"-------
    for thisComponent in conf_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if resp_5.keys in ['', [], None]:  # No response was made
        resp_5.keys = None
    trials.addData('resp_5.keys',resp_5.keys)
    if resp_5.keys != None:  # we had a response
        trials.addData('resp_5.rt', resp_5.rt)
    trials.addData('resp_5.started', resp_5.tStartRefresh)
    trials.addData('resp_5.stopped', resp_5.tStopRefresh)
    trials.addData('image_9.started', image_9.tStartRefresh)
    trials.addData('image_9.stopped', image_9.tStopRefresh)
    
    # ------Prepare to start Routine "feedback"-------
    continueRoutine = True
    # update component parameters for each repeat
    tmp = event.getKeys()
    mykey = mykey+tmp[1:]
    #__________________________________________
    if corrAns=='w':
        msg='lottery ticket was « white »'
    else:
        msg='lottery ticket was « black »'
    #__________________________________________    
    if mykey[0]=='left':
        msg = 'Congrass\n\n'+msg+'\n&' if mykey[1]==corrAns else 'Opps...!\n\n'+msg+'\nbut'
        msg=msg+' you select red adviser\n←'
    else:
        msg = 'Congrass\n\n'+msg+'\n&' if mykey[3]==corrAns else 'Opps...!\n\n'+msg+'\nbut'
        msg=msg+' you select blue adviser\n→'
    #__________________________________________
    mykey[2] = '100' if mykey[2]=='space' else mykey[2][-1]+'0'
        
    if mykey[1]=='w':
        red='advise white ticket \n by '+mykey[2]+'% of confidence'
    else:
        red='advise black ticket \n by '+mykey[2]+'% of confidence'
    #__________________________________________
    mykey[4] = '100' if mykey[4]=='space' else mykey[4][-1]+'0'
    
    if mykey[3]=='w':
        blue='advise white ticket \n by '+mykey[4]+'% of confidence'
    else:
        blue='advise black ticket \n by '+mykey[4]+'% of confidence'
    key_resp_7.keys = []
    key_resp_7.rt = []
    _key_resp_7_allKeys = []
    msg_c.setText(msg)
    key_resp_8.keys = []
    key_resp_8.rt = []
    _key_resp_8_allKeys = []
    msg_r.setText(red)
    msg_b.setText(blue)
    # keep track of which components have finished
    feedbackComponents = [key_resp_7, msg_c, image_c, client_turn, image_r, image_b, key_resp_8, text_2, msg_r, msg_b]
    for thisComponent in feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    feedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "feedback"-------
    while continueRoutine:
        # get current time
        t = feedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=feedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *key_resp_7* updates
        waitOnFlip = False
        if key_resp_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_7.frameNStart = frameN  # exact frame index
            key_resp_7.tStart = t  # local t and not account for scr refresh
            key_resp_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_7, 'tStartRefresh')  # time at next scr refresh
            key_resp_7.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_7.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_7.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_7.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_7.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_7_allKeys.extend(theseKeys)
            if len(_key_resp_7_allKeys):
                key_resp_7.keys = _key_resp_7_allKeys[-1].name  # just the last key pressed
                key_resp_7.rt = _key_resp_7_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *msg_c* updates
        if msg_c.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            msg_c.frameNStart = frameN  # exact frame index
            msg_c.tStart = t  # local t and not account for scr refresh
            msg_c.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(msg_c, 'tStartRefresh')  # time at next scr refresh
            msg_c.setAutoDraw(True)
        
        # *image_c* updates
        if image_c.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_c.frameNStart = frameN  # exact frame index
            image_c.tStart = t  # local t and not account for scr refresh
            image_c.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_c, 'tStartRefresh')  # time at next scr refresh
            image_c.setAutoDraw(True)
        
        # *client_turn* updates
        if client_turn.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            client_turn.frameNStart = frameN  # exact frame index
            client_turn.tStart = t  # local t and not account for scr refresh
            client_turn.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(client_turn, 'tStartRefresh')  # time at next scr refresh
            client_turn.setAutoDraw(True)
        
        # *image_r* updates
        if image_r.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_r.frameNStart = frameN  # exact frame index
            image_r.tStart = t  # local t and not account for scr refresh
            image_r.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_r, 'tStartRefresh')  # time at next scr refresh
            image_r.setAutoDraw(True)
        
        # *image_b* updates
        if image_b.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_b.frameNStart = frameN  # exact frame index
            image_b.tStart = t  # local t and not account for scr refresh
            image_b.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_b, 'tStartRefresh')  # time at next scr refresh
            image_b.setAutoDraw(True)
        
        # *key_resp_8* updates
        waitOnFlip = False
        if key_resp_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_8.frameNStart = frameN  # exact frame index
            key_resp_8.tStart = t  # local t and not account for scr refresh
            key_resp_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_8, 'tStartRefresh')  # time at next scr refresh
            key_resp_8.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_8.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_8.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_8.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_8.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_8_allKeys.extend(theseKeys)
            if len(_key_resp_8_allKeys):
                key_resp_8.keys = _key_resp_8_allKeys[-1].name  # just the last key pressed
                key_resp_8.rt = _key_resp_8_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *text_2* updates
        if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_2.frameNStart = frameN  # exact frame index
            text_2.tStart = t  # local t and not account for scr refresh
            text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
            text_2.setAutoDraw(True)
        
        # *msg_r* updates
        if msg_r.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            msg_r.frameNStart = frameN  # exact frame index
            msg_r.tStart = t  # local t and not account for scr refresh
            msg_r.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(msg_r, 'tStartRefresh')  # time at next scr refresh
            msg_r.setAutoDraw(True)
        
        # *msg_b* updates
        if msg_b.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            msg_b.frameNStart = frameN  # exact frame index
            msg_b.tStart = t  # local t and not account for scr refresh
            msg_b.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(msg_b, 'tStartRefresh')  # time at next scr refresh
            msg_b.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedback"-------
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "feedback" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


# ------Prepare to start Routine "thanks"-------
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
thanksComponents = [thanksText]
for thisComponent in thanksComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
thanksClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "thanks"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = thanksClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=thanksClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *thanksText* updates
    if thanksText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        thanksText.frameNStart = frameN  # exact frame index
        thanksText.tStart = t  # local t and not account for scr refresh
        thanksText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(thanksText, 'tStartRefresh')  # time at next scr refresh
        thanksText.setAutoDraw(True)
    if thanksText.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > thanksText.tStartRefresh + 2.0-frameTolerance:
            # keep track of stop time/frame for later
            thanksText.tStop = t  # not accounting for scr refresh
            thanksText.frameNStop = frameN  # exact frame index
            win.timeOnFlip(thanksText, 'tStopRefresh')  # time at next scr refresh
            thanksText.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in thanksComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "thanks"-------
for thisComponent in thanksComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
