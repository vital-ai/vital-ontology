
import datetime
from com_vitalai_aimp_domain.model.DialogAction import DialogAction


class Question(DialogAction):
        chatRulesOutputChannelFactName: str
        chatRulesOutputFactName: str
        columnsDefinition: str
        conditionalLogic: str
        constraints: str
        description: str
        dialogToCallName: str
        dialogToCallScope: str
        handlerResultFactName: str
        index: float
        internalProcessingChoice: str
        interruptedFactName: str
        maxRetriesCount: int
        placeholder: str
        prefilledAnswer: str
        previousAnswer: str
        propertyName: str
        propertyType: str
        questionContent: str
        questionDataJSON: str
        questionOption: str
        questionPreviousContent: str
        questionSubType: str
        questionType: str
        requestType: str
        sameAsCheckBoxLabel: str
        scriptBody: str
        sectionHeaderHTML: str
        shortDescription: str
        targetChannel: str
        text: str
        textChannelFactName: str
        textFactName: str
        textToSpeak: str
        broadcastOnly: bool
        currentChannelTarget: bool
        handlerEnabled: bool
        hidden: bool
        ignoreStandardIntents: bool
        internalAnswerProcessingEnabled: bool
        internalOnly: bool
        otherChannelTarget: bool
        processWithChatRules: bool
        questionCountExcluded: bool
        readOnlyQuestion: bool
        sameAsCheckboxEnabled: bool
        sendAsUser: bool
        skippable: bool

