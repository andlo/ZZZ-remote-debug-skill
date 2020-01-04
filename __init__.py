from mycroft import MycroftSkill, intent_file_handler
import subprocess
from mycroft.configuration.config import LocalConf, USER_CONFIG, Configuration
from mycroft.messagebus.message import Message
import subprocess


class RemoteDebug(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('debug.remote.intent')
    def handle_debug_remote(self, message):
        self.log.info('Starting PTVSD - Python Tools for Visual Studio debug server.....')
        self.log.info('Setting padatious single_thread = true so skillsservice runs in single thread.')
        self.log.info('A sideeffect from that everything is not as fast as normal.')
        self.log.info('To inject PTVSD into mycroft.skills skillservice will be restarted.')
        self.log.info('After restart of skillservice, all skills are loaded and you are readdy to go.')
        self.log.info('')
        self.log.info('Debugserver is on port 5678 reddy for attatch.')
        self.log.info('THEIA IDE is alreddy setup so you just have to start debug from debug menu')
        self.log.info('')
        self.log.info('When finish debugging - single_thread settings are restored and skillservice')
        self.log.info('are restarted. Restarting skillservice when debugger is injected will not work!')
        self.log.info('you have to start (or stop and start or just stop) debug from the skill.')
        self.log.info('')
        self.log.info('Happy Mycrofting.')
        self.log.info('')
        self.padatious_single_thread(True)
        proc = subprocess.Popen(self.root_dir + '/BeginDebug.sh', shell=True)
        proc.wait()

    @intent_file_handler('stop.debug.remote.intent')
    def handle_stop_debug_remote(self, message):
        self.log.info('Stoppig PTVSD - Python Tools for Visual Studio debug server.....')
        self.log.info('Setting padatious single_thread = false')
        self.log.info('Restarting skillservice')
        self.padatious_single_thread(False)
        proc = subprocess.Popen(self.root_dir + '/EndDebug.sh', shell=True)
        proc.wait

    def padatious_single_thread(self, update):
        if update is True:
            new_config = {
                'padatious': {
                    "single_thread": "true"
                    }
            }
        if update is False:
            new_config = {
                'padatious': {
                    "single_thread": "false"
                    }
            }
        user_config = LocalConf(USER_CONFIG)
        user_config.merge(new_config)
        user_config.store()
        self.bus.emit(Message('configuration.updated'))


def create_skill():
    return RemoteDebug()

