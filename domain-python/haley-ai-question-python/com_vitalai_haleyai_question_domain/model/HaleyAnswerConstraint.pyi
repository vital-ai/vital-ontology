
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class HaleyAnswerConstraint(VITAL_Node):
        booleanAnswerValue: bool
        choiceAnswerValue: str
        dateRangeDecrease: int
        dateRangeIncrease: int
        dateTimeAnswerValue: datetime
        doubleAnswerValue: float
        doubleRangeDecrease: float
        doubleRangeIncrease: float
        fileAnswerValueURI: str
        haleyAnswerComparison: str
        haleyAnswerConstantURI: str
        haleyAnswerConstraintComparatorURI: str
        haleyAnswerConstraintRelationshipURI: str
        haleyAnswerConstraintType: str
        haleyAnswerDataType: str
        haleyAnswerTypeComparison: str
        haleyAnswerUnitType: str
        haleyCurrencyType: str
        integerAnswerValue: int
        integerRangeDecrease: int
        integerRangeIncrease: int
        longTextAnswerValue: str
        lowerBoundCurrencyValue: float
        lowerBoundDateValue: datetime
        lowerBoundDoubleValue: float
        lowerBoundIntegerValue: int
        multiChoiceAnswerValue: str
        multiTaxonomyAnswerValue: str
        objectAnswerValueURI: str
        signatureAnswerValue: str
        taxonomyAnswerValue: str
        upperBoundCurrencyValue: float
        upperBoundDateValue: datetime
        upperBoundDoubleValue: float
        upperBoundIntegerValue: int

