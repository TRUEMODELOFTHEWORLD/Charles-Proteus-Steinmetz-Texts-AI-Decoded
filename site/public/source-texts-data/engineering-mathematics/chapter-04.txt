CHAPTER V. 
METHODS OF APPROXIMATION. 

124. The investigation even of apparently simple engineer- 
ing problems frequently leads to expressions which are so 
complicated as to make the numerical calculations of a series 
of values very cumbersonme and almost impossible in practical 
work. Fortunately in many such cases of engineering prob- 
lems, and especially in the field of electrical engineering, the 
different quantities which enter into the problem are of very 
different magnitude. Many apparently compHcated expres- 
sions can frequently be greatly simplified, to such an extent as 
to permit a quick calculation of numerical values, by neglect- 
ing terms which are so small that their omission has no appre- 
ciable effect on the accuracy of the result; that is, leaves the 
result correct within the limits of accuracy required in engineer- 
ing, which usually, depending on the nature of the problem, 
is not greater than from 0.1 per cent to 1 per cent^;^ 

Thus, for instance, the voltage consumed by the resistance 
of an alternating-current transformer is at full load current 
only a small fraction of the supply voltage, and the exciting 
current of the transformer is only a small fraction of the full 
load current, and, therefore, the voltage consumed by the 
exciting current in the resistance of the transformer is only 
a small fraction of a small fraction of the supply voltage, hence, 
it is negligible in most cases, and the transformer equations are 
greatly simplified by omitting it. The power loss in a large 
generator or motor is a small fraction of the input or output, 
the drop of speed at load in an induction motor or direct- 
current shunt motor is a small fraction of the speed, etc., and 
the square of this fraction can in most cases be neglected, and 
the expression simplified thereby. 

Frequently, therefore, in engineering expressions con- 
taining small quantities, the products, squares and higher 

187 


188 ENGINEERING MATHEMATICS. 

powers of such quantities may be dropped and the expression 
thereby simplified; or, if the quantities are not quite as small 
as to permit the neglect of their squares, or where a high 
accuracy is required, the first and second powers may be retained 
and only the cubes and higher powers dropped. 

The most common method of procedure is, to resolve the 
expression into an infinite series of successive powers of the 
small quantity, and then retain of this series only the first 
term, or only the first two or three terms, etc., depending on the 
smallness of the quantity and the required accuracy^ 

125. The forms most frequently used in the reduction of 
expressions containing small quantities are multipHcation and 
division, the binomial series, the exponential and the logarithmic 
series, the sine and the cosine series, etc. 

Denoting a small quantity by s, and where several occur, 
by Si, S2, S3 . . . the following expression may be written: 
/ 

(,0±Sl)(l±S2)=l±S]±S2±SlS2, ; 

and, since S1S2 is small compared with the small quantities 
Si and S2, or, as usually expressed, S1S2 is a small quantity of 

r* fjj higher order (in this case of second order), it may be neglectod, 

'-^ f and the expression written: 

X (l±Si)(l±S2)=l±Si±S2 (1) 

This is one of the most useful simplifications : the multiplica- 
tion of terms containing small quantities is replaced by the 
simple addition of the small quantities. 

If the small quantities Si and S2 are not added (or subtracted) 
to 1, but to other finite, that is, not small quantities a and h, 
a and h can be taken out as factors, thus, 


X (a±si)(6±S2)=a6/l±^Vl±|Va/l±^-±|Y . 


(2) 


where — and -j- must be small quantities. 

As seen, in this case, s\ and S2 need not necessarily be abso- 
lutely small quantities, but may be quite large, provided that 
a and h are still larger in magnitude; that is, Si must be small 
compared with a, and S2 small compared with h. For instance. 


METHODS OF APPROXIMATION. 189 

in astronomical calculations the mass of the earth (which 
absolutely can certainly not be considered a small quantity) 
is neglected as small quantity compared with the mass of the 
sun. Also in the effect of a lightning stroke on a primary 
distribution circuit, the normal line voltage of 2200 may be 
neglected as small compared with the voltage impressed by 
lightning, etc. 

126. Example. In a direct-current shunt motor, the im- 
pressed voltage is eo = 125 volts; the armature resistance is 
ro = 0.02 ohm; the field resistance is ri = 50 ohms; the power 
consumed by friction is pf=^300 watts, and the power consumed 
by iron loss is pi= iOO watts. What is the power output of 
the motor at ^o = 50, 100 and 150 amperes input? 

The power produced at the armature conductors is the 
product of the voltage e generated in the armature conductors, 
and the current i through the armature, and the power output 
at the motor pulley is, 

p = ei-pf-pi. ....... (3) 

The current in the motor field is — , and the armature current 

n 

therefore is, 

^ = ^0--, (4) 

where — is a small quantity, compared with 2*0. 

The voltage consumed by the armature resistance is roi, 
and the voltage generated in the motor armature thus is: 

e = eo — roi, (5) 

where roi is a small quantity compared with eo. 
Substituting herein for i the value (4) gives. 


eo- 


ro{io-'f) (6) 


Since the second term of (6) is small compared with eo, 

and in this second term, the second term — is small com- 

ri 

pared with io, it can be neglected as a small term of highc^r 


190 ENGINEERING MATHEMATICS. 

order; that is, as small compared with a small term, and 
expression (6) simplified to 

e = eo-roio (7) 

Substituting (4) and (7) into (3) gives, 

p = (eo - ^o^o) [io - yj - Vf- Pi 

--(•-?)('-5)-'"-'" w 

Expression (8) contains a product, of two terms with small 
quantities, which can be multipHed by equation (1), and thereby 
gives. 


p = eo^o[l—---JJ-pf-pi 


= eoio-roto^-- — Pf-pi (9) 

Substituting the numerical values gives, 

p = 125^o-0.02^o2-562.5-300-400 
= 125^0 - Omio^ - 1260 approximately ; 

thus, for 10=50, 100, and 150 amperes; p = 4940, 11,040, and 
17,040 watts respectively. 

127. Expressions containing a small quantity in the denom- 
inator are frequently simplified by bringing the small quantity 
in the numerator, by division as discussed in Chapter II para- 
graph 39, that is, by the series, 

:; = 1^X+X^TX^-^X^^X^+ . . .; . . . (10) 

l±X 

which series, if a; is a small quantity s, can be approximated 
by: 

1 


1 — « 


(11) 


METHODS OF APPROXIMATION. 


191 


or, where a greater accuracy is required, 

1 


1+s 


1-s+s^ 


^^ — - = 1+S+S2, 

1 — s 


(12) 


By the same expressions (11) and (12) a small quantity 
contained in the numerator may be brought into the denominator 
where this is more convenient, thus : 


i+.s=j--; 


l — s = rr--r-', etc. 

l+s' 


(13) 


More generally then, an expression like -— , where s is 

small compared with a, may be simplified by approximation to 
the form, 


h b _b/ s\ 


(14) 


QTj^wli^ a greater exactness is required, by taking in the second 
term, 

■^V T±s--ai}^-a^-^ '15) 

128. Example. AVhat is the current input to an induction 
motor, at impressed voltage eo and slip s (given as fraction of 
synchronous speed) if ro — jxo is the impedance of the primary 
circuit of the motor, and ri — jxi the impedance of the secondary 
circuit of the motor at full frequency, and the exciting current 
of the motor is neglected; assuming s to be a small quantity; 
that is, the motor running at full speed? 

Let E be the e.m.f. generated by the mutual magnetic flux, 
that is, the magnetic flux which interlinks with primary and 
with secondary circuit, in the primary circuit. Since the fre- 
quency of the secondary circuit is the fraction 8 of the frequency 


192 ENGINEERING MATHEMATICS. 

of the primary circuit, the generated e.m.f. of the secondary 
circuit is sE. 

Since x\ is the reactance of the secondary circuit at full 
frequency, at the fraction s of full frequency the reactance 
of the secondary circuit is sxi, and the impedance of the sec- 
ondary circuit at slip s, therefore, is ri — jsx\] hence the 
secondary current is, 

• ri-]sxi 

If the exciting current is neglected, the primary current 
equals the secondary current (assuming the secondary of the 
same number of turns as the primary, or reduced to the same 
number of turns) ; hence, the current input into the motor is 

sE 

(16) 


ri-]sxi 


The second term in the denominator is small compared 
with the first term, and the expression (16) thus can be 
approximated bv 


'■'"h^) 


The voltage E generated in the primary circuit equals the 
impressed voltage eo, minus the voltage consumed by the 
current / in the primary impedance; to—jxq thus is 

E = eo-I{ro-jXo) (IS) 

Substituting (17) into (18) gives 

E = eo-'Aro-jxo)(lH'^) (19) 

In expression (19), the second term on the right-hand side, 
which is the impedance drop in the primary circuit, is small 


compared with the first term eo, and in the factor 


(■<■) 


of this small term, the small term j^— can thus be neglected 


METHODS OF APPROXIMATION. 


193 


as a small term of higher order, and equation (19) abbreviated 
to 


E = eo---{ro-]Xo). 
^1 


(20) 


From (20) it follows that 


E = 


and from (13), 


l+-{ro-jxo) 
^1 


E = eo \ l-—(ro-jxo) 


(21) 


Substituting (21) into (17) gives 


/ 


seo 


and from (1), 


(•OI'-^<-«>l 


seo\ ^ ro . Xo + .Ti 

= — \ 1 — S— + 1S 

ri ri ' ri j 


(22) 


If then, /oo^^'o+ytV is the exciting current, the total 
current input into the motor is, approximately, 

/o=(+|oo 

=7f|l+«^+J«^77-^)+to+no'. ■ ■ . (23) 

129. One of the most important expressions used for the J^ ^^^^ 
r(Hkiction of small terms is the binomial series: 

1 


(l±.x)« = l±nx + 


n{n—l') ^ n(n—\){n—2) 


-x^± 


13 


n{n-lMn-2)(n-S) , 
+ -^- ^±. 


(24) 


If X is a small term s, this gives the approximation, 

l±s)" = l±ns; (25) 


194 ENGINEERING MATHEMATICS. 

or, using the second term also, it gives 

y^ (l±s)« = l±ns+^^^^^^s2 (26) 

In a more general form, this expression gives 

^(a±s)- = a"(l±^)" = a-(l±^'j; etc. . . (27) 

By the binomial, higher powers of terms containing small 
quantities, and, assuming n as a fraction, roots containing 
small quantities, can be eliminated; for instance. 


\/a±.s = (a±s)«=a«f l±-j '' = v^fl±— j; 
1 


11 1 / s\-^_l^/ ns\ 


1 
1 


(a±s) «=a «(1± 


m 
nn ^ . X- -/ s\« n/ — / ^A 

V(a±s)^ = (a±s)«=a«l 1 ±- I =va»»M±— I; etc. 

One of the most common uses of the binomial series is for 
the elimination of squares and square roots, and very fre- 
quently it can be conveniently applied in mere numerical calcu- 
lations; as, for instance, 

(201)2 = 2002(1 +-J-J = 40,000(1 +j-y =40,400; 
29.92 = 302(l-3i3)^900(l-j^^)=000-6 = 894; 


vmS = 10\/l-0.02 = 10(1 -0.02)2 =10(1-0.01) = 9.99; 
1 1 1 


XOS (1+0.03)1/2 1.015 


= 0.985; etc. 


METHODS OF APPROXIMATION. 195 

130. Example i. If r is the resistance, x the reactance of an 
alternating-current circuit with impressed voltage e, the 
current is 


1 = 


r2+x2 


If the reactance x is small compared with the resistance r, 
as is the case in an incandescent lamp circuit, then, 


._ _ _ _ef /xV] ~2 


m 


i^' 


e 
r 

If the resistance is small compared with the reactance, as 
is the case in a reactive coil, then, 

e e £' r /r \- 1 2 

Vf^+x^ TrV ^ 


-,V^)-"-'© 


<^-w, 


(28) 


Example 2. How does the short-circuit current of an 
alternator vary with the speed, at constant field excitation? 

When an alternator is short circuited, the total voltage 
generated in its armature is consumed by the resistance and the 
synchronous reactance of the armature. 

The voltage generated in the armature at constant field 
excitation is proportional to its speed. Therefore, if eo is the 
voltage generated in the armature at some given speed So, 
for instance, the rated speed of the machine, the voltage 
generated at any other speed S is 


196 ENGINEERING MATHEMATICS. 

S 
or, if for convenience, the fraction -^ is denoted by a, then 

a = -^ and e = aeo, 

oo 

where a is the ratio of the actual speed, to that speed at which 
the generated voltage is eo- 

If r is the resistance of the alternator armature, xq the 
synchronous reactance at speed So, the synchronous reactance 
at speed Sh x = axo, and the current at short circuit then is 

i=^^=^ , "■"> (29) 

Usually r and xo are of such magnitude that r consumes 
at full load about 1 per cent or less of the generated voltage, 
while the reactance voltage of xq is of the magnitude of from 
20 to 50 per cent. Thus r is small compared with xq, and if 
a is not very small, equation (29) can be approximated by 


aeo eo 

1 = 


\ \axoJ 


\ 2 xo\ 2 \axoj 
axo^ /I 4-1 — 1 


'-.Ki)T ■ ■ ™ 


^ 


)/ 

Then if a:o = 20r, the following relations exist: 
a= 0.2 0.5 1.0 2.0 

i = -X0.9688 0.995 0.99875 0.99969 

That is, the short-circuit current of an alternator is practi- 
cally constant independent of the speed, and begins to decrease 
only at very low speeds. 

131. Exponential functions, logarithms, and trigonometric 
functions are the ones frequently met in electrical engineering. 

The exponential function is defined by the series, 

^ ^ x^ 7^ x^ xP 

^> ^^ '— '— '— I— 


METHODS OF APPROXIMATION. 197 

and, if x is a small quantity, s, the exponential function, may 
be approximated by the equation, 

€±^ = l±s; (32) 

or, by the more general equation, 

and, if a greater accuracy i.s required, the second term may 
be included, thus. 


?2 


£±«=i±s+^,, {m 


and then 


^±as^lj^as+'^'-. ...... (35) 

— ; hence, /^o^^*'*^^'^* 

)<^log.(l±x)=±Jl-^-. 

Resolving -r-TT ^^^^ ^ series, by (10), and then integrating, 
gives 

log£ (l±x)=/± I (lTx+a:2q=r'^ + . . .)dx\ 

( y? x^ x^ x^\ ,_ ■ 

[y^[jj{. This logarithmic series (36) leads to the apj^mximaiion, 

log£(l±5)=±s; (37) 

or, including the second term, it gives 

)( loge(l±s)=±s-A^ (38) 

and the more generaLexpression is, respectively, 

S^log. (a±s) = log a\\ ±^- j =log a+log \\ ±^) =log a±^,-i^(39) 


198 ENGINEERING MATHEMATICS 

and, more accurately, 


s s^ 


loge (a±s) = loga±---2 


a a^ 


(40) 


Since logio iV = logio eXloge N = OASiS loge A/", equations (39) 
and (40) may be written thus, 

logio(l±s)=±0.4343s; 

■logio(a±s)=logio a ±0.4343- \' ' ' ' (^1) 

132. The trigonometric functions are represented by the 
infinite series : 


^ x^ x^ ofi 
cosx=l-|2+|4-J6+..-; 

X^ X^ x^ 


(42) 


which w^hen s is a small quantity, may be approxima^eiby 

1 cos s = \ and sin ,s = s; . . . 
or, they may be represented in closer approximation b^ 


- cos s = l — — ; 
sm s==s(^— g-j; 
or, by the more general expressions, 


A ( 1 «'^') 

cos as = 1 and \cosa.s = l — ^y 

JL Sin as = as and \ sm as =-as[ — -^ j . 


(43) 
(44) 

u 

(45) 


133. Other functions containing small terms may frequently 
be approximated by Taylor's series, or its special case, 
MacLaurin's series. 

MacLaurin's series is written thus : 


/(.t) =/(0) +xf'm +pf"(0) +p"'(o) +, 


(46) 


METHODS OF APPROXIMATION. 199 

where /', /", /'", etc., are respectively the first, second, third, 
etc., differential quotient of/; hence, 

/(a)^/(0)+s/'(0); j 

/(as)=/(0)+as/'(0). J 

Taylor's series is written thus, 


(47^ 


(49) 


fib+x) =f{b) +xf'{b) +^/"(b) +T^f"'(b) +..., . (48) 

and leads to the approximations : 

f{h±s)=f{b)±sf{b); 

f(b±as)=f(b)±a.sr(b). J 

Many of the previously discussed approximations can be 
considered as special cases of (47) and (49). 

134. As seen in the preceding, convenient equations for the 
approximation of expressions containing small terms are 
derived from various infinite series, which are summarized 
below : 
1 


l±x 


l=Fx+x2=Fx3+x*qF. . . 


X . n(n-l) ^ n(n-l)(n-2) , 
(l±.x)" = l±nx + — j^ — -x^±- r^ -x^ + . 

/V.2 nf3 /Tr«4 

/y»2 QcS 'Y'4 

loge {l±x)=±x--±-^-j±. . . ; 

/y^ y»4 /Y»t) 

cosx = l-i2+jj-j^+...; 

x^ x^ x"^ 
,,nx = x-^+^-i^ + ...; 

.Ax) =/(0) +x/'(0) +£r(0) +i^/"'(0) + . . . ; 

fib ±x) =f{b) ±xf'(b) +|/"(6) ±|/"'(« + . . . 


(SO) 


200 


ENGINEERING MATHEMATICS. 


The first approximations, derived by neglecting all higher 
terms but the first power of the small quantity a; = s in these 
series, are: 


il±s>=---l±ns; 

e±^ = l±S', 

log5(l±s)= ±s: 

■ .S2" _ 

~2r 

cos s = 1 ; 

- .S2" ^ 
2J' 

sin s = s; 

/(s)=/(0)+s/'(0); 

+fr(0)]; 

f{h±s)==fib)±sf'ih); 

+Jr(^^)]; 

(51) 


and, in addition hereto is to be remembered the multiplication 
rule, 

(l±si)(l±82) = l±.si±S2; [±8182]. . . (52) 

135. The accuracy of the approximation can be. estimated 
by calculating the next term beyond that which is used. 
This term is given in brackets in the above equations (50) 
and (51). 

Thus, when calculating a series of numerical values by 
approximation, for the one value, for which, as seen by the 
nature of the problem, the approximation is least close, the 
next term is calculated, and if this is less than the permissible 
limits of accuracy, the approximation is satisfactory. 

For instance, in Example 2 of paragraph 130, the approxi- 
mate value of the short-circuit current was found in (30), as 


% = ■ 


eo 

Xo 


2\axo) 1 


1-^1- 


METHODS OF APPROXIMATION. 201 

The next term in the parenthesis of equation (30), by the 
binomial, would have been H ^^ — s^; substituting n=— J: 

s = ( — ) , the next becomes +'5-1 — ) . The smaller the a, the Ma^ 
\axo/ ' 8 \axo/ ' *^^^ 

less exact is the approximation. ^ 

The smallest value of a, considered in paragraph 130, was 

a = 0.2. For Xo = 20r, this gives +o( — =0.00146, as the 
value of the first neglected term, and in the accuracy of the 
result this is of the magnitude of - X 0.00146, out of - X 0.9688, 
the value given in paragraph 130; that is, the approximation 
gives the result correctly within n Qfion =0.0015 or within one- 
sixth of one per cent, which is sufficiently close for all engineer- 
ing purposes, and with larger a the values are still closer 
approximations. 

136. It is interesting to note the different expressions, 
which are approximated by (1+s) and by (1 — s). Some of 
them are given in the following : 


1+. 
1 


1-s' 


-r^.v-v^- 


202 ENGINEERING MATHEMATICS. 


^ 


{n—m)s' 
etc. 


2-s-'; 

l+log. (1+s); 
l-log.(l-s); 


1 + 
1-n 


1 + 


nlog=(l+^); 

etc. 
1 +sin s] 


l+nsm — : 


VI +2s; VT-2s; 

1 1 


Vl-2s' \/r+2i' 


1 1 


•v^l — ns' v^l+ns' 


4-ms / 1 — ws 


\ 

l + (n-m)s' 

etc. 

£" 

-3- 

2- 

-C; 

l+loge(l-s); 

-hged+s); 

l+nlog.(l-0; 

-nhg,(l+~); 

1+log.^;^; 

-iog.^i_,: 

etc. 

-sins; 

-71 sin ^; 

METHODS OF APPROXIMATION. 203 

, 1 . , 1 . 

IH — sin ns: 1 — sin ns; 

cos \/ — 2s; cos v^; 

etc. etc. 

137. As an example may be considered the redaction to its 
simplest form, of the expression : 

2si /9T" 

Va-</(a + si^3i4_sin6s2i ^e<^ cos^ J— 


then, 


-3«(a+2si) I -a loge^^-p|i| Va-2si 
4— sin6s2 = 4(l — jsin6s2) ==4(l — ^s^ 


a' 


■c< 


1-^ 


l-'^^'^S^ V^"|=^-" '°^y 7^ =-^~'* 'o&^l-2f 

^ a 

= l-alog£(^l-^j=l+S2; 
V S^:2Fi = ai/2 (^1 - ^y ^' = ai/2 (1 - ^) ; 


204 ENGINEERING MATHEMATICS. 

hence, 


F = 


^i/2xa3/4(l+|il)x4(l-|82)xaV4x(l+2^)(l-2j) 


(1 


_ \4a2 a a J 

a3/2(l-3s2+2-- + S2--) 
\ a a / 

\ 4 a. a J 

138. As further example may be considered the equations 
of an alternating-current electric circuit, containing distributed 
resistance, inductance, capacity, and shunted conductance, for 
instance, a long-distance transmission line or an underground 
high-potential cable. 

Equations of the Transmission Line. 

Let I be the distance along the line, from some starting 
point; E^ the voltage; 7, the current at point I, expressed as 
vector quantities or general numbers; Zo^ro—jxo, the line 
impedance per unit length (for instance, per mile); Yo=^go—jhQ 
= Hne admittance, shunted, per unit length; then, rn is the 
ohmic effective resistance; .To, the self-inductive reactance; 
&o, the condensive susceptance, that is, wattless charging 
current divided by volts, and go = energy component of admit- 
tance, that is, energy component of charging current, divided 
by volts, per unit length, as, per mile. 

Considering a line element dl, the voltage, dE, consumed 
by the impedance is ZQidl, and the current, dl, consumed by 
the admittance is Y^Edl; hence, the following relations may be 
WTitten : 

f =^0/; (1) 


METHODS OF APPROXIMATION. 205 

Differentiating (1), and substituting (2) therein gives 

— ZoYoE, (3) 

and from (1) it follows that, 

r '^ dE .. 

''-ZoW ''^ 

Equation (3) is integrated by 

E = AeBi, (5) 

and (5) subtstituted in (3) gives 


B=±VZoYo; (6) 

hence, from (5) and (4), it follows 

^_^j^+\/z^oi4-^42£-v/za^or, (7) 


/ = .^{4l£ + VZoFoi_,l,,_Vz.F„Zl. 


(8) 


Next assume 

I^Iq, the entire length of line; 

Z=Zo^o, the total line impedance; , . . . (9) 

and F=ZoFo, the total line admittance; 

then, substituting (9) into (7) and (8), the following expressions 
are obtained : 

Ei = Ais+^^ + A2i-^^^', 


/i =^^}Ai£+v^- A.s-^^^] 


(10) 


as the voltage and current at the generator end of the line. 

139. If now ^0 and (0 respectively are the current and 
voltage at the step-down end of the line, for 1=0, by sub- 
stituting Z=0 into (7) and (8), 

Ai+A2=Eo; 

II \ (11) 


Ai — A2 = h 


206 


ENGINEERING MATHEMATICS. 


Substituting in (10) for the exponential function, the series^ 

24" 


__ ZY ZYVZY Z^Y^ Z^YWZY 


120 


and arranging by (41+^2) and (Ai— A2), and substituting 
here for the expressions (11), gives 


Ei = Eq 


\ ZY Z^Y^] ^, r ZY Z^Y^] 
/+^+^r)+^^M'^^"'"l20-}' 


,,^ r ZY Z^Y^ 

+ YEo\l+-^+-j^ 


H 


(13) 


When l=—lo, that is, for Eq and /o at the generator side, and 
El and /i at the step-down side of the hne, the sign of the 
second term of equation (13) merely reverses. 

140. From the foregoing, it follows that, if Z is the total 
impedance; Y, the total shunted admittance of a transmission 
line, ^Eq and /o, the voltage and current at one end; Ei and Zi, 
the voltage arid current at the other end of the transmission 
line; then. 


^ ^ ,^ ZY Z^Y^] 
Ei = Eo\l+^+-^ 


±ZIo 


ZY Z2y2 

"^ 6 "^ 12"0~ 


, r ,^ ZY Z^Y^] ^^^ \^ ZY Z^Y^] 


(14) 


where the plus sign applies if Eq, Iq is the step-down end, 
the minus sign, if Eq, Iq is the step-up end of the transmission 
line. 

In practically all cases, the quadratic term can be neglected, 
and the equations simplified, thus. 


El = Eq 


..¥Uz,Ji.f 


/i = /o]l+^l±F^o(l+^[, 


and the error made hereby is of the magnitude of less than 


(15) 


Z2Y2 


METHODS OF APPROXIMATION. 207 

Except in the case of very long lines, the second term of 
the second term can also usually be neglected, which givet> 


/,= /o(l+^)±y^o, 


(16) 


and the error made hereby is of the magnitude of less than — 

of the line impedance voltage and line charging current. 

141. Example. Assume 200 miles of 60-cycle line, on non- 
inductive load of ^0 = 100,000 volts; and io = 100 amperes. 
The line constants, as taken from tables are Z = 104 — 140/ ohms 
and F=— 0.0013/ ohms; hence, 

Zy=- (0.182 +0.136/); 

^1 = 100000(1-0.091-0.068/) +100(104-104/) 
= 101400 - 20800/, in volts ; 

fi = 100(1 -0.091 -0.068/) -0.0013/ + 100000 
= 91 — 136.8/, in amperes. 

_, . zy 0.174X0.0013 0.226 ^^_ 

The error is -^ = ^ = — ^ — = 0.038. 

6 6 6 

Neglecting the second term of Ei, ^7o = 17,400, the error is 
0.038 X 17400 = 660 volts = 0.6 per cent. 

Neglecting the second term of h, yEo = lSO, the error is 
0.038 X 130 = 5 amperes = 3 per cent. ' 

Although the charging current of the line is 130 per cent 
of output current, the error in the current is only 3 per cent. 

Using the equations (15), which are nearly as simple, brings 

the error down to -^= '^. =0.0021, or less than one-quarter 

per cent. 

Hence, only in extreme cases the equations (14) need to be 

used. Their error would be less than i=^ = 3.6x10"^, or one 

three-thousandth per cent. 


208 ENGINEERING MATHEMATICS. 

The accuracy of the preceding approximation can be esti- 
mated by considering the physical meaning of Z and Y: Z 
is the hne impedance; hence Zl the impedance voltage, and 

zi 

u=--^, the impedance voltage of the line, as fraction of total 

voltage; Y is the shunted admittance; hence YE the charging 

YE 
current, and v=—j-, the charging current of the line, as fraction 

of total current. 

Multiplying gives uv = ZY; that is, the constant ZY is the 
product of impedance voltage and charging current, expressed 
as fractions of full voltage and full current, respectively. In 
any economically feasible power transmission, irrespective of 
its length, both of these fractions, and especially the first, 
must be relatively small, and their product therefore is a small 
quantity, and its higher powers negligible. 

In any economically feasible constant potential transmission 
line the preceding approximations are therefore permissible.
