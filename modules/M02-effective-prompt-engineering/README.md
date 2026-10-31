# Module 02 | Effective Prompt Engineering
### Twinkle & Celestyn — Design & Troubleshooting Lab

**Episode runtime:** 41:11 · **Guide type:** Timestamped listening companion · **Track:** AI-first foundations

> **No hands-on lab in this module.** The hydropower handoff and prompt examples are explanations, not assignments. This guide helps you follow the narration and recognize what makes a prompt useful and factually defensible. You do **not** need to sign in to Power Apps or configure an AI tool.
>
> **Listen with timestamps:** [Watch the Module 02 podcast on YouTube](https://youtu.be/q4C4eKex1pg). The links below open the episode at the corresponding topic. Video playback times may vary slightly.

## 1. Follow the podcast by timestamp

| Time | Follow along with Twinkle & Celestyn |
|---|---|
| **[00:00](https://youtu.be/q4C4eKex1pg?t=0)** | Why fluent AI writing is not proof of accuracy |
| **[01:56](https://youtu.be/q4C4eKex1pg?t=116)** | Generative text, images, code, tokens, and patterns |
| **[03:28](https://youtu.be/q4C4eKex1pg?t=208)** | What prompt engineering means |
| **[04:12](https://youtu.be/q4C4eKex1pg?t=252)** | Why a model is not simply a library of approved answers |
| **[06:42](https://youtu.be/q4C4eKex1pg?t=402)** | SunnyVerse Hydropower Operations: the fictional shift handoff |
| **[08:21](https://youtu.be/q4C4eKex1pg?t=501)** | What goes wrong with “Summarize the handoff” |
| **[09:53](https://youtu.be/q4C4eKex1pg?t=593)** | Requested inspection versus reported completion |
| **[11:48](https://youtu.be/q4C4eKex1pg?t=708)** | The two basic parts: instruction and context |
| **[14:16](https://youtu.be/q4C4eKex1pg?t=856)** | Audience: experienced supervisor versus new reader |
| **[15:48](https://youtu.be/q4C4eKex1pg?t=948)** | Tone and purpose: operational notes versus persuasion |
| **[17:54](https://youtu.be/q4C4eKex1pg?t=1074)** | Why “make it professional” is too vague |
| **[19:14](https://youtu.be/q4C4eKex1pg?t=1154)** | Useful context versus irrelevant or excessive detail |
| **[20:38](https://youtu.be/q4C4eKex1pg?t=1238)** | Simple and detailed prompts; when each is appropriate |
| **[22:24](https://youtu.be/q4C4eKex1pg?t=1344)** | Conflicting instructions and unsupported demands |
| **[23:50](https://youtu.be/q4C4eKex1pg?t=1430)** | Describing visual outputs with more precision |
| **[25:20](https://youtu.be/q4C4eKex1pg?t=1520)** | Product modes and settings do not guarantee factuality |
| **[27:20](https://youtu.be/q4C4eKex1pg?t=1640)** | Check generated claims against the real evidence |
| **[28:49](https://youtu.be/q4C4eKex1pg?t=1729)** | Topic mixing, chat context, and starting fresh |
| **[31:35](https://youtu.be/q4C4eKex1pg?t=1895)** | Output length and retaining important unresolved items |
| **[33:33](https://youtu.be/q4C4eKex1pg?t=2013)** | Paragraphs, bullets, and tables are formats—not verification |
| **[35:29](https://youtu.be/q4C4eKex1pg?t=2129)** | Clarify an imperfect answer without inventing facts |
| **[38:39](https://youtu.be/q4C4eKex1pg?t=2319)** | Recap and the transition to AI-assisted application planning |

## 2. Keep the hydropower example straight

At **[06:42](https://youtu.be/q4C4eKex1pg?t=402)–[11:48](https://youtu.be/q4C4eKex1pg?t=708)**, the hosts introduce a *fictional* shift note from **SunnyVerse Hydropower Operations**. The core issue is the difference between something reported, something requested, and something unknown.

| What the fictional note establishes | What it does **not** establish |
|---|---|
| A reservoir-level observation was recorded at **06:00**. | The numerical reservoir measurement or whether it is safe. |
| A debris-screen inspection was **requested**. | That an inspection occurred, passed, or was completed. |
| An equipment-alarm status update is **missing**. | That the alarm was resolved, dismissed, or escalated. |

**Read the verbs carefully:** “requested” describes an instruction; “completed” describes an outcome. An AI-generated sentence cannot turn the first into the second. A polished table or a confident tone cannot fill a gap in the original evidence.

## 3. What an effective prompt contains

At **[11:48](https://youtu.be/q4C4eKex1pg?t=708)–[20:38](https://youtu.be/q4C4eKex1pg?t=1238)**, Twinkle and Celestyn distinguish *instruction* (the work to do) from *context* (the information and boundaries needed to do it).

| Part | Question to answer | Hydropower example |
|---|---|---|
| **Instruction** | What should the system produce? | Summarize the handoff and identify unresolved items. |
| **Relevant context** | Which facts may it use? | Only the fictional handoff note and stated statuses. |
| **Audience and purpose** | Who will read this, and why? | Incoming Hydro Shift Supervisor preparing for handoff. |
| **Evidence boundary** | What must it not assume? | Never treat a requested inspection as completed; mark missing alarm status as unknown. |
| **Presentation** | How should the answer look? | A short status summary with a separate open-items section. |

### Example wording from the lesson's ideas — not a required exercise

This original, copy-friendly illustration puts those elements together. It is **not** a record of an AI model being tested, a real operations log, or a task you must complete.

```text
Task: Summarize the handoff for an incoming Hydro Shift Supervisor.

Fictional source note:
- A reservoir-level observation was recorded at 06:00.
- A debris-screen inspection was requested; no completion result is supplied.
- No equipment-alarm status update is supplied.

Instructions:
- Separate recorded facts, outstanding requests, and unknown statuses.
- Do not assume that an inspection was completed or an alarm resolved.
- Use a concise, neutral tone.
- State when the source note does not provide an answer.

Output: One short summary plus a bullet list of open or unknown items.
```

A faithful hypothetical summary would say: **“Reservoir observation recorded at 06:00; debris-screen inspection requested, completion not documented; equipment-alarm status not provided.”** This is an *illustration of acceptable phrasing*, not a generated or independently verified operating result.

## 4. Choose only the detail the task needs

Follow **[20:38](https://youtu.be/q4C4eKex1pg?t=1238)–[35:29](https://youtu.be/q4C4eKex1pg?t=2129)** as the hosts examine different prompt choices.

| Situation | Better direction | Why it matters |
|---|---|---|
| A straightforward title or brief rewrite | A simple, direct prompt may be enough. | Complexity is useful only when there is a real requirement. |
| Several readers, statuses, and evidence limits | Give specific instructions, audience, and boundaries. | Reduces ambiguity but does not guarantee correctness. |
| “Include only verified facts” **and** “show every item resolved” | Remove the conflicting demand. | Missing information must remain missing. |
| An illustration of a solar farm | Specify subject, viewpoint, lighting, and style. | Visual detail narrows the intended result. |
| A short operational handoff | Preserve every unresolved or unknown item, even when brief. | Over-compression can discard the most important caveat. |
| A paragraph versus a table | Choose the format most useful to the reader. | Formatting changes readability, not truthfulness. |
| A response that wrongly states “inspection complete” | Identify the exact unsupported statement and request a correction. | A revision still needs human review against source records. |

### Five quick checks while reading any generated answer

1. **Task:** Did it do what was asked?
2. **Evidence:** Is each important factual claim supported by supplied records?
3. **Status:** Did it keep *observed*, *requested*, *completed*, and *unknown* separate?
4. **Reader:** Is the wording appropriate to the audience and purpose?
5. **Presentation:** Does its length and format preserve important exceptions?

These are **reading checks**, not a scored assessment or mandatory learner assignment.

## 5. Three important interpretations of the narration

Keep the following distinctions in mind while listening:

- **Generating is not the same as looking up facts.** A model can produce text from learned patterns, but modern AI systems *can also* use search, retrieval, tools, and cited sources. Do not interpret “there is no library” as a claim that all AI products lack retrieval.
- **A setting or prompt does not guarantee truth.** Search, reasoning modes, stricter wording, or lower sampling randomness may influence responses; none establishes a missing inspection result. Compare the answer with authoritative evidence.
- **A new chat is a context-management tactic, not a security or verification control.** Depending on the product, it may reduce irrelevant conversation history but cannot remove training limitations, guarantee privacy, or override how connected data and memory are handled.

**Privacy reminder:** The handoff in this guide is fictional. Do not paste confidential operating notes, staff details, or live infrastructure records into an AI tool unless organizational policy and access controls permit it.

## 6. Where this fits in the AB-410 sequence

**Module 01** explained how to choose Power Platform components. **Module 02** teaches how to communicate a task and its evidence boundaries to generative AI. **Module 03** moves to AI-assisted application planning with Power Apps Plans. The later Dataverse, Power Apps, Power Pages, and Power Automate modules cover their own configuration procedures. Detailed prompt building within solutions belongs to its later designated curriculum material—not to this conceptual lesson.

---

**Official learning reference:** [Microsoft Learn — Create effective prompts for generative AI training tools](https://learn.microsoft.com/en-us/training/modules/create-prompts-for-generative-ai-training-tools/)  
**Creator:** [SunnyVerse AI Labs](https://www.youtube.com/@SunnyVerseAILabs) · Independent educational companion · All SunnyVerse operations scenarios and data are fictional.  
**Episode runtime:** Approximately 41:11. YouTube chapter positions may vary slightly.