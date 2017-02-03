from TranscriptionService.src.ImapConnection import ImapConnection


class Scribe(object):

    def __init__(self):
        self._scan = None
        self._write = None
