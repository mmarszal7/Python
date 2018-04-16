function [Wagi, Odleglosci, Tab]=Wczytaj()

clear Wagi
clear Tab
clear Odleglosci

Wagi = dlmread('Osiedle/Wagi.txt','')';
Tab = dlmread('Osiedle/Tab.txt','');
Odleglosci = dlmread('Osiedle/Odleglosci.txt','');

