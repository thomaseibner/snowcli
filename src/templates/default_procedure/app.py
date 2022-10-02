# Test locally
# > python app.py
#
# Create and deploy in snowflake:
# > snowcli procedure package
# > snowcli procedure create --environment dev
# > snowcli procedure call -f 'helloProcedure()'
import sys


def hello() -> str:
    return 'Hello World!'


# For local debugging. Be aware you may need to type-convert arguments if you add input parameters
if __name__ == '__main__':
    if len(sys.argv) > 1:
        print(hello(sys.argv[1:]))  # type: ignore
    else:
        print(hello())