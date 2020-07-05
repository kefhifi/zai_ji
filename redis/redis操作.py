from redis import *


def main():
    try:
        redis_obj = StrictRedis(host="119.45.0.4", port=39328, db=0, decode_responses=True, password="H3z5udsuz7ze_Pk7w8qp2")
    except Exception as ret:
        print(ret)
    else:
        if not redis_obj.set("hello", "12345"):
            print("redis set error!")
            exit(1)
        print(redis_obj.get("hello"))


if __name__ == "__main__":
    main()

