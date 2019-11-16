def fcounter(Class, *args, **kwargs):
    fields    = set(i for i in dir(Class) if not i.startswith("_") and not callable(getattr(Class, i)))
    functions = set(i for i in dir(Class) if not i.startswith("_") and callable(getattr(Class, i)))
    
    C = Class(*args, **kwargs)

    fields_new    = set(i for i in dir(C) if not i.startswith("_") and not callable(getattr(C, i)))
    functions_new = set(i for i in dir(C) if not i.startswith("_") and callable(getattr(C, i)))

    return (sorted(list(functions)), sorted(list(fields)),  sorted(list(functions_new - functions)), sorted(list(fields_new - fields)))
