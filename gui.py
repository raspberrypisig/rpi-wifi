#!/usr/bin/env python3

# Before running
# pip3 install PySimpleGUI

import PySimpleGUI as gui
from enum import Enum

class Windows(Enum):
  FIRSTWINDOW=1
  APMODEWINDOW=2
  RESETWINDOW=3

firstLayout = [
           [gui.Text('AP Mode or Normal(Reset) Mode')],
           [gui.Button('AP Mode'), gui.Button('Normal Mode')]
         ]

apModeWindowLayout = [
                     [gui.Text('Enter AP SSID          '), gui.Input()],
                     [gui.Text('Enter AP Password   '), gui.Input()],
                     [gui.Text('Enter client SSID      '), gui.Input()],
                     [gui.Text('Enter client password'), gui.Input()],
                     [gui.Button('Enter AP Mode')]

                   ]

resetWindowLayout = [
                      [gui.Text('We are about to undo AP Mode and revert back to Normal. Continue?')],
                      [gui.Button('Yes'), gui.Button('No')]
                    ]

GUIWindow = gui.Window('RPI Wifi').layout(firstLayout)
currentWindow = Windows.FIRSTWINDOW

while True:
  ev1, vals1 = GUIWindow.Read()
  
  if ev1 is None or ev1 == 'Exit':
    print('Exiting')
    break

  if currentWindow == Windows.FIRSTWINDOW and ev1 == 'AP Mode':
    GUIWindow.Hide()
    currentWindow = Windows.APMODEWINDOW
    MainWindow = gui.Window('RPI WIFI').layout(apModeWindowLayout.copy())  
    while True:
      ev2, vals2 = MainWindow.Read()
      if ev2 is None or ev2 == 'Exit':
        currentWindow = Windows.FIRSTWINDOW
        MainWindow.Close()
        GUIWindow.UnHide()
        break

  if currentWindow == Windows.FIRSTWINDOW and ev1 == 'Normal Mode':
    GUIWindow.Hide()
    currentWindow = Windows.RESETWINDOW
    MainWindow = gui.Window('RPI WIFI').layout(resetWindowLayout.copy())  
    while True:
      ev2, vals2 = MainWindow.Read()
      if ev2 is None or ev2 == 'Exit':
        currentWindow = Windows.FIRSTWINDOW
        MainWindow.Close()
        GUIWindow.UnHide()
        break

        



  