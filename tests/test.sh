#!/usr/bin/env bash
if [[ $1 ]]
then
	FILE=$1
else
	FILE='.'
fi

hitch test -s local.yml $FILE
