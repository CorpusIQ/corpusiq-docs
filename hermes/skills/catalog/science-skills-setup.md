---
title: "Science Skills - PubMed, arXiv and Lab Data Setup"
description: "google-deepmind/science-skills: 87.9K combined installs. 40 Google agent skills for paper search, genomics, structural biology and chemistry."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/science-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-30"
tags: ["hermes skill", "agent skill", "skill setup", "bioinformatics", "literature search", "google deepmind"]
---

# Science Skills - Setup Guide

**Source:** [google-deepmind/science-skills](https://www.skills.sh/google-deepmind/science-skills) via skills.sh - 87.9K combined installs across 42 indexed listings; first seen 2026-10-30 (evening sweep)

**GitHub:** [google-deepmind/science-skills](https://github.com/google-deepmind/science-skills) - 3,363 stars, Apache-2.0, branch main, last pushed 2026-10-23; 40 `SKILL.md` files, one per skill under `skills/<skill_name>/`, 36 of them with a `scripts/` directory and 36 with `references/`, alongside `plugin.json` (`name: science`, version 1.3.1) and `SKILL_LICENSES.md` for third party data terms; `uv` and `credentials` are single-file shared skills

**Category:** Scientific research skills for literature search, omics databases, structural biology and chemistry

**Quality Tier:** 🟡 Yellow - Gen Agent Trust Hub and Socket pass every sampled skill while four literature-search skills carry a Snyk Warn, and the whole suite ships under Apache-2.0 from Google DeepMind

Science skills is published by Google DeepMind as a collection of agent skills for scientific research tasks, spanning genomics, structural biology, cheminformatics and literature search. Each skill is a directory holding a `SKILL.md` with structured instructions plus the Python scripts that do the actual work, and the README positions the set as the reference implementation for science work in Google Antigravity, where it runs as the Science plugin. The repository is not an official Google product, but it is maintained in the open under Apache-2.0 and it has the shape of something a lab would actually rely on: 3,363 stars, a versioned plugin manifest, and a separate licences file because several of the data sources it queries impose their own terms.

The authoring style is what makes the suite worth reading even if you only want one skill. Descriptions name the trigger and then name the anti-trigger, so `alphafold-database-fetch-and-analyze` says to ask for a UniProt accession rather than guessing from a gene name, and `foldseek-structural-search` refuses to run on a bare sequence. Retrieval is delegated to bundled scripts executed through `uv`, which keeps JSON out of the model's reasoning path, and the arXiv skill explicitly enforces one request every three seconds inside its own script rather than trusting the agent to pace itself. A dedicated `credentials` skill defines how API keys are checked and requested without the value ever entering the context.

## Installation

The README's primary route is a single skills CLI call:

```bash
npx skills add google-deepmind/science-skills/
```

In Google Antigravity the same set arrives as a plugin instead, and the README treats that as the intended environment:

```text
Customizations > Build with Google > Science > Add
```

The first skill you trigger will ask for approval to install `uv`, the package manager every script runs under, and the README recommends restarting Antigravity after that first install. Keys are expected in `~/.env`:

```bash
echo "ALPHAGENOME_API_KEY=your_actual_api_key" >> ~/.env
```

For a Hermes profile the durable route is a directory copy, because there is no Antigravity plugin host here. Each skill is self contained, so clone once and copy the ones you need with their scripts intact:

```bash
git clone https://github.com/google-deepmind/science-skills.git
cd science-skills
cp -r skills/literature_search_arxiv ~/.hermes/profiles/corpusiq/skills/literature-search-arxiv
cp -r skills/pubmed_database ~/.hermes/profiles/corpusiq/skills/pubmed-database
cp -r skills/credentials ~/.hermes/profiles/corpusiq/skills/credentials
```

The checkout holds 40 skill directories, every one with a `SKILL.md`. Copy `credentials` and `uv` alongside whatever else you install, since several skills check for them before doing anything, and do not edit files inside an Antigravity plugin install directory if you also use that route, because the README notes those changes are overwritten on update.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| literature-search-arxiv | 3,413 | Searching arXiv for papers and preprints, extracting metadata and abstracts, and downloading full-text PDF or HTML with the bundled script enforcing the arXiv request rate. |
| literature-search-openalex | 3,129 | Querying OpenAlex for papers, authors, institutions, topics, publishers and funders, resolving DOIs and aggregating bibliometrics such as citation counts and h-index. |
| pubmed-database | 2,739 | Searching PubMed and its clinical trial literature, fetching abstracts and full text, and linking papers to gene, protein, nucleotide and compound records. |
| literature-search-europepmc | 2,588 | Searching Europe PMC, downloading open-access full texts by PMCID, and pulling citation lists and bibliographies. |
| literature-search-biorxiv | 2,495 | Browsing bioRxiv and medRxiv preprints by DOI or by narrow date range with category and keyword filters. |
| uv | 2,470 | Checking whether the uv package manager is installed, installing it when missing, and putting it on PATH for the other skills. |
| workflow-skill-creator | 2,437 | Distilling a completed workflow or interaction into a reusable skill file, including the plain "make this a skill" request. |
| clinical-trials-database | 2,385 | Searching ClinicalTrials.gov by condition, drug, location, status or phase, reading eligibility criteria, and counting trials across conditions or sponsors. |
| pdb-database | 2,263 | Finding and downloading experimental 3D structures by sequence or structure similarity, and reading structure experiment metadata. |
| alphafold-database-fetch-and-analyze | 2,258 | Fetching AlphaFold predicted structures for a UniProt accession and reading pLDDT confidence, domain boundaries and disorder. |
| pubchem-database | 2,255 | Querying PubChem by name, CID or SMILES for properties, similarity and substructure search, and bioactivity. |
| ncbi-sequence-fetch | 2,246 | Pulling protein and nucleotide sequences from NCBI E-utilities by accession, gene and organism, locus tag, PubMed ID or patent number. |
| pymol | 2,242 | Rendering and analysing protein structures in PyMOL: alignments, distance and contact measurement, binding site highlights, B-factor colouring. |
| openfda-database | 2,236 | Querying openFDA for adverse events, recalls, labelling, approvals, shortages and 510(k) clearances across its 28 API endpoints. |
| alphagenome-single-variant-analysis | 2,222 | Scoring non-coding variant effects on gene expression, chromatin accessibility, histone marks and splicing through the AlphaGenome API. |
| uniprot-database | 2,218 | Protein metadata, function, taxonomy and sequences across UniProtKB, UniParc and UniRef, plus identifier mapping and publication lookups. |
| chembl-database | 2,210 | Querying ChEMBL for bioactive molecules, drug targets, IC50 and Ki values, approved drugs and structure searches. |
| clinvar-database | 2,207 | Reading clinical significance and pathogenicity classifications for human variants, including VUS calls and hard positive benchmark controls. |
| ensembl-database | 2,199 | Resolving gene, transcript and protein IDs, fetching genomic and protein sequences, reading exon structure, and running VEP consequence predictions. |
| opentargets-database | 2,187 | Querying Open Targets for target-disease associations, tractability and safety data, omics evidence and known drugs. |

The remaining 22 indexed listings range from 326 to 2,186 installs.

## Why This Matters for Hermes Agents

An agent asked about a variant, a compound or a paper usually answers from memory, and that is exactly where fabricated citations and invented p-values come from. These skills replace recall with a call to the primary source, and the response comes back as JSON from arXiv, OpenAlex, PubMed, Ensembl, UniProt, PDB or openFDA rather than as a plausible-sounding paragraph.

The routing discipline is the part worth copying into other suites. Each description names the situation that should trigger the skill and often names the sibling that should handle the neighbouring case instead, so an agent holding 40 half-similar retrieval skills still picks the structural search when it is given coordinates and the sequence search when it is given FASTA. Without that, a large suite degrades into whichever skill sorts first.

Every skill keeps the heavy lifting in scripts run through `uv`, and the instructions tell the agent to redirect output to a file and parse it separately. The arXiv skill spells out why: a hundred results will blow past the context window, so limit `--max_results` or paginate. That is the right default for a long-lived profile with a fixed context budget.

Attribution and rate limits are encoded rather than hoped for. The literature skills cap request rates inside their own scripts and require the agent to list the URLs of the papers it used, and 35 of the 40 skills instruct the agent to write a licence acknowledgement file under `.licenses/` in the workspace on first use.

Key handling is centralised in `credentials`, which checks `~/.env` with `grep -sq` so the value never reaches the transcript, and which blocks the calling skill until a missing key is added. For a profile that carries client data, a protocol like that is more useful than a warning in a README.

## Usage

| You say | What happens |
|---|---|
| "Find recent papers on CRISPR off-target prediction and give me the DOIs" | literature-search-openalex queries the OpenAlex API, returns titles, DOIs and citation counts, and can download the open-access PDFs. |
| "What does ClinVar say about this variant, is it pathogenic?" | clinvar-database pulls the clinical significance classification, evidence rationale and review status for the variant, and flags VUS rather than rounding it to a call. |
| "Get the AlphaFold structure for P00533 and tell me how confident it is" | alphafold-database-fetch-and-analyze retrieves the predicted model for that UniProt accession and reports pLDDT confidence plus domain boundaries and disorder regions. |
| "Are there recruiting trials for this drug in Arizona?" | clinical-trials-database queries ClinicalTrials.gov APIv2 by intervention, location and status, then returns the matching NCT IDs and eligibility criteria. |
| "Map this gene symbol to a protein ID and pull the sequence" | ensembl-database resolves the identifier and fetches the sequence, with uniprot-database and ncbi-sequence-fetch covering the cross-references. |
| "Render this structure with the active site highlighted" | pymol loads the structure and writes an image, with the active site residues selected and coloured. |
| "Turn what we just did into a skill we can rerun" | workflow-skill-creator distils the finished interaction into a `SKILL.md` with triggers and steps. |

## Verification

Both raw paths below returned 200 on branch main when this guide was written on 2026-10-30:

```bash
curl -sL -o /dev/null -w "%{http_code} alphafold\n" \
  https://raw.githubusercontent.com/google-deepmind/science-skills/main/skills/alphafold_database_fetch_and_analyze/SKILL.md
curl -sL -o /dev/null -w "%{http_code} alphagenome\n" \
  https://raw.githubusercontent.com/google-deepmind/science-skills/main/skills/alphagenome_atlas_website_links/SKILL.md
```

Expect `200` twice. The same pattern works for any other skill by swapping the directory name, and the directory names use underscores while the `name:` in each frontmatter uses hyphens, so check the tree rather than guessing the URL.

After a copy lands in the profile, confirm the file and the two shared prerequisites:

```bash
ls ~/.hermes/profiles/corpusiq/skills/literature-search-arxiv
head -8 ~/.hermes/profiles/corpusiq/skills/literature-search-arxiv/SKILL.md
uv --version
```

A good copy shows `SKILL.md` beside a `scripts/` directory, frontmatter whose `name:` is `literature-search-arxiv`, and a `uv` version with no traceback. If `uv` is missing, install the `uv` skill first and let it run, because every skill that calls a script assumes it is on PATH.

## Security

skills.sh verdicts for sampled skills (verified 2026-10-30) - re-check the security pages on skills.sh before production use. A Warn is not a failure, but it is not a clean bill either: Snyk flags a skill whose behaviour deserves a read before production use, and here that lands on the four literature-search skills, which are precisely the ones that make outbound HTTP requests and download PDFs.

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| literature-search-arxiv | Pass | Pass | Warn |
| literature-search-openalex | Pass | Pass | Warn |
| pubmed-database | Pass | Pass | Warn |
| literature-search-europepmc | Pass | Pass | Warn |
| science-skills-common | Pass | Pass | Pass |

Read that table for what it is: two auditors returned Pass on every sampled skill, one returned Warn on the four network-facing literature skills and Pass on the shared common skill. The Warn attaches to outbound request behaviour, so treat it as a prompt to read the scripts that fetch, not as a statement that this repository was found to do something specific. Only five of the 42 listings were sampled, so the verdicts describe those five files rather than the suite.

The work itself is outbound API traffic to public research sources, and each skill tells you which. The arXiv skill caps itself at one request every three seconds and asks the agent to cite the URLs it used; several skills write a `.licenses/` acknowledgement file into the workspace on first use, recording that the data source terms were surfaced along with a timestamp. Those terms are not uniform, which is why the repository ships `SKILL_LICENSES.md`: individual skills reference third party data sources with their own licences, and the README puts responsibility for compliance on the user rather than the skill.

Credential handling is the other surface. The `credentials` skill checks for a key with `grep -sq` against `~/.env` and stops the calling skill until the key is present, and the README's own example appends `ALPHAGENOME_API_KEY` to `~/.env` in plain text. That keeps keys out of the transcript, but it does put them in an unencrypted dotfile, so scope those keys and rotate them as you would any other secret.

## Limitations

- Snapshot data, verified 2026-10-30: 87,871 combined installs across 42 indexed listings; 3,363 GitHub stars; Apache-2.0; last pushed 2026-10-23. Counts drift over time.
- The index outruns the tree. skills.sh carries 42 listings while the checkout holds 40 skill directories, and the two extras, `scienceskillscommon` at 699 and `science-skills-common` at 326, match no directory under `skills/`: they look like two spellings of one shared listing rather than two skills to install.
- The counts are not a ranking. The 20 listed skills sit inside a narrow band from 2,187 to 3,413 installs, so the order says almost nothing about which skill is better; `uv` at 2,470 is an installer helper and outranks most of the databases.
- Nothing works without `uv` and a network. Scripts are invoked as `uv run scripts/...` relative to the skill directory, so a copy that lands with the scripts stripped, or an agent whose working directory is elsewhere, fails at the first call. The first run also asks for approval to install `uv`.
- Some skills need keys to be useful. AlphaGenome requires one, while ClinVar, OpenAlex and PubMed run without one at a lower rate limit: the optional `NCBI_API_KEY` lifts PubMed from 3 to 10 requests per second, and a keyless batch run reaches a 429 sooner.
- The suite is authored for Google Antigravity and its Science plugin, and the README states plainly that this is not an official Google product. Skills copied into another harness lose the plugin's own update path and become yours to maintain.

## Related

- [Academic Research Skills - Paper Pipeline for Agents Setup](/hermes/skills/catalog/academic-research-skills-setup)
- [Research Paper Writing Pipeline - Academic ML/AI Paper Production Setup](/hermes/skills/catalog/research-paper-writing-setup)
- [Agent Research Skills - Academic Paper Suite Setup](/hermes/skills/catalog/lingzhi227-agent-research-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install `uv` and `credentials` before anything else. The first skill you trigger will try to install `uv` anyway, and `credentials` is what stops a missing key from becoming a half-finished retrieval run.
- Copy the directories you need rather than all 40. Each skill carries its own scripts, and a narrow set of three or four databases is easier to audit than a whole research stack.
- Read the negative triggers before invoking. Descriptions such as "do not use if the user only has a protein name" exist to route between neighbouring skills, and ignoring them produces confident answers from the wrong tool.
- Put keys in `~/.env` and check them with `grep -sq "^KEY_NAME=" ~/.env` rather than echoing the value, which is exactly the protocol the `credentials` skill codifies.
- Redirect every script to a file and parse it. The arXiv skill warns that 100+ results will exceed the context window, and the same holds for OpenAlex and PubMed result sets.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
