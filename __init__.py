"""
Skill remote-debug-skill
Copyright (C) 2020  Andreas Lorensen

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from mycroft import MycroftSkill, intent_file_handler
from mycroft.configuration.config import LocalConf, USER_CONFIG, Configuration
from mycroft.messagebus.message import Message
import os
import subprocess
import ptvsd


class RemoteDebug(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    def initialize(self):
        if not self.settings.get('padatious_single_thread'):
            self.settings['padatious_single_thread'] = Configuration.get()['padatious']["single_thread"]

        if self.settings['padatious_single_thread'] is not Configuration.get()['padatious']["single_thread"]:
            self.set_single_thread(self.settings['padatious_single_thread'])

    @intent_file_handler('debug.remote.intent')
    def handle_debug_remote(self, message):
        self.log.info('Starting PTVSD - Python Tools for Visual Studio debug server.....')
        self.set_single_thread(True)
        self.log.info('')
        try:
            ptvsd.enable_attach(address=('0.0.0.0', '5678'))
            self.log.info('Debugserver port 5678 reddy for attatch.')
            self.log.info('THEIA IDE is alreddy setup so you just have to start debug from debug menu')
        except Exception:
            self.log.info('PTVSD already running')

    @intent_file_handler('stop.debug.remote.intent')
    def handle_stop_debug_remote(self, message):
        self.log.info('Stoppig PTVSD - Python Tools for Visual Studio debug server.....')
        self.set_single_thread(self.settings['padatious_single_thread'])
        self.log.info('Restarting skillservice')
        subprocess.Popen('mycroft-start skills restart', preexec_fn=os.setsid, shell=True)

    def set_single_thread(self, update):
        new_config = {
                       'padatious': {
                       'single_thread': update
                        }
                     }
        user_config = LocalConf(USER_CONFIG)
        user_config.merge(new_config)
        user_config.store()
        self.log.info('Setting padatious single_thread = ' + str(update))
        self.bus.emit(Message('configuration.updated'))

    def shutdown(self):
        self.set_single_thread(self.settings['padatious_single_thread'])


def create_skill():
    return RemoteDebug()

