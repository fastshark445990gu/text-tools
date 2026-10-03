# text-tools

A small collection of command-line utilities I use to clean, inspect, and transform plain text.

## Features

- Normalize whitespace and line endings
- Remove duplicate or empty lines
- Sort lines alphabetically or by length
- Count words, characters, and lines
- Convert text to lowercase, uppercase, title case, or slug format
- Read from files or standard input for easy shell pipelines

## Install

Requires Python 3.10 or newer.

    git clone https://github.com/your-username/text-tools.git
    cd text-tools
    python -m pip install .

## Usage

Clean a file and write the result to standard output:

    text-tools clean notes.txt

Remove duplicate lines and save the result:

    text-tools dedupe input.txt > output.txt

Pipe text between commands:

    cat draft.txt | text-tools slug

List all commands and options:

    text-tools --help

Built for the repetitive text chores that were too small for a script but too common to keep doing by hand.