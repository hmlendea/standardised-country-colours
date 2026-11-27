# Colour mappings

Every shipped mapping, with the vanilla value it replaces and the country's lifecycle position. All 135 entries are rendered into `standardised-country-colours/common/country_definitions/sc_country_colours.txt` (inside the built folder, `out/vic3/`), in the same alphabetical order by tag.

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

Eight entries change the vanilla colour syntax rather than only the value: `BAH`, `BRZ`, `CAS`, `CEY`, `GRN`, `NET`, and `SPA` replace `hsv360` blocks, and `DEN` replaces an `hsv` block, each with a plain RGB block. The comparison column shows the resulting RGB.

## Distribution

| Lifecycle | Count |
|-----------|-------|
| `start` only | 55 |
| `formable` only | 27 |
| Both | 10 |
| `release only` | 43 |

## The table

| Tag | Country | Palette entry | New colour | Vanilla colour | Source | Lifecycle |
|-----|---------|---------------|------------|----------------|--------|-----------|
| `ABK` | Abkhazia | — | `#00993E` | `#5CBC49` | Official flag | start |
| `AFG` | Afghanistan | — | `#A37939` | `#5C9498` | Crusader Kings 2 | formable |
| `ALB` | Albania | — | `#AC2E26` | `#B5486A` | eRepublik (Old UI) | release only |
| `ALD` | Algeria | — | `#006633` | `#DCCA60` | Official flag | formable |
| `ALI` | Altai | — | `#FFFFFF` | `#4A79C6` | Official flag | release only |
| `ALK` | Alaska | — | `#0F204B` | `#F9FBFF` | Official flag | start |
| `ANL` | Andalusia | — | `#1F8A28` | `#F0E69B` | Crusader Kings 2 | release only |
| `AOT` | Aotearoa | Maori | `#CA1415` | `#2F8CBF` | Civilization 6 | formable |
| `APC` | Apache | — | `#C49B6F` | `#C69E6D` | Total War: Medieval 2 - Kingdoms | start |
| `ARA` | Arabia | — | `#2B582E` | `#426F13` | Civilization 5 (Arabia) | formable |
| `ARG` | Argentina | — | `#74ACDF` | `#6566A3` | Official flag | start |
| `ARM` | Armenia | — | `#207355` | `#803F80` | Total War: Rome | release only |
| `ARN` | Aragon | — | `#A66216` | `#A64448` | Crusader Kings 2 | release only |
| `AST` | Australia | — | `#156C30` | `#4D8B6A` | Civilization 6 | formable |
| `ASU` | Asturias | — | `#0066FF` | `#68ADE6` | Official flag | release only |
| `AUS` | Austria | — | `#C8102E` | `#D3DCF0` | Official flag | start |
| `AZB` | Azerbaijan | — | `#509E2F` | `#AC3820` | Official flag | release only |
| `BAD` | Baden | — | `#E2001A` | `#76E5D7` | Official flag | start |
| `BAH` | Bahamas | — | `#00778B` | `#00778C` | Official flag | release only |
| `BAV` | Bavaria | — | `#0098D4` | `#79AFEB` | Official flag | start |
| `BEL` | Belgium | — | `#7D9A40` | `#EBC87F` | eRepublik (Old UI) | start |
| `BEN` | Benin | — | `#008751` | `#6EAD81` | Official flag | start |
| `BHT` | India | — | `#128807` | `#68447C` | Civilization 5 | formable |
| `BHU` | Bhutan | — | `#FFCD00` | `#5DB44C` | Official flag | start |
| `BOH` | Bohemia | Czechia | `#00AB93` | `#A18B28` | Age of Empires II HD (Teal) | release only |
| `BOL` | Bolivia | — | `#F0E53C` | `#DBB6B6` | Official flag | start |
| `BOS` | Bosnia-Herzegovina | Bosnia | `#002395` | `#F0A782` | Official flag | release only |
| `BRD` | Burundi | — | `#C8102E` | `#15BF10` | Official flag | start |
| `BRI` | Brittany | — | `#FFFFFF` | `#D7C3E1` | Official flag | release only |
| `BRU` | Brunei | — | `#F7E017` | `#2959AE` | Official flag | start |
| `BRY` | Buryatia | — | `#0039A6` | `#323278` | Official flag | release only |
| `BRZ` | Brazil | — | `#009440` | `#279C54` | Official flag | start, formable |
| `BUG` | Buganda | — | `#003CC8` | `#1515E3` | Official flag | start |
| `BUL` | Bulgaria | — | `#715865` | `#746B8C` | Crusader Kings 2 | release only |
| `BUR` | Burma | Myanmar | `#34B233` | `#6DA87F` | Official Flag | start |
| `BYE` | Belarus | — | `#CE1720` | `#ACAAAA` | Official flag | release only |
| `BYZ` | Byzantium | Eastern Roman Empire | `#460076` | `#9352AD` | Civilization 5 (Rome) | formable |
| `CAL` | California | — | `#FFFFFF` | `#90B56A` | Official flag | release only |
| `CAM` | Cambodia | — | `#E00025` | `#7FB43C` | Official flag | start |
| `CAN` | Canada | — | `#D52B1E` | `#71353F` | Official flag | formable |
| `CAS` | Castile | Castille | `#F3D117` | `#C7B342` | Crusader Kings 2 | release only |
| `CEY` | Sri Lanka | — | `#8D153A` | `#9C2F2F` | Official flag | release only |
| `CHC` | Chechnya | — | `#227733` | `#233430` | Official flag | start |
| `CHI` | China | — | `#EE1C25` | `#FCB93D` | Official flag (PRC) | start, formable |
| `CHL` | Chile | — | `#ECFFAE` | `#EC9F59` | eRepublik (Old UI) | start |
| `CIR` | Circassia | Adygea | `#296912` | `#4B6037` | Official flag | start |
| `CLM` | Colombia | — | `#012A6C` | `#FFEAA8` | Civilization 6 (Gran Colombia) | start, formable |
| `COR` | Corsica | — | `#000000` | `#44F2EC` | Official flag | release only |
| `CRI` | Crimea | — | `#00A3DD` | `#C8CA55` | Official flag (Crimean Tatar People) | release only |
| `CRO` | Croatia | — | `#867ACC` | `#FF7EF2` | eRepublik (Old UI) | start |
| `CSC` | Cascadia | — | `#275F2F` | `#699849` | Official flag | release only |
| `CYP` | Cyprus | — | `#FFFFFF` | `#4E4B27` | Official flag | release only |
| `DEN` | Denmark | — | `#C8102E` | `#802019` | Official flag | start |
| `ECU` | Ecuador | — | `#FFDD00` | `#2B8DAC` | Official flag | start |
| `EGY` | Egypt | — | `#FFFF2B` | `#FFCD9B` | Civilization 4 | start |
| `ELS` | El Salvador | — | `#0047AB` | `#002F5E` | Official flag | release only |
| `ENG` | England | — | `#6D0200` | `#B4633A` | Civilization 5 | formable |
| `EST` | Estonia | — | `#0072CE` | `#638999` | Official flag | release only |
| `ETH` | Ethiopia | — | `#02280F` | `#3878BF` | Civilization 5 | formable |
| `FIN` | Finland | — | `#FFFFFF` | `#CDD4E4` | Official flag | start |
| `FLA` | Flanders | — | `#FEEA28` | `#2B8DAC` | Official flag | release only |
| `FRA` | France | — | `#000099` | `#1432D2` | Official flag (Capet) | start, formable |
| `GAL` | Galicia-Lodomeria | Galicia-Volhynia | `#329682` | `#0D5182` | Crusader Kings 2 | formable |
| `GEO` | Georgia | — | `#F9F9F9` | `#D22D2D` | Civilization 6 | formable |
| `GER` | Germany | — | `#B3B2B8` | `#93826E` | Civilization 5 | formable |
| `GRE` | Greece | — | `#FFFFFF` | `#7AB4D2` | Official flag | start |
| `GRN` | Greenland | — | `#FFFFFF` | `#1B852C` | Official flag | release only |
| `HND` | India | — | `#128807` | `#964DF0` | Civilization 5 | release only |
| `HRE` | Central Europe | Holy Roman Empire | `#000000` | `#FAFAF5` | Total War: Medieval 2 | formable |
| `HUN` | Hungary | — | `#EA5946` | `#98555C` | Total War: Medieval 2 | start |
| `IDN` | Indonesia | — | `#6FD3DA` | `#008080` | Civilization 5 | formable |
| `IRE` | Ireland | — | `#00340A` | `#709669` | Total War: Medieval 2 - Kingdoms | formable |
| `IRO` | Haudenosaunee | Iroquois | `#415757` | `#57B650` | Civilization 5 | release only |
| `IRQ` | Iraq | — | `#2D7639` | `#7A846E` | Crusader Kings 2 | release only |
| `ISR` | Israel | — | `#FFFFFF` | `#96D4D6` | Israel | release only |
| `ITA` | Italy | — | `#587D2D` | `#7DAB54` | eRepublik (Old UI) | formable |
| `JAP` | Japan | — | `#FFFFFF` | `#C2353C` | Civilization 5 | start |
| `KAZ` | Kazakhstan | — | `#00ABC2` | `#6E96BE` | Official flag | formable |
| `KON` | Kongo | — | `#F7D801` | `#C7A08B` | Civilization 6 | start |
| `KOR` | Korea | South Korea | `#0047A0` | `#9D9061` | Official flag | start |
| `KUK` | Danubian State | Carpathia | `#D27323` | `#BE5A5F` | Crusader Kings 2 | formable |
| `KUR` | Kurdistan | — | `#278E43` | `#C0F547` | Official flag (Kingdom of Kurdistan) | release only |
| `LAT` | Latvia | — | `#9D2235` | `#6D1D50` | Official flag | release only |
| `LIT` | Lithuania | — | `#0C1EC8` | `#9A4574` | Total War: Medieval 2 - Kingdoms | release only |
| `LOM` | Lombardia | Lombardy | `#C017D9` | `#926C92` | Total War: Rome - Barbarian Invasion | release only |
| `LUX` | Luxembourg | — | `#00A3E0` | `#358C49` | Official flag | start |
| `MAD` | Madagascar | — | `#F9423A` | `#759678` | Official flag | start |
| `MAL` | Mali | — | `#780001` | `#4BB31B` | Civilization 6 | formable |
| `MAY` | Maya | — | `#009605` | `#62588E` | Total War: Medieval 2 - Kingdoms | release only |
| `MEX` | Mexico | — | `#006847` | `#388F35` | Official flag | start, formable |
| `MGB` | Maghreb | — | `#FE7800` | `#D13F2C` | Total War: Medieval 2 (Moors) | formable |
| `MGL` | Mongolia | — | `#F4E7AA` | `#FFE07C` | Total War: Medieval 2 | release only |
| `MOL` | Moldavia | Moldova | `#B00000` | `#889D17` | Official flag (principality) | start |
| `MON` | Montenegro | — | `#CAA030` | `#276C8C` | eRepublik (Old UI) | start |
| `MOR` | Morocco | — | `#910200` | `#E09271` | Civilization 5 | start |
| `NAV` | Navarra | — | `#967805` | `#FCE93A` | Crusader Kings 2 | release only |
| `NEP` | Nepal | — | `#E52320` | `#89B77C` | Official flag (1856-1930) | start |
| `NET` | Netherlands | — | `#FF9000` | `#CC5F29` | Civilization 5 | start |
| `NOR` | Norway | — | `#80241A` | `#75A5BC` | Total War: Medieval 2 - Kingdoms | start, formable |
| `NZL` | New Zealand | — | `#012169` | `#5AFA7F` | Official flag | release only |
| `PAP` | Rome | — | `#8E001C` | `#D3DCB2` | Official flag | start |
| `PAT` | Mapuche | — | `#004FCE` | `#C4190A` | Civilization 6 | start |
| `PER` | Persia | — | `#12CCF5` | `#3C96E6` | Civilization 4 | start |
| `PEU` | Peru | — | `#D91023` | `#7C8CA2` | Official flag | formable |
| `PNS` | Polynesia | — | `#D95900` | `#F48C1E` | Civilization 5 | formable |
| `POL` | Poland | — | `#780001` | `#C55C6A` | Civilization 6 | start, formable |
| `POR` | Portugal | — | `#006035` | `#1C5294` | Official flag | start |
| `PRG` | Paraguay | — | `#241265` | `#B12C1D` | eRepublik (Old UI) | start |
| `RAJ` | Rajputana | Rajastan | `#FF6400` | `#310D16` | Crusader Kings 2 | formable |
| `ROM` | Romania | — | `#FCD116` | `#1560B2` | Official flag | formable |
| `RUS` | Russia | — | `#EFB400` | `#2F5B12` | Civilization 5 | start, formable |
| `SAF` | South Africa | — | `#994D99` | `#B49E7F` | eRepublik (Old UI) | start |
| `SAR` | Sardinia-Piedmont | Sardinia | `#D2A5FF` | `#7592A7` | Crusader Kings 2 | start |
| `SAX` | Saxony | — | `#000000` | `#9B93B4` | Total War: Medieval 2 | start |
| `SCA` | Scandinavia | — | `#3E7ABD` | `#3E7ABD` | Crusader Kings 2 | formable |
| `SCO` | Scotland | — | `#00105E` | `#C7AF0C` | Total War: Medieval 2 | release only |
| `SER` | Serbia | — | `#C6363C` | `#A64839` | Official flag | start |
| `SIA` | Siam | — | `#F5E637` | `#5889AC` | Civilization 5 | start |
| `SIC` | Two Sicilies | Sicily | `#464646` | `#49984C` | Total War: Medieval 2 | start |
| `SLO` | Slovenia | — | `#7DB1C6` | `#415B7E` | eRepublik (Old UI) | release only |
| `SPA` | Spain | — | `#FABD00` | `#D48806` | Official flag | start, formable |
| `SWE` | Sweden | — | `#005293` | `#5782C7` | Official flag | start, formable |
| `SWI` | Switzerland | — | `#DA291C` | `#A52D26` | Official flag | start |
| `SWZ` | Swaziland | Eswatini | `#B10C0C` | `#FFD900` | Official flag | start |
| `SYR` | Syria | — | `#FFF4AE` | `#F1F5F0` | Civilization 5 (Assyria) | release only |
| `TRH` | Turkestan | — | `#CC9615` | `#D50027` | Crusader Kings 2 | formable |
| `TRS` | Transylvania | — | `#1B4B8B` | `#D3CFAD` | Official flag | start |
| `TUR` | Turkey | — | `#237806` | `#AACEA2` | Total War: Medieval 2 | start |
| `UKR` | Ukraine | — | `#0057B7` | `#3E5AF0` | Official flag | release only |
| `USA` | America | United States | `#1F3378` | `#425EC1` | Civilization 5 | start, formable |
| `VEN` | Venice | — | `#790303` | `#B40C01` | Total War: Medieval 2 | release only |
| `VNZ` | Venezuela | — | `#CB7BD2` | `#FFB08C` | eRepublik (Old UI) | start |
| `WAL` | Wallachia | Romania | `#FCD116` | `#A17E80` | Official flag | start |
| `WLS` | Wales | — | `#2BA224` | `#797E94` | Total War: Medieval 2 - Kingdoms | release only |
| `ZUL` | Zulu | — | `#783D02` | `#CCBAC9` | Civilization 6 | start |

## Notable entries

| Tag | Note |
|-----|------|
| `SCA` | The only mapping whose value equals vanilla exactly (`#3E7ABD`). It is shipped so the palette provenance is recorded; it changes nothing on the map. |
| `APC` | Within three units of vanilla per component (`#C49B6F` against `#C69E6D`); visually near-identical. |
| `BAH` | Differs from vanilla by one unit in the blue component (`#00778B` against `#00778C`); visually identical. |
| `CLM` | The largest single change by component distance: `#FFEAA8` to `#012A6C`, cream replaced by navy. |
| `HRE` | A near-white replaced by pure black: `#FAFAF5` to `#000000`. |
| `PAP` | Vanilla is a pale green-white (`#D3DCB2`); the standardised value is a deep red (`#8E001C`). |
| `BOS` | Vanilla is a pale peach (`#F0A782`); the standardised value is a deep blue (`#002395`). |
| `CYP`, `FIN`, `GRE`, `ISR`, `JAP`, `ALI`, `CAL` | Mapped to pure or near-pure white, which is legible only against contrasting neighbours. |
| `COR`, `SAX` | Mapped to pure black, which is legible only against contrasting neighbours. |
| `BHT`, `HND` | Two Indian tags sharing the palette's single India entry. |
| `ROM`, `WAL` | Romania and Wallachia sharing the palette's single Romania entry. |
| `ABK`, `ALD`, `ALI`, `ALK`, `BAD`, `BAH`, `BEL`, `BEN`, `BHU`, `BRD`, `BRU`, `BRY`, `BUG`, `BUR`, `CAL`, `CEY`, `CHC`, `CHL`, `CIR`, `COR`, `CRI`, `CSC`, `ECU`, `KAZ`, `MON`, `PEU`, `PRG`, `SAF`, `SLO`, `VNZ` | Added when the mod was synchronised to the palette's Principal table; each was resolved from a palette entry that names it directly. |
| `ALB`, `ASU`, `CRO`, `ITA`, `NEP` | Realigned to their palette Principal values; the previous values came from the palette's Alternative table. |
| `ELS`, `FLA`, `GRN`, `SWZ` | Added when the palette gained their Principal rows; each was resolved to the tag that carries the same identity. `SWZ` (vanilla "Swaziland") is the only one present at the start; the other three are release-only. |
| `SWZ` | The vanilla localised name is "Swaziland", so the comment appends the palette entry: `Swaziland (palette: Eswatini)`. |

## Palette entries with no matching tag

These appear in the palette's Principal table but cannot be shipped, because no Victoria 3 definition carries that identity:

Aargau, Achterhoek, African Union, Aland, Alania, Alemannia, American Samoa, Amsterdam, Anatolia, Anchorage, Angola, Antarctica, Antiochia, Aquitaine, Aruba, Azores, Aztec Empire, Babylon, Bangladesh, Barbados, Bashkorotostan, Basque Country, Belize, Berberia, Berlin, Bessarabia, Bharatpur, Botswana, Buckinghamshire, Bucovina, Burgundy, Burkina Faso, Caithness, Cape Verde, Carinthia, Carthage, Ceuta, Chelyabinsk, Chicago, Christmas Island, Colorado, Confederate States, Connacht, Cook Islands, Courland, Cree, Cumania, Curaçao, DR Congo, Dacia, Daylam, Djibouti, Dobrogea, Dominica, Dominican Republic, Durban, Epirus, Espirito Santo, European Union, Faroe Islands, French Polynesia, Friesland, Frisia, Gambia, Gaul, Geneva, Gibraltar, Glarus, Gondwana, Groningen, Hausaland, Hunnic Empire, Inca, Ingushetia, Iskolat, Jerusalem, Kalmar Union, Khazaria, Khmer, Kosovo, Liechtenstein, Lotharingia, Macedonia, Mauretania, Milan, Monaco, Moravia, Naples, Normandy, North Korea, Novgorod, Nubia, Numidia, Ostergotaland, Outremer, Palau, Parthia, Pontus, Qatar, Romagna, Roxolania, Sarmatia, Sassania, Saudi Arabia, Saurashtra, Scythia, Seleucia, Senegal, Shizuoka, Shoshone, Singapore, Slavia, Smolensk, Songhai, Sosnowiec, South Dakota, St Gallen, Stavropol, Sumeria, Suriname, Taiwan, Tanzania, Tarascans, Taurica, Terengganu, Teutonia, Thailand, Thrace, Thurgau, Timor Leste, Timurid Empire, Tlaxcala, Tocantins, Togo, Tokelau, Toronto, Transnistria, Trebizond, Trinidad and Tobago, Ulyanovsk, Vandalia, Vastergotland, Vatican, Veraguas, Vietnam, Volga Bulgaria, Volgograd, Warwickshire, Wendish Empire, Zurich.

Six palette rows carry a matching Victoria 3 tag but no mapping, so they are not shipped: `Savoie` (`SAV`, localised "Savoy"), `Sierra Leone` (`SIL`), `Turkmenistan` (`TRC`), `Tuscany` (`TUS`), `Uzbekistan` (`UZB`) and `Wallonia` (`WLL`).

Two palette rows name a country the game also defines under a second tag: `Georgia` resolves to both `GEO` (Caucasus) and `GRG` (the American state), and `Syria`, whose palette alias is `Assyria`, resolves to both `SYR` and `ASS`. Both pairs were resolved to the country the palette names — `GEO` and `SYR` — because the palette describes the historical states, not the game's regional tags.

`Babylon` and `Gambia` are special cases: the palette lists them and the game has a localisation key for each, but no country definition block exists, so there is nothing to inject into.

## Related documents

- [components/mod-content.md](./components/mod-content.md) — the file format.
- [flows/colour-authoring.md](./flows/colour-authoring.md) — adding a mapping.
- [behaviour/country-colour-override.md](./behaviour/country-colour-override.md) — what a player sees.