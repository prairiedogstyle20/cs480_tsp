@echo off
:: Basic build file for TSP program
echo Build Started
g++ -o Node.o -c Node.cpp
g++ -o Graph.o -c Graph.cpp
g++ -o Main.o -c Main.cpp
g++ -o Main.exe Main.o Graph.o Node.o
echo Build Complete
