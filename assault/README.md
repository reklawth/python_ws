# assault

A simple CLI load testing tool.

## Installation

Install using `pip`:
```
$pip install assault
```

## Usage

The simplest usage of `assault` requires only a URL to test against and 500 requests synchronously (one at a time)
* This is what it wuld look like:
```
$ assault https://example.com
.... Done!
--- Results ---
Successful requests    500
Slowest                0.010s
Fastest                0.001s
Average                0.003s
Total time             0.620s
Requests Per Minute    48360
Requests Per Second    806
```

If we want to add concurrency, we will use the `-c` option and we can use the `-r` option to specify how many rquests that we would like to make:
```
$ assault https://example.com
.... Done!
--- Results ---
Successful requests    3000
Slowest                0.010s
Fastest                0.001s
Average                0.003s
Total time             2.400s
Requests Per Minute    90000
Requests Per Second    1250
```

If you wuold like to see these results in JSON format then you can use the `-j` option with a path to a JSON file:
```
$ assault -r 3000 -c 10 -j output.hson https://example.com
.... Done!
```

## Development

For working on assault you will need to have Python >= 3.7 (because we will be using `asyncio`) and [`pipenv`][1] installed.  Whith those installed, run the follwoing command to crate a virtualenv for the project and fect the dependencies:
```
$pipenv install --dev
...
```

From there, activate the virtualenv and get to work:
```
$ pipenv shell
...
(assault) $
```

[1] https://docs.pipenv.org/en/latest/
[2] setup.py came from: https://raw.githubusercontent.com/navdeep-G/setup.py/master/setup.py
[3] [argparse](https://docs.python.org/3/library/argparse.html) -- The `argparse` module makes it easy to write user-friendly command-line interfaces.  The program defines what arguments it requires, and `argparse` will figure out how to parse those out of `sys.argv`.  The `argparse` module also automatically generates help and usage messages and issues errors when users give the program invalid arguments.
[4] [Click](https://click.palletsprojects.com/en/7.x/) is a Python package for creating beautiful command line interfaces in a composable way with as little code as necessary.
[5] [asyncio](https://docs.python.org/3/library/asyncio.html) is a library to write [asynchronous](https://realpython.com/async-io-python/) or concurrent code using the `async` and `await` syntax.
[6] The [doctest](https://docs.python.org/3/library/doctest.html) module searches for pieces of text that look like interactive Python sessions, and then executes those sessions to verify that they work exactly as shown. 
[7] The [typing](https://docs.python.org/3/library/typing.html) module provides runtime support for [type hints](https://realpython.com/python-type-checking/) as specified by PEP 484, PEP 526, PEP 544, PEP 586, PEP 589, and PEP 591.  

## For later
* Entry points = entry_points={"console_scripts": ["assault=assault.cli:cli"],},
* pip install -e .
* Event loop
* [GIL](https://realpython.com/python-gil/) - Global interpreter lock
* requests package is not meant to work with asyncio, so it will need to be placed in its own function
* `async` and `await` are used in tandem, to use await it must be in an `async` function
* To run 20 workers making 1000 requests to google.com from CLI:
  ```
  DEBUG=true assault -r 100 -c 20 https://google.com
  ```
* Research Test-Driven Development
* To run doctests on the stats module:
  ```
  python -m doctest assault/stats.py 
  ```