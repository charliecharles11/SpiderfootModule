# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# Name:         sfp_new_module
# Purpose:      SpiderFoot plug-in for creating new modules.
#
# Author:      Carlos Díaz Gil <cdiaz5638@gmail.com>
#
# Created:     23/07/2022
# Copyright:   (c) Carlos Díaz Gil 2022
# Licence:     GPL
# -------------------------------------------------------------------------------


from spiderfoot import SpiderFootEvent, SpiderFootPlugin
import socket

class sfp_new_module(SpiderFootPlugin):

    meta = {
        'name': "GetIPbyHostName",
        'summary': "Get the IP through the domain name",
        'flags': [""],
        'useCases': [""],
        'categories': ["Passive DNS"]
    }

    # Default options
    opts = {
    }

    # Option descriptions
    optdescs = {
    }

    results = None

    def setup(self, sfc, userOpts=dict()):
        self.sf = sfc
        self.results = self.tempStorage()

        for opt in list(userOpts.keys()):
            self.opts[opt] = userOpts[opt]

    # What events is this module interested in for input
    def watchedEvents(self):
        return ["DOMAIN_NAME", "DOMAIN_NAME_PARENT", "CO_HOSTED_SITE_DOMAIN", 
                "AFFILIATE_DOMAIN_NAME", "SIMILARDOMAIN"]

    # What events this module produces
    # This is to support the end user in selecting modules based on events
    # produced.
    def producedEvents(self):
        return ["IP_ADDRESS"]

    # Handle events sent to this module
    def handleEvent(self, event):
        eventName = event.eventType
        srcModuleName = event.module
        eventData = event.data

        if eventData in self.results:
            return

        self.results[eventData] = True

        self.sf.debug(f"Received event, {eventName}, from {srcModuleName}")

        try:
            data = None

            self.sf.debug(f"We use the data: {eventData}")
            print(f"We use the data: {eventData}")

            data = socket.gethostbyname(eventData)

            if not data:
                self.sf.error("Unable to perform <ACTION MODULE> on " + eventData)
                return
        except Exception as e:
            self.sf.error("Unable to perform the <ACTION MODULE> on " + eventData + ": " + str(e))
            return

        typ = "DOMAIN_NAME"
        data = "newdomaintest.com"

        evt = SpiderFootEvent("IP_ADDRESS", data, self.__name__, event)
        self.notifyListeners(evt)

# End of sfp_new_module class