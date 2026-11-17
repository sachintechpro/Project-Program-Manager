# Context help and role-aware work assistant

The **? Help** button and floating assistant follow the signed-in role, page and selected initiative.

**Field help:** Explanations and examples for over 260 data parameters, sourced from the readable CSV catalogs in `seed/help/`. Guidance includes relevant SAFe definitions and human control reminders.

**Guided chat:** Works without a paid model. It can describe the current stage, the user's assigned approval controls, contract review needs and owned RAID items with recorded due dates. It cannot edit or approve any item.

**Connected AI:** Optional. The organization must configure a live OpenAI connector, and each user must turn on **Use connected AI**. The server supplies minimal role-permitted context. It does not automatically send raw contracts, private financial records or credentials, or provide any action-executing tools.

**Access and audit:** Session and CSRF checks protect the chat endpoint. The server enforces permissions even if someone asks to see a different role's information. Chat history clears on role switch. The audit ledger records request metadata rather than raw questions.

**Limitations:** This is a working demo with synthetic business records. The assistant is a work guide, not an authoritative SAFe certifier, production operations bot or evidence of executed tests. Before live organizational use, establish identity, data retention and external-model governance and perform independent security validation.
