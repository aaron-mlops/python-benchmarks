import argparse
import time
import requests
import concurrent.futures


def request_sleep():
    start_time = time.time()
    _ = requests.get("http://localhost:8002/sleep")
    end_time = time.time()
    return end_time - start_time


if __name__ == "__main__":
    # parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--num_users", type=int, default=10)
    parser.add_argument("--total_requests", type=int, default=100)
    args = parser.parse_args()

    pool = concurrent.futures.ThreadPoolExecutor(max_workers=args.num_users)

    total_start_time = time.time()

    procs = []
    for i in range(args.total_requests):
        procs.append(pool.submit(request_sleep))

    times = []
    for p in concurrent.futures.as_completed(procs):
        times.append(p.result())

    total_end_time = time.time()

    print(f"num_users: {args.num_users}, total_requests: {args.total_requests}")
    print("avg:")
    print(round(sum(times) / len(times), 5))
    print("total:")
    print(round(total_end_time - total_start_time, 5))
