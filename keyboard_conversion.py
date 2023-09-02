# (You can map your own keyboard)

class To:
   AZERTY = "azerty"
   QWERTY = "qwerty"

AZERTY_MAP = """@&é"‘(§è!çà)-azertyuiop^$qsdfghjklmù`<wxcvbn,;:=#1234567890°_AZERTYUIOP¨*QSDFGHJKLM%£>WXCVBN?./+ """
QWERTY_MAP = """§1234567890-=qwertyuiop[]asdfghjkl;’\`zxcvbnm,./±!@#$%^&*()_+QWERTYUIOP{}ASDFGHJKL:"|~ZXCVBNM<>? """



def keyboard_conversion(message: str, to: str) -> str:
    """
    A Keyboard Conversion to switch the Azerty keyboard to the Qwerty keyboard and vise-versa
    """
    match to:
        case To.AZERTY:
            conversion_dict = dict(zip(QWERTY_MAP, AZERTY_MAP))
        case To.QWERTY:
            conversion_dict = dict(zip(AZERTY_MAP, QWERTY_MAP))
        case _:
            raise ValueError("The to option is not valable, check the To class")
        
    if not type(message) == str:
        raise ValueError(f"{type(message)} is not class string")
    new_message = ""
    for character in message:
        new_message += conversion_dict[character]
    return new_message
