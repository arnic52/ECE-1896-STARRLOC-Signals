% Adam Nichols
% ECE 1896
% Team Starr Loc
% 20 March 2025

% create plots to represent calibration data

% reset the workspace
clear, clc

% import data from the text file
filename = "arduino_output.txt";
data = importdata(filename);



% Define a format pattern to extract Step, X, Y, Z
pattern = 'Az: %d\tEl: %d\tX: %d\tY: %d\tZ: %d';

% create vectors from the imported data
step = zeros(length(data),1);
az = zeros(length(data),1);
el = zeros(length(data),1);
x = zeros(length(data),1);
y = zeros(length(data),1);
z = zeros(length(data),1);

for i = 1:length(data)
    % Example input string
    line = data{i};
    
    % Extract values
    curr = sscanf(line, pattern, [1, 5]);
    az(i) = curr(1);
    el(i) = curr(2);
    x(i) = curr(3);
    y(i) = curr(4);
    z(i) = curr(5);
end

% reshape for plots
az = reshape(az,40,[]);
el = reshape(el,40,[]);
x = reshape(x,40,[]);
y = reshape(y,40,[]);
z = reshape(z,40,[]);

% convert az/el into spherical coordinates
az_pol = az / 4500 * 2*pi;
el_pol = el / 4500 * 2*pi;



% % get the magnitude of the spherical radius vectorr
% mag_all = sqrt(x.^2+y.^2+z.^2);
% offset = sum(mag_all)/length(mag_all);
% scale = max(abs(mag_all));

% determine the offsets for the measurements
x_offset = (max(max(x))+min(min(x)))/2;
y_offset = (max(max(y))+min(min(y)))/2;
z_offset = (max(max(z))+min(min(z)))/2;

% scale x and y by their offset to center at zero
x = x - x_offset;
y = y - y_offset;
z = z - z_offset;

% scale x and y to be within 1
x_scale = max(max(abs(x)));
x = x / x_scale;
y_scale = max(max(abs(y)));
y = y / y_scale;
z_scale = max(max(abs(z)));
z = z / z_scale;

% % use the arctangent to get the bearing
% az_exp = atan2(x,-y);
% %az_exp = unwrap(az_exp,[],2);
% az_deg = az_exp*180/pi - 9.25;


% use the arctangent to get the elevation
el_exp = atan2(y,z);
el_exp = unwrap(el_exp,[],1);
el_deg = el_exp*180/pi;

% create plots of x, y, z vs. step
figure(1)
clf
mesh(az,el,x)
title("Plot of X vs. Step")
xlabel("Az step number")
ylabel("El step number")
zlabel("Sensor reading")

% create plots of x, y, z vs. step
figure(2)
clf
mesh(az,el,y)
title("Plot of Y vs. Step")
xlabel("Az step number")
ylabel("El step number")
zlabel("Sensor reading")

% create plots of x, y, z vs. step
figure(3)
clf
mesh(az,el,z)
title("Plot of Z vs. Step")
xlabel("Az step number")
ylabel("El step number")
zlabel("Sensor reading")

% create plots of x, y, z vs. step
figure(4)
clf
mesh(az,el,el_deg)
title("Plot of Y+Z vs. Step")
xlabel("Az step number")
ylabel("El step number")
zlabel("Sensor reading")
