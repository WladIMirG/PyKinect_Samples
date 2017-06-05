clear all;
close all;
clc;

% load('puntos_cursor.mat');
load('Nuevos_cursor.mat');
NewPos;
tramos = 5;
[nf nc] = size(NewPos);
if nc > 0
    for i = 1:1:nc
        i;
        nX(i)= -NewPos(i).x;
        nY(i)= NewPos(i).z;
        nZ(i)= NewPos(i).y;
    end
    lim = 1.25
    limi = find(nY<lim&nY>0.3&nZ>0);
    limi1 = find(nY<lim&nY>0.3&nZ<0);
    limi2 = find(nZ>0);
%     limi = find(nZ<lim&nZ>0.3&nY>0);
%     limi1 = find(nZ<lim&nZ>0.3&nY<0);
%     limi2 = find(nY>0);
%     limi2 = find(nZ>1.3);
%     % Plot Examples
%     plot(X(pos, 1), X(pos, 2), 'k+','LineWidth', 2, ...
%     'MarkerSize', 7);
%     plot(X(neg, 1), X(neg, 2), 'ko', 'MarkerFaceColor', 'y', ...
%     'MarkerSize', 7);
    nnz = nZ(limi);
    nnz(:)=-1;
    plot3 (nX(limi),nY(limi),nZ(limi),'r.')
    hold on;
    plot3 (nX(limi1),nY(limi1),nZ(limi1),'g.');
    % plot (X,Y, 'b')
    % hold on

    % axis([-160 160 -120 120]);
    % view ([1,1,1])
    view ([-1,-1,1])
    xlabel('X')
    ylabel('Y')
    % zlabel('Tim')
else
    error = 'Esto no esta funcionando'
end