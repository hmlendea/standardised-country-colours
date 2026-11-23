# Component: packaging and distribution

## Release workflow

`.github/workflows/github-release.yml` is the only automation in the repository.

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
| Build the release archive | `zip -r` | Produces `standardised-country-colours_<version>.zip` containing the mod folder |
| Publish the release asset | `softprops/action-gh-release@v2` | Attaches the archive to the release |

`VERSION` resolves to `${{ inputs.tag || github.event.release.tag_name }}` so a manual run publishes the same asset a released run would.

### Permissions

`contents: write`, required to attach the asset. No other scope is requested.

### What is not done

- No checksum is computed or attached.
- The release body is left as the maintainer wrote it.
- No staging directory is created and no files are copied, because the archive is built from the checked-out tree.
- No Steam Workshop, Paradox Mods, or Nexus Mods upload exists.

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

The archive's top-level entry is the mod folder itself, so extracting it into the mod directory produces the layout the launcher expects. Extracting its contents directly into the mod directory would scatter `common/` and `.metadata/` at the wrong level.

## Manual distribution

A user may clone the repository and copy `standardised-country-colours/` into the mod directory instead. Both routes yield the same tree.

## Version policy

`metadata.json.version` and the Git tag are independent strings; the workflow derives the archive name from the tag, not from the metadata. Keep them in step to avoid a launcher label that contradicts the downloaded archive name.

## Related documents

- [build-and-deployment.md](../build-and-deployment.md) — operator procedure.
- [integrations.md](../integrations.md) — GitHub and Steam as external systems.
- [invariants.md](../invariants.md) — release invariants R1–R4.