
PLAIN = "plain"
PLAIN_UP = "plain_uppercase"
PLAIN_LO = "plain_lowercase"
JSON = "json"
XML = "xml"

SUPPORTED = [PLAIN, PLAIN_UP, PLAIN_LO, JSON, XML]


def get_formatted(msg, imie, nazwisko, format):
    result = ""
    if format == PLAIN:
        result = plain_text(msg, imie, nazwisko)
    elif format == PLAIN_UP:
        result = plain_text_upper_case(msg, imie, nazwisko)
    elif format == PLAIN_LO:
        result = plain_text_lower_case(msg, imie, nazwisko)
    elif format == JSON:
        result = format_to_json(msg, imie, nazwisko)
    elif format == XML:
        result = format_to_xml(msg, imie, nazwisko)
    return result


def format_to_json(msg, imie, nazwisko):
    return ('{ "imie":"' + imie + '", "nazwisko":"' + nazwisko + '", "mgs":"' +
            msg + '"}')


def format_to_xml(msg, imie, nazwisko):
    return ('<greetings><name>' + imie + '</name><surname>' +
            nazwisko + '</surname><msg>' +
            msg + '</msg></greetings>')


def plain_text(msg, imie, nazwisko):
    return imie + ' ' + nazwisko + ' ' + msg


def plain_text_upper_case(msg, imie, nazwisko):
    return plain_text(msg.upper(), imie.upper(), nazwisko.upper())


def plain_text_lower_case(msg, imie, nazwisko):
    return plain_text(msg.lower(), imie.lower(), nazwisko.lower())
