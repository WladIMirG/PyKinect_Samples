clear all;
close all;
clc;

% load('puntos_cursor.mat');
load('Nuevos_cursor.mat');
NewPos;
[f c] = size(NewPos)
tramos = 5;
[nf nc] = size(NewPos);

for i = 1:1:nc
    i
    nX(i)= NewPos(i).x;
    nY(i)= NewPos(i).y;
    nZ(i)= NewPos(i).z;
end
plot3 (nX,nY,nZ,'r.')
hold on
% plot (X,Y, 'b')
% hold on

% axis([-160 160 -120 120]);
% view ([1,1,1])
view ([0,0,-1])
xlabel('X')
ylabel('Y')
% zlabel('Tim')