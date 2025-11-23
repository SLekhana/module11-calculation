from abc import ABC, abstractmethod
from typing import Dict, Type

class CalculationStrategy(ABC):
    @abstractmethod
    def calculate(self, a: float, b: float) -> float:
        pass
    
    @abstractmethod
    def get_type(self) -> str:
        pass

class AddCalculation(CalculationStrategy):
    def calculate(self, a: float, b: float) -> float:
        return a + b
    
    def get_type(self) -> str:
        return "Add"

class SubtractCalculation(CalculationStrategy):
    def calculate(self, a: float, b: float) -> float:
        return a - b
    
    def get_type(self) -> str:
        return "Subtract"

class MultiplyCalculation(CalculationStrategy):
    def calculate(self, a: float, b: float) -> float:
        return a * b
    
    def get_type(self) -> str:
        return "Multiply"

class DivideCalculation(CalculationStrategy):
    def calculate(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Division by zero is not allowed")
        return a / b
    
    def get_type(self) -> str:
        return "Divide"

class CalculationFactory:
    _strategies: Dict[str, Type[CalculationStrategy]] = {
        "Add": AddCalculation,
        "Subtract": SubtractCalculation,
        "Multiply": MultiplyCalculation,
        "Divide": DivideCalculation,
    }
    
    @classmethod
    def create_calculation(cls, calculation_type: str) -> CalculationStrategy:
        strategy_class = cls._strategies.get(calculation_type)
        if strategy_class is None:
            raise ValueError(
                f"Invalid calculation type: {calculation_type}. "
                f"Supported types: {', '.join(cls._strategies.keys())}"
            )
        return strategy_class()
    
    @classmethod
    def register_strategy(cls, calculation_type: str, strategy_class: Type[CalculationStrategy]):
        cls._strategies[calculation_type] = strategy_class
    
    @classmethod
    def get_supported_types(cls) -> list:
        return list(cls._strategies.keys())

def perform_calculation(a: float, b: float, calculation_type: str) -> float:
    strategy = CalculationFactory.create_calculation(calculation_type)
    return strategy.calculate(a, b)
