#!/usr/bin/python

from gi.repository import Notify
import gettext
import os

gettext.install("dsctl-detect-media-removal")
Notify.init("dsctl-detect-media-removal")
pyn = Notify.Notification()
pyn.set_urgency(Notify.Urgency.CRITICAL)
pyn.set_timeout(Notify.EXPIRES_NEVER)
pyn.set_app_name("DSCTL")
os.environ['XAUTHORITY'] = "/home/ubuntu/.Xauthority"
os.environ['DISPLAY'] = ":0.0"

pyn.update(_("Warning: Media removed!"), _("The media containing the Discreete Linux system has been removed. Discreete Linux will become unstable. Save your work immediately and reboot!"), "important")
pyn.show() 
