- [MouseMover Utility](#mousemover-utility)
  - [Prerequisites](#prerequisites)
  - [Setup Virtual Environment](#setup-virtual-environment)
  - [Execute the utility](#execute-the-utility)

# MouseMover Utility

It's a simple utility to make your mouse move without any physical intervention.

## Prerequisites

Make sure you have [python => 3.7](https://www.python.org/downloads/) [pip](https://pip.pypa.io/en/stable/installation/) installed.

## Setup Virtual Environment

1. Activate the virtual env ( optional )

```bash
pip install virtualenv
python -m venv mousemover
source mousemover/bin/activate
```

2. Clone the source repository

```bash
git clone https://github.com/superarvind/mousemover.git
```

3. Install dependency modules
```bash
pip install -r requirements.txt
```

## Execute the utility

1. Execute the command on the terminal and leave it open.
```bash
python move.py
```