# My modification of Python script for reading data from Eastron SDM630 over ModBus


All registers
MODBUS offset | Description | Units | Data type
2 | Phase 2 line to neutral volts | Volts | single
4 | Phase 3 line to neutral volts | Volts | single
6 | Phase 1 current | Amps | single
8 | Phase 2 current | Amps | single
10 | Phase 3 current | Amps | single
12 | Phase 1 power | Watts | single
14 | Phase 2 power | Watts | single
16 | Phase 3 power | Watts | single
18 | Phase 1 volt amps | VoltAm ps | single
20 | Phase 2 volt amps | VoltAm ps | single
22 | Phase 3 volt amps | VoltAm ps | single
24 | Phase 1 volt amps reactive | VAr | single
26 | Phase 2 volt amps reactive | VAr | single
28 | Phase 3 volt amps reactive | VAr | single
30 | Phase 1 power factor (1) | None | single
32 | Phase 2 power factor (1) | None | single
34 | Phase 3 power factor (1) | None | single
36 | Phase 1 phase angle | Degre es | single
38 | Phase 2 phase angle | Degre es | single
40 | Phase 3 phase angle | Degre es | single
42 | Average line to neutral volts | Volts | single
46 | Average line current | Amps | single
48 | Sum of line currents | Amps | single
52 | Total system power | Watts | single
56 | Total system volt amps | VA | single
60 | Total system var | VAr | single
62 | Total system power factor (1) | None | single
66 | Total system phase angle | Degre es | single
70 | Frequency of supply voltages | Hz | single
72 | Import wh since last reset (2) | kWh/M Wh | single
74 | Export wh since last reset (2) | kWH/ MWh | single
76 | Import varh since last reset (2) | kVArh/ MVArh | single
78 | Export varh since last reset (2) | kVArh/ MVArh | single
80 | Vah since last reset (2) | kVAh/ MVAh | single
82 | Ah since last reset(3) | Ah/kAh | single
84 | Total system power demand (4) | Watts | single
86 | Maximum total system power | Watts | single
100 | Total system va demand | VA | single
102 | Maximum total system va demand | VA | single
104 | Neutral current demand | Amps | single
106 | Maximum neutral current demand | Amps | single
200 | Line 1 to line 2 volts | Volts | single
202 | Line 2 to line 3 volts | Volts | single
204 | Line 3 to line 1 volts | Volts | single
206 | Average line to line volts | Volts | single
224 | Neutral current | Amps | single
234 | Phase 1 l/n volts thd | % | single
236 | Phase 2 l/n volts thd | % | single
238 | Phase 3 l/n volts thd | % | single
240 | Phase 1 current thd | % | single
242 | Phase 2 current thd | % | single
244 | Phase 3 current thd | % | single
248 | Average line to neutral volts thd | % | single
250 | Average line current thd | % | single
254 | -total system power factor (5) | Degre es | single
258 | Phase 1 current demand | Amps | single
260 | Phase 2 current demand | Amps | single
262 | Phase 3 current demand | Amps | single
264 | Maximum phase 1 current demand | Amps | single
266 | Maximum phase 2 current demand | Amps | single
268 | Maximum phase 3 current demand | Amps | single
334 | Line 1 to line 2 volts thd |   | single
336 | Line 2 to line 3 volts thd |   | single
338 | Line 3 to line 1 volts thd |   | single
340 | Average line to line volts thd |   | single
