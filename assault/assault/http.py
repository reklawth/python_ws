import asyncio
import time


def fetch(url):
    """ Make the request and return the results """
    pass


def worker(name, queue, results):
    """ A function to take unmade requests from a queue and perform the work then add results to the results list.  """
    pass


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
