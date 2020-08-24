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
[5] [asyncio](https://docs.python.org/3/library/asyncio.html) is a library to write concurrent code using the async/await syntax.

## For later
* Entry points = entry_points={"console_scripts": ["assault=assault.cli:cli"],},
* pip install -e .