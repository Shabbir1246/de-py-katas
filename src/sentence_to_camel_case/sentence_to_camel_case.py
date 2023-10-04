def sentence_to_camel_case(arg1, arg):
    title_format = arg1.title().replace(' ', '')
    if arg == True:
        return title_format
    else: 
        return title_format[0].lower() + title_format[1:]