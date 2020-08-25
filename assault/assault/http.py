import asyncio
import time
import os
import requests


def fetch(url):
    """ Make the request and return the results """
    started_at = time.monotonic()
    response = requests.get(url)
    request_time = time.monotonic() - started_at
    return {"status_code": response.status_code, "request_time": request_time}


# Worker's job is to listen forever, and if something comes into the queue to be done, it takes item off of the queue, executes it and returns results by appending it to results list
async def worker(name, queue, results):
    """ A function to take unmade requests from a queue and perform the work then add results to the results list.  """
    loop = asyncio.get_event_loop()
    while True:
        url = await queue.get()
        if os.getenv("DEBUG"):
            print(f"{name} - Fetching {url}")
        future_result = loop.run_in_executor(
            None, fetch, url
        )  # spawn a task, schedule work to be done (running a function), url is the arg to be passed
        result = await future_result
        results.append(result)
        queue.task_done()


async def distribute_work(url, requests, concurrency, results):
    """ Divide up the work into batches and collect the final results """
    queue = asyncio.Queue()  # Queue to hold onto all of the jobs that we want to run

    for _ in range(requests):
        queue.put_nowait(url)  # Requests per URL

    tasks = []
    for i in range(concurrency):
        task = asyncio.create_task(
            worker(f"worker-{i+1}", queue, results)
        )  # Create a worker for however much concurrency we want have, give it queue and results to start adding information to.
        tasks.append(task)

    started_at = time.monotonic()  # Figure out when we are starting
    await queue.join()  # Execute everything inside of the queue
    total_time = (
        time.monotonic() - started_at
    )  # Figure out when we finished everything inside of the queue

    for task in tasks:
        task.cancel()  # Cancel our long running workers

    print("---")
    print(
        f"{concurrency} workers took {total_time:.2f} seconds to complete {len(results)} requests"
    )


def assault(url, requests, concurrency):
    """ Entrypoint to making requests """
    results = []
    asyncio.run(
        distribute_work(url, requests, concurrency, results)
    )  # This line will return a co-routine that asyncio.run will execute
    print(results)
