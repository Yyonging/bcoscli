cod
-----
easy to use the click package to add command for a interactive terminal!
1. support autocompetation
2. support arrow up or down for history command

Installing
-----

Install and update using `pip`:



    pip install -U bcoscli


A Simple Example
-----

.. code-block:: python
    # use in terminal:
    # default rpc port is 8545
    just: python bcoscli 127.0.0.1:8545

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

