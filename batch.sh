#!/bin/bash

filename=$1
for line in `cat $filename`
do
    arr=(${line//,/ })
    user=${arr[0]}
    passwd=${arr[1]}
    python newsmth.py $user $passwd > .local_$user &
    echo $line
done


