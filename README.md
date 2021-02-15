# My modification of Python script for reading data from Eastron SDM630 over ModBus

All registers

| MODBUS offset | Description | Units |
| ------------- | -------------------- | --------- |
| 2 | Phase 2 line to neutral volts | Volts |
| 4 | Phase 3 line to neutral volts | Volts |
| 6 | Phase 1 current | Amps |
| 8 | Phase 2 current | Amps |
| 10 | Phase 3 current | Amps |
| 12 | Phase 1 power | Watts |
| 14 | Phase 2 power | Watts |
| 16 | Phase 3 power | Watts |
| 18 | Phase 1 volt amps | VoltAmps |
| 20 | Phase 2 volt amps | VoltAmps |
| 22 | Phase 3 volt amps | VoltAmps |
| 24 | Phase 1 volt amps reactive | VAr |
| 26 | Phase 2 volt amps reactive | VAr |
| 28 | Phase 3 volt amps reactive | VAr |
| 30 | Phase 1 power factor (1) | None |
| 32 | Phase 2 power factor (1) | None |
| 34 | Phase 3 power factor (1) | None |
| 36 | Phase 1 phase angle | Degrees |
| 38 | Phase 2 phase angle | Degrees |
| 40 | Phase 3 phase angle | Degrees |
| 42 | Average line to neutral volts | Volts |
| 46 | Average line current | Amps |
| 48 | Sum of line currents | Amps |
| 52 | Total system power | Watts |
| 56 | Total system volt amps | VA |
| 60 | Total system var | VAr |
| 62 | Total system power factor (1) | None |
| 66 | Total system phase angle | Degre es |
| 70 | Frequency of supply voltages | Hz |
| 72 | Import wh since last reset (2) | kWh / MWh |
| 74 | Export wh since last reset (2) | kWH / MWh |
| 76 | Import varh since last reset (2) | kVArh / MVArh |
| 78 | Export varh since last reset (2) | kVArh / MVArh |
| 80 | Vah since last reset (2) | kVAh / MVAh |
| 82 | Ah since last reset(3) | Ah / kAh |
| 84 | Total system power demand (4) | Watts |
| 86 | Maximum total system power | Watts |
| 100 | Total system va demand | VA |
| 102 | Maximum total system va demand | VA |
| 104 | Neutral current demand | Amps |
| 106 | Maximum neutral current demand | Amps |
| 200 | Line 1 to line 2 volts | Volts |
| 202 | Line 2 to line 3 volts | Volts |
| 204 | Line 3 to line 1 volts | Volts |
| 206 | Average line to line volts | Volts |
| 224 | Neutral current | Amps |
| 234 | Phase 1 l/n volts thd | % |
| 236 | Phase 2 l/n volts thd | % |
| 238 | Phase 3 l/n volts thd | % |
| 240 | Phase 1 current thd | % |
| 242 | Phase 2 current thd | % |
| 244 | Phase 3 current thd | % |
| 248 | Average line to neutral volts thd | % | |
| 250 | Average line current thd | % |
| 254 | -total system power factor (5) | Degrees |
| 258 | Phase 1 current demand | Amps |
| 260 | Phase 2 current demand | Amps |
| 262 | Phase 3 current demand | Amps |
| 264 | Maximum phase 1 current demand | Amps |
| 266 | Maximum phase 2 current demand | Amps |
| 268 | Maximum phase 3 current demand | Amps |
| 334 | Line 1 to line 2 volts thd |   |
| 336 | Line 2 to line 3 volts thd |   |
| 338 | Line 3 to line 1 volts thd |   |
| 340 | Average line to line volts thd |   |

