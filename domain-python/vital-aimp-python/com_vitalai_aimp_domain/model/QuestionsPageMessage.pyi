
import datetime
from com_vitalai_aimp_domain.model.AIMPMessage import AIMPMessage


class QuestionsPageMessage(AIMPMessage):
        dialogPageURI: str
        multiChoiceQuestionInstruction: str
        nextButtonLabel: str
        page: int
        pageTypeIdentifier: str
        previousButtonLabel: str
        questionsPageThemeURI: str
        scrollToQuestionIndex: float
        status: str
        submitButtonLabel: str
        totalPages: int
        goodbyePage: bool
        hidePageCount: bool
        nextButtonEnabled: bool
        previousButtonEnabled: bool
        questionCountPanelDisabled: bool
        saveAnswersOnGoingBack: bool
        staticQuestionsList: bool
        submitButtonEnabled: bool

