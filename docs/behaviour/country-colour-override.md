# Behaviour: country colour override

This document describes what a player observes. The mechanism is documented in [flows/country-colour-injection.md](../flows/country-colour-injection.md).

## The observed behaviour

When the mod is enabled, 89 countries render with a different map colour from vanilla. The change is visible in three places that all read the same value:

| Surface | Appearance |
|---------|------------|
| Map fill | The territory polygon of the country |
| Country list and ledger | The swatch beside the country name |
| Diplomacy and war screens | The colour used to identify the country |

## Representative changes

| Country | Vanilla | Standardised | Character of the change |
|---------|---------|--------------|-------------------------|
| France (`FRA`) | `#1432D2` | `#000099` | Darker, deeper blue |
| Denmark (`DEN`) | `#801219` | `#C8102E` | Brighter, more saturated red |
| Austria (`AUS`) | `#D3DCF0` | `#C8102E` | From pale blue to red |
| Central Europe (`HRE`) | `#FAFAF5` | `#000000` | From near-white to black |
| Colombia (`CLM`) | `#FFEAA8` | `#012A6C` | From cream to navy |
| Cyprus (`CYP`) | `#4E4B27` | `#FFFFFF` | From olive to white |
| Georgia (`GEO`) | `#D22D2D` | `#F9F9F9` | From red to near-white |
| Japan (`JAP`) | `#C2353C` | `#FFFFFF` | From red to white |
| Persia (`PER`) | `#3C96E6` | `#B10803` | From azure to deep red |
| Rajputana (`RAJ`) | `#310D16` | `#FF6400` | From near-black to vivid orange |

The full set is in [colour-mappings.md](../colour-mappings.md).

## Where the effect is visible

The 89 mapped tags divide into three practical groups.

| Group | Count | When a player sees the colour |
|-------|-------|-------------------------------|
| Present at the 1836 start | 40 | Immediately, from the first map view |
| Formation targets only | 22 | After the country is formed |
| Neither at start nor formable | 27 | After the country is released from an existing state |

Ten tags are both present at the start and formation targets — for example `BRZ`, `CHI`, `RUS`, `SPA`, `SWE`, `MEX`, `POL`, `FRA`, `CLM`, and `USA`.

## What is preserved

The mod changes one key. Everything else a player can observe about the country is unchanged:

- tier, country type, and rank;
- primary cultures and religion;
- capital and naming rules;
- regnal numbering;
- unit colours, which are separate keys;
- flags and coats of arms;
- laws, interest groups, and starting politics.

## What does not change even when mapped

| Situation | Observed colour |
|-----------|-----------------|
| A conditional map-colour block matches | The named colour from `dynamic_country_map_colors`, for example a communist Germany's red or a republican France's blue |
| The country is a subject and the `subject_map_color` rule is `allow_subject_map_color` | The overlord's colour |
| The country is at war and the map mode highlights belligerents | The map mode's own tinting |

See [map-colour-conflicts.md](./map-colour-conflicts.md).

## Behavioural consequences of enabling the mod

| Consequence | Detail |
|-------------|--------|
| Multiplayer | Every client must run the mod, because the metadata declares synchronisation |
| Save games | Adding or removing the mod between sessions changes colours but does not alter game state, because no script or effect is introduced |
| Achievements | Mods do not disable achievements in Victoria 3, but a debug-mode session and console use are separate matters |
| Checksum | The mod alters the content checksum; a session's mod set must match to resume a multiplayer save |

## What is not overridden

Most countries keep their vanilla colours. A country left at vanilla is a correct outcome, not a defect. See [design-decisions.md](../design-decisions.md) decision D7.