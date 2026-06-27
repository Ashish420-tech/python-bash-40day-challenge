#!/bin/bash

add(){

result=$(($1+$2))
echo "$result"

}

sum=$(add 10 20)

echo $sum
