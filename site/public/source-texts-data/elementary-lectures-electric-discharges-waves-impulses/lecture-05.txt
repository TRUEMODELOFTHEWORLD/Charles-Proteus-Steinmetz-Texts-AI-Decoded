LECTURE V. 

SINGLE-ENERGY TRANSIENT OF IRONCLAD 
CIRCUIT. 

22. Usually in electric circuits, current, voltage, the magnetic 
field and the dielectric field are proportional to each other, and the 
transient thus is a simple exponential, if resulting from one form of 
stored energy, as discussed in the preceding lectures. This, how- 
ever, is no longer the case if the magnetic field contains iron or 
other magnetic materials, or if the dielectric field reaches densities 
beyond the dielectric strength of the carrier of the field, etc. ; and 
the proportionality between current or voltage and their respective 
fields, the magnetic and the dielectric, thus ceases, or, as it may be 
expressed, the inductance L is not constant, but varies with the 
current, or the capacity is not constant, but varies with the voltage. 

The most important case is that of the ironclad magnetic cir- 
cuit, as it exists in one of the most important electrical apparatus, 
the alternating-current transformer. If the iron magnetic circuit 
contains an air gap of sufficient length, the magnetizing force con- 
sumed in the iron, below magnetic saturation, is small compared 
with that consumed in the air gap, and the magnetic flux, therefore, 
is proportional to the current up to the values where magnetic 
saturation begins. Below saturation values of current, the tran- 
sient thus is the simple exponential discussed before. 

If the magnetic circuit is closed entirely by iron, the magnetic 
flux is not proportional to the current, and the inductance thus not 
constant, but varies over the entire range of currents, following 
the permeability curve of the iron. Furthermore, the transient 
due to a decrease of the stored magnetic energy differs in shape 
and in value from that due to an increase of magnetic energy, since 
the rising and decreasing magnetization curves differ, as shown by 
the hysteresis cycle. 

Since no satisfactory mathematical expression has yet been 
found for the cyclic curve of hysteresis, a mathematical calcula- 
tion is not feasible,, but the transient has to be calculated by an 
'^''"r '*_/ ? :,": \ : 52 


SINGLE-ENERGY TRANSIENT OF IRONCLAD CIRCUIT. 53 

approximate step-by-step method, as illustrated for the starting 
transient of an alternating-current transformer in "Transient Elec- 
tric Phenomena and Oscillations," Section I, Chapter XII. Such 
methods are very cumbersome and applicable only to numerical 
instances. 

An approximate calculation, giving an idea of the shape of the 
transient of the ironclad magnetic circuit, can be made by neglect- 
ing the difference between the rising and decreasing magnetic 
characteristic, and using the approximation of the magnetic char- 
acteristic given by Frohlich's formula: 


which is usually represented in the form given by Kennelly: 

T/> 

p = - = a + crOC; (2) 

that is, the reluctivity is a linear function of the field intensity. 
It gives a fair approximation for higher magnetic densities. 

This formula is based on the fairly rational assumption that the 
permeability of the iron is proportional to its remaining magnetiza- 
bility. That is, the magnetic-flux density (B consists of a compo- 
nent 3C, the field intensity, which is the flux density in space, and 
a component (B' = (B — 3C, which is the additional flux density 
carried by the iron. (B' is frequently called the " metallic-flux 
density." With increasing 3C, (B' reaches a finite limiting value, 
which in iron is about 

&x' = 20,000 lines per cm2. * 

At any density (B', the remaining magnetizability then is 
(B^' — (B', and, assuming the (metallic) permeability as proportional 
hereto, gives 

and, substituting 


gives 

a, = cftco'rc^ 

* See "On the Law of Hysteresis," Part II, A.I.E.E. Transactions, 1892, 
page 621. 


54 ELECTRIC DISCHARGES, WAVES AND IMPULSES. 
or, substituting 


1_ 1 

*** / t*« ,—fc / (/ • 


gives equation (1). 

For OC = 0 in equation (1), ^ = - ; for 3C = oo » = - ; that is, 

uv a: cr 

in equation (1), - = initial permeability, - = saturation value of 

Oi (7 

magnetic density. 

If the magnetic circuit contains an air gap, the reluctance of the 
iron part is given by equation (2), that of the air part is constant, 
and the total reluctance thus is 

p = ft + ffK, 

where 3 = a plus the reluctance of the air gap. Equation (1), 
therefore, remains applicable, except that the value of a is in- 
creased. 

In addition to the metallic flux given by equation (1), a greater 
or smaller part of the flux always passes through the air or through 
space in general, and then has constant permeance, that is, is given 
by 


23. In general, the flux in an ironclad magnetic circuit can, 
therefore, be represented as function of the current by an expression 
of the form 


where , . = & is that part of the flux which passes through 
1 -f- ut 

the iron and whatever air space may be in series with the iron, 
and a is the part of the flux passing through nonmagnetic 
material. 

Denoting now 


L2 = nc 10-8, i 

where n = number of turns of the electric circuit, which is inter- 
linked with the magnetic circuit, L2 is the inductance of the air 
part of the magnetic circuit, LI the (virtual) initial inductance, that 
is, inductance at very small currents, of the iron part of the mag- 


SINGLE-ENERGY TRANSIENT OF IRONCLAD CIRCUIT. 55 
netic circuit, and =- the saturation value of the flux in the iron. 

72,CJ>' d 

That is, for i = 0, — r- = Z/i ; and for i = oo , <£' = T . 

i 0 

If r = resistance, the duration of the component of the transient 
resulting from the air flux would be 

_ L2 nc 10~8 

*V-7" T~ 

and the duration of the transient which would result from the 
initial inductance of the iron flux would be 


The differential equation of the transient is: induced voltage 
plus resistance drop equal zero ; that is, 


Substituting (3) and differentiating gives 
na 10~8 di . .,_ a di ' . 

(i+Wdi + ncl0rSdt+ 

and, substituting (5) and (6), 


t(l + bi)2 Z5 d* ' 

hence, separating the variables, 

Tidi + Tidi + dt = Q 

The first term is integrated by resolving into partial fractions 

1 1 6 6 

i(l + 6i)2 " i 1 + 6i (1 + 6i)2>. 

and the integration of differential equation (7) then gives 


If then, for the time t = tQ, the current is i = i0, these values 
substituted in (8) give the integration constant C: 

T1log- + !T2logio + T- + ^o + C = 0, (9) 


56 ELECTRIC DISCHARGES, WAVES AND IMPULSES. 
and, subtracting (8) from (9), gives 


1 + 6i 5 ' 


(10) 


This equation is so complex in i that it is not possible to cal- 
culate from the different values of t the corresponding values of i; 
but inversely, for different values of i the corresponding values 
of t can be calculated, and the corresponding values of i and t, 
derived in this manner, can be plotted as a curve, which gives the 
single-energy transient of the ironclad magnetic circuit. 


Tra 


sient o 


Ironclad Inductive Circuit : 


t=2.92- 


i + 


t-.6i j 


l+.6i 


(dotted: t = 1.0851g i— .50?) 


2 3 4 5 

Fig. 29. 


6 seconds 


Such is done in Fig. 29, for the values of the constants 


a = 4 X 105, 
c = 4 X 104, 
b = .6, 
n = 300. 


SINGLE-ENERGY TRANSIENT OF IRONCLAD CIRCUIT. 57 


58 ELECTRIC DISCHARGES, WAVES AND IMPULSES. 
This gives 

T = 4 

Assuming i0 = 10 amperes for t0 = 0, gives from (10) the equa- 
tion : 

4 


T = 2.92 - 1 9.21 log10 ^ + . 


921 


.6 i 


Herein, the logarithms have been reduced to the base 10 by 
division with logwe = .4343. 

For comparison is shown, in dotted line, in Fig. 29, the transient 
of a circuit containing no iron, and of such constants as to give 
about the same duration: 

t = 1.0S5log™i- .507. 

As seen, in the ironclad transient the current curve is very 
much steeper in the range of high currents, where magnetic sat- 
uration is reached, but the current is slower in the range of medium 
magnetic densities. 

Thus, in ironclad transients very high-current values of short 
duration may occur, and such transients, as those of the starting 
current of alternating-current transformers, may therefore be of 
serious importance by their excessive current values. 

An oscillogram of the voltage and current waves in an 11,000-kw. 
high-voltage 60-cycle three-phase transformer, when switching onto 
the generating station near the most unfavorable point of the 
wave, is reproduced in Fig. 30. As seen, an excessive current rush 
persists for a number of cycles, causing a distortion of the volt- 
age wave, and the current waves remain unsymmetrical for many 
cycles.
