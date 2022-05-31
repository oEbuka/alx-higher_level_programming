#!/usr/bin/python3
# Author - Obiora Ebuka

def remove_char_at(str, n):
    if n < 0:
        return (str)
    return (str[:n] + str[n+1:])
