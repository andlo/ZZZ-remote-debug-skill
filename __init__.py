from mycroft import MycroftSkill, intent_file_handler
from mycroft.configuration.config import LocalConf, USER_CONFIG, Configuration
from mycroft.messagebus.message import Message
import subprocess
import ptvsd


class RemoteDebug(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    def initialize(self):
        self.padatious_config = Configuration.get()['padatious']
        if self.padatious_config.get("single_thread"):
            self.single_thread = self.padatious_config["single_thread"]
        else:
            self.single_thread = "False"



    @intent_file_handler('debug.remote.intent')
    def handle_debug_remote(self, message):
        self.log.info('Starting PTVSD - Python Tools for Visual Studio debug server.....')
        self.set_single_thread(True)
        self.log.info('')
        try:
            ptvsd.enable_attach(address=('0.0.0.0', '5678'), log_dir='/var/log/mycroft')
            self.log.info('Debugserver port 5678 reddy for attatch.')
            self.log.info('THEIA IDE is alreddy setup so you just have to start debug from debug menu')
            self.log.info('')
            self.log.info('When finish debugging - single_thread settings are restored and skillservice')
            self.log.info('are restarted. Restarting skillservice when debugger is injected will end PTVSD,')
            self.log.info('but not reset single_thread setting.')
            self.log.info('')
            self.log.info('Happy Mycrofting.')
            self.log.info('')
        except Exception:
            self.log.info('PTVSD already running')


    @intent_file_handler('stop.debug.remote.intent')
    def handle_stop_debug_remote(self, message):
        self.log.info('Stoppig PTVSD - Python Tools for Visual Studio debug server.....')
        self.set_single_thread(self.single_thread)
        self.log.info('Restarting skillservice')
        subprocess.Popen('mycroft-start skills restart',
                         cwd=self.SafePath, preexec_fn=os.setsid, shell=True)
        self.test = None

    def set_single_thread(self, update):
        new_config = {
                       'padatious': {
                       'single_thread': str(update)
                        }
                     }
        user_config = LocalConf(USER_CONFIG)
        user_config.merge(new_config)
        user_config.store()
        self.log.info('Setting padatious single_thread = ' + str(update))
        self.bus.emit(Message('configuration.updated'))

    def shutdown(self):
        self.set_single_thread(self.single_thread)


def create_skill():
    return RemoteDebug()

