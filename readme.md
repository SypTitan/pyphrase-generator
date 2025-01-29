<div align="center">
<h1>Passphrase Generator</h1>
</div>
<div align="center">
<img src="https://imgs.xkcd.com/comics/password_strength.png" width="60%" height="-1" alt="xkcd #936: Password Strength">
</div>
</lb>
<div align="center">
A simple CLI that generates (somewhat secure) passphrases, inspired by <a href="https://xkcd.com/936/">xkcd #936</a>, creating phrases by picking words from a list of 100 adjectives and 100 nouns.
</div>


## Installation
This project uses [uv](https://docs.astral.sh/uv/) as project manager.

To use the project, install uv, clone the repo, and run `uv sync`.

## Usage
```
uv run generate [-l|--lowercase] [-s sep|--separator sep] [length]
uv run gen [-l|--lowercase] [-s sep|--separator sep] [length]
```

## Examples
```
uv run generate                 # Lazy Slow Card Hope
uv run generate 2               # Fancy Gate
uv run generate -l              # dry dream grass sheep
uv run generate -l 6            # slow warm high wise bridge moon
uv run generate -s "-"          # Purple-Paper-Door-Town
uv run generate -l -s "_" 3     # gray_bold_sword
```
---

<details>
    <summary><h2 style="display:inline-block">Adjectives used in generation</h2></summary>

    red
    blue
    green
    yellow
    purple
    orange
    black
    white
    gray
    brown
    tall
    short
    big
    small
    tiny
    huge
    wide
    narrow
    thick
    thin
    fast
    slow
    hot
    cold
    warm
    cool
    bright
    dark
    loud
    quiet
    soft
    hard
    rough
    smooth
    sharp
    dull
    clean
    dirty
    dry
    wet
    new
    old
    young
    fresh
    stale
    rich
    poor
    full
    empty
    light
    heavy
    strong
    weak
    bold
    shy
    brave
    calm
    wild
    tame
    sweet
    sour
    bitter
    mild
    spicy
    flat
    round
    square
    deep
    shallow
    high
    low
    long
    quick
    slow
    busy
    lazy
    proud
    wise
    funny
    stern
    kind
    mean
    nice
    neat
    messy
    plain
    fancy
    rare
    pure
    raw
    ripe
    safe
    sick
    sore
    tidy
    vast
    warm
    wise
    real
    main
</details>

<details>
    <summary><h2 style="display:inline-block">Nouns used in generation</h2></summary>

    time
    door
    tree
    bird
    fish
    book
    hand
    star
    ring
    king
    queen
    heart
    fire
    rain
    snow
    wind
    moon
    ship
    road
    path
    house
    chair
    table
    wall
    floor
    roof
    food
    bread
    milk
    meat
    fruit
    apple
    stone
    sand
    lake
    river
    hill
    cloud
    storm
    light
    sound
    voice
    child
    horse
    sheep
    plant
    grass
    leaf
    wood
    metal
    glass
    gold
    paper
    clock
    wheel
    train
    plane
    sword
    shield
    crown
    bridge
    tower
    gate
    cave
    farm
    field
    coast
    beach
    world
    earth
    water
    ocean
    game
    song
    film
    story
    money
    work
    room
    card
    tooth
    hair
    face
    head
    foot
    nose
    mind
    gift
    shop
    town
    city
    park
    dream
    life
    hope
    friend
    baby
    bird
    dog
    cat
</details>