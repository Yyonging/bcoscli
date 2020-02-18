bcoscli
-----
*** more convenient then the offical skd ***

easy to use the FISCO-BCOS blockchain for a interactive terminal!  

easy to use the FISCO-BCOS blockchain as sdk!  

1. config so easy
2. support autocompetation
3. support arrow up or down for history command
4. colorful

Installing
-----

Install and update using `pip`:



    pip install -U bcoscli


A Simple Example
-----

as terminal just:



    # default rpc port is 8545
    
    python bcoscli 127.0.0.1:8545

as sdk:

.. code-block:: python



    class MyConfig:

        HOST_RPC = 'http://192.168.0.107:9545' # your fisco-bcos node's rpc address
        ECHO = 0 # close the terminal output 

    if __name__ == "__main__":
        import bcoscli
        # define your config
        bcoscli.set_config(MyConfig)
        print(bcoscli.getClientVersion())
        print(bcoscli.getBlockNumber(11))
