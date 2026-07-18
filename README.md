# Arrow Programming Language

<img width="1254" height="1254" alt="ARROW LANG" src="https://github.com/user-attachments/assets/774c2dda-fbc7-4eba-90a3-44e8465c665c" />


> **Arrow is a Flow Programming Language.**
>
> Data flows through functions.
> The language stays small.
> The Standard Library does the rest.

---

# Philosophy

Arrow was designed around a simple idea:

> **Data flows through the program.**

Instead of focusing on objects or classes, Arrow focuses on transformations.

```arrow
data
    -> function
    -> function
    -> function
```

Arrow aims to be:

- Simple
- Readable
- Minimal
- Consistent

Arrow intentionally avoids:

- Complex Object-Oriented Programming
- Dozens of keywords
- Unnecessary syntax
- Hidden behavior

---

# Hello World

```arrow
"Hello, Arrow!" <<
```

---

# Variables

Assignment

```arrow
10 >> x

"Andrea" >> name

true >> online
```

Reading

```arrow
x <<
```

---

# Input

User input

```arrow
$> "Name: " >> name
```

Command line arguments

```arrow
£> 0 >> input

£> 1 >> output
```

Execution

```bash
python arrow.py program.arr input.txt output.txt
```

---

# Pipeline

The pipeline is the core of Arrow.

```arrow
10
    -> double
    <<
```

Multiple pipelines

```arrow
10
    -> double
    -> double
    <<
```

---

# Functions

Definition

```arrow
fn double x

    <- x * 2

-fn
```

Usage

```arrow
10
    -> double
    <<
```

Multiple parameters

```arrow
fn add a b

    <- a + b

-fn

10 20
    -> add
    <<
```

---

# Control Flow

## If

```arrow
if age >= 18

    "Adult" <<

-if
```

## If / Else

```arrow
if age >= 18

    "Adult" <<

else

    "Minor" <<

-if
```

## While

```arrow
0 >> x

wh x < 5

    x <<

    x + 1 >> x

-wh
```

## For

```arrow
[10 20 30] >> numbers

for n in numbers

    n <<

-for
```

---

# Arrays

Creation

```arrow
[10 20 30] >> numbers
```

Access

```arrow
numbers[0] <<
```

---

# Structs

Definition

```arrow
ST person

    name
    age

-ST
```

Creation

```arrow
person § "Andrea" 30 >> p
```

Access

```arrow
p.name <<

p.age <<
```

Modification

```arrow
40 >> p.age
```

---

# Comments

```arrow
// This is a comment
```

---

# Modules

Arrow keeps the language small.

Features are added through modules.

```arrow
<math>

<string>

<json>

<http>

<quantum>

<gleam>
```

Example

```arrow
<math>

10 20
    -> math.add
    <<
```

---

# Standard Library

Examples

```arrow
text
    -> upper
```

```arrow
numbers
    -> sum
```

```arrow
numbers
    -> reverse
```

```arrow
numbers
    -> length
```

---

# File Operations

Read

```arrow
"notes.txt"
    -> read
    <<
```

Write

```arrow
"notes.txt"
    -> write "Hello"
```

Append

```arrow
"notes.txt"
    -> append "World"
```

---

# Example Program

```arrow
<math>

ST person

    name
    age

-ST


fn greet p

    <- "Hello " + p.name

-fn


$> "Name: " >> name

$> "Age: " >> age


person § name age >> user


user
    -> greet
    <<
```

---

# Language Core

Arrow intentionally has very few keywords.

```
fn
if
else
wh
for
in
ST
```

Special operators

```
>>
<<
->
<-
§
$>
£>
```

Module import

```
<module>
```

---

# Current Status

Implemented

- Variables
- Numbers
- Strings
- Booleans
- Functions
- Pipelines
- Arrays
- Structs
- if / else
- while
- for
- User Input
- CLI Arguments

In Progress

- Complete Standard Library
- File System API
- Module System
- Documentation

Future

- HTTP
- JSON
- Database
- Quantum Computing Module
- Gleam Integration

---

# Vision

Arrow is not designed to become a huge language.

Instead:

- The language remains small.
- The Standard Library grows.
- Modules add new capabilities.

The syntax should stay recognizable years from now.

---

# Long-term Goal

Arrow aims to become a simple language for:

- Terminal applications
- Automation
- Utilities
- Data transformation
- Scripting
- Learning functional programming
- Building small and medium-sized tools

Future modules may also provide:

- HTTP
- Networking
- JSON
- Databases
- Quantum Computing
- Integration with Gleam

Without changing the core syntax.

---

# License

MIT License<img width="1254" height="1254" alt="ARROW LANG" src="https://github.com/user-attachments/assets/4ae04529-5781-44cd-8249-50683be79c8a" />
