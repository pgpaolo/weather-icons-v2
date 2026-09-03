# Branching model

This repository uses a simple two-branch model:

- `main` — stable published version of Weather Icons v2.
- `develop` — integration branch for work in progress, experiments, new icons and metadata changes before promotion to `main`.

Recommended flow:

1. create a feature branch from `develop`;
2. commit icon, mapping or documentation changes there;
3. open a pull request into `develop`;
4. validate the complete set;
5. promote tested changes from `develop` to `main` through a pull request.

Direct commits to `main` should be kept to repository maintenance and controlled publishing automation.
