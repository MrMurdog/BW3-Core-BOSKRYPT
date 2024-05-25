#!/usr/bin/python
# -*- coding: utf-8 -*-
r"""!
    ____  ____  ______       __      __       __       _____
   / __ )/ __ \/ ___/ |     / /___ _/ /______/ /_     |__  /
  / __  / / / /\__ \| | /| / / __ `/ __/ ___/ __ \     /_ <
 / /_/ / /_/ /___/ /| |/ |/ / /_/ / /_/ /__/ / / /   ___/ /
/_____/\____//____/ |__/|__/\__,_/\__/\___/_/ /_/   /____/
                German BOS Information Script
                     by Bastian Schroll

@file:        template_module.py
@date:        25.05.2024
@author:      MrMurdog
@description: BoskryptLibrary Handler
@version:     1.0.0
@dev_state    in proc...
"""
import logging
from module.moduleBase import ModuleBase

# ###################### #
# Custom plugin includes #

from module.lib.BoskryptLibary import Decrypt

# ###################### #

logging.debug("- %s loaded", __name__)


class BoswatchModule(ModuleBase):
    r"""!Description of the Module"""
    def __init__(self, config):
        r"""!Do not change anything here!"""
        super().__init__(__name__, config)  # you can access the config class on 'self.config'

    def onLoad(self):
        r"""!Called by import of the plugin
        Remove if not implemented"""
        
        self.registerWildcard('DMSG', 'dec_message') # Wildcard {DMSG} | dec_message für die unverschlüsselte Naricht registriert
        # self.registerWildcard('DKEY', 'des_key') # Wildcard {DKEY} | des_key für die beschreibung des Key´s / für debug zwecke
        # self.registerWildcard('BKKEY', 'bk_key') # Wildcard {BKKEY} | bk_key für den Boskrypt key / Multikey support ausstehend./ für debug
        
        
    def doWork(self, bwPacket):
        r"""!start an run of the module.

        @param bwPacket: A BOSWatch packet instance"""
        if bwPacket.get("mode") == "fms":
            pass
        elif bwPacket.get("mode") == "zvei":
            pass
        elif bwPacket.get("mode") == "pocsag":
            
            load_conf_dkey = self.config.get("des_key") # wird nur für entwicklungszwecke verwendet
            load_conf_bkkey = self.config.get("bk_key") # Der BKKey
            
            logging.debug(f'Lade {load_conf_dkey} | {load_conf_bkkey} in den Decrypter')
            
            fetch_msg = bwPacket.get('message')
            
            decode = Decrypt(load_conf_bkkey, fetch_msg)
            
            logging.debug(f'Das Ergebniss vom Decrypter: {decode}')
            
            bwPacket.set('DMSG', decode)
            
            logging.debug('BW Paket wurde erstellt und mit dem Wert versehen.')
            
            return bwPacket
            
            pass
        elif bwPacket.get("mode") == "msg":
            pass

        return bwPacket

    def onUnload(self):
        r"""!Called by destruction of the plugin
        Remove if not implemented"""
        pass
