# Branching model

The repository uses a stable-main plus short-lived feature-branch model.

- `main` — stable published version.
- `feature/*` — temporary review branches created directly from `main` for artwork, mapping, documentation or tooling changes.

Current candidate branch:

```text
feature/weather-icons-v3-redesign
```

Recommended flow:

1. start the feature branch from the current `main`;
2. make the artwork and documentation changes in that branch;
3. run the full metadata, mapping and PNG validation;
4. perform a visual review;
5. open a pull request from the feature branch to `main`;
6. merge only after the candidate passes review;
7. delete the feature branch after publication.

There is no permanent `develop` integration branch in the simplified model. Direct commits to `main` should be limited to controlled repository maintenance or approved publishing operations.
