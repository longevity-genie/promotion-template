# Japan contacts catalogue

`japan-contacts-catalogue.csv` holds Japanese organisations, companies, researchers,
media, patient communities and funding programmes relevant to promoting Sugar-Sugar
in Japan, specifically in the context of the DWIH Deep Tech Launchpad Japan 2026
(November 21-28, Tokyo and Kansai).

It is **not** a destination list. You do not post into these — you write to them,
meet them, or apply to them. A row with no concrete `suggested_ask` is a bookmark.

Researched 2026-09-02 from web searches in English and Japanese, cross-referenced
with the DWIH Tokyo network partner list and existing project catalogues.

## Columns

| Column | Meaning |
|---|---|
| `jp_id` | Stable slug, prefixed by `jp-`. |
| `name` | Organisation, person or programme name. Japanese name in parentheses where relevant. |
| `type` | `organization` / `company` / `person` / `media` / `community` / `program`. |
| `country` | `JP` for domestic, `US/JP` for foreign companies with Japan offices, `JP/EU` for bilateral programmes. |
| `category` | `professional` / `advocacy` / `research` / `funding` / `industry` / `media` / `creator` / `events`. |
| `language` | Primary language. `ja` / `en` / `ja/en`. Most rows are `ja` — this is the point of the file. |
| `url` | Website or profile URL. |
| `contact` | Email or contact channel where found. Many Japanese organisations use web forms rather than published email. |
| `relevance` | `A` core fit · `B` good · `C` marginal. |
| `why_relevant` | Why this contact matters for Sugar-Sugar specifically. |
| `suggested_ask` | The one concrete thing to ask for. |
| `dwih_angle` | How this contact connects to the DWIH Launchpad trip — geography, programme structure, or partner network. |
| `status` | `uncontacted` / `contacted` / `meeting-scheduled` / `agreed` / `declined`. |
| `notes` | Cross-references, caveats, and verification notes. |

## What the research found

**Japanese diabetes media operates in Japanese.** The patient-facing ecosystem runs
through dm-net.co.jp (糖尿病ネットワーク, online since 1996), the monthly magazine
Sakae (さかえ, published by JADEC), and patient blogger platforms like note.com.
English-language outreach will not reach Japanese patients. The study already has a
Japanese UI gap — adding Japanese to Sugar-Sugar should be considered before the trip.

**Three structural bridges exist between German and Japanese diabetes research:**

1. **EFSD-JDS Reciprocal Travel Research Fellowship** — a bilateral programme that
   funds European diabetes researchers visiting Japan and vice versa. A German PI
   presenting a human-baseline study is the programme's intended use case.

2. **DWIH Tokyo network** — AMED, AIST, JST, JSPS and RIKEN are all listed network
   partners. These are the funding and institutional gatekeepers.

3. **AMED SICORP** — Strategic International Collaborative Research Program with
   active EU joint calls. The most plausible route to funded Japanese collaboration.

**The Kansai leg is where the industry contacts live.** ARKRAY (Kyoto, glucose
monitoring since 1960) and Light Touch Technology (Osaka, non-invasive glucose
sensing venture) are both reachable during the Kansai portion of the trip. LTT is
the closest Japanese parallel to DiaMonTech in the existing CGM manufacturer catalogue
— a deep-tech sensing startup with a commercial incentive to join independent
benchmarking.

**Patient communities cluster around type 1 diabetes.** YOKOHAMA VOX (seminar series
with CGM discussion groups) and Japan IDDM Network (national NPO with 1600 local
groups) are the ground-level recruitment channels. Both operate in Japanese.

**Exercise is the hook in Japan too.** Honma Taiki, the most visible Japanese T1D
lifestyle creator found, is cycling across Japan with diabetes — the same exercise
framing that rates highest in the existing media catalogue for English-language
creators.

## Priority for the DWIH trip (November 21-28)

**Before the trip:**
1. Check EFSD-JDS fellowship eligibility and deadlines
2. Check AMED SICORP open calls for Germany-Japan digital health
3. Pitch an article to dm-net.co.jp and Sakae
4. Contact YOKOHAMA VOX about presenting at a future session
5. Consider adding Japanese to the Sugar-Sugar UI

**During Tokyo (likely Nov 21-24):**
- NCGM meeting (Shinjuku) — J-DREAMS database, research collaboration
- Dexcom Japan office — local research partnerships
- CureApp / Terumo-MICIN — digital therapy ecosystem
- Vitalism Foundation / longevity events if timing aligns

**During Kansai (likely Nov 25-28):**
- ARKRAY headquarters (Kyoto) — glucose monitoring, HCP network
- Kyoto University diabetes department — seminar or guest lecture
- Light Touch Technology (Osaka) — non-invasive sensor benchmarking
- KPUM longevity epidemiology (Kyoto) — if the aging angle is pursued

## Cross-references with existing catalogues

- Dexcom Japan → `dexcom` row in `cgm-manufacturers-catalogue.csv` (global contact)
- Abbott Japan → `abbott` row in `cgm-manufacturers-catalogue.csv` (IIS process)
- Light Touch Technology → analogous to `diamontech` in `cgm-manufacturers-catalogue.csv`
- Japan Diabetes Society → analogous to `diabetes-technology-society-1` in `linkedin-people-catalogue.csv`
- Anton's aging research → `project_enhancement-bio.md` in memory

## Language note

Many rows have `language: ja`. Japanese academic and medical institutions often have
English-capable international affairs offices, but the patient communities, media, and
creator contacts operate almost entirely in Japanese. Draft outreach in Japanese for
patient-facing contacts; English is acceptable for institutional and research contacts
when routed through international affairs departments.
