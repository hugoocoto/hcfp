# HCFP - Hugo's Config File Parser

## About `.hcf` format

The simplest file format I can imagine. Inspired by `.ini`. I’ve designed it to be easy to use for users and easy to implement for developers.

### Formal definition

```txt
identifier  = [^ \n\t]+
value       = [^\n]+
comment     = "//".*
padding     = " "*

field   -> ^ padding identifier ":"               padding comment? $
assign  -> ^ padding identifier " " padding value padding comment? $
ignored -> ^                                      padding comment? $

body -> (field | assign | ignored)*
```

### Textual definition

The file format has two types of entries: field names and values. Field names
are identifiers followed by a colon (`:`). Every value declared after a field
name belongs to that field.

Values are defined by a key (an identifier), followed by one or more spaces,
and then a string — starting from the first non-space character and ending at
the last non-space character. Identifiers are defined as consecutive
characters without spaces.

### Data structure

Data should be accessed using the field name and key name, which return the
associated string value. Invalid operations, such as accessing a non-existent
field or key, are language-specific. The implementation *may* provide
functionality to add or modify values, as well as to dump data to a file, but
these are not required. The only required features are reading from a file and
accessing data by field and key. Printing functions are also optional.

## Undefined behavior

* Should `\//` be ignored as a comment introducer?

## Implementations by language

* [Python](./src/python/hcfp.py)
* [C](./src/c/hcfp.h)
