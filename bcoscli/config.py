class Config:

    HOST_RPC = 'http://127.0.0.0:8545' # your fisco-bcos node's rpc address
    ECHO = 1  # open the terminal output, set 0 for close

def set_config(cls=None):
    for key in cls.__dict__:
        if not key.startswith("__"):
            setattr(Config, key, getattr(cls, key, None))
