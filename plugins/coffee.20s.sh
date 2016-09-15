#!/bin/bash
if [ -f /usr/local/bin/python ]
then
    /usr/local/bin/python "$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )/../coffee.py"
elif [ -f /usr/bin/python ]
then
    /usr/bin/python "$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )/../coffee.py"
else
    echo "no python found"
fi

