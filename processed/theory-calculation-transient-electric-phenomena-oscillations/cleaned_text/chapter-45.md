CHAPTER V. 

DISTRIBUTED SERIES CAPACITY. 

43. The capacity of a transmission line, cable, or high-poten- 
tial transformer coil is shunted capacity, that is, capacity from 
conductor to ground, or from conductor to return conductor, or 
shunting across a section of the conductor, as from turn to turn 
or layer to layer of a transformer coil. 

In some circuits, in addition to this shunted capacity, dis- 
tributed series capacity also exists, that is, the circuit is broken 
at frequent and regular intervals by gaps filled with a dielectric 
or insulator, as air, and the two faces of the conductor ends thus 
constitute a condenser in series with the circuit. Where the 
elements of the circuit are short enough so as to be represented, 
approximately, as conductor differentials, the circuit constitutes 
a circuit with distributed series capacity. 

An illustration of such a circuit' is afforded by the so-called 
" multi-gap lightning arrester," as shown diagrammatically in 
Fig. 90, which consists of a large number of metal cylinders p, q 
. . . , with small spark gaps between the cylinders, connected 
between line L and ground G. This arrangement, Fig. 90, can 
be represented diagrammatically by Fig. 91. Each cylinder has 
a capacity (70 against ground, a capacity C against the adja- 
cent cylinder, a resistance r, — usually very small, — and an 
inductance L. 

If such a series of n equal spark gaps is connected across a 

& 
constant supply voltage e0, each gap has a voltage e = — . If, 

Tl 

however, the supply voltage is alternating, the voltage does not 
divide uniformly between the gaps, but the potential difference 
is the greater, that is, the potential gradient steeper the nearer 
the gap is to the line L, and this distribution of potential becomes 
the more non-uniform the higher the frequency; that is, the 
greater the charging current of the capacity of the cylinder 
against ground. The charging currents against ground, of all 

848 


DISTRIBUTED SERIES CAPACITY 


349 


the cylinders from q to the ground G, Figs. 90 and 91, must pass 
the gap between the adjacent cylinders p and g; that is, the 
charging current of the condenser represented by two adjacent 


-00000000000000-1 


Fig. 90. Multi-gap lightning arrester. 

cylinders p and q is the sum of all the charging currents from 
qtoG', and as the potential difference between the two cylinders 
p and q is proportional to the charging current of the condenser 


'filMI — i 


T 


Fig. 91. Equivalent circuit of a multi-gap lightning arrester. 

formed by these two cylinders, C, this potential difference 
increases towards L, being, at each point proportional to the 
vector sum of all the charging currents, against ground, of all 
the cylinders between this point and ground. 

The higher the frequency, the more non-uniform is the poten- 
tial gradient along the circuit and the lower is the total supply 
voltage required to bring the maximum potential gradient, near 
the line L, above the disruptive voltage, that is, to initiate the 
discharge. Thus such a multigap structure is discriminating 
regarding frequency; that is, the discharge voltage with increas- 


350 TRANSIENT PHENOMENA 

ing frequency, does not remain constant, but decreases with 
increase of frequency, when the frequency becomes sufficiently 
high to give appreciable charging currents. Hence high fre- 
quency oscillations discharge over such a structure at lower 
voltage than machine frequencies. 

For a further discussion of the feature which makes such a 
multigap structure useful for lightning protection, see A. I. E. E. 
Transactions, 1906, pp. 431, 448, 1907, p. 425, etc. 

44. Such circuits with distributed series capacity are of great 
interest in that it is probable that lightning flashes in the clouds 
are discharges in such circuits. From the distance traversed by 
lightning flashes in the clouds, their character, and the disruptive 
strength of air, it appears certain that no potential difference 
can exist in the clouds of such magnitude as to cause a disruptive 
discharge across a mile or more of space. It is probable that 
as the result of condensation of moisture, and the lack of uni- 
formity of such condensation, due to the gusty nature of air 
currents, a non-uniform distribution of potential is produced 
between the rain drops in the cloud; and when the potential 
gradient somewhere in space exceeds the disruptive value, an 
oscillatory discharge starts between the rain drops, and grad- 
ually, in a number of successive discharges, traverses the cloud 
and equalizes the potential gradient. A study of circuits 
containing distributed series capacity thus leads to an under- 
standing of the phenomena occurring in the thunder cloud during 
the lightning discharge.* 

Only a general outline can be given in the following. 

45. In a circuit containing distributed resistance, conductance, 
inductance, shunt, and series capacity, as the multigap lightning 
arrester, Fig. 90, represented electrically as a circuit in Fig. 91, 
let r = the effective resistance per unit length of circuit, or per 
circuit element, that is, per arrester cylinder; g = the shunt 
conductance per unit length, representing leakage, brush dis- 
charge, electrical radiation, etc.; L = the inductance per unit 
length of circuit; C = the series capacity per unit length of cir- 
cuit, or circuit element, that is, capacity between adjacent arrester 
cylinders, and <70 = the shunt capacity per unit length of circuit, 
or circuit element, that is, capacity between arrester cylinder and 

* See paper, "Lightning and Lightning Protection," N.E.L.A., 1907. 
Reprinted and enlarged in " General Lectures on Electrical Engineering," by 
Author. 


DISTRIBUTED SERIES CAPACITY 351 

ground. If then / = the frequency of impressed e.m.f., the 
series impedance per unit length of circuit is 

Z'=r-j(x-xc); (1) 

the shunt admittance per unit length of circuit is 

Y - g - jb, (2) 

where 

x = 2 nfL, 

1 


b - 2 xfCt; 
or the absolute values are 


(3) 


z = Vr2 + (x~xcy 
and (4) 

y = 


If the distance along the circuit from line L towards ground 
G is denoted by Z, the potential difference between point I and 
ground by E, and the current at point I by 7, the differential 
equations of the circuit are * 

f-Z7 (5) 

and 

. l-3^ <6> 

Differentiating (5) and substituting (6) therein gives 

(7) 

tM 

Equation (7) is integrated by 

where 

a = VYZ = a - //?, (9) 


« = ^\{yz + gr — b (x — xc)} 
and J- (10) 

/? = 


* Section III, Chapter II, paragraph 7. 


352 TRANSIENT PHENOMENA 

Substituting (10) in (8) and eliminating the imaginary expo- 
nents by the substitution of trigonometric functions, 

E = A,£-al (cos pi + j sin pi) + A2e+al (cos pi - j sin pi). (11) 

46. However, if n = the total length of circuit from line L to 
ground G, or total number of arrester cylinders between line and 
ground, for I = n, 

E = 0, (12) 

and for I = 0, 

E = e0 = the impressed e.m.f, (13) 

Substituting (12) and (13) into (11) gives 

0 = Ajfi— * (cos pn + j sin pri) + A2e+an (cos pn- - j sin pri) 

and 

eo = «i ~t~ ^jJ 

hence, 

1 "" 1 - £-2an (cos 2 ph f j sin 2 /?n) ' (14) 

A2 = - A^"2"*1 (cos 2pn + j sin 2 /?n), 
and the potential difference against ground is 

c'-a'(cos pl+j sin pi) - £-*(2*-f) [cos /? (2 n-Z) +/ sin p(2n-l)] 
1 - £~2*n (cos 2pn + j sin 2 /?n) 

(15) 
From equation (5), substituting (15) and (9), we have 


(cos pl + j sin pl)+e~a(2n-l) [cos p(2n-l) +j sin ft (2 n-Z)] 


1 _ £-2aw(cos 2pn + j sin 

(16) 

Reduced to absolute terms this gives the potential difference 
against ground as 


4/j-s ll + e-2-C2»-o._2e : twcos2/?(n -Z) 
6==eoV r- -^i^ — o.-2<m^ r^-^: » (17) 


DISTRIBUTED SERIES CAPACITY 353 

the current as 


"! +' "+2e-:-"cos2/?(tt-0 

1 +«-««- 2. -»- COB 


and the potential gradient, or potential difference between adja- 
cent cylinders, is 


For an infinite length of line, n = <*> , that is, for a very large 
number of lightning arrester cylinders, where e~2an is negligible, 
as in the case where the discharge passes from the line into the 
arrester without reaching the ground, equations (17), (18), (19) 
simplify to 

• -V"1, (20) 


(21) 

1 £ 

and 

e> = e0xc \Jy-t-*l\ (22) 

that is, are simple exponential curves. 
Substituting (4) and (3) in (21) and (22) gives 


c 2 + 

(23) 


C2j[l - (2^/ 

and 

; = 27r/Ce'; (24) 

or, approximately, if r and </ are negligible, we have 


e' 
and 


- v cir-- 


47. Assume, as example, a lightning arrester having the fol- 
lowing constants: L = 2 X 10~8 henry; C0 = 10~13 farads; 


354 TRANSIENT PHENOMENA 

C = 4 X 10~n farads; r = 1 ohm; g = 4 X 10-6 mho;/ - 108 = 
100 million cycles per second; n = 300 cylinders, and e0 = 30,000 
volts; then from equation (3), x = 12.6 ohms, xc = 39.7 ohms, and 
b = 62.8 X 10-6 mhos; 

from equation (1), 

Z = 1 + 27.1 / ohms; 

from equation (2), 

Y = (4 - 62.8 j)10-6 mho; 
from equation (4), 

z = 27.1 ohms and y = 62.9 X 10~6 mho; 
from equation (10), 

a = 0.0021 and /? = 0.0412; 
from equation (17), 

e = 35,500 Vr0™21 + 0.08 e*-0042' - 0.568 cos (24.72 -0.0824 Q; 
from equation (18), 

i = 54 V£-0-0042 ' + 0.08 e^0'0042 1 + 0.568 cos (24.72 - 0.0824 /), 
and from equation (19), 


e' - 2140 v^0-0042 ' + 0.08 e^-0042' +0.568 cos (24.72 - 0.0824 I) . 

Hence, at I = 0, e = 30,000 volts, i - 64.6 amperes, and 
ef = 2560 volts; and at I = 300, e = 0, i = 57.5 amperes, arid 
^ = 2280 volts. 

With voltages per gap varying from 2280 to 2560, 300 gaps 
would, by addition, give a total voltage of about 730,000, while 
the actual voltage is only about one-twenty-fourth thereof; that 
is, the sum of the voltages of many spark-gaps in series may be 
many times the resultant voltage, and a lightning flash may pass 
possibly for miles through clouds with a total potential of only 
a few hundred million volts. In the above example the 300 
cylinders include 7.86 complete wave-lengths of the discharge.
