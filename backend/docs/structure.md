# Project Sturcture

We have used a custom structure that didn't mention in the official Vuejs Guide, here is a brief intro

## Overview

```
app/
    core/
    crud/
    db/
    models/
    routers/
    schemas/
    tests/ 
docs/
scripts/
```

## Details

### docs

Where all documentation stored. 

### app

All the funtional code stored

### core

it controls the app's behavior

### crud

it is the repository of command for all possible database manipulation
convert general function calls to database manupulation

### db

establish the connection fromm database to back end

### models

all the logical calculaton.
it have all the class and functionn on how to manipulate the database
the real logical part of lineup

### routers

all the url schemas of the applicatioin

### schemas

build new database and migrate all the data in the old database if exists.

### tests

all the tests (not totally finished)
