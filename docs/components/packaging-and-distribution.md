# Component: packaging and distribution

## Release workflow

`.github/workflows/github-release.yml` publishes the GitHub release asset. It is one of three release workflows; `.github/workflows/steam-workshop-release.yml` publishes the Steam Workshop item and `.github/workflows/nexus-mods-release.yml` publishes the Nexus Mods file.

### Triggers

| Trigger | Behaviour |
|---------|-----------|
| `release: types: [published]` | Runs after a maintainer publishes a release, using its tag |
| `workflow_dispatch` with a required `tag` input | Runs on demand against a nominated tag |

The published-release trigger is deliberate: it decouples packaging from pushing a tag, so a release can be prepared, inspected, and then published.

### Steps

| Step | Action | Effect |
|------|--------|--------|
| Check out the repository | `actions/checkout@v7` with `ref: ${{ env.VERSION }}` | Works on the exact tagged tree |
| Extract the version | Shell | Strips the leading `v` from the tag and exports it |
| Build the mod | `python3 scripts/build.py --version "${{ steps.version.outputs.version }}" --game "${GAME}"` | Renders the mod folder at the tag's version |
| Build the release archive | `zip -r` | Produces `standardised-country-colours_<group>_<version>.zip` containing the mod folder |
| Publish the release asset | `softprops/action-gh-release@v2` | Attaches the archive to the release |

The workflow defines three jobs, `hoi4`, `victoria3`, and `imperator`, each with its own `GAME` and `GROUP` environment variables. All jobs run the same steps in parallel.

`VERSION` resolves to `${{ inputs.tag || github.event.release.tag_name }}` so a manual run publishes the same assets a released run would.

### Permissions

`contents: write`, required to attach the assets. No other scope is requested.

### What is not done

- No checksum is computed or attached.
- The release body is left as the maintainer wrote it.
- The built folders remain under `out/<game>/`; nothing is staged at the repository root.

## Steam Workshop workflow

`.github/workflows/steam-workshop-release.yml` uploads each game edition's mod folder to its matching Workshop item.

### Triggers

| Trigger | Behaviour |
|---------|-----------|
| `push: tags: ['v*.*.*']` | Runs on every version-tag push, using `github.ref_name` |
| `workflow_dispatch` with a required `tag` input | Runs on demand against a nominated tag |

### Steps

| Step | Action | Effect |
|------|--------|--------|
| Check out the repository | `actions/checkout@v7` with `ref: ${{ env.VERSION }}` | Works on the exact tagged tree |
| Build the mod | `python3 scripts/build.py --game <game> --version "${VERSION#v}"` | Renders the mod folder at the tag's version |
| Upload to Steam Workshop | `hmlendea/steam-workshop-update@latest` | Publishes `out/<group>/standardised-country-colours/` to the matching Workshop item, adds a changenote linking to the GitHub release |

The workflow defines three jobs, `hoi4`, `victoria3`, and `imperator`. Hearts of Iron IV publishes to Workshop item `3845820843` for Steam app `394360`; Victoria 3 publishes to Workshop item `3844790373` for Steam app `529340`; Imperator: Rome publishes to Workshop item `3845414842` for Steam app `859580`.

Each upload step supplies `icon: "out/<group>/standardised-country-colours/thumbnail.png"`, so the descriptor's `previewfile` is the mod's Workshop artwork. The action downscales the image to a 512-pixel limit before upload, so the `thumbnail.png` in the build output may be larger than the Workshop dimensions require.

`VERSION` resolves to `${{ inputs.tag || github.ref_name }}` so a manual run publishes the requested tag.

### Secrets

The upload reads `STEAM_USERNAME`, `STEAM_PASSWORD`, and `STEAM_2FA_SEED` from repository secrets. The workflow only references the `${{secrets...}}` expressions; no value is stored in the repository.

### What is not done

- The archive is not retained; only the extracted folder is uploaded.
- No content transformation is applied; the uploaded folder is the freshly built tree.
- Paradox Mods is not targeted.

## Nexus Mods workflow

`.github/workflows/nexus-mods-release.yml` uploads the mod archive to Nexus Mods.

### Triggers

| Trigger | Behaviour |
|---------|-----------|
| `push: tags: ['v*.*.*']` | Runs on every version-tag push, using `github.ref_name` |
| `workflow_dispatch` with a required `tag` input | Runs on demand against a nominated tag |

### Steps

| Step | Action | Effect |
|------|--------|--------|
| Check out the repository | `actions/checkout@v7` with `ref: ${{ env.VERSION }}` | Works on the exact tagged tree |
| Build the mod | `python3 scripts/build.py --game <game> --version "${VERSION#v}"` | Renders the mod folder at the tag's version |
| Build the release archive | `zip -r` | Produces `release-<game>.zip` containing the mod folder |
| Upload to Nexus Mods | `Nexus-Mods/upload-action@v1.0.0-beta.11` | Publishes to the matching Nexus Mods file, sets the tag as the version, archives the previous version |

The workflow defines three jobs, `hoi4`, `imperator`, and `victoria3`. Hearts of Iron IV publishes to file `8459265`; Imperator: Rome publishes to file `8454045`; Victoria 3 publishes to file `8446233`.

`VERSION` resolves to `${{ inputs.tag || github.ref_name }}` so a manual run publishes the requested tag.

### Secrets

The upload reads `NEXUSMODS_API_KEY` from repository secrets. The workflow only references the `${{ secrets... }}` expression; no value is stored in the repository.

### What is not done

- The archive is published as a single main-category file; no optional or miscellaneous files are managed.
- No checksum or signature is attached.
- Steam Workshop and Paradox Mods are not targeted.

## The published artefact

```text
standardised-country-colours_<version>.zip
└── standardised-country-colours/
    ├── .metadata/
    │   ├── metadata.json
    │   └── thumbnail.png
    ├── common/
    │   └── country_definitions/
    │       └── sc_country_colours.txt
    └── thumbnail.png
```

The Victoria 3 archive nests the `.metadata/` layout shown above; the Imperator: Rome archive holds `descriptor.mod`, a sibling `.mod` file, and the `setup/countries/` tree instead. In both cases the archive's top-level entry is the mod folder itself, so extracting it into the mod directory produces the layout the launcher expects. Extracting its contents directly into the mod directory would scatter the content folders at the wrong level.

## Manual distribution

A user may run `scripts/build.py` and copy its `out/<game>/standardised-country-colours/` output into the mod directory. That folder is byte-identical to any release archive's contents.

## Workshop page description

`description/steam-workshop.bbcode` holds the BBCode body of the item page, kept in version control so a revision is reviewed and tracked. It is a publication artefact, not part of the mod folder, and neither release workflow reads or archives it. An upload happens only when a maintainer pastes the file contents into the Workshop item.

## Version policy

`metadata.json.version` is supplied to `scripts/build.py` through its `--version` argument, and the Git tag is an independent string; the workflow derives the archive name from the tag, not from the metadata. Keep them in step to avoid a launcher label that contradicts the downloaded archive name.

## Related documents

- [build-and-deployment.md](../build-and-deployment.md) — operator procedure.
- [integrations.md](../integrations.md) — GitHub and Steam as external systems.
- [invariants.md](../invariants.md) — release invariants R1–R5.