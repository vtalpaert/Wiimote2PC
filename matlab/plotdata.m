clear all
close all

rdata1;
rdata2;
rdata3;
rdata4;


figure(1)
plot3(data2(:,1),data2(:,2),data2(:,3))
xlabel('x')
ylabel('y')
zlabel('z')
grid on
axis equal
hold on
plot3(data3(:,1),data3(:,2),data3(:,3), 'g')
plot3(data4(:,1),data4(:,2),data4(:,3), 'r')

%% pointing up and forward x rotation
rdata5;
figure(2)
plot(data5(:,1))
hold on
plot(data5(:,2),'g')
plot(data5(:,3),'r')
grid on
legend('x','y', 'z')
xlabel('data')
ylabel('value')
title('x rotation')

%% y rotation
rdata6;
figure(3)
plot(data6(:,1))
hold on
plot(data6(:,2),'g')
plot(data6(:,3),'r')
grid on
legend('x','y', 'z')
xlabel('data')
ylabel('value')
title('y rotation')