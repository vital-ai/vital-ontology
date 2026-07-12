# chat-ai

| | |
|---|---|
| **IRI** | `http://vital.ai/ontology/chat-ai` |
| **Version** | 0.1.0 |
| **OWL file** | `domain-ontology/chat-ai-0.1.0.owl` |
| **Classes** | 497 |
| **Properties** | 718 |
| **Imports** | `haley`, `haley-ai-kg`, `haley-ai-ml`, `vital-aimp` |
| **Python package** | [vital-ai-chat](https://pypi.org/project/vital-ai-chat/) |

## Purpose

The **chat application** domain: the full set of request/response message
types, administration commands, notifications, payments, and quotas
exchanged by the Vital AI chat applications.

This is the leaf of the domain package chain — installing `vital-ai-chat`
transitively installs every other Vital AI domain package.

## Key classes

- **Chat messages** — `AcceptChatRequest`, `ChatCreditNotificationMessage`,
  `ChatQuotaNotificationMessage`, and many more typed chat interactions.
- **Administration** — `AcceptAccountInviteAdminRequest`,
  `AcceptLoginChangeAdminRequest`, `AcceptMemberInviteAdminRequest`,
  `AcceptDeveloperRequest`.
- **`AIMPMessageMetaInfo`** — metadata attached to AIMP messages in chat
  context.
- **Payments / quotas** — `ChatQuotaInternalNotification` and related
  classes.

## Notes

With 497 classes this is the second-largest ontology. Most classes are
specialized request/response types for specific chat operations.
