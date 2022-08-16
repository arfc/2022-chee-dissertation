// Gmsh project created on Fri Oct 22 12:34:02 2021
//+
Point(1) = {0, 0, 0, 1.0};
//+
Point(2) = {2, 0, 0, 1.0};
//+
Point(3) = {0, 3.25, 0, 1.0};
//+
Point(4) = {2, 3.25, 0, 1.0};
//+
Point(5) = {25.1, 3.25, 0, 1.0};
//+
Point(6) = {27.1, 3.25, 0, 1.0};
//+
Point(7) = {27.1, 0, 0, 1.0};
//+
Point(8) = {25.1, 0, 0, 1.0};
//+
Point(9) = {2, 0.35, 0, 1.0};
//+
Point(10) = {2, 2.9, 0, 1.0};
//+
Point(11) = {25.1, 2.9, 0, 1.0};
//+
Point(12) = {25.1, 0.35, 0, 1.0};
//+
Line(1) = {3, 1};
//+
Line(2) = {2, 1};
//+
Line(3) = {2, 9};
//+
Line(4) = {9, 10};
//+
Line(5) = {10, 4};
//+
Line(6) = {3, 4};
//+
Line(7) = {4, 5};
//+
Line(8) = {5, 11};
//+
Line(9) = {11, 12};
//+
Line(10) = {12, 8};
//+
Line(11) = {8, 2};
//+
Line(12) = {8, 7};
//+
Line(13) = {7, 6};
//+
Line(14) = {6, 5};
//+
Point(13) = {4.31, 0.35, 0, 1.0};
//+
Point(14) = {6.62, 0.35, 0, 1.0};
//+
Point(15) = {8.93, 0.35, 0, 1.0};
//+
Point(16) = {11.24, 0.35, 0, 1.0};
//+
Point(17) = {13.55, 0.35, 0, 1.0};
//+
Point(18) = {15.86, 0.35, 0, 1.0};
//+
Point(19) = {18.17, 0.35, 0, 1.0};
//+
Point(20) = {20.48, 0.35, 0, 1.0};
//+
Point(21) = {22.79, 0.35, 0, 1.0};
//+
Point(22) = {22.79, 2.9, 0, 1.0};
//+
Point(23) = {20.48, 2.9, 0, 1.0};
//+
Point(24) = {18.17, 2.9, 0, 1.0};
//+
Point(25) = {15.86, 2.9, 0, 1.0};
//+
Point(26) = {13.55, 2.9, 0, 1.0};
//+
Point(27) = {11.24, 2.9, 0, 1.0};
//+
Point(28) = {8.93, 2.9, 0, 1.0};
//+
Point(29) = {6.62, 2.9, 0, 1.0};
//+
Point(30) = {4.31, 2.9, 0, 1.0};
//+
Line(15) = {10, 30};
//+
Line(16) = {30, 13};
//+
Line(17) = {13, 9};
//+
Line(18) = {13, 14};
//+
Line(19) = {14, 29};
//+
Line(20) = {29, 30};
//+
Line(21) = {29, 28};
//+
Line(22) = {28, 15};
//+
Line(23) = {15, 14};
//+
Line(24) = {14, 15};
//+
Line(25) = {16, 27};
//+
Line(26) = {27, 28};
//+
Line(27) = {15, 16};
//+
Line(28) = {16, 17};
//+
Line(29) = {17, 26};
//+
Line(30) = {26, 27};
//+
Line(31) = {26, 25};
//+
Line(32) = {25, 18};
//+
Line(33) = {18, 17};
//+
Line(34) = {18, 19};
//+
Line(35) = {19, 24};
//+
Line(36) = {24, 25};
//+
Line(37) = {19, 20};
//+
Line(38) = {20, 23};
//+
Line(39) = {24, 23};
//+
Line(40) = {23, 22};
//+
Line(41) = {22, 21};
//+
Line(42) = {21, 20};
//+
Line(43) = {20, 21};
//+
Line(44) = {21, 12};
//+
Line(45) = {22, 11};
//+
Curve Loop(1) = {1, -2, 3, 4, 5, -6};
//+
Plane Surface(1) = {1};
//+
Curve Loop(2) = {15, 16, 17, 4};
//+
Plane Surface(2) = {2};
//+
Curve Loop(3) = {20, 16, 18, 19};
//+
Plane Surface(3) = {3};
//+
Curve Loop(4) = {19, 21, 22, 23};
//+
Plane Surface(4) = {4};
//+
Curve Loop(5) = {15, -20, 21, -26, -30, 31, -36, 39, 40, 45, -8, -7, -5};
//+
Plane Surface(5) = {5};
//+
Curve Loop(6) = {14, 8, 9, 10, 12, 13};
//+
Plane Surface(6) = {6};
//+
Curve Loop(7) = {41, 44, -9, -45};
//+
Plane Surface(7) = {7};
//+
Curve Loop(8) = {38, 40, 41, 42};
//+
Plane Surface(8) = {8};
//+
Curve Loop(9) = {35, 39, -38, -37};
//+
Plane Surface(9) = {9};
//+
Curve Loop(10) = {22, 27, 25, 26};
//+
Plane Surface(10) = {10};
//+
Curve Loop(11) = {25, -30, -29, -28};
//+
Plane Surface(11) = {11};
//+
Curve Loop(12) = {29, 31, 32, 33};
//+
Plane Surface(12) = {12};
//+
Curve Loop(13) = {32, 34, 35, 36};
//+
Plane Surface(13) = {13};
//+
Curve Loop(14) = {44, 10, 11, 3, -17, 18, -23, 27, 28, -33, 34, 37, -42};
//+
Plane Surface(14) = {14};
//+
Physical Surface("graphite1") = {1};
//+
Physical Surface("graphite2") = {6};
//+
Physical Surface("flibetop") = {5};
//+
Physical Surface("flibe") = {5, 14};
//+
Physical Surface("flibetop") -= {5};
//+
Physical Surface("fuel1") = {2};
//+
Physical Surface("fuel2", 46) = {3};
//+
Physical Surface("fuel2", 46) += {3};
//+
Physical Surface("fuel3") = {4};
//+
Physical Surface("fuel4") = {10};
//+
Physical Surface("fuel5") = {11};
//+
Physical Surface("fuel6") = {12};
//+
Physical Surface("fuel7") = {13};
//+
Physical Surface("fuel8") = {9};
//+
Physical Surface("fuel9") = {8};
//+
Physical Surface("fuel10") = {7};
