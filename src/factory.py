from TranscriptionService.src.Scribe import Scribe


def get_scribe():
    """Get an instance of Scribe
    Scribe can either transcribe wav files from emails or a dB
    Get/Check settings for IMAP Connection
    Initialize Scribe with IMAP Connection
    Get/Check settings for dB Connection
    Initialize Scribe with dB Connection
    :return: Scribe()
    """
    return Scribe()
