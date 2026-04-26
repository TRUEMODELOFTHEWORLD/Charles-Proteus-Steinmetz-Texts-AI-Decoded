CHAPTER XL 

GENERAL SYSTEM OF CIRCUITS. 

(A) Circuits containing resistance and inductance only. 

95. Let, upon a general system or network of circuits con- 
nected with each other directly or inductively, and containing 
resistance and inductance, but no capacity, a system of e.m.fs., 
ey be impressed. These e.m.fs. may be of any frequency or 
wave shape, or may be continuous or anything else, but are 
supposed to be given by their equations. They may be free of 
transient terms, or may contain transient terms depending upon 
the currents in the system. In the latter case, the dependency 
of the e.m.f. upon the currents must obviously be given. 

Then, in each branch circuit, 

^5~=0, (1) 

where e = total impressed e.m.f.; r. = resistance; L = induc- 
tance, of the circuit or branch of circuit traversed by current i, 
and Ms = mutual inductance of this circuit with any circuit in 
inductive relation thereto and traversed by current is. 

The currents in the different branch circuits of the system 
depend upon each other by Kirchhoff's law, 

D i - 0 (2) 

at every branching point of the system. 

By equation (2) many of the currents can be eliminated by 
expressing them in terms of the other currents, but a certain 
number of independent currents are left. 

Let n = the number of independent currents, denoting these 
currents by i-K, where K = 1, 2, . . . n. (3) 

Usually, from physical considerations, the number of inde- 
pendent currents of the system, n, can immediately be given. 

168 


GENERAL SYSTEM OF CIRCUITS 169 

For these n currents iK, n independent differential equations 
of form (1) can be written down, between the impressed e.m.fs. 
ey or their combinations, and currents which are expressed by 
the n independent currents iK. They are given by applying 
equation (1) to a closed circuit or ring in the system. 

These equations are of the form 

eq~r V'*~?K c^ = 0 | (4) 

where q = 1, 2, ... n, 

where the n2 coefficients bq are of the dimension of resistance ) ,-\ 
and the n2 coefficients cKq of the dimension of inductance. ) ^ 

These n simultaneous differential equations of n variables iK 
are integrated by the equations 


' A?,-*, (6) 

1 

where iKf is the stationary value of current iK, reached for t = <x> . 
Substituting (6) in (4) gives 


M^-^O. (7) 

1 


For t = oo , this equation becomes 


These n equations (8) determine the stationary components 
of the n currents, iK'. 

Subtracting (8) from (7) gives, for the transient components 
of currents iK, 


the n equations 


170 TRANSIENT PHENOMENA 

Reversing the order of summation in (10) gives 

A-o =0- 


(11) 


The n equations (11) must be identities, that is, the coefficients 
of £~aJ must individually disappear. Each equation (11) thus 
gives m equations between the constants a, A, b, c, for i = 1, 
2, . . . m, and since n equations (11) exist, we get altogether mn 
equations of the form 


where 


-0, 


q = 1, 2, 3,. . . n and i = 1, 2, 3,. . . m. 


(12) 


In addition hereto, the n terminal conditions, or values of 
current iK" for t = 0: iK°, give by substitution in (9) n further 
equations, 


(13) 


There thus exist (mn + n) equations for the determination 
of the mn constants A* and the m constants ai} or altogether 
(mn + m) constants. That is, 


and 
where 


m = n 

n 

i* = i' + 2)1' A* £~a*> 
i 


Af 


<„•; 


and 


(14) 
(15) 

(16) 
(17) 

(18) 


GENERAL SYSTEM OF CIRCUITS 


171 


Each of the n sets of n linear homogeneous equations in 
A* (16) which contains the same index i gives by elimination 
of At" the same determinant : 


-a^1, bf-atf, b^- 


Thus the n values of at are the n roots of the equation of nth 
degree (19), and determined by solving this equation. 

Substituting these n values of at in the equations (16) gives 
n2 linear homogeneous equations in A/, of which n (n — 1) are 
independent equations, and these n (n — 1) independent equa- 
tions together with the n equations (17) give the n2 linear 
equations required for the determination of the n2 con- 
stants A*. 

The problem of determining the equations of the phenomena 
in starting, or in any other way changing the circuit conditions, 
in a general system containing only resistance and inductance, 
with n independent currents and such impressed e.m.fs., ey, 
that the equations of stationary condition, 


can be solved, still depends upon the solution of an equation of 
nth degree, in the exponents at of the exponential functions 
which represent the transient term. 

96. As an example of the application of this method may 
be considered the following case, sketched diagrammatically in 
Fig. 42: 

An alternator of e.m.f. E cos (6 - 00) feeds over resistance 
rl the primary of a transformer of mutual reactance xm. The 
secondary of this transformer feeds over resistances r2 and rs 
the primary of a second transformer of mutual reactance xmo, 
and the secondary of this second transformer is closed by resist- 
ance r4. Across the circuit between the two transformers and 
the two resistances r2 and r3, is connected a continuous-current 


172 


TRANSIENT PHENOMENA 


e.m.f., e0, as a battery, in series with an inductive reactance x. 
The transformers obviously must be such as not to be saturated 
magnetically by the component of continuous current which 
traverses them, must for instance be open core transformers. 


Fig. 42. Alternating-current circuit containing mutual and self-inductive 
reactance, resistance and continuous e.m.f. 


Let iv iv iw is, i4 = currents in the different circuits; then, at 
the dividing point P, by equation (2) we have 


hence, iQ = i3 — i2, 

leaving four independent currents iv i2, i3, i^. 
This gives four equations (4) : 


E 


M 


-e- 


=0, 


Xm , _ ~\ X ( ~~~ 

,dd 
•x\**- ^1 

"^ \ JQ JQ I ~ U? 


(20) 


and 


(21) 


If now i/, i2', i',, t/ are the permanent terms of current, by 
substituting these into (21) and subtraction, the equations of 
the transient terms rearranged are : 


q: K = 

1 

2 
3 


GENERAL SYSTEM OF CIRCUITS 
234 


173 


di2 

__ nt £ I If n I /v. 

* 7rt I ' •*» 1^'*' 


do 

din 


0, 


= 0, 


^'4 

W 


0. 


(22) 


These equations integrated by 


.-a, a 


(23) 


give for the determination of the exponents c^ the determinant 

(19): 

r, - axm 0 0 


0 

0 ax r3 — ax - axmo 


0 0 


-ax 


mo 


= 0; 


(24) 


or, resolved, 


- a 


- axrxr4 (ra + ra) + r1rar8r4 = 0. 

Assuming now the numerical values, 
rt = 1 


(25) 


r, « 1 


xm = 10 

X™Q = 10 

« = 100 
r4 = 10 

equation (25) gives 

/ = a4 + 11 a3 - 0.11 a2 - 0.2 a + 0.001 = 0. 

The sixteen coefficients, 

A?, i = 1, 2, 3, 4, ft = 1, 2, 3, 4, 

are now determined by the 16 independent linear equations (12) 
and (13). 


(27) 


1T4 TRANSIENT PHENOMENA 

(B) Circuits containing resistance, self -inductance, mutual in- 
ductance and capacity. 

97. The general method of dealing with such a system is the 
same as in (A). 

Kirchhoff's equation (1) is of the form 

i 

dt = 0. (28) 

Eliminating now all the currents which can be expressed 
in terms of other currents, by means of equation (2), leaves 
n independent currents : 

iK, K = 1, 2, . . . n. 

Substituting these currents iK in equations (28) gives n inde- 
pendent equations of the form 

n n 7 • n 

eq - X" &A - X" c«'-ir - X" &ff / *« dt = °- (29) 

i i i 

Resolving these equations for / iK dt gives 

e/ = i fi*= 2> + I>- + 2;c^ (so) 


as the equations of the potential differences at the condensers. 
Differentiating (29) gives 


where q = 1, 2, . . . n. 

By the same reasoning as before, the solution of these equa- 
tions (31) can be split into two components, a permanent term, 

(32) 


and a transient term, which disappears for t = oo , and is given 
by the n simultaneous differential equations of second order, 
thus : 


GENERAL SYSTEM OF CIRCUITS 
These equations are integrated by 

m 

IK ^ ^^l i ^ ' * 

1 

Substituting (34) in (33) gives 


where q = 1, 2, . . . n, 

* = 1, 2, . . . n, 

and i = 1, 2, . . . m. 

Reversing in these n equations the order of summation, 


175 

(34) 

(35) 
(36) 


= 0, (37) 


and this gives, as identity, the mn equations for the determina- 
tion of the constants : 


where 


(38) 


q = 1, 2, . . . n and i = 1, 2, . . . m. 

In addition to these mn equations (38), two sets of terminal 
conditions exist, depending respectively on the instantaneous 
current and the instantaneous condenser potential at the moment 
of start. 

The current is 


and the condenser potential of the circuit q is 


hence, for i = 0, 


« o _ v / i \V A * 

*« - 1K ' ' Zu **» 1 


(39) 


' ; (40) 


(41) 


176 TRANSIENT PHENOMENA 

where K = 1, 2, . . . n, 

and e* = eq - £. 6.V •- £ « c,< ^° , (42) 

i i 

where, q = 1, 2 ... n; 

or, substituting (39) in (40), and then putting t = 0, 


)1' 4"(&.« - OA4). (43) 


1 1 

As seen, in (41) and (43), the first term is the instantaneous 
value of the permanent current i'K and condenser potential eq'. 

These two sets of n equations each, given by the terminal 
conditions of the current, i'K = iK° (42), and condenser potential, 
eq' = eq° (43), together with the mn equations (38), give a total 
of (mn + 2 n) equations for the determination of the mn con- 
stants A* and the m constants ai} that is, a total of (mn + m) 
constants. 

From 

mn + 2 n = mn -f m 

it follows that 

m = 2 n. (44) 

We have, then, 2 n constants, ai} giving the coefficients in the 
exponents of the 2 n exponential transient terms, and 2 n2 
coefficients, A*, and for their determination 2n2 equations, 

£« Af (g* - aj>* + afcf) = 0, (45) 

i 

n equations, 

t = i«, (46) 


and n equations, 

x^ 

i i 


GENERAL SYSTEM OF CIRCUITS 


where 


ft*! ; 

«y J<=o 


177 

(48) 


or the difference between the condenser potential required by 
the permanent term and the actual condenser potential at time 
t = 0} where 

q = 1, 2, 3, . . . n, 


and 


K = 1, 2, 3, . . . n, 
i = 1, 2, 3, . . . 2 n. 


(49) 


Eliminating A* from the equations (45) gives for each of the 
2 n sets of n equations which have the same at- the determinant : 


g3n - 


= 0.(50) 


The 2 n values of a, thus are the roots of an equation of 2 nth 
order. 

Substituting these values of at- in equations (45), (46), (47), 
leaves 2 n (n — 1) independent equations (45) and 2 n inde- 
pendent equations (46) and (47), or a total of 2 n2 linear equa- 
tions, for the determination of the 2 n2 constants Aft which now 
can easily be solved. 

The roots of equation (50) may either be real or may be com- 
plex imaginary, and in the latter case each pair of conjugate 
roots gives by elimination of the imaginary form an electric 
oscillation. 

That is, the solution of the problem of n independent circuits 
leads to n transient terms, each of which may be either an 
oscillation or a pair of exponential functions. 

98. The preceding discussion gives the general method of the 
determination of the transient phenomena occurring in any 
system or net work of circuits containing resistances, self-indue- 


178 TRANSIENT PHENOMENA 

tances and mutual inductances and capacities, and impressed and 
counter e.m.fs. of any frequency or wave shape, alternating or con- 
tinuous. 

It presupposes, however, 

(1) That the solution of the system for the permanent terms 
of currents and e.m.fs. is given. 

(2) That, if the impressed e.m.fs. contain transient terms 
depending upon the currents in the system, these transient 
terms of impressed or counter e.m.fs. are given as linear functions 
of the currents or of their differential coefficients, that is, the 
rate of change of the currents. 

(3) That resistance, inductance, and capacity are constant 
quantities, and for instance magnetic saturation does not appear. 

The determination of the transient terms requires the solution 
of an equation of 2 nth degree, which is lowered by one degree 
for every independent circuit which contains no capacity. 

Thus, for instance, a divided circuit having capacity in either 
branch leads to a quartic equation. A transmission line loaded 
with inductive or non-inductive load, when representing the 
capacity of the line by a condenser shunted across its middle, 
leads to a cubic equation.
