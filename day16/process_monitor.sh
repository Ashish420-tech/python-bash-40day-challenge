#!/bin/bash



while true
do
    clear

    echo "===== CPU ====="
    top -b -n1 | head -10

    echo

    echo "===== Memory ====="
    free -h

    sleep 5
done
