---
title: "ChinaMedVisit MCP - Hospital Prices in China vs US"
description: "A keyless MCP server that puts a priced range and a currency conversion in front of the model instead of an invented number, and substitutes quietly when."

category: "Healthcare / Cost Data"
stars: "0 (remote Streamable HTTP, keyless and stateless; six tools, all six driven)"
added: 2026-11-15
source: "the mcp.so submission queue entry #7414 filed 2026-11-15T02:02:26Z, and a driven session on 2026-11-15 in which all six tools were called over Streamable HTTP, 21 tools/call requests in total"
relevance: ★★★
tags: [healthcare, medical-costs, price-transparency, china, hospitals, medical-tourism, keyless, remote, mcp]
last_updated: "2026-11-15"
---

# ChinaMedVisit MCP

**A price is the one number an assistant will always improvise, and healthcare is where the improvisation costs the most.** Ask a general model what a 3T brain MRI with contrast costs in Shanghai and it will produce a figure with a dollar sign on it and no source. Ask what an executive health screening costs and the answer sounds identical whether the underlying table covers eleven procedures or eleven thousand.

ChinaMedVisit is a small, free, stateless server that answers that question from a fixed table across **eleven** procedures, four currencies of comparison and five Chinese cities, and the reason it earns a page here is not the size of the table. It is that every row carries the RMB range, an explicit conversion rate, the US self-pay average and the UK private rate in the same object, so the arithmetic can be checked by hand rather than trusted.

**The defect is equally worth recording: it does not refuse a bad argument, it substitutes.** Ask for a procedure slug that does not exist and you get the whole-body PET-CT row back with no error marker, and ask for a city that is not covered and you get Beijing's hospitals under a response that prints the city you asked for. Both are covered below with the transcripts.

```
Server type:   remote Streamable HTTP, stateless
Endpoint:      https://chinamedvisit.com/api/mcp
Server:        com.chinamedvisit/mcp, version 1.0.0
Protocol:      2025-06-18
Auth:          none (no key, no account, no OAuth)
Tools:         6 (estimate_china_medical_cost, lookup_tier3a_international_hospital,
               get_medical_tourism_itinerary_plan, get_bilingual_hospital_phrasebook,
               check_china_medical_visa_and_payment_prep, compare_tier3a_imc_vs_private_hospital)
Repository:    https://github.com/AbigailDavised/chinamedvisit-mcp
Website:       https://chinamedvisit.com
Listed on:     the mcp.so submission queue as #7414
```

## The evidence tier

**Keyless and driven.** No credential was needed at any point. `initialize` answered **200** as `com.chinamedvisit/mcp` **1.0.0** on protocol **2025-06-18**, `tools/list` returned **six** schemas with closed enums on every required argument, and **21** `tools/call` requests were run: all eleven procedure slugs, three hospital lookups, the itinerary planner at two stay lengths, the phrasebook, the payment and visa check, the comparison tool, and four deliberately wrong calls to see how the server answers an error.

## The tool surface

| Tool | Required argument | Enum | What it returns |
|---|---|---|---|
| `estimate_china_medical_cost` | `procedureId` | 11 procedure slugs | Tier-3A IMC price range in RMB, a USD conversion at 7.2, the US self-pay average, the UK private rate, the savings percentage and the turnaround. |
| `lookup_tier3a_international_hospital` | `city` | Beijing, Shanghai, Guangzhou, Shenzhen, Chengdu | Hospitals with address, switchboard number, specialty focus and accepted payment methods. |
| `get_medical_tourism_itinerary_plan` | `visitPurpose` | 4 purposes, plus `stayDays` | A day-by-day schedule and a dossier checklist. |
| `get_bilingual_hospital_phrasebook` | `scenario` | 5 scenarios | English, Chinese and pinyin cards. |
| `check_china_medical_visa_and_payment_prep` | `paymentMethod` | 4 methods | Payment advice and a visa note. |
| `compare_tier3a_imc_vs_private_hospital` | `priority` | 4 priorities | Two paragraphs comparing public academic IMCs against private international clinics. |

## What the eleven procedures returned, and the check beside each one

Every figure in the middle three columns is the server's own output. The last column is mine, recomputed from the RMB midpoint at the rate the server itself prints.

| Procedure | RMB range | USD at 7.2 | US self-pay | Stated saving | My check |
|---|---|---|---|---|---|
| Chief physician consultation | 300 to 800 | ~$76 | $450 | 83% | 550 / 7.2 = 76.39; (450 - 76) / 450 = 83.1% |
| Pathology second opinion | 600 to 1,800 | ~$167 | $1,500 | 89% | 1,200 / 7.2 = 166.67; 88.9% |
| MDT tumour board | 1,500 to 3,500 | ~$347 | $2,800 | 88% | 2,500 / 7.2 = 347.2; 87.6% |
| Contrast chest CT | 650 to 1,300 | ~$135 | $1,400 | 90% | 975 / 7.2 = 135.4; 90.3% |
| 3T brain MRI with contrast | 1,200 to 2,400 | ~$250 | $2,200 | 89% | 1,800 / 7.2 = 250; 88.6% |
| Painless gastroscopy and colonoscopy | 2,200 to 4,200 | ~$444 | $3,800 | 88% | 3,200 / 7.2 = 444.4; 88.3% |
| Executive health screening | 4,500 to 9,800 | ~$993 | $4,500 | 78% | 7,150 / 7.2 = 993; 77.9% |
| Coronary angiography | 4,500 to 8,500 | ~$903 | $8,200 | 89% | 6,500 / 7.2 = 902.8; 89.0% |
| Knee arthroscopy, meniscus | 18,000 to 32,000 | ~$3,472 | $14,500 | 76% | 25,000 / 7.2 = 3,472.2; 76.1% |
| Whole-body PET-CT | 7,000 to 11,000 | ~$1,250 | $5,800 | 78% | 9,000 / 7.2 = 1,250; 78.4% |
| Total hip arthroplasty | 45,000 to 78,000 | ~$8,542 | $38,000 | 78% | 61,500 / 7.2 = 8,541.67; 77.5% |

**The conversion is the whole method, and it is stated.** Every row prints `at 7.2 RMB/USD` in the answer, so the USD number is a division rather than a coincidence, and the savings figure is computed against the USD midpoint rather than against the top or the bottom of the range. Eleven of eleven reproduce, which is the property that makes a price table quotable at all.

## The hospitals, and what the directory actually contains

`lookup_tier3a_international_hospital` at `city: Beijing` returned **two** entries: PUMCH's International Medical Department at 1 Shuaifuyuan with +86 10 6915 6114, and Beijing Tongren's IMC with ophthalmology as its stated focus. Adding `specialtyFocus: oncology` for Chengdu returned one entry, West China Hospital (Huaxi IMC) at 37 Guoxue Alley. The tool accepts a free-text specialty and filters on it rather than validating it against a list, which is the right shape for a five-city directory and the wrong shape for a promise.

## The itinerary planner, and a stay length that does not shorten the plan

`get_medical_tourism_itinerary_plan` at `oncology_second_opinion` with `stayDays: 5` returned a five-day schedule: fasting bloodwork and passport registration on day one, imaging on day two, an MDT review on days three and four, and the stamped dossier on day five, beside a four-item checklist that names DICOM files on USB and pathology slides.

The same call at `stayDays: 2` returned `recommendedStayDays: 2` and **the same five-day schedule**, day five included. A caller who passes a short window is told the window is fine and handed a plan that does not fit in it. For a planning aid that is the more dangerous of the two defects found here, because the number at the top of the answer reads as a confirmation.

## The two quiet substitutions

**An unknown slug returns somebody else's procedure.** `estimate_china_medical_cost` with `procedureId: colonoscopy`, which is not in the enum, returned **200** with the whole-body PET-CT row, `isError` absent: 7,000 to 11,000 RMB, $1,250, a 78 percent saving, and a Chinese name for an oncology scan. Nothing in the payload says the slug was not recognised. A caller building a cost sheet from a hand-written list would attach a PET-CT price to a colonoscopy and see no warning.

**A missing required argument returns a default, not an error.** Calling the same tool with an empty argument object returned the same PET-CT row with the `procedureId` field simply absent from the response. The schema marks `procedureId` as required, and the server answers regardless.

**An uncovered city is answered with another city's hospitals.** `city: Xian` returned the Beijing pair, in a payload that prints `"city": "Xian"` at the top, so the label and the contents disagree inside one object. Xi'an is not in the enum, and the enum is where a caller finds out it is not covered; nothing at call time enforces it.

Recorded as behaviour, not as a verdict: the fix is a refusal with the valid list, and three of the four error paths measured here would be silent wrong answers in production.

## What the prose tools are worth

`compare_tier3a_imc_vs_private_hospital` returns two paragraphs and no numbers, and the one sentence that carries commercial weight is the second: private international clinics bill **2x to 4x** the public Tier-3A IMC rate and take direct billing from Cigna, Allianz, Bupa and Aetna, while the public IMC takes a passport at the desk and costs less. `check_china_medical_visa_and_payment_prep` at `alipay_wechat_linked` states the fee rule that decides small payments: Alipay waives its 3 percent foreign-card fee under 200 RMB and charges it above. Both are useful to a traveller and neither is a returned data field, so neither is something a model can reconcile against a second source.

## Limits

Eleven procedures, five cities, one conversion rate with no date on it, and a price table with no `asOf` field anywhere in the responses. The UK figures are in pounds sterling with no conversion. The phrasebook covers five scenarios. Nothing here is a quote from a hospital, a billing code or an insurance determination, and the directory is a marketing surface for a medical-tourism operator rather than a registry of licensed facilities.

## FAQ

### Does it need a key or an account?

No. Every call in this guide was made without a credential, and the endpoint is stateless, so no session identifier is issued and none is required.

### Can the numbers be trusted?

The arithmetic inside each row can be checked and does check: eleven of eleven reproduce from the RMB midpoint at the stated 7.2 rate. Whether the underlying ranges are current is a different question, and the server returns no date, so treat the figures as a stated vendor range rather than a verified market price.

### What happens if I pass a procedure it does not know?

It returns the whole-body PET-CT row with a 200 and no error marker. Validate your slug against the enum in `tools/list` before you call, because the server will not do it for you.

### Where does this fit a business?

Self-funded benefit plans, expatriate cover and travel-medical budgeting are the three places where a priced comparison with an explicit conversion beats an improvised estimate, and this is the first entry in this catalog for medical procedure pricing in any currency.

## Related reading

- [External MCP server catalog](/hermes/mcp/servers/external/) for the rest of the servers evaluated and catalogued here
- [CorpusIQ connectors](https://corpusiq.io/connectors) for the read-only business systems this catalog is built around
