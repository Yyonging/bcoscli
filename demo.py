
class MyConfig:

    HOST_RPC = 'http://192.168.0.107:9545' # your fisco-bcos node's rpc address
    ECHO = 0 # close the terminal output 

if __name__ == "__main__":
    import bcoscli
    # use bcoscli as sdk
    # define your config
    bcoscli.set_config(MyConfig)
    print(bcoscli.getClientVersion())
    print(bcoscli.getBlockNumber(11))

    # use bcoscli as terminal tool
    # define your config
    bcoscli.Config.HOST_RPC = 'http://192.168.0.107:9545'
    bcoscli.Config.ECHO = 1 # open terminal ouput, default is 1
    bcoscli.main()
