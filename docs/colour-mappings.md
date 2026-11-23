# Colour mappings

Every shipped mapping, with the vanilla value it replaces and the country's lifecycle position. All 89 entries are in `standardised-country-colours/common/country_definitions/sc_country_colours.txt`, in the same alphabetical order by tag.

## Column reference

| Column | Meaning |
|--------|---------|
| Tag | The three-letter country key the block injects into |
| Country | The vanilla localised name, as recorded in the file comment |
| Palette entry | The palette row name, shown only when it differs from the country name |
| New colour | The injected value |
| Vanilla colour | The value the injection replaces, converted to `#RRGGBB` from whatever syntax vanilla used |
| Source | The palette attribution |
| Lifecycle | `start` = exists at the 1836 start; `formable` = a country-formation target; `release only` = neither |

Four entries change the vanilla colour syntax rather than only the value: `BRZ`, `NET`, and `SPA` replace `hsv360` blocks, and `DEN` replaces an `hsv` block, each with a plain RGB block. The comparison column shows the resulting RGB.

## Distribution

| Lifecycle | Count |
|-----------|-------|
| `start` only | 30 |
| `formable` only | 22 |
| Both | 10 |
| `release only` | 27 |

## The table

| Tag | Country | Palette entry | New colour | Vanilla colour | Source | Lifecycle |
|-----|---------|---------------|------------|----------------|--------|-----------|
| `AFG` | Afghanistan | — | `#A37939` | `#5C9498` | Crusader Kings II | formable |
| `ALB` | Albania | — | `#FF0000` | `#B5486A` | Official flag | release only |
| `ANL` | Andalusia | — | `#1F8A28` | `#F0E69B` | Crusader Kings II | release only |
| `AOT` | Aotearoa | Maori | `#CA1415` | `#2F8CBF` | Civilization VI | formable |
| `APC` | Apache | — | `#C49B6F` | `#C69E6D` | Total War: Medieval II - Kingdoms | start |
| `ARA` | Arabia | — | `#2B582E` | `#426F13` | Civilization V (Arabia) | formable |
| `ARM` | Armenia | — | `#207355` | `#803F80` | Total War: Rome | release only |
| `ARN` | Aragon | — | `#A66216` | `#A64448` | Crusader Kings II | release only |
| `AST` | Australia | — | `#156C30` | `#4D8B6A` | Civilization VI | formable |
| `ASU` | Asturias | — | `#E9BC5B` | `#68ADE6` | Crusader Kings II | release only |
| `AUS` | Austria | — | `#C8102E` | `#D3DCF0` | Official flag | start |
| `BHT` | India | — | `#128807` | `#68447C` | Civilization V | formable |
| `BOH` | Bohemia | — | `#00AB93` | `#A18B28` | Age of Empires II HD (Teal) | release only |
| `BOS` | Bosnia-Herzegovina | Bosnia | `#002395` | `#F0A782` | Official flag | release only |
| `BRZ` | Brazil | — | `#009440` | `#279C54` | Offical Flag | start, formable |
| `BUL` | Bulgaria | — | `#715865` | `#746B8C` | Crusader Kings II | release only |
| `BYE` | Belarus | — | `#CE1720` | `#ACAAAA` | Official flag | release only |
| `BYZ` | Byzantium | Byzantine Empire | `#460076` | `#9352AD` | Civilization V (Rome) | formable |
| `CAM` | Cambodia | Khmer | `#750073` | `#7FB43C` | Civilization VI | start |
| `CAN` | Canada | — | `#D52B1E` | `#71353F` | Official flag | formable |
| `CHI` | China | — | `#EE1C25` | `#FCB93D` | Official flag (PRC) | start, formable |
| `CLM` | Colombia | — | `#012A6C` | `#FFEAA8` | Civilization VI (Gran Colombia) | start, formable |
| `CRO` | Croatia | — | `#7A2E3A` | `#FF7EF2` | Crusader Kings II | start |
| `CYP` | Cyprus | — | `#FFFFFF` | `#4E4B27` | Official flag | release only |
| `DEN` | Denmark | — | `#C8102E` | `#802019` | Official flag | start |
| `EGY` | Egypt | — | `#DDB045` | `#FFCD9B` | Total War: Medieval II | start |
| `ENG` | England | — | `#6D0200` | `#B4633A` | Civilization V | formable |
| `EST` | Estonia | — | `#0072CE` | `#638999` | Official flag | release only |
| `ETH` | Ethiopia | — | `#02280F` | `#3878BF` | Civilization V | formable |
| `FIN` | Finland | — | `#FFFFFF` | `#CDD4E4` | Official flag | start |
| `FRA` | France | — | `#000099` | `#1432D2` | Official flag (Capet) | start, formable |
| `GAL` | Galicia-Lodomeria | Galicia-Volhynia | `#329682` | `#0D5182` | Crusader Kings II | formable |
| `GEO` | Georgia | — | `#F9F9F9` | `#D22D2D` | Civilization VI | formable |
| `GER` | Germany | — | `#B3B2B8` | `#93826E` | Civilization V | release only |
| `GRE` | Greece | — | `#FFFFFF` | `#7AB4D2` | Official flag | start |
| `HND` | India | — | `#128807` | `#964DF0` | Civilization V | release only |
| `HRE` | Central Europe | Holy Roman Empire | `#000000` | `#FAFAF5` | Total War: Medieval II | formable |
| `HUN` | Hungary | — | `#EA5946` | `#98555C` | Total War: Medieval II | start |
| `IDN` | Indonesia | — | `#6FD3DA` | `#008080` | Civilization V | formable |
| `IRE` | Ireland | — | `#00340A` | `#709669` | Total War: Medieval II - Kingdoms | formable |
| `IRO` | Haudenosaunee | Iroquois | `#415757` | `#57B650` | Civilization V | release only |
| `IRQ` | Iraq | — | `#2D7639` | `#7A846E` | Crusader Kings II | release only |
| `ISR` | Israel | — | `#FFFFFF` | `#96D4D6` | Israel | release only |
| `ITA` | Italy | — | `#F4E3A0` | `#7DAB54` | Crusader Kings II | formable |
| `JAP` | Japan | — | `#FFFFFF` | `#C2353C` | Civilization V | start |
| `KON` | Kongo | — | `#F7D801` | `#C7A08B` | Civilization VI | start |
| `KOR` | Korea | — | `#0047A0` | `#9D9061` | Official flag | start |
| `KUK` | Danubian State | Carpathia | `#D27323` | `#BE5A5F` | Crusader Kings II | formable |
| `LAT` | Latvia | — | `#9D2235` | `#6D1D50` | Official flag | release only |
| `LIT` | Lithuania | — | `#0C1EC8` | `#9A4574` | Total War: Medieval II - Kingdoms | release only |
| `LOM` | Lombardia | Lombardy | `#C017D9` | `#926C92` | Total War: Rome - Barbarian Invasion | release only |
| `MAL` | Mali | — | `#780001` | `#4BB31B` | Civilization VI | formable |
| `MAY` | Maya | — | `#009605` | `#62588E` | Total War: Medieval II - Kingdoms | release only |
| `MEX` | Mexico | — | `#006847` | `#388F35` | Official flag | start, formable |
| `MGL` | Mongolia | — | `#F4E7AA` | `#FFE07C` | Total War: Medieval II | release only |
| `MOL` | Moldavia | Moldova | `#B00000` | `#889D17` | Official flag (principality) | start |
| `MOR` | Morocco | — | `#910200` | `#E09271` | Civilization V | start |
| `NAV` | Navarra | — | `#967805` | `#FCE93A` | Crusader Kings II | release only |
| `NEP` | Nepal | — | `#AF3C1E` | `#89B77C` | Crusader Kings II | start |
| `NET` | Netherlands | — | `#FF9000` | `#CC5F29` | Civilization V | start |
| `NOR` | Norway | — | `#012A6C` | `#75A5BC` | Civilization VI | start |
| `PAP` | Rome | — | `#8E001C` | `#D3DCB2` | Official flag | start |
| `PAT` | Mapuche | — | `#004FCE` | `#C4190A` | Civilization VI | start |
| `PER` | Persia | — | `#B10803` | `#3C96E6` | Civilization V | start |
| `PNS` | Polynesia | — | `#D95900` | `#F48C1E` | Civilization V | formable |
| `POL` | Poland | — | `#780001` | `#C55C6A` | Civilization VI | start, formable |
| `POR` | Portugal | — | `#006035` | `#1C5294` | Official flag | start |
| `RAJ` | Rajputana | Rajastan | `#FF6400` | `#310D16` | Crusader Kings II | formable |
| `ROM` | Romania | — | `#FCD116` | `#1560B2` | Official flag | formable |
| `RUS` | Russia | — | `#EFB400` | `#2F5B12` | Civilization V | start, formable |
| `SAR` | Sardinia-Piedmont | Sardinia | `#D2A5FF` | `#7592A7` | Crusader Kings II | start |
| `SAX` | Saxony | — | `#000000` | `#9B93B4` | Total War: Medieval II | start |
| `SCA` | Scandinavia | — | `#3E7ABD` | `#3E7ABD` | Crusader Kings II | formable |
| `SCO` | Scotland | — | `#00105E` | `#C7AF0C` | Total War: Medieval II | release only |
| `SER` | Serbia | — | `#FFB37F` | `#A64839` | eRepublik | start |
| `SIA` | Siam | — | `#F5E637` | `#5889AC` | Civilization V | start |
| `SIC` | Two Sicilies | Sicily | `#464646` | `#49984C` | Total War: Medieval II | start |
| `SPA` | Spain | — | `#FABD00` | `#D48806` | Official flag | start, formable |
| `SWE` | Sweden | — | `#005293` | `#5782C7` | Official flag | start, formable |
| `SYR` | Syria | — | `#FFF4AE` | `#F1F5F0` | Civilization V (Assyria) | release only |
| `TRH` | Turkestan | — | `#CC9615` | `#D50027` | Crusader Kings II | formable |
| `TRS` | Transylvania | — | `#1B4B8B` | `#D3CFAD` | Official flag | start |
| `TUR` | Turkey | — | `#237806` | `#AACEA2` | Total War: Medieval II | start |
| `UKR` | Ukraine | — | `#0057B7` | `#3E5AF0` | Official flag | release only |
| `USA` | America | United States | `#1F3378` | `#425EC1` | Civilization V | start, formable |
| `VEN` | Venice | — | `#790303` | `#B40C01` | Total War: Medieval II | release only |
| `WAL` | Wallachia | — | `#FCD116` | `#A17E80` | Official flag | start |
| `WLS` | Wales | — | `#2BA224` | `#797E94` | Total War: Medieval II - Kingdoms | release only |
| `ZUL` | Zulu | — | `#783D02` | `#CCBAC9` | Civilization VI | start |
## Notable entries

| Tag | Note |
|-----|------|
| `SCA` | The only mapping whose value equals vanilla exactly (`#3E7ABD`). It is shipped so the palette provenance is recorded; it changes nothing on the map. |
| `APC` | Within three units of vanilla per component (`#C49B6F` against `#C69E6D`); visually near-identical. |
| `HRE` | The largest single change: `#FAFAF5` to `#000000`, a near-white replaced by pure black. |
| `PAP` | Vanilla is a pale green-white (`#D3DCB2`); the standardised value is a deep red (`#8E001C`). |
| `CYP`, `FIN`, `GRE`, `ISR`, `JAP` | Mapped to pure or near-pure white, which is legible only against contrasting neighbours. |
| `SAX` | Mapped to pure black, which is legible only against contrasting neighbours. |
| `BHT`, `HND` | Two Indian tags sharing the palette's single India entry. |
| `ROM`, `WAL` | Romania and Wallachia sharing the palette's single Romania entry. |

## Palette entries with no matching tag

These appear in the palette but cannot be shipped, because no Victoria 3 definition carries that identity:

African Union, Alania, Alemannia, Anatolia, Antiochia, Aquitaine, Aztec Empire, Babylon, Berberia, Burgundy, Carinthia, Carthage, Castille, Cree, Cumania, Dacia, Daylam, European Union, Frisia, Gaul, Gondwana, Gothia, Hausaland, Hunnic Empire, Inca, Jerusalem, Kalmar Union, Khazaria, Kosovo, Lotharingia, Macedonia, Mauretania, Milan, Moors, Moravia, Normandy, Novgorod, Nubia, Numidia, Ostrogothia, Outremer, Parthia, Pontus, Romagna, Roxolania, Sarmatia, Sassania, Scythia, Seleucia, Shoshone, Slavia, Songhai, Sumeria, Tarascans, Taurica, Teutonic State, Thrace, Timurid Empire, Tlaxcala, Vandalia, Vatican, Vietnam, Volga Bulgaria, Wendish Empire.

`Babylon` is a special case: the palette lists it and the game has a localisation key for it, but no country definition block exists, so there is nothing to inject into.

## Related documents

- [components/mod-content.md](./components/mod-content.md) — the file format.
- [flows/colour-authoring.md](./flows/colour-authoring.md) — adding a mapping.
- [behaviour/country-colour-override.md](./behaviour/country-colour-override.md) — what a player sees.