from redis import *

if __name__ == "__main__":
    try:
        sr = StrictRedis(host='localhost', port=6379, db=0)
        result = sr.get("a")
        print(result)
    except Exception as e:
        print(e)

