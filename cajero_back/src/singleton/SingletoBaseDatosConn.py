

class SingletoBaseDatosConn(type):
    _instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance == None:
            cls._instance[cls] = super().__call__(*args, **kwargs)
        return cls._instance[cls]

