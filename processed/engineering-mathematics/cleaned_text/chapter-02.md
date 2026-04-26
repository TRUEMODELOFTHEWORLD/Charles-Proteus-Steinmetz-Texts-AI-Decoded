CHAPTER II. 
POTENTIAL SERIES AND EXPONENTIAL FUNCTION. 

A. GENERAL. 

39. An expression such as 

y-xk w 

represents a fraction; that is, the result of division, and hke 
any fraction it can be calculated; that is, the fractional form 
eliminated, by dividing the numerator by the denominator, thus : 

l-x l = l+x + x2 + a:3 + . . . 
l-x 

x—x^ - 


x-—x^ 

-^x\ 

Hence, the fraction (1) can also be expressed in the form: 


( 2/=TX~^-'^"^^ + ^^'^^'^' • • 


(2) 


This is an infinite series of successive powers of x, or a poten- 
tial series. 

In the same manner, by dividing through, the expression 

y^ih' ■ ^^^ 

can be reduced to the infinite series, 

y=j^ = l-x-hx^-x^+- |(4) 

52 


POTENTIAL SERIES AND EXPONENTIAL FUNCTION. 53 

The infinite series (2) or (4) is another form of representa- 
tion of the expression (1) or (3), just as the periodic decimal 
fraction is another representation of the common fraction 
(for instance 0.6363 = 7/11). 

40. As the series contains an infinite number of terms, 
in calculating numerical values from such a series perfect 
exactness can never be reached: since only a finite number of 
terms are calculated, the result can only be an approximation. 
By taking a sufficient number of terms of tlie series, however, 
the approximation can be made as close as desired; that is, 
numerical values may be calculated as exactly as necessary, 
so that for engineering purposes the infinite series (2) or (4) 
gives just as exact numerical values as calculation by a finite 
expression (1) or (2), provided a sufficient number of terms 
are used. In most engineering calculations, an exactness of 
0.1 per cent is sufficient; rarely is an exactness of 0.01 per cent 
or even greater required, as the unavoidable variations in the 
nature of the materials used in engineering structures, and the 
accuracy of the measuring instruments impose a hmit on the 
exactness of the result. 

For the value x = 0.5, the expression (1) gives y = z. — p-^ = 2; 

while, its representation by the series (2) gives 

2/ = 1+0.5 + 0.25+0.125+0.0625 + 0.03125 + ... (5) 

and the successive approximations of the numerical values of 
y then are : 

xising one term: y=l =1; error: —1 

" tw^o terms: i/=l + 0.5 =1.5; " -0.5 

" three terms: ?/= 1 + 0.5+ 0.25 =1.75" '" -0.25 

" four terms: 2/=l + 0.5+0.25+0.125 =1.875; " -0.125 

'' five terms: ?/ = 1 + 0.5+0.25+0.125+0.0625= 1.9375 " -0.0625 

It is seen that the successive approximations come closer and 
closer to the correct value, y = 2, but in this case always remain 
below it; that is, the series (2) approaches its limit from below, 
as shown in Fig. 24, in which the successive approximations 
are marked by crosses. 

For the value re = 0.5, the approach of the successive 
approximations to the Hmit is rather slow, and to get an accuracy 
of 0.1 per cent, that is, bring the error down to less than 0.002, 
requires a considerable number of terms. 


54 ENGINEERING MATHEMATICS. 

For a: = 0.1 the series (2) is 

2/ = l +0.1 +0.01 +0.001 +0.0001+ (6) 

and the successive approximations thus are 


1: 
2: 
3: 

2/ = l.ll; 

4: 

2/=i.ni; 

5: 

2/=i.iiii; 

and as, 

by (1), 

the final or Umiting value is 

y=Y 

1 10 

1.1111 ... 

-0.1 9 

j^ 

+ 

+ 4 
3 

* "6 

/^ 

< 

V' 

■-, 

Fig. 24. Direct Convergent Series with One-sided Approach. 

the fourth approximation already brings the error well below 
0.1 per cent, and sufficient accuracy thus is reached for most 
engineering purposes by using four terms of the series. 
41. The expression (3) gives, for x = 0.5, the value. 

Represented by series (4), it gives 

2/ = l-0.5 + 0.25 -0.125+0.0625 -0.03125+ - (7) 

the successive approximations are; 

1st: 2/=l =1; error: +0.333... 

2d: 2/=l-0.5 =0.5; " -0.1666... 

3d: i/=l-0.5+0.25 =0.75; " +0.0833... 

4th: 2/- 1-0.5+0.25-0.125 =0.625; " -0.04166... 

oth: 2/= 1-0.5+0.25-0.125+0.0625 = 0.6875; " +0.020833... 

As seen, the successive approximations of this series come 
closer and closer to the correct value ?/ = 0.6666 . . . , but in this 
case are alternately above and below the correct or limiting 


POTENTIAL SERIES AND EXPONENTIAL FUNCTION, 55 

value, that is, the series (4) approaches its limit from both sides, 
as shown in P'ig. 25, while the series (2) approached the Umit 
from below, and still other series may approach their limit 
from above. 

With such alternating approach of the series to the limit, 
as exhibited by series (4), the limiting or final value is between 
any tw^o successive approximations, that is, the error of any 
approximation is less than the difference betw^een this and the 
next following approximation. 

42. Substituting x = 2 into the expressions (1) and (2), 
equation (1) gives 


\ 


3 

+ 


5 


i 


^~l+x 


Fig. 25. Alternating Convergent Series. 

while the infinite series (2) gives 

2/ = l+2-r4+8 + 16+32 + ...; 

and the successive approximations of the latter thus are 

1; 3; 7; 15; 31; 63...; 

that is, the successive approximations do not approach closer 
and closer to a final value, but, on the contrary, get further and 
further aw^ay from each other, and give entirely wrong results. 
They give increasing positive values, which apparently approach 
oo for the entire series, while the correct value of the expression, 
by (1), is2/= -1. 

Therefore, for x = 2, the series (2) gives unreasonable results, 
and thus cannot be used for calculating numerical values. 

The same is the case with the representation (4) of the 
expression (3) for x = 2. The expression (3) gives 

J/=Y^ = 0.3333...; 


56 ENGINEERING MATHEMATICS. 

while the infinite series (4) gives 

2/ = l -2+4-8 + 16-32+ -.. ., 

and the successive approximations of the latter thus are 

1; -1; +3; -5; +11: -21; . . .: 

hence, while the successive values still are alternately above 
and below the correct or limiting value, they do not approach 
it with increasing closeness, but more and more diverge there- 
from. 

Such a series, in which the values derived by the calcula- 
tion of more and more terms do not approach a final value 
closer and closer, is called divergent, while a series is called 
convergent if the successive approximations approach a final 
value with increasing closeness. 

43 • While a finite expression, as (1) or (3), holds good for 
all values of x, and numerical values of it can be calculated 
whatever may be the value of the independent variable x, an 
infinite series, as (2) and (4), frequently does not give a finite 
result for every value of x, but only for values within a certain 
range. For instance, in the above series, (for —1 <x< + l, 
the series is convergent; while for values of x outside of this /^a 
range the series is divergent and thus useless. J jn^ 

AVhen representing an expression by an infinite series, 
itXnus<is necessary to determine that the series is convergentJ> 
tnat is, approaches with increasing number of terms a finite^^ 
limiting value, <otherwise the series cannot be used.y Wheret 
the series is convergent within a certain range of'^x, diver- 
gent outside of this range, it can be used only in the range of 
convergency, but outside of this range it cannot be used ffor 
deriving numerical values;);;but some other form of representa- 
tion has to be found w^hicl^ is convergent^ 

This can frequently be done, and the expression thus repre- 
sented by one series in one range and by another series in 

another range. For instance, the expression (1), 2/ = t— :, by 

substitutins;, x = -, can be written in the form 

1 u 

i+- 

u 


POTENTIAL SERIES AND EXPONENTIAL FUNCTION. 57 

and then developed into a series by dividing the numerator 
by the denominator, which gives 

or, resubstituting x, 

1111 

y~x~x^^x^~x^^-"' .... (8) 

which is convergent for x = 2, and for a: = 2 it gives 

2/ = 0.5 -0.25 +0.125 -0.0625 + . . . (9) 
With the successive approximations : 

0.5; 0.25; 0.375; 0.3125. . ., 
which approach the final limiting value, 

2/ = 0.333. . . 

44. An infinite series can be used only if it is convergent. 
Mathemetical methods exist for determining whether a series 
is convergent or not. For engineering purposes, however, 
these methods usually are unnecessary; /for practical use it 
is not sufficient that a series be convergent, but it must con- 
verge so rapidly — ^that is, the successive terms of the series 
must decrease at such a great rate — that accurate numerical 
results are derived by the calculation of only a very few terms'^ 
two or three, or perhaps three or four. This, for instancd^ 
is the case with the series (2) and (4) for a; = 0.1 or less. For 
x = 0.5, the series (2) and (4) are still convergent, as seen in 
(5) and (7), but are useless for most engineering purposes, as 
the successive terms decrease so slowly that a large number 
of terms have to be calculated to get accurate results, and for 
such lengthy calculations there is no time in engineering work. 
If,\ however, (the successive terms of a series decrease at such 
a rapid rate that all but the first few terms can be neglected, 
the series is certain to be convergent.) 

In a series therefore, in which there is a question whether 
it is convergent or divergent, as for instance the series 

.11111 

^^ "^2 "^3 "^4 "^5 "^6 "^' • • (<^^^e^gen^)^ 


58 ENGINEERING MATHEMATICS. 

or 

,11111 
y- 1 -"2 +3 - J +g - jT -f . . . (convergent), 

the matter of convergeney is of little imjx)rtancc for engineer- 
ing calculation, as the scri(»H is useh^ss in any case; that is, does 
not give accurate numerical results with a reasonably moderat/C 
amount of calculation. 
^ ' <^A series, to be usable for engineering work, must have 
the successive terms decreasing at a very rapid rat(% and if 
this is the case, the series is convergent, and the mathematical 
investigations of convergtmcy thus usually becomes unnecessary 
in engineering work^ 

45. It would rarely be advantageous to develop such simple 
expressions as (1) and (3) into infinite series, such as (2) and 
(4), since the calculation of numerical values from (1) and (3) 
is simpler than from the series (2) and (4), even though very 
few terms of the s(»ries ncuul to Ixi used. 

The use of the scTies^ (2) or (4) instea<l of the expressions 
(1) and (3) ther(*fore( is advantageous only if these series( con- 
verges so rapidly that only \\\v first two terms are nvjuinMl 
for numerical calculation,] and the third term is negligible*; 
that is, for very small values of j. Thus, for xs-O.Ol, accord- 
ing to (2), 

t/ = 1 +0.01 +0.0001 +. . . = 1 +0.01, 

as the next term, 0.0001, is aln^ady less than 0.01 per cent of 
the value of the total expression, 
y For very small values of j*, then^fore,)by (1) and (2), 

U-— i-l+A (10) 

and by (3) and (4), 


\ 


and tnese expressions (lO) and (11) arc useful and very com- 
monly used in engineering calculation for sim{)lifying work. 
For instance, if 1 i)lus or minus a very small (luantity appears 
as factor in the denominator of an expn\ssion, it can Ix* replaced 
by 1 minus or plus the same small quantity as factor in the 
numerator of the expression, and inversely. 


For exainplo, if a direct-current receiving circuit, of resist- 
ance r, is fed by a supply voltagt^ cq over a line of low 
Resistance ro, what is the voltage e at the ix?ceiving circuit? 

The total resistance is r=f tq; hence, the current, t = ' . , 
and the voltage at the receiving circuit is 

^-r^-^o— (12) 

If now To is small compared with r, it is 

1-?^} (13) 


1 
r 


As; flic next ItM'm (»r the sorit>s woiiM In* ( -) . the errui 

\/7 ' 
made by the simpler expression (13) is less than ( — ) . Thus, 
if To is 3 per cent of r, which is a fair average in interior light- 
ing circuits, {-) =0.032 = 0.0009, or less than 0.1 percent; 

hence, is usuall^^ negligible. 

46. If an expression in its finite form is moi*e complicated 
and thereby less convenient for numerical calculation, as for 
instance if it contains roots, development into an infinite series 
frequently simplifies the calculation. 

Very convenient for development into an infinite series 
of powers or roots, is the binomial theorem, 


(14) 


X * n(n-l) _ n(n-l)(n-2) ^ 

If II 4 

where 

|w«-lX2x3X. . .Xm. 

Thus, for instance, in an alternating-current circuit of 
resistance r, reactance x, and supply voltage e, the curi-ent is. 


^■v^T7^ "^) 


60 ENGINEERING MATHEMATICS. 

If this circuit is practically non-inductive, as an incandescent 
lighting circuit; that is, if x is small compared with r, (15) 
can be written in the form, 


._ e e 


h©T', . . . ae, 


and the square root can be developed by the binomial (14), thus, 
u= yyj ; n= --, and gives 

h(r)T*=-i(7)"-s(r)'-f.(")'-- <■:) 

In this series (17), if x = 0.1r or less; that is, the reactance 
is not more than 10 per cent of the resistance, the third term, 

Q ( - ) , is less than 0.01 per cent; hence, negligible, and the 

series is approximated with sufficient exactness by the fii-st 
two terms, 

and equation (16) of the current then gives 

-tI'-I©! « 

This expression is simpler for numerical calculations than 
the expression (15), as it contains no square root. 

47. Development into a series may become necessary, if 
further operations have to be carried out with an expression 
for which the expression is not suited, or at least not well suited. 
This is often the case where the expression has to be integrated, 
since very few expressions can be integrated. 

{ Expressions under an integral sign therefore very commonly 
have to be developed into an infinite series to carry out the 
integration. \ 


POTENTIAL SERIES AND EXPONENTIAL FUNCTION. 61 


EXAMPLE 1. 

Of the equilateral hyperbola (Fig. 26), 

xy = a^, (20) 

the length L of the arc between Xi=2a and 0:2 = 10a is to be 
calculated. 

An element dl of the arc is the hypothenuse of a right triangle 
with dx and dy as cathetes. It, therefore, is, 


dl = Vdx^+dy'^ 


-MH)'" «» 


\ 

\ 

\ 

\ 

\ 

\ 

V 

V 

d> 

% 

xy= 

-.a- 

iCi 

-£ 

r. 

and from (20), 


Fig. 26. Equilateral Hyperbola. 


dy 


^=7 ^^^ dx 


Substituting (22) in (21) gives, 

hence, the length L of the arc, from xi to X2 is. 


(22) 


(23) 


(24) 


62 ENGINEERING MATHEMATICS. 


Substituting - = v; that is, dx = adv, also substituting 

Vi=-=2 and 2;, = - =10, .... (25) 


gives 

r^' i r 

,4^^' (26) 


4SyF^^ 


The expression under the integral is inconvenient for integra- 
tion; it is preferably developed into an infinite series, by the 
binomial theorem (14). 

Write u = -2 and n = -^, then 


V 


1^^ ±_J_ _i ^ 

and 

L 1 1 1 


[ 2X3XV* 7X8X2;8 11X16X2;^^ 

+ I + 1 

3X128X1-16 J 

and substituting the numerical values, 
L = a\ (10-2) +i(0.125-0.001) 

-^(0.0078-0) +-47^(0.0001 -0) ■ 
5b 17d 

= a{8 +0.0207-0.0001} = 8.0206a. 

As seen, in this series, only the first two terms are appreciable 
in value, the third term less than 0.01 per cent of the total, 
and hence negligible, therefore the series converges very 
rapidly, and numerical values can easily be calculated by it. 


POTENTIAL SERIES AND EXPONENTIAL FUNCTION, 63 

For xi<2 a; that is, Vi <2, the series converges less rapidly, 
and becomes divergent for xi<a; or, Vi<l. Thus this series 
(17) is convergent for v>l, but near this limit of convergency 
it is of no use for engineering calculation, as it does not converge 
with sufficient rapidity, and it becomes suitable for engineering 
calculation only when V} approaches 2. 

EXAMPLE 2. 

48. (log 1=0, and, therefore log (1-hx) is a small quantity 
if X is small. / log (l+x) shall therefore be developed in such 
a series of powers of x, which permits its rapid calculation 
without using logarithm tables. 

It is 

log«=J -; 
then, substituting (1+x) for u gives, 

^log(l+.r)=Jj^^ (18) 

From equation (4) 

■z = l — X-hX^ — X^ + . . . , 

1+x ' • 

hence, substituted into (18), 

I0g(l^.)^=/(1-X..-X3....).. 

( = i dx- I xdx + j x^dx — I x^dx + . . . 

x^ x^ x/^ ,^^, 

= :c— 2+3--4-+ ••• ; (19) 


V 


x 


hence, if x is very small, — is negligible, and, therefore, all 

terms beyond the first are negligible, thus, 

log(l4-a;j=x; (20) 

while, if the second term is still appreciable in value, the more 
complete, but still fairly simple expression can be used. 


( 

^ 


log(l+a:) = x-|' = x(l-|) (21) 


64 ENGINEERING MATHEMATICS. 

If instead of the natural logarithm, as used above^ the 
decimal logarithm is required, the following relation may be 
applied : 

logio a = logio£ logs a = 0.4343 logs a, . . (22) 

logio ci is expressed by logs cl, and thus (19), (20) (21) assume 
the form. 


logio(l+:r)=0.4343(^x--+-— j+... j; . (23) 
or, approximately, 

logio(l+a:)=0.4343x; • (24) 

or, more accurately, 

logio(l+.T)=0.4343x(l-|). . ; . (25) 

B. DIFFERENTIAL EQUATIONS. 

49. The representation by an infinite series is of special 
value in those cases, in which no finite expression of the func- 
tion is known, as for instance, if the relation between x and y 
is given by a differential equation. 

Differential equations are solved by separating the variables, 
that is, bringing the terms containing the one variable, 2/, on 
one side of the equation, the terms with the other variable x 
on the other side of the equation, and then separately integrat- 
ing both sides of the equation. Very rarely, however, is it 
possible to separate the variables in this manner, and where 
it cannot be done, usually no systematic method of solving the 
differential equation exists, but this has to be done by trying 
different functions, until one is found which satisfies the 
equation. 

In electrical engineering, currents and voltages are dealt 
with as functions of time. The current and c.m.f. giving the 
power lost in resistance are related to each other by Ohm's 
law. Current also produces a magnetic field, and this magnetic 
field by its changes generates an e.m.f. — the e.m.f. of self- 
inductance. In this case, e.m.f. is related to the change of 
current; that is, the differential coefficient of the current, and 
thus also to the differential coefficient of e.m.f., since the e.m.f. 


POTENTIAL SERIES AND EXPONENTIAL FUNCTION. 65 

is related to the current by Ohm's law. In a condenser, the 
current and therefore, b}^ Ohm's law, the e.m.f., depends upon 
and is proportional to the rate of change of the e.m.f. impressed 
upon the condenser; that is, it is proportional to the differential 
coefficient of e.m.f. 

Therefore, in circuits having resistance and inductance, 
or resistance and capacity, a relation exists between currents 
and e.m.f s., and their differential coefficients, and in circuits 
having resistance, inductance and capacity, a double relation 
of this kind exists; that is, a relation between current or e.m.f. 
and their first and second differential coefficients. 

The most common differential equations of electrical engineer- 
ing thus are the relations betw^een the function and its differential 
coefficient, which in its simplest form is, 

i=»^ ««) 

or 

'!""■ ' (»' 

and where the circuit has capacity as well as inductance, the 
second differential coefficient also enters, and the relation in 
its simplest form is, 

§'-r. (=») 

or 

S-^' (29) 

and the most general form of this most common differential 
equation of electrical engineering then is, 

g+2c|+«2/+6=0 (30) 

The differential equations (26) and (27) can be integrated 
by separating the variables, but not so with equations (28), 
(29) and (30); the latter require' solution by trial. 

50. The general method of solution may be illustrated with 
the equation (26) : 

i-» « 


66 ENGINEERING MATHEMATICS. 

To determine whether this equation can be integrated by an 
infinite series, choose such an infinite series, and then, by sub- 
stituting it into equation (26), ascertain whether it satisfies 
the equation (26) ; that is, makes the left side equal to the right 
side for every value of x. 

Let, 

y^ao-^aix±a2x'^ + a'6X^-\-a^x^-\- (31) 

be an infinite series, of which the coefficients (Iq, a\, ao, as. . . 
are still unknown, and by substituting (31) into the differential 
equation (26), determine whether such values of these coefficients 
can be found, which make the series (31) satisfy the equation (26). 
Differentiating (31) gives, 

-^--ai+2a2X+Sa3X^+4:a4X^ + (32) ^ 

The differential equation (26) transposed gives, 

J-^^=0 • • (33). 

Substituting (31) and (32) into (33), and arranging the terms 
in the order of x, gives, 

(ai — ao) + (2a2 — ai)x + {Sas — a2)x^ 

+ {4:a4'^3)x^ + (5a5-ai)x^ + . . .=0. . (34) 

If then the above series (31) is a solution of the differential 
equation (26), the expression (34) must be an identity; that is, 
must hold for every value of x. 

If, however, it holds for every value of x, it does so also 
for x = 0, and in this case, all the terms except the first vanish, 
and (34) becomes, 

ai — ao = 0; or, ai=ao (35) 

To make (31) a solution of the differential equation (ai — ao) 
must therefore equal 0. This being the case, the term (ai — ao) 
can be dropped in (34), which then becomes, 

(2a2~ai)x + {Sa3-a2)x^ + {4:a4—a3)x^ + (^a5-a4)x'^ + . . .=0; 

or, 

a'{(2a2-ai) + (3a3-a2)x- + (4a4-a3\r2 + . . .{=0. 


POTENTIAL SERIES AND EXPONENTIAL FUNCTION. 67 

Since this equation must hold for every value of x, the second 
term of the equation must be zero, since the first term, x, is 
not necessarily zero. This gives, 

fe— «i)+(3a3 — a2)a: + (4a4- 03)^2 + . . .=0. 

As this equation holds for every value of x, it holds also for 
x = 0. In this case, however, all terms except the first vanish, 
and, 

2a2-ai=0; (36) 

hence. 


02=2' 

from (35), 

Continuing the same reasoning, 

3a3-a2 = 0, 4a4— 03=0, etc. 

Therefore, if an expression of successive powers of x, such as 
(34), is an identity, that is, holds for every value of x, then all 
the coefficients of all the powers of x must separately he zero."^ 

Hence, 

ai — aQ=0] or ai = ao; 


(37) 


2a2-ai=0; 

or GL2—^=-^] 

3a3-;^2 = 0; 

a2 «o 
or a3=^3=-3; 

4a4-3a3=0; 

«,3 «0 

ov a^=j=j; 
etc. 

etc., 

* The reader must realize the difference between an expression (34), as 
equation in x, and as substitution product of a function; that is, an as 
identity. 

Regardless of the values of the coefficients, an expression (34) as equation 
gives a number of separate values of a:, the roots of the equation, which 
make the left side of (34) equal zero, that is, solve the equation. If, however, 
the infinite series (31) is a solution of the differential equation (26), then 
the expression (34), which is the result of substituting (31) into (26), must 
be correct not only for a limited number of values of x, which are the roots 
of the equation, but for all values of x, that is, no matter what value is 
chosen for x, the left side of (34) must always give the same result, 0, that 
is, it must not be changed by a change of x, or in other words, it must not 
contain x, hence all the cpefficients of the powers of x must be zero. 


68 


ENGINEERING MATHEMATICS. 


(39) 


Therefore, if the coefficients of the series (31) are chosen 
by equation (37), this series satisfies the differential equation 
(is); that is, 

r ^2 ^3 ^4 ] 

2/ = ao{l+x+-2+T3+p- + ...j. . . . (38) 
is the solution of the differential equation, 

51. In the same manner, the differential equation (27), 

dz 

Tx-""'' ■ ■ • 

is solved by an infinite series, 

z = ao^-aiX-\-a2x'^-\-azX^-\-. . ., .... (40) 

and the coefficients of this series determined by substituting 
(40) into (39), in the same manner as done above. This gives, 

(ai — aao) + {2a2 — aai)x + {Za^ — aa2)x'^ 

+ (4a4-aa3)a:3 + . . .=0, . (41) 

and, as this equation must be an identity, all its coefficients 
must be zero; that is, 

ai — aao = 0; or ai = aao; 

a a2 
2a2—aai=0; or a2 = ai-^ = ao-:^ 


Sas — aa2 = 0 ; or as = 02 ^ = ao 75- 
4a4— aa3 = 0; or 04 = as 


ao^ 


(42) 


3 

a 
4 
etc., etc. 

and the solution of differential equation (39) is, 

( a%2 a^x^ a^x^ ] ,^^^ 

2: = ao|l+ax+-2-+-|3-+-n- + ...j. . . (43) 

52. These solutions, (38) and (43), of the differential equa- 
tions (26) and (39), are not single solutions, but each contains 
an infinite number of solutions, as it contains an arbitrary 


POTENTIAL SERIES AND EXPONENTIAL FUNCTION. 69 

constant ao] that is, a constant which may have any desired 
numerical vahie. 

This can easily be seen^ since, if ^ is a solution of the dif- 
ferential equation, 

dz 
dx 

then, any multiple, or fraction of z, hz, also is a solution of the 
differential equation; 

d{hz) .. . 

since the 6 cancels. 

Such a constant, ao, which is not determined by the coeffi- 
cients of the mathematical problem, but is left arbitrary, and 
requires for its determinations some further condition in 
addition to the differential equation, is called an integration 
constant. It usually is determined by some additional require- 
ments of the physical problem, which the differential equation 
represents; that is, by a so-called terminal condition, as, for 
instance, by having the value of y given for some particular 
value of X, usually for x = 0, or x=qc. 

The differential equation, 

i-r. («> 

thus, is> solved by the function, 

y = aoyo, (45) 

where, 

7>2 'Y'3 '1^4 

i/o = l+x+-+i3+jj + ..., .... (46) 

and the differential equation, 

-r = a^, (47) 

dx ' ' 

is solved by the function, 

z = aoZo, . (48) 

where, 

a^x^ aV a4.r4 
Zo = l+ax-\-—^+-r^+-r^+ (49) 


70 ENGINEERING MATHEMATICS. 

yo and zq thus are the simplest forms of the solutions y and z 
of the differential equations (26) and (39). 

53. It is interesting now to determine the value of ?/". To 
raise the infinite series (46), which represents 2/0 ; to the nth 
power, would obviously be a very complicated operation. 

However, 

-i^'^y-'d' ^50) 

dv 
and since from (44) w~""2/; • • • (51) 

by substituting (51) into (50), 

dv"' 

-h-^r-' (52) 

hence, the same equation as (47), but with ?/" instead of z. 
Hence, if y is the solution of the differential equation, 

dy 

then z = y'^ is the solution of the differential equation (52), 

dz 

-y- = nz. 
dx 

However, the solution of this differential equation from (47), 
(48), and (49), is 

z = aQZo'y 


ZQ = l+nx-\- 
that is, if 


2o = l+na:+-Y--f-j^-f-. 


then, 

ZQ = yo'^ = ^+rix^-Y+-w-^'") • • • (53) 

therefore the series y is raised to the nth power by multiply- 
ing the variable x by n. 


POTENTIAL SERIES AND EXPONENTIAL FUNCTION. 71 

Substituting now in equation (53) for n the value - gives 

2^^T = i + i+i+-+_ + ... : .... (54) 

that is, a constant numerical value. This numerical value 

equals 2.7182828. . ., and is usually represented by the symbol e. 

Therefore, 

j_ 

2/0^ = ^' 
hence, 

^2 j3 j4 

2/o = c- = l+x+-+jj+p- + ..., (55) 

and 

n~X^ Tl^X^ 71'^X'^ 

2;o = 2/o'' = (-'^)"=-'"'' = l+^-c+-^+-|^+-j^ + . . . ; (56) 

therefore, the infinite series, which integrates above differential 
equation, is an exponential function with the base 

£ = 2.7182818 (57) 

The solution of the differential equation, 

t- '=«' 

thus is, 

2/ = «o^^ (5^) 

and the solution of the differential equation, 

%=^y^ ^'''^ 

is, 

2/ = «o-'^^ (^>1) 

where aQ is an integration constant. 

The exponential function thus is one of the most common 
functions met in electrical engineering problems. 

The above described method of solving a problem, by assum- 
ing a solution in a form containing a number of unknown 
coefficients, Oq, ai, a2 . . ., substituting the solution in the problem 
and thereby determining the coefficients, is called the method 
of indeterminate coefficients. It is one of the most convenient 


72 ENGINEERING MATHEMATICS. 

and most frequently used methods of solving engineering 
problems. 

EXAMPLE 1. 

54. In a 4-pole 500-volt 50-kw. direct-current shunt motor, 
the resistance of the field circuit, inclusive of field rheostat, is 
250 ohms. Each field pole contains 4000 turns, and produces 
at 500 volts impressed upon the field circuit, 8 megalines of 
magnetic flux per pole. 

What is the equation of the field current, and how much 
time after closing the field switch is required for the field cur- 
rent to reach 90 per cent of its final value? 

Let r be the resistance of the field circuit, L the inductance 
of the field circuit, and i the field current, then the voltage 
consumed in resistance is, 


In general, in an electric circuit, the current produces a 
magnetic field; that is, lines of magnetic flux surrounding the 
conductor of the current ; or, it is usually expressed, interlinked 
with the current. This magnetic field changes with a change of 
the current, and usually is proportional thereto. A change 
of the magnetic field surrounding a conductor, however, gen- 
erates an e.m.f. in the conductor, and this e.m.f. is proportional 
to the rate of change of the magnetic field; hence, is pro- 
portional to the rate of change of the current, or to 

di . 

-T., with a proportionality factor L, which is called the induct- 
ance of the circuit. This counter-generated e.m.f. is in oppo- 

di 
sition to the current, —L-r, and thus consumes an e.m.f., 
' dt' 

di . , 
+ L-Z, which is called the e.m.f, consumed by self -inductances 
at 

or inductance e.m.f. 

Therefore, by the inductance, L, of the field circuit, a voltage 

is consumed which is proportional to the rate of change of the 

field current, thus, 

^di 

'^ = ^di' 


POTENTIAL SERIES AND EXPONENTIAL FUNCTION. 73 

Since the supply voltage, and thus the total voltage consumed 
in the field circuit, is e = 500 volts, 

or, rearranged, 

di e—ri 
JC~L~' 

Substituting herein, 

u = e—ri] (63) 


hence, 

dii di 

gives. 


dt ^ dV 


du r ,^,, 

*=-L« (64) 

T 

This is the same differential equation as (39), with a=— y, 

Ij 

and therefore is integrated by the function, 
therefore, resubstituting from (63), 


and 


--rt 
e—ri = ao£ ^ , 


e , ao -L^ 


t=-i-s ^ (65) 

r r ^ ^ 


This solution (65), still contains the unknown quantity ao; 
or, the integration constant, and this is determined by know- 
ing the current i for some particular value of the time t. 

Before closing the field switch and thereby impressing the 
voltage on the field, the field current obviously is zero. In the 
moment of closing the field switch, the current thus is still 
zero; that is, 

i = 0 for ; = 0 (66) 


74 ENGINEERING MATHEMATICS. 

Substituting these values in (65) gives, 

hence, 


(67) 


is the final solution of the differential equation (62); that is, 
it is the value of the field current, i, as function of the time, i, 
after closing the field switch. 

After infinite time, ^ = oo , the current i assumes the final 
value io, which is given by substituting t = oo into equation 
(67), thus, V 

to = -=77^ = 2 amperes; .... (o8) 

hence, by substituting (68) into (67), this equation can also be 
written, 

= 2[i-b-~l')^ .... . (69) 

where io = 2 is the final value assumed by the field current. 
The time h, after which the field current i has reached 90 
per cent of its final value i^, is given by substituting i = 0.9fo 
into (69), thus, 

0.9to=io(l-^"~^''), 
and 

Taking the logarithm of both sides, 

r 
-^^ilog£=-l; 

and 

h=-^ (70) 

r log £ 


POTENTIAL SERIES AND EXPONENTIAL FUNCTION. 75 

55. The inductance L is calculated from the data given 
in the problem. Inductance is measured by the number of 
interlinkages of the electric circuit, with the magnetic flux 
produced by one absolute unit of current in the circuit; that 
is, it equals the product of magnetic flux and number of turns 
divided by the absolute current. 

A current of ^0=2 amperes represents 0.2 absolute units, 
since the absolute unit of current is 10 amperes. The number 
of field turns per pole is 4000; hence, the total number of turns 
n = 4x4000 = 16,000. The magnetic flux at full excitation, 
or i'o =0.2 absolute units of current, is given as (^=8x10® lines 
of magnetic force. The inductance of the field thus is: 

^ n0 16000X8X106 ^^^ ^^^ ^ , ^ .^ ^,^, 

L = -^ = jr^ = 640 X 109 absolute units = 640.^ , 

Iq 0.2 ' 

the practical unit of inductance, or the henry (h) being 10^ 
absolute units. 

Substituting L = 640 r = 250 and e = oOO, into equation (67) 
and (70) gives 

i = 2(l-£-«-9f), 
and 

640 
^^^250X0.4343^'^-^-'^^^ ^^^^ 

Therefore it takes about 6 sec. before the motor field has 
reached 90 per cent of its final value. 

The reader is advised to calculate and plot the numerical 
values of i from equation (71), for 
^ = 0, 0.1, 0.2, 0.4, 0.6, 0.8, 1.0, 1.5, 2.0, 3, 4, 5, 6, 8, 10 sec. 

This calculation is best made in the form of a table, thus; 


,-o.39< = jV_o.39nog., 

and, 

log £ =0.4343; 

hence. 

0.39 logs =0.1694i; 

and. 

.-0-39' = iV_o.l694<. 

76 


ENGINEERING MATHEMATICS, 


The values of £-o-39< ^^^ ^jgQ ^g taken directly from the 
tables of the exponential function, at the end of the book. 


t 

0.1694« 

-0.169^4 

,-0.39^ 

l_^-0.39i 

2(1- c- -390 

= -/V-U.1694< 

; 

0.0 
0.1 
0.2 
0.4 
0.6 
0.8 
etc. 

0 
0.0170 
0.0339 
0.0678 
0.1016 
0.1355 

0 
0.9830-1 
0.9661-1 
0.9322-1 
0.8984-1 
0.8645-1 

1 

0.962 
0.925 
0.855 
0.791 
0.732 

0 
0.038 
0.075 
0.145 
0.209 
0.268 

0 
0.076 
0.150 
0.290 
0.418 
0.536 

EXAMPLE 2. 

56. A condenser of 20 mf. capacity, is charged to a potential 
of 60 = 10,000 volts, and then discharges through a resistance 
of 2 megohms. What is the equation of the discharge current, 

and after how long a time has 
the voltage at the condenser 
dropped to 0.1 its initial value? 
A condenser acts as a reser- 
voir of electric energy, similar 
to a tank as water reservoir. 
If in a water tank, Fig. 27, A 
is the sectional area of the tank, 
e, the height of water, or water 
pressure, and water flows out 
of the tank, then the height e 
decreases by the flow of water; 
that is the tank empties, and 
the current of water, i, is proportional to the change of the 

de 
water level or height of water, — , and to the area A of the 


Fig. 27. Water Reservoir. 


tank; that is, it is. 


(U' 


de 
dt' 


(72) 


The minus sign stands on the right-hand side, as for positive 
i; that is, out-flow, the height of the water decreases; that is, 
de is negative. 


POTENTIAL SERIES AND EXPONENTIAL FUNCTION. 77 

In an electric reservoir, the electric pressure or voltage e 
corresponds to the water pressure or height of the water, and 
to the storage capacity or sectional area A of the water tank 
corresponds the electric storage capacity of the condenser, 
called capacity C. The current, or, flow out of an electric 
condenser, thus is, 

--4I (-3) 

The capacity of condenser is, 

C = 20 mf = 20x10-6 farads. 
The resistance of the discharge path is, 
r = 2X106 ohms; 
hence, the current taken by the resistance, r, is 


and thus 


. e 


^ dt r 


and 

dt ~ Cr ^' 

Therefore, from (60) (61), 

t_ 

and for ^ = 0, 6 = ^0 = 10,000 volts; hence 


and 

0.1 of the initial value: 
Ls reached at : 


10,000 = ao, (74) 

t_ 

e = €Q£ Cr 

= 10,000£-^^25< volts; 

6 = 0.1^0, 

=Rl = 92sec (75) 


78 ENGINEERING MATHEMATICS. 

The reader is advised to calculate and plot the numerical 
values of e, from equation (74), for 

/ = 0; 2; 4; 6; 8; 10; 15; 20; 30; 40; 60; 80; 100; 150; 200 sec. 

57. Wherever in an electric circuit, in addition to resistance, 
inductance and capacity both occur, the relations between 
currents and voltages lead to an equation containing the second 
differential coefficient, as discussed above. 

The simplest form of such equation is: 

ih'^y (7«) 

To integrate this by the method of indeterminate coefficients, 
we assume as solution of the equation (76) the infinite series, 

y=-^ao+aiX+a2X^+fi'iX^+a^x'^ + {77)- 

in which the coefficients ao, ai, a2, as, a^. . . are indeterminate. 
Differentiating -(67) twice, gives 

^==2a2 + 2X3a3X + 3X4a4a:2 + 4x5a5a-3 + ..., . (78) 

and substituting (77) and (78) into (76) gives the identity, 

2a2+2x3a3X+3x4a4x2+4x5a5x3 + . . . 

=a{ao-\-aiX-\-a2X^+a^x^-\-. . .); 

or, arranged in order of x, 

{2a2-aao) +x{2xSa^-aai) +x^{3Xia4-aa2) 

+ x3(4x5a5-aa3)+. . .=0 (79) 

Since this equation (79) is an identity, the coefficients of 
all powers of x must individually equal zero. This gives for 
the determination of these hitherto indeterminate coefficients 
the equations, 

2a2 — aao==0: 
2x3a3-aai=0: 
3x4a^-aa2 = 0; 
4Xoao — aa3 = 0, etc. 


POTENTIAL SERIES AND EXPONENTIAL FUNCTION. 79 
Therefore 


aao 

afi] 

03- 3 ; 

aa2 
^^"3X4 = 

aoa2 

aar, 
"^-4X5 = 

aia2 
5 

aa4 

"^^-5X6 = 

aoa^ 

6 ' 

"^"6X7 = 

7 

aae 

^«-7x8 = 

= 8 ' 

aa7 
^^-8X9 = 

9 

etc., 

etc. 

Substituting these values in (77), 
2/ = a„|l+-2-+^+^+.. 


o^x^ aH^ a'^x'' 


\ ax+ ,„ I ,. 
I |3 li 


(80) 


In tWs case, two coefficients ao and ai thus remain inde- 
terminate, as was to be expected, as a differential equation 
of second order must have two integration constants in its 
most general form of solution. 

Substituting into this equation, 

62 = a; 
that is, 

h = \/a, (81) 

S=+^2/, (82) 


and 
2/ = aoi 


62^ 6%4 66^ 

h^x^ ¥x^ 67^7 


+a]6 


''^+ir+^+-i7-+--- •• (83) 


80 ENGINEERING MATHEMATICS. 

In this case, instead of the integration constants ao and a\y 
the two new integration constants A and B can be introduced 
by the equations 

aQ = A-\-B and aih = A — B', 
hence, 

A = — ^ — and B= — ; 

and, substituting these into equation (83), gives, 
, r , &2^2 53^3 54^4 ^ 

^ f ^ ^ h^^ h^x^ ¥x^ 1 

+B^l-hx+-^- 13- +-|4- "+•••}• • ^^4) 

The first series, however, from (56), for n = h is e"^^^, and 
the second series from (56), for n=—b is £~^*. 
Therefore, the infinite series (83) is, 

2/ = A£+&^+5£-^*; (85) 

that is, it is the sum of two exponential functions, the one with 
a positive, the other with a negative exponent. 
Hence, the difTerential equation, 

S=a2/, ........ (76) 

is integrated by the function, 

2/-^£+^^+5s-^^ (86) 

where, 

b = Va. (87) 

However, if a is a negative quantity, h = Va is imaginary, 
and can be represented by 

b = jc, (88) 

where 

c^=-a (89) 

In this case, equation (86) assumes the form. 


POTENTIAL SERIES AND EXPONENTIAL FUNCTION. 81 

that is, if in the differential equation (76) a is a positive quantity, 
= +6^^ this differential equation is integrated by the sum of 
the two exponential functions (86) ; if, however, a is a negative 
quantity, = — c^, the solution (86) appears in the form of exponen- 
tial functions with imaginary exponents (90). 

58. In the latter case, a form of the solution of differential 
equation (76) can be derived which does not contain the 
imaginary appearance, by turning back to equation (80), and 
substituting therein a=—c^, which gives, 


= -r2 


c^y 


y-% 


{'- 


cH^ c^x^ c^x^ 

-^r- + -n 177- + , 


11 li 


aic 


ex 77r-+-T^ 1-. 


|3 |5 


(91) 


■h 


or, writing* A = 00 and B= — aic. 


y=A\l-^^ + 


c^x^ c'^x^ c^x^ 


li I 


+ 


+B\ ex 


+-r^ +, 


I li 


(92) 


The solution then is given by the sum of two infinite series, 
thus. 


, , , c^x^ c%4 c^x^ 


and 


as 


It |6 


v(cx)=cx— 


r^T^ 


c^x^ 


- +, 


(93) 


y = Au(cx)-\-Bv(cx) (94) 

In the i^-series, a change of the sign of x does not change 
the value olu. 


u{ — cx)=u{+cx). . 
Such a function is called an even function. 


(95) 


82 ENGINEERING MATHEMATICS. 

In the v-scries, a change of the sign of x reverses the sign 
of V, as seen from (93) : 

v{-cx) = -v{+cx) (96) 

Such a function is called an odd function. 
It can be shown that 

u{cx)=Qo^cx and v{cx)=^mcx; . . . (97) 
hence, 

2/ = -A cos ex +5 sin ex, ..... (98) 

where A and B are the integration constants, which are to be 
determined by the terminal conditions of the physical problem. 
Therefore, the solution of the differential equation 

d^^=^y^ • (9^) 

has two different forms, an exponential and a trigonometric. 
If 4t is positive, 

^^ dhi 

^^-+^y' (100) 

it is: 

y = As + ^'^+BB-^^, (101) 

If a negative, 


■'O" 


d-y 
it is: 


^=-cY. (102) 


2/ = A cos ex +5 sin ex (103) 

In the latter case, the solution (101) would appear as ex- 
ponential function with imaginary exponents; 

y^Ae+^'^+Be-^''^ (104) 

As (104) obviously must be the same function as (103), it 
follows that exponential functions with imaginary exponents 
must be expressible by trigonometric functions. 


POTENTIAL SERIES AND EXPONENTIAL FUNCTION. 83 


59. The exponential functions and the trigonometric func- 
tions, according to the preceding discussion, are expressed by 
the infinite series, 


x^ x^ r^ x^ 

j>2 -j«4 /p6 

COS X=l—-r+'r-r—-r^ + —. . . 
2 |4 |D 

/v»3 'Y'O -vT 

sin^ = x-i3+j^-j^ + -... 


(105) 


Therefore, substituting ju for x, 

■' 2 -^ |3 |4 •'5 6 ■' |/ 

/, u^ u^ u^ \ ./ u^ u^ u^ \ 


However, the first part of this series is cos u, the latter part 
sin u, by (105); that is, 


£^" = cos 16+/ sin \i. 
Substituting —u for +u gives, 

£ - 2" = cos u — j sin u. 
Combining (106) and (107) gives, 


(106) 


(107) 


^+jM_|_ g-iu 


COS u = 


and 


c+iu_ f—ju 


sm w = 


2/ 


rio8) 


Substituting in (106) to (108), jv for u, gives, 
£~'' = cos /iJ+ysin p, 1 


and. 


"^ "^ = cos p — y sin jv. 


. (109) 


84 ENGINEERING MATHEMATICS. 

Adding and subtracting gives respectively, 

cosp = , 

and 


sm ]v = 


(110) 


2j -J 

By these equations, (106) to (110), exponential functions 
with imaginary exponents can be transformed into trigono- 
metric functions with real angles, and exponential functions 
with real exponents into trignometric functions with imaginary 
angles, and inversely. 

Mathematically, the trigonometric functions thus do not 
constitute a separate class of functions, but may be considered 
as exponential functions with imaginary angles, and it can be 
said broadly that the solution of the above differential equa- 
tions is given by the exponential function, but that in this 
function the exponent may be real, or may be imaginary, and 
in the latter case, the expression is put into real form by intro- 
ducing the trigonometric functions. 

EXAMPLE 1. 

6o. A condenser (as an underground high-potential cable) 
of 20 mf. capacity, and of a voltage of eo = 10,000, discharges 
through an inductance of 50 mh. and of negligible resistance, 
What is the equation of the discharge current? 

The current consumed by a condenser of capacity C and 

potential difference e is proportional to the rate of change 

of the potential difference, and to the capacity; hence, it is 

de 
C—^, and the current from the condenser; or, its discharge 

CLl 

current, is 

--^l-- • (1") 

The voltage consumed by an inductance L is proportional 
to the rate of change of the current in the inductance, and to the 
inductance; hence, 

^-4 • • • (112) 


POTENTIAL SERIES AND EXPONENTIAL FUNCTION. 85 

■* 
Differentiating (112) gives, 

de dH 

and substituting this into (111) gives, 

dH dH 1 . 

'^-^^^ ^'' W^^'cV^ ' ' ' (1^^) 

as the differential equation of the problem. 

This equation (113) is the same as (102), for c^^ttTj thus 
is solved by the expression, 

and the potential difference at the condenser or at the inductance 
is, by substituting (114) into (112), 

These equations (114) and (115) still contain two unknown 
constants, A and B, which have to be determined by the terminal 
conditions, that is, by the known conditions of current and 
voltage at some particular time. 

At the moment of starting the discharge; or, at the time 
^ = 0, the current is zero, and the voltage is that to which the 
condenser is charged, that is, -^ = 0, and e = eo. 

Substituting these values in equations (114) and (115) 
gives, 

fL 


0 = A and eQ=^\-7^B] 


hence 

B = e^ 


\L 


and, substituting for A and B the values in (114) and (115), 
gives 

\C . t 


and 

t 
P=en COS — =^ 
^ ° VCL 


(116) 


86 ENGINEERING MATHEMATICS. 

Substituting the numerical values, ^0 = 10,000 volts, (7 = 20 
mf.= 20X10- 6 farads, L = 50 mh.=0.05h. gives, 


J 


^ = 0.02 and VC'L^IO-^; 


hence, 

i = 200 sin 1000 t and 6 = 10,000 cos 1000 t. 

6 1. The discharge thus is alternating. ' In reality, due to 
the unavoidable resistance in the discharge path, the alterna- 
tions gradually die out, that is, the discharge is oscillating. 

The time of one complete period is given by, 

1000^0=2;:; or, to=^. 
Hence the frenquency, 

/= — = —^ — = 159 cycles per second. 

As the circuit in addition to the inductance necessarily 
contains resistance r, besides the voltage consumed by the 
inductance by equation (112), voltage is consumed by the 
resistance, thus 

er = ri, . (117) 

and the total voltage consumed by resistance r and inductance 
L, thus is 

e = n + Lj^ (118) 

Differentiating (118) gives, 

dc di dH 
jr'dt'^^'Tt^^ 


-=r-+L—^ , ni9) 


and, substituting this into equation (111), gives, 

dt^^^dt 


+ Cr^.+CL~=0, (120) 


as the differential equation of the problem. 

This differential equation is of the more general form, ("2^ 
62. The more general differential equation {22% ^^ 

g+2^+«, + 6 = 0, (121) 


POTENTIAL SERIES AND EXPONENTIAL FUNCTION. 87 
can, by substituting, 

y+l-^, . ■ (122) 

which gives 

dy dz 
dx dx 

be transformed into the somewhat simpler form, 

S-^4>«-^ (123) 

It may also be solved by the method of indeterminate 
coefficients, by substituting for z an infinite series of powers of 
Xj and determining thereby the coefficients of the series. 

As, however, the simpler forms of this equation were solved 
by exponential functions, the applicability of the exponential 
functions to this equation (123) may be directly tried, by the 
method of indeterminate coefficients. That is, assume as solu- 
tion an exponential function, 

z = Ae-^', (124) 


where A and h are unls:nown constants. Substituting (124) 
into (123), if such values of A and h can be found, which make 
the substitution product an identity, (124) is a solution of 
the differential equation (123). 
From (124) it follows that, 

dz d^'^ 

y-=-bAE-^^] and ^ = hUe-^^, . . (125) 

dx ' d^x ' 

and substituting (124) and (125) into (123), gives, 

AB-^^{b^ + 2ch+a}=0 (126) 

As seen, this equation is satisfied for every value of x, that 
is, it is an identity, if the parenthesis is zero, thus, 

b^+2cb+a = 0, (127) 

and the value of b, calculated by the quadratic equation (127), 
thus makes (124) a solution of (123), and leaves A still undeter- 
mined, as integration constant. 


88 ENGINEERING MATHEMATICS. 

From (127), 

h=-c±Vc^-a; (128) 

or, substituting, 

Vc^-a = p, (129) 

into (128), the equation becomes, 

b^-c±p (130) 

Hence, two values of h exist, 

hi=—c-\-p and 62=— c— p, . . . (131) 
and, therefore, the differential equation, 

g+2c|+««=0, (132) 

is solved by Ae^^^; or, by Ae^^*, or, by any combination of 
these two solutions. The most general solution is, 

that is, 

^ . . . (131) 

h '■ 


= £-^^{^l£+P^+^2£~^'=! . 


As roots of a quadratic equation, 61 and 62 may both be 
real quantities, or may be complex imaginary, and in the 
latter case, the solution (131) appears in imaginary form, and 
has to be reduced or modified for use, so as to eliminate the 
imaginary appearance, by the relations (106) and (107). 

EXAMPLE. A 

63. Assume, in the example in paragraph 9, the discharge 
circuit of the condenser of (7 = 20 mf. capacity, to contain, 
besides the inductance, L = 0.05 h, the resistance, r = 125 ohms. 

The general equation of the problem, (120), dividing by 
C L, becomes, 

dH r di i ^ ,,^^^ 


POTENTIAL SERIES' AND EXPONENTIAL FUNCTION, 89 
This is the equation (123), for: 


x = t, 2c = 7=2500: 


z = i, a 


iCL) 


= 106 


. . (133) 


If 


p = Vc^ — a, then 


and, writing 


P = 7: 


and since 


2L' 


2^ = 10 and ^ = 2500, 
s = 75 and p = 750. 


The equation of the current from (131) then is. 


i=.Aie 2l' +^^,. 2L 


(134) 


(135) 


(136) 


(137) 


This equation still contains two unknown quantities, the inte- 
gration constants Ai and A2, which are determined by the 
terminal condition : The values of current and of voltage at the 
beginning of the discharge, or ^ = 0. 

This requires the determination of the equation of the 
voltage at the condenser terminals . This obviously is the voltage 
consumed by resistance and inductance, and is expressed by 
equation (118), 

e = ri + Lj^; . (118) 


90 ENGINEERING MATHEMATICS. 

di 
hence, substituting herein the value of i and -jt, from equation 

(137), gives 

(r-8 _L±f/l f r—s ^~^t r-\-s ^-^-y) 


= c 2L . 


LtlA,,^^U'^A.,s-^'\, (138) 


and, substituting the numerical values (133) and (136) into 
equations (137) and (138), gives 


(139) 


and, 

e = 100Ai£-^oof+25A2£-2ooo' J 

At the moment of the beginning of the discharge, ^ = 0, 
the current is zero and the voltage is 10,000; that is, 

t = 0; i = 0; c= 10,000 ..... .(140) 

Substituting (140) into (139) gives, 

0=^1+^2, 10,000 = 100^1+25^2; 
hence, 

A2=-Ai] Ai=: 133.3; .42= -133.3. 

Therefore, the current and voltage are, 

t= 133.3 js-^^^^-s-^'^^^M, 


e=13,333c-soof-3333£-2ooo^ 


(142) 


The reader is advised to calculate and plot the numerical 
values of i and e, and of their two components, for, 

^ = 0, 0.2, 0.4, 0.6, 1, 1.2, 1.5, 2, 2.5, 3, 4, 5, 6x10-^ sec. 


POTENTIAL SERIES AND EXPONENTIAL FUNCTION. 91 

64. Assuming, however, that the resistance of the discharge 
circuit is only r = 80 ohms (instead of 125 ohms, as assumed 
above : 

r^—-p in equation (134) then becomes —3600, and there- 
fore : 

s = \/-3600 = 60V-1 = 60/, 
and 

P=^=6ooy. 

The equation of the current (137) thus appears in imaginary 

form, 

i = £-8ooq^^£ + 6oo;< + ^2£-6ooyn^ . . . (143) 

The same is also true of the equation of voltage. 

As it is obvious, however, physically, that a real current 
must be coexistent with a real e.m.f., it follows that this 
imaginary form of the expression of current and voltage is only 
apparent, and that in reality, by substituting for the exponential 
functions with imaginary exponents their trigononetric expres- 
sions, the imaginary terms must ehminate, and the equation 
(ii6)- appear in real form. 
''^According to equations (106) and (107), 

e+6ooyf_cos 600f +/ sin 600^; 1 


(144) 


£-600?^ = cos 600^-/ sin 600^. J 

Substituting (144) into (143) gives, 

1 = £-800^1 Bi cos 600^+^2 sin 600^!, . . (145) 

where Bi and B2 are combinations of the previous integration 
constants Ai and A2 thus, 

Bi = Ai+A2, and B2=j(Ai-A2). . . (146) 

By substituting the numerical values, the condenser e.m.f., 
given by equation (138), then becomes, 

e = £-800^1 (40 +30j)Ai(cos 600^ +/ sin 6000 

+ (40-30y)A2(cos 600i-/sin 6000 ! 
= £ - 800/ 1 (40Bi + 30B2)cos 600^ + (40^2 - 30Bi) sin 600^ \ . (147) 


92 ENGINEERING MATHEMATICS. 

Since for i=0, i = 0 and e = 10,000 volts (140), substituting 
into (145) and (147), 

0 = Bi and 10,000 = 40 Bi+SO B2. 

Therefore, Bi = 0 and 52 = 333 and, by (145) and (147), 

?: = 333£-8oo^sin600i; 1 

• . (148) 
e = 10,000£-8oo^ (cos 600 ^ + 1.33 sin 600 t. J 

As seen, in this case the current i is larger, and current 
and e.m.f. are the product of an exponential term (gradually 
decreasing value) and a trigonometric term (alternating value) ; 
that is, they consist of successive alternations of gradually 
decreasing amplitude. Such functions are called oscillating 
functions. Practically all disturbances in electric circuits 
consist of such oscillating currents and voltages. 


600^ = 2;: gives, as the time of one complete period, 
and the frequency is 


^ = ^ = 0.0105 sec; 
600 ' 


/=-^ = 95.3 cycles per sec. 

In this particular case, as the resistance is relatively high, 
the oscillations die out rather rapidly. 

The reader is advised to calculate and plot the numerical 

values of i and e, and of their exponential terms, for every 30 

T T T 
degrees, that is, for ^ = 0, -rx, 2 j^, 3 t^, etc., for the first two 

periods, and also to derive the equations, and calculate and plot 
the numerical values, for the same capacity, C = 20 mf., and 
same inductance, L = 0.05/i, but for the much lower resistance, 
r = 20 ohms. 

65. Tables of e"*"^ and £~^, for 5 decimals, and tables of 
log e"^^ and log £~^, for 6 decimals, are given at the end of 
the book, and also a table of e~^ for 3 decimals. For most 
engineering purposes the latter is sufficient; where a higher 
accuracy is required, the 5 decimal table may be used, and for 


POTENTIAL SERIES AND EXPONENTIAL FUNCTION. 93 

highest accuracy interpolation by the logarithmic table may be 
employed. For instance, ♦ 

g — 13.6847^9 

From the logarithmic table, 

log £-10 =5.657055, 
log £-3 =8.697117, 
log £-0-6 =9.739423, * 
log £-0.08 = 9 965256, 


log £-0.0047 = 9.998133 
added 


interpolated, 

between log £-0004 = 9993263, 
. and log £-0 005 = 9.997829), 


log £-13-6847 = 4.056984 = 0.056984 - 6. 
From common logarithmic tables, 

^-13.6847 = 1.14021x10-6.
