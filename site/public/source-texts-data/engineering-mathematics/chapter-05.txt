CHAPTER VI. 
EMPIRICAL CURVES. 

A. General. 

142. The results of observation or tests usually are plotted 
in a curve. Such curves, for instance, are given by the core 
loss of an electric generator, as function of the voltage; or, 
the current in a circuit, as function of the time, etc. When 
plotting from numerical observations, the curves are empirical, 
and the first and most important problem which has to be 
solved to make such curves useful is to find equations for the 
same, that is, find a function, y=f{x), which represents the 
curve. As long as the equation of the curve is not known its 
utihty is very limited. While numerical values can be taken 
from the plotted curve, no general conclusions can be derived 
from it, no general investigations based on it regarding the 
conditions of efficiency, output, etc. An illustration hereof is 
afforded by the comparison of the electric and the magnetic 
circuit. In the electric circuit, the relation between e.m.f. and 

e 
current is given by Ohm's law, i = -, and calculations are uni- 
versally and easily made. In the magnetic circuit, however, 
the term corresponding to the resistance, the reluctance, is not 
a constant, and the relation between m.m.f. and magnetic flux 
cannot be expressed by a general law, but only by an empirical 
curve, the magnetic characteristic, and as the result, calcula- 
tions of magnetic circuits cannot be made as conveniently and 
as general in nature as calculations of electric circuits. 

If by observation or test a number of corresponding values 
of the independent variable x and the dependent variable y are 
determined, the problem is to find an equation, y=f{x), which 
represents these corresponding values: xi, X2, xz . , , Xn, and 
2/1, 2/2, 2/3 .. . yn, approximately, that is, within the errors of 
observation. 

209 


210 ENGINEERING MATHEMATICS. 

The mathematical expression which represents an empirical 
curve may be a rational equation or an empirical equation. 
It is a rational equation if it can be derived theoretically as a 
conclusion from some general law of nature, or as an approxima- 
tion thereof, but is an empirical equation if no theoretical 
reason can be seen for the particular form of the equation. 
For instance, when representing the dying out of an electrical 
current in an inductive circuit by an exponential function of 
time, we have a rational equation: the induced voltage, and 
therefore, by Ohm's law, the current, varies proportionally to the 
rate of change of the current, that is, its differential quotient, 
and as the exponential function has the characteristic of being 
proportional to its differential quotient, the exponential function 
thus rationally represents the dying out of the current in an 
inductive circuit. On the other hand, the relation between the 
loss by magnetic hysteresis and the magnetic density: W=-q(^^'^, 
is an empirical equation since no reason can be seen for this 
law of the 1.6th power, except that it agrees with the observa- 
tions. 

A rational equation, as a deduction from a general law of 
nature, applies universally, within the range of the observa- 
tions as well as beyond it, while an empirical equation can with 
certainty be relied upon only within the range of observation 
from which it is derived, and extrapolation beyond this range 
becomes increasingly uncertain. A rational equation there- 
fore is far "preferable to an empirical one. As regards the 
accuracy of representing the observations, no material difference 
exists between a rational and an empirical equation. An 
empirical equation frequently represents the observations with 
great accuracy, while inversely a rational equation usually 
does not rigidly represent the observations, for the reason that 
in nature the conditions on which the rational law is based are 
rarely perfectly fulfilled. For instance, the representation of a 
decaying current by an exponential fimction is based on the 
assumption that the resistance and the inductance of the cu'cuit 
are constant, and capacity absent, and none of these conditions 
can ever be perfectly satisfied, and thus a deviation occurs from 
the theoretical condition, by what is called " secondary effects." 

143. To derive an equation, which represents an empirical 
curve, careful consideration should first be given to the physical 


EMPIRICAL CURVES. 211 

nature of the phenomenon which is to be expressed, since 
thereby the number of expressions which may be tried on the 
empirical curve is often greatly reduced. Much assistance is 
usually given by considering the zero points of the curve and 
the points at infinity. For instance, if the observations repre- 
sent the core loss of a transformer or electric generator, the 
curve must go through the origin, that is, y = 0 for x = 0, and 
the mathematical expression of the curve y =f(x) can contain 
no constant term. Furthermore, in this case, with increasing x, 
i/must continuously increase, so that for x = 00, y = Qc. Again, 
if the observations represent the dying out of a current as 
function of the time, it is obvious that for x = oo, y=0. In 
representing the power consumed by a motor when running 
without load, as function of the voltage, for x = 0, y cannot be 
=0, but must equal the mechanical friction, and an expression 
like y = Axf^ cannot represent the observations, but the equation 
must contain a constant term. 

Thus, first, from the nature of the phenomenon, which is 
represented by the empirical curve, it is determined 

(a) Whether the curve is periodic or non-periodic. 

(6) Whether the equation contains constant terms, that is, 
for x = 0, 2/7^0, and inversely, or whether the curve passes 
through the origin: that is, y = 0 for a: = 0, or whether it is 
h3^erbolic ; that is, y= 00 for x = 0, or x = 00 for y = 0. 

(c) What values the expression reaches for 00. That is, 
whether for x = oo, 2/ = ^, or 2/ = 0, and inversely. 

(d) Whether the curve continuously increases or decreases, or 
reaches maxima and minima. 

(e) Whether the law of the curve may change within the 
range of the observations, by some phenomenon appearing in 
some observations which does not occur in the other. Thus, 
for instance, in observations in which the magnetic density 
enters, as core loss, excitation curve, etc., frequently the curve 
law changes with the beginning of magnetic saturation, and in 
this case only the data below magnetic saturation would be used 
for deriving the theoretical equations, and the effect of magnetic 
saturation treated as secondary phenomenon. Or, for instance, 
when studying the excitation current of an induction motor, 
that is, the current consumed when running light, at low 
voltage the current may increase again with decreasing voltage, 


212 ENGIN^EERING MATHEMATICS. 

instead of decreasing, as result of the friction load, when the 
voltage is so low that the mechanical friction constitutes an 
appreciable part of the motor output. Thus, empirical curves 
can be represented by a single equation only when the physical 
conditions remain constant within the range of the observations. 

From the shape of the curve then frequently, with some 
experience, a guess can be made on the probable form of the 
equation which may express it. In this connection, therefore, 
it is of the greatest assistance to be familiar with the shapes of 
the more common forms of curves, by plotting and studying 
various forms of equations y=f{x). 

By changing the scale in which observations are plotted 
the apparent shape of the curve may be modified, and it is 
therefore desirable in plotting to use such a scale that the 
average slope of the curve is about 45 deg. A much greater or 
much lesser slope should be avoided, since it does not show the 
character of the curve as well. 

B. Non-Periodic Curves. 

144. The most common non-periodic curves are the potential 
series, the parabolic and hyperbolic curves, and the exponential 
and logarithmic curves. 

The Potential Serie^. 

Theoretically, any set of observations can be represented 
exactly by a potential series of any one of the following forms : 

y = ao + aiX-\-a2X^-{-a3X^-\- . . . ; .... (1) 

y = aiX+a2X^-haix^ + . . . ; (2) 

cii 0,2 CLS /^s 

2/=a„+-+-+-3 + ...: (3) 

ai 02 as , ,., 

2'=^+F^ + ? + W 

if a sufficiently large number of terms are chosen. 

For instance, if n corresponding numerical values of x and y 
are given, Xi, 2/1; X2, 2/2; ... x„, yn, they can be represented 


EMPIRICAL CURVES. 


213 


by the series (1), when choosing as many terms as required to 
give n constants a: 


y = ao+aix+a2X^-{-. . .+an_in"~i. 


(5) 


By substituting the corresponding values Xi, yi] X2, 2/2, •• . 
into equation (5), there are obtained n equations, which de- 
termine the n constants ao, ai, a2, . . . a„_i. 

Usually, however, such representation is irrational, anc; 
therefore meaningless and useless. 


Table I. 


e 
100 ""^ 

Pi=y 

-0.5 

+ 2x 

+ 2.5x2 

-1.5x3 

+ 1.5x< 

-2x6 

+ X6 

0.4 
0.6 
O.S 

0.63 
1.36 
2.18 

-0.5 
-0.5 
-0.5 

+0.8 
+ 1.2 
+ 1.6 

+ 0.4 
+0.9 
+ 1.6 

-0.10 
-0.32 
-0.77 

+ 0.04 
+0.19 
+ 0.61 

- 0.02 

- 0.16 

- 0.65 

0 
+ 0.05 
+ 0.26 

1.0 
1.2 
1.4 

3.00 
3.93 
6.22 

-0.5 
-0.5 
-0.5 

+ 2.0 

+ 2.4 
+ 2.8 

+ 2.5 
+3.6 
+4.9 

-1.50 
-2.59 
-4.12 

+ 1.50 
+ 3.11 

+ 5.76 

- 2.00 

- 4.98 
-10.76 

+ 1.00 
+ 2.89 
+ 6.13 

1.6 

8.59 

-0.5 

+3.2 

+ 6.4 

-6.14 

+9.83 

-20.97 

+ 16.78 

Let, for instance, the first column of Table I represent the 
voltage, YrjQ = ^j in hundreds of volts, and the second column 

the core loss, Pi=y, in kilowatts, of an 125- volt 100-h.p. direct- 
current motor. Since seven sets of observations are given, 
they can be represented by a potential series with seven con- 
stants, thus, 

y = ao+aix-\-a2X^+. . .-\-aex^, .... (6) 

and by substituting the observations in (6), and calculating the 
constants a from the seven equations derived in this manner, 
there is obtained as empirical expression of the core loss of 
the motor the equation. 


t/= -0.5 +2X+2.5X2- 1.5x3 + 15^4_2a;5+x6. 


(7) 


This expression (7), however, while exactly representing 
the seven observations, has no physical meaning, as easily 
seen by plotting the individual terms. In Fig. 60, y appears 


214 


ENGINEERING MATHEMATICS. 


as the resultant of a number of large positive and negative 
terms. Furthermore, if one of the observations is omitted, 
and the potential series calculated from the remaining six 
values, a series reaching up to x^ would be the result, thus, 

2/ = ao4-aix+a2x2 + . . .+a5X^, .... (8) 


16 

1 

J 

12 

/ 

r 

b / V 

8 

i 

^ 

r 

i 

-^ 

rt 

y^ 

^ 

^ 

^ 

€1 

'i^X. 

D 

_ 

_-3 

= 

^ 

^ 

"~^~ 

!». 

■^ 

:'--^ 

-fl 

.5 

-i 

N 

s 

^^ 

^^. 

??- 

^ 

\ 

^ 

^ 

-8 

\ 

0^ 

^' 

^ 

-12 

\ 

V 

\ 

-ic 

\ 

\ 

x = 

\ 

•SO 

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

1 

2 

1 

4 

) 

6 

Fig. 60. Terms of Empirical Expression of Excitation Power. 

but the constants a in (8) would have entirely different numer- 
ical values from those in (7), thus showing that the equation 
(7) has no rational meaning. 

145' The potential series (1) to (4) thus can be used to 
represent an empirical curve only under the following condi- 
tions': 

1. If the successive coefficients ao, ai, a2, ... decrease in 
value so rapidly that within the range of observation the 
higher terms become rapidly smaller and appear as mere 
secondary terms. 


EMPIRICAL CURVES. 


215 


2. If the successive coefficients a follow a definite law, 
indicating a convergent series which represents some other 
function, as an exponential, trigonometric, etc. 

3. If all the coefficients, a, are very small, with the exception 
of a few of them, and only the latter ones thus need to be con- 
sidered. 

Table II. 


X 

1/ 

v^ 

1/1 

0.4 
0.6 
0.8 

0.89 
1.35 
1.96 

0.88 
1.34 
1.94 

0.01 
0.01 
0.02 

1.0 
1.2 
1.4 

2.72 
3.62 
4.63 

2.70 
2.59 
4.59 

0.02 
0.03 
0.04 

1.6 

5.76 

5.65 

0.11 

For instance, let the numbers in column 1 of Table II 
represent the speed x of a fan motor, as fraction of the rated 
speed, and those in column 2 represent the torque y, that is, 
the turning moment of the motor. These values can be 
represented bj' the equation, 

2/ = 0.r)+0.02x + 2.5.r2-0.3r^ +0.015x^-0.02x5 +0.01.r6. (9) 

In this case, only the constant term and the terms with 
x2 and x^ have appreciable values, and the remaining terms 
probably are merely the result of errors of observations, that is, 
the approximate equation is of the form. 


y = ao+a2X^ + asX^. .... 

Using the values of the coefficients from (9), gives 
y = 0.5+2.5x^-0.3x^ \ . . 


(10) 


(11) 


The numerical values calculated from (11) are given in column 
3 of Table II as y', and the difTerence between them and the 
observations of column 2 are given in column 4, as yi. 


216 ENGINEERING MATHEMATICS. 

The values of column 4 can now be represented by the same 
form of equation, namely, 

2/1 = &o + &2x2 +63^3, (12) 

in which the constants ho, 62, hs are calculated by the method 
of least squares, as described in paragraph 120 of Chapter IV, 
and give 

2/1= 0.031 -0.093:r2+ 0.076x3 (13) 

Equation (13) added to (11) gives the final approximate 
equation of the torque, as, 

2/0 = 0.531 +2.407.T2- 0.224x3 (14) 

The equation (14) probably is the approximation of* a 
rational equation, since the first term, 0.531, represents the 
bearing friction; the second term, 2.407x^ (which is the largest), 
represents the work done by the fan in moving the air, a 
resistance proportional to the square of the speed, and the 
third term approximates the decrease of the air resistance due 
to the churning motion of the air created by the fan. 

In general, the potential series is of limited usefulness; it 
rarely has a rational meaning and is mainly used, where the 
curve approximately follows a simple law, as a straight line, 
to represent by small terms the deviation from this simple law, 
that is, the secondary effects, etc. Its use, thus, is often 
temporary, giving an empirical approximation pending the 
derivation of a more rational law. 

The Parabolic and the Hyperbolic Curves. 

146. One of the most useful classes of curves in engineering 
are those represented by the equation, 

y = ax^; (15) 

or, the more general equation, 

y-h = a{x-cy (16) 

Equation (16) differs from (15) only by the coastant terms h 
and c; that is, it gives a different location to the coordinate 


EMPIRICAL CURVES. 217 

center, but the curve shape is the same, so that in discussing 
the general shapes, only equation (15) need be considered. 

If n is positive, the curves y = ax'^ are 'parabolic curves, 
passing through the origin and increasing with increasing x, 
li n>\,y increases with increasing rapidity, if n<l, t/ increases 
with decreasing rapidity. 

If the exponent is negative, the curves y^ax'"^^ — are 

hyperbolic curves, starting from 2/ =00 for x=0, and decreasing 
to y=0 for x= 00. 

n^\ gives the straight line through the origin, n=0 and 
n=oo give, respectively, straight horizontal and vertical lines. 

Figs. 61 to 71 give various curve shapes, corresponding to 
different values of n. 

Parabolic Curves. 

Fig. 61. n = 2; y = x'^\ the common parabola. 
Fig. 62. n = 4; y = x'^', the biquadratic parabola. 


Fig. 63. n = 8; 

y = x^. 

Fig. 64. n = i; 

y= Vx', again the common parabola. 

Fig. 65. n = i; 

y= -^'j the biquadratic parabola. 

Fig. 66. n = \\ 

y = </x. 

Hyperbolic Curves. 

Fig. 67. n=— 1; 2/ =~; the equilateral h)rperbola. 


Fig. 68. n=-2; y^j^. 
Fig. 69. n=-4; 1/=-,. 

Fig. 70. n=-|; y=-^. 

1 1 

Fig. 71. n=-j; 2/=-^. 


218 


ENGINEERING MATHEMATICS. 


=1 


_ 

■^ 

■->s 

s 

s 

\ 

\ 

< 

5 

a 

t 

t 

C 

) 

< 

§ 

i 

o 

? 

— ' 


-= 

' ■ 

^ 

^ 

^^ 

^ 

S^ 

\ 

V 

\ 

\ 

\ 

5 

f 

c 

T 

r 

I 

I 

H 

: 

I 

i 

5 

? 

§ 

3 

5 

c 

c 

J 

c5 PL, 


« CD 
o 

O 


-^ 

^ 

^ 

^^ 

•^ 

^ 

•^ 

^ 

V, 

V 

N 

\ 

\ 

s 

\ 

\, 

s 

\ 

\ 

\ 

\ 

i 

c 

^ 

r 

5 

ii 

ft 

C 

^ 

< 

> 

0 

■; 

L. 

i 

5 

\ 

i 

U 

r4 « 

II 

5si 


00 O 

'o 


EMPIRICAL CURVES. 


219 


^ 

IaI 

^ 

"^ 

^ 

^ 

"^ 

.^ 

x^ 

,y 

y 

/ 

y 

j\.a— 

/ 

/ 

/ 

/ 

J\-A 

/ 

/ 

/ 

( 

J 

1 

0 

2 

0 

4 

p 

6 

0 

8 

1 

0 

1 

% 

I 

4 

1 

6 

i 

8 

2 

9 

Fig. 64. Parabolic Curve. y = \/x. 


tf'S- 

^~~" 

-— ■ 

=^ 

liO- 

-^ 

-^" 

^ 

-^ 

' 

0-8- 

^^ 

-^ 

-^ 

^ 

n-fi-1 

/ 

/ 

/. 

r 

n-^- 

_ 

0 

2 

0 

1 

0 

6 

0 

8 

1 

0 

1 

2 

1 

4 

1 

6 

1 

8 

2 

0 

Fig. 65. Parabolic Curve. y= -yix. 


220 


ENGINEERING MATHEMATICS. 


. 

^- 

■ 


n fi 

> 

/ 

z' 

L 

r 

0 

3 

0 

4 

0 

6 

0 

8 

1 

0 

1 

2 

1 

i 

1 

5 

I 

3 

2 

) 

Fig. 66. Parabolic Curve. y = 's/x. 

' 

I 

\ 

\ 

\ 

« 

-1 a 

\ 

V 

\ 

1 O 

\ 

\ 

\ 

f\ Q 

\ 

V 

\ 

v^ 

l\-A 

^-- 

^ 

■ 

i 

0 

4 

0 

8 

1 

2 

1 

6 

2 

« 

2 

* 

2 

8 

3 

2 

3 

6 

4 

0 

Fig, 67. Hyperbolic Curve (Equilateral Hyperbola), y 


EMPIRICAL CURVES. 


221 


jfcan 

n 

O Q_ 

' 

I 

\ 

o_/\_ 

\ 

\ 

\ 

\ 

\ 

1^ 

\ 

/\_Q_ 

\ 

\ 

s 

A_i4 

N 

V, 

"^ 

"~~~ 

— 1 

— 


0.4 0.8 1.3 1.6 .2.0 2.4 2.8 3.2 3.6 4.0 4.4 


Fig. 

68. 

Hyperbolic Curve. 

y 

X 

9^ 

. 

Ol 

* 

1-R- 

hSi- 

\ 

\ 

\ 

\ 

\ 

\, 

\ 

v^ 

"^^ 

1 

____ 

__ 

0.4 0.8 1.2 1.6 2.0 2.4 2.8 3.2 3.6 4.0 4.4 


Fig. 69. Hyperbolic Curve. y = —^. 


7 


222 


ENGINEERING MATHEMATICS. 


i:k{p 

n 

>/ll 

i 

4 

4iO 

\ 

\ 

\ 

\ 

\ 

s 

N 

^ 

^^ 

^■ 

. 

— - 

■ 

— ■ 

0 

i 

0 

8 

1 

2 

1 

6 

2 

0 

2 

i 

2 

8 

3 

2 

3 

6 

A 

0 

4 4 

Fig. 70. Hyperbolic Curve. y=-—p. 

r 

0 Q 

2v4 

s. 

\ 

s 

V 

^ 

^ 

"^ 

^- 

. 


"~ 

"^~~ 

0 

i 

0 

8 

1 

2 

1 

6 

2 

0 

2 

4 

2 

8 

3 

2 

3 

6 

i 

0 

4 

4 

Fig. 71. Hyperbolic Curve. y = 


EMPIRICAL CURVES. 223 

In Fig. 72, sixteen different parabolic and hyperbolic curves 
are drawn together on the same sheet, for the following values : 
n = l, 2, 4, 8, ^; i i *, 0; -1, -2, -4, -8; -i, -{, -i 

147. Parabolic and hyperboHc curves may easily be recog- 
nized by the fact that ifx is changed by a constant factor, y also 
changes by a constant factor. 

Thus, in the curve y = x~, doubling the x increases the y 
fourfold; in the curve y = x^'^^, doubling the x increases the y 
threefold, etc.; that is, if in a curve, 

f(qx) 

"iTT-T- = constant, for constant g, . . . (17) 

the curve is a parabolic or hyperbolic curve, y = ax'^, and 

fiqx) a{qxY 

f{x)^~l^^'^^ ^^^^ 

If q is nearly 1, that is, the x is changed onjy by a small 
value, substituting ^' = 1+8, where s is a small quantity, from 
equation (18), 

f{x-\-sx) ^^ . 

hence, 

f{x-\-sx)-f{x)=ns; (19) 

that is, changing x by a small percentage sx, y changes by a pro- 
portional small percentage nsy. 

Thus, parabolic and hyperbolic curves can be recognized by 
a small percentage change of x, giving a proportional small 
percentage change of y, and the proportionaUty factor is the 
exponent n; or, they can be recognized by doubling x and 
seeing whether y hereby changes by a constant factor. 

As illustration are shown in Fig. 73 the parabolic curves, 
which, for a doubling of .r, increase y: 2, 3, 4, 5, 6, and 8 fold. 

Unfortunately, this convenient way of recognizing parabolic 
and hyperbolic curves applies only if the curve passes through 
the origin, that is, has no constant term. If constant terms 
exist, as in equation (16), not x and y, but (x—c) and (y—b) 
follow the law of proportionate increases, and the recognition 


224 


ENGINEERING MATHEMATICS. 


becomes more difficult; that is, various values of c and of h 
are to be tried to find one which gives the proportionality. 


Z^i 

\ 

\ 

\, 

8 

fi' 

•y 

2.0 

\ 

\ 

\ 

\ 

I 

1 

II 

^ 

1 

1 

/ 

\ 

y=x 

■\ 

\ 

\ 

1 
1 

^ 

/ 

/ 

/ - 

L.8 

\ 

\ 

\ 

\ 
\ 

1 

H 

/ 
f 

/ 

) 

\ 

\ 
\ 

\ 

\ 

\ 

-/ 
1 

/ 

\ 
\ 

\ 

\ 

\ 

\ 

\ 

\ 
\ 

/ 
/ 

/ 

\ 

\ 

\ 

\ 

\ 

\ 

\ 

/ 
/ 

/ 

'^^ 

.f/ 

\ 

\ 

\ 

V 

\ 

\ 

\ 

\ 

\ 

\ 

i 

' 
1 

/ 

/ 

\ 

\, 

\ 

N, 

\ 

\ 

\ 
\ 

\ 

1 

/ 

1 o 

N 

■^ 

N 

\, 

\ 

\ 

V 

\ 

jl 

1 

/ 

% 

^ 

\ 

\, 

\ 

.,\ 

% 

/// 

/ 

^ 

^ 

^^^ 

.^'^ 

Hyp 

erbo 

ic Cu 

rves 

^^^ 

s^ 

\ \\\ 

1 

::i!ir_ 

"^^ 

V 

Fill 
^1 

i.U 

Pari 

ibolic 

Curv 

es 

^ 

^ 

'^ 

'*^. 

n:^ 

■:^ 

y 

i^IZj 

^ 

^ 

.'^' 

y 

X 

\\\ 

s 

'■•- 

y 

*i*?-c 

/ 

/ 

y 

/" 

X 

^ 

/ 

/ 

/ 

\\ 

\ 

\ 

\ 

^< 

'*-.' 

/ 

/ 

/ 

y 

/- 

/ 

/ 

\ 

// 

y 

\ 

\^ 

"^ 

^ 

'/ 

f 

/ 

/ 

/ 

/ 

1 
1 

\ 

\ 

\ 

\ 

/ 
/ 

/ 

/ 

/ 

/ 

1 , 

\ 

\ 

^^ 

0.4 

/ 

/ 

/ 

/ 

/ 

1 
/ 

\ 

V 
\ 

»i 

7 

/ 

/ 

/ 

. 

/ 

/ 

\ 

\ 

V 

"\^ 

1<?^^^. 

0.2 

/ 

/ 

y 

/ 

/ 

/ 

/ 

/ 

N 

x^^ 

'A 

^ 

^^ 

/ 

^ 

/ 

--ii 

^^-^ 

0,2 0.4 0.6 0.8 1.0 1.2 1.4 l.G 

Fig. 72. Parabolic and Hyperbolic Curves. y = xn. 

148. Taking the logarithm of equation (15) gives 

log2/ = loga+nloga:; (20) 


EMPIRICAL CURVES. 


225 


that is, a straight hne; hence, a parabolic or hyperbolic curve can 
be recognized by plotting the logarithm of y against the loga- 
rithm of X. If this gives a straight line, the cm've is parabolic 
or hyperbolic, and the slope of the logarithmic curve, tan ^ = n, 
is the exponent. 


7 

^ 

9-n 

" 

m 

'^ 1 1 

1 1 

1 . 

7 

/ 

1 

/ 

I 

'// 

/ 

1 

/' 

/ 

\ 

§/ 

1-A 

i 

7 

/ 

/// 

/ 

/ 

j_o 

i 

V. 

/ 

J 

'/ 

l_n 

^ 

A 

^ 

0-R- 

w 

/ 

/ 

/ 

// 

/ 

/ 

/ h 

O /!_ 

/ 

/ 

^// 

^ 

/ 

/ 

// 

y/> 

/ 

/ 

y 

// 

'A 

y 

/ 

y 

<< 

d 

y 

Z 

^ 

^ 

^ 

y 

0.2 0.4 0.6 0.8 1.0 1.2 1.4 

Fig. 73. Parabolic Curves. y=xn. 


1.6 


This again applies only if the curve contain no constant 
term. If constant terms exist, the logarithmic line is curved. 
Therefore, by trying different constants c and 5, the curvature 
of the logarithmic line changes, and by interpolation such 
constants can be found, which make the logarithmic Hne straight, 
and in this way, the constants c and h may be evaluated. If 
only one constant exist, that is, only h or only c, the process is 
relatively simple, but it becomes rather complicated with both 


226 


ENGINEERING MATHEMATICS. 


constants. This fact makes it all the more desirable to get 
from the physical nature of the problem some idea on the 
existence and the value of the constant terms. 

Exponential and Logarithmic Curves. 

149. A function, which is very frequently met in electrical 
engineering, and in engineering and physics in general, is the 
exponential function, 

2/ = a£"^; (21) 

which may be written in the more general form, . 

I/— ?> = a£«^^-^^ 


(22) 


Usually, it appears with negative exponent, that is, in the 
form. 


y = ae 


(23) 


Fig. 74 shows the curve given by the exponential function 
(23) for a = l; n^l] that is. 


2/=£- 


(24) 


as seen, with increasing positive x, y decreases to 0 at x= + 00, 
and with increasing negative x, y increases to 00 at a: = — 00. 

The curve, y=z^'', has the same shape, except that the 
positive and the negative side (right and left) are interchanged. 

Inverted these equations (21) to (24) may also be written 
thus, 


1 y 

^ a' 


n{x—c) = \og 


'-h 


nx= — log 


y 


x=-hgy] 
that is, as logarithmic curves. 


(25) 


EMPIRICAL CURVES. 


227 


150. The characteristic of the exponential function (21) is, 
that an increase of x by a constant term increases (or, in (23) 
and (24), decreases) y by a constant factor. 

Thus, if an empirical curve, y^f{x), has such characteristic 
that 

f(x + q) 


fix) 


= constant, for constant q, 


(26) 


\1 

r^ 

-1t4 

o) 

\ 

\ 

\ 

\ 

\ 

■onj- 

\ 

\ 

ItO 

\ 

\ 

\ 

\ 

D-A 

V 

\ 

N 

\ 

\ 

s. 

\^ 

s. 

0 n 

\ 

\ 

\ 

\^ 

n A 

N 

N 

s 

\ 

in 

\ 

^ 

^ 

-0.-JJ 

^" 

-^ 

"^ 

-^ 

.,.. 

-2.0 -1.6 -1.2 -0.8 -0.4 0 0.4 0.8 1.2 

Fi G. 74 . Exponential Function . y^e-x. 


1.6 


2.0 


the curve is an exponential function, y^ae^"", and the following 
equation may be written : 


f(x-\-q) a£"(^+g> 
fix) ~ as"^ 


= enq 


(27) 


Hereby the exponential function can easily be recognized, 
and distinguished from the parabolic curve; in the former a 
constant terw,^ in the latter a constant factor of x causes a 
change of 2/ by a constant factor. 

As result hereof, the exponential curve with negative 
exponent vanishes, that is, becomes negligibly small, with far 
greater rapidity than the hyperboHc curve, and the exponential 


228 


ENGINEERING MATHEMATICS. 


function with positive exponent reaches practically infinite 
values far more rapidly than the paraboHc curve. This is 
illustrated in Fig. 75, in which are shown superimposed 
the exponential curve, 2/=^"^ and the hyperbolic curve, 

2.4 
2/ = 7 — , -, r-\oy which coincides with the exponential curve 

at :r = 0 and at x = l. 

Taking the logarithm of equation (21) gives log 2/=^ log a + 
nx log £, that is, log 2/ is a linear function of x, and plotting 
log y against x gives a straight line. This is characteristic of 


V 

1 

-1:0 

\ 

\ 

-U;o 

^ 

s5 ' 

xt 

2.4 

^. 

0;6 

(a 

J+LS 

5)=^S 

^ 

V 

V 

H 

0:4 

^ 

"^ 

2 

.4 

2 

^r^ 

rl.55 

£■ 

^ 

^ 

0;2 

■" — 


■ 

■^ 

0.4 0.8 1.2 1.6 2.0 2.4 2.8 3.2 3.6 

P'iG. 75. Hyperbolic and Exponential Curves C'omparison. 


4.0 


the exponential functions, and a convenient method of recog- 
nizing them. 

However, both of these characteristics apply only if x and y 
contain no constant terms. With a single exponential function, 
only the constant term of y needs consideration, as the constant 
term of x may be eliminated. Equation (22) may be written 
thus: 

2/— 6 = a£"^^""''^ 

=^At^^ 


(28) 

where ^ = as"* is a constant. 

An exponential function which contains a constant term h 
would not give a straight line when plotting log 2/ against x. 


EMPIRICAL CURVES. 


229 


but would give a curve. In this case then log (y—h) would be 
plotted against x for various values of b, and by interpolation 
that value of b found which makes the logarithmic curve a 
straight line. 

151. While the exponential function, when appearing singly, 
is easily recognized, this becomes more difficult with com- 


i_i 

(1) 2/=£-a?+o.5^"2«' 

(5) 2/=r«^-o.5£~2« 

(6) y=e-X_Q^^s-2X 

(7) y = e-X-£-'^^ 

(8) y= e'a'-i.ss-saj 

1 0 

\^ 

(1) 

\ 

\ 

-i-.o 

Vs) 

l\ 

\ 

\ 

-0.-8 

\* 

,v 

v\ 

\ 

nN 

\ 

-A r; 

\^ 

[^1 

\ 

^ 

\ 

n\ 

^ 

V 

-0.-4- 

(Ql 

^ 

^ 

N 

/ 

^ 

-~-^ 

"^ 

^ 

^ 

-0.2 

^~--i:i^^ 

/ 

<-) 

fe=^ 

^ 

L^ 

' 

' 

^k= 

/ 

/ 

-==^ 

==- 

/ 

1 

0 

8 

1 

2 

1 

6 

2 

" 

2 

4 

2 

8 

— 0- 

A8) 

-0.2 

/ 

/ 

-0.4 

/ 

L. 

Fig. 76. Exponential Functions. 

binations of two exponential functions of different coefficients 
in the exponent, thus, 

2/ = ai£-''»^±a2£"'^, (29) 

since for the various values of ai, 0.2, c\, C2, quite a number of 
various forms of the function appear. 

As such a combination of two exponential functions fre- 
quently appears in engineering, some of the characteristic forms 
are plotted in Figs. 76 to 78. 


230 


ENGINEERING MATHEMATICS. 


r 

(1) 2/=£-«^+0.6£"10* 

f3) 2/=£~^-o.l£'ioa; 

(4) 2/=£-a;-o.5£-io^ 

(5) 2/=£-a;-,£-ioa; 

(6) 2/=£-«^-U£-10» 

V 

) 

\ 

i\ 

<-^ 

\ 

'V- 

\ 

W 

?^ 

K 

// 

\ 

\ 

f 

) 

\| 

\ 

s 

\ 

\ 

^ 

■^ 

^^ 

■■ 


■— 

0 

i 

0 

8 

1 

2 

1 

6 

2 

0 

2 

4 

2 

8 

L4 


1^ 


1.0 


0.8 


0.6 


0.4 


0.2 


-0.2 


-0.4 


Fig. 77. Exponential Functions. 


Fig. 76 gives the following combinations of £~^ and £~2'; 

(1) l/=£-^+0.5£-2^; 

(2) 2/=£-^+0.2£-2^; 

(3) y=e--] 

(4) y=£-^-0,2e-2'; 

(5) i/=£-^-0.5£-2x; 

(6) 2/=^"^-O.S£-2^; 

(7) 2/=£---£-2- 

(8) 2/=£""'^-1.5£"2^ 


EMPIRICAL CURVES. 


231 


■■ 

~1 

/ 

■fJOi 

/ 

/ 

-2;0 

/ 

/ 

■4 

/ 

/ 

/ 

/ 

/ 

/ 

/ 

/ 

/ 

. / 

/ 

/ 

.^^ 

r 

/ 

y 

/ 

/ 

/ 

/ 

_, 

/ 

.^7 

/ 

• 

-0.8* 

/ 

/ 

y 

/ 

(he 

/ 

/■ 

ni 

/ 

/ 

/ 

/ 

0 

2 

0 

4 

» 

6 

0 

8 

1 

0 

1 

2 

1 

4 

Fig. 78. Hyperbolic Functions. 
Fig. 77 gives the following combination of t~^ and £~^®^: 

(1) 2/=£--+0.5£-i<^^; 

(2) 2/=^"^; 

(3) ^=£-^-O.U-io^; 

(4) i/=£-^-0.5£-i<^^; 

(5) |/=.-x_,-10x. 

(6) '^=£-^-1.5£-i^^ 

Fig. 78 gives the hyperbolic functions as combinations cf 
f^' and £~^ thus, 

2/ = cosh a: = i( e"^ =^ + £~ ^) ; 

2/ = sinh a: = J(£''"^— £~^). 


232 ENGINEERING MATHEMATICS. 


C. Evaluation of Empirical Curves. 

152. In attempting to solve the problem of finding a mathe- 
matical equation, y=f{x), for a series of observations or tests, 
the corresponding values of x and y are first tabulated and 
plotted as a curve. 

From the nature of the physical problem, which is repre- 
sented by the numerical values, there are derived as many 
data as possible concerning the nature of the curve and of the 
function which represents it, especially at the zero values and 
the values at infinity. Frequently hereby the existence or 
absence of constant terms in the equation is indicated. 

The log X and log y are tabulated and curves plotted between 
X, y, log X, log y, and seen, whether some of these curves is a 
straight line and thereby indicates the exponential function, or 
the parabolic or hyperbolic function. 

If cross-section paper is available, having both coordinates 
divided in logarithmic scale, and also cross-section paper having 
one coordinate divided in logarithmic, the other in common 
scale, the tabulation of log x and log y can be saved and x 
and y directly plotted on these two forms of logarithmic cross- 
section paper. 

If neither of the four curves: x, y; x, log y; hgx, y; log x, 
log 2/ is a straight line, and from the physical condition the 
absence of a constant term is assured, the function is neither 
an exponential nor a parabolic or hyperbolic. If a constant 
term is probable or possible, curves are plotted between x, 
y—b, log X, log (y—h) for various values of 6, and if hereby 
one of the curves straightens out, then, by interpolation, 
that value of h is found, which makes one of the curves a straight 
line, and thereby gives the curve law. In the same manner, 
if a constant term is suspected in the x, the value (x—c) is 
used and curves plotted for various values of c. Frequently the 
existence and the character of a constant term is indicated by 
the shape of the curve ; for instance, if one of the curves plotted 
between x, y, log x, log y approaches straightness for high, or for 
low values of the abscissas, but curves considerably at the 
other end, a constant term may be suspected, which becomes 
less appreciable at one end of the range. For instance, the 
efTect of the constant c in (x—c) decreases with increase of x. 


EMPIRICAL CURVES. 233 

Sometimes one of the curves may be a straight Hne at one 
end, but curve at the other end. This may indicate the presence 
of a term, which vanishes for a part of the observations. In 
this case only the observations of the range which gives a 
straight line are used for deriving the curve law, the curve 
calculated therefrom, and then the difference between the 
calculated curve and the observations further investigated. 

Such a deviation of the curve from a straight line may also 
indicate a change of the curve law, by the appearance of 
secondary phenomena, as magnetic saturation, and in this case, 
an equation may exist only for that part of the curve where the 
secondary phenomena are not yet appreciable. 

If neither the exponential functions nor the parabolic and 
hyperbolic curves satisfactorily represent the observations, 

X 

further trials may be made by calculating and tabulating - 

y X XI 

and -, and plotting curves between x, y,-, -. Also expressions 
X y X ' 

as x^+hy^, and {x—aY+h(y—c)^, etc., may be studied. 

Theoretical reasoning based on the nature of the phenomenon 
represented by the numerical data frequently gives an indi- 
cation of the form of the equation, which is to be expected, 
and inversely, after a mathematical equation has been derived 
a trial may be made to relate the equation to known laws and 
therebj^ reduce it to a rational equation. 

In general, the resolution of empirical data into a mathe- 
matical expression largely depends on trial, directed by judg- 
ment based on the shape of the curve and on a knowledge of 
the curve shapes of various functions, and only general rules 
can thus be given. 

A number of examples may illustrate the general methods of 
reduction of empirical data into mathematical functions. 

153. Example 1. In a 118-volt tungsten filament incan- 
descent lamp, corresponding values of the terminal voltage e 
and the current i are observed, that is, the so-called '' volt- 
ampere characteristic '' is taken, and therefrom an equation for 
the volt-ampere characteristic is to be found. 

The corresponding values of e and i are tabulated in the 
first two columns of Table III and plotted as curve I in Fig. 79. 
In the third and fourth column of Table III are given log e 


234 


ENGINEERING MATHEMATICS. 


and logi. In Fig. 79 then are plotted e, logi, as curve II 
log e, i, as curve III; log e, log i, as curve IV. 

As seen from Fig. 79, curve IV is a straight line, that is, 

log i = A+7iloge] or, i = ae^., 

which is a parabolic curve. 

0.2 0.4 0.6 0.8 1.0 1.2 1.4 1.6 1.8 2:0 2.2 2A=log 6 


2 

p 4 

) e 

p 8 

) 160 1^0 

\' 

0 1 

K) 1^0 2( 

K) 2^=e 

logi 

^.-^ 

-J 

9.6 

y- 

J 

^ 

^ 

^ 

as 

jsr 

^ 

>^ 

,S.^ 

l^ 

'y 

l^ 

9:4. 

xoS 

X^ 

/ 

r/ 

V 

9.3 

/ 

/ 

IV 

/ 

/ 

9.2 
9.1 

/ 

/ 

/ 

/ 

/ 

t 

/ 

i F.o 

/ 

fy^ 

1 

0.45 8.9 

f 

.S 

y 

" / 

040 "5a 

/ 

^ 

i^ 

^ 

/ 

0.35 8.7 
0.30 8.6 
025 8 <% 

/ 

^^ 

^ 

y'^ 

/ 

1 

/ 

< 

^ 

y 

i 

/ 

/ 

y 

y 

/ 

.^ 

0.20 8.4 
0.15 8.3 
0.10 8.2 
0 05 8.1 

/ 

/ 

/ 

4 

/ 

/ 

^^ 

A 

.0** 

/ 

^ 

^ 

1 

- 

-^ 

Fig. 79. Investigation of Volt-ampere Characteristic of Tungsten Lamp 

Filament. 

The constants a and n may now be calculated from the 
numerical data of Table III by the method of least squares, 
as discussed in Chapter IV, paragraph 120. While this method 
gives the most accurate results, it is so laborious as to be seldom 


EMPIRICAL CURVES. 


235 


used in engineering; generally, values of the constants a 
and n, sufficiently accurate for most practical purposes, are 
derived by the following method : 

Table III. 
VOLT-AMPERE CHARACTERISTIC OF 118-VOLT TUNGSTEN LAMP. 


e 

i 

log e 

log i 

8211 +0-6 log 6 

A 

2 

00245 

0-301 

8-392 

8-389 

-0.003 

4 

0-037 

0-602 

8-568 

5-572 

-0004 

8 

00568 

0-903 

8-754 

g-753 

+ 0001 

16 

0-0855 

1-204 

8-932 

8- 933 

-0.001 

25 

0-1125 

1398 

9-051 

9-050 

+ 0.001 

32 

0-1295 

1-505 

9-112 

9-114 

-0002 

50 
64 

01715 
0-200 

1.699 
1.806 

§.234 

9-230 
9-295 

+ 0004 
+ 0006 

9.301 

100 

0-2605 

2-000 

9-416 

9-411 

+ 0005 

125 

0-2965 

2-097 

9-472 

9-469 

+ 0-003 

150 

03295 

2-176 

9-518 

§-518 

0 

180 

0-3635 

2-255 

9-561 

9-564 

-0-003 

200 

03865 

2-301 

9- 587 

9-592 

-0005 

218 

0407 

2-338 

9-610 

9-614 

-0-004 

17= 7. 612 

2-040 

avg. ±0.003 = 

0 . 7 per cent 

r= 14-973 

6-465 

f= 7-361 

4-425 

4-425 

n= = 

7381 

0-6011~0 

-6 

i'14= 22-585 

8- 505 

06X22-585 = 

= 13. 551 

4 = 8.505-13 

■551 = 4.954 

1-954-14 = 

8-211 

logt = g.211+0.6l 

og e and i = 

0-01625e''« 

The fourteen sets of observations are divided into two 
groups of seven each, and the sums of log e and log i formed. 
They are indicated as 27 in Table III. 

Then subtracting the two groups 27 from each other, 
oliminates A, and dividing the two differences J, gives the 
exponent, n = 0.6011; this is so near to 0.6 that it is reasonable 
to assume that n = 0.6, and this value then is used. 


236 ENGINEERING MATHEMATICS. 

Now the sum of all the values of log e is formed, given as 
214 in Table II, and multiplied with n = 0.6, and the product 
subtracted from the sum of all the logl The difference J 
then equals 14^, and, divided by 14, gives 

A = log a = 8.211; 

hence, a = 0.01625, and the volt-ampere characteristic of this 
tungsten lamp thus follows the equation, 

logt = 8.211+0.61oge; 
^ = 0.01625e0•6. 

From e and i can be derived the power input p = ei, and the 

resistance r = — : 
I - 

p = 0.016256i-6; 

,0-4 


^ 0.01625' 

and, eliminating e from these two expressions, gives 

p = 0.01625V = 1.135r4xl0-i^ 

that is, the power input varies with the fourth power of the 
resistance. 

Assuming the resistance r as proportional to the absolute 
temperature T, and considering that the power input into the 
lamp is radiated from it, that is, is the power of radiation P^, 
the equation between p and r also is the equation between P^ 
and T, thus, 

P, = A:T4; 

that is, the radiation is proportional to the fourth power of the 
absolute temperature. This is the law of black body radiation, 
and above equation of the volt-ampere characteristic of the 
tungsten lamp thus appears as a conclusion from the radiation 
law, that is, as a rational equation. 

154. Example 2. In a magnetite arc, at constant arc length, 
the voltage consumed by the arc, e, is observed for different 


EMPIRICAL CURVES. 


237 


values of current i. To find the equation of the volt-ampere 
characteristic of the magnetite arc : 

Table IV. 

VOLT-AMPERE CHARACTERISTIC OF MAGNETITE ARC. 


e 

log i 

log e 

(e-40) 

log (e- 40) 

(e-30) 

log (e-30) 

ec 

160 

9-699 

2-204 

120 

2- 079 

130 

2.114 

158 

120 

0000 

2-079 

80 

1-903 

90 

1954 

120-4 

94 

0301 

1-973 

54 

1-732 

64 

1806 

94 

75 

0-602 

1-875 

35 

1-544 

45 

1-653 

75-2 

62 

0-903 

1.792 

22 

1-342 

32 

1505 

62 

56 

1079 

1.748 

16 

1-204 

26 

1.415 

56-2 

0.5 

1 
2 

4 
8 

12 


-2 
+ 0-4 
0 

+ 0-2 

0 
+ 0-2 


^■3 = 0-000 5874 

^■3 = 2.584 4. 573 

^ = 2-584 -1301 

-1301 

a = = - 0 - 5034 ~ - 0 - 5 

2. 584 - 

i"6 = 2.584 10-447 

2. 584 X -0-5 = -1292 

^= 11-739 
11-739-^6= 1956 

log(e-30) = 1.956-0.5logi 

90- 4 

e— 30 =90-4*""* and e= '■ — =- 

30 + ^i 


The first four columns of Table IV give i, e, log i, log e. 
Fig. 80 gives the curves: i, e, as I; i, hge, as II; hgi, e, as 
III; log i, log e, as IV. 

Neither of these curves is a straight line. Curve IV is 
relatively the straightest, especially for high values of e. This 
points toward the existence of a constant term. The existence 
of a constant term in the arc voltage, the so-called " counter 
e.m.f. of the arc " is physically probable. In Table IV thus 
are given the values (e— 40) and log (e— 40), and plotted as 
curve V. This shows the opposite curvature of IV. Thus the. 
constant term is less than 40. Estimating by interpolation, and 
calculating in Table IV (e—SO) and log (e— 30), the latter, 
plotted against log i gives the straight line VI. The curve law 
thus is 

log (e-30) =A+a log ^. 


238 


ENGINEERING MATHEMATICS. 


Proceeding in Table IV in the same manner with logi 
and log (6—30) as was done in Table III with loge and logt, 
gives 

n=-0.5; A = loga = 1.956; and a = 90.4; 


Fig. 80. Investigation of Volt-ampere Characteristic of Magnetite Arc. 

hence 

log (e-30) = 1.956-0.5 log i"; 

e-30-90.4i;-o-5; 
90.4 


e = 30+- 


\% 


EMPIRICAL CURVES, 


239 


which is the equation of the magnetite arc volt-ampere charac- 
teristic. 

155. Example 3. The change of current resulting from a 
change of the conditions of an electric circuit containing resist- 
ance, inductance, and capacity is recorded by oscillograph and 
gives the curve reproduced as I in Fig. 81. From this curve 


log 

■\ 

"^ 

_^ 

^ 

H 

V 

i 

\ 

\ 

s 

0 A 

1 

\ 

\^ 

N 

\ 

\ 

\ 

\ 

\, 

\ 

\ 

N 

\^ 

] 

r 

\ 

V 

\ 
II 

\ 

1 n 

—) 

V*- 

\ 

N 

k 

y 

\, 

"< 

K 

iiA^ 

\ 

\, 

\. 

y:o 

\ 

\ 

\, 

\ 

\ 

i\ 

<.• 

N 

^ 

\ 

^ 

0 

4 

0 

8 

1 

2 

t 

1 

6 

2 

0 

2 

4 

2 

8 

Fig. 81. Investigation of Curve of Current Change in Electric Circuit. 

are taken the numerical values tabulated iis t and i in the first 
two columns of Table V. In the third and fourth columns are 
given log^ and \ogi, and curves then plotted in the usual 
manner. Of these curves only the one between t and logi 
is shown, as II in Fig. 81, since it gives a straight line for the 
higher values of t. For the higher values of t, therefore, 

\ogi = A~ht', or, ^ = a£~"*; 
that is, it is an exponential function. 


240 


ENGINEERING MATHEMATICS. 


Table V. 
TRANSIENT CURRENT CHARACTERISTICS. 


t 

i 

log< 

logi 

i 

11 = 
4.94£-1.07< 

i' = J 

log i' 

12 = 

2.85£-3.84« 

V = 

ii — 12 

1 

0 

2.10 

— 

0.322 

0 

4.94 

2.84 

0461 

2.85 

2. 09 

-0-01 

0.1 

2.48 

9.000 

0394 

0.1 

4.44 

1.96 

0.292 

1.94 

2.50 

+ 002 

0.2 

2-66 

5.301 

0.425 

02 

3.98 

1.32 

0.121 

1.32 

2.66 

0 

0.4 
0.8 

2.58 
2.00 

9.602 
9. 903 

0.412 
0.301 

0 8 

3.21 
2.09 

0.63 
009 

9.799 

0.61 
0.13 

2-60 
1.96 

+ 0.02 
-0-04 

8-954 

1.2 

1.36 

0079 

0134 

1.2 

1.36 

0 

— 

0.03 

1.33 

-0.03 

1.6 

090 

0.204 

9. 954 

1.6 

0.89 

-0.01 

— 

0.01 

0-88 

-0.02 

2.0 

0.58 

0301 

9. 763 

2.0 

0.58 

0 

— 

— 

0-58 

0 

2.5 

0.34 

0398 

9.531 

2.5 

0.34 

0 

— 

— 

0-34 

0 

3.0 

0.20 

0.477 

9.301 

3.0 

0.20 

0 

~ 

" 

0.20 

0 

13 =4.8 ^3 = 9.851 

^2 = 0.1 0.753 

48 9-851 

— ,= 1.6 ^-^^ = 9.950 

^■2 = 0. 6 9. 920 

3 ' 3 
^2 =5.5 ^"2 = 9. 832 

J 

^ = 0.5 -0.83; 

5.5 „ „, 9. 832 ^ „„ 
= 2.75 = 9. 416 

0.5Xlog £ = 0.217 

2 . 2 

^ = 1.15 ^ = -0.534 

n=— 3.J 

)4 

1.15Xlog £ = 0.499; n=-1.07 

^"4 = 0. 7 0653 

^"5 =10.3 i'5 = 8.683 

0.7Xlog£ = 0.304 

10. 3Xlog £ = 4.473 

O.S04X-3.84 = 

-1.16' 

1 
3 
5 

4. 473 X -1.107 

= -4. 784 

f = 1.82( 

^ = 3. 467 

1.820-4 = 045 

8.467-*-5 = 0.693 

log M = 0. 693-1 

07< log £ log t2 = 0 . 455 - 3 . 84« log e 

ti=^4.94£-1.07f 12= 2. 85 

E-3.84< 

ic = 

= 4.94e-1.07«-2.85s-3.84< 

To calculate the constants a and n, the range of values is 
used, in which the curve II is straight; that is, from t = \.2 
to ^ = 3. As these are five observations, they are grouped in two 
pairs, the first 3, and the last 2, and then for t and log i, one- 
third of the sum of the first 3, and one-half of the sum of the 
last 2 are taken. Subtracting, this gives, 

ii = 1.15; J log?: =-0.534. 

Since, however, the equation, i = a£~^\ when logarithmated, 
gives 

log i = log a—nt log s, 
thus A log i=—n log eAt, 


EMPIRICAL. CURVES. 241 

it is necessary to multiply M by log £ = 0.4343 before dividing it 
into log i to derive the value of n. This gives n== 1.07. 

Taking now the sum of all the five values of ty multiplying by 
log £, and subtracting from the sum of all the five values of 
log 1, 5A= 3.467; hence, 

A = log a =0.693, 
and 

log ii= 0.693 -1.07nog£; 

The current ii is calculated and given in the sixth column 
of Table V, and the difference ^' = J = ^l — ^ in the seventh 
column. As seen, from t = 1.2 upward, ii agrees with the 
observations. Below t = 1.2, however, a difference i' remains, 
and becomes considerable for low values of t. This difference 
apparently is due to a second term, which vanishes for higher 
values of t. Thus, the same method is now applied to the 
term i'; column 8 gives log^', and in curve III of Fig. 81 is 
plotted logi' against t. This curve is seen to be a straight 
line, that is, i' is an exponential function of t. 

Resolving t' in the same manner, by using the first four 
points of the curve, from ^ = 0 to ^ = 0.4, gives 

log 12 = 0.455 -3.84nog e; 

l2 = 2.85£-3-84^ 

and, therefore, 

^=^l_^2 = 4.94£-l•07^-2.85£-3•84« 

is the equation representing the current change. 

The numerical values are calculated from this equation 
and given under ic in Table V, the amount of their difference 
from the observed values are given in the last column of this 
table. 

A still greater approximation may be secured by adding 
the calculated values of 12 to the observed values of i in the 
last five observations, and from the result derive a second 
approximation of ii, and by means of this a second approxi- 
mation of ^2. 


242 


ENGINEERING MATHEMATICS. 


156. As further example may be considered the resolution 
of the core loss curve of an electric motor, which had been 
expressed irrationally by a potential series in paragraph 144 
and Table I. 

Table VI. 
CORE LOSS CURVE. 


e 
Volts. 

Pi kw. 

log e 

log Pi 

1.6 log e 

A=logPi 

-1.6 log e 

Pc 

J 

40 

0.63 

1.602 

9.799 

2.563 

7.236 

0.70 

-0.07 

60 

1.36 

1778 

0.134 

2.845 

7.289 

7.293 I avg. 

1.34 

+ 0.02 

80 

2.18 

1.903 

0.338 

3.045 

2.12 

+ 0.06 

100 

3. 00 

2.000 

0.477 

3.200 

7.277 7.282 

3. 03 

-0.03 

120 

3.93 

2.079 

0.594 

3.326 

7.268 J 

4.05 

-0.12 

140 

6.22 

2.146 

0.794 

3.434 

7. 360 

5.20 

+ 1.02 

160 

8.59 

2.204 

0.934 

3.526 

7-408 

6.43 

+ 2.16 

i-a 

= 5.283 

0.271 

lcgPt = 7.282 + 1.6loge 

^■3-3 

= 1.761 

0.090 

i't = 1.914e»«, in watts 

i-s 

= 4.079 

1.071 

2'2-f-2 

= 2.0395 

0.535 

A 

= 02785 

0.445 

r 

0.445 

= 1.598- 

1.6 

0.2785 

4 

The first two columns of Table VI give the observed values 
of the voltage e and the core loss Pi in kilowatts. The next 
two columns give log e and log Pi. Plotting the curves shows 
that loge, log Pi is approximately a straight Hne, as seen in 
Fig. 82, with the exception of the two highest points of the 
curve. 

Excluding therefore the last two points, the first five obser- 
vations give a parabolic curve. 

The exponent of this curve is found by Table VI as 
71=1.598; that is, with sufficient approximation, as n=1.6. 

To see how far the observations agree with the curve, as 
given by the equation, 

Pi=ae^'^ 


in the fifth column 1.6 log e is recorded, and in the sixth column, 
A = loga = logPi— 1.61oge. As seen, the first and the last 
two values of A differ from the rest. The first value corre- 


EMPIRICAL CURVES. 


243 


spends to such a low value of Pi as to lower the accuracy of 
the observation. Averaging then the four middle values, 
gives A = 7.282 ; hence, 

log Pf= 7.282 + 1.6 log e, 
Pi=1.914ei-»- in watts. 


1.6 

1.7 

1.8 

1.9 

2.0 

2.1 

2.2 

log 

Pi 

lo 

^e 

■ -J 

( 

Px 

/ 

kw. 

0^8 

/ 

6 

jd^ 

/ 

0:6 

/ 

/ 

,9\ 

/ 

f 

70 

0r4 

r 

\o>| 

hy 

( 

.<?^ 

Q.ar 

/ 

/ 

/ 

/<}.0 

n r\ 

/ 

/ 

/ 

K-n 

/ 

> 

/ 

Q Q_ 

/ 

/ 

/ 

^-fv 

/ 

/< 

» 

<? 

/ 

7 

i 

r^' 

-o.n 

y 

/ 

/" 

< 

^ 

"'^ 

0 

i 

) 

6 

) 

8 

) 

i=1'^=. 

JO 

1' 

0 

1( 

9 

Fig. 82. Investigation of Cuvres. 


This equation is calculated, as Pc, and plotted in Fig. 82. 
The observed values of Pi are marked by circles. As seen, 
the agreement is satisfactory, with the exception of the two 
highest values, at which apparently an additional loss appears, 
which does not exist at lower voltages. This loss probably is 
due to eddy currents caused by the increasing magnetic stray 
field resulting from magnetic saturation. 


244 


ENGINEERING MATHEMATICS. 


i57» As a final example may be considered the resolution 
of the magnetic characteristic, plotted as curve I in Fig. 83, 
and given in the first two columns of Table VII as OC and (B. 

Table VIL 
MAGNETIC CHARACTERISTIC. 


5C 

(B 
kUolines 

logSC 

log (B 

(B 

5C 

3C 
(B 

(B, 

J 

2 

30 

0-301 

0-477 

1-5 

0-667 

6-4 

+ 3.4 

4 

8-4 

0.602 

0-924 

2.1 

0-476 

9.7 

+ 1-3 

6 

11.2 

0-778 

1-049 

1867 

0-536 

11.6 

+ 0.4 

8 

13-0 

0-903 

1-114 

1.625 

0 614 

13.0 

0 

10 

14-0 

1-000 

1-146 

1.40 

0715 

13.9 

-0.1 

15 

15-4 

1-176 

1.188 

1.033 

0974 

15-45 

+ 0.05 

20 

16-3 

1-301 

1.212 

0.815 

1-227 

16-3 

0 

30 

17-2 

1.477 

1.236 

0573 

1-74 

17.3 

+ 0.1 

40 

17-8 

1.602 

1.250 

0-445 

2-25 

17-8 

0 

60 

18. 5 

1.778 

1.267 

0308 

3-25 

18-4 

-0.1 

80 

188 

1.903 

1.274 

0-235 

4-25 

188 

0 

^4 = 53 

3-530 

/ 

^•4 = 210 

11-49 

^ = 157 

7J6 

157 

= 0-0507 

7. 96 

^■8 = 263 

26C 

5X0-0507 = 
1-686-8 = 

15. 020 
=13-334 

= 1-686 
= 0-211 

5C 

.211+0-0£ 

,073C and 

(B= — 

02 

5C 

11+0-0507 

3C' 

Plotting 5C, (B, log 5C, log (B against each other leads to no 
results, neither does the introduction of a constant term do 
this. Thus in the fifth and sixth columns of Table VII are 

calculated -zz and — , and are plotted against 5C and against (B. 

Of these four curves, only the curve of — against 5C is shown 

in Fig. 83, as II. This curve is a straight line with the exception 
of the lowest values; that is, 


(B 


a+h5C. 


EMPIRICAL CURVES. 


245 


Excluding the three lowest values of the observations, as 

not lying on the straight line, from the remaining eight values^ 

as calculated in Table VII, the following relation may be 

derived, 

3C 
--^0.211+0.0507 5C, 

05 


■■■^~~ 

y 

7\ 

/ 

- 

/ 

3:5 

/ 

A 

ii;X) 

/ 

/ 

on 

^ 

/ 

„ 

\ 

— 

^— 

y 

I 

X 

^' 

/ 

/ 

/ 

1.5 

f 

/ 

c 

1 n r 

/ 

i 

o 

/ 

i 

/ 

>^ 

1 

r 

4 

1 

3 

2 

3 

2 

0 

^ 

0 

^r 

0 

e 

D 

7 

> 

sb 

Fig. 83. Investigation of Magnetization Curve, 
and herefrom, 

5C 


(B = 


0.211 +0.0507 5C 


is the equation of the magnetic characteristic for values of 3C 
from eight upward. 

The values calculated from this equation are given as (B 
in Table VII. 


246 ENGINEERING MATHEMATICS. 

nn 

The difference between the observed values of-^, and the 

value given by above equation, which is appreciable up to 
JC=-6, could now be further investigated, and would be found 
to approximately follow an exponential law. 

D. Periodic Curves. 

158. All periodic functions can be expressed by a trigo- 
nometric series, or Fourier series, as has been discussed in 
Chapter III, and the methods of resolution and arrangements 
devised to carry out the work rapidly have also been dis- 
cussed in Chapter III. 

The resolution of a periodic function thus consists in the 
determination of the higher harmonics, which are super- 
imposed on the fundamental wave. 

As periodic curves are of the greatest importance in elec- 
trical engineering, in the theory of alternating-current phe- 
nomena, a familiarity with the wave shapes produced by the 
different harmonics is desirable. This familiarity should be 
sufficient to enable one to judge immediately from the shape 
of the wave, as given by oscillograph, etc., which harmonics 
are present. 

The effect of the lower harmonics, such as the third, fifth, 
seventh, etc. (or the second, fourth, etc., where present), is 
to change the shape of the wave, make it differ from sine 
shape, and in the '' Theory and Calculation of Alternating- 
current Phenomena," 4th. Ed., Chapter XXX, a number of 
characteristic distortions, such as the flat top, peaked wave, saw 
tooth, double and triple peaked, sharp zero, flat zero, etc., have 
been discussed with regard to the harmonics that enter into 
their composition. 

159. High harmonics do not change the shape of the wave 
much, but superimpose ripples on it, and by counting the 
number of ripples per half wave, or per wave, the order of the 
harmonic can rapidly be determined. For instance, the wave 
shown in Fig. 84 contains mainly the eleventh harmonic, as 
there are eleven ripples per wave (Fig. 84). 

Very frequently high harmonics appear in pairs of nearly 
the same frequency and intensity, as an eleventh and a thir- 


EMPIRICAL CURVES. 247 

teenth harmonic, etc. In this case, the ripples in the wave 
shape show maxima, where the two harmonics coincide, and 
nodes, where the two harmonics are in opposition. The 
presence of nodes makes the counting of the number of ripples 
per complete wave more difficult. A convenient method of 
procedure in this case is, to measure the distance or space 


Fig. 84. Wave in which Eleventh Harmonic Predominates. 

between the maxima of one or a few ripples in the .range where 
they are pronounced, and count the number of nodes per 
cycle. For instance, in the wave. Fig. 85, the space of two 
ripples is about 60 deg., and two nodes exist per complete 

wave. 60 deg. for two ripples, gives 2 X-:^= 12 ripples per 


Fig. 85. Wave in which Eleventh .and Thirteenth Harmonics Predominate. 

complete wave, as the average frequency of the two existing 
harmonics, and since these harmonics differ by 2 (since there 
are two nodes), their order is the eleventh and the thirteenth 
harmonics. 

This method of determining two similar harmonics, with a 
little practice, becomes very convenient and useful, and may 


248 ENGINEERING MATHEMATICS. 

frequently be used visually also, in determining the frequency 
of hunting of synchronous machines, etc. In the phenomenon 
of hunting, frequently two periods are superimposed, forced 
frequency, resulting from the speed of generator, etc., and the 
natural frequency of the machine. Counting the number of 
impulses, /, per minute, and the number of nodes, n, gives the 

71/ Tl 

two frequencies :/+- and/— -; and as one of these frequencies 

is the impressed engine frequency, this affords a check. 

Not infrequently wave-shape distortions are met, which 
are not due to higher harmonics of the fundamental wave, 
but are incommensurable therewith. In this case there are 
two entirely unrelated frequencies. This, for instance, occurs 
in the secondary circuit of the single-phase induction motor; 
two sets of currents, of the frequencies /« and (2/—/^) exist 
(where / is the primary frequency and /s the frequency of 
slip). Of this nature, frequently, is the distortion produced by 
surges, oscillations, arcing grounds, etc., in electric circuits; 
it is a combination of the natural frequency of the circuit 
with the impressed frequency. Telephonic currents commonly 
show such multiple frequencies, which are not harmonics of 
each other.
