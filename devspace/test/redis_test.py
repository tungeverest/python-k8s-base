import os
import redis


def redis_test_connect():
    redis_password = os.environ.get("REDIS_PASSWORD", "wesang")
    is_cluster = os.environ.get("IS_LOCAL_CLUSTER")
    ip_cluster = os.environ.get("LOCAL_CLUSTER_IP")
    port = 6379
    if is_cluster:
        redis_host = 'redis-svc'
    else:
        port = 30379
        redis_host = ip_cluster

    print("REDIS_PASSWORD", redis_password)
    _redis_pool = redis.ConnectionPool(
        host=redis_host,
        port=port,
        password=redis_password,
        db=0,
        decode_responses=True,
        socket_connect_timeout=30
    )
    try:
        redis_client = redis.Redis(connection_pool=_redis_pool)
    except Exception:
        raise Exception("Redis can't connect")
    redis_client.ping()
    print("Redis connected")
