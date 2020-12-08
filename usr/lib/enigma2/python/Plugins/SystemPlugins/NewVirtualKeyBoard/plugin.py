#!/usr/bin/python
# -*- coding: utf-8 -*-

from Plugins.Plugin import PluginDescriptor
from Components.config import config
from enigma import getDesktop
from Plugins.SystemPlugins.NewVirtualKeyBoard.VirtualKeyBoard import *

screenwidth = getDesktop(0).size()

def main(session, **kwargs):
	from .VirtualKeyBoard import nvKeyboardSetup
	session.open(nvKeyboardSetup)


def menu(menuid, **kwargs):
	if menuid == 'system':
		return [(_('VirtualKeyBoard setup'), main, 'virtulkeyBoard_setup', None)]
	else:
		return []

ICONFILE = 'images/plugin-icon_sd.png'
if screenwidth.width() > 1280:
	ICONFILE = 'images/plugin-icon.png'
DES = (_('Setup virtual keyboard'))
PNAME = (_('VirtualKeyboard'))
pluginlist = PluginDescriptor(name=PNAME, description=DES, where=PluginDescriptor.WHERE_PLUGINMENU, icon=ICONFILE, fnc=main, needsRestart=False)

def Plugins(**kwargs):
	result = [
		PluginDescriptor(
			name=PNAME,
			description = DES,
			where = PluginDescriptor.WHERE_MENU,
			fnc = menu,
			needsRestart=False
		),
	]
	if config.NewVirtualKeyBoard.showinplugins.value:
		result.append(pluginlist)
	return result
