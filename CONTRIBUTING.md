[![Donate](https://img.shields.io/badge/-%E2%99%A5%20Donate-%23ff69b4)](https://hmlendea.go.ro/funding)

# Contributing to Standardised Country Colours

This document covers the guidelines and processes for contributing to this project, including how to report issues, suggest enhancements, submit code changes, and follow project standards.

## 📑 Table of Contents

- [Contributing](#contributing)
  - [Reporting Issues](#reporting-issues)
  - [Suggesting Enhancements](#suggesting-enhancements)
  - [Code Contributions](#code-contributions)
    - [Prerequisites](#prerequisites)
    - [Development Setup](#development-setup)
    - [Making Changes](#making-changes)
    - [Pull Request Guidelines](#pull-request-guidelines)
  - [Code Style](#code-style)
  - [Documentation](#documentation)
- [Code of Conduct](#code-of-conduct)
- [Security](#security)
- [Donations](#donations)
- [License](#license)
- [Getting Assistance](#getting-assistance)

## 🤝 Contributing

### Reporting Issues

- Search existing issues first.
- Use the issue templates if available.
- Provide clear reproduction steps.
- Include environment details.

### Suggesting Enhancements

- Check the existing discussions.
- Explain the use case and expected conduct.
- Consider the implementation complexity.

### Code Contributions

#### Prerequisites

- [Victoria 3](https://store.steampowered.com/app/529340/), for verifying the mod in a running game
- [Python 3](https://www.python.org/), for running the build; only the standard library is used
- A text editor that preserves the UTF-8 byte-order mark, which Victoria 3 requires for every script and localisation file

#### Development Setup

```bash
# Clone the repository
git clone https://github.com/hmlendea/vic3-standardised-country-colours.git
cd vic3-standardised-country-colours

# Install dependencies
# No dependency installation is required; the build uses only the Python 3 standard library.

# Build the mod
python3 scripts/build.py --game victoria3 --version 1.0.0
```

#### Making Changes

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature/your-feature-name`
3. Make your changes.
6. Commit with clear and descriptive messages.
7. Push to your fork.
8. Open a Pull Request.

#### Pull Request Guidelines

- Target the `master` branch.
- Keep PRs focused and atomic.
- Revise documentation if applicable.
- Include tests for any new functionality.
- Ensure the CI checks pass.

### Code Style

Follow the project's coding standards:
- Indent with tabs in the generated definitions, matching the surrounding content.
- Keep one country per block, with the three-letter tag as the block key.
- Prefer `INJECT:<tag>` over `REPLACE:<tag>` so that only the colour is changed.
- Change the build inputs — the shared palette snapshot in `src/colours.md` or the per-game configuration under `scripts/games/` — rather than the generated `standardised-country-colours/` folder.

### Documentation

- Revise relevant docs for changes.
- Follow the documentation style guide.
- Preview changes locally if possible.

## 📜 Code of Conduct

This project follows the [Code of Conduct](./CODE_OF_CONDUCT.md).

## 🔒 Security

Report security vulnerabilities per the [Security Policy](./SECURITY.md).

## 💝 Donations

This project is developed and maintained during spare time. If you find it useful, consider [donating](https://hmlendea.go.ro/funding) and giving it a star ⭐️ on GitHub!

## 📄 License

By contributing, you agree that your contributions will be licensed under the GNU General Public License v3.0.

## ❓ Getting Assistance

- Use [GitHub Issues](https://github.com/hmlendea/vic3-standardised-country-colours/issues) for questions or support.
- Check existing discussions and documentation first.
