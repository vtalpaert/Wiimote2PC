clear all
close all

data1;


figure(1)
plot3(data(:,1),data(:,2),data(:,3))
xlabel('x')
ylabel('y')
zlabel('z')
grid on
axis equal
hold on