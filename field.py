def field(items, *args):
    assert len(args) > 0
    result = []
    for seti in items:
        args_in_seti = [arg for arg in args if arg in seti]
        result.append({arg: seti[arg] for arg in args_in_seti} if len(args) > 1 else seti[args_in_seti[0]] if len(args_in_seti) > 0 else None)
    while None in result:
        result.remove(None)
    while {} in result:
        result.remove({})
    return result