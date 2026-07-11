
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class HaleyChatStripePaymentIntent(VITAL_Node):
        currentSubscriptionLevelURI: str
        desiredSubscriptionLevelURI: str
        haleyChatCustomerIdentifier: str
        haleyChatPaymentMethodIdentifier: str
        haleyChatStripeClientSecret: str
        haleyChatStripeInvoiceId: str
        haleyChatStripeMessage: str
        haleyChatStripePaymentAmount: int
        haleyChatStripePaymentIntentId: str
        haleyChatStripePaymentIntentStatusURI: str
        haleyChatStripeStatusTypeURI: str
        haleyChatStripeToken: str
        stripePaymentMethodIdentifier: str
        accountURI: str
        loginURI: str

