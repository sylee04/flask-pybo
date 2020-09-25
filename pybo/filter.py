#def format_datetime(value, fmt='%Y년 %m월 %d일 %H:%M'):
def format_datetime(value, fmt='%Y. %m. %d. %H:%M'):
    return value.strftime(fmt)
#UnicodeEncodeError: 'locale' codec can't encode character '\ub144' in position 2: Illegal byte sequence