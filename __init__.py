from mycroft import MycroftSkill, intent_file_handler


class RemoteDebug(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('debug.remote.intent')
    def handle_debug_remote(self, message):
        self.speak_dialog('debug.remote')


def create_skill():
    return RemoteDebug()

