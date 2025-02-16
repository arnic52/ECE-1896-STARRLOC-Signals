% Adam Nichols
% Profs. Li, Yun, Jacobs
% ECE 1896
% 22 January 2025

% convert Keplerian elements into azimuth and elevation angles

% ISS Keplerian elements from https://www.amsat.org/tle/daily-bulletin.txt
% measurements last updated: 1/22/2025 at 9:09pm

% ISS
% 1 25544U 98067A   25022.80907568  .00027349  00000-0  47853-3 0  9999
% 2 25544  51.6395 307.1435 0002239 116.3272 339.5792 15.50411369492617

% initialize keps in character arrays
satellite = 'ISS';
line1 = '1 25544U 98067A   25022.80907568  .00027349  00000-0  47853-3 0  9999';
line2 = '2 25544  51.6395 307.1435 0002239 116.3272 339.5792 15.50411369492617';

% initialize my coordinates 
ground_station_coords = '402636N795730W';  % SSOE Benedum Building
ground_station_latitude = ground_station_coords(1:7);
ground_station_longitude = ground_station_coords(8:14);

% Line 1 format: (as of https://www.amsat.org/keplerian-elements-formats/)
% Column     Description
%  01-01     Line Number of Element Data
%  03-07     Satellite Number
%  08        Classification.   Almost always "U" for unclassified
%  10-11     International Designator (Last two digits of launch year)
%  12-14     International Designator (Launch number of the year)
%  15-17     International Designator (Piece of launch)
%  19-20     Epoch Year (Last two digits of year)
%  21-32     Epoch (Day number and fractional portion of the day)
%  34-43     1st Derivative of the Mean Motion with respect to Time *
%  45-52     2nd Derivative of the Mean Motion with respect to Time (decimal point assumed) *
%  54-61     BSTAR drag term 
%  63-63     Ephemeris type
%  65-68     Element set number (modern TLEs from USSF always use 999)
%  69-69     Checksum (Modulo 10)

% extract data into separate variables
epoch_year = line1(19:20);
epoch_day = line1(21:32);
mean_motion_first_derivative = line1(34:43);
mean_motion_second_derivative = line1(45:52);
drag = line1(54:61);

% checksum format (as of https://www.amsat.org/keplerian-elements-formats/)
% Start with zero.
% For each digit in the line, add the value of the digit.
% Blanks, periods, letters, ‘+’ signs add zero
% For’-‘ signs add 1
% Take the last decimal digit of the result (that is, take the result modulo 10) as the check digit.

% Line 2 format: (as of https://www.amsat.org/keplerian-elements-formats/)
% Column     Description
%  01-01     Line Number of Element Data
%  03-07     Satellite Catalog Number
%  09-16     Inclination [Degrees]
%  18-25     Right Ascension of the Ascending Node [Degrees]
%  27-33     Eccentricity (decimal point assumed)
%  35-42     Argument of Perigee [Degrees]
%  44-51     Mean Anomaly [Degrees]
%  53-63     Mean Motion [Revs per day]
%  64-68     Revolution number at epoch [Revs] 
%  69-69     Checksum (Modulo 10)

% extract data into separate variables
inclination = line2(9:16);
ascending_node = line2(18:25);
eccentricity = line2(27:33);
perigee = line2(35:42);
mean_anomaly = line2(44:51);
mean_motion_revs_day = line2(53:63);
revolution_num_at_epoch = line2(64:68);