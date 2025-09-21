# Snake Game Refactoring TODO

## Overview
This document outlines structural improvements and refactoring suggestions for the snake game to make it more maintainable, testable, and extensible.

## Current Strengths
- ✅ Good modular structure with logical class separation
- ✅ Clean imports and dependencies
- ✅ Use of enums (Direction)
- ✅ Type hints implementation

## Major Structural Issues to Address

### 1. Snake Class Refactoring
**Current Problems:**
- Too many responsibilities (movement, collision, position management)
- Unused `update_position()` method
- Duplicated logic between `update_position()` and `update_snake()`
- Hardcoded logic in `fill_positions()`

**TODO:**
- [ ] Split Snake into multiple specialized classes:
  - [ ] Create `SnakeBody` class - manages list of positions and growth
  - [ ] Create `SnakeMovement` class - handles direction changes and movement calculations
  - [ ] Create `SnakeCollision` class - handles collision detection (walls, self-collision)
  - [ ] Refactor `Snake` to be a coordinator that uses these components
  - [ ] Remove unused `update_position()` method
  - [ ] Consolidate position update logic

### 2. GameBoard Class Refactoring
**Current Problems:**
- Mixing data structure with rendering logic
- Complex coordinate transformation in `set_value()`
- Tight coupling between game logic and display logic

**TODO:**
- [ ] Separate concerns into specialized classes:
  - [ ] Create `GameBoard` - pure data structure for game state
  - [ ] Create `BoardRenderer` - handles all curses-specific rendering logic
  - [ ] Create `CoordinateMapper` - handles coordinate transformations between game space and display space
  - [ ] Move `print_board()` logic to `BoardRenderer`
  - [ ] Simplify `set_value()` method

### 3. Game Loop Class Refactoring
**Current Problems:**
- Single class handling input, game logic, rendering, and timing
- Hard-coded game rules mixed with game loop logic
- No clear separation between game state and game flow

**TODO:**
- [ ] Create specialized classes:
  - [ ] Create `InputHandler` - processes keyboard input and converts to game actions
  - [ ] Create `GameRules` - contains collision detection, scoring logic, win/lose conditions
  - [ ] Create `GameTimer` - manages game timing and refresh rates
  - [ ] Create `GameState` - holds current game state (score, running status, etc.)
  - [ ] Refactor `Game.run()` to coordinate these components

### 4. Food Class Simplification
**Current Problems:**
- Unnecessary complexity with `exists` flag and `shape` properties
- Position generation logic could be more robust

**TODO:**
- [ ] Simplify Food class to focus on position and generation
- [ ] Remove unnecessary `exists` and `shape` properties
- [ ] Move collision detection with snake to dedicated collision system
- [ ] Improve position generation robustness

## Missing Abstractions to Implement

### 1. Game Entity System
**TODO:**
- [ ] Create base `GameEntity` class:
  ```python
  class GameEntity:
      def __init__(self, position: Tuple[int, int]):
          self.position = position
      
      def get_position(self) -> Tuple[int, int]:
          return self.position
      
      def set_position(self, position: Tuple[int, int]):
          self.position = position
  ```
- [ ] Make `Snake` and `Food` inherit from `GameEntity`
- [ ] Standardize position handling across all entities

### 2. Event System
**TODO:**
- [ ] Create `GameEvent` class:
  ```python
  class GameEvent:
      def __init__(self, event_type: str, data: dict = None):
          self.type = event_type
          self.data = data or {}
  ```
- [ ] Create `EventManager` class for loose coupling
- [ ] Implement event subscription and publishing system
- [ ] Replace direct method calls with events where appropriate

### 3. Configuration Management
**TODO:**
- [ ] Create `GameConfig` class:
  ```python
  class GameConfig:
      def __init__(self):
          self.refresh_timer = 0.5
          self.snake_shape = "#"
          self.food_shape = "•"
          self.colors = {...}
          self.bounds_checking = True
  ```
- [ ] Centralize all game settings
- [ ] Make configuration easily modifiable
- [ ] Remove hardcoded values from classes

## Function Relocation Tasks

### Move to InputHandler:
- [ ] All keyboard input processing from `Game.run()`
- [ ] Key-to-direction mapping logic
- [ ] Input validation and error handling

### Move to GameRules:
- [ ] Collision detection logic from `Game.run()`
- [ ] Score calculation
- [ ] Win/lose condition checking
- [ ] Game rule validation

### Move to BoardRenderer:
- [ ] All curses-specific rendering from `GameBoard.print_board()`
- [ ] Color management
- [ ] Screen clearing and refreshing
- [ ] Display formatting

### Move to SnakeMovement:
- [ ] `update_direction()` from `Snake`
- [ ] Movement calculation logic
- [ ] Direction validation

### Move to SnakeCollision:
- [ ] `is_out_of_bounds()` from `Snake`
- [ ] Self-collision detection
- [ ] Wall collision detection

## Additional Improvements

### 1. Error Handling
**TODO:**
- [ ] Add proper exception handling for curses operations
- [ ] Validate game parameters more robustly
- [ ] Handle edge cases in coordinate calculations
- [ ] Add graceful error recovery

### 2. Constants Management
**TODO:**
- [ ] Move all magic numbers to `constants.py`
- [ ] Create named constants for:
  - [ ] ASCII codes (key codes)
  - [ ] Timing values
  - [ ] Board dimensions
  - [ ] Color codes
- [ ] Remove hardcoded values from classes

### 3. State Management
**TODO:**
- [ ] Create proper game state machine
- [ ] Implement states: initialization, running, paused, game-over
- [ ] Add state transition logic
- [ ] Handle state-specific behavior

### 4. Testing Structure
**TODO:**
- [ ] Add unit tests for individual components
- [ ] Create mock objects for curses operations
- [ ] Test game logic independently of UI
- [ ] Add integration tests
- [ ] Set up test framework (pytest)

## Suggested New Architecture

```
GameEngine/
├── GameState (holds current state)
├── GameConfig (configuration)
├── EventManager (event system)
├── InputHandler (keyboard input)
├── GameRules (collision, scoring)
├── GameTimer (timing control)
└── Renderer/
    ├── BoardRenderer
    └── CoordinateMapper

GameEntities/
├── GameEntity (base class)
├── Snake/
│   ├── SnakeBody
│   ├── SnakeMovement
│   └── SnakeCollision
└── Food

GameBoard (pure data structure)
```

## Implementation Priority

### Phase 1: Core Refactoring
1. [ ] Create `GameConfig` class
2. [ ] Implement `GameEntity` base class
3. [ ] Split `Snake` class into specialized components
4. [ ] Separate `GameBoard` rendering logic

### Phase 2: Game Loop Improvements
1. [ ] Create `InputHandler`
2. [ ] Create `GameRules`
3. [ ] Create `GameTimer`
4. [ ] Refactor `Game.run()` method

### Phase 3: Advanced Features
1. [ ] Implement event system
2. [ ] Add state management
3. [ ] Improve error handling
4. [ ] Add comprehensive testing

### Phase 4: Polish
1. [ ] Optimize performance
2. [ ] Add documentation
3. [ ] Code cleanup and review
4. [ ] Final testing

## Notes
- Each TODO item should be implemented incrementally
- Test each change before moving to the next
- Consider creating feature branches for major refactoring
- Keep the game playable throughout the refactoring process