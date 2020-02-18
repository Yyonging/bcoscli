import sys
import bcoscli

if __name__ == "__main__":
    if len(sys.argv) > 1:
        bcoscli.Config.HOST_RPC = 'http://'+sys.argv[1]
    bcoscli.main()
