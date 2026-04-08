#!/bin/zsh
base="https://dimacs.rutgers.edu/~graham/ssbd/ssbd"
for i in {1..10}; do
    curl -f -O "${base}${i}.pdf"
done