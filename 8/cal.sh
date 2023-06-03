#!/bin/bash
read -p "Enter first number: " number1
read -p "Enter operation(+,-,*,/): " operand
read -p "Enter second number: " number2


if [[ $operand == "+" ]];
then
  sum=$(($number1 + $number2))
  echo $sum
elif [[ $operand == "-" ]];
then
  sub=$(($number1 - $number2))
  echo $sub
elif [[ $operand == "*" ]];
then
  multi=$(($number1 * $number2))
  echo $multi
elif [[ $operand == "/" ]];
then
  div=$(($number1 / $number2))
  echo $div
fi