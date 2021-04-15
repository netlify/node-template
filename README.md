# node-template

This is a GitHub [cookiecutter](https://cookiecutter.readthedocs.io/en/1.7.2/installation.html) template for Netlify Node.js repositories.

Please feel free to use this template when starting a new Node.js repository.

## Setup

- `cookiecutter gh:netlify/node-template`
- Create a GitHub repository and push the generated local repo

### Release please setup

We use [release please](https://github.com/google-github-actions/release-please-action) to automate release publishing.
For the `release-please.yml` GitHub workflow to work you'll need to add 3 secrets to your repo:

1. `TOKENS_PRIVATE_KEY` - a GitHub app private key
2. `TOKENS_APP_ID` - a GitHub app id
3. `NPM_TOKEN` - an `npm` automation token

The GitHub app is used to generate GitHub tokens to and should be installed on the repo and have `Contents` and `Pull requests` read & write permissions.
You can create a new GitHub app by visiting `https://github.com/organizations/<org>/settings/apps/new`

> It's useful to add those secrets at an organization level instead of at the repo level

## Contributors

Please see [CONTRIBUTING.md](./CONTRIBUTING.md) for instructions on how to set up and work on this repository. Thanks
for contributing!
