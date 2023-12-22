<p  align="center">
  <strong> gitcommit enhanced</strong>
  <br>
  <code>A tool for writing conventional commits in an easy way.</code>
</p>

# Install

To install

```
pip install gitcommit-enhanced
```

To use, run the following command from within a git repository

```
gitcommit
```

# Overview

The purpose of this utility is to expedite the process of committing with a conventional message format in a user friendly way. This tool is not templated, because it sticks rigidly to the [Conventional Commit standard](https://www.conventionalcommits.org), and thus not designed to be 'altered' on a case by case basis.

Commit messages produced follow the general template:

```
<type>[(optional scope)]: <description>

[BREAKING CHANGE: ][optional body / required if breaking change]

[optional footer]
```

Additional rules implemeted:

1. Subject line (i.e. top) should be no more than 61 characters.
2. Every other line should be no more than 79 characters.
3. Wrapping is allowed in the body and footer, NOT in the subject.

## Acknowledgements

This repo is a fork of https://github.com/nebbles/gitcommit which not under active development . I have modified it as per my own requirements and have made some changes to the existing code and its structure while keeping the core entact.

## License

This work is published under [GNU GPLv3](./LICENSE).
