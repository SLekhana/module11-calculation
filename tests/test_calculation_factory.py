import pytest
from app.factory.calculation_factory import (
    CalculationFactory, AddCalculation, SubtractCalculation,
    MultiplyCalculation, DivideCalculation, perform_calculation
)

class TestCalculationStrategies:
    def test_add_calculation(self):
        calc = AddCalculation()
        assert calc.calculate(5, 3) == 8
        assert calc.calculate(-5, 3) == -2
        assert calc.get_type() == "Add"
    
    def test_subtract_calculation(self):
        calc = SubtractCalculation()
        assert calc.calculate(5, 3) == 2
        assert calc.get_type() == "Subtract"
    
    def test_multiply_calculation(self):
        calc = MultiplyCalculation()
        assert calc.calculate(5, 3) == 15
        assert calc.get_type() == "Multiply"
    
    def test_divide_calculation(self):
        calc = DivideCalculation()
        assert calc.calculate(6, 3) == 2
        assert calc.get_type() == "Divide"
    
    def test_divide_by_zero(self):
        calc = DivideCalculation()
        with pytest.raises(ValueError, match="Division by zero"):
            calc.calculate(5, 0)

class TestCalculationFactory:
    def test_factory_creates_add(self):
        calc = CalculationFactory.create_calculation("Add")
        assert isinstance(calc, AddCalculation)
    
    def test_factory_creates_all_types(self):
        for calc_type in ["Add", "Subtract", "Multiply", "Divide"]:
            calc = CalculationFactory.create_calculation(calc_type)
            assert calc is not None
    
    def test_factory_invalid_type(self):
        with pytest.raises(ValueError, match="Invalid calculation type"):
            CalculationFactory.create_calculation("Invalid")
    
    def test_get_supported_types(self):
        types = CalculationFactory.get_supported_types()
        assert len(types) == 4
        assert "Add" in types

class TestPerformCalculation:
    def test_perform_add(self):
        assert perform_calculation(10, 5, "Add") == 15
    
    def test_perform_subtract(self):
        assert perform_calculation(10, 5, "Subtract") == 5
    
    def test_perform_multiply(self):
        assert perform_calculation(10, 5, "Multiply") == 50
    
    def test_perform_divide(self):
        assert perform_calculation(10, 5, "Divide") == 2
    
    def test_perform_divide_by_zero(self):
        with pytest.raises(ValueError):
            perform_calculation(10, 0, "Divide")
