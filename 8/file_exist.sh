#!/bin/bash

echo "Please enter a filename:"
read filename

if test -f "$filename";
then
  echo "File exists"
else
  touch "$filename"
  echo "File created"
fi