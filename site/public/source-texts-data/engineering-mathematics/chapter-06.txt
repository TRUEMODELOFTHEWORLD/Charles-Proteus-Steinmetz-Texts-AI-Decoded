CHAPTER VII. 
NUMERICAL CALCULATIONS. 

i6o. Engineering work leads to more or less extensive 
numerical calculations, when applying the general theoretical 
investigation to the specific cases which are under considera- 
tion. Of importance in such engineering calculation^ are : 

(a) The method of calculation. 

(5) The degree of exactness required in the calculation. 

(c) The intelligibility of the results. 

(d) The reliability of the calculation. 

a. Method of Calculation. 

Before beginning a more extensive calculation, it is desirable 
carefully to scrutinize and to investigate the method, to find 
the simplest way, since frequently by a suitable method and 
system of calculation the work can be reduced to a small frac- 
tion of what it would otherwise be, and what appear to be 
hopelessly complex calculations may thus be carried out 
quickly and expeditiously by a proper arrangement of the 
work. The most convenient way usually is the arrangement 
in tabular form. 

As example, consider the problem of calculating the regula- 
tion of a 6(),000-volt transmission line, of r = 60 ohms resist- 
ance, a;= 135 ohms inductive reactance, and 6 = 0.0012 conden- 
sive susceptance, for various values of non-inductive, inductive, 
and condensive load. 

Starting with the complete equations of the long-distance 
transmission line, as given in "Theory and Calculation of 
Transient Electric Phenomena and Oscillations," Section III, 
paragraph 9, and considering that for every one of the various 
power-factors, lag, and lead, a sufficient number of values 

249 


250 


ENGINEERING MATHEMATICS. 


have to be calculated to give a curve, the amount of work 
appears hopelessly large. 

However, without loss of engineering exactness, the equa- 
tion of the transmission line can be simplified by approxima- 
tion, as discussed in Chapter V, paragraph 123, to the form. 


+ ^/o 


1+- 


ZY 


+ F^oU+^^ 


(1) 


where Eo, h are voltage and current, respectively at the step- 
down end, El, I\ at the step-up end of the line; and 

Z = r—jx = Q^—\Zbj is the total line impedance; 

Y = g — jh= —0.0012/ is the total shunted line admittance. 

Herefrom follow the numerical values : 


ZY (60-135.f)(-0.0012i) 

■^2 2 


= 1 - 0.036./- 0.081 = 0.919 - 0.036/; 


ZY 


1+- g- = 1 - 0.012/- 0.027 = 0.973 - 0.012/; 


ryi ZY 

Z 14--,- 


-»4'' 


= (60- 135/) (0.973 -0.012/) 

= 58.4-0.72/- 131.1/- 1.62 = 56.8-131.8/; 

= (-0.0012/) (0.973 -0.012/) 

= -0.001168/-0.0000144 = (-0.0144- 1.168/)10-2 


hence, substituting in (1), the following equations may be 
written : 


J^i = (0.919-0.036/)J5;o+(56.8-131.8/)/o = A +5; 1 

/i = (0.919 -0.036/)7o - (0.0144 +1.168/)^olO-3 = C-D. / 


(2> 


NUMERICAL CALCULATIONS, 


251 


i6i. Now the work of calculating a series of numerical 
values is continued in tabular form, as follows : 

1. 100 PER CENT Power-factor. 

Eo=60 kv. at step-down end of line. 

A = (0.919-0.036/)£;o=55.1-2.2y kv. 

D = (0. 0 144+1. 168?) £?o 10- 3 = 0.9 + 70.1/ amp. 


Iq amp. 

Bkv. 

Ei = ei- 

-eJ2 
= A+B. 

ei2 + g22 = g2. 

e 

— = tan e. 

ei 

4-6. 

0 

0 

55.1- 

- 2.2/ 

3036+ 5 = 3041 

55.1 

-0.040 

- 2.3 

20 

1.1- 2.6/ 

56.2- 

- 4.8/ 

3158+ 23 = 3181 

56.4 

-0.085 

- 4.9 

40 

2.3- 5.3/ 

57.4- 

- 9.5/ 

3295+ 56 = 3351 

57.9 

-0.131 

- 7.5 

60 

3.4- 7.9/ 

58.5- 

-10.1/ 

3422 + 102 = 3524 

59.4 

-0.173 

- 9.9 

80 

4.5-10.5/ 

59.6- 

-12.7/ 

3552 + 161 = 3713 

60.9 

-0.213 

-12.0 

100 

5.7-13.2/ 

60.8- 

-15.4/ 

3697 + 237 = 3934 

62.7 

-0.253 

-14.2 

120 

6.8-15.8/ 

61.9- 

-18.0/ 

3832 + 324=4156 

64.5 

-0.291 

-16.3 

h 
amp. 

, C amp. 

Il = tl=/t2 

= C-D 

tl2 + t22 = i2 

i 

*i=tam 

A-i 

2^t- 

i 4-e= 

4-«'* 

Power- 
factor 

0 

0 

-0.7-90.1/ 

4914+1 = 4915 

70.1 

+ 78 

+ 89.1 
-90.9 

-88.6 

0.024 

20 

18.4-0.7/ 

17.5-70.8/ 

5013+ 306= 5319 

72.9 

-4.04 

-76.3 

-71.4 

0.332 

40 

36.8-1.4/ 

35.9-71.5/ 

5112 + 1289= 6401 

80.0 

-1.99 

-63.4 

-55.9 

0.558 

60 

55.1-2.2/ 

54.2-72.3/ 

5227 + 2938= 8165 

90.4 

-1.33 

-53.1 

-43.2 

0.728 

80 

73.5-2.9/ 

72.6-73.0/ 

5329 + 5271=10600 

103.0 

-1.055 

-45.2 

-33.2 

0.837 

100 

91.9-3.6/ 

91.0-73.9/ 

8281 + 5432=13713 

117.1 

-0.811 

-39.1 

-24.9 

0.907 

120 

110.3-4.3/ 

109.4-74.4/ 

11969 + 5535=17504 

132.3 

-0.680 

-34.1 

-17.8 

0.952 
lead 

61 = 60 kv. at step-up end of line. 

/o 
amp. 

Red. Factor, 

e 
60 

amp. 

kv. 

amp. 

Power-Factor. 

0 

0.918 

0 

65.5 

76.4 

0.024 

20 

0.940 

21.3 

63.8 

77.5 

0.332 

40 

0.965 

41.4 

62.1 

82.9 

0.558 

60 

0.990 

60.6 

60.6 

91.4 

0.728 

80 

1.015 

78.8 

59.1 

101.5 

0.837 

100 

1.045 

95.7 

57.5 

112.3 

0.907 

120 

1.075 

111.7 

55.8 

122.8 

0.952 
lead 

Curves of Iq, e^, ij, cos d, plotted in Fig. 86. 

252 ENGINEERING MATHEMATICS. 

2. 90 Per Cent Power-Factor, Lag. 


cos ^ = 0.9; sin^ = \/l-0.92 = 0.436; 
/o = ^o(cos d+jsin ^)=2o(0.9 +0.436/); 

j&i = (0.919- 0.036j>o + (56.8- 131.8y) (0.9 +0.436j)^ 

= (0.919-0.036f)eo + (108.5-93.8j>'o = A+5'; 
7i = (0.919-0.036f)(0.9+0.436y)io- (0.0144 + 1.168j>ol0-3 
= (0.843 +0.366y)io- (0.0144 + 1.168j>olO-3 = C'-D, 

and now the table is calculated in the same manner as under 1. 
Then corresponding tables are calculated, in the same 
manner, for power-factor, =0.8 and =0.7, respectively, lag, 
and for power-factor =0.9, 0.8, 0.7, lead; that is, for 

cos ^+y sin 6' = 0.8+0.6y; 
0.7+0.714/; 
0.9-0.436/; 
0.8-0.6/: 
0.7-0.714/. 

Then curves are plotted for ail seven values of power-factor, 
from 0.7 lag to 0.7 lead. 

From these curves, for a number of values of io, for instance, 
to = 20, 40, 60, 80, 100, numerical values of ii, eo, cos d, are 
taken, and plotted as curves, which, for the same voltage 
ei = 60 at the step-up end, give ii, eo, and cos d, for the same 
value to, that is, give the regulation of the line at constant 
current output for varying power-factor. 

b. Accuracy of Calculation. 

162. Not all engineering calculations require the same 
degree of accuracy. When calculating the efficiency of a large 
alternator it may be of importance to detcTmine whether it is 
97.7 or 97.8 per cent, that is, an accuracy within one-tenth 
per cent may be required; in other cases, as for instance, 
when estimating the voltage which may be produced in an 
electric circuit by a line disturbance, it may be sufficient to 


NUMERICAL CALCULATIONS. 


253 


determine whether this voltage would be hmited to double 
the rxormal circuit voltage, or whether it might be 5 or 10 
times the normal voltage. 

In general; according to the degree of accuracy, engineering 
calculations may be roughly divided into three classes : 

(a) Estimation of the magnitude of an effect; that is, 
determining approximate numerical values within 25, 50, or 
100 per cent. Very frequently such very rough approximation 
is sufficient, and is all that can be expected or calculated. 


kv. 

^^ 

■-- 

Co 

. 

65 

ei 

^^ 

y 

y 

'^^'^ 

> 

y 

y 

- 

ii^ 

^ 

^ 

^ 

-"^ 

< 

/ 

^1 

n^> 

/ 

/ 

J 

/ 

/ 

/ 

/ 

/ 

/ 

2 

3 

4 

3 

6 

b 

8 

3 

1 

X) 

1^ 

a. 

e 


■120 


1001.00 


80 0.-80 


0.40 


0.20 


^ 0 


Fig. 86. Transmission Line Characteristics. 


For instance, when investigating the short-circuit current of an 
electric generating system, it is of importance to know whether 
this current is 3 or 4 times normal current, or whether it is 
40 to 50 times normal current, but it is immaterial whether 
it is 45 to 46 or 50 times normal. In studying lightning 
phenomena, and, in general, abnormal voltages in electric 
systems, calculating the discharge capacity of lightning arres- 
ters, etc., the magnitude of the quantity is often sufficient. In 


254 ^ ENGINEERING MATHEMATICS. 

calculating the critical speed of turbine alternators, or the 
natural period of oscillation of synchronous machines, the 
same applies, since it is of importance only to see that these 
speeds are sufficiently^ remote from the normal operating speed 
to give no trouble in operation. 

(b) Approximate calculation, requiring an accuracy of one 
or a few per cent only; a large part of engineering calcu- 
lations fall in this class, especially calculations in the realm of 
design. Although, frequently, a higher accuracy could be 
reached in the calculation proper, it would be of no value, 
since the data on which the calculations are based are sus- 
ceptible to variations beyond control, due to variation in the 
material, in the mechanical dimensions, etc. 

Thus, for instance, the exciting current of induction motors 
may vary by several per cent, due to variations of the length 
of air gap, so small as to be beyond the limits of constructive 
accuracy, and a calculation exact to a fraction of one per cent, 
while theoretically possible, thus would be practically useless, 
The calculation of the ampere-turns required for the shunt 
field excitation, or for the series field of a direct-current 
generator needs only moderate exactness, as variations in the 
magnetic material, in the speed regulation of the driving 
power, etc., produce differences amounting to several per 
cent. 

(c) Exact engineering calculations, as, for instance, the 
calculations of the efficiency of apparatus, the regulation of 
transformers, the characteristic curves of induction motors, 
etc. These are determined with an accuracy frequently amount- 
ing to one-tenth of one per cent and even greater. 

Even for most exact engineering calculations, the accuracy 
of the slide rule is usually sufficient, if intelligently used, that 
is, used so as to get the greatest accuracy. Thus, in dividing, 
for instance, 297 by 283 by the slide rule, the proper way is 
to divide 297-283 = 14 by 283, and to add the result to 1. 
This gives a greater accuracy than direct division. For accu- 
rate calculations, preferably the glass slide should not be used, 
but the result interpolated by the eye. 

163. While the calculations are unsatisfactory, if not carried 
out with the degree of exactness which is feasible and desirable, 
it is equally wrong to give numerical values with a number of 


NUMERICAL CALCULATIONS. 255 

ciphers greater than the method or the purpose of the calcula- 
tion warrants. For instance, if in the design of a direct-current 
generator, the calculated field ampere-turns are given as 9738, 
such a numerical value destroys the confidence in the work of 
the calculator or designer, as it implies an accuracy greater 
than possible, and thereby shows a lack of judgment. 

The number of ciphers in which the result of calculation is 
given should signify the exactness, In this respect two 
systems are in use: 

(a) Numerical values are given with one more decimal 
than warranted by the probable error of the result; that is, 
the decimal before the last is correct, but the last decimal may 
be wrong by several units. This method is usually employed 
in astronomy, physics, etc. 

(6) Numerical values are given with as many decimals as 
the accuracy of the calculation warrants; that is, the last 
decimal is probably correct within half a unit. For instance, 
an efficiency of 86 per cent means an efficiency between 85.5 
and 86.5 per cent; an efficiency of 97.3 per cent means an 
efficiency between 97.25 and 97.35 per cent, etc. This system 
is generally used in engineering calculations. To get accuracy 
of the last decimal of the result, the calculations then must 
be carried out for one more decimal than given in the result. 
For instance, when calculating the efficiency by adding the 
various percentages of losses, data like the following may be 
given : 

Core loss 2.73 per cent 

i^r 1.06 '' 

Friction 0.93 " 

Total 4.72 

Efficiency 100-4.72 = 95.38 

Approximately 95.4 " 

It is obvious that throughout the same calculation the 
same degree of accuracy must be observed. 
It follows herefrom that the values : 

2i; 2.5; 2.50; 2.500, 


256 ENGINEERING MATHEMATICS. 

while mathematically equal, are not equal in their meaning as 
an engineering result : 

2.5 means between 2.45 and 2.55; 
2.50 means between 2.495 and 2.505; 
2.500 means between 2.4995 and 2.5005; 

while 2i gives no clue to the accuracy of the value. 

Thus it is not permissible to add zeros, or drop, zeros at 
the end of numerical values, nor is it permissible, for instance, 
to replace fractions as 1/16 by 0.0625, without changing the 
meaning of the numerical value, as regards its accuracy. 
This is not always realized, and especially in the reduction of 
common fractions to decimals an unjustified laxness exists 
which impairs the reliability of the results. For instance, if 
in an arc lamp the arc length, for which the mechanism is 
adjusted, is stated to be 0.8125 inch, such a statement is 
ridiculous, as no arc lamp mechanism can control for one-tenth 
as great an accuracy as implied in this numerical value: the 
value is an unjustified translation from 13/16 inch. 

The principle thus should be adhered to, that all calcula- 
tions are carried out for one decimal more than the exactness 
required or feasible, and in the result the last decimal dropped; 
that is, the result given so that the last decimal is probably 
correct within half a unit. 

c. Intelligibility of Engineering Data. 

164. In engineering calculations the value of the results 
mainly depends on the information derived from them, that is, 
on their intelligibility. To make the numerical results and 
their meaning as intelligible as possible, it thus is desirable, 
whenever a series of values are calculated, to carefully arrange 
them in tables and plot them in a curve or in cur^^s. The 
latter is necessary, since for most engineers the plotted curve 
gives a much better conception of the shape. and the variation 
of a quantity than numerical tables. 

Even where only a single point is required, as the core 
loss at full load, or the excitation of an electric generator at 
rated voltage, it is generally preferable to calculate a few 


NUMERICAL CALCULATIONS. 


257 


■■ 

Volts 

— 


100 

0 

2 

0 

4 

0 

6 

0 

8 

1 

0 

Fig. 87. Compounding Curve. 


points near the desired value, so as to get at least a short piece 
of curve including the desired point. 

The main advantage, and foremost purpose of curve plotting 
thus is to show the shape of the function, and thereby give 
a clearer conception of it ; 
but for recording numerical 
values, and deriving numer- 
ical values from it, the plotted 
curve is inferior to the table, 
due to the limited accuracy 
possible in a plotted curve, 
and the further inaccuracy 
resulting when drawing a 
curve through the plotted cal- 
culated points. To some 
extent, the numerical values 
as taken from a plotted curve, 
depend on the particular 
kind of curve rule used in 
plotting the curve. 

In general, curves are used for two different purposes, and 
on the purpose for which the curve is plotted, should depend 
the method of plotting, as the scale, the zero values, etc. 

When curves are used to 
illustrate the shape of the 
function, so as to show how 
much and in what manner a 
quantity varies as function 
of another, large divisions of 
inconspicuous cross-section- 
ing are desirable, but it is 
-49o| essential that the cross- 
sectioning should extend to 
the zero values of the func- 
tion, even if the numerical 
values do not extend so 
far, since otherwise a wrong 
impression would be con- 
ferred. As illustrations are plotted in Figs. 87 and 88, the 
compounding curve of a direct-current generator. The arrange- 


V 

olts 
-550 

^ 

■^ 

,^ 

^ 

y 

y 

JLXt\ 

/ 

0 

2 

0 

i 

0 

6 

0 

8 

1 

0 • 

Fig. 88. Compounding Curve. 


258 


ENGINEERING MATHEMATICS. 


ment in Fig. 87 is correct ; it shows the relative variation 
of voltage as function of the load. Fig. 88, in which the 
cross-sectioning does not begin at the scale zero, confers the 


— 

___ 

__^ 

-- 

/^ 

^ 

/ 

/ 

9. 

; 

/ 

c 

K 

1 

3 

2 

> 

3 

) 

* 

) 

5 

3 

6 

3 

7 

D 

Fig. 89. Curve Plotted to show Characteristic Shape. 


Fig. 90. Curve Plotted for Use as De.sign Data. 


wrong impression that the variation of voltage is far greater 
than it really is. 

When curves are used to record numerical values and 
derive them from the curve, as, for instance, is connnonly the 


NUMERICAL CALCULATIONS. 


259 


case with magnetization curves, it is unnecessary to have the zero 
of the function coincide with the zero of the cross-sectioning, but 
rather preferable not to have it so, if thereby a better scale of 
the curve can be secured. It is desirable, however, to use suffi- 
ciently small cross-sectioning to make it possible to take 
numerical values from the curve with good accuracy. This is 
illustrated by Figs. 89 and 90. Both show the magnetic charac- 
teristic of soft steel, for the range above (B = 8000, in which it is 
usually employed. Fig. 89 shows the proper way of plotting 
for showing the shape of the function, Fig. 90 the proper way of 
plotting for use of the curve to derive numerical values therefrom. 


\ 

V 

\, 

\ 

\ 

I 

\ 

\ 

^! 

\ 

\, 

\ 

k\ 

\ 

\ 

^ 

s 

>s. 

^ 

X 

~^, 

III 

^ 

-- 

'~~ 

~ 

Fig. 91. Same Function Plotted to Different Scales; I is correct. 

165. Curves should be plotted in such a manner as to show 
the quantity which they represent, and its variation, as well as 
possible. Two features are desirable herefor: 

1. To use such a scale that the average slope of the curve, 
or at least of the more important part of it, does not differ 
much from 45 deg. Hereby variations of curvature are best 
shown. To illustrate this, the exponential function y = e~'^ is 
plotted in three different scales, as curves I, II, III, in Fig. 91. 
Curve I has the proper scale. 

2. To use such a scale, that the total range of ordinates is 
not much different from the total range of abscissas. Thus 
when plotting the power-factor of an induction motor, in 
Fig. 92, curve I is preferable to curves II or III. 


260 


ENGINEERING MATHEMATICS, 


These two requirements frequently are at variance with 
each other, and then a compromise has to be made between 
them, that is, such a scale chosen that the total ranges of the 
two coordinates do not differ much, and at the same time 
the average slope of the curve is not far from 45 deg. This 
usually leads to a somewhat rectangular area covered by the 
curve, as shown, for instance, by curve I, in Fig. 91. 

In curve plotting, a scale should be used which is easily 
read. Hence, only full scale, double scale, and half scale 
should be used. Triple scale and one-third scale are practically 
unreadable, and should therefore never be used. Quadruple 


7 

^ 

"^ 

^ 

T- 

^ 

/ 

/ 

/ 

y' 

/ 

/ 

/ 

1 

/ 

/ 

III 

^ 

— 

r 

^ 

^ 

/ 

^ 

Y 

/ 

Fig. 92. Same Function Plotted to Different Scales; I is Correct. 


scale and quarter scale are difficult to read and therefore unde- 
sirable, and are generally unnecessary, since quadruple scale 
is not much different from half scale with a ten times smaller 
unit, and quarter scale not much different from double scale 
of a ten times larger unit. 

i66. Any engineering calculation on which it is worth 
while to devote any time, is worth being recorded wdth suffi- 
cient completeness to be generally intelligible. Very often in 
making calculations the data on which the calculation is based, 
the subject and the purpose of the calculation are given incom- 
pletely or not at all, since they are familiar to the calculator at 
the time of calculation. The calculation thus would be unin- 


NUMERICAL CALCULATIONS. 261 

telligible to any other engineer, and usually becomes unintelli- 
gible even to the calculator in a few weeks. 

In addition to the name and the date, all calculations should 
be accompanied by a complete record of the object and purpose 
of the calculation, the apparatus, the assumptions made, the 
data used, reference to other calculations or data employed, 
etc., in shorty they should include all the information required 
to make the calculation intelligible to another engineer without 
further information besides that contained in the calculations, 
or in the references given therein. The small amount of time 
and work required to do this is negligible compared with the 
increased utility of the calcuktion. 

Tables and curves belonging to the calculation should in 
the same way be completely identified with it and contain 
sufficient data to be intelligible. 

d. Reliability of Numerical Calculations. 

167. The most important and essential requirement of 
numerical engineering calculations is their absolute reliability. 
When making a calculation, the most brilliant ability, theo- 
retical knowledge and practical experience of an engineer are 
made useless, and even worse than useless, by a single error in 
an important calculation. 

Reliability of the numerical calculation is of vastly greater 
importance in engineering than in any other field. In pure 
mathematics an error in the numerical calculation of an 
example which illustrates a general proposition, does not detract 
from the interest and value of the latter, which is the main 
purpose; in physics, the general law which is the subject of 
the' investigation remains true, and the investigation of interest 
and use, even if in the numerical illustration of the law an 
error is made. With the most brilliant engineering design, 
however, if in the numerical calculation of a single structural 
member an error has been made, and its strength thereby calcu- 
lated wrong, the rotor of the machine flies to pieces by centrifugal 
forces, or the bridge collapses, and with it the reputation of the 
engineer. The essential difference between engineering and 
purely scientific caclulations is the rapid check on the correct- 
ness of the calculation, which is usually afforded by the per- 


262 ENGINEERING MATHEMATICS. 

forniance of the calculated structure — but too late to correct 
errors. 

Thus rapidity of calculation, while by itself useful, is of no 
value whatever compared with reliability — ^that is, correct- 
ness. 

One of the first and most important requirements to secure 
reliability is neatness and care in the execution of the calcula- 
tion. If the calculation is made on any kind of a sheet of 
paper, with lead pencil, with frequent striking out and correct- 
ing of figures, etc., it is practically hopeless to expect correct 
results from any more extensive calculations. Thus the work 
should be done with pen and ink, on white ruled paper; if 
changes have to be made, they should preferably be made by 
erasing, and not by striking out. In general, the appearance of 
the work is one of the best indications of its reUability. The 
arrangement in tabular form, where a series of values are calcu- 
lated, offers considerable assistance in improving the reliability. 

i68. Essential in all extensive calculations is a complete 
system of checking the results, to insure correctness. 

One way is to have the same calculation made independently 
by two different calculators, and then compare the results. 
Another way is to have a few points of the calculation checked 
by somebody else. Neither way is satisfactory, as it is not 
always possible for an engineer to have the assistance of another 
engineer to check his work, and besides this, an engineer should 
and must be able to make numerical calculations so that he can 
absolutely rely on their correctness without somebody else 
assisting him. 

In any more important calculations every operation thus 
should be performed twice, preferably in a different manner. 
Thus, when multiplying or dividing by the slide rule, the multi- 
plication or division should be repeated mentally, approxi- 
mately, as check; when adding a column of figures, it should be 
added first downward, then as check upward, etc. 

Where an exact calculation is requked, first the magnitude 
of the quantity should be estimated, if not already known, 
then an approximate calculation made, which can frequently 
be done mentally, and then the exact calculation; or, inversely, 
after the exact calculation, the result may be checked by an 
approximate mental calculation. 


NUMERICAL CALCULATIONS. 2G3 

Where a series of values is to be calculated, it is advisable 
first to calculate a few individual points, and then, entirely 
independently, calculate in tabular form the series of values, 
and then use the previously calculated values as check. Or, 
inversely, after calculating the series of values a few points 
should independently be calculated as check. 

When a series of values is calculated, it is usually easier to 
secure rehability than when calculating a single value, since 
in the former case the different values check each other. There- 
fore it is always advisable to calculate a number of values, 
that is, a short curve branch, even if only a single point is 
required. After calculating a series of values, they are plotted 
as a curve to see whether they give a smooth curve. If the 
entire curve is irregular, the calculation should be thrown away, 
and the entire work done anew, and if this happens repeatedly 
with the same calculator, the calculator is advised to find 
another position more in agreement with his mental capacity. 
If a single point of the curve appears irregular, this points to 
an error in its calculation, and the calculation of the point is 
checked; it the error is not found, this point is calculated 
entirely separately, since it is much more difficult to find an 
error which has been made than it is to avoid making an 
error. 

169. Some of the most frequent numerical errors are : 

1. The decimal error, that is, a misplaced decimal point. 
This should not be possible in the final result, since the magni- 
tude of the latter should by judgment or approximate calcula- 
tion be known sufficiently to exclude a mistake by a factor 10. 
However, under a square root or higher root, in the exponent 
of a decreasing exponential function, etc., a decimal error may 
occur without affecting the result so much as to be immediately 
noticed. The same is the case if the decimal error occurs in a 
term which is relatively small compared with the other terms, 
and thereby does not affect the result very much. For instance, 
in the calculation of the induction motor characteristics, the 
quantity ri^+s^xi^ appears, and for small values of the sHp s, 
the second term s^xi^ is small compared with ri^, so that a 
decimal error in it would affect the total value sufficiently to 
make it seriously wrong, but not sufficiently to be obvious. 

2. Omission of the factor or divisor 2. 


264 ENGINEERING MATHEMATICS. 

3. Error in the sign, that is, using the plus sign instead of 
the minus sign, and inversely. Here again, the danger is 
especially great, if the quantity on which the wrong sign is 
used combines with a larger quantity, and so does not affect 
the result sufl^ciently to become obvious. 

4. Omitting entire terms of smaller magnitude, etc. 


APPENDIX A. 

NOTES ON THE THEORY OF FUNCTIONS. 

A. General Functions. 

170. The most general algebraic expression of powers of 
X and y, 

F(x,y) = (aoo+aoiX-\-ao2X^ + . . .) +(^10 + «i 1:^^ + ^112.^^ + . . .)2/ 
+ {a2o+a2ix + a22X^ + . . .)2/^ + - • • 
+ {ano+anix+an2X^ + . . .)y''-0, . . . . (1) 

is the implicit analytic function. It relates y and x so that to 
every value of x there correspond n values of y, and to every 
value of y there correspond m values of x, if m is the exponent 
of the highest power of a: in (1). 

Assuming expression (1) solved for y (which usually cannot 
be carried out in final form, as it requires the solution of an 
equation of the r^th order in y, with coefficients which are 
expressions of x), the explicit analytic function, 

y-m, (2) 

is obtained. Inversely, solving the implicit function (1) for 
X, that is, from the explicit function (2), expressing x as 
function of y, gives the reverse function of (2); that is 

x=/i(2/) (3) 

In the general algebraic function, in its implicit form (1), 
or the explicit form (2), or the reverse function (3), x and y 
are assumed as general numbers; that is, as complex quan- 
tities; thus, 

X = Xi+jX2] \ 

(4) 

y=yi+jy2, J 

and likewise are the coefficients ooo, aoi • • . cinn'. 

265 


266 ENGINEERING MATHEMATICS. 

If all the coefficients a are real, and x is real, the corre- 
sponding n values of y are either real, or pairs of conjugate 
complex imaginary quantities: 2/1 +^2/2 and y\ — jy2. 

171. For 71 = 1, the implicit function (1), solved for y, gives 
the rational function, 

aoo+aoiX + ao2y^ + . . . , . 

and if in this function (5) the denominator contains no x, the 
integer function, 

y = ai)+aix+a2X^-\ . . .-\-amX'^, , . . . (6) 

is obtained. 

For n = 2, the implicit function (1) can be solved for 1/ as a 
quadratic equation, and thereby gives 

-{aio+anX + ai-2X^ + ...)± 

that is, the explicit form (2) of equation (1) contains in this 
case a square root. 

For n>2, the explicit form y=f{x) either becomes very 
complicated, for n = 3 and n = 4, or cannot be produced in 
finite form, as it requires the solution of an equation of more 
than the fourth order. Nevertheless, y is still a function of 
x, and can as such be calculated by approximation, etc. 

To find the value yi, which by function (1) corresponds to 
x^x\, Taylor's theorem offers a rapid approximation. Sub- 
stituting xi in function (1) gives an expression which is of 
the nth order in y, thus: F(xiy), and the problem now is to 
find a value y\, which makes F(xi,yi) =0. 

However, 

X r./ X ,dF(xi,y) h^d^F{xi,7j) 
Fix,, yi)==F(x,, y) +^— ^- +j2 ^y ' +- ^ , • i^) 

where h = yi — y is the difference between the correct value t/i 
and any chosen value y. 


APPENDIX A, 


267 


Neglecting the higher orders of the small quantity h, in 
(8), and considering that F(xi,yi) =0, gives 


h = 


F{x,,y) 

dF{x^,yy 

dy 


(9) 


and herefrom is obtained yi=y-\-h, as first approximation. 
Using this value of i/i as y in (9) gives a second approximation, 
which usually is sufficiently close. 

172. New functions are defined by the integrals of the 
analytic functions (1) or (2), and by their reverse functions. 
They are called Ahelian integrals and Abelian functions. 

Thus in the most general case (1), the explicit function 
corresponding to (1) being 


the integral, 


z= i f{x)dx, 


(2) 


then is the general Abelian integral, and its reverse function, 

x = <l>{z), 

the general Abelian function. 

(a) In the case, n = l, function (2) gives the rational function 
(5), and its special case, the integer function (6). 

Function (6) can be integrated by powers of x. (5) can be 
resolved into partial fractions, and thereby leads to integrals 
of the following forms : 

(1) I xmdx] 

(2) P-; 
J x-a' 


(4) 


r dx 

J 1 +^' 


(10) 


268 ENGINEERING MATHEMATICS. 

Integrals (10), (1), and (3) integrated give rational functions, 
(10), (2) gives the logarithmic function log (x—a), and (10), (4) 
the arc function arc tan x. 

As the arc functions are logarithmic functions with complex 
imaginary argument, this case of the integral of the rational 
function thus leads to the logarithmic function, or the loga- 
rithmic integral, which in its simplest form is 

z-^l -^ = logx, ....... (11) 

and gives as its reverse function the exponential function, 

X=£^ (12) 

It is expressed by the infinite series, 

^2 ^3 ^ 

e^=l+e+_+_+jj+ . (13) 

as seen in Chapter II, paragraph 53. 

173. b. In the case, n=2, function (2) appears as the expres- 
sion (7), which contams a square root of some power of x. It.s 
first part is a rational function, and as such has already been 
discussed in a. There remains thus the integral function, 

/Vbo+hiX + b2X^-\-. . .+6p.i:^^ 
■ ■ 5-^ dx. . . . (14) 
Co+ClX-{-C2X^-\-. . . 

This expression (14) leads to a series of important functions. 
(1) Forp = lor2, 

r Vbo+biX + b2X^ ^ ^_. 

Z= I ; : ^- dx (15) 

J Co-\-CiX+C2X^-\-. . • 

By substitution, resolution into partial fractions, and 
separation of rational functions, this integral (11) can be 
reduced to the standard form, 

dx 
In the case of the minus sign, this gives 


'-jr^^^ ^^^^ 


/dx 


z= I — = arc sin x, (17) 


APPENDIX A. 


2m 


and as reverse functions thereof, there are obtained the trigo- 
notrteiric functions. 

x = sin z, 1 

(IS) 

Vl — X^ = COS z. J 

In the case of the plus sign, integral (16) gives 


= — log{ Vl+x^— xj =arc sinh x, . 

Vl+X2 

and reverse functions thereof are the hyperbolic functions, 

c + 2— e-Z 1 


(19) 


X 


vTTx2= 


2 


sinh^;; 


= cosh z. 


(20) 


The trigonometric functions are expressed by the series : 


y3 9;5 y7 

sin2 = 2-Tj + l^-|y + .: . ; 

^2 ^4 ^ 
COS^=l-^+^-jg+..., 


(21) 


as seen in Chapter II, paragraph 58. 

The hyperbolic functions, by substituting for £+« and e' 
the series (13), can be expressed by the series: 


z ?^ z"^ 
sinh z = z+77^+^-\-T=- + . . . ; 
|3 |o \!_ 

z^ ^ ifi 
coshe=l+i2+jj+jg+.... 


(22) 


174. In the next case, p=3 or 4, 

/Vfeo +61X +620:2 +63.^^ + ?>4^ 


Co + CiX+C2X2 + 


dx, 


(23) 


already leads beyond the elementary functions, that is, (23) 
cannot be integrated by rational, logarithmic or arc functions, 


270 


ENGINEERING MATHEMATICS. 


but gives a new class of functions; the elliptic integrals, and 
their reverse functions, the elliptic functions, so called, because 
they bear to the eUipse a relation similar to that, which the 
trigonometric functions bear to the circle and the hyperbolic 
functions to the equilateral hyperbola. 

The integral (23) can be resolved into elementary functions, 
and the three classes of elliptic integrals : 


dx 


vx{i-x){i-cHy 

xdx 

Vx{i-x){i-cHy 

dx 


h)Vx(l-x)(l-c^x) 


(24) 


(These three classes of integrals may be expressed in several 
different forms.) 

The reverse functions of the elliptic integrals are given by 
the elliptic functions : 

Vx = sin am(u, c); 


V 1 — x = cos am{u, c) ; 
Vl —c^x = Jam{u, c); 


(25) 


known, respectively, as sine-amplitude, cosine-amplitude, delta- 
amplitude. 

Elliptic functions are in some respects similar to trigo- 
nometric functions, as is seen, but they are more general, 
depending, as they do, not only on the variable x, but also on 
the constant c. They have the interesting property of being 
doubly periodic. The trigonometric functions are periodic, with 
the periodicity 2;r, that is, repeat the same values after every 
change of the angle by 2;r. The elliptic functions have two 
periods pi and p2, that is, 


sin am{u +npi +w,p2, c) =sin am{u, c), etc.; 


(26) 


hence, increasing the variable u by any multiple of either 
period pi and p2, repeats the same values. 


APPENDIX A, 


271 


The two periods are given by the equations, 

dx 


Vi 


-X' 


2\^x{\-x){l-cHy 


dx 


(27) 


2\/x{l-x){l-c^x) ] 

175. Elliptic functions can be expressed as ratios of two 
infinite series, and these series, which form the numerator and 
the denominator of the elliptic function, are called theta func- 
tions and expressed by the symbol 6, thus 


sinaw(u, c)=-^ /-..A' 
COS am(u, c) =y\-i _ 2 


».© 


Jam{u, c) == -yll — c^- 


(28) 


'-is)' 

and the four 6 functions may be expressed by the series: 
^o(^) = 1 —2q cos 2^ +2^^ cos 4a: —2q^ cos 6a; H — . . . ; 

25 

di(x) =2gi/4 sin x -2g9/4 sin 3x +2g4 sin 5a; - + . . . ; 

25 

^2^=2(2^/4 cos a; +2^9/4 COS 3a: +2^ 4 cos5a: + ... ; 
(93(x) = l+2(?cos2a:+2^cos4a:+259cos6a: + . . . , 


(29) 


where 


1 . P2 

q=s9- and a = '\n^—. 


(30) 


In the case of integral function (14), where p>4, similar 
integrals and their reverse functions appear, more complex 


272 ENGINEERING MATHEMATICS. 

than the elliptic functions, and of a greater number of periodici- 
ties. They are called hyperelliptic integrals and hyperelliptic 
functions, and the latter are again expressed by means of auxil- 
iary^ functions, the hyperelliptic 6 functions. 

176. Many problems of physics and of engineering lead to 
elliptic functions, and these functions thus are of considerable^ 
importance. For instance, the motion of the pendulum is 
expressed by elliptic functions of time, and its period thereby 
is a function of the amplitude, increasing with increasing ampli- 
tude: that is, in the so-called "second pendulum," the time of 
one swing is not constant and equal to one second, but only 
approximately so. This approximation is very close, as long 
as the amplitude of the swing is very small and constant, but 
if the amplitude of the swing of the pendulum varies and 
reaches large values, the time of the swing, or the period ot 
the pendulum, can no longer be assumed as constant and an 
exact calculation of the motion of the pendulum by elliptic 
functions becomes necessary. 

In electrical engineering, one has frequently to deal w^ith 
oscillations similar to those of the pendulum, for instance, 
in the hunting or surging of synchronous machines. In 
general, the frequency of oscillation is assumed as constant, 
but where, as in cumulative hunting of synchronous machines, 
the amplitude of the swing reaches large values, an appreciable 
change of the period must be expected, and where the hunting 
is a resonance effect with some other periodic motion, as the 
engine rotation, the change of frequency with increase of 
amplitude of the oscillation breaks the complete resonance and 
thereby tends to limit the amplitude of the swing. 

177. As example of the application of elliptic integrals, may 
be considered the determination of the length of the arc of an 
ellipse. 

Let the ellipse of equation 

5-^4=1' (31) 

be represented in Fig. 93, with the circumscribed circle, 

jc2 + y2 = a2 (32) 


APPENDIX A. 


273 


To every point P = x, y of the ellipse then corresponds a 
point P\ = x, y\ on the circle, which has the same abscissa x, 
and an angle d^AOP\. 

The arc of the ellipse, from A to P, then is given by the 
integral, 

L = a \ — , ^ ^ =zi .... (33) 

where 


z){l-c'z) 

z = ^m^ d=(-] and c 
is the eccentricity of the ellipse. 


Va^ — b^ 


(34) 


Fig. 93. Rectification of Ellipse. 

Thus the problem leads to an elliptic integral of the first 
and of the second class. 

For more complete discussion of the elliptic integrals and 
the elliptic functions, reierence must be made to the text-books 
of mathematics. 

B. Special Functions. 

178. Numerous special functions have been derived by the 
exigencies of mathematical problems, mainly of astronomy, but 
in the latter decades also of physics and of engineering. Some 
of them have already been discussed as special cases of the 
general Abelian integral and its reverse function, as the expo- 
nential, trigonometric, hyperbolic, etc., functions. 


274 ENGINEERING MATHEMATICS. 

Functions may be represented by an infinite series of terms; 
that is, as a ^um of an infinite number of terms, which pro- 
gressively decrease, that is, approach zero. The denotation of 
the terms is commonly represented by the summation sign 2. 

Thus the exponential functions may be written, when 
defining, 

|0 = 1; |n = lX2X3X4X. . .Xn, 
as 

e- = l+x+;^*+j^+. ..==S»;--, .... (35) 

I— l_. ^ l__ 

which means, that terms ,— are to be added for all values of n 

from n = 0 to n = oc . 

The trigonometric and hyperbolic functions may be written 
in the form : 

sina:-x--~+T^-j;^ + . . . = Sn(-i)n • . (36) 


j3 |5 |7 0 ' ' |2n + l 


.y2 7^ /y.6 oo ^2n 

cosx=l-|^+ij-g + ... = 2»r-l)ni^; . . (37) 


x^ x^ x"^ ^ X^""*"^ 


sinhx-a:+j^+y^+yy+. . . = 2n-^— -^; . . . (38) 


eosha. = l+g+^+i^ + ... = Snj^ (39) 

Functions also may be expressed by a series of factors; 
that is, as a product of an infinite series of factors, which pro- 
gressively approach unity. The product series is commonly 
represented by the symbol JJ. 

Thus, for instance, the sine function can be expressed in the 
form, 

sinx=x(l-5)(l-£,)(l-£)... = xt(l-i). (40) 

179. Integration of known functions frequently leads to new 
functions. Thus from the general algebraic functions were 


APPENDIX A. 275 

derived the Abelian functions. In physics and in engineering, 
integration of special functions in this manner frequently leads 
to new special functions. 

For instance, in the study of the propagation through space, 
of the magnetic field of a conductor, in wireless telegraphy, 
lightning protection, etc., we get new functions. If ^=/(0 
is the current in the conductor, as function of the time t, at a 
distance x from the conductor the magnetic field lags by the 

X 

time ti = -, where S is the speed of propagation (velocity of 

light). Since the field intensity decreases inversely propor- 
tional to the distance x, it thus is proportional to 


y= — - — ; (41) 

and the total magnetic flux then is / 
2= j ydx 

A'-l) 

-j^T^'i' <*2) 

If the current is an alternating current, that is, f (t) a 
trigonometric function of time, equation (42) leads to the 
functions, 


/sin ; 

X 

"J 


dx: 


cos X ^ 
-ax. 


(43) 


If the current is a dh-ect current, rising as exponential 
function of the time, equation (42) leads to the function, 


/s'^dx 
--•••' (44) 


X 


27G 


ENGINEERING MATHEMATICS. 


Substituting in (43) and (44), for sin x, cos a:, £^ their 
infinite series (21) and (13), and then integrating, gives the 
following : 


sin X x^ x^ x^ 

X '^*^^^~3]3"^5J5"7|7^~ 


J sin X 

r 


cosa; x^ X* x^ 

~rfx = logx-2J2+4J4-gje 


(15) 


^dx = logx+x+2|+3|3+... 

For further discussion of these functions see 'Theory and 
Calculation of Transient Electric Phenomena and Oscillations," 
Section III, Chapter VIII. 

i8o. If y=f{x) is a function of x, and z= | f {x)dx = 6{x) 
its integral, the definite integral, ^^ \ f{^)dx, is no longer 

Ja 

a function of x but a constant, 

For instance, if y^c{x — nY, then 

c{x—n)^ 


0= I c{x—n 


)Hx = 


and the definite integral is 


=r^^'- 


nYdx = -\{h — n)^—{a—n)^\. 


This definite integral does not contain x, but it contains 
all the constants of the function / {x), thus is a function of 
these constants c and n, as it varies with a variation of these 
constants. 

In this manner new functions may be derived by definite 
integrals. 

Thus, if 

y=f{x,u,v...) (46) 


is a function of x, containing the constants u, v , . , 


APPENDIX A. 277 

The definite integral, 

, . - . Z=rf(x,u,v...)dx, . .... (47) 

is not .a function of x, but still is a function o( u, v . . . , and 
may be a new function. 

i8i. For instance, let " 

y^s-^x""-^; (48) 

then the integral, 

/(u)= n--x^-Mx, (49) 

is a new function of u, called the gamma function. 

Some properties of this function may be derived by partial 
integration, thus : 

r(u + l)=ur(u); (50) 

if n is an integer number, 

r(u) = (u-l){u-2)...(u-n)r(u-n), . . (51) 
and since 

r(i)=i, (52) 

if u is an integer number, then, 

r(u) = \u-h (53) 

C. Exponential, Trigonometric and Hyperbolic Functions. 

(a) Functions of Real Variables. 

182. The exponential, trigonometric, and hyperbolic func- 
tions are defined as the reverse functions of the integrals, 

a. u= j— =logx, (54) 

and: x=£« (55) 

...... (56) 


r dx 

h. u= I y ==arcsmx; 


278 ENGINEERING MATHEMATICS. 

and: x=8mu, (57) 

Vl-x^ = cosu, (58) 

/dx 

;^^^^===-log{Vr+^-xl; . . . . (59) 

and x= X — =sinhw; .... (60) 

Vl+x2= — =coshw (61) 

From (57) and (58) it follows that 

sm^u+cos^u = l (62) 

From (60) and (61) it follows that 

cos^/ii/ — sin 2/ii^ = l (63) 

Substituting ( — x) for x in (56), gives {—u) instead of u, 
and therefrom, 

sin (— w) = — sin 1^ (64) 

Substituting {—u) for u in (60), reverses the sign of x, 
that is, 

sinh ( — w) = — sinhii. ... (65) 

Substituting {—x) for x in (58) and (61), does not change 
the value of the square root, that is, 

cos ( — w)=cos w, (66) 

cosh {—u)= cosh u, (67) 

Which signifies that cos u and cosh u are even functions, while 
sin u and sinh u are odd functions. 

Adding and subtractijig (60) and (61), gives 

£±M = cosh w± sinh ?/ (68) 


APPENDIX A. 279 

(h) Functions of Imaginary Variables. 
183. Substituting, in (56) and (59), a: = —jy, thus y = jx, gives 

dx 


^^^'^ ^=/vfo^ (^^-^ ^=/ 


Vl+x^' 


a: = sinw; x=sinhi^ = 


\/l+x^ = cosu; vTTx2 = coshu = 


2 ' 


hence, y,,= J-^, hence, ju=j'^^; 

2/=sinhfu= ^5 ; 2/=sin/w; . . . (69) 


£JU _|_ g-JU 


V 1+2/^ = cosh /i^ = 2 5 vl — 2/2 = cos/i^; . . . (70) 

Resubstituting x in both 

sinh/u £jw-£-i« £" — £-" sinm ,^,, 

ic = smw = ^ — = — ?P ; a: = sinhi^ = — t: — = — :^—: (71) 

] 2? '- 2 J 


Vl — x2 = cos w = cosh ju Vi+x2 = cosht^ = 


£«+£-^ 


2 


=cos/w. . (72) 

Adding and subtracting, 

£^" = cos u±j sin w=cosh /w±sinh /i^ 
and £ ± « = cosh i* ± sinh u = cos /w T J sin jw. . . (73) 

(c) Functions of Complex Variables 

184. It is : 

£u±jt,= £^e±/t»=£u(cosi;±/smt;); . . . (74) 


280 ENGINEERING MATHEMATICS. 

sin (u i/iO =sin u cos ;v ±cos u sin jv 

= Sin w cosh V ± ^ cos w sinh v = — ^ — sin u ± ] — ^ — cos w 


cos(w ± jv) = cos It cos p^ sin w sin jv 

= cos u cosh ?; ^ /sin u sinh r = — ^ — cos u =F j — ^ — sin u ; 


(75) 


■ (76) 


sinh {u ± jv) = ^ = — ^ — cos v ± j — ^ — sin v 

= sinh u cos v±j cosh u sin v\ 


.U ff.— u 


^ 2 

= cosh u cos V ±y sinh ti sin v; 


cosh(2^ ± jv) = ~ = ^^ — '-^ — cos V ± j — ^ — sin v 


etc. 


(77) 


\ (78) 


(d) Relations. 

185. From the preceding equations it thus follows that the 
three functions, exponential, trigonometric, and hyperbolic, 
are so related to each other, that any one of them can be 
expressed by any other one, so- that when allowing imaginary 
and complex imaginary variables, one function is sufficient. 
As such, naturally, the exponential function would generally 
be chosen. 

Furthermore, it follows, that all functions with imaginary 
and complex imaginary variables can be reduced to functions 
of real variables by the use of only two of the three classes 
of functions. In this case, the exponential and the trigono- 
metric functions would usually be chosen. 

Since functions with complex imaginary variables can be 
resolved into functions with real variables, for their calculation 
tables of the functions of real variables are sufficient. 

The relations, by which any function can be expressed by 
any other, are calculated from the preceding paragraph, by 
the following equations : 


APPENDIX A. 


281 


f ±" = cosh u ±sinh u = cos fu ^F / sin fu; 
£'^^^' = coi>v± j sin V = cosh jv ± j sinh jv ; 
£"±/'' == £« (cos v±j sin i;), 

sinh ju £^""— £~^'" 


sni w 


2/ ' 


sin jv = j sinh r = / — ^ 

sin {u±jii) =sin i^ cosh ?? ±/ cos u sinh v 

= — ^ — sin u±j — - — cos u ; 


(a) 


(&) 


COS u = cosh ju 


cos p = cosh V 


£?M^ C-7U 


cos {u±jv) = COS u cosh i;=F / sjn 21 sinh 2; 

= — ^^ — COS 2iTJ- — 7^ — sin u; 


(e) 


sinh ti = 


sinh jv = j sin 2 


£"— £ " sin JU 
2 7 ' 


sinh {u±jv) =sinh u cos ?; ±/ cosh w sin v 

-£-" .£«+£-" . 

2 — cos vi; — 2 — ^^^ ^j 


£^— £ 


id) 


cosh w = 


£"+£-" 


cos ]U\ 


£?U -j- £-?v 

cosh jv = cos V = ^ — ; 

cosh (u ± jv) = cosh u cos v±j sinh u sin ?; 

£«-f£-W ffW_ £ — U 

= :^ cos v±j sin v. 


ie) 


282 ENGINEERING MATHEMATICS. 

And from (b) and (d), respectively (c) and (e), it follows that 


sinh {u + jv) = j sin {±v— ju) = ±j sin {v ± ju) ; 
cosh ('U±/i')=cos {v^^ju). 


} . c^ 


Tables of the exponential functions and their logarithms, 
and of the hyperbolic functions with real variables, are given 
in the following Appendix B. 


APPENDIX B. 

TWO TABLES OF EXPONENTIAL AND HYPERBOLIC 

FUNCTIONS. 

Table I. 


6 = 2.7183. 

log £ = 0.4343. 

X 

xio-» 

XlO-2 

xio-i 

XI 

1.0 

0.999 

0.990 

0.905 

0.368 

1.2 

1.4 
1.6 

1.8 


0.988 
0.986 
0.984 
0.982 

0.887 
0.869 
0.852 
0.835 

0.301 
0.247 
0.202 
0.165 

2.0 

0.998 

0.980 

0.819 

0.135 

2.5 
3.0 
3.5 
4.0 
4.5 

0.997 
0.996 

0.975 
0.970 
0.966 
0.961 
0.956 

0.779 
0.741 
0.705 
0.670 
0.638 

0.082 
0.050 
0.030 
0.018 
0.011 

5.0 

0.995 

0.951 

0.607 

0.007 

6 

7 
8 
9 

0.994 
0.993 
0.992 
0.991 

0.942 
0.932 
0.923 
0.914 

0.549 
0.497 
0.449 
0.407 

0.002 
0.001 
0.000 

10 

0.990 

0.905 

0.368 


283 


284 


ENGINEERING MATHEMATICS. 


Table IL 


EXPONENTIAL AND HYPERBOLIC FUNCTIONS. 

£ = 2.718282^2.7183, log £ = 0.4342945 ~ 0.4343. 

cosh x = h{£ + ^ + £-^\, sinhx = ^|£ + ^-£--^|. 


,, ! 

434 

435 

0 

0 

0 

0.1 

43 

43 

0.2 

87 

87 

0.3 

130 

130 

0.4 

174 

174 

0.5 

217 

217 

0.6 

261 

261 

0.7 

304 

304 

0.8, 

347 

348 

0.9 

391 

391 

1.0 

434 

435 

0 


0.001 
0.002 
0.003 
0.004 


0.005 


0.006 
0.007 
0.008 
0.009 


0.010 


0.012 
0.014 
0.016 
0.018 


0.020 


0.025 
0.030 
0.035 
0.040 
0.045 


0.050 


0.06 
0.07 
0.08 
0.09 


0.10 


0.12 
0.14 
0.16 
0.18 


logfH-x 


0.000434 
0.000869 
0.001303 
0.001737 


0.002171 


0.002606 
0 . 003040 
0.003474 
0.003909 


0.004343 


0.005212 
0.006080 
0.006949 
0.007817 


0.008686 


0.010857 
0.013029 
0.015200 
0.017372 
0.019543 


0.02171i 


0.026058 
0.030401 
0.034744 
LO. 039086 


0.043429 


0.052115 
0.060801 
0.069487 
0.078173 


0.20 0.086859 


Jlog 

£±^ 


434 
435 
434 
434 

434 

435 

434 
434 
435 

434 


log £~^ 


.999566 1 
.999131 


00100 
1.00200 
1.00301 
9.99826311.00401 


9.997829 1.00501 


9.997394 
9.996960 1 
9.996526 1 
9.996091 


9.995657 


.994788 
.993920 1 
.993051 
.992183 1 


9.991314 


9.989143 1 
9.986971 
9.984800 
9.982628 1 
9.98045' 


9.978285 1.05127 


(3942 1 


9.97 

9.969599 1 
9.9652.56 1 
9.960914 


9.956571 


9.947885 
9.939199 
9.930513 1 
9.921827 1 


£ + X 


0.99900 1 
0.99800 1 
0.99700 1 
0.99601 


1 . 00602 
00702 
00803 

1.00904 


1.01005 


1.01207 
01410 

1.01613 
01816 


1.02020 


02531 

1.03046 

1.03562 

.04081 

1.04603 


.06184 

.07251 

.08329 

1.09417 


1.10516 


1 . 12750 

1 . 15027 

17351 

19721 


0.99501 


0.9940: 
0.99302 1 
0.99203 1 
0.99104 1 


0.99005 1.00005 


0.9880' 
0.98610 1 
0.98413 1 
0.98216 1 


0.97531 


0.97045 1 
0.96561 1 
0.96079 1 
0.95600 1 


0.941 

0 . 9323911 

0.9231 

0.91393 


0.90484 


0.8869 
0.86936 
0.85214 
0.83527 


9.913141 1.22140 0.81873 1.02006 0.20134 0.20 


cosh X 


00000 

00000 

00000 

1.00001 


1.00001 


1.00002 
.00002 
.00003 
. 00004 


1.00007 
.00010 
.00013 
.00016 


0.98020 1.00020 


00031 
00046 
00062 
00080 
00102 


0.95123 1.00125 0.05003 


sinh 


0.00100 
0.00200 
0.00300 
0.00400 


0.00500 


0.00600 
0.00700 
0.00800 
0.00900 


0.01000 


0.01200 
0.01400 
0.01600 
0.01800 


0.02000 


0.02500 
0.03000 
0.03500 
0.04001 
0.04502 


6 1 


00180 0.06004 

00245 0.07006 

1. 00321; 0.08008 

1.00405 0.09011 


1.00500 0.10016 

i 


1.00721 0.12028 
1.00982 0.14046 
1.01283 0.16069 
1.01624 0.18097 


0 


0.001 
0.002 
0.003 
0.004 


0.005 


0.006 
0.007 
0.008 
0.009 


0.010 

0.012 
0.014 
0.016 
0.018 

0.020 


0.025 
0.030 
0.035 
0.040 
0.045 


0.050 


0.06 
0.07 
0.08 
0.09 


0 . 10 


0.12 
0.14 
0.16 
0.18 


£ + 0.001 = 1.001000494, f-o^O' = 0.99900049. 


APPENDIX B, 

Table II — Continued. 

EXPONENTIAL AND HYPERBOLIC FUNCTIONS. 


285 


X 

log e + ^ 

log £-^ 

£ + ^ 

£-^ 

cosh X 

sinh X 

X 

0.20 

0.086859 

9.913141 

1.22140 

0.81873 

1.02006 

0.20134 

0.20 

0.25 
0.30 
0.35 
0.40 
0.45 

0.108574 
0.130288 
0.152003 
0.173718 
0.195433 

9.891426 
9.869712 
9.847997 
9.826282 
9.804567 

1 . 28403 
1.34986 
1.41907 
1.49183 
1.56831 

0.77880 
0.74082 
0.70469 
0.67032 
0.63763 

1.03142 
1.04534 
1.06188 
1.08108 
1 . 10297 

0.25261 
0.30457 
0.35719 
0.41076 
0.46534 

0.25 
0.30 
0.35 
0.40 
0.45 

0.50 

0.217147 

9.782853 

1.64870 

0.60653 

1.12761 

0.52108 

0.50 

0.6 

0.7 
0.8 
0.9 

0.260577 
0.304006 
0.347436 
0.390865 

9.739423 
9.695994 
9.652564 
9.609135 

1.82212 
2.01375 
2.22554 
2.45960 

0.54881 
0.49659 
0.44933 
0.40657 

1 . 19546 
1.25517 
1.33744 
1.43309 

0.63666 

0.75858 
0.88811 
1.02657 

0.6 
0.7 
0.8 
0.9 

1.0 

0.434294 

9.565706 

2.71828 

0.36788 

1.54308 

1 . 17520 

1.0 

1.2 
1.4 
1.6 
1.8 

0.521153 
0.608012 
0.694871 
0.781730 

9.478847 
9.391988 
9.305129 
9.218270 

3.32011 
4.05520 
4.95304 
6.04965 

0.30119 
0.24660 
0.20190 
0.16530 

1.81065 
2.15090 
2.57745 
3.10745 

1.50946 
1.90430 
2.37557 
3.44218 

1.2 
1.4 
1.6 
1.8 

2.0 

0.868589 

9.131411 

7.38906 

0.13534 

3.76220 

3.62686 

2.0 

2.5 
3.0 
3.5 
4.0 
4.5 

1.085736 
1.302883 
1.520030 
1.737178 
1.954325 

8.914264 
8.694117 
8.479970 
8.262822 
8.045675 

12.1825 
20.0855 
33.1154 
54.5983 
90.0170 

0.082085 
0.049797 
0.030197 
0.018316 
0.011109 

6.1323 
10.0677 
16.5728 
27.3083 
45.0141 

6.0002 
10.0178 
16.5426 
27 . 2900 
45.0030 

2.5 
3.0 
3.5 
4.0 
4.5 

5.0 

2.171472 

7.828528 

148.413 

0.006738 

74.210 

74.203 

5.0 

6 

7 
8 
9 

2.605767 
3.040061 
3.474356 
3.908650 

7.394233 
6.959939 
6.525644 
6.091350 

403.428 
1096.63 
2980.96 
8103.08 

0.002479 
0.000912 
0.000335 
0.000123 

201.715 

201.713 

6 

7 
8 
9 

10 

for X 

>6 

10 

4.342945 

5.657055 

22026.5 

0.0000454 

12 
14 
16 

18 

5.211534 
6.080123 
6.948712 
7.817301 

4.788466 
3.919877 
3.051288 
2.182699 

162755 

1202610 

8886120 

65660000 

0.0000061 
0.00000083 
0.00000011 
0.00000002 

12 
14 
16 
18 

20 

8.685890 

1.314110 

485166000 

0.00000000 

20
