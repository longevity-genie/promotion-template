---
dest_id: li-grp-ai-genetics
platform: linkedin-group
group_id: 9032464
group_name: "AI and Genetics"
language: en
pillar_id: p00-site
deriv_id:
utm_source: li-grp-ai-genetics
utm_medium: community
utm_campaign: enhbio-site
utm_content: shr-0005
link_used: https://enhancement.bio/?utm_source=li-grp-ai-genetics&utm_medium=community&utm_campaign=enhbio-site&utm_content=shr-0005
suggested_send_time: 2026-08-18T11:00
boost_ok: risky
post_approval_queue: no
media_needed: none - text post with the link in the body
status: pending
platform_msg_id:
permalink:
---

<!-- WHY THIS VARIANT, FOR THIS ROOM
Small but precisely on-topic. This is the one room where the Ask GPT / Ask Claude integration is the lead rather than a footnote, and the ask is an invitation to break it, which suits a technical audience better than an invitation to admire it. No admin approval queue.

HOW IT GETS SENT: by hand or by a browser agent in a logged-in session. There is no
LinkedIn Groups API and no scheduler can reach a group composer. See
registry/linkedin-groups-catalogue.README.md.
-->

We put Ask GPT and Ask Claude buttons on every gene page of an open enhancement-genetics knowledgebase. I would like people here to try breaking them: where does the model wander away from the sources?

The underlying data are 136 genes from 72 source species, 1,134 experimental records, 973 DOI-linked references and 751 registered clinical trials, held in nine relational tables synced from DoltHub. Each claim carries a rating for how far up the translational ladder it got - cell line, model animal, primate, human trial or market - with split ratings where confidence in the mechanism differs from confidence in the intervention.

That structure is the reason the assistants are worth testing. Asked about Dsup, the model has the evidence rung, the tissue and the DOI in front of it. It can give the uncomfortable answer - protective in human kidney cells, damaging in rat cortical neurons - instead of smoothing the contradiction away. Grounding a model on a curated evidence ladder is different from grounding it on abstracts, and I do not think we have the boundary right yet.

Open under MIT if you want the schema. There is a character generator on top with a 100-credit budget, which is how most people end up reading the entries at all.

https://enhancement.bio/?utm_source=li-grp-ai-genetics&utm_medium=community&utm_campaign=enhbio-site&utm_content=shr-0005

If you build retrieval over biomedical data and can tell me where this approach fails, I would like to hear it.
