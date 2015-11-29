#!/bin/bash
IFS=:
total=0
declare -a array=();
while read name pass gid x x x shell 
do
    array[$counter]=${gid#0};
    let counter=counter+1;
#   echo $counter;
done < $1
#echo ${array[@]}

for i in ${array[@]}; do
let      total=total+i;
      done
      echo "Total: $total"
