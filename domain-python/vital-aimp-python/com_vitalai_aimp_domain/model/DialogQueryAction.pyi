
import datetime
from com_vitalai_aimp_domain.model.DialogAction import DialogAction


class DialogQueryAction(DialogAction):
        criteriaType: str
        destinationFactName: str
        destinationFactScope: str
        errorMessagePropertyName: str
        propertyName: str
        queryType: str
        relationshipFactName: str
        relationshipFactScope: str
        sourceFactName: str
        sourceFactScope: str
        statusPropertyName: str
        targetService: str
        timeoutSeconds: int
        graphObjectsLinked: bool

