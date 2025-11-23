import pytest
from app.models.calculation import Calculation
from app.schemas.calculation import CalculationCreate, CalculationType
from app.factory.calculation_factory import perform_calculation

class TestCalculationModel:
    def test_create_calculation(self, db_session):
        calc = Calculation(a=10.0, b=5.0, type="Add", result=15.0)
        db_session.add(calc)
        db_session.commit()
        db_session.refresh(calc)
        
        assert calc.id is not None
        assert calc.a == 10.0
        assert calc.result == 15.0
    
    def test_create_all_types(self, db_session):
        calculations = [
            Calculation(a=10.0, b=5.0, type="Add", result=15.0),
            Calculation(a=10.0, b=5.0, type="Subtract", result=5.0),
            Calculation(a=10.0, b=5.0, type="Multiply", result=50.0),
            Calculation(a=10.0, b=5.0, type="Divide", result=2.0),
        ]
        for calc in calculations:
            db_session.add(calc)
        db_session.commit()
        
        saved = db_session.query(Calculation).all()
        assert len(saved) == 4
    
    def test_read_calculation(self, db_session):
        calc = Calculation(a=20.0, b=4.0, type="Divide", result=5.0)
        db_session.add(calc)
        db_session.commit()
        
        saved = db_session.query(Calculation).filter_by(id=calc.id).first()
        assert saved.a == 20.0
        assert saved.type == "Divide"
    
    def test_delete_calculation(self, db_session):
        calc = Calculation(a=10.0, b=5.0, type="Add", result=15.0)
        db_session.add(calc)
        db_session.commit()
        calc_id = calc.id
        
        db_session.delete(calc)
        db_session.commit()
        
        deleted = db_session.query(Calculation).filter_by(id=calc_id).first()
        assert deleted is None

class TestCalculationIntegration:
    def test_create_and_compute(self, db_session):
        calc_schema = CalculationCreate(a=15.0, b=3.0, type=CalculationType.MULTIPLY)
        result = perform_calculation(calc_schema.a, calc_schema.b, calc_schema.type.value)
        
        calc = Calculation(
            a=calc_schema.a, b=calc_schema.b,
            type=calc_schema.type.value, result=result
        )
        db_session.add(calc)
        db_session.commit()
        
        assert calc.result == 45.0
