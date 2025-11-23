import pytest
from pydantic import ValidationError
from app.schemas.calculation import CalculationCreate, CalculationRead, CalculationType
from datetime import datetime

class TestCalculationCreateSchema:
    def test_valid_add_calculation(self):
        calc = CalculationCreate(a=10.0, b=5.0, type=CalculationType.ADD)
        assert calc.a == 10.0
        assert calc.type == CalculationType.ADD
    
    def test_all_calculation_types(self):
        for calc_type in ["Add", "Subtract", "Multiply", "Divide"]:
            if calc_type == "Divide":
                calc = CalculationCreate(a=10.0, b=5.0, type=calc_type)
            else:
                calc = CalculationCreate(a=10.0, b=5.0, type=calc_type)
            assert calc.type.value == calc_type
    
    def test_divide_by_zero_validation(self):
        with pytest.raises(ValidationError) as exc_info:
            CalculationCreate(a=10.0, b=0.0, type="Divide")
        errors = exc_info.value.errors()
        assert any("Division by zero" in str(error) for error in errors)
    
    def test_invalid_calculation_type(self):
        with pytest.raises(ValidationError):
            CalculationCreate(a=10.0, b=5.0, type="Invalid")
    
    def test_missing_required_fields(self):
        with pytest.raises(ValidationError):
            CalculationCreate(a=10.0)
    
    def test_negative_numbers(self):
        calc = CalculationCreate(a=-10.0, b=5.0, type="Add")
        assert calc.a == -10.0

class TestCalculationReadSchema:
    def test_calculation_read_from_dict(self):
        data = {
            "id": 1, "a": 10.0, "b": 5.0, "type": "Add",
            "result": 15.0, "user_id": 1, "created_at": datetime.utcnow()
        }
        calc = CalculationRead(**data)
        assert calc.id == 1
        assert calc.result == 15.0
