# -*- coding: utf-8 -*-
"""Manarati welcome speech test

"""

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

import GPIO
__author__ = 'Capt-ley'

LOGGER = getLogger(__Capt-ley__)

class WelcomeManaratiSkill(MycroftSkill):

    def __init__(self):
        super(WelcomeManaratiSkill, self).__init__(name="WelcomeManaratiSkill")
        """You don't have to include the constructor unless you plan to declare state variables for the Skill object. 
        If you plan to declare state variables, then they should be defined in this block. 
        If you don't include the constructor, the name of the Skill will be taken from the name of the class, 
        in this case 'WelcomeManaratiSkill'."""
        self.already_said_hello = False
        self.be_friendly = True
        self.hello_phrases = ['Hello', 'Hallå', 'Olá']

    def initialize(self):
        manaratiactivate_intent = IntentBuilder("manaratiactivate").require("manaratiactivate").build()
        self.register_intent(manaratiactivate_intent, self.handle_manaratiactivate_intent)


    def handle_manaratiactivate_intent(self, message):
        self.speak_dialog("welcomemanarati")












