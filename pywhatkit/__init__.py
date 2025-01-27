""" Version 5.4
# Status: Development

"""
__VERSION__ = "Version 5.4 (Development)"

from platform import system

from pywhatkit.ascii_art import image_to_ascii_art
from pywhatkit.handwriting import text_to_handwriting
from pywhatkit.mail import send_hmail, send_mail
from pywhatkit.misc import info, playonyt, search, show_history
from pywhatkit.sc import cancel_shutdown, shutdown
from pywhatkit.whats import (
    open_web,
    sendwhatmsg,
    sendwhatmsg_instantly,
    sendwhatmsg_to_group,
    sendwhatmsg_to_group_instantly,
    sendwhats_image,
    sendwhatdoc_immediately,
    sendimg_or_video_immediately
)

_system = system().lower()
if _system in ("darwin", "windows"):
    from pywhatkit.misc import take_screenshot

if _system == "windows":
    from pywhatkit.remotekit import start_server
