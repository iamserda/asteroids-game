# Asteroids (Pygame)

A fast, classic Asteroids-style arcade game built with Pygame. Pilot a nimble triangle ship, dodge incoming rocks, and blast asteroids into smaller fragments. The gameplay loop is simple and satisfying, and the codebase is small enough to explore in an afternoon.

## Features
- Classic Asteroids movement and shooting.
- Procedural asteroid spawns from screen edges.
- Asteroid splitting with varied sizes and velocities.
- Lightweight logging of game state and events for debugging.

## Requirements
- Python 3.12+
- Pygame 2.6.1

## Install
Use your preferred Python environment manager, then install dependencies:

With uv:

```bash
uv sync
```

With pip:

```bash
pip install pygame==2.6.1
```

## Run
```bash
python main.py
```

## Controls
- `W` / `S`: Thrust forward / reverse
- `A` / `D`: Rotate left / right
- `Space`: Shoot

## Project Layout
- `main.py`: game loop and sprite groups
- `player.py`: player ship behavior
- `asteroid.py`: asteroid behavior and splitting
- `asteroidfield.py`: spawns asteroids at screen edges
- `shot.py`: projectile behavior
- `logger.py`: optional debug logging to JSONL

## Logging
When enabled via `logger.py`, the game writes lightweight JSONL files:
- `game_state.jsonl`: periodic snapshots of sprites and positions
- `game_events.jsonl`: notable events like hits and splits

## License
MIT (or your preferred license)
