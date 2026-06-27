#!/bin/bash

backup(){

tar -czf backup.tar.gz "$1"

echo "Backup completed"

}

backup "$1"
