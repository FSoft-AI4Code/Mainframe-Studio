# Generated from grammar/panel/Panel.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,121,771,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,
        7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,
        13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,
        20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,
        26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,
        33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,
        39,2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,
        46,7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,52,7,
        52,2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,2,57,7,57,2,58,7,58,2,
        59,7,59,2,60,7,60,2,61,7,61,2,62,7,62,2,63,7,63,2,64,7,64,2,65,7,
        65,2,66,7,66,2,67,7,67,2,68,7,68,2,69,7,69,2,70,7,70,2,71,7,71,2,
        72,7,72,2,73,7,73,2,74,7,74,2,75,7,75,2,76,7,76,2,77,7,77,2,78,7,
        78,2,79,7,79,2,80,7,80,2,81,7,81,2,82,7,82,2,83,7,83,2,84,7,84,2,
        85,7,85,2,86,7,86,2,87,7,87,2,88,7,88,2,89,7,89,2,90,7,90,2,91,7,
        91,2,92,7,92,2,93,7,93,2,94,7,94,2,95,7,95,2,96,7,96,2,97,7,97,2,
        98,7,98,2,99,7,99,2,100,7,100,2,101,7,101,2,102,7,102,1,0,4,0,208,
        8,0,11,0,12,0,209,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,221,8,
        1,1,2,1,2,1,2,5,2,226,8,2,10,2,12,2,229,9,2,1,3,1,3,1,3,5,3,234,
        8,3,10,3,12,3,237,9,3,1,3,4,3,240,8,3,11,3,12,3,241,1,4,1,4,1,5,
        1,5,1,5,4,5,249,8,5,11,5,12,5,250,1,6,1,6,1,6,3,6,256,8,6,1,6,3,
        6,259,8,6,1,6,4,6,262,8,6,11,6,12,6,263,1,7,1,7,4,7,268,8,7,11,7,
        12,7,269,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,
        3,8,286,8,8,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,4,10,296,8,10,11,
        10,12,10,297,3,10,300,8,10,1,11,1,11,1,11,1,11,1,11,1,12,1,12,1,
        13,1,13,1,13,1,13,1,13,1,14,1,14,1,15,1,15,1,15,1,15,1,15,1,16,1,
        16,1,17,1,17,1,17,1,17,1,17,1,18,1,18,1,19,1,19,1,19,1,19,1,19,1,
        20,1,20,1,21,1,21,1,21,1,21,1,21,1,22,1,22,1,23,1,23,1,23,1,23,1,
        23,1,24,1,24,1,25,1,25,1,25,1,25,1,25,1,26,1,26,1,27,1,27,1,27,1,
        27,1,27,1,28,1,28,1,28,1,28,1,28,1,29,1,29,1,30,1,30,1,30,1,30,1,
        30,1,31,1,31,1,31,1,31,1,31,1,32,1,32,1,33,1,33,1,33,5,33,385,8,
        33,10,33,12,33,388,9,33,1,34,1,34,1,34,1,34,1,34,3,34,395,8,34,1,
        35,1,35,1,36,1,36,1,36,1,36,3,36,403,8,36,1,36,1,36,1,36,1,37,1,
        37,1,38,1,38,1,39,1,39,1,39,1,39,1,39,1,40,1,40,1,40,1,40,1,40,1,
        40,3,40,423,8,40,1,41,1,41,1,41,1,41,1,41,1,42,1,42,1,42,1,42,3,
        42,434,8,42,1,43,1,43,5,43,438,8,43,10,43,12,43,441,9,43,1,44,1,
        44,1,44,3,44,446,8,44,1,45,3,45,449,8,45,1,45,1,45,1,46,1,46,1,46,
        1,46,1,46,3,46,458,8,46,1,47,1,47,1,48,1,48,1,48,3,48,465,8,48,1,
        48,1,48,1,48,5,48,470,8,48,10,48,12,48,473,9,48,1,49,1,49,1,50,1,
        50,1,51,1,51,4,51,481,8,51,11,51,12,51,482,3,51,485,8,51,1,52,1,
        52,1,52,1,52,1,52,1,52,1,52,5,52,494,8,52,10,52,12,52,497,9,52,1,
        52,1,52,3,52,501,8,52,1,52,1,52,1,53,1,53,1,53,1,53,1,54,1,54,1,
        54,1,54,1,54,3,54,514,8,54,1,55,1,55,1,56,1,56,1,56,1,56,1,56,1,
        56,1,57,1,57,1,57,1,57,1,57,5,57,529,8,57,10,57,12,57,532,9,57,1,
        57,1,57,1,57,1,57,1,57,1,57,1,57,1,57,1,57,3,57,543,8,57,1,58,1,
        58,1,58,1,58,1,58,1,58,1,58,1,58,1,58,1,58,1,58,3,58,556,8,58,1,
        59,1,59,1,60,1,60,1,60,1,60,1,60,1,60,1,61,1,61,1,62,1,62,1,63,1,
        63,1,63,5,63,573,8,63,10,63,12,63,576,9,63,1,64,1,64,1,65,1,65,1,
        66,1,66,1,67,1,67,1,68,1,68,3,68,588,8,68,1,69,1,69,1,69,1,70,1,
        70,1,71,1,71,1,71,1,72,1,72,1,72,5,72,601,8,72,10,72,12,72,604,9,
        72,1,73,1,73,1,73,5,73,609,8,73,10,73,12,73,612,9,73,1,74,1,74,1,
        74,4,74,617,8,74,11,74,12,74,618,1,74,1,74,1,74,1,74,1,74,1,74,5,
        74,627,8,74,10,74,12,74,630,9,74,1,74,1,74,3,74,634,8,74,1,75,1,
        75,1,76,1,76,1,77,1,77,1,78,1,78,1,78,5,78,645,8,78,10,78,12,78,
        648,9,78,1,79,1,79,1,79,5,79,653,8,79,10,79,12,79,656,9,79,1,80,
        1,80,1,80,4,80,661,8,80,11,80,12,80,662,1,80,1,80,1,81,1,81,1,82,
        1,82,1,82,1,82,1,82,1,83,1,83,1,84,1,84,1,84,1,85,1,85,1,85,1,85,
        3,85,683,8,85,1,86,1,86,1,86,1,86,1,86,5,86,690,8,86,10,86,12,86,
        693,9,86,1,86,1,86,1,87,1,87,1,88,1,88,1,88,1,88,1,88,5,88,704,8,
        88,10,88,12,88,707,9,88,1,88,1,88,1,89,1,89,1,90,1,90,3,90,715,8,
        90,1,91,1,91,3,91,719,8,91,1,92,1,92,1,92,1,92,1,92,1,92,3,92,727,
        8,92,1,92,1,92,1,93,1,93,1,94,1,94,1,95,1,95,1,96,1,96,1,96,1,96,
        1,96,5,96,742,8,96,10,96,12,96,745,9,96,1,96,1,96,1,96,1,96,1,97,
        1,97,1,98,1,98,1,98,1,99,1,99,1,100,1,100,1,101,1,101,1,101,1,101,
        1,101,1,101,1,101,3,101,767,8,101,1,102,1,102,1,102,0,0,103,0,2,
        4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,
        50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,92,
        94,96,98,100,102,104,106,108,110,112,114,116,118,120,122,124,126,
        128,130,132,134,136,138,140,142,144,146,148,150,152,154,156,158,
        160,162,164,166,168,170,172,174,176,178,180,182,184,186,188,190,
        192,194,196,198,200,202,204,0,13,3,0,89,90,116,116,120,120,1,0,102,
        104,2,0,96,96,98,99,1,0,54,55,2,0,54,55,93,94,2,0,28,28,34,35,3,
        0,3,8,11,22,121,121,1,0,48,49,4,0,29,31,57,74,80,82,86,87,1,0,119,
        120,1,0,29,31,2,0,44,44,119,119,4,0,37,37,45,45,80,80,90,90,757,
        0,207,1,0,0,0,2,220,1,0,0,0,4,222,1,0,0,0,6,230,1,0,0,0,8,243,1,
        0,0,0,10,248,1,0,0,0,12,252,1,0,0,0,14,265,1,0,0,0,16,285,1,0,0,
        0,18,287,1,0,0,0,20,299,1,0,0,0,22,301,1,0,0,0,24,306,1,0,0,0,26,
        308,1,0,0,0,28,313,1,0,0,0,30,315,1,0,0,0,32,320,1,0,0,0,34,322,
        1,0,0,0,36,327,1,0,0,0,38,329,1,0,0,0,40,334,1,0,0,0,42,336,1,0,
        0,0,44,341,1,0,0,0,46,343,1,0,0,0,48,348,1,0,0,0,50,350,1,0,0,0,
        52,355,1,0,0,0,54,357,1,0,0,0,56,362,1,0,0,0,58,367,1,0,0,0,60,369,
        1,0,0,0,62,374,1,0,0,0,64,379,1,0,0,0,66,381,1,0,0,0,68,394,1,0,
        0,0,70,396,1,0,0,0,72,398,1,0,0,0,74,407,1,0,0,0,76,409,1,0,0,0,
        78,411,1,0,0,0,80,422,1,0,0,0,82,424,1,0,0,0,84,429,1,0,0,0,86,435,
        1,0,0,0,88,442,1,0,0,0,90,448,1,0,0,0,92,457,1,0,0,0,94,459,1,0,
        0,0,96,464,1,0,0,0,98,474,1,0,0,0,100,476,1,0,0,0,102,484,1,0,0,
        0,104,486,1,0,0,0,106,504,1,0,0,0,108,513,1,0,0,0,110,515,1,0,0,
        0,112,517,1,0,0,0,114,542,1,0,0,0,116,555,1,0,0,0,118,557,1,0,0,
        0,120,559,1,0,0,0,122,565,1,0,0,0,124,567,1,0,0,0,126,569,1,0,0,
        0,128,577,1,0,0,0,130,579,1,0,0,0,132,581,1,0,0,0,134,583,1,0,0,
        0,136,585,1,0,0,0,138,589,1,0,0,0,140,592,1,0,0,0,142,594,1,0,0,
        0,144,597,1,0,0,0,146,605,1,0,0,0,148,633,1,0,0,0,150,635,1,0,0,
        0,152,637,1,0,0,0,154,639,1,0,0,0,156,641,1,0,0,0,158,649,1,0,0,
        0,160,657,1,0,0,0,162,666,1,0,0,0,164,668,1,0,0,0,166,673,1,0,0,
        0,168,675,1,0,0,0,170,682,1,0,0,0,172,684,1,0,0,0,174,696,1,0,0,
        0,176,698,1,0,0,0,178,710,1,0,0,0,180,714,1,0,0,0,182,718,1,0,0,
        0,184,720,1,0,0,0,186,730,1,0,0,0,188,732,1,0,0,0,190,734,1,0,0,
        0,192,736,1,0,0,0,194,750,1,0,0,0,196,752,1,0,0,0,198,755,1,0,0,
        0,200,757,1,0,0,0,202,766,1,0,0,0,204,768,1,0,0,0,206,208,3,2,1,
        0,207,206,1,0,0,0,208,209,1,0,0,0,209,207,1,0,0,0,209,210,1,0,0,
        0,210,211,1,0,0,0,211,212,5,0,0,1,212,1,1,0,0,0,213,221,3,12,6,0,
        214,221,3,66,33,0,215,221,3,156,78,0,216,221,3,158,79,0,217,221,
        3,168,84,0,218,221,3,6,3,0,219,221,3,4,2,0,220,213,1,0,0,0,220,214,
        1,0,0,0,220,215,1,0,0,0,220,216,1,0,0,0,220,217,1,0,0,0,220,218,
        1,0,0,0,220,219,1,0,0,0,221,3,1,0,0,0,222,223,5,2,0,0,223,227,5,
        107,0,0,224,226,3,80,40,0,225,224,1,0,0,0,226,229,1,0,0,0,227,225,
        1,0,0,0,227,228,1,0,0,0,228,5,1,0,0,0,229,227,1,0,0,0,230,231,5,
        2,0,0,231,235,5,106,0,0,232,234,3,8,4,0,233,232,1,0,0,0,234,237,
        1,0,0,0,235,233,1,0,0,0,235,236,1,0,0,0,236,239,1,0,0,0,237,235,
        1,0,0,0,238,240,3,10,5,0,239,238,1,0,0,0,240,241,1,0,0,0,241,239,
        1,0,0,0,241,242,1,0,0,0,242,7,1,0,0,0,243,244,5,119,0,0,244,9,1,
        0,0,0,245,249,5,119,0,0,246,249,3,64,32,0,247,249,3,204,102,0,248,
        245,1,0,0,0,248,246,1,0,0,0,248,247,1,0,0,0,249,250,1,0,0,0,250,
        248,1,0,0,0,250,251,1,0,0,0,251,11,1,0,0,0,252,253,5,2,0,0,253,255,
        5,23,0,0,254,256,3,160,80,0,255,254,1,0,0,0,255,256,1,0,0,0,256,
        258,1,0,0,0,257,259,3,164,82,0,258,257,1,0,0,0,258,259,1,0,0,0,259,
        261,1,0,0,0,260,262,3,14,7,0,261,260,1,0,0,0,262,263,1,0,0,0,263,
        261,1,0,0,0,263,264,1,0,0,0,264,13,1,0,0,0,265,267,3,64,32,0,266,
        268,3,16,8,0,267,266,1,0,0,0,268,269,1,0,0,0,269,267,1,0,0,0,269,
        270,1,0,0,0,270,15,1,0,0,0,271,286,3,54,27,0,272,286,3,56,28,0,273,
        286,3,60,30,0,274,286,3,62,31,0,275,286,3,50,25,0,276,286,3,46,23,
        0,277,286,3,42,21,0,278,286,3,38,19,0,279,286,3,30,15,0,280,286,
        3,34,17,0,281,286,3,26,13,0,282,286,3,164,82,0,283,286,3,22,11,0,
        284,286,3,18,9,0,285,271,1,0,0,0,285,272,1,0,0,0,285,273,1,0,0,0,
        285,274,1,0,0,0,285,275,1,0,0,0,285,276,1,0,0,0,285,277,1,0,0,0,
        285,278,1,0,0,0,285,279,1,0,0,0,285,280,1,0,0,0,285,281,1,0,0,0,
        285,282,1,0,0,0,285,283,1,0,0,0,285,284,1,0,0,0,286,17,1,0,0,0,287,
        288,5,110,0,0,288,289,5,1,0,0,289,290,3,20,10,0,290,291,5,2,0,0,
        291,19,1,0,0,0,292,300,5,111,0,0,293,300,5,112,0,0,294,296,5,119,
        0,0,295,294,1,0,0,0,296,297,1,0,0,0,297,295,1,0,0,0,297,298,1,0,
        0,0,298,300,1,0,0,0,299,292,1,0,0,0,299,293,1,0,0,0,299,295,1,0,
        0,0,300,21,1,0,0,0,301,302,5,108,0,0,302,303,5,1,0,0,303,304,3,24,
        12,0,304,305,5,2,0,0,305,23,1,0,0,0,306,307,7,0,0,0,307,25,1,0,0,
        0,308,309,5,105,0,0,309,310,5,1,0,0,310,311,3,28,14,0,311,312,5,
        2,0,0,312,27,1,0,0,0,313,314,7,1,0,0,314,29,1,0,0,0,315,316,5,97,
        0,0,316,317,5,1,0,0,317,318,3,32,16,0,318,319,5,2,0,0,319,31,1,0,
        0,0,320,321,7,2,0,0,321,33,1,0,0,0,322,323,5,100,0,0,323,324,5,1,
        0,0,324,325,3,36,18,0,325,326,5,2,0,0,326,35,1,0,0,0,327,328,7,3,
        0,0,328,37,1,0,0,0,329,330,5,91,0,0,330,331,5,1,0,0,331,332,3,40,
        20,0,332,333,5,2,0,0,333,39,1,0,0,0,334,335,7,3,0,0,335,41,1,0,0,
        0,336,337,5,92,0,0,337,338,5,1,0,0,338,339,3,44,22,0,339,340,5,2,
        0,0,340,43,1,0,0,0,341,342,7,4,0,0,342,45,1,0,0,0,343,344,5,88,0,
        0,344,345,5,1,0,0,345,346,3,48,24,0,346,347,5,2,0,0,347,47,1,0,0,
        0,348,349,7,0,0,0,349,49,1,0,0,0,350,351,5,53,0,0,351,352,5,1,0,
        0,352,353,3,52,26,0,353,354,5,2,0,0,354,51,1,0,0,0,355,356,7,3,0,
        0,356,53,1,0,0,0,357,358,5,37,0,0,358,359,5,1,0,0,359,360,3,202,
        101,0,360,361,5,2,0,0,361,55,1,0,0,0,362,363,5,33,0,0,363,364,5,
        1,0,0,364,365,3,58,29,0,365,366,5,2,0,0,366,57,1,0,0,0,367,368,7,
        5,0,0,368,59,1,0,0,0,369,370,5,25,0,0,370,371,5,1,0,0,371,372,3,
        202,101,0,372,373,5,2,0,0,373,61,1,0,0,0,374,375,5,32,0,0,375,376,
        5,1,0,0,376,377,3,202,101,0,377,378,5,2,0,0,378,63,1,0,0,0,379,380,
        7,6,0,0,380,65,1,0,0,0,381,382,5,2,0,0,382,386,5,24,0,0,383,385,
        3,68,34,0,384,383,1,0,0,0,385,388,1,0,0,0,386,384,1,0,0,0,386,387,
        1,0,0,0,387,67,1,0,0,0,388,386,1,0,0,0,389,395,3,70,35,0,390,395,
        3,72,36,0,391,395,3,160,80,0,392,395,3,164,82,0,393,395,3,78,39,
        0,394,389,1,0,0,0,394,390,1,0,0,0,394,391,1,0,0,0,394,392,1,0,0,
        0,394,393,1,0,0,0,395,69,1,0,0,0,396,397,5,38,0,0,397,71,1,0,0,0,
        398,399,5,39,0,0,399,400,5,1,0,0,400,402,3,74,37,0,401,403,5,9,0,
        0,402,401,1,0,0,0,402,403,1,0,0,0,403,404,1,0,0,0,404,405,3,76,38,
        0,405,406,5,2,0,0,406,73,1,0,0,0,407,408,5,116,0,0,408,75,1,0,0,
        0,409,410,5,116,0,0,410,77,1,0,0,0,411,412,5,95,0,0,412,413,5,1,
        0,0,413,414,3,74,37,0,414,415,5,2,0,0,415,79,1,0,0,0,416,423,3,138,
        69,0,417,423,3,146,73,0,418,423,3,84,42,0,419,423,3,104,52,0,420,
        423,3,144,72,0,421,423,3,82,41,0,422,416,1,0,0,0,422,417,1,0,0,0,
        422,418,1,0,0,0,422,419,1,0,0,0,422,420,1,0,0,0,422,421,1,0,0,0,
        423,81,1,0,0,0,424,425,5,109,0,0,425,426,5,1,0,0,426,427,3,140,70,
        0,427,428,5,2,0,0,428,83,1,0,0,0,429,430,5,47,0,0,430,431,3,86,43,
        0,431,433,3,102,51,0,432,434,3,136,68,0,433,432,1,0,0,0,433,434,
        1,0,0,0,434,85,1,0,0,0,435,439,3,90,45,0,436,438,3,88,44,0,437,436,
        1,0,0,0,438,441,1,0,0,0,439,437,1,0,0,0,439,440,1,0,0,0,440,87,1,
        0,0,0,441,439,1,0,0,0,442,445,7,7,0,0,443,446,3,90,45,0,444,446,
        5,116,0,0,445,443,1,0,0,0,445,444,1,0,0,0,446,89,1,0,0,0,447,449,
        5,50,0,0,448,447,1,0,0,0,448,449,1,0,0,0,449,450,1,0,0,0,450,451,
        3,92,46,0,451,91,1,0,0,0,452,453,5,1,0,0,453,454,3,86,43,0,454,455,
        5,2,0,0,455,458,1,0,0,0,456,458,3,94,47,0,457,452,1,0,0,0,457,456,
        1,0,0,0,458,93,1,0,0,0,459,460,3,96,48,0,460,95,1,0,0,0,461,462,
        3,98,49,0,462,463,3,100,50,0,463,465,1,0,0,0,464,461,1,0,0,0,464,
        465,1,0,0,0,465,466,1,0,0,0,466,471,3,98,49,0,467,468,5,9,0,0,468,
        470,3,98,49,0,469,467,1,0,0,0,470,473,1,0,0,0,471,469,1,0,0,0,471,
        472,1,0,0,0,472,97,1,0,0,0,473,471,1,0,0,0,474,475,3,202,101,0,475,
        99,1,0,0,0,476,477,5,10,0,0,477,101,1,0,0,0,478,485,3,80,40,0,479,
        481,3,104,52,0,480,479,1,0,0,0,481,482,1,0,0,0,482,480,1,0,0,0,482,
        483,1,0,0,0,483,485,1,0,0,0,484,478,1,0,0,0,484,480,1,0,0,0,485,
        103,1,0,0,0,486,487,5,56,0,0,487,488,5,1,0,0,488,489,3,140,70,0,
        489,490,5,9,0,0,490,495,3,108,54,0,491,492,5,9,0,0,492,494,3,108,
        54,0,493,491,1,0,0,0,494,497,1,0,0,0,495,493,1,0,0,0,495,496,1,0,
        0,0,496,500,1,0,0,0,497,495,1,0,0,0,498,499,5,9,0,0,499,501,3,106,
        53,0,500,498,1,0,0,0,500,501,1,0,0,0,501,502,1,0,0,0,502,503,5,2,
        0,0,503,105,1,0,0,0,504,505,5,45,0,0,505,506,5,10,0,0,506,507,3,
        202,101,0,507,107,1,0,0,0,508,514,3,110,55,0,509,514,3,112,56,0,
        510,514,3,114,57,0,511,514,3,116,58,0,512,514,3,120,60,0,513,508,
        1,0,0,0,513,509,1,0,0,0,513,510,1,0,0,0,513,511,1,0,0,0,513,512,
        1,0,0,0,514,109,1,0,0,0,515,516,7,8,0,0,516,111,1,0,0,0,517,518,
        5,75,0,0,518,519,5,9,0,0,519,520,3,100,50,0,520,521,5,9,0,0,521,
        522,3,122,61,0,522,113,1,0,0,0,523,524,5,76,0,0,524,525,5,9,0,0,
        525,530,3,202,101,0,526,527,5,9,0,0,527,529,3,202,101,0,528,526,
        1,0,0,0,529,532,1,0,0,0,530,528,1,0,0,0,530,531,1,0,0,0,531,543,
        1,0,0,0,532,530,1,0,0,0,533,534,5,77,0,0,534,535,5,9,0,0,535,543,
        3,126,63,0,536,537,5,78,0,0,537,538,5,9,0,0,538,543,3,126,63,0,539,
        540,5,79,0,0,540,541,5,9,0,0,541,543,3,202,101,0,542,523,1,0,0,0,
        542,533,1,0,0,0,542,536,1,0,0,0,542,539,1,0,0,0,543,115,1,0,0,0,
        544,545,5,83,0,0,545,546,5,9,0,0,546,556,3,118,59,0,547,548,5,84,
        0,0,548,549,5,9,0,0,549,550,3,128,64,0,550,551,5,9,0,0,551,552,3,
        130,65,0,552,553,5,9,0,0,553,554,3,124,62,0,554,556,1,0,0,0,555,
        544,1,0,0,0,555,547,1,0,0,0,556,117,1,0,0,0,557,558,7,9,0,0,558,
        119,1,0,0,0,559,560,5,85,0,0,560,561,5,9,0,0,561,562,3,132,66,0,
        562,563,5,9,0,0,563,564,3,134,67,0,564,121,1,0,0,0,565,566,5,116,
        0,0,566,123,1,0,0,0,567,568,5,120,0,0,568,125,1,0,0,0,569,574,5,
        119,0,0,570,571,5,9,0,0,571,573,5,119,0,0,572,570,1,0,0,0,573,576,
        1,0,0,0,574,572,1,0,0,0,574,575,1,0,0,0,575,127,1,0,0,0,576,574,
        1,0,0,0,577,578,5,119,0,0,578,129,1,0,0,0,579,580,5,120,0,0,580,
        131,1,0,0,0,581,582,3,202,101,0,582,133,1,0,0,0,583,584,3,202,101,
        0,584,135,1,0,0,0,585,587,5,51,0,0,586,588,3,80,40,0,587,586,1,0,
        0,0,587,588,1,0,0,0,588,137,1,0,0,0,589,590,3,140,70,0,590,591,3,
        142,71,0,591,139,1,0,0,0,592,593,5,119,0,0,593,141,1,0,0,0,594,595,
        5,10,0,0,595,596,3,202,101,0,596,143,1,0,0,0,597,598,5,41,0,0,598,
        602,3,148,74,0,599,601,3,152,76,0,600,599,1,0,0,0,601,604,1,0,0,
        0,602,600,1,0,0,0,602,603,1,0,0,0,603,145,1,0,0,0,604,602,1,0,0,
        0,605,606,5,42,0,0,606,610,3,148,74,0,607,609,3,154,77,0,608,607,
        1,0,0,0,609,612,1,0,0,0,610,608,1,0,0,0,610,611,1,0,0,0,611,147,
        1,0,0,0,612,610,1,0,0,0,613,634,5,119,0,0,614,616,5,1,0,0,615,617,
        3,150,75,0,616,615,1,0,0,0,617,618,1,0,0,0,618,616,1,0,0,0,618,619,
        1,0,0,0,619,620,1,0,0,0,620,621,5,2,0,0,621,634,1,0,0,0,622,623,
        5,1,0,0,623,628,3,150,75,0,624,625,5,9,0,0,625,627,3,150,75,0,626,
        624,1,0,0,0,627,630,1,0,0,0,628,626,1,0,0,0,628,629,1,0,0,0,629,
        631,1,0,0,0,630,628,1,0,0,0,631,632,5,2,0,0,632,634,1,0,0,0,633,
        613,1,0,0,0,633,614,1,0,0,0,633,622,1,0,0,0,634,149,1,0,0,0,635,
        636,3,202,101,0,636,151,1,0,0,0,637,638,3,202,101,0,638,153,1,0,
        0,0,639,640,3,202,101,0,640,155,1,0,0,0,641,642,5,2,0,0,642,646,
        5,40,0,0,643,645,3,80,40,0,644,643,1,0,0,0,645,648,1,0,0,0,646,644,
        1,0,0,0,646,647,1,0,0,0,647,157,1,0,0,0,648,646,1,0,0,0,649,650,
        5,2,0,0,650,654,5,43,0,0,651,653,3,80,40,0,652,651,1,0,0,0,653,656,
        1,0,0,0,654,652,1,0,0,0,654,655,1,0,0,0,655,159,1,0,0,0,656,654,
        1,0,0,0,657,658,5,26,0,0,658,660,5,1,0,0,659,661,3,162,81,0,660,
        659,1,0,0,0,661,662,1,0,0,0,662,660,1,0,0,0,662,663,1,0,0,0,663,
        664,1,0,0,0,664,665,5,2,0,0,665,161,1,0,0,0,666,667,3,64,32,0,667,
        163,1,0,0,0,668,669,5,27,0,0,669,670,5,1,0,0,670,671,3,166,83,0,
        671,672,5,2,0,0,672,165,1,0,0,0,673,674,7,10,0,0,674,167,1,0,0,0,
        675,676,5,2,0,0,676,677,5,44,0,0,677,169,1,0,0,0,678,683,3,192,96,
        0,679,683,3,184,92,0,680,683,3,176,88,0,681,683,3,172,86,0,682,678,
        1,0,0,0,682,679,1,0,0,0,682,680,1,0,0,0,682,681,1,0,0,0,683,171,
        1,0,0,0,684,685,5,113,0,0,685,686,5,1,0,0,686,691,3,174,87,0,687,
        688,5,9,0,0,688,690,3,174,87,0,689,687,1,0,0,0,690,693,1,0,0,0,691,
        689,1,0,0,0,691,692,1,0,0,0,692,694,1,0,0,0,693,691,1,0,0,0,694,
        695,5,2,0,0,695,173,1,0,0,0,696,697,7,11,0,0,697,175,1,0,0,0,698,
        699,5,101,0,0,699,700,5,1,0,0,700,705,3,178,89,0,701,702,5,9,0,0,
        702,704,3,178,89,0,703,701,1,0,0,0,704,707,1,0,0,0,705,703,1,0,0,
        0,705,706,1,0,0,0,706,708,1,0,0,0,707,705,1,0,0,0,708,709,5,2,0,
        0,709,177,1,0,0,0,710,711,5,119,0,0,711,179,1,0,0,0,712,715,5,120,
        0,0,713,715,3,140,70,0,714,712,1,0,0,0,714,713,1,0,0,0,715,181,1,
        0,0,0,716,719,5,116,0,0,717,719,3,140,70,0,718,716,1,0,0,0,718,717,
        1,0,0,0,719,183,1,0,0,0,720,721,5,36,0,0,721,722,5,1,0,0,722,723,
        3,186,93,0,723,726,5,9,0,0,724,727,3,188,94,0,725,727,3,190,95,0,
        726,724,1,0,0,0,726,725,1,0,0,0,727,728,1,0,0,0,728,729,5,2,0,0,
        729,185,1,0,0,0,730,731,3,180,90,0,731,187,1,0,0,0,732,733,3,182,
        91,0,733,189,1,0,0,0,734,735,3,180,90,0,735,191,1,0,0,0,736,737,
        5,52,0,0,737,738,5,1,0,0,738,743,3,196,98,0,739,740,5,9,0,0,740,
        742,3,196,98,0,741,739,1,0,0,0,742,745,1,0,0,0,743,741,1,0,0,0,743,
        744,1,0,0,0,744,746,1,0,0,0,745,743,1,0,0,0,746,747,5,9,0,0,747,
        748,3,194,97,0,748,749,5,2,0,0,749,193,1,0,0,0,750,751,5,120,0,0,
        751,195,1,0,0,0,752,753,3,198,99,0,753,754,3,200,100,0,754,197,1,
        0,0,0,755,756,3,202,101,0,756,199,1,0,0,0,757,758,3,202,101,0,758,
        201,1,0,0,0,759,767,5,119,0,0,760,767,3,180,90,0,761,767,3,170,85,
        0,762,767,3,182,91,0,763,767,5,11,0,0,764,767,3,140,70,0,765,767,
        3,204,102,0,766,759,1,0,0,0,766,760,1,0,0,0,766,761,1,0,0,0,766,
        762,1,0,0,0,766,763,1,0,0,0,766,764,1,0,0,0,766,765,1,0,0,0,767,
        203,1,0,0,0,768,769,7,12,0,0,769,205,1,0,0,0,51,209,220,227,235,
        241,248,250,255,258,263,269,285,297,299,386,394,402,422,433,439,
        445,448,457,464,471,482,484,495,500,513,530,542,555,574,587,602,
        610,618,628,633,646,654,662,682,691,705,714,718,726,743,766
    ]

class PanelParser ( Parser ):

    grammarFileName = "Panel.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'\\'", "'/'", "'@'", "'!'", 
                     "'$'", "'?'", "','", "'='", "'*'", "'+'", "'#'", "'\"'", 
                     "'_'", "'|'", "']'", "'['", "'''", "'>'", "'<'", "'^'" ]

    symbolicNames = [ "<INVALID>", "LPAREN", "RPAREN", "SSLASH", "SLASH", 
                      "AMPCHAR", "EXCLAIMCHAR", "DOLLARCHAR", "JP_MYSTERYCHAR", 
                      "COMMACHAR", "EQUALCHAR", "ASTERISK", "PLUSCHAR", 
                      "HASHCHAR", "DOUBLEQUOTE", "UNDERSCORE", "PIPECHAR", 
                      "RBRACKET", "LBRACKET", "SINGLEQUOTE", "GREATERTHAN", 
                      "LESSTHAN", "CARET", "ATTR", "BODY", "COLOR", "DEFAULT", 
                      "FORMAT", "HIGH", "EBCDIC", "DBCS", "MIX", "HILITE", 
                      "INTENS", "LOW", "NON", "TRUNC", "TYPE", "KANA", "WINDOW", 
                      "INIT", "VGET", "VPUT", "PROC", "END", "MSG", "THEN", 
                      "IF", "AND", "OR", "NOT", "ELSE", "TRANS", "SKIP_", 
                      "ON", "OFF", "VER", "NONBLANK", "ALPHA", "ALPHAB", 
                      "BIT", "DSNAME", "DSNAMEF", "DSNAMEFM", "DSNAMEPQ", 
                      "DSNAMEQ", "ENUM", "FILEID", "HEX", "IDATE", "INCLUDE", 
                      "IPADDR4", "ITIME", "JDATE", "JSTD", "LEN", "LIST", 
                      "LISTV", "LISTVX", "LISTX", "NAME", "NAMEF", "NUM", 
                      "PICT", "PICTCN", "RANGE", "STDDATE", "STDTIME", "PAD", 
                      "NULLS", "USER", "EXTEND", "CAPS", "IN", "OUT", "WIDTH", 
                      "SCRL", "AREA", "DYNAMIC", "GRAPHIC", "SCROLL", "LVLINE", 
                      "LEFT", "RIGHT", "AXIS", "JUST", "MODEL", "REINIT", 
                      "PADC", "REFRESH", "OUTLINE", "NONE", "BOX", "PFK", 
                      "NEWLINE", "WS", "INTEGERLITERAL", "COMMENT", "COMMENT2", 
                      "IDENTIFIER", "STRINGLITERAL", "JP_CHAR" ]

    RULE_startRule = 0
    RULE_section = 1
    RULE_reinitSection = 2
    RULE_modelSection = 3
    RULE_modelParam = 4
    RULE_model = 5
    RULE_attributeSection = 6
    RULE_attributeComponent = 7
    RULE_attrParameter = 8
    RULE_outlineParam = 9
    RULE_outlineValue = 10
    RULE_padcParam = 11
    RULE_padcValue = 12
    RULE_justParam = 13
    RULE_justValue = 14
    RULE_areaParam = 15
    RULE_areaValue = 16
    RULE_scrollParam = 17
    RULE_scrollValue = 18
    RULE_extendParam = 19
    RULE_extendValue = 20
    RULE_capsParam = 21
    RULE_capsValue = 22
    RULE_padParam = 23
    RULE_padValue = 24
    RULE_skipParam = 25
    RULE_skipValue = 26
    RULE_typeParam = 27
    RULE_intensParam = 28
    RULE_intensValue = 29
    RULE_colorParam = 30
    RULE_hiliteParam = 31
    RULE_attrChar = 32
    RULE_bodySection = 33
    RULE_bodyParam = 34
    RULE_kanaParam = 35
    RULE_windowParam = 36
    RULE_width = 37
    RULE_length = 38
    RULE_widthPara = 39
    RULE_statement = 40
    RULE_refreshStatement = 41
    RULE_ifStatement = 42
    RULE_condition = 43
    RULE_andOrCondition = 44
    RULE_combinableCondition = 45
    RULE_simpleCondition = 46
    RULE_relationCondition = 47
    RULE_relationArithmeticComparison = 48
    RULE_arithmeticExpression = 49
    RULE_relationalOperator = 50
    RULE_thenIf = 51
    RULE_verStatement = 52
    RULE_verMsg = 53
    RULE_verCriteria = 54
    RULE_simpleCriteria = 55
    RULE_lengthCriteria = 56
    RULE_listCriteria = 57
    RULE_pictCriteria = 58
    RULE_picValue = 59
    RULE_rangeCriteria = 60
    RULE_expectedLength = 61
    RULE_stringValue = 62
    RULE_varlist = 63
    RULE_maskCharacter = 64
    RULE_fieldMask = 65
    RULE_lower = 66
    RULE_upper = 67
    RULE_elseIf = 68
    RULE_assignStatement = 69
    RULE_variable = 70
    RULE_assignPart = 71
    RULE_vgetStatement = 72
    RULE_vputStatement = 73
    RULE_name_list = 74
    RULE_name_list_item = 75
    RULE_vgetParameter = 76
    RULE_vputParameter = 77
    RULE_initSection = 78
    RULE_procSection = 79
    RULE_defaultParam = 80
    RULE_defValue = 81
    RULE_formatParam = 82
    RULE_formatValue = 83
    RULE_endSection = 84
    RULE_panelFunction = 85
    RULE_pfkFunc = 86
    RULE_pfkParam = 87
    RULE_lvlineFunc = 88
    RULE_lvlineParam = 89
    RULE_stringExpression = 90
    RULE_integerExpression = 91
    RULE_truncFunc = 92
    RULE_stringToTrunc = 93
    RULE_indexToTrunc = 94
    RULE_subStringToTrunc = 95
    RULE_transFunc = 96
    RULE_transDefaultOutput = 97
    RULE_transParam = 98
    RULE_transVariable = 99
    RULE_transReturn = 100
    RULE_value = 101
    RULE_charDataKeyword = 102

    ruleNames =  [ "startRule", "section", "reinitSection", "modelSection", 
                   "modelParam", "model", "attributeSection", "attributeComponent", 
                   "attrParameter", "outlineParam", "outlineValue", "padcParam", 
                   "padcValue", "justParam", "justValue", "areaParam", "areaValue", 
                   "scrollParam", "scrollValue", "extendParam", "extendValue", 
                   "capsParam", "capsValue", "padParam", "padValue", "skipParam", 
                   "skipValue", "typeParam", "intensParam", "intensValue", 
                   "colorParam", "hiliteParam", "attrChar", "bodySection", 
                   "bodyParam", "kanaParam", "windowParam", "width", "length", 
                   "widthPara", "statement", "refreshStatement", "ifStatement", 
                   "condition", "andOrCondition", "combinableCondition", 
                   "simpleCondition", "relationCondition", "relationArithmeticComparison", 
                   "arithmeticExpression", "relationalOperator", "thenIf", 
                   "verStatement", "verMsg", "verCriteria", "simpleCriteria", 
                   "lengthCriteria", "listCriteria", "pictCriteria", "picValue", 
                   "rangeCriteria", "expectedLength", "stringValue", "varlist", 
                   "maskCharacter", "fieldMask", "lower", "upper", "elseIf", 
                   "assignStatement", "variable", "assignPart", "vgetStatement", 
                   "vputStatement", "name_list", "name_list_item", "vgetParameter", 
                   "vputParameter", "initSection", "procSection", "defaultParam", 
                   "defValue", "formatParam", "formatValue", "endSection", 
                   "panelFunction", "pfkFunc", "pfkParam", "lvlineFunc", 
                   "lvlineParam", "stringExpression", "integerExpression", 
                   "truncFunc", "stringToTrunc", "indexToTrunc", "subStringToTrunc", 
                   "transFunc", "transDefaultOutput", "transParam", "transVariable", 
                   "transReturn", "value", "charDataKeyword" ]

    EOF = Token.EOF
    LPAREN=1
    RPAREN=2
    SSLASH=3
    SLASH=4
    AMPCHAR=5
    EXCLAIMCHAR=6
    DOLLARCHAR=7
    JP_MYSTERYCHAR=8
    COMMACHAR=9
    EQUALCHAR=10
    ASTERISK=11
    PLUSCHAR=12
    HASHCHAR=13
    DOUBLEQUOTE=14
    UNDERSCORE=15
    PIPECHAR=16
    RBRACKET=17
    LBRACKET=18
    SINGLEQUOTE=19
    GREATERTHAN=20
    LESSTHAN=21
    CARET=22
    ATTR=23
    BODY=24
    COLOR=25
    DEFAULT=26
    FORMAT=27
    HIGH=28
    EBCDIC=29
    DBCS=30
    MIX=31
    HILITE=32
    INTENS=33
    LOW=34
    NON=35
    TRUNC=36
    TYPE=37
    KANA=38
    WINDOW=39
    INIT=40
    VGET=41
    VPUT=42
    PROC=43
    END=44
    MSG=45
    THEN=46
    IF=47
    AND=48
    OR=49
    NOT=50
    ELSE=51
    TRANS=52
    SKIP_=53
    ON=54
    OFF=55
    VER=56
    NONBLANK=57
    ALPHA=58
    ALPHAB=59
    BIT=60
    DSNAME=61
    DSNAMEF=62
    DSNAMEFM=63
    DSNAMEPQ=64
    DSNAMEQ=65
    ENUM=66
    FILEID=67
    HEX=68
    IDATE=69
    INCLUDE=70
    IPADDR4=71
    ITIME=72
    JDATE=73
    JSTD=74
    LEN=75
    LIST=76
    LISTV=77
    LISTVX=78
    LISTX=79
    NAME=80
    NAMEF=81
    NUM=82
    PICT=83
    PICTCN=84
    RANGE=85
    STDDATE=86
    STDTIME=87
    PAD=88
    NULLS=89
    USER=90
    EXTEND=91
    CAPS=92
    IN=93
    OUT=94
    WIDTH=95
    SCRL=96
    AREA=97
    DYNAMIC=98
    GRAPHIC=99
    SCROLL=100
    LVLINE=101
    LEFT=102
    RIGHT=103
    AXIS=104
    JUST=105
    MODEL=106
    REINIT=107
    PADC=108
    REFRESH=109
    OUTLINE=110
    NONE=111
    BOX=112
    PFK=113
    NEWLINE=114
    WS=115
    INTEGERLITERAL=116
    COMMENT=117
    COMMENT2=118
    IDENTIFIER=119
    STRINGLITERAL=120
    JP_CHAR=121

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartRuleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(PanelParser.EOF, 0)

        def section(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PanelParser.SectionContext)
            else:
                return self.getTypedRuleContext(PanelParser.SectionContext,i)


        def getRuleIndex(self):
            return PanelParser.RULE_startRule

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStartRule" ):
                listener.enterStartRule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStartRule" ):
                listener.exitStartRule(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStartRule" ):
                return visitor.visitStartRule(self)
            else:
                return visitor.visitChildren(self)




    def startRule(self):

        localctx = PanelParser.StartRuleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_startRule)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 206
                self.section()
                self.state = 209 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==2):
                    break

            self.state = 211
            self.match(PanelParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attributeSection(self):
            return self.getTypedRuleContext(PanelParser.AttributeSectionContext,0)


        def bodySection(self):
            return self.getTypedRuleContext(PanelParser.BodySectionContext,0)


        def initSection(self):
            return self.getTypedRuleContext(PanelParser.InitSectionContext,0)


        def procSection(self):
            return self.getTypedRuleContext(PanelParser.ProcSectionContext,0)


        def endSection(self):
            return self.getTypedRuleContext(PanelParser.EndSectionContext,0)


        def modelSection(self):
            return self.getTypedRuleContext(PanelParser.ModelSectionContext,0)


        def reinitSection(self):
            return self.getTypedRuleContext(PanelParser.ReinitSectionContext,0)


        def getRuleIndex(self):
            return PanelParser.RULE_section

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSection" ):
                listener.enterSection(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSection" ):
                listener.exitSection(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSection" ):
                return visitor.visitSection(self)
            else:
                return visitor.visitChildren(self)




    def section(self):

        localctx = PanelParser.SectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_section)
        try:
            self.state = 220
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 213
                self.attributeSection()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 214
                self.bodySection()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 215
                self.initSection()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 216
                self.procSection()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 217
                self.endSection()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 218
                self.modelSection()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 219
                self.reinitSection()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReinitSectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RPAREN(self):
            return self.getToken(PanelParser.RPAREN, 0)

        def REINIT(self):
            return self.getToken(PanelParser.REINIT, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PanelParser.StatementContext)
            else:
                return self.getTypedRuleContext(PanelParser.StatementContext,i)


        def getRuleIndex(self):
            return PanelParser.RULE_reinitSection

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReinitSection" ):
                listener.enterReinitSection(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReinitSection" ):
                listener.exitReinitSection(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReinitSection" ):
                return visitor.visitReinitSection(self)
            else:
                return visitor.visitChildren(self)




    def reinitSection(self):

        localctx = PanelParser.ReinitSectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_reinitSection)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            self.match(PanelParser.RPAREN)
            self.state = 223
            self.match(PanelParser.REINIT)
            self.state = 227
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 72204928596049920) != 0) or _la==109 or _la==119:
                self.state = 224
                self.statement()
                self.state = 229
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ModelSectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RPAREN(self):
            return self.getToken(PanelParser.RPAREN, 0)

        def MODEL(self):
            return self.getToken(PanelParser.MODEL, 0)

        def modelParam(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PanelParser.ModelParamContext)
            else:
                return self.getTypedRuleContext(PanelParser.ModelParamContext,i)


        def model(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PanelParser.ModelContext)
            else:
                return self.getTypedRuleContext(PanelParser.ModelContext,i)


        def getRuleIndex(self):
            return PanelParser.RULE_modelSection

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModelSection" ):
                listener.enterModelSection(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModelSection" ):
                listener.exitModelSection(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitModelSection" ):
                return visitor.visitModelSection(self)
            else:
                return visitor.visitChildren(self)




    def modelSection(self):

        localctx = PanelParser.ModelSectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_modelSection)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self.match(PanelParser.RPAREN)
            self.state = 231
            self.match(PanelParser.MODEL)
            self.state = 235
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 232
                    self.modelParam() 
                self.state = 237
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

            self.state = 239 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 238
                self.model()
                self.state = 241 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 35321819429368) != 0) or ((((_la - 80)) & ~0x3f) == 0 and ((1 << (_la - 80)) & 2748779070465) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ModelParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(PanelParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return PanelParser.RULE_modelParam

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModelParam" ):
                listener.enterModelParam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModelParam" ):
                listener.exitModelParam(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitModelParam" ):
                return visitor.visitModelParam(self)
            else:
                return visitor.visitChildren(self)




    def modelParam(self):

        localctx = PanelParser.ModelParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_modelParam)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 243
            self.match(PanelParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ModelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(PanelParser.IDENTIFIER)
            else:
                return self.getToken(PanelParser.IDENTIFIER, i)

        def attrChar(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PanelParser.AttrCharContext)
            else:
                return self.getTypedRuleContext(PanelParser.AttrCharContext,i)


        def charDataKeyword(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PanelParser.CharDataKeywordContext)
            else:
                return self.getTypedRuleContext(PanelParser.CharDataKeywordContext,i)


        def getRuleIndex(self):
            return PanelParser.RULE_model

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModel" ):
                listener.enterModel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModel" ):
                listener.exitModel(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitModel" ):
                return visitor.visitModel(self)
            else:
                return visitor.visitChildren(self)




    def model(self):

        localctx = PanelParser.ModelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_model)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 248
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [119]:
                        self.state = 245
                        self.match(PanelParser.IDENTIFIER)
                        pass
                    elif token in [3, 4, 5, 6, 7, 8, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 121]:
                        self.state = 246
                        self.attrChar()
                        pass
                    elif token in [37, 45, 80, 90]:
                        self.state = 247
                        self.charDataKeyword()
                        pass
                    else:
                        raise NoViableAltException(self)


                else:
                    raise NoViableAltException(self)
                self.state = 250 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttributeSectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RPAREN(self):
            return self.getToken(PanelParser.RPAREN, 0)

        def ATTR(self):
            return self.getToken(PanelParser.ATTR, 0)

        def defaultParam(self):
            return self.getTypedRuleContext(PanelParser.DefaultParamContext,0)


        def formatParam(self):
            return self.getTypedRuleContext(PanelParser.FormatParamContext,0)


        def attributeComponent(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PanelParser.AttributeComponentContext)
            else:
                return self.getTypedRuleContext(PanelParser.AttributeComponentContext,i)


        def getRuleIndex(self):
            return PanelParser.RULE_attributeSection

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttributeSection" ):
                listener.enterAttributeSection(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttributeSection" ):
                listener.exitAttributeSection(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttributeSection" ):
                return visitor.visitAttributeSection(self)
            else:
                return visitor.visitChildren(self)




    def attributeSection(self):

        localctx = PanelParser.AttributeSectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_attributeSection)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 252
            self.match(PanelParser.RPAREN)
            self.state = 253
            self.match(PanelParser.ATTR)
            self.state = 255
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==26:
                self.state = 254
                self.defaultParam()


            self.state = 258
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==27:
                self.state = 257
                self.formatParam()


            self.state = 261 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 260
                self.attributeComponent()
                self.state = 263 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 8387064) != 0) or _la==121):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttributeComponentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attrChar(self):
            return self.getTypedRuleContext(PanelParser.AttrCharContext,0)


        def attrParameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PanelParser.AttrParameterContext)
            else:
                return self.getTypedRuleContext(PanelParser.AttrParameterContext,i)


        def getRuleIndex(self):
            return PanelParser.RULE_attributeComponent

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttributeComponent" ):
                listener.enterAttributeComponent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttributeComponent" ):
                listener.exitAttributeComponent(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttributeComponent" ):
                return visitor.visitAttributeComponent(self)
            else:
                return visitor.visitChildren(self)




    def attributeComponent(self):

        localctx = PanelParser.AttributeComponentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_attributeComponent)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 265
            self.attrChar()
            self.state = 267 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 266
                self.attrParameter()
                self.state = 269 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 9007349746368512) != 0) or ((((_la - 88)) & ~0x3f) == 0 and ((1 << (_la - 88)) & 5378585) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttrParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeParam(self):
            return self.getTypedRuleContext(PanelParser.TypeParamContext,0)


        def intensParam(self):
            return self.getTypedRuleContext(PanelParser.IntensParamContext,0)


        def colorParam(self):
            return self.getTypedRuleContext(PanelParser.ColorParamContext,0)


        def hiliteParam(self):
            return self.getTypedRuleContext(PanelParser.HiliteParamContext,0)


        def skipParam(self):
            return self.getTypedRuleContext(PanelParser.SkipParamContext,0)


        def padParam(self):
            return self.getTypedRuleContext(PanelParser.PadParamContext,0)


        def capsParam(self):
            return self.getTypedRuleContext(PanelParser.CapsParamContext,0)


        def extendParam(self):
            return self.getTypedRuleContext(PanelParser.ExtendParamContext,0)


        def areaParam(self):
            return self.getTypedRuleContext(PanelParser.AreaParamContext,0)


        def scrollParam(self):
            return self.getTypedRuleContext(PanelParser.ScrollParamContext,0)


        def justParam(self):
            return self.getTypedRuleContext(PanelParser.JustParamContext,0)


        def formatParam(self):
            return self.getTypedRuleContext(PanelParser.FormatParamContext,0)


        def padcParam(self):
            return self.getTypedRuleContext(PanelParser.PadcParamContext,0)


        def outlineParam(self):
            return self.getTypedRuleContext(PanelParser.OutlineParamContext,0)


        def getRuleIndex(self):
            return PanelParser.RULE_attrParameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttrParameter" ):
                listener.enterAttrParameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttrParameter" ):
                listener.exitAttrParameter(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttrParameter" ):
                return visitor.visitAttrParameter(self)
            else:
                return visitor.visitChildren(self)




    def attrParameter(self):

        localctx = PanelParser.AttrParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_attrParameter)
        try:
            self.state = 285
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [37]:
                self.enterOuterAlt(localctx, 1)
                self.state = 271
                self.typeParam()
                pass
            elif token in [33]:
                self.enterOuterAlt(localctx, 2)
                self.state = 272
                self.intensParam()
                pass
            elif token in [25]:
                self.enterOuterAlt(localctx, 3)
                self.state = 273
                self.colorParam()
                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 4)
                self.state = 274
                self.hiliteParam()
                pass
            elif token in [53]:
                self.enterOuterAlt(localctx, 5)
                self.state = 275
                self.skipParam()
                pass
            elif token in [88]:
                self.enterOuterAlt(localctx, 6)
                self.state = 276
                self.padParam()
                pass
            elif token in [92]:
                self.enterOuterAlt(localctx, 7)
                self.state = 277
                self.capsParam()
                pass
            elif token in [91]:
                self.enterOuterAlt(localctx, 8)
                self.state = 278
                self.extendParam()
                pass
            elif token in [97]:
                self.enterOuterAlt(localctx, 9)
                self.state = 279
                self.areaParam()
                pass
            elif token in [100]:
                self.enterOuterAlt(localctx, 10)
                self.state = 280
                self.scrollParam()
                pass
            elif token in [105]:
                self.enterOuterAlt(localctx, 11)
                self.state = 281
                self.justParam()
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 12)
                self.state = 282
                self.formatParam()
                pass
            elif token in [108]:
                self.enterOuterAlt(localctx, 13)
                self.state = 283
                self.padcParam()
                pass
            elif token in [110]:
                self.enterOuterAlt(localctx, 14)
                self.state = 284
                self.outlineParam()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OutlineParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OUTLINE(self):
            return self.getToken(PanelParser.OUTLINE, 0)

        def LPAREN(self):
            return self.getToken(PanelParser.LPAREN, 0)

        def outlineValue(self):
            return self.getTypedRuleContext(PanelParser.OutlineValueContext,0)


        def RPAREN(self):
            return self.getToken(PanelParser.RPAREN, 0)

        def getRuleIndex(self):
            return PanelParser.RULE_outlineParam

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOutlineParam" ):
                listener.enterOutlineParam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOutlineParam" ):
                listener.exitOutlineParam(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOutlineParam" ):
                return visitor.visitOutlineParam(self)
            else:
                return visitor.visitChildren(self)




    def outlineParam(self):

        localctx = PanelParser.OutlineParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_outlineParam)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 287
            self.match(PanelParser.OUTLINE)
            self.state = 288
            self.match(PanelParser.LPAREN)
            self.state = 289
            self.outlineValue()
            self.state = 290
            self.match(PanelParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OutlineValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NONE(self):
            return self.getToken(PanelParser.NONE, 0)

        def BOX(self):
            return self.getToken(PanelParser.BOX, 0)

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(PanelParser.IDENTIFIER)
            else:
                return self.getToken(PanelParser.IDENTIFIER, i)

        def getRuleIndex(self):
            return PanelParser.RULE_outlineValue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOutlineValue" ):
                listener.enterOutlineValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOutlineValue" ):
                listener.exitOutlineValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOutlineValue" ):
                return visitor.visitOutlineValue(self)
            else:
                return visitor.visitChildren(self)




    def outlineValue(self):

        localctx = PanelParser.OutlineValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_outlineValue)
        self._la = 0 # Token type
        try:
            self.state = 299
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [111]:
                self.enterOuterAlt(localctx, 1)
                self.state = 292
                self.match(PanelParser.NONE)
                pass
            elif token in [112]:
                self.enterOuterAlt(localctx, 2)
                self.state = 293
                self.match(PanelParser.BOX)
                pass
            elif token in [119]:
                self.enterOuterAlt(localctx, 3)
                self.state = 295 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 294
                    self.match(PanelParser.IDENTIFIER)
                    self.state = 297 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==119):
                        break

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PadcParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PADC(self):
            return self.getToken(PanelParser.PADC, 0)

        def LPAREN(self):
            return self.getToken(PanelParser.LPAREN, 0)

        def padcValue(self):
            return self.getTypedRuleContext(PanelParser.PadcValueContext,0)


        def RPAREN(self):
            return self.getToken(PanelParser.RPAREN, 0)

        def getRuleIndex(self):
            return PanelParser.RULE_padcParam

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPadcParam" ):
                listener.enterPadcParam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPadcParam" ):
                listener.exitPadcParam(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPadcParam" ):
                return visitor.visitPadcParam(self)
            else:
                return visitor.visitChildren(self)




    def padcParam(self):

        localctx = PanelParser.PadcParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_padcParam)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 301
            self.match(PanelParser.PADC)
            self.state = 302
            self.match(PanelParser.LPAREN)
            self.state = 303
            self.padcValue()
            self.state = 304
            self.match(PanelParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PadcValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGERLITERAL(self):
            return self.getToken(PanelParser.INTEGERLITERAL, 0)

        def NULLS(self):
            return self.getToken(PanelParser.NULLS, 0)

        def USER(self):
            return self.getToken(PanelParser.USER, 0)

        def STRINGLITERAL(self):
            return self.getToken(PanelParser.STRINGLITERAL, 0)

        def getRuleIndex(self):
            return PanelParser.RULE_padcValue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPadcValue" ):
                listener.enterPadcValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPadcValue" ):
                listener.exitPadcValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPadcValue" ):
                return visitor.visitPadcValue(self)
            else:
                return visitor.visitChildren(self)




    def padcValue(self):

        localctx = PanelParser.PadcValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_padcValue)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 306
            _la = self._input.LA(1)
            if not(((((_la - 89)) & ~0x3f) == 0 and ((1 << (_la - 89)) & 2281701379) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class JustParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def JUST(self):
            return self.getToken(PanelParser.JUST, 0)

        def LPAREN(self):
            return self.getToken(PanelParser.LPAREN, 0)

        def justValue(self):
            return self.getTypedRuleContext(PanelParser.JustValueContext,0)


        def RPAREN(self):
            return self.getToken(PanelParser.RPAREN, 0)

        def getRuleIndex(self):
            return PanelParser.RULE_justParam

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJustParam" ):
                listener.enterJustParam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJustParam" ):
                listener.exitJustParam(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitJustParam" ):
                return visitor.visitJustParam(self)
            else:
                return visitor.visitChildren(self)




    def justParam(self):

        localctx = PanelParser.JustParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_justParam)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 308
            self.match(PanelParser.JUST)
            self.state = 309
            self.match(PanelParser.LPAREN)
            self.state = 310
            self.justValue()
            self.state = 311
            self.match(PanelParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class JustValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT(self):
            return self.getToken(PanelParser.LEFT, 0)

        def RIGHT(self):
            return self.getToken(PanelParser.RIGHT, 0)

        def AXIS(self):
            return self.getToken(PanelParser.AXIS, 0)

        def getRuleIndex(self):
            return PanelParser.RULE_justValue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJustValue" ):
                listener.enterJustValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJustValue" ):
                listener.exitJustValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitJustValue" ):
                return visitor.visitJustValue(self)
            else:
                return visitor.visitChildren(self)




    def justValue(self):

        localctx = PanelParser.JustValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_justValue)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 313
            _la = self._input.LA(1)
            if not(((((_la - 102)) & ~0x3f) == 0 and ((1 << (_la - 102)) & 7) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AreaParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AREA(self):
            return self.getToken(PanelParser.AREA, 0)

        def LPAREN(self):
            return self.getToken(PanelParser.LPAREN, 0)

        def areaValue(self):
            return self.getTypedRuleContext(PanelParser.AreaValueContext,0)


        def RPAREN(self):
            return self.getToken(PanelParser.RPAREN, 0)

        def getRuleIndex(self):
            return PanelParser.RULE_areaParam

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAreaParam" ):
                listener.enterAreaParam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAreaParam" ):
                listener.exitAreaParam(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAreaParam" ):
                return visitor.visitAreaParam(self)
            else:
                return visitor.visitChildren(self)




    def areaParam(self):

        localctx = PanelParser.AreaParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_areaParam)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 315
            self.match(PanelParser.AREA)
            self.state = 316
            self.match(PanelParser.LPAREN)
            self.state = 317
            self.areaValue()
            self.state = 318
            self.match(PanelParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AreaValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DYNAMIC(self):
            return self.getToken(PanelParser.DYNAMIC, 0)

        def GRAPHIC(self):
            return self.getToken(PanelParser.GRAPHIC, 0)

        def SCRL(self):
            return self.getToken(PanelParser.SCRL, 0)

        def getRuleIndex(self):
            return PanelParser.RULE_areaValue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAreaValue" ):
                listener.enterAreaValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAreaValue" ):
                listener.exitAreaValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAreaValue" ):
                return visitor.visitAreaValue(self)
            else:
                return visitor.visitChildren(self)




    def areaValue(self):

        localctx = PanelParser.AreaValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_areaValue)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 320
            _la = self._input.LA(1)
            if not(((((_la - 96)) & ~0x3f) == 0 and ((1 << (_la - 96)) & 13) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ScrollParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SCROLL(self):
            return self.getToken(PanelParser.SCROLL, 0)

        def LPAREN(self):
            return self.getToken(PanelParser.LPAREN, 0)

        def scrollValue(self):
            return self.getTypedRuleContext(PanelParser.ScrollValueContext,0)


        def RPAREN(self):
            return self.getToken(PanelParser.RPAREN, 0)

        def getRuleIndex(self):
            return PanelParser.RULE_scrollParam

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterScrollParam" ):
                listener.enterScrollParam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitScrollParam" ):
                listener.exitScrollParam(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScrollParam" ):
                return visitor.visitScrollParam(self)
            else:
                return visitor.visitChildren(self)




    def scrollParam(self):

        localctx = PanelParser.ScrollParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_scrollParam)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 322
            self.match(PanelParser.SCROLL)
            self.state = 323
            self.match(PanelParser.LPAREN)
            self.state = 324
            self.scrollValue()
            self.state = 325
            self.match(PanelParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ScrollValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ON(self):
            return self.getToken(PanelParser.ON, 0)

        def OFF(self):
            return self.getToken(PanelParser.OFF, 0)

        def getRuleIndex(self):
            return PanelParser.RULE_scrollValue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterScrollValue" ):
                listener.enterScrollValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitScrollValue" ):
                listener.exitScrollValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScrollValue" ):
                return visitor.visitScrollValue(self)
            else:
                return visitor.visitChildren(self)




    def scrollValue(self):

        localctx = PanelParser.ScrollValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_scrollValue)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 327
            _la = self._input.LA(1)
            if not(_la==54 or _la==55):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExtendParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EXTEND(self):
            return self.getToken(PanelParser.EXTEND, 0)

        def LPAREN(self):
            return self.getToken(PanelParser.LPAREN, 0)

        def extendValue(self):
            return self.getTypedRuleContext(PanelParser.ExtendValueContext,0)


        def RPAREN(self):
            return self.getToken(PanelParser.RPAREN, 0)

        def getRuleIndex(self):
            return PanelParser.RULE_extendParam

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExtendParam" ):
                listener.enterExtendParam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExtendParam" ):
                listener.exitExtendParam(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExtendParam" ):
                return visitor.visitExtendParam(self)
            else:
                return visitor.visitChildren(self)




    def extendParam(self):

        localctx = PanelParser.ExtendParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_extendParam)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 329
            self.match(PanelParser.EXTEND)
            self.state = 330
            self.match(PanelParser.LPAREN)
            self.state = 331
            self.extendValue()
            self.state = 332
            self.match(PanelParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExtendValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ON(self):
            return self.getToken(PanelParser.ON, 0)

        def OFF(self):
            return self.getToken(PanelParser.OFF, 0)

        def getRuleIndex(self):
            return PanelParser.RULE_extendValue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExtendValue" ):
                listener.enterExtendValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExtendValue" ):
                listener.exitExtendValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExtendValue" ):
                return visitor.visitExtendValue(self)
            else:
                return visitor.visitChildren(self)




    def extendValue(self):

        localctx = PanelParser.ExtendValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_extendValue)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 334
            _la = self._input.LA(1)
            if not(_la==54 or _la==55):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CapsParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CAPS(self):
            return self.getToken(PanelParser.CAPS, 0)

        def LPAREN(self):
            return self.getToken(PanelParser.LPAREN, 0)

        def capsValue(self):
            return self.getTypedRuleContext(PanelParser.CapsValueContext,0)


        def RPAREN(self):
            return self.getToken(PanelParser.RPAREN, 0)

        def getRuleIndex(self):
            return PanelParser.RULE_capsParam

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCapsParam" ):
                listener.enterCapsParam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCapsParam" ):
                listener.exitCapsParam(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCapsParam" ):
                return visitor.visitCapsParam(self)
            else:
                return visitor.visitChildren(self)




    def capsParam(self):

        localctx = PanelParser.CapsParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_capsParam)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 336
            self.match(PanelParser.CAPS)
            self.state = 337
            self.match(PanelParser.LPAREN)
            self.state = 338
            self.capsValue()
            self.state = 339
            self.match(PanelParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CapsValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ON(self):
            return self.getToken(PanelParser.ON, 0)

        def OFF(self):
            return self.getToken(PanelParser.OFF, 0)

        def IN(self):
            return self.getToken(PanelParser.IN, 0)

        def OUT(self):
            return self.getToken(PanelParser.OUT, 0)

        def getRuleIndex(self):
            return PanelParser.RULE_capsValue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCapsValue" ):
                listener.enterCapsValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCapsValue" ):
                listener.exitCapsValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCapsValue" ):
                return visitor.visitCapsValue(self)
            else:
                return visitor.visitChildren(self)




    def capsValue(self):

        localctx = PanelParser.CapsValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_capsValue)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 341
            _la = self._input.LA(1)
            if not(((((_la - 54)) & ~0x3f) == 0 and ((1 << (_la - 54)) & 1649267441667) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PadParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PAD(self):
            return self.getToken(PanelParser.PAD, 0)

        def LPAREN(self):
            return self.getToken(PanelParser.LPAREN, 0)

        def padValue(self):
            return self.getTypedRuleContext(PanelParser.PadValueContext,0)


        def RPAREN(self):
            return self.getToken(PanelParser.RPAREN, 0)

        def getRuleIndex(self):
            return PanelParser.RULE_padParam

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPadParam" ):
                listener.enterPadParam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPadParam" ):
                listener.exitPadParam(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPadParam" ):
                return visitor.visitPadParam(self)
            else:
                return visitor.visitChildren(self)




    def padParam(self):

        localctx = PanelParser.PadParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_padParam)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 343
            self.match(PanelParser.PAD)
            self.state = 344
            self.match(PanelParser.LPAREN)
            self.state = 345
            self.padValue()
            self.state = 346
            self.match(PanelParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PadValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGERLITERAL(self):
            return self.getToken(PanelParser.INTEGERLITERAL, 0)

        def NULLS(self):
            return self.getToken(PanelParser.NULLS, 0)

        def USER(self):
            return self.getToken(PanelParser.USER, 0)

        def STRINGLITERAL(self):
            return self.getToken(PanelParser.STRINGLITERAL, 0)

        def getRuleIndex(self):
            return PanelParser.RULE_padValue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPadValue" ):
                listener.enterPadValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPadValue" ):
                listener.exitPadValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPadValue" ):
                return visitor.visitPadValue(self)
            else:
                return visitor.visitChildren(self)




    def padValue(self):

        localctx = PanelParser.PadValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_padValue)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 348
            _la = self._input.LA(1)
            if not(((((_la - 89)) & ~0x3f) == 0 and ((1 << (_la - 89)) & 2281701379) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SkipParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SKIP_(self):
            return self.getToken(PanelParser.SKIP_, 0)

        def LPAREN(self):
            return self.getToken(PanelParser.LPAREN, 0)

        def skipValue(self):
            return self.getTypedRuleContext(PanelParser.SkipValueContext,0)


        def RPAREN(self):
            return self.getToken(PanelParser.RPAREN, 0)

        def getRuleIndex(self):
            return PanelParser.RULE_skipParam

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSkipParam" ):
                listener.enterSkipParam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSkipParam" ):
                listener.exitSkipParam(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSkipParam" ):
                return visitor.visitSkipParam(self)
            else:
                return visitor.visitChildren(self)




    def skipParam(self):

        localctx = PanelParser.SkipParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_skipParam)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 350
            self.match(PanelParser.SKIP_)
            self.state = 351
            self.match(PanelParser.LPAREN)
            self.state = 352
            self.skipValue()
            self.state = 353
            self.match(PanelParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SkipValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ON(self):
            return self.getToken(PanelParser.ON, 0)

        def OFF(self):
            return self.getToken(PanelParser.OFF, 0)

        def getRuleIndex(self):
            return PanelParser.RULE_skipValue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSkipValue" ):
                listener.enterSkipValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSkipValue" ):
                listener.exitSkipValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSkipValue" ):
                return visitor.visitSkipValue(self)
            else:
                return visitor.visitChildren(self)




    def skipValue(self):

        localctx = PanelParser.SkipValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_skipValue)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 355
            _la = self._input.LA(1)
            if not(_la==54 or _la==55):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(PanelParser.TYPE, 0)

        def LPAREN(self):
            return self.getToken(PanelParser.LPAREN, 0)

        def value(self):
            return self.getTypedRuleContext(PanelParser.ValueContext,0)


        def RPAREN(self):
            return self.getToken(PanelParser.RPAREN, 0)

        def getRuleIndex(self):
            return PanelParser.RULE_typeParam

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeParam" ):
                listener.enterTypeParam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeParam" ):
                listener.exitTypeParam(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeParam" ):
                return visitor.visitTypeParam(self)
            else:
                return visitor.visitChildren(self)




    def typeParam(self):

        localctx = PanelParser.TypeParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_typeParam)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 357
            self.match(PanelParser.TYPE)
            self.state = 358
            self.match(PanelParser.LPAREN)
            self.state = 359
            self.value()
            self.state = 360
            self.match(PanelParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IntensParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTENS(self):
            return self.getToken(PanelParser.INTENS, 0)

        def LPAREN(self):
            return self.getToken(PanelParser.LPAREN, 0)

        def intensValue(self):
            return self.getTypedRuleContext(PanelParser.IntensValueContext,0)


        def RPAREN(self):
            return self.getToken(PanelParser.RPAREN, 0)

        def getRuleIndex(self):
            return PanelParser.RULE_intensParam

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIntensParam" ):
                listener.enterIntensParam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntensParam" ):
                listener.exitIntensParam(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntensParam" ):
                return visitor.visitIntensParam(self)
            else:
                return visitor.visitChildren(self)




    def intensParam(self):

        localctx = PanelParser.IntensParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_intensParam)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 362
            self.match(PanelParser.INTENS)
            self.state = 363
            self.match(PanelParser.LPAREN)
            self.state = 364
            self.intensValue()
            self.state = 365
            self.match(PanelParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IntensValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def HIGH(self):
            return self.getToken(PanelParser.HIGH, 0)

        def LOW(self):
            return self.getToken(PanelParser.LOW, 0)

        def NON(self):
            return self.getToken(PanelParser.NON, 0)

        def getRuleIndex(self):
            return PanelParser.RULE_intensValue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIntensValue" ):
                listener.enterIntensValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntensValue" ):
                listener.exitIntensValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntensValue" ):
                return visitor.visitIntensValue(self)
            else:
                return visitor.visitChildren(self)




    def intensValue(self):

        localctx = PanelParser.IntensValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_intensValue)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 367
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 51808043008) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ColorParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLOR(self):
            return self.getToken(PanelParser.COLOR, 0)

        def LPAREN(self):
            return self.getToken(PanelParser.LPAREN, 0)

        def value(self):
            return self.getTypedRuleContext(PanelParser.ValueContext,0)


        def RPAREN(self):
            return self.getToken(PanelParser.RPAREN, 0)

        def getRuleIndex(self):
            return PanelParser.RULE_colorParam

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColorParam" ):
                listener.enterColorParam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColorParam" ):
                listener.exitColorParam(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitColorParam" ):
                return visitor.visitColorParam(self)
            else:
                return visitor.visitChildren(self)




    def colorParam(self):

        localctx = PanelParser.ColorParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_colorParam)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 369
            self.match(PanelParser.COLOR)
            self.state = 370
            self.match(PanelParser.LPAREN)
            self.state = 371
            self.value()
            self.state = 372
            self.match(PanelParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HiliteParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def HILITE(self):
            return self.getToken(PanelParser.HILITE, 0)

        def LPAREN(self):
            return self.getToken(PanelParser.LPAREN, 0)

        def value(self):
            return self.getTypedRuleContext(PanelParser.ValueContext,0)


        def RPAREN(self):
            return self.getToken(PanelParser.RPAREN, 0)

        def getRuleIndex(self):
            return PanelParser.RULE_hiliteParam

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHiliteParam" ):
                listener.enterHiliteParam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHiliteParam" ):
                listener.exitHiliteParam(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHiliteParam" ):
                return visitor.visitHiliteParam(self)
            else:
                return visitor.visitChildren(self)




    def hiliteParam(self):

        localctx = PanelParser.HiliteParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_hiliteParam)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 374
            self.match(PanelParser.HILITE)
            self.state = 375
            self.match(PanelParser.LPAREN)
            self.state = 376
            self.value()
            self.state = 377
            self.match(PanelParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttrCharContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SSLASH(self):
            return self.getToken(PanelParser.SSLASH, 0)

        def JP_MYSTERYCHAR(self):
            return self.getToken(PanelParser.JP_MYSTERYCHAR, 0)

        def AMPCHAR(self):
            return self.getToken(PanelParser.AMPCHAR, 0)

        def EXCLAIMCHAR(self):
            return self.getToken(PanelParser.EXCLAIMCHAR, 0)

        def DOLLARCHAR(self):
            return self.getToken(PanelParser.DOLLARCHAR, 0)

        def JP_CHAR(self):
            return self.getToken(PanelParser.JP_CHAR, 0)

        def PLUSCHAR(self):
            return self.getToken(PanelParser.PLUSCHAR, 0)

        def HASHCHAR(self):
            return self.getToken(PanelParser.HASHCHAR, 0)

        def LBRACKET(self):
            return self.getToken(PanelParser.LBRACKET, 0)

        def RBRACKET(self):
            return self.getToken(PanelParser.RBRACKET, 0)

        def DOUBLEQUOTE(self):
            return self.getToken(PanelParser.DOUBLEQUOTE, 0)

        def UNDERSCORE(self):
            return self.getToken(PanelParser.UNDERSCORE, 0)

        def ASTERISK(self):
            return self.getToken(PanelParser.ASTERISK, 0)

        def SLASH(self):
            return self.getToken(PanelParser.SLASH, 0)

        def PIPECHAR(self):
            return self.getToken(PanelParser.PIPECHAR, 0)

        def SINGLEQUOTE(self):
            return self.getToken(PanelParser.SINGLEQUOTE, 0)

        def GREATERTHAN(self):
            return self.getToken(PanelParser.GREATERTHAN, 0)

        def LESSTHAN(self):
            return self.getToken(PanelParser.LESSTHAN, 0)

        def CARET(self):
            return self.getToken(PanelParser.CARET, 0)

        def getRuleIndex(self):
            return PanelParser.RULE_attrChar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttrChar" ):
                listener.enterAttrChar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttrChar" ):
                listener.exitAttrChar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttrChar" ):
                return visitor.visitAttrChar(self)
            else:
                return visitor.visitChildren(self)




    def attrChar(self):

        localctx = PanelParser.AttrCharContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_attrChar)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 379
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8387064) != 0) or _la==121):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodySectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RPAREN(self):
            return self.getToken(PanelParser.RPAREN, 0)

        def BODY(self):
            return self.getToken(PanelParser.BODY, 0)

        def bodyParam(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PanelParser.BodyParamContext)
            else:
                return self.getTypedRuleContext(PanelParser.BodyParamContext,i)


        def getRuleIndex(self):
            return PanelParser.RULE_bodySection

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBodySection" ):
                listener.enterBodySection(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBodySection" ):
                listener.exitBodySection(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBodySection" ):
                return visitor.visitBodySection(self)
            else:
                return visitor.visitChildren(self)




    def bodySection(self):

        localctx = PanelParser.BodySectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_bodySection)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 381
            self.match(PanelParser.RPAREN)
            self.state = 382
            self.match(PanelParser.BODY)
            self.state = 386
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 824835047424) != 0) or _la==95:
                self.state = 383
                self.bodyParam()
                self.state = 388
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def kanaParam(self):
            return self.getTypedRuleContext(PanelParser.KanaParamContext,0)


        def windowParam(self):
            return self.getTypedRuleContext(PanelParser.WindowParamContext,0)


        def defaultParam(self):
            return self.getTypedRuleContext(PanelParser.DefaultParamContext,0)


        def formatParam(self):
            return self.getTypedRuleContext(PanelParser.FormatParamContext,0)


        def widthPara(self):
            return self.getTypedRuleContext(PanelParser.WidthParaContext,0)


        def getRuleIndex(self):
            return PanelParser.RULE_bodyParam

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBodyParam" ):
                listener.enterBodyParam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBodyParam" ):
                listener.exitBodyParam(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBodyParam" ):
                return visitor.visitBodyParam(self)
            else:
                return visitor.visitChildren(self)




    def bodyParam(self):

        localctx = PanelParser.BodyParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_bodyParam)
        try:
            self.state = 394
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [38]:
                self.enterOuterAlt(localctx, 1)
                self.state = 389
                self.kanaParam()
                pass
            elif token in [39]:
                self.enterOuterAlt(localctx, 2)
                self.state = 390
                self.windowParam()
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 3)
                self.state = 391
                self.defaultParam()
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 4)
                self.state = 392
                self.formatParam()
                pass
            elif token in [95]:
                self.enterOuterAlt(localctx, 5)
                self.state = 393
                self.widthPara()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class KanaParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KANA(self):
            return self.getToken(PanelParser.KANA, 0)

        def getRuleIndex(self):
            return PanelParser.RULE_kanaParam

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKanaParam" ):
                listener.enterKanaParam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKanaParam" ):
                listener.exitKanaParam(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKanaParam" ):
                return visitor.visitKanaParam(self)
            else:
                return visitor.visitChildren(self)




    def kanaParam(self):

        localctx = PanelParser.KanaParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_kanaParam)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 396
            self.match(PanelParser.KANA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WindowParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WINDOW(self):
            return self.getToken(PanelParser.WINDOW, 0)

        def LPAREN(self):
            return self.getToken(PanelParser.LPAREN, 0)

        def width(self):
            return self.getTypedRuleContext(PanelParser.WidthContext,0)


        def length(self):
            return self.getTypedRuleContext(PanelParser.LengthContext,0)


        def RPAREN(self):
            return self.getToken(PanelParser.RPAREN, 0)

        def COMMACHAR(self):
            return self.getToken(PanelParser.COMMACHAR, 0)

        def getRuleIndex(self):
            return PanelParser.RULE_windowParam

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWindowParam" ):
                listener.enterWindowParam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWindowParam" ):
                listener.exitWindowParam(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWindowParam" ):
                return visitor.visitWindowParam(self)
            else:
                return visitor.visitChildren(self)




    def windowParam(self):

        localctx = PanelParser.WindowParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_windowParam)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 398
            self.match(PanelParser.WINDOW)
            self.state = 399
            self.match(PanelParser.LPAREN)
            self.state = 400
            self.width()
            self.state = 402
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 401
                self.match(PanelParser.COMMACHAR)


            self.state = 404
            self.length()
            self.state = 405
            self.match(PanelParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WidthContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGERLITERAL(self):
            return self.getToken(PanelParser.INTEGERLITERAL, 0)

        def getRuleIndex(self):
            return PanelParser.RULE_width

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWidth" ):
                listener.enterWidth(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWidth" ):
                listener.exitWidth(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWidth" ):
                return visitor.visitWidth(self)
            else:
                return visitor.visitChildren(self)




    def width(self):

        localctx = PanelParser.WidthContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_width)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 407
            self.match(PanelParser.INTEGERLITERAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LengthContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGERLITERAL(self):
            return self.getToken(PanelParser.INTEGERLITERAL, 0)

        def getRuleIndex(self):
            return PanelParser.RULE_length

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLength" ):
                listener.enterLength(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLength" ):
                listener.exitLength(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLength" ):
                return visitor.visitLength(self)
            else:
                return visitor.visitChildren(self)




    def length(self):

        localctx = PanelParser.LengthContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_length)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 409
            self.match(PanelParser.INTEGERLITERAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WidthParaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WIDTH(self):
            return self.getToken(PanelParser.WIDTH, 0)

        def LPAREN(self):
            return self.getToken(PanelParser.LPAREN, 0)

        def width(self):
            return self.getTypedRuleContext(PanelParser.WidthContext,0)


        def RPAREN(self):
            return self.getToken(PanelParser.RPAREN, 0)

        def getRuleIndex(self):
            return PanelParser.RULE_widthPara

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWidthPara" ):
                listener.enterWidthPara(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWidthPara" ):
                listener.exitWidthPara(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWidthPara" ):
                return visitor.visitWidthPara(self)
            else:
                return visitor.visitChildren(self)




    def widthPara(self):

        localctx = PanelParser.WidthParaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_widthPara)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 411
            self.match(PanelParser.WIDTH)
            self.state = 412
            self.match(PanelParser.LPAREN)
            self.state = 413
            self.width()
            self.state = 414
            self.match(PanelParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignStatement(self):
            return self.getTypedRuleContext(PanelParser.AssignStatementContext,0)


        def vputStatement(self):
            return self.getTypedRuleContext(PanelParser.VputStatementContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(PanelParser.IfStatementContext,0)


        def verStatement(self):
            return self.getTypedRuleContext(PanelParser.VerStatementContext,0)


        def vgetStatement(self):
            return self.getTypedRuleContext(PanelParser.VgetStatementContext,0)


        def refreshStatement(self):
            return self.getTypedRuleContext(PanelParser.RefreshStatementContext,0)


        def getRuleIndex(self):
            return PanelParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = PanelParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_statement)
        try:
            self.state = 422
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [119]:
                self.enterOuterAlt(localctx, 1)
                self.state = 416
                self.assignStatement()
                pass
            elif token in [42]:
                self.enterOuterAlt(localctx, 2)
                self.state = 417
                self.vputStatement()
                pass
            elif token in [47]:
                self.enterOuterAlt(localctx, 3)
                self.state = 418
                self.ifStatement()
                pass
            elif token in [56]:
                self.enterOuterAlt(localctx, 4)
                self.state = 419
                self.verStatement()
                pass
            elif token in [41]:
                self.enterOuterAlt(localctx, 5)
                self.state = 420
                self.vgetStatement()
                pass
            elif token in [109]:
                self.enterOuterAlt(localctx, 6)
                self.state = 421
                self.refreshStatement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RefreshStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def REFRESH(self):
            return self.getToken(PanelParser.REFRESH, 0)

        def LPAREN(self):
            return self.getToken(PanelParser.LPAREN, 0)

        def variable(self):
            return self.getTypedRuleContext(PanelParser.VariableContext,0)


        def RPAREN(self):
            return self.getToken(PanelParser.RPAREN, 0)

        def getRuleIndex(self):
            return PanelParser.RULE_refreshStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRefreshStatement" ):
                listener.enterRefreshStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRefreshStatement" ):
                listener.exitRefreshStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRefreshStatement" ):
                return visitor.visitRefreshStatement(self)
            else:
                return visitor.visitChildren(self)




    def refreshStatement(self):

        localctx = PanelParser.RefreshStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_refreshStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 424
            self.match(PanelParser.REFRESH)
            self.state = 425
            self.match(PanelParser.LPAREN)
            self.state = 426
            self.variable()
            self.state = 427
            self.match(PanelParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(PanelParser.IF, 0)

        def condition(self):
            return self.getTypedRuleContext(PanelParser.ConditionContext,0)


        def thenIf(self):
            return self.getTypedRuleContext(PanelParser.ThenIfContext,0)


        def elseIf(self):
            return self.getTypedRuleContext(PanelParser.ElseIfContext,0)


        def getRuleIndex(self):
            return PanelParser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = PanelParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_ifStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 429
            self.match(PanelParser.IF)
            self.state = 430
            self.condition()
            self.state = 431
            self.thenIf()
            self.state = 433
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.state = 432
                self.elseIf()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def combinableCondition(self):
            return self.getTypedRuleContext(PanelParser.CombinableConditionContext,0)


        def andOrCondition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PanelParser.AndOrConditionContext)
            else:
                return self.getTypedRuleContext(PanelParser.AndOrConditionContext,i)


        def getRuleIndex(self):
            return PanelParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)




    def condition(self):

        localctx = PanelParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_condition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 435
            self.combinableCondition()
            self.state = 439
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==48 or _la==49:
                self.state = 436
                self.andOrCondition()
                self.state = 441
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AndOrConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AND(self):
            return self.getToken(PanelParser.AND, 0)

        def OR(self):
            return self.getToken(PanelParser.OR, 0)

        def combinableCondition(self):
            return self.getTypedRuleContext(PanelParser.CombinableConditionContext,0)


        def INTEGERLITERAL(self):
            return self.getToken(PanelParser.INTEGERLITERAL, 0)

        def getRuleIndex(self):
            return PanelParser.RULE_andOrCondition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAndOrCondition" ):
                listener.enterAndOrCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAndOrCondition" ):
                listener.exitAndOrCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAndOrCondition" ):
                return visitor.visitAndOrCondition(self)
            else:
                return visitor.visitChildren(self)




    def andOrCondition(self):

        localctx = PanelParser.AndOrConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_andOrCondition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 442
            _la = self._input.LA(1)
            if not(_la==48 or _la==49):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 445
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.state = 443
                self.combinableCondition()
                pass

            elif la_ == 2:
                self.state = 444
                self.match(PanelParser.INTEGERLITERAL)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CombinableConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simpleCondition(self):
            return self.getTypedRuleContext(PanelParser.SimpleConditionContext,0)


        def NOT(self):
            return self.getToken(PanelParser.NOT, 0)

        def getRuleIndex(self):
            return PanelParser.RULE_combinableCondition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCombinableCondition" ):
                listener.enterCombinableCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCombinableCondition" ):
                listener.exitCombinableCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCombinableCondition" ):
                return visitor.visitCombinableCondition(self)
            else:
                return visitor.visitChildren(self)




    def combinableCondition(self):

        localctx = PanelParser.CombinableConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_combinableCondition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 448
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==50:
                self.state = 447
                self.match(PanelParser.NOT)


            self.state = 450
            self.simpleCondition()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SimpleConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(PanelParser.LPAREN, 0)

        def condition(self):
            return self.getTypedRuleContext(PanelParser.ConditionContext,0)


        def RPAREN(self):
            return self.getToken(PanelParser.RPAREN, 0)

        def relationCondition(self):
            return self.getTypedRuleContext(PanelParser.RelationConditionContext,0)


        def getRuleIndex(self):
            return PanelParser.RULE_simpleCondition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimpleCondition" ):
                listener.enterSimpleCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimpleCondition" ):
                listener.exitSimpleCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimpleCondition" ):
                return visitor.visitSimpleCondition(self)
            else:
                return visitor.visitChildren(self)




    def simpleCondition(self):

        localctx = PanelParser.SimpleConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_simpleCondition)
        try:
            self.state = 457
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 452
                self.match(PanelParser.LPAREN)
                self.state = 453
                self.condition()
                self.state = 454
                self.match(PanelParser.RPAREN)
                pass
            elif token in [11, 36, 37, 45, 52, 80, 90, 101, 113, 116, 119, 120]:
                self.enterOuterAlt(localctx, 2)
                self.state = 456
                self.relationCondition()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relationArithmeticComparison(self):
            return self.getTypedRuleContext(PanelParser.RelationArithmeticComparisonContext,0)


        def getRuleIndex(self):
            return PanelParser.RULE_relationCondition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelationCondition" ):
                listener.enterRelationCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelationCondition" ):
                listener.exitRelationCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelationCondition" ):
                return visitor.visitRelationCondition(self)
            else:
                return visitor.visitChildren(self)




    def relationCondition(self):

        localctx = PanelParser.RelationConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_relationCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 459
            self.relationArithmeticComparison()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationArithmeticComparisonContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arithmeticExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PanelParser.ArithmeticExpressionContext)
            else:
                return self.getTypedRuleContext(PanelParser.ArithmeticExpressionContext,i)


        def relationalOperator(self):
            return self.getTypedRuleContext(PanelParser.RelationalOperatorContext,0)


        def COMMACHAR(self, i:int=None):
            if i is None:
                return self.getTokens(PanelParser.COMMACHAR)
            else:
                return self.getToken(PanelParser.COMMACHAR, i)

        def getRuleIndex(self):
            return PanelParser.RULE_relationArithmeticComparison

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelationArithmeticComparison" ):
                listener.enterRelationArithmeticComparison(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelationArithmeticComparison" ):
                listener.exitRelationArithmeticComparison(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelationArithmeticComparison" ):
                return visitor.visitRelationArithmeticComparison(self)
            else:
                return visitor.visitChildren(self)




    def relationArithmeticComparison(self):

        localctx = PanelParser.RelationArithmeticComparisonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_relationArithmeticComparison)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 464
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.state = 461
                self.arithmeticExpression()
                self.state = 462
                self.relationalOperator()


            self.state = 466
            self.arithmeticExpression()
            self.state = 471
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 467
                self.match(PanelParser.COMMACHAR)
                self.state = 468
                self.arithmeticExpression()
                self.state = 473
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArithmeticExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self):
            return self.getTypedRuleContext(PanelParser.ValueContext,0)


        def getRuleIndex(self):
            return PanelParser.RULE_arithmeticExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArithmeticExpression" ):
                listener.enterArithmeticExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArithmeticExpression" ):
                listener.exitArithmeticExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArithmeticExpression" ):
                return visitor.visitArithmeticExpression(self)
            else:
                return visitor.visitChildren(self)




    def arithmeticExpression(self):

        localctx = PanelParser.ArithmeticExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_arithmeticExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 474
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationalOperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUALCHAR(self):
            return self.getToken(PanelParser.EQUALCHAR, 0)

        def getRuleIndex(self):
            return PanelParser.RULE_relationalOperator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelationalOperator" ):
                listener.enterRelationalOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelationalOperator" ):
                listener.exitRelationalOperator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelationalOperator" ):
                return visitor.visitRelationalOperator(self)
            else:
                return visitor.visitChildren(self)




    def relationalOperator(self):

        localctx = PanelParser.RelationalOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_relationalOperator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 476
            self.match(PanelParser.EQUALCHAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ThenIfContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(PanelParser.StatementContext,0)


        def verStatement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PanelParser.VerStatementContext)
            else:
                return self.getTypedRuleContext(PanelParser.VerStatementContext,i)


        def getRuleIndex(self):
            return PanelParser.RULE_thenIf

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterThenIf" ):
                listener.enterThenIf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitThenIf" ):
                listener.exitThenIf(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitThenIf" ):
                return visitor.visitThenIf(self)
            else:
                return visitor.visitChildren(self)




    def thenIf(self):

        localctx = PanelParser.ThenIfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_thenIf)
        try:
            self.state = 484
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 478
                self.statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 480 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 479
                        self.verStatement()

                    else:
                        raise NoViableAltException(self)
                    self.state = 482 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VerStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VER(self):
            return self.getToken(PanelParser.VER, 0)

        def LPAREN(self):
            return self.getToken(PanelParser.LPAREN, 0)

        def variable(self):
            return self.getTypedRuleContext(PanelParser.VariableContext,0)


        def COMMACHAR(self, i:int=None):
            if i is None:
                return self.getTokens(PanelParser.COMMACHAR)
            else:
                return self.getToken(PanelParser.COMMACHAR, i)

        def verCriteria(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PanelParser.VerCriteriaContext)
            else:
                return self.getTypedRuleContext(PanelParser.VerCriteriaContext,i)


        def RPAREN(self):
            return self.getToken(PanelParser.RPAREN, 0)

        def verMsg(self):
            return self.getTypedRuleContext(PanelParser.VerMsgContext,0)


        def getRuleIndex(self):
            return PanelParser.RULE_verStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVerStatement" ):
                listener.enterVerStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVerStatement" ):
                listener.exitVerStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVerStatement" ):
                return visitor.visitVerStatement(self)
            else:
                return visitor.visitChildren(self)




    def verStatement(self):

        localctx = PanelParser.VerStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_verStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 486
            self.match(PanelParser.VER)
            self.state = 487
            self.match(PanelParser.LPAREN)
            self.state = 488
            self.variable()
            self.state = 489
            self.match(PanelParser.COMMACHAR)
            self.state = 490
            self.verCriteria()
            self.state = 495
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 491
                    self.match(PanelParser.COMMACHAR)
                    self.state = 492
                    self.verCriteria() 
                self.state = 497
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

            self.state = 500
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 498
                self.match(PanelParser.COMMACHAR)
                self.state = 499
                self.verMsg()


            self.state = 502
            self.match(PanelParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VerMsgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MSG(self):
            return self.getToken(PanelParser.MSG, 0)

        def EQUALCHAR(self):
            return self.getToken(PanelParser.EQUALCHAR, 0)

        def value(self):
            return self.getTypedRuleContext(PanelParser.ValueContext,0)


        def getRuleIndex(self):
            return PanelParser.RULE_verMsg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVerMsg" ):
                listener.enterVerMsg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVerMsg" ):
                listener.exitVerMsg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVerMsg" ):
                return visitor.visitVerMsg(self)
            else:
                return visitor.visitChildren(self)




    def verMsg(self):

        localctx = PanelParser.VerMsgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_verMsg)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 504
            self.match(PanelParser.MSG)
            self.state = 505
            self.match(PanelParser.EQUALCHAR)
            self.state = 506
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VerCriteriaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simpleCriteria(self):
            return self.getTypedRuleContext(PanelParser.SimpleCriteriaContext,0)


        def lengthCriteria(self):
            return self.getTypedRuleContext(PanelParser.LengthCriteriaContext,0)


        def listCriteria(self):
            return self.getTypedRuleContext(PanelParser.ListCriteriaContext,0)


        def pictCriteria(self):
            return self.getTypedRuleContext(PanelParser.PictCriteriaContext,0)


        def rangeCriteria(self):
            return self.getTypedRuleContext(PanelParser.RangeCriteriaContext,0)


        def getRuleIndex(self):
            return PanelParser.RULE_verCriteria

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVerCriteria" ):
                listener.enterVerCriteria(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVerCriteria" ):
                listener.exitVerCriteria(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVerCriteria" ):
                return visitor.visitVerCriteria(self)
            else:
                return visitor.visitChildren(self)




    def verCriteria(self):

        localctx = PanelParser.VerCriteriaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_verCriteria)
        try:
            self.state = 513
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [29, 30, 31, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 80, 81, 82, 86, 87]:
                self.enterOuterAlt(localctx, 1)
                self.state = 508
                self.simpleCriteria()
                pass
            elif token in [75]:
                self.enterOuterAlt(localctx, 2)
                self.state = 509
                self.lengthCriteria()
                pass
            elif token in [76, 77, 78, 79]:
                self.enterOuterAlt(localctx, 3)
                self.state = 510
                self.listCriteria()
                pass
            elif token in [83, 84]:
                self.enterOuterAlt(localctx, 4)
                self.state = 511
                self.pictCriteria()
                pass
            elif token in [85]:
                self.enterOuterAlt(localctx, 5)
                self.state = 512
                self.rangeCriteria()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SimpleCriteriaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NONBLANK(self):
            return self.getToken(PanelParser.NONBLANK, 0)

        def ALPHA(self):
            return self.getToken(PanelParser.ALPHA, 0)

        def ALPHAB(self):
            return self.getToken(PanelParser.ALPHAB, 0)

        def BIT(self):
            return self.getToken(PanelParser.BIT, 0)

        def DBCS(self):
            return self.getToken(PanelParser.DBCS, 0)

        def DSNAME(self):
            return self.getToken(PanelParser.DSNAME, 0)

        def DSNAMEF(self):
            return self.getToken(PanelParser.DSNAMEF, 0)

        def DSNAMEFM(self):
            return self.getToken(PanelParser.DSNAMEFM, 0)

        def DSNAMEPQ(self):
            return self.getToken(PanelParser.DSNAMEPQ, 0)

        def DSNAMEQ(self):
            return self.getToken(PanelParser.DSNAMEQ, 0)

        def EBCDIC(self):
            return self.getToken(PanelParser.EBCDIC, 0)

        def ENUM(self):
            return self.getToken(PanelParser.ENUM, 0)

        def FILEID(self):
            return self.getToken(PanelParser.FILEID, 0)

        def HEX(self):
            return self.getToken(PanelParser.HEX, 0)

        def IDATE(self):
            return self.getToken(PanelParser.IDATE, 0)

        def INCLUDE(self):
            return self.getToken(PanelParser.INCLUDE, 0)

        def IPADDR4(self):
            return self.getToken(PanelParser.IPADDR4, 0)

        def ITIME(self):
            return self.getToken(PanelParser.ITIME, 0)

        def JDATE(self):
            return self.getToken(PanelParser.JDATE, 0)

        def JSTD(self):
            return self.getToken(PanelParser.JSTD, 0)

        def MIX(self):
            return self.getToken(PanelParser.MIX, 0)

        def NAME(self):
            return self.getToken(PanelParser.NAME, 0)

        def NAMEF(self):
            return self.getToken(PanelParser.NAMEF, 0)

        def NUM(self):
            return self.getToken(PanelParser.NUM, 0)

        def STDDATE(self):
            return self.getToken(PanelParser.STDDATE, 0)

        def STDTIME(self):
            return self.getToken(PanelParser.STDTIME, 0)

        def getRuleIndex(self):
            return PanelParser.RULE_simpleCriteria

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimpleCriteria" ):
                listener.enterSimpleCriteria(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimpleCriteria" ):
                listener.exitSimpleCriteria(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimpleCriteria" ):
                return visitor.visitSimpleCriteria(self)
            else:
                return visitor.visitChildren(self)




    def simpleCriteria(self):

        localctx = PanelParser.SimpleCriteriaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_simpleCriteria)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 515
            _la = self._input.LA(1)
            if not(((((_la - 29)) & ~0x3f) == 0 and ((1 << (_la - 29)) & 448178531399106567) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LengthCriteriaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEN(self):
            return self.getToken(PanelParser.LEN, 0)

        def COMMACHAR(self, i:int=None):
            if i is None:
                return self.getTokens(PanelParser.COMMACHAR)
            else:
                return self.getToken(PanelParser.COMMACHAR, i)

        def relationalOperator(self):
            return self.getTypedRuleContext(PanelParser.RelationalOperatorContext,0)


        def expectedLength(self):
            return self.getTypedRuleContext(PanelParser.ExpectedLengthContext,0)


        def getRuleIndex(self):
            return PanelParser.RULE_lengthCriteria

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLengthCriteria" ):
                listener.enterLengthCriteria(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLengthCriteria" ):
                listener.exitLengthCriteria(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLengthCriteria" ):
                return visitor.visitLengthCriteria(self)
            else:
                return visitor.visitChildren(self)




    def lengthCriteria(self):

        localctx = PanelParser.LengthCriteriaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_lengthCriteria)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 517
            self.match(PanelParser.LEN)
            self.state = 518
            self.match(PanelParser.COMMACHAR)
            self.state = 519
            self.relationalOperator()
            self.state = 520
            self.match(PanelParser.COMMACHAR)
            self.state = 521
            self.expectedLength()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListCriteriaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LIST(self):
            return self.getToken(PanelParser.LIST, 0)

        def COMMACHAR(self, i:int=None):
            if i is None:
                return self.getTokens(PanelParser.COMMACHAR)
            else:
                return self.getToken(PanelParser.COMMACHAR, i)

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PanelParser.ValueContext)
            else:
                return self.getTypedRuleContext(PanelParser.ValueContext,i)


        def LISTV(self):
            return self.getToken(PanelParser.LISTV, 0)

        def varlist(self):
            return self.getTypedRuleContext(PanelParser.VarlistContext,0)


        def LISTVX(self):
            return self.getToken(PanelParser.LISTVX, 0)

        def LISTX(self):
            return self.getToken(PanelParser.LISTX, 0)

        def getRuleIndex(self):
            return PanelParser.RULE_listCriteria

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListCriteria" ):
                listener.enterListCriteria(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListCriteria" ):
                listener.exitListCriteria(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListCriteria" ):
                return visitor.visitListCriteria(self)
            else:
                return visitor.visitChildren(self)




    def listCriteria(self):

        localctx = PanelParser.ListCriteriaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_listCriteria)
        try:
            self.state = 542
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [76]:
                self.enterOuterAlt(localctx, 1)
                self.state = 523
                self.match(PanelParser.LIST)
                self.state = 524
                self.match(PanelParser.COMMACHAR)
                self.state = 525
                self.value()
                self.state = 530
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 526
                        self.match(PanelParser.COMMACHAR)
                        self.state = 527
                        self.value() 
                    self.state = 532
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

                pass
            elif token in [77]:
                self.enterOuterAlt(localctx, 2)
                self.state = 533
                self.match(PanelParser.LISTV)
                self.state = 534
                self.match(PanelParser.COMMACHAR)
                self.state = 535
                self.varlist()
                pass
            elif token in [78]:
                self.enterOuterAlt(localctx, 3)
                self.state = 536
                self.match(PanelParser.LISTVX)
                self.state = 537
                self.match(PanelParser.COMMACHAR)
                self.state = 538
                self.varlist()
                pass
            elif token in [79]:
                self.enterOuterAlt(localctx, 4)
                self.state = 539
                self.match(PanelParser.LISTX)
                self.state = 540
                self.match(PanelParser.COMMACHAR)
                self.state = 541
                self.value()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PictCriteriaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PICT(self):
            return self.getToken(PanelParser.PICT, 0)

        def COMMACHAR(self, i:int=None):
            if i is None:
                return self.getTokens(PanelParser.COMMACHAR)
            else:
                return self.getToken(PanelParser.COMMACHAR, i)

        def picValue(self):
            return self.getTypedRuleContext(PanelParser.PicValueContext,0)


        def PICTCN(self):
            return self.getToken(PanelParser.PICTCN, 0)

        def maskCharacter(self):
            return self.getTypedRuleContext(PanelParser.MaskCharacterContext,0)


        def fieldMask(self):
            return self.getTypedRuleContext(PanelParser.FieldMaskContext,0)


        def stringValue(self):
            return self.getTypedRuleContext(PanelParser.StringValueContext,0)


        def getRuleIndex(self):
            return PanelParser.RULE_pictCriteria

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPictCriteria" ):
                listener.enterPictCriteria(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPictCriteria" ):
                listener.exitPictCriteria(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPictCriteria" ):
                return visitor.visitPictCriteria(self)
            else:
                return visitor.visitChildren(self)




    def pictCriteria(self):

        localctx = PanelParser.PictCriteriaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_pictCriteria)
        try:
            self.state = 555
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [83]:
                self.enterOuterAlt(localctx, 1)
                self.state = 544
                self.match(PanelParser.PICT)
                self.state = 545
                self.match(PanelParser.COMMACHAR)
                self.state = 546
                self.picValue()
                pass
            elif token in [84]:
                self.enterOuterAlt(localctx, 2)
                self.state = 547
                self.match(PanelParser.PICTCN)
                self.state = 548
                self.match(PanelParser.COMMACHAR)
                self.state = 549
                self.maskCharacter()
                self.state = 550
                self.match(PanelParser.COMMACHAR)
                self.state = 551
                self.fieldMask()
                self.state = 552
                self.match(PanelParser.COMMACHAR)
                self.state = 553
                self.stringValue()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PicValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(PanelParser.IDENTIFIER, 0)

        def STRINGLITERAL(self):
            return self.getToken(PanelParser.STRINGLITERAL, 0)

        def getRuleIndex(self):
            return PanelParser.RULE_picValue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPicValue" ):
                listener.enterPicValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPicValue" ):
                listener.exitPicValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPicValue" ):
                return visitor.visitPicValue(self)
            else:
                return visitor.visitChildren(self)




    def picValue(self):

        localctx = PanelParser.PicValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_picValue)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 557
            _la = self._input.LA(1)
            if not(_la==119 or _la==120):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RangeCriteriaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RANGE(self):
            return self.getToken(PanelParser.RANGE, 0)

        def COMMACHAR(self, i:int=None):
            if i is None:
                return self.getTokens(PanelParser.COMMACHAR)
            else:
                return self.getToken(PanelParser.COMMACHAR, i)

        def lower(self):
            return self.getTypedRuleContext(PanelParser.LowerContext,0)


        def upper(self):
            return self.getTypedRuleContext(PanelParser.UpperContext,0)


        def getRuleIndex(self):
            return PanelParser.RULE_rangeCriteria

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRangeCriteria" ):
                listener.enterRangeCriteria(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRangeCriteria" ):
                listener.exitRangeCriteria(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRangeCriteria" ):
                return visitor.visitRangeCriteria(self)
            else:
                return visitor.visitChildren(self)




    def rangeCriteria(self):

        localctx = PanelParser.RangeCriteriaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_rangeCriteria)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 559
            self.match(PanelParser.RANGE)
            self.state = 560
            self.match(PanelParser.COMMACHAR)
            self.state = 561
            self.lower()
            self.state = 562
            self.match(PanelParser.COMMACHAR)
            self.state = 563
            self.upper()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpectedLengthContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGERLITERAL(self):
            return self.getToken(PanelParser.INTEGERLITERAL, 0)

        def getRuleIndex(self):
            return PanelParser.RULE_expectedLength

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpectedLength" ):
                listener.enterExpectedLength(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpectedLength" ):
                listener.exitExpectedLength(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpectedLength" ):
                return visitor.visitExpectedLength(self)
            else:
                return visitor.visitChildren(self)




    def expectedLength(self):

        localctx = PanelParser.ExpectedLengthContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_expectedLength)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 565
            self.match(PanelParser.INTEGERLITERAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StringValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRINGLITERAL(self):
            return self.getToken(PanelParser.STRINGLITERAL, 0)

        def getRuleIndex(self):
            return PanelParser.RULE_stringValue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStringValue" ):
                listener.enterStringValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStringValue" ):
                listener.exitStringValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringValue" ):
                return visitor.visitStringValue(self)
            else:
                return visitor.visitChildren(self)




    def stringValue(self):

        localctx = PanelParser.StringValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_stringValue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 567
            self.match(PanelParser.STRINGLITERAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(PanelParser.IDENTIFIER)
            else:
                return self.getToken(PanelParser.IDENTIFIER, i)

        def COMMACHAR(self, i:int=None):
            if i is None:
                return self.getTokens(PanelParser.COMMACHAR)
            else:
                return self.getToken(PanelParser.COMMACHAR, i)

        def getRuleIndex(self):
            return PanelParser.RULE_varlist

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarlist" ):
                listener.enterVarlist(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarlist" ):
                listener.exitVarlist(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarlist" ):
                return visitor.visitVarlist(self)
            else:
                return visitor.visitChildren(self)




    def varlist(self):

        localctx = PanelParser.VarlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_varlist)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 569
            self.match(PanelParser.IDENTIFIER)
            self.state = 574
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 570
                    self.match(PanelParser.COMMACHAR)
                    self.state = 571
                    self.match(PanelParser.IDENTIFIER) 
                self.state = 576
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MaskCharacterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(PanelParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return PanelParser.RULE_maskCharacter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMaskCharacter" ):
                listener.enterMaskCharacter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMaskCharacter" ):
                listener.exitMaskCharacter(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMaskCharacter" ):
                return visitor.visitMaskCharacter(self)
            else:
                return visitor.visitChildren(self)




    def maskCharacter(self):

        localctx = PanelParser.MaskCharacterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_maskCharacter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 577
            self.match(PanelParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldMaskContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRINGLITERAL(self):
            return self.getToken(PanelParser.STRINGLITERAL, 0)

        def getRuleIndex(self):
            return PanelParser.RULE_fieldMask

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFieldMask" ):
                listener.enterFieldMask(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFieldMask" ):
                listener.exitFieldMask(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFieldMask" ):
                return visitor.visitFieldMask(self)
            else:
                return visitor.visitChildren(self)




    def fieldMask(self):

        localctx = PanelParser.FieldMaskContext(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_fieldMask)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 579
            self.match(PanelParser.STRINGLITERAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LowerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self):
            return self.getTypedRuleContext(PanelParser.ValueContext,0)


        def getRuleIndex(self):
            return PanelParser.RULE_lower

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLower" ):
                listener.enterLower(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLower" ):
                listener.exitLower(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLower" ):
                return visitor.visitLower(self)
            else:
                return visitor.visitChildren(self)




    def lower(self):

        localctx = PanelParser.LowerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 132, self.RULE_lower)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 581
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UpperContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self):
            return self.getTypedRuleContext(PanelParser.ValueContext,0)


        def getRuleIndex(self):
            return PanelParser.RULE_upper

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUpper" ):
                listener.enterUpper(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUpper" ):
                listener.exitUpper(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUpper" ):
                return visitor.visitUpper(self)
            else:
                return visitor.visitChildren(self)




    def upper(self):

        localctx = PanelParser.UpperContext(self, self._ctx, self.state)
        self.enterRule(localctx, 134, self.RULE_upper)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 583
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseIfContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(PanelParser.ELSE, 0)

        def statement(self):
            return self.getTypedRuleContext(PanelParser.StatementContext,0)


        def getRuleIndex(self):
            return PanelParser.RULE_elseIf

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElseIf" ):
                listener.enterElseIf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElseIf" ):
                listener.exitElseIf(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseIf" ):
                return visitor.visitElseIf(self)
            else:
                return visitor.visitChildren(self)




    def elseIf(self):

        localctx = PanelParser.ElseIfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 136, self.RULE_elseIf)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 585
            self.match(PanelParser.ELSE)
            self.state = 587
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.state = 586
                self.statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self):
            return self.getTypedRuleContext(PanelParser.VariableContext,0)


        def assignPart(self):
            return self.getTypedRuleContext(PanelParser.AssignPartContext,0)


        def getRuleIndex(self):
            return PanelParser.RULE_assignStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignStatement" ):
                listener.enterAssignStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignStatement" ):
                listener.exitAssignStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignStatement" ):
                return visitor.visitAssignStatement(self)
            else:
                return visitor.visitChildren(self)




    def assignStatement(self):

        localctx = PanelParser.AssignStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 138, self.RULE_assignStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 589
            self.variable()
            self.state = 590
            self.assignPart()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(PanelParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return PanelParser.RULE_variable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable" ):
                listener.enterVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable" ):
                listener.exitVariable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable" ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)




    def variable(self):

        localctx = PanelParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 140, self.RULE_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 592
            self.match(PanelParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignPartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUALCHAR(self):
            return self.getToken(PanelParser.EQUALCHAR, 0)

        def value(self):
            return self.getTypedRuleContext(PanelParser.ValueContext,0)


        def getRuleIndex(self):
            return PanelParser.RULE_assignPart

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignPart" ):
                listener.enterAssignPart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignPart" ):
                listener.exitAssignPart(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignPart" ):
                return visitor.visitAssignPart(self)
            else:
                return visitor.visitChildren(self)




    def assignPart(self):

        localctx = PanelParser.AssignPartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 142, self.RULE_assignPart)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 594
            self.match(PanelParser.EQUALCHAR)
            self.state = 595
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VgetStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VGET(self):
            return self.getToken(PanelParser.VGET, 0)

        def name_list(self):
            return self.getTypedRuleContext(PanelParser.Name_listContext,0)


        def vgetParameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PanelParser.VgetParameterContext)
            else:
                return self.getTypedRuleContext(PanelParser.VgetParameterContext,i)


        def getRuleIndex(self):
            return PanelParser.RULE_vgetStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVgetStatement" ):
                listener.enterVgetStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVgetStatement" ):
                listener.exitVgetStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVgetStatement" ):
                return visitor.visitVgetStatement(self)
            else:
                return visitor.visitChildren(self)




    def vgetStatement(self):

        localctx = PanelParser.VgetStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 144, self.RULE_vgetStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 597
            self.match(PanelParser.VGET)
            self.state = 598
            self.name_list()
            self.state = 602
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 599
                    self.vgetParameter() 
                self.state = 604
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VputStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VPUT(self):
            return self.getToken(PanelParser.VPUT, 0)

        def name_list(self):
            return self.getTypedRuleContext(PanelParser.Name_listContext,0)


        def vputParameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PanelParser.VputParameterContext)
            else:
                return self.getTypedRuleContext(PanelParser.VputParameterContext,i)


        def getRuleIndex(self):
            return PanelParser.RULE_vputStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVputStatement" ):
                listener.enterVputStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVputStatement" ):
                listener.exitVputStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVputStatement" ):
                return visitor.visitVputStatement(self)
            else:
                return visitor.visitChildren(self)




    def vputStatement(self):

        localctx = PanelParser.VputStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 146, self.RULE_vputStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 605
            self.match(PanelParser.VPUT)
            self.state = 606
            self.name_list()
            self.state = 610
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,36,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 607
                    self.vputParameter() 
                self.state = 612
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,36,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Name_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(PanelParser.IDENTIFIER, 0)

        def LPAREN(self):
            return self.getToken(PanelParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(PanelParser.RPAREN, 0)

        def name_list_item(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PanelParser.Name_list_itemContext)
            else:
                return self.getTypedRuleContext(PanelParser.Name_list_itemContext,i)


        def COMMACHAR(self, i:int=None):
            if i is None:
                return self.getTokens(PanelParser.COMMACHAR)
            else:
                return self.getToken(PanelParser.COMMACHAR, i)

        def getRuleIndex(self):
            return PanelParser.RULE_name_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterName_list" ):
                listener.enterName_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitName_list" ):
                listener.exitName_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitName_list" ):
                return visitor.visitName_list(self)
            else:
                return visitor.visitChildren(self)




    def name_list(self):

        localctx = PanelParser.Name_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 148, self.RULE_name_list)
        self._la = 0 # Token type
        try:
            self.state = 633
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 613
                self.match(PanelParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 614
                self.match(PanelParser.LPAREN)
                self.state = 616 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 615
                    self.name_list_item()
                    self.state = 618 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 4538990157891584) != 0) or ((((_la - 80)) & ~0x3f) == 0 and ((1 << (_la - 80)) & 1726578951169) != 0)):
                        break

                self.state = 620
                self.match(PanelParser.RPAREN)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 622
                self.match(PanelParser.LPAREN)
                self.state = 623
                self.name_list_item()
                self.state = 628
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==9:
                    self.state = 624
                    self.match(PanelParser.COMMACHAR)
                    self.state = 625
                    self.name_list_item()
                    self.state = 630
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 631
                self.match(PanelParser.RPAREN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Name_list_itemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self):
            return self.getTypedRuleContext(PanelParser.ValueContext,0)


        def getRuleIndex(self):
            return PanelParser.RULE_name_list_item

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterName_list_item" ):
                listener.enterName_list_item(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitName_list_item" ):
                listener.exitName_list_item(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitName_list_item" ):
                return visitor.visitName_list_item(self)
            else:
                return visitor.visitChildren(self)




    def name_list_item(self):

        localctx = PanelParser.Name_list_itemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 150, self.RULE_name_list_item)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 635
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VgetParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self):
            return self.getTypedRuleContext(PanelParser.ValueContext,0)


        def getRuleIndex(self):
            return PanelParser.RULE_vgetParameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVgetParameter" ):
                listener.enterVgetParameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVgetParameter" ):
                listener.exitVgetParameter(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVgetParameter" ):
                return visitor.visitVgetParameter(self)
            else:
                return visitor.visitChildren(self)




    def vgetParameter(self):

        localctx = PanelParser.VgetParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 152, self.RULE_vgetParameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 637
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VputParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self):
            return self.getTypedRuleContext(PanelParser.ValueContext,0)


        def getRuleIndex(self):
            return PanelParser.RULE_vputParameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVputParameter" ):
                listener.enterVputParameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVputParameter" ):
                listener.exitVputParameter(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVputParameter" ):
                return visitor.visitVputParameter(self)
            else:
                return visitor.visitChildren(self)




    def vputParameter(self):

        localctx = PanelParser.VputParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 154, self.RULE_vputParameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 639
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InitSectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RPAREN(self):
            return self.getToken(PanelParser.RPAREN, 0)

        def INIT(self):
            return self.getToken(PanelParser.INIT, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PanelParser.StatementContext)
            else:
                return self.getTypedRuleContext(PanelParser.StatementContext,i)


        def getRuleIndex(self):
            return PanelParser.RULE_initSection

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInitSection" ):
                listener.enterInitSection(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInitSection" ):
                listener.exitInitSection(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInitSection" ):
                return visitor.visitInitSection(self)
            else:
                return visitor.visitChildren(self)




    def initSection(self):

        localctx = PanelParser.InitSectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 156, self.RULE_initSection)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 641
            self.match(PanelParser.RPAREN)
            self.state = 642
            self.match(PanelParser.INIT)
            self.state = 646
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 72204928596049920) != 0) or _la==109 or _la==119:
                self.state = 643
                self.statement()
                self.state = 648
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProcSectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RPAREN(self):
            return self.getToken(PanelParser.RPAREN, 0)

        def PROC(self):
            return self.getToken(PanelParser.PROC, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PanelParser.StatementContext)
            else:
                return self.getTypedRuleContext(PanelParser.StatementContext,i)


        def getRuleIndex(self):
            return PanelParser.RULE_procSection

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProcSection" ):
                listener.enterProcSection(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProcSection" ):
                listener.exitProcSection(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProcSection" ):
                return visitor.visitProcSection(self)
            else:
                return visitor.visitChildren(self)




    def procSection(self):

        localctx = PanelParser.ProcSectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 158, self.RULE_procSection)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 649
            self.match(PanelParser.RPAREN)
            self.state = 650
            self.match(PanelParser.PROC)
            self.state = 654
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 72204928596049920) != 0) or _la==109 or _la==119:
                self.state = 651
                self.statement()
                self.state = 656
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefaultParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEFAULT(self):
            return self.getToken(PanelParser.DEFAULT, 0)

        def LPAREN(self):
            return self.getToken(PanelParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(PanelParser.RPAREN, 0)

        def defValue(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PanelParser.DefValueContext)
            else:
                return self.getTypedRuleContext(PanelParser.DefValueContext,i)


        def getRuleIndex(self):
            return PanelParser.RULE_defaultParam

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefaultParam" ):
                listener.enterDefaultParam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefaultParam" ):
                listener.exitDefaultParam(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefaultParam" ):
                return visitor.visitDefaultParam(self)
            else:
                return visitor.visitChildren(self)




    def defaultParam(self):

        localctx = PanelParser.DefaultParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 160, self.RULE_defaultParam)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 657
            self.match(PanelParser.DEFAULT)
            self.state = 658
            self.match(PanelParser.LPAREN)
            self.state = 660 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 659
                self.defValue()
                self.state = 662 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 8387064) != 0) or _la==121):
                    break

            self.state = 664
            self.match(PanelParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attrChar(self):
            return self.getTypedRuleContext(PanelParser.AttrCharContext,0)


        def getRuleIndex(self):
            return PanelParser.RULE_defValue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefValue" ):
                listener.enterDefValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefValue" ):
                listener.exitDefValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefValue" ):
                return visitor.visitDefValue(self)
            else:
                return visitor.visitChildren(self)




    def defValue(self):

        localctx = PanelParser.DefValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 162, self.RULE_defValue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 666
            self.attrChar()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FormatParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FORMAT(self):
            return self.getToken(PanelParser.FORMAT, 0)

        def LPAREN(self):
            return self.getToken(PanelParser.LPAREN, 0)

        def formatValue(self):
            return self.getTypedRuleContext(PanelParser.FormatValueContext,0)


        def RPAREN(self):
            return self.getToken(PanelParser.RPAREN, 0)

        def getRuleIndex(self):
            return PanelParser.RULE_formatParam

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFormatParam" ):
                listener.enterFormatParam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFormatParam" ):
                listener.exitFormatParam(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFormatParam" ):
                return visitor.visitFormatParam(self)
            else:
                return visitor.visitChildren(self)




    def formatParam(self):

        localctx = PanelParser.FormatParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 164, self.RULE_formatParam)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 668
            self.match(PanelParser.FORMAT)
            self.state = 669
            self.match(PanelParser.LPAREN)
            self.state = 670
            self.formatValue()
            self.state = 671
            self.match(PanelParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FormatValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EBCDIC(self):
            return self.getToken(PanelParser.EBCDIC, 0)

        def DBCS(self):
            return self.getToken(PanelParser.DBCS, 0)

        def MIX(self):
            return self.getToken(PanelParser.MIX, 0)

        def getRuleIndex(self):
            return PanelParser.RULE_formatValue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFormatValue" ):
                listener.enterFormatValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFormatValue" ):
                listener.exitFormatValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFormatValue" ):
                return visitor.visitFormatValue(self)
            else:
                return visitor.visitChildren(self)




    def formatValue(self):

        localctx = PanelParser.FormatValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 166, self.RULE_formatValue)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 673
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3758096384) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EndSectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RPAREN(self):
            return self.getToken(PanelParser.RPAREN, 0)

        def END(self):
            return self.getToken(PanelParser.END, 0)

        def getRuleIndex(self):
            return PanelParser.RULE_endSection

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEndSection" ):
                listener.enterEndSection(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEndSection" ):
                listener.exitEndSection(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEndSection" ):
                return visitor.visitEndSection(self)
            else:
                return visitor.visitChildren(self)




    def endSection(self):

        localctx = PanelParser.EndSectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 168, self.RULE_endSection)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 675
            self.match(PanelParser.RPAREN)
            self.state = 676
            self.match(PanelParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PanelFunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def transFunc(self):
            return self.getTypedRuleContext(PanelParser.TransFuncContext,0)


        def truncFunc(self):
            return self.getTypedRuleContext(PanelParser.TruncFuncContext,0)


        def lvlineFunc(self):
            return self.getTypedRuleContext(PanelParser.LvlineFuncContext,0)


        def pfkFunc(self):
            return self.getTypedRuleContext(PanelParser.PfkFuncContext,0)


        def getRuleIndex(self):
            return PanelParser.RULE_panelFunction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPanelFunction" ):
                listener.enterPanelFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPanelFunction" ):
                listener.exitPanelFunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPanelFunction" ):
                return visitor.visitPanelFunction(self)
            else:
                return visitor.visitChildren(self)




    def panelFunction(self):

        localctx = PanelParser.PanelFunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 170, self.RULE_panelFunction)
        try:
            self.state = 682
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [52]:
                self.enterOuterAlt(localctx, 1)
                self.state = 678
                self.transFunc()
                pass
            elif token in [36]:
                self.enterOuterAlt(localctx, 2)
                self.state = 679
                self.truncFunc()
                pass
            elif token in [101]:
                self.enterOuterAlt(localctx, 3)
                self.state = 680
                self.lvlineFunc()
                pass
            elif token in [113]:
                self.enterOuterAlt(localctx, 4)
                self.state = 681
                self.pfkFunc()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PfkFuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PFK(self):
            return self.getToken(PanelParser.PFK, 0)

        def LPAREN(self):
            return self.getToken(PanelParser.LPAREN, 0)

        def pfkParam(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PanelParser.PfkParamContext)
            else:
                return self.getTypedRuleContext(PanelParser.PfkParamContext,i)


        def RPAREN(self):
            return self.getToken(PanelParser.RPAREN, 0)

        def COMMACHAR(self, i:int=None):
            if i is None:
                return self.getTokens(PanelParser.COMMACHAR)
            else:
                return self.getToken(PanelParser.COMMACHAR, i)

        def getRuleIndex(self):
            return PanelParser.RULE_pfkFunc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPfkFunc" ):
                listener.enterPfkFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPfkFunc" ):
                listener.exitPfkFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPfkFunc" ):
                return visitor.visitPfkFunc(self)
            else:
                return visitor.visitChildren(self)




    def pfkFunc(self):

        localctx = PanelParser.PfkFuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 172, self.RULE_pfkFunc)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 684
            self.match(PanelParser.PFK)
            self.state = 685
            self.match(PanelParser.LPAREN)
            self.state = 686
            self.pfkParam()
            self.state = 691
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 687
                self.match(PanelParser.COMMACHAR)
                self.state = 688
                self.pfkParam()
                self.state = 693
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 694
            self.match(PanelParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PfkParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(PanelParser.IDENTIFIER, 0)

        def END(self):
            return self.getToken(PanelParser.END, 0)

        def getRuleIndex(self):
            return PanelParser.RULE_pfkParam

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPfkParam" ):
                listener.enterPfkParam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPfkParam" ):
                listener.exitPfkParam(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPfkParam" ):
                return visitor.visitPfkParam(self)
            else:
                return visitor.visitChildren(self)




    def pfkParam(self):

        localctx = PanelParser.PfkParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 174, self.RULE_pfkParam)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 696
            _la = self._input.LA(1)
            if not(_la==44 or _la==119):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LvlineFuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LVLINE(self):
            return self.getToken(PanelParser.LVLINE, 0)

        def LPAREN(self):
            return self.getToken(PanelParser.LPAREN, 0)

        def lvlineParam(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PanelParser.LvlineParamContext)
            else:
                return self.getTypedRuleContext(PanelParser.LvlineParamContext,i)


        def RPAREN(self):
            return self.getToken(PanelParser.RPAREN, 0)

        def COMMACHAR(self, i:int=None):
            if i is None:
                return self.getTokens(PanelParser.COMMACHAR)
            else:
                return self.getToken(PanelParser.COMMACHAR, i)

        def getRuleIndex(self):
            return PanelParser.RULE_lvlineFunc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLvlineFunc" ):
                listener.enterLvlineFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLvlineFunc" ):
                listener.exitLvlineFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLvlineFunc" ):
                return visitor.visitLvlineFunc(self)
            else:
                return visitor.visitChildren(self)




    def lvlineFunc(self):

        localctx = PanelParser.LvlineFuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 176, self.RULE_lvlineFunc)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 698
            self.match(PanelParser.LVLINE)
            self.state = 699
            self.match(PanelParser.LPAREN)
            self.state = 700
            self.lvlineParam()
            self.state = 705
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 701
                self.match(PanelParser.COMMACHAR)
                self.state = 702
                self.lvlineParam()
                self.state = 707
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 708
            self.match(PanelParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LvlineParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(PanelParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return PanelParser.RULE_lvlineParam

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLvlineParam" ):
                listener.enterLvlineParam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLvlineParam" ):
                listener.exitLvlineParam(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLvlineParam" ):
                return visitor.visitLvlineParam(self)
            else:
                return visitor.visitChildren(self)




    def lvlineParam(self):

        localctx = PanelParser.LvlineParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 178, self.RULE_lvlineParam)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 710
            self.match(PanelParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StringExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRINGLITERAL(self):
            return self.getToken(PanelParser.STRINGLITERAL, 0)

        def variable(self):
            return self.getTypedRuleContext(PanelParser.VariableContext,0)


        def getRuleIndex(self):
            return PanelParser.RULE_stringExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStringExpression" ):
                listener.enterStringExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStringExpression" ):
                listener.exitStringExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringExpression" ):
                return visitor.visitStringExpression(self)
            else:
                return visitor.visitChildren(self)




    def stringExpression(self):

        localctx = PanelParser.StringExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 180, self.RULE_stringExpression)
        try:
            self.state = 714
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [120]:
                self.enterOuterAlt(localctx, 1)
                self.state = 712
                self.match(PanelParser.STRINGLITERAL)
                pass
            elif token in [119]:
                self.enterOuterAlt(localctx, 2)
                self.state = 713
                self.variable()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IntegerExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGERLITERAL(self):
            return self.getToken(PanelParser.INTEGERLITERAL, 0)

        def variable(self):
            return self.getTypedRuleContext(PanelParser.VariableContext,0)


        def getRuleIndex(self):
            return PanelParser.RULE_integerExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIntegerExpression" ):
                listener.enterIntegerExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntegerExpression" ):
                listener.exitIntegerExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntegerExpression" ):
                return visitor.visitIntegerExpression(self)
            else:
                return visitor.visitChildren(self)




    def integerExpression(self):

        localctx = PanelParser.IntegerExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 182, self.RULE_integerExpression)
        try:
            self.state = 718
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [116]:
                self.enterOuterAlt(localctx, 1)
                self.state = 716
                self.match(PanelParser.INTEGERLITERAL)
                pass
            elif token in [119]:
                self.enterOuterAlt(localctx, 2)
                self.state = 717
                self.variable()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TruncFuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUNC(self):
            return self.getToken(PanelParser.TRUNC, 0)

        def LPAREN(self):
            return self.getToken(PanelParser.LPAREN, 0)

        def stringToTrunc(self):
            return self.getTypedRuleContext(PanelParser.StringToTruncContext,0)


        def COMMACHAR(self):
            return self.getToken(PanelParser.COMMACHAR, 0)

        def RPAREN(self):
            return self.getToken(PanelParser.RPAREN, 0)

        def indexToTrunc(self):
            return self.getTypedRuleContext(PanelParser.IndexToTruncContext,0)


        def subStringToTrunc(self):
            return self.getTypedRuleContext(PanelParser.SubStringToTruncContext,0)


        def getRuleIndex(self):
            return PanelParser.RULE_truncFunc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTruncFunc" ):
                listener.enterTruncFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTruncFunc" ):
                listener.exitTruncFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTruncFunc" ):
                return visitor.visitTruncFunc(self)
            else:
                return visitor.visitChildren(self)




    def truncFunc(self):

        localctx = PanelParser.TruncFuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 184, self.RULE_truncFunc)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 720
            self.match(PanelParser.TRUNC)
            self.state = 721
            self.match(PanelParser.LPAREN)
            self.state = 722
            self.stringToTrunc()
            self.state = 723
            self.match(PanelParser.COMMACHAR)
            self.state = 726
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                self.state = 724
                self.indexToTrunc()
                pass

            elif la_ == 2:
                self.state = 725
                self.subStringToTrunc()
                pass


            self.state = 728
            self.match(PanelParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StringToTruncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stringExpression(self):
            return self.getTypedRuleContext(PanelParser.StringExpressionContext,0)


        def getRuleIndex(self):
            return PanelParser.RULE_stringToTrunc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStringToTrunc" ):
                listener.enterStringToTrunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStringToTrunc" ):
                listener.exitStringToTrunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringToTrunc" ):
                return visitor.visitStringToTrunc(self)
            else:
                return visitor.visitChildren(self)




    def stringToTrunc(self):

        localctx = PanelParser.StringToTruncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 186, self.RULE_stringToTrunc)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 730
            self.stringExpression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IndexToTruncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def integerExpression(self):
            return self.getTypedRuleContext(PanelParser.IntegerExpressionContext,0)


        def getRuleIndex(self):
            return PanelParser.RULE_indexToTrunc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIndexToTrunc" ):
                listener.enterIndexToTrunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIndexToTrunc" ):
                listener.exitIndexToTrunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndexToTrunc" ):
                return visitor.visitIndexToTrunc(self)
            else:
                return visitor.visitChildren(self)




    def indexToTrunc(self):

        localctx = PanelParser.IndexToTruncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 188, self.RULE_indexToTrunc)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 732
            self.integerExpression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubStringToTruncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stringExpression(self):
            return self.getTypedRuleContext(PanelParser.StringExpressionContext,0)


        def getRuleIndex(self):
            return PanelParser.RULE_subStringToTrunc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubStringToTrunc" ):
                listener.enterSubStringToTrunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubStringToTrunc" ):
                listener.exitSubStringToTrunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubStringToTrunc" ):
                return visitor.visitSubStringToTrunc(self)
            else:
                return visitor.visitChildren(self)




    def subStringToTrunc(self):

        localctx = PanelParser.SubStringToTruncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 190, self.RULE_subStringToTrunc)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 734
            self.stringExpression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TransFuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRANS(self):
            return self.getToken(PanelParser.TRANS, 0)

        def LPAREN(self):
            return self.getToken(PanelParser.LPAREN, 0)

        def transParam(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PanelParser.TransParamContext)
            else:
                return self.getTypedRuleContext(PanelParser.TransParamContext,i)


        def COMMACHAR(self, i:int=None):
            if i is None:
                return self.getTokens(PanelParser.COMMACHAR)
            else:
                return self.getToken(PanelParser.COMMACHAR, i)

        def transDefaultOutput(self):
            return self.getTypedRuleContext(PanelParser.TransDefaultOutputContext,0)


        def RPAREN(self):
            return self.getToken(PanelParser.RPAREN, 0)

        def getRuleIndex(self):
            return PanelParser.RULE_transFunc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTransFunc" ):
                listener.enterTransFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTransFunc" ):
                listener.exitTransFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTransFunc" ):
                return visitor.visitTransFunc(self)
            else:
                return visitor.visitChildren(self)




    def transFunc(self):

        localctx = PanelParser.TransFuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 192, self.RULE_transFunc)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 736
            self.match(PanelParser.TRANS)
            self.state = 737
            self.match(PanelParser.LPAREN)
            self.state = 738
            self.transParam()
            self.state = 743
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,49,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 739
                    self.match(PanelParser.COMMACHAR)
                    self.state = 740
                    self.transParam() 
                self.state = 745
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,49,self._ctx)

            self.state = 746
            self.match(PanelParser.COMMACHAR)
            self.state = 747
            self.transDefaultOutput()
            self.state = 748
            self.match(PanelParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TransDefaultOutputContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRINGLITERAL(self):
            return self.getToken(PanelParser.STRINGLITERAL, 0)

        def getRuleIndex(self):
            return PanelParser.RULE_transDefaultOutput

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTransDefaultOutput" ):
                listener.enterTransDefaultOutput(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTransDefaultOutput" ):
                listener.exitTransDefaultOutput(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTransDefaultOutput" ):
                return visitor.visitTransDefaultOutput(self)
            else:
                return visitor.visitChildren(self)




    def transDefaultOutput(self):

        localctx = PanelParser.TransDefaultOutputContext(self, self._ctx, self.state)
        self.enterRule(localctx, 194, self.RULE_transDefaultOutput)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 750
            self.match(PanelParser.STRINGLITERAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TransParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def transVariable(self):
            return self.getTypedRuleContext(PanelParser.TransVariableContext,0)


        def transReturn(self):
            return self.getTypedRuleContext(PanelParser.TransReturnContext,0)


        def getRuleIndex(self):
            return PanelParser.RULE_transParam

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTransParam" ):
                listener.enterTransParam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTransParam" ):
                listener.exitTransParam(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTransParam" ):
                return visitor.visitTransParam(self)
            else:
                return visitor.visitChildren(self)




    def transParam(self):

        localctx = PanelParser.TransParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 196, self.RULE_transParam)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 752
            self.transVariable()
            self.state = 753
            self.transReturn()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TransVariableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self):
            return self.getTypedRuleContext(PanelParser.ValueContext,0)


        def getRuleIndex(self):
            return PanelParser.RULE_transVariable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTransVariable" ):
                listener.enterTransVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTransVariable" ):
                listener.exitTransVariable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTransVariable" ):
                return visitor.visitTransVariable(self)
            else:
                return visitor.visitChildren(self)




    def transVariable(self):

        localctx = PanelParser.TransVariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 198, self.RULE_transVariable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 755
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TransReturnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self):
            return self.getTypedRuleContext(PanelParser.ValueContext,0)


        def getRuleIndex(self):
            return PanelParser.RULE_transReturn

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTransReturn" ):
                listener.enterTransReturn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTransReturn" ):
                listener.exitTransReturn(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTransReturn" ):
                return visitor.visitTransReturn(self)
            else:
                return visitor.visitChildren(self)




    def transReturn(self):

        localctx = PanelParser.TransReturnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 200, self.RULE_transReturn)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 757
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(PanelParser.IDENTIFIER, 0)

        def stringExpression(self):
            return self.getTypedRuleContext(PanelParser.StringExpressionContext,0)


        def panelFunction(self):
            return self.getTypedRuleContext(PanelParser.PanelFunctionContext,0)


        def integerExpression(self):
            return self.getTypedRuleContext(PanelParser.IntegerExpressionContext,0)


        def ASTERISK(self):
            return self.getToken(PanelParser.ASTERISK, 0)

        def variable(self):
            return self.getTypedRuleContext(PanelParser.VariableContext,0)


        def charDataKeyword(self):
            return self.getTypedRuleContext(PanelParser.CharDataKeywordContext,0)


        def getRuleIndex(self):
            return PanelParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)




    def value(self):

        localctx = PanelParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 202, self.RULE_value)
        try:
            self.state = 766
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 759
                self.match(PanelParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 760
                self.stringExpression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 761
                self.panelFunction()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 762
                self.integerExpression()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 763
                self.match(PanelParser.ASTERISK)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 764
                self.variable()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 765
                self.charDataKeyword()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CharDataKeywordContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MSG(self):
            return self.getToken(PanelParser.MSG, 0)

        def TYPE(self):
            return self.getToken(PanelParser.TYPE, 0)

        def USER(self):
            return self.getToken(PanelParser.USER, 0)

        def NAME(self):
            return self.getToken(PanelParser.NAME, 0)

        def getRuleIndex(self):
            return PanelParser.RULE_charDataKeyword

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCharDataKeyword" ):
                listener.enterCharDataKeyword(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCharDataKeyword" ):
                listener.exitCharDataKeyword(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCharDataKeyword" ):
                return visitor.visitCharDataKeyword(self)
            else:
                return visitor.visitChildren(self)




    def charDataKeyword(self):

        localctx = PanelParser.CharDataKeywordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 204, self.RULE_charDataKeyword)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 768
            _la = self._input.LA(1)
            if not(((((_la - 37)) & ~0x3f) == 0 and ((1 << (_la - 37)) & 9015995347763457) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





