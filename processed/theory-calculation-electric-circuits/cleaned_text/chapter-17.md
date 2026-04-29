CHAPTER XVII 

CIRCUITS WITH DISTRIBUTED LEAKAGE 

172. If an uninsulated electric circuit is immersed in a high- 
resistance conducting medium, such as water, the current does 
not remain entirely in the "circuit,*' but more or less leaks 
through the surrounding medium. The current, then^ is not the 
same throughout the entire circuit, but varies from point to point: 
the currents at two points of the circuit differ from each other by 
the current which leaks from the circuit between these two points. 

Such circuits with distributed leakage are the rail return circuit 
of electric railways; the lead armors of cables laid directly in the 
ground; water and gas pipes, etc. With lead-armored cables in 
ducts, with railway return circuits where the rails are supported 
•above the ground by sleepers, as in interurban roads, the leakage 
may be localized at frequently recurring points; the breaks in the 
ducts, the sleepers supporting the rails, etc., but even then an 
assumption of distributed leakage probably best represents the 
conditions. The same applies to low-voltage distributing sys- 
tems, telephone and telegraph lines, etc. 

The current in the conductor with distributed leakage may 
be the result of a voltage impressed upon a circuit of which the 
leaky conductor is a part, as is the case with the rail return of 
electric railways, or occurs when a cable conductor grounds on 
the cable armor, and the current thereby returns over the armor; 
or it may be induced in the leaky conductor, as in the lead armor 
of a single-conductor cable traversed by an alternating current; 
or it may enter the conductor as leakage current, as is the case 
in cable armors, gas and water pipes, etc., in those cases where 
they pick up stray railway return currents, etc. 

When dealing with direct-current circuits, the induetance and 
the capacity of the conductor do not come into consideration 
except in the transients of current change, and in stationary con- 
ditions such a circuit thus is one of distributed series resistance 
and shunted conductance. 

Inductance also is absent with the current induced in the cable 
armor by an alternating current traversing the cable conductor, 

330 


CIRCUITS WITH DISTRIBUTED LEAKAGE 331 

and with all low- and medium-voltage conductors, with the com- 
mercial frequencies of alternating currents, the capacity effects 
are so small as to be negligible. 

In high-voltage conductors, such as transmission lines, etc., in 
general, capacity and inductance require consideration as well as 
resistance and shunted conductance. This general case is fully 
discussed in "Theory and Calculation of Transient Electric Phe- 
nomena and Oscillations," and in "Electric Discharges, Waves 
and Impulses," more particularly in the fourth section of the 
former book. 

173, Let, then, in a conductor having uniformly distributed 
leakage, or in that conductor section, in which the leakage can 
be considered as approximately uniformly distributed, 

r = resistance per unit length of conductor (series resistance), 

g = leakage conductance per unit length of conductor (shunted 
conductance), 
and assume, at first, that no e.m.f. is induced in this conductor. 

The voltage, de, consumed in any line element, di, of this con- 
ductor, then is that consumed by the current, i, in the series 
resistance of the line element, rdl, thus: 

de = irdl. (1) 

The current, df, consumed in any line element, dl, that is, the 
difference of current between the two ends of this line element, 
then, is the current which leaks from the conductor in this line 
element, through the leakage conductance, gdl, thus; 

di = egdL (2) 

Differentiating (2) and substituting into (1) gives 

dH 

W^ = rgi. (3) 

This equation is integrated by (see "Engineering Mathematics,'' 
Chapter II) 

i = A€-«^ (4) 

Substituting (4) into (3) gives 

hence, 

a = ±\/rg, 
and thus, the current^ 


332 


ELECTRIC CIRCUITS 


where Ai and A 2 are determined by the terminal conditions, as 
integration constants. 

Substituting (5) into (2) gives as the voUage, 


(6) 


174. (a) If the conductor is of infinite length, that is, of such 
great length, that the current which reaches the end is negligible 
compared with the current entering the conductor, it is 

i = for I = 00. 
This gives 

hence, 


A2 = 0, 

i = i4€_-vivi 
e = \i- Ae" 


y/rgl 


4 


= a/- t 


(7) 


That is: 

A leaky conductor of infinite length, that is, of such great length 
that practically no current penetrates to its end, of series resist- 
ance, r, and shunted conductance, g, per unit length, has an effect- 
ive resistance, 

r. = ^ (8) 

It is interesting to note, that a change of r or g changes the 
effective resistance, ro, and thus the current flowing into the con- 
ductor at constant impressed voltage, or the voltage consumed 
at constant-current input, much less than the change of r or g. 

(6) If the conductor is open at the end I = Zo, it is 

i = for I = Zo, 
hence, substituted into (5) 

and, putting 

it is 

i = A{ e"*"^*^ ^'"-'^ — €"" vi^ Co-') } 


= 'J- A {e'^^^'o Co"') _|- g- Vra Co-0 } 


(9) 


CIRCUITS WITH DISTRIBUTED LEAKAGE 333 

(c) If the conductor is grounded at the end I = Zo, it is 

e = for Z = Zo, 
hence, substituted into (6), 

= Ai€"Viv/o_ ^2€+V^^^, 


and, putting 
it is 


(10) 


(d) If the circuit, at Z = Zo, is closed by a resistance, R, it is 

- = /2 for Z = Zo, 
t 

hence, substituting (5) and (6), gives 


hence. 


Ai =^i«-2VraJojf| 


R 


Thus, 


>/i+« 


ft 


i = Ale-v"-!-'- 


-i^ 


fl + xf 
^g 


9_ ^-(2/o-OVra 


} 


e = ^4{«-vr»' + 


ft 


- f- 


176. Substituting, 


«+V^ 


OVra} 


(11) 


ro = \/- 

yg 


(8) 


as the ''effective resistance of the leaky conductor of infinite 
length," 


i 


334 ELECTRIC CIRCUITS 

and 

a = v^ (12) 

as the "attenuation constant" of the leaky conductor, it is 


R + ro ' 


(13) 


These equations (13) can be written in various different forms. 
They are interesting in showing in a direct-current circuit features 
which usually are considered as characteristic of wave trans- 
mission, that is, of alternating-current circuits with distributed 
capacity. 

The first term of equations (13) may be considered as the out- 
flowing components of current and voltage respectively, the sec- 
ond terms as the reflected components, and at the end of the 
circuit of distributed leakage, reflection would be considered as 
occurring at the resistance, R. 

If R>ro, the second term is positive, that is, partial reflection 
of current occurs, while the return voltage adds itself to the in- 
coming voltage. If R = <» , the reflection of current is complete. 

If R<r oy the second term is negative, that is, partial reflection 
of voltage occurs, while the return current adds itself to the 
incoming current. If /2 = 0, the reflection of voltage is complete. 

If ft = ro, the second term vanishes, and equations (13) be- 
come those of (7), of an infinitely long conductor. That is: 

A resistance, 72, equal to the effective resistance, ro = \ -,o{ the 

infinitely long conductor of distributed resistance and shunted 
conductance, as terminal of a finite conductor of this character 
passes current and voltage without reflection. A higher resist- 
ance partially reflects the current and increases the voltage, and 
a lower resistance partially reflects the voltage and increases the 
current. Infinite resistance gives complete reflection of current 
and doubles the voltage, while zero resistance gives complete re- 
flection of voltage and doubles the current. 

The term,ro = -v/-, thus takes in direct-current circuits the same 

position as the ''surge impedance" -v/t^ or -v/ y in alternating-cur- 
rent circuits. 


CIRCUITS WITH DISTRIBUTED LEAKAGE 335 

176, Consider an instance: it has been proposed, for the pur- 
pose of effectively grounding the overhead ground wire used for 
protection of transmission lines, to run a bare underground con- 
ductor, a few feet below the ground surface, and to connect the 
overhead ground wire to the underground wire at every pole. 
Assuming the underground conductor to be a bare copper wire 
having 0.41 cm. diameter, the overhead ground wire a steel cable 
equivalent in conductivity to a copper wire of 0.52 cm. diameter. 
What is the effective ground resistance of the underground wire 
alone, what that of the underground and overhead wire together? 
Assuming the leakage resistance of the underground wire to be 
3 X 10"' mhos per meter? 

The resistance of the underground wire is 1.3 X 10"' ohms, that 
of the overhead ground wire is 0.82 X 10"' ohms per meter. 

The effective resistance of one underground wire then is 

r = 1.3 X 10-'; g = 3 X 10"', hence, 

ro = 0.66 ohm 

thus, two underground wires in multiple, in the two different di- 
rections, give an effective ground resistance of 

0.33 ohm, 

including the overhead ground wire, the resistance is 

r = J J = 0.5 X 10-'; flf = 3 X 10"', 

1.3 X 10"' "*" 0.82 X 10-' 
hence, 

ro = 0.41 ohm, 

thus, the two underground and two overhead wires together give 
an effective resistance of 

0.205 ohm. 

This is a very much lower ground resistance than most local 
grounds possess. 

Assuming that io is the current which enters this ground wire 
at one point, I = 0, then the equation of current distribution, by 
(7), is 

r = 0.25 X 10"'; g = 6 X 10"' (two in multiple, m 

the two opposite directions) 


336 


ELECTRIC CIRCUITS 


hence 


ro = yjl = 0. 


205 


C-1.22W 


a = y/rg = 1.225 X IQ-^ 
thus, 

i = to€" 

6 = 0.205 io€-i-22« 

where { is given in kilometers. 

At various distances from the starting point, the current in 
the conductors thus is: 


distance: 0. . 
i X io X 1. . 


0.5 
0.54 


1.0 
0.294 


1.5 
0.155 


2.0 
0.086 


2.5 
0.046 


3.0 
0.025 


4.0 
0.0074 


5 km. 
0.0021 


As seen, beyond 2 km. distance, the current in the conductor is 
practically nothing. 

177. If the current, i, is an alternating current, and the con- 
dition such that inductance and capacity are negligible, the 
equations (7), (9), (10), (11) and (13) remain the same, except that 
i, 6 and A are vector quantities, or general numbers: J, ^, A. 

Considering thus the more general case, where a voltage is in- 
duced in the leaky conductor. Such for instance is the case in the 
lead armor of a single-conductor alternating-current cable. 
Let, then, 

r = resistance per unit length, 

g = shunted conductance per unit length, 

-Fo = voltage induced in the conductor, per unit length. 


It is, then, in a line element, di. 


11 = ^/ - ^0 


dl 


= g^ 


(14) 


(15) 


Differentiating (15) and substituting into (14) gives 

This is integrated by 

r 


(16) 


(17) 


CIRCUITS WITH DISTRIBUTED LEAKAGE 337 

and by substituting (17) into (16), we get 

o« = rg (18) 

hence, the current, 

I = ^.6-' + 42*-^-' + — " (19) 

r 

where 

a = +\^rg 

and A I and A 2 are complex imaginary integration constants. 
Substituting (18) into (15) gives the voUagey 

^ = ro{Aic-«^- 42€+«^} (20) 

where 


ro = ^: 


- (21) 

g 

178. Suppose now no voltage is impressed upon the conductor, 
but the only existing voltage is that induced in the conductor, 
as for instance the cable armor. 

(a) Suppose the conductor is open at both ends: I = +h and 
Z = — Zo, having the length 2 Zo. 

It then is 

/ = for Z = ±Zo 

Substituting this in (19) gives 

Ai€-^^» + A2€-^'« + — = 

r 


hence, 


and 


A A —El 

Ai = A2 = 


y(^^^lo -f €"^'") 


Eo 

r 


1 - 


^ = Lo^„p-'-*-' 


in the center of the conductor, for Z = 0, it is 

Eo 


(22) 


f= r 

^ = 

22 


1 - 


€-Wo + € 


-xU 


338 


ELECTRIC CIRCUITS 


at the ends of the conductor, for J = ± h, it is 

/ = 


— alo 


-al. 


hence, if the conductor is long, so that € is negligible compared 


with 


.+aio 


, it is 


For an infinitely long conductor, io = «> , equations (22) become 

-Bo 


/ = 


(23) 


^ = 
as was to be expected. 

(6) Suppose the conductor is grounded at one end, Z = 0, and 
open at the other end, I = h. It is, then, 

^ = for Z = 
/ = for Z = Jo, 

hence, the equations are the same as (22). That is, a conductor 
grounded at one end and opeA at the other is the same as a con- 
ductor of twice the length, open at both ends. 

A conductor grounded at both ends gives the same equation as 
an infinitely long conductor (23). 

Suppose alo is large, so that €~ ^ is negligible compared with 
e"^**^, in equation (22). Then for all values of Z, except those very 
close to Zo, -F and the exponential term of / are negligible. 

That is, for the entire length of the leaky conductor, except 
very close to the ends, it is, approximately, 

Eo 


/ = 


(24) 


^ = 

Near the ends of the conductor, where I is near to Zo, e"^ is 
negligible compared with e"^"', and equations (22) thus assume the 
form, 

Eo 
r 


f ^^\l ^ ^-a(lo-l)\ 


E = - Eot-^^^-^^ 
r 


(25) 


CIRCUITS WITH DISTRIBUTED LEAKAGE 339 

179. As an instance, consider the lead armor of a single-conductor 
cable, 10 km. long, carrying an alternating current such that it 
induces 60 volts per kilometer. The armor is open at either end, 
and of internal diameter of 4.2 cm., external diameter of 4.6 cm. 
The leakage conductance from the cable armor to ground is 1 
mho per kilometer. What is the voltage and current distribution 
in the cable? What is it with 10 mhos, what with 0.1 mho per 
kilometer leakage conductance? 

A lead section of the armor of (2.3* — 2.1*) x = 2.7 cm.*, at 
the specific resistance of lead p = 19 X 10"*, gives: r = 0.7 ohm 
per kilometer. 
It is, then, 

r = 0.7 

(7= 1 
lo = 5 

£o = 60 
thus, 

a = 0.84 
ro = 0.84 
hence 

/ = 86{ 1 - 0.015 («+°-»*' + «-»■«*') } 
^ = 1.08{€+°**' -«-"**'} 


(26) 


Thus the maximum current in the cable armor is, Z = 0: / = 
83.4 amp., and this current decreases very slowly, and is still, for 
I = 2:/ = 79 amp. 

The maximum voltage between cable armor and ground is, for 
I = ±5: £ = 72 volts, and decreases fairly rapidly, being, for 
I = ±4:£ = 31.1 volts. 

If the cable is laid in very well-conducting soil, 


it is 


Sf = 10 


a = 2.65 
ro = 0.265. 

/ = 86{1 - 1.75 X 10-^6+2-^' + c-^-^)} \ ,„. 
^ = 40 X 10-^ {6+2-«^ - €-2-^ } J ^^^^ 

in this case, the current is practically constant, / = 86, and the 
voltage zero over the entire cable armor except very near the ends, 
where it rises to -B = 22.7 volts for I = 5. Within 1 km. from 
the ends, or for Z = 4, it is still: / = 80; B = 1.6. That is, over 


340 


ELECTRIC CIRCUITS 


most of the length, the cable armor already acts as an infinitely 
loQg conductor. 

Hence, for values of I near the end of the conductor, / and E ^^ 
more conveniently expressed by the equation (25), 

E = 22 7«~^'**''~" I 


i: 


I 


9 


10 


/ 


180 


— 


yz. 


■=. 


Li; 


— 


— 


~~N 


/ 


1«1 


/ 


/ 


a- 


1 


N 


^ 


M 


/ 


/ 


V\ 


/ 


1 


I 


_^ 


/ 


1 


an 


1 


/- 


" 


3 


■-1 


^ 


y 


/ 


/ 


/ 


\ 


)f 


in 


// 


/ 


' 


; 


;, \ 


so 


/ 


/ 


^ 


A 


a 


/a 


10 


^ 


" 


/ 


/ 


'I 


1 


/ 


-40 


1 


A 


-.1 


-m 


/ 


/ 


1 


1 


1 


1 


iWI 


_ 


Inversely, if the cable is laid in ducts, which are fairly dry, and 
the leakage conductance thus is only 


a = 0.265 
ro = 2.65 


CIRCUITS WITH DISTRIBUTED LEAKAGE 341 
hence, 


(29) 


/ = 86 { 1 - 0.25 (€+o-2«« + €-«-26W) } 

In this case, the maximum voltage between cable armor and 
ground is, at Z = ±5 :E = 200. 

As illustrations are shown, in Fig. 128, with I as abscissse, the 
curves of / and E, calculated from equations (26), (28) and (29). 

180. Considering now the case of a conductor, which is not 
connected to a source of voltage, nor has any voltage induced in 
it, but is laid in a ground in which a potential difference exists, 
due to stray currents passing through the ground. Such, for 
instance, may be a water pipe laid in the ground parallel with a 
poorly bonded railway circuit. 

Assuming the potential difference, 6o, exists in the ground, per 
unit length of conductor. The conditions obviously are the same, 
as if the ground were at constant potential, and the potential 
difference, -eo, existed in the conductor per unit length. Thus 
we get the same equations as (22) and (23). If the potential 
difference is continuous, as when due to a direct-current railway 
circuit, obviously the quantities I, E, Ai and A 2 are not alternat- 
ing vector quantities, but scalar numbers: i, c, etc. That is, 


e = — eo 


60 

t = — 

r 


ro €+*»' — e-"' 


(30) 


Assuming thus as an instance a water pipe of 5 km. length: 
{0 = 5, extending through a territory having 50 volts potential 
difference, or : 60 = 10. Assuming that it is connected with the 
return circuit so that there is no potential difference at one end: 

e = for Z = 0. 

Let the resistance of the water pipe be r = 0.01 ohm per kilo- 
meter, and the leakage conductance be g = 10 mhos per kilometer. 
It is, then, 

r = 0.01 
Sf = 10 
io = 5 

Co = 10 
thus, 

a = 0.316 

ro = 0.0316 


342 

hence, 


ELECTRIC CIRCUITS 

i - 1000 I 1 - 0.2 (,+•■"■' + ,-«■•'") I 
e - 6.2 I ,*■"" - ,->■"•!] 


hence, the maximum current, toil = Q:i = 600 amp. 
the maximum voltage, for I = 5 : e = 28.8 volts. 


iw' 


/ 


i: 


/ 


~- 


/ 


\ 


/ 


fa 


600 


^, 


/ 


\ 


IB 


m 


y 


1! 


WO 


e/ 


\ 


^■ 


in 


» 


/ 


y 


200 


/ 


if H 


^ \ 


s 


/ 


.' 


\ 


/ 


\, 


^:^ 


• 


u 


S i 


A 


(31) 


As seen, a very considerable current may flow under these 
conditions. 

Fig. 129 shows, with I as abscissie, the current, i, and voltage, e, 

and the current which enters the conductor per unit length, ».
