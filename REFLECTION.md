# Module 11 Assignment Reflection

## Student Information
- **Name**: Lekhana Sandra
- **Module**: 11 - Calculation Model with Factory Pattern
- **Date**: November 2025

## Assignment Overview

This assignment focused on implementing a calculation system using SQLAlchemy models, Pydantic validation, and the Factory design pattern, with comprehensive testing and CI/CD deployment.

## Implementation Summary

### 1. SQLAlchemy Model
- Created `Calculation` model with fields: id, a, b, type, result, user_id, created_at
- Implemented foreign key relationship with User model
- Chose to store computed results for performance and audit purposes

### 2. Pydantic Schemas
- `CalculationCreate`: Input validation with division-by-zero checking
- `CalculationRead`: Output serialization
- `CalculationType`: Enum for operation types
- Used `model_validator` for complex validation logic

### 3. Factory Pattern
- Abstract `CalculationStrategy` base class
- Four concrete implementations: Add, Subtract, Multiply, Divide
- `CalculationFactory` for strategy instantiation
- Extensible design for adding new operations

### 4. Testing
- 14 factory unit tests (100% coverage)
- 7 schema validation tests
- 5 database integration tests
- Total: 26 tests, all passing

## Challenges and Solutions

### Challenge 1: Python Version Compatibility
**Problem**: Initial setup used Python 3.13, causing psycopg2-binary and pydantic-core build failures.

**Solution**: Switched to Python 3.11 using conda environment:
```bash
conda create -n module11 python=3.11 -y
conda activate module11
```

### Challenge 2: Pydantic Validation Order
**Problem**: Field-level validators weren't catching division by zero because type wasn't validated first.

**Solution**: Changed from `@field_validator` to `@model_validator(mode='after')` to validate after all fields are set:
```python
@model_validator(mode='after')
def validate_division(self):
    if self.type == CalculationType.DIVIDE and self.b == 0:
        raise ValueError("Division by zero is not allowed")
    return self
```

### Challenge 3: Test Database Management
**Problem**: Needed consistent test environment across local and CI.

**Solution**: Used SQLite locally and PostgreSQL in CI, with proper fixtures for isolation.

## Key Learnings

1. **Factory Pattern Value**: Makes code extensible - adding new operations requires no changes to existing code
2. **Validation Layers**: Multiple validation points (Pydantic + Factory) provide defense in depth
3. **Test Organization**: Separating unit and integration tests improves clarity and speed
4. **CI/CD Benefits**: Automated testing catches issues before deployment

## Technical Skills Demonstrated

- ✅ SQLAlchemy ORM and database modeling
- ✅ Pydantic validation and serialization
- ✅ Design patterns (Factory, Strategy)
- ✅ Unit and integration testing with pytest
- ✅ GitHub Actions CI/CD
- ✅ Docker containerization
- ✅ Professional documentation

## Time Investment

- Planning: 1 hour
- Implementation: 3 hours
- Testing: 2 hours
- CI/CD Setup: 1 hour
- Documentation: 1 hour
- **Total**: ~8 hours

## Future Improvements

1. Add more calculation types (power, modulo, square root)
2. Implement calculation history endpoints
3. Add user authentication integration
4. Create frontend interface
5. Add performance monitoring

## Conclusion

This assignment successfully demonstrates production-ready software development practices including proper architecture, comprehensive testing, and automated deployment. The factory pattern makes the system highly maintainable and extensible.

---

**Submitted**: November 2025 
**Repository**: https://github.com/SLekhana/module11-calculation 
**Docker Hub**: https://hub.docker.com/repository/docker/lekhanasandra/fastapi-calc-app/general 
