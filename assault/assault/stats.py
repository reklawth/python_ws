from typing import List, Dict
from statistics import mean


class Results:
    """
    Results handles calculating statistics based on a list of requests that are made.
    Here is an example of what the information will look like:

    Successful requests    500
    Slowest                0.010s
    Fastest                0.001s
    Average                0.003s
    Total time             0.620s
    Requests Per Minute    48360
    Requests Per Second    806
    """

    def __init__(self, total_time: float, requests: List[Dict]):
        self.total_time = total_time
        self.requests = sorted(
            requests, key=lambda r: r["request_time"]
        )  # lambda will find request_time as the key to sort requests, and return sorted requests

    def slowest(self) -> float:
        """ 
        Returns the completion time of the slowest request

        >>> results = Results(10.6, [{
        ...     'status_code': 200,
        ...     'request_time': 3.4,
        ... }, {
        ...     'status_code': 500,
        ...     'request_time': 6.1,
        ... }, {
        ...     'status_code': 200,
        ...     'request_time': 1.04,
        ... }])
        >>> results.slowest()
        6.1
        """
        return self.requests[-1]["request_time"]

    def fastest(self) -> float:
        """ 
        Returns the completion time of the fastest request

        >>> results = Results(10.6, [{
        ...     'status_code': 200,
        ...     'request_time': 3.4,
        ... }, {
        ...     'status_code': 500,
        ...     'request_time': 6.1,
        ... }, {
        ...     'status_code': 200,
        ...     'request_time': 1.04,
        ... }])
        >>> results.fastest()
        1.04
        """
        return self.requests[0]["request_time"]

    def average_time(self) -> float:
        """ 
        Returns the completion time of the average request

        >>> results = Results(10.6, [{
        ...     'status_code': 200,
        ...     'request_time': 3.4,
        ... }, {
        ...     'status_code': 500,
        ...     'request_time': 6.1,
        ... }, {
        ...     'status_code': 200,
        ...     'request_time': 1.04,
        ... }])
        >>> results.average_time()
        3.513333333333333
        """
        return mean(
            [r["request_time"] for r in self.requests]
        )  # data needs to be an iterable, so we use a list comprehension to give a list that only contains request time

    def successful_requests(self) -> int:
        """ 
        Returns the number of successful requests

        >>> results = Results(10.6, [{
        ...     'request_time': 3.4,
        ...     'status_code': 200,
        ... }, {
        ...     'status_code': 500,
        ...     'request_time': 6.1,
        ... }, {
        ...     'status_code': 200,
        ...     'request_time': 1.04,
        ... }])
        >>> results.successful_requests()
        2
        """
        return len([r for r in self.requests if r["status_code"] in range(200, 299)])
        pass
