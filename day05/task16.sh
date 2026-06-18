#!/bin/bash

check()
{
  return 0
}

check

echo $?


sum(){
  echo $(($1+$2))
}

result=$(sum 10 20)

echo "$result"
