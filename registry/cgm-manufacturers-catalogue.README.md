# CGM manufacturers catalogue

`cgm-manufacturers-catalogue.csv` is the outreach reference for the companies that
make the sensors Sugar-Sugar reads. It is **not** an audience and not a posting
destination. What these rows buy is different from what a community row buys:
free sensor hardware, API and parser access, anonymised trace data, and co-authored
validation - and, further out, a manufacturer with a reason to cite the study.

Extracted 2026-08-27 from `temp/CGM Manufacturers Outreach Overview.pdf`, a
Sugar-Sugar-specific market and contact analysis. Every email and portal in this file
comes from that report; none was guessed. Verify an address before a first send -
corporate mailboxes churn.

## Columns

| Column | Meaning |
|---|---|
| `mfr_id` | Short stable slug. |
| `name`, `country` | Company and where it operates from. |
| `tier` | `1` market leaders · `2` established specialists · `3` fast-scaling Asian manufacturers · `4` pre-commercial non-invasive R&D. |
| `market_share` | Range from the source report, or its R&D stage. |
| `products` | Flagship platforms, sensing method, wear period. |
| `reachability` | The report's own rating, `Very Easy` to `Hard`. This is the column to sort by. |
| `contact_emails` | Named mailboxes, with what each one is for. |
| `portals` | Developer portals, grant portals, corporate sites. |
| `why_relevant` | Why this company connects to Sugar-Sugar specifically. |
| `suggested_ask` | The concrete thing to ask for. |
| `phase` | Which outreach phase the source report places it in. |
| `status` | `uncontacted` / `contacted` / `partner` / `declined`. |

## Reachability is inverse to market share, and that is the whole strategy

The three companies with 80%+ of the market between them are the three hardest to
reach. Abbott filters everything that is not an Investigator-Initiated Study
submission; Medtronic routes unsolicited digital-health contact through a review
committee. Meanwhile the manufacturers rated **Very Easy** - Sibionics, DiaMonTech,
Afon, Know Labs - answer from the founding team within days, because independent
benchmarking is worth more to them than to the incumbents.

So the order of approach matters more than the size of the target:

**Phase 1, weeks 1-4 — the open doors.**
- **Sibionics** runs a standing Research Fund that explicitly invites AI and digital-health
  researchers to apply for in-kind sensors, reviewed by a three-person panel. It is the
  single best first contact in this file: lowest friction, highest fit, and it produces
  free hardware.
- **Dexcom**'s developer portal gives instant sandbox credentials with no pre-approval.
  Note the architecture: Dexcom enforces a retrospective delay on glucose values (1h US,
  3h international) precisely to stop third parties making real-time clinical decisions.
  Sugar-Sugar evaluates retrospective traces, so it fits inside that rule rather than
  against it - say so explicitly in the first email.
- **Know Labs** maintains a `trials@` mailbox created to intake exactly this kind of
  proposal. **DiaMonTech** (German, which pairs with the Rostock affiliation), **Afon**
  and **PKvitality** (EU Horizon funded, so a plausible co-applicant) are the same shape.

**Phase 2, weeks 4-12 — the formal submissions.** Abbott's IIS process, Roche, i-SENS,
Sinocare. Abbott's financial grant round closes 15 September each year, but non-financial
support - sensors, anonymised data, trace collaboration - is reviewed continuously, which
is the door to use.

**Phase 3, months 3-6 — the enterprises.** Medtronic's ISR committee, and deeper parser
work with Medtrum alongside the open-source community.

## The two strongest strategic fits

**Roche** built Accu-Chek SmartGuide Predict with IBM: an ML app that forecasts glucose
trends and impending hypoglycaemia. Sugar-Sugar's entire thesis is establishing the human
baseline those models should be measured against. That is not a generic pitch - it is the
same problem from the other side.

**Medtronic**, for the same reason in a harder package: benchmarking human forecasting
error against the MiniMed 780G predictive Auto-Basal algorithm.

## Cross-references

Medtrum and MicroTech both connect to communities already in this registry - Medtrum
through Nightscout and AndroidAPS integrations (see the Telegram catalogue), MicroTech
through the LinX CGM user group in the Facebook catalogue. Roche has a Romanian arm
(accu-chek.ro) worth pairing with the Romanian outreach.

---

## Second source, merged 2026-08-28

A second report — `temp/Global CGM Manufacturer Landscape and Outreach Assessment for
the Sugar-Sugar Study.pdf` — was merged in. It adds three manufacturers, corrects one
fact, sharpens the market-share figures, and contributes the outreach doctrine below,
which is the more valuable half.

**Three companies added:** Infinovo Medical (Glunovo), whose traces appear in recent
randomised accuracy studies; Biolinq, whose Shine patch carries an integrated display and
needs no phone — interesting precisely because it changes what a user *sees*, in a study
about what users can predict; and Glucotrack, investigational only and listed mainly so
it is not rediscovered as a lead.

**One correction that matters.** The first report described Senseonics as "partnered with
Ascensia". Ascensia handed Eversense commercialisation back to Senseonics in January 2026.
Contact Senseonics directly; do not assume Ascensia is still the gatekeeper.

**Companies that look like manufacturers and are not.** Ascensia (former distributor),
A. Menarini Diagnostics (European registration and distribution partner for Sinocare),
GlucoRx AiDEX (a retail rebrand of the MicroTech platform), Trinity Biotech/WaveForm,
Allez Health, and Sony (contract manufacturing for Afon). None gets a row. Where a retail
brand appears, identify the underlying manufacturer and file format rather than
double-counting.

## Keep the ask small

The single most useful thing in the second report is how modest the request should be. A
manufacturer does not need to become a sponsor, hand over identifiable patient data,
expose a private cloud API, or endorse any finding. A workable collaboration is three
things:

1. validating how users can export their own CGM histories;
2. a synthetic or de-identified example file and a data dictionary, for parser testing;
3. circulating an ethics-approved study invitation through their patient or HCP channels.

**Frame it differently depending on whether the format is already supported.** Sugar-Sugar
already reads Dexcom, Libre, Medtronic and Nightscout. For those, lead with participant
recruitment and export validation — never "please integrate your CGM", which asks them for
work. For unsupported manufacturers, lead with format compatibility: it is a concrete
technical deliverable with an obvious benefit to their own users.

Per-company wording that the report calls out specifically: for **Roche**, state plainly
that Sugar-Sugar measures human prediction and is not evaluating SmartGuide Predict's
proprietary algorithms. For **Medtronic**, ask only for the CGM trace and export layer.
For **Sinocare**, coordinate European recruitment with Menarini where its exclusive
reimbursed-market rights apply.

## Do not put Abbott, Dexcom and Medtronic in a room together

This is a real hazard, not a formality. Abbott manufactures the Instinct CGM for MiniMed
while competing with Medtronic in standalone CGM, and Dexcom's 2025 reporting continued to
carry Abbott-related patent-litigation expenditure. Convening the three as one consortium
invites the reading that participation endorses a competitor or accepts comparative
marketing claims.

Send **separate bilateral invitations, on identical terms**, and publish a device-neutral
collaboration policy alongside them. State in the opening message that no manufacturer
ranking or sensor-accuracy comparison is intended.

## The two reports disagree on who to contact first

Worth knowing, because the disagreement is about strategy rather than fact.

- The **first** report sequences by *openness*: Sibionics first, because its Research Fund
  is a standing invitation that yields free sensors, then Dexcom's self-service developer
  portal and the non-invasive startups.
- The **second** sequences by *reach*: Abbott, Dexcom, Medtronic, Senseonics, Roche and
  Sinocare first, on the grounds that the top three cover nearly 97% of 2025 shipments.
  Its second wave is MicroTech, SIBIONICS, Medtrum, i-SENS, Infinovo and POCTech/Yuwell.

Both are defensible and they are not exclusive. The Sibionics application costs an
afternoon and can run in parallel with the formal submissions, which take weeks to be
read. The `phase` column follows the first report's sequencing; treat the second report's
ranking as the priority order *within* a phase.

## Treat the market shares as ordering, not measurement

The 52.83% / 33.89% / 10.10% figures are attributed to Mordor Intelligence's 2025 shipment
analysis. Every smaller figure is an analytical bound derived from the 3.18% residual and
public commercial reach. They are fit for deciding who to email first and for nothing else
— not investment valuation, not antitrust or market-definition work.
