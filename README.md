# text-tools

A small personal collection of command-line utilities for everyday text cleanup and transformation.

## Features

- Normalize whitespace and line endings
- Change text case
- Sort and deduplicate lines
- Count words, characters, and lines
- Find and replace text with regular expressions
- Read from files or standard input

## Install

```bash
git clone https://github.com/your-username/text-tools.git
cd text-tools
npm install
npm link
```

## Usage

```bash
text-tools <command> [options] [file]
```

Examples:

```bash
text-tools count notes.txt
text-tools dedupe names.txt
cat draft.txt | text-tools normalize
text-tools replace "old" "new" document.txt
```

Run `text-tools --help` to see all commands and options.