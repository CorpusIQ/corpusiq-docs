#!/usr/bin/env python3
"""Fail closed on unscoped public data-retention claims.

The public contract is intentionally narrower than "we store nothing": direct
MCP requests fetch live, raw customer files and full connector response payloads
are not retained, and direct MCP does not build embeddings or file indexes.
Operational logs can retain query text, per-user tool-call metadata, and bounded
outcome summaries for up to 30 days. Optional indexed search and compliance
receipts have separate lifecycles.
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent

ADDITIONAL_BLANKET_PATTERN = re.compile(
    r"\bno(?:\s+(?:financial|business|customer|client|source|raw)){0,3}\s+data\s+"
    r"(?:is\s+)?(?:\w+[, ]+){0,5}"
    r"(?:stored|persisted|retained|cached|kept|saved)\b|"
    r"\b(?:CorpusIQ|we|they|servers?)?\s*"
    r"(?:stores?|retains?|keeps?|saves?|caches?)\s+no\s+"
    r"(?:customer\s+|business\s+)?"
    r"(?:data|information|content|records?|results?)\b|"
    r"\b(?:customer|business|client|financial)\s+data\s+(?:is|are)\s+"
    r"never\s+(?:kept|saved)\b|"
    r"\b(?:we|CorpusIQ|they|servers?)\s+do(?:es)?\s+not\s+"
    r"(?:save|keep|store|persist|retain|cache)\s+"
    r"(?:data|information|content|records?|results?)\b|"
    r"\b(?:we|CorpusIQ|they|servers?)\s+don['’]t\s+"
    r"(?:save|keep|store|persist|retain|cache)\s+anything\b|"
    r"\b(?:customer\s+|business\s+)?records?\s+(?:is|are)\s+not\s+"
    r"written\s+to\s+disk\b|"
    r"\b(?:your\s+|customer\s+|business\s+)?data\s+exists?\s+only\s+"
    r"in\s+(?:the\s+)?context\s+window\b|"
    r"\bdata\s+is\s+deleted\s+immediately\s+after\s+"
    r"(?:each|the)\s+response\b|"
    r"\bno\s+(?:data\s+)?storage\b"
    r"(?!\s+(?:cost|to\s+provision)|-tenet)|"
    r"\b(?:data|content|results?|payloads?)?[^.\n]{0,50}"
    r"\bgone\s+after\s+(?:the\s+)?response\b|"
    r"\btransient\s+processing\s+only\b|"
    r"\bno\s+(?:embedding|secondary\s+data)\s+store\b|"
    r"\b(?:audit\s+)?logs?[^.\n]{0,60}\bcontains?\s+no\s+"
    r"(?:business\s+|customer\s+)?data\b|"
    r"\bno\s+data\s+movement\b|"
    r"\bno\s+(?:data\s+)?(?:copies|duplication)\b|"
    r"\bdelete\s+all\s+(?:user\s+|associated\s+|customer\s+)?data\b|"
    r"\bpermanently\s+(?:deletes?|deleted|removes?|removed)\s+all\s+"
    r"(?:user\s+|associated\s+|customer\s+)?(?:data|information)\b|"
    r"\ball\s+(?:user\s+|associated\s+|customer\s+)?data\s+"
    r"(?:has|have|is|are)\s+(?:been\s+)?permanently\s+"
    r"(?:deleted|removed)\b|"
    r"\bfull\s+deletion\b[^.\n]{0,50}\bno\s+waiting\s+period\b",
    re.IGNORECASE,
)

# Each expression identifies an unscoped, blanket public promise. Keep these
# intentionally explicit: widening this list must not turn unrelated uses of
# words such as "discard" into retention-policy failures.
FORBIDDEN_PATTERNS: tuple[tuple[str, re.Pattern[str]], ...] = (
    (
        "unsupported regional residency guarantee",
        re.compile(
            r"\b(?:keeping\s+)?data\s+processing\s+"
            r"(?:stays?|remains?|staying|within)\s+regional\s+boundaries\b|"
            r"\bdata\s+processing\s+must\s+stay\s+within\s+specified\s+geographic\s+boundaries\b|"
            r"\bquer(?:y|ies)\b[^.\n]{0,120}\bmust\s+be\s+processed\s+by\s+infrastructure\s+in\s+the\s+(?:EU|US|APAC)\b|"
            r"\bquer(?:y|ies)\b[^.\n]{0,120}\bprocessed\s+by\s+infrastructure\s+in\s+that\s+region\b",
            re.IGNORECASE,
        ),
    ),
    (
        "unsupported public webhook contract",
        re.compile(
            r"\bCorpusIQ\s+(?:webhooks?\s+notify|can\s+send\s+HTTP\s+callbacks?)\b|"
            r"\bCorpusIQ\s+(?:sends?|delivers?|retries?)\b[^.\n]{0,100}\bwebhook|"
            r"\b(?:all|every)\s+webhook\s+deliver(?:y|ies)\s+(?:is|are)\s+signed\b|"
            r"\bfailed\s+deliveries\s+(?:are\s+)?retried\b|"
            r"\bSettings\s*(?:→|->)\s*Webhooks\b|"
            r"\bCorpusIQ\s+Webhooks\b[^.\n]{0,120}\b(?:event\s+notifications?|HMAC)\b|"
            r"\bCorpusIQ-Signature\b[^.\n]{0,100}\b(?:header|HMAC-SHA256)\b|"
            r"\bHMAC[- ]signed\s+(?:tool\s+)?responses?\b|"
            r"\bCorpusIQ\b[^.\n]{0,100}\bHMAC\s+signatures?\b",
            re.IGNORECASE,
        ),
    ),
    ("additional blanket lifecycle claim", ADDITIONAL_BLANKET_PATTERN),
    (
        "zero/no data storage",
        re.compile(
            r"\b(?:zero|no)\s+(?:persistent\s+)?"
            r"(?:customer\s+|business\s+)?"
            r"(?:data|document|file|message|content)\s+"
            r"(?:is\s+)?(?:storage|stored|persistence|retention)\b|"
            r"\bzero(?:-|\s+)(?:file\s+|data\s+)?(?:storage|retention)\b|"
            r"\bdata\s+storage\**\s*\|\s*(?:[^|\n]{0,12})?zero\b",
            re.IGNORECASE,
        ),
    ),
    (
        "blanket no persistent storage",
        re.compile(r"\bno\s+persistent\s+(?:copy|storage)\b", re.IGNORECASE),
    ),
    (
        "never/does-not store or persist",
        re.compile(
            r"\bnever\s+(?:stores?|stored|persists?|persisted|retains?|retained|"
            r"caches?|cached|copy|copies|copied)\b|"
            r"\b(?:does|do)\s+not\s+(?:stores?|persist|retain|cache|copy)\b|"
            r"\bdoesn['’]t\s+(?:store|persist|retain|cache|copy)\b|"
            r"\b(?:CorpusIQ|we|they|MCP\s+servers?|connectors?)\s+"
            r"don['’]t\s+(?:store|persist|retain|cache|copy)\b|"
            r"\b(?:data|content|messages?|records?|results?|responses?|emails?|files?|"
            r"business data|customer data|crm data|financial data)\s+(?:is|are)\s+"
            r"(?:not|never)\s+(?:stored|persisted|retained|cached|copied)\b|"
            r"\b(?:data|content|messages?|records?|results?|responses?|emails?|files?|"
            r"business data|customer data|crm data|financial data)\s+"
            r"(?:isn['’]t|aren['’]t)\s+"
            r"(?:stored|persisted|retained|cached|copied)\b|"
            r"\b(?:stores?|retains?|caches?|copies?)\s+no\s+"
            r"(?:customer\s+|business\s+)?data\b|"
            r"\bnothing\s+(?:is|was)\s+(?:\w+[, ]+){0,4}"
            r"(?:stored|retained|persisted|cached|warehoused)\b|"
            r"\bnothing\s+(?:is|was)\s+copied\b|"
            r"\bnever\s+(?:\w+\s+){1,5}or\s+"
            r"(?:stores?|retains?|persists?|caches?|copies?)\b",
            re.IGNORECASE,
        ),
    ),
    (
        "not persisted",
        re.compile(
            r"\b(?:does|do)\s+not\s+persist\b|\bnot\s+(?:be\s+)?persisted\b",
            re.IGNORECASE,
        ),
    ),
    (
        "store nothing/nothing stored",
        re.compile(
            r"\b(?:stores?|stored)\s+nothing\b|"
            r"\bnothing\s+(?:is\s+)?(?:stored|persisted|retained|cached|written)\b",
            re.IGNORECASE,
        ),
    ),
    (
        "unscoped discarded payload",
        re.compile(
            r"\b(?:data|content|messages?|records?|results?|responses?|query results?|"
            r"business data|customer data|crm data|financial data)\b"
            r"[^\n.!?]{0,120}\bdiscarded\b|"
            r"\bdiscarded\s+(?:immediately|after|once|when)\b",
            re.IGNORECASE,
        ),
    ),
    (
        "data never leaves",
        re.compile(r"\bdata\s+never\s+leaves\b", re.IGNORECASE),
    ),
    (
        "storage table claims none",
        re.compile(r"\bstorage\s*\|[^|\n]*\bnone\b", re.IGNORECASE),
    ),
    (
        "blanket no answer to storage question",
        re.compile(
            r"(?:does|do|is|are)[^?\n]{0,120}\b(?:store|stored|storage|retain)"
            r"[^?\n]*\?(?:[^\n]{0,80}\n\s*|[^A-Za-z0-9\n]{0,80})"
            r"(?:A:\s*)?\**No\.",
            re.IGNORECASE,
        ),
    ),
    (
        "zero or none retained",
        re.compile(
            r"\b(?:we|CorpusIQ|the\s+(?:service|platform))?\s*"
            r"(?:retain|save|keep|store|hold)s?\s+"
            r"(?:zero|no|none\s+of)\s+(?:your\s+|customer\s+|business\s+)?"
            r"(?:data|information|content|records?|results?)\b",
            re.IGNORECASE,
        ),
    ),
    (
        "never touches durable storage",
        re.compile(
            r"\b(?:customer\s+|business\s+|your\s+)?"
            r"(?:data|information|content|records?|results?|responses?)\s+"
            r"never\s+(?:touch(?:es)?|reach(?:es)?|hit(?:s)?)\s+"
            r"(?:the\s+)?(?:disk|storage|database)\b",
            re.IGNORECASE,
        ),
    ),
    (
        "response erased after use",
        re.compile(
            r"\b(?:the\s+)?(?:data|information|content|records?|results?|responses?)\s+"
            r"(?:disappears?|vanishes?|is\s+erased|is\s+destroyed)\s+"
            r"(?:immediately\s+)?after\s+(?:answering|the\s+(?:answer|response)|each\s+request)\b|"
            r"\b(?:we|CorpusIQ)\s+(?:erase|destroy|delete)s?\s+every\s+"
            r"(?:customer\s+)?(?:record|result|response|payload)\s+after\s+answering\b",
            re.IGNORECASE,
        ),
    ),
    (
        "no second copy or duplicate",
        re.compile(
            r"\bno\s+(?:second|additional|separate|duplicate)\s+"
            r"(?:copy|copies|replica|record)\b|"
            r"\bwithout\s+(?:creating|making)\s+(?:a\s+)?"
            r"(?:second|additional|separate|duplicate)\s+copy\b|"
            r"\bdata\s+stays?\s+(?:in|within|at)\s+(?:the\s+)?"
            r"(?:source|source\s+system|vendor|tenant|account|systems?|platforms?)\b|"
            r"\b(?:your\s+|customer\s+|business\s+|store\s+|CRM\s+|project\s+|"
            r"Jira\s+|Shopify\s+|QuickBooks\s+)?data\s+stays?\s+in\s+"
            r"(?!the\s+(?:EU|US|APAC)\b|region\b|[A-Z]{2}\s+region\b)"
            r"(?:[A-Z][A-Za-z0-9.]+|your\s+(?:systems?|platforms?))\b|"
            r"\b(?:there(?:'|’)s\s+)?no\s+(?:copy|duplicate\s+data)\s+to\b|"
            r"\bwithout\s+data\s+duplication\b",
            re.IGNORECASE,
        ),
    ),
    (
        "retention table claims none",
        re.compile(
            r"\bretention\s*\|[^|\n]{0,40}\b(?:none|zero|n/?a)\b",
            re.IGNORECASE,
        ),
    ),
    (
        "blanket no answer to retention question",
        re.compile(
            r"(?:is|are|does|do)[^?\n]{0,140}\b(?:data|content|records?|results?)\b"
            r"[^?\n]{0,80}\b(?:retained|stored|saved|cached|copied)\b[^?\n]*\?"
            r"(?:[^\n]{0,100}\n\s*|[^A-Za-z0-9\n]{0,100})(?:A:\s*)?\**No\b",
            re.IGNORECASE,
        ),
    ),
    (
        "scoped claim with blanket suffix",
        re.compile(
            r"\b(?:doesn['’]t|does\s+not)\s+retain\s+raw\s+customer\s+files?\s+or\s+"
            r"full\s+connector\s+response\s+payloads?[^.\n]{0,100}?"
            r"(?:,\s*)?\b(?:or|and)\s+(?:anything|nothing)\s+else\b|"
            r"\b(?:doesn['’]t|does\s+not)\s+retain\s+raw\s+customer\s+files?\s+or\s+"
            r"full\s+connector\s+response\s+payloads?[^.\n]{0,80}"
            r"\bkeeps?\s+nothing\s+else\b|"
            r"\b(?:doesn['’]t|does\s+not)\s+retain\s+raw\s+customer\s+files?\s+or\s+"
            r"full\s+connector\s+response\s+payloads?[^.\n]{0,80}"
            r"\bnothing\s+else\s+(?:is\s+)?(?:stored|retained|saved|cached|copied)\b|"
            r"\b(?:doesn['’]t|does\s+not)\s+retain\s+raw\s+customer\s+files?\s+or\s+"
            r"full\s+connector\s+response\s+payloads?[^.\n]{0,100}"
            r"\bno\s+other\s+(?:data|information|content|records?|files?|results?)\s+"
            r"(?:remains?|persists?|is\s+(?:stored|retained|saved|cached))\b",
            re.IGNORECASE,
        ),
    ),
    (
        "ephemeral blanket",
        re.compile(
            r"\bephemeral\s+(?:by\s+design|access|processing|queries?|responses?)\b",
            re.IGNORECASE,
        ),
    ),
    (
        "unqualified model-training guarantee",
        re.compile(
            r"\bprevents?\s+(?:the\s+)?model\s+training\s+on\s+customer\s+data\b|"
            r"\b(?:the\s+architecture|the\s+service|CorpusIQ)\s+prevents?\s+"
            r"model\s+training\s+on\s+customer\s+data\b|"
            r"\b(?:CorpusIQ|we)\s+(?:never|do(?:es)?\s+not)\s+train(?:s)?\s+"
            r"(?:models?\s+)?on\s+(?:your|customer|business)\s+data\b|"
            r"\b(?:your|customer|business)\s+(?:data|information|content)\s+"
            r"never\s+trains?\s+(?:a|the|any)?\s*models?\b|"
            r"\bno\s+customer\s+content\s+enters?\s+(?:model\s+)?training\b|"
            r"\b(?:your|customer|business)?\s*records?\s+(?:does|do)\s+not\s+"
            r"feed\s+(?:any\s+)?models?\b|"
            r"\b(?:CorpusIQ|we)\s+(?:do\s+not|don['’]t|never)\s+learns?\s+from\s+"
            r"(?:your|customer|business)\s+(?:data|content|information)\b|"
            r"\b(?:your|customer|business)\s+(?:data|content|information)\s+"
            r"(?:is|are)\s+never\s+used\s+to\s+improve\s+models?\b|"
            r"\b(?:your|customer|business)\s+prompts?\s+(?:is|are)\s+excluded\s+"
            r"from\s+(?:model\s+)?training\b",
            re.IGNORECASE,
        ),
    ),
    (
        "SOC 2 certification overclaim",
        re.compile(
            r"\bSOC\s*2\*{0,2}\s*(?:\|\s*)?(?:compliant|certified|ready|attestation|attested)\b|"
            r"\bSOC\s*2\s+Type\s*(?:II|2)\s+(?:certified|attested)\b|"
            r"\bSOC\s*2\s+(?:audited|verified|assured|approved)\b",
            re.IGNORECASE,
        ),
    ),
    (
        "immediate deletion overclaim",
        re.compile(
            r"\bimmediate\s+deletion\s+endpoint\b|"
            r"\b(?:all|every)\s+(?:customer\s+|user\s+)?"
            r"(?:data|information|records?)\s+(?:is|are)\s+deleted\s+immediately\b|"
            r"\b(?:customer\s+|user\s+|your\s+)?(?:data|information|records?)\s+"
            r"(?:is|are)\s+(?:purged|erased|deleted|removed)\s+instantly\b|"
            r"\b(?:customer\s+|user\s+|your\s+)?(?:data|information|records?)\s+"
            r"(?:is|are)\s+erased\s+as\s+soon\s+as\s+(?:the\s+)?response\s+completes\b|"
            r"\b(?:your\s+)?data\s+is\s+gone\s+the\s+moment\s+(?:the\s+)?"
            r"(?:answer|response)\s+is\s+returned\b|"
            r"\b(?:customer\s+|user\s+|your\s+)?(?:data|information|records?)\s+"
            r"(?:is|are)\s+removed\s+without\s+delay\b|"
            r"\b(?:customer\s+|user\s+|your\s+)?(?:data|information|records?)\s+"
            r"(?:is|are)\s+wiped\s+immediately\b|"
            r"\bclosing\s+(?:the|your|an)\s+account\b[^.\n]{0,80}"
            r"\b(?:removes?|deletes?|erases?|purges?)\s+(?:every|all)\s+"
            r"(?:trace|traces|record|records|data|information)\b",
            re.IGNORECASE,
        ),
    ),
    (
        "expanded lifecycle and boundary semantics",
        re.compile(
            r"\b(?:zero|no|not\s+a\s+single)\s+(?:customer\s+|business\s+)?"
            r"records?\s+(?:is|are)\s+retained\b|"
            r"\b(?:we|CorpusIQ|the\s+(?:service|platform))\s+retain(?:s)?\s+"
            r"absolutely\s+no\s+(?:customer\s+|business\s+)?records?\b|"
            r"\b(?:we|CorpusIQ|the\s+(?:service|platform))\s+save(?:s)?\s+none\b|"
            r"\bretention\*{0,2}\s*:\*{0,2}\s*(?:\*{0,2})?(?:none|zero|n/?a)\b|"
            r"\b(?:request|query|response|service)\b[^.\n]{0,80}\bleaves?\s+no\s+"
            r"(?:customer\s+|business\s+)?records?\s+behind\b|"
            r"\b(?:service|platform|CorpusIQ|we)\s+writes?\s+nothing\s+to\s+disk\b|"
            r"\b(?:source|source\s+system|vendor)\s+remains?\s+the\s+only\s+copy\b|"
            r"\b(?:the\s+)?data\s+stays?\s+where\s+it\s+is\b|"
            r"\b(?:customer\s+|business\s+)?(?:data|content|information|PHI)\s+"
            r"never\s+(?:leaves?|crosses?)\s+(?:the\s+)?"
            r"(?:corporate|secure|customer|network|tenant)\s+boundary\b|"
            r"\ball\s+data\s+processing\s+(?:remains?|stays?)\s+in\s+"
            r"(?:your\s+)?(?:Microsoft\s+365\s+)?(?:region|tenant|boundary)\b|"
            r"\b(?:is|are|does|do)\s+[^?\n]{0,140}\b(?:data|content|records?|results?)\b"
            r"[^?\n]{0,100}\b(?:retained|stored|saved|cached|copied)\b[^?\n]*\?"
            r"[^A-Za-z0-9\n]{0,40}(?:A:\s*)?\**No\b|"
            r"\b(?:CorpusIQ|we|the\s+(?:service|platform))\s+maintains?\s+zero\s+"
            r"(?:customer\s+|business\s+)?records?\b|"
            r"\bno\s+(?:customer\s+|business\s+)?records?\s+remain(?:s)?\s+after\s+"
            r"(?:the\s+)?(?:request|query|response|answer)\b|"
            r"\bretention\s+period\s*:\s*(?:0|zero)\s+"
            r"(?:seconds?|minutes?|hours?|days?)\b|"
            r"\bstored\s+duration\s*:\s*(?:none|zero|0)\b|"
            r"\b(?:customer\s+|business\s+)?data\s+(?:is|are)\s+kept\s+for\s+"
            r"(?:zero|0)\s+(?:seconds?|minutes?|hours?|days?)\b|"
            r"\b(?:customer\s+|business\s+)?(?:data|content|information|records?)\s+"
            r"(?:is|are)\s+(?:retained|stored|saved|kept)\s+for\s+(?:zero|0)\s+"
            r"(?:seconds?|minutes?|hours?|days?)\b|"
            r"\bnothing\s+survives?\s+between\s+(?:requests?|queries|responses?)\b|"
            r"\b(?:request|query|response)\s+leaves?\s+no\s+(?:data\s+)?trace\b|"
            r"\b(?:customer\s+|business\s+)?(?:data|information|content|records?)\s+"
            r"(?:is|are)\s+never\s+persisted\s+anywhere\b|"
            r"\b(?:your\s+|customer\s+|business\s+)?records?\s+remain(?:s)?\s+"
            r"exclusively\s+in\s+(?:the\s+)?(?:source|source\s+system|vendor)\b|"
            r"\b(?:customer\s+|business\s+)?(?:data|content|information)\s+never\s+"
            r"exits?\s+(?:your\s+|the\s+)?(?:tenant|network|environment|region)\b|"
            r"\bprocessing\s+occurs?\s+solely\s+in\s+(?:the\s+)?customer\s+environment\b|"
            r"\bno\s+(?:customer\s+|business\s+)?(?:data|content|information)\s+"
            r"crosses?\s+(?:the\s+)?(?:regional|corporate|tenant|network)\s+boundary\b|"
            r"\b(?:does|do|is|are)\s+[^?\n]{0,140}"
            r"(?:retain|keep|store|save|cache|copy)[^?\n]*\?\s*"
            r"(?:A:\s*)?(?:absolutely\s+not|never)\b|"
            r"\b(?:we|CorpusIQ|the\s+(?:service|platform))\s+preserves?\s+no\s+"
            r"(?:customer\s+|business\s+)?(?:data|information|content|records?)\b|"
            r"\bnothing\s+(?:is\s+)?(?:remains?|persists?|survives?)\s+"
            r"(?:on|in|within)\s+(?:our|the|CorpusIQ)\s+(?:servers?|systems?|platform)\b|"
            r"\b(?:customer\s+|business\s+|your\s+)?(?:records?|data|information|content)\s+"
            r"remain(?:s)?\s+(?:solely|only|exclusively)\s+in\s+"
            r"(?:the\s+)?[A-Za-z][A-Za-z0-9 ._-]{1,50}\b|"
            r"\b(?:do|does|is|are)\s+[^?\n]{0,100}\b(?:retain|store|keep|save|cache)"
            r"[^?\n]*\?\s*(?:<[^>]+>\s*)*(?:A:\s*)?(?:No|Never|Absolutely\s+not)\b",
            re.IGNORECASE,
        ),
    ),
    (
        "blanket indexing denial",
        re.compile(
            r"\b(?:CorpusIQ|we|MCP(?:\s+servers?)?)\s+(?:does|do)\s+not\s+index\b|"
            r"\b(?:CorpusIQ|we|MCP(?:\s+servers?)?)\s+doesn['’]t\s+index\b|"
            r"\bnothing\s+(?:is\s+)?indexed\b|"
            r"\bno\s+(?:stale\s+)?index(?:es|ing)\b|"
            r"\bthere\s+(?:is|are|isn['’]t|aren['’]t)\s+no\s+indexing\b|"
            r"\bthere(?:'|’)s\s+no\s+indexing\b",
            re.IGNORECASE,
        ),
    ),
    (
        "blanket no answer to lifecycle question",
        re.compile(
            r"\b(?:do|does|is|are)\b[^?\n]{0,140}"
            r"\b(?:retain|retained|keep|kept|persist|saved?|cache|cached|stored?|remain|copy)\b"
            r"[^?\n]{0,100}\?(?:\s|<[^>]+>|[*_—:-]){0,100}"
            r"(?:(?:A|Answer)\s*:\s*)?(?:Absolutely\s+not|Never|No(?:\s*,\s*it\s+does\s+not)?)[!.—,]?",
            re.IGNORECASE | re.DOTALL,
        ),
    ),
)

# The only negative-retention claims this gate permits are explicitly scoped to
# the two payload classes in the canonical direct-MCP disclosure. Optional
# indexed-search and log-retention statements are positive lifecycle claims and
# do not need an exception.
SCOPED_OBJECT = re.compile(
    r"\b(?:raw customer files?|full connector response payloads?)\b",
    re.IGNORECASE,
)


@dataclass(frozen=True)
class Finding:
    path: Path
    line: int
    family: str
    excerpt: str


def _sentence_at(text: str, start: int, end: int) -> str:
    left = max(text.rfind("\n", 0, start), text.rfind(".", 0, start)) + 1
    stops = [pos for pos in (text.find("\n", end), text.find(".", end)) if pos >= 0]
    right = min(stops) if stops else len(text)
    return text[left:right].strip()


def _is_precisely_scoped(sentence: str) -> bool:
    """Allow only raw-file/full-payload negative-retention statements."""
    if not SCOPED_OBJECT.search(sentence):
        return False
    if ADDITIONAL_BLANKET_PATTERN.search(sentence):
        return False
    # A generic blanket promise remains forbidden even if a scoped object is
    # tacked onto the same sentence. Neutral uses of "data" (for example,
    # "secondary-data footprint") do not invalidate an otherwise exact claim.
    blanket = re.search(
        r"\b(?:zero|no)\s+(?:customer\s+|business\s+)?data\s+"
        r"(?:storage|stored|persistence|retention)\b|"
        r"\bzero(?:-|\s+)(?:file\s+|data\s+)?(?:storage|retention)\b|"
        r"\bdata\s+storage\**\s*\|\s*(?:[^|\n]{0,12})?zero\b|"
        r"\bno\s+persistent\s+(?:business\s+|customer\s+)?data\s+storage\b|"
        r"\bdoesn['’]t\s+(?:store|persist|retain|cache|copy)\s+data\b|"
        r"\b(?:CorpusIQ|we|they|MCP\s+servers?|connectors?)\s+"
        r"don['’]t\s+(?:store|persist|retain|cache|copy)\s+data\b|"
        r"\b(?:data|customer data|business data)\s+(?:isn['’]t|aren['’]t)\s+"
        r"(?:stored|persisted|retained|cached|copied)\b|"
        r"\b(?:stores?|retains?|caches?|copies?)\s+no\s+"
        r"(?:customer\s+|business\s+)?data\b|"
        r"\bnever\s+(?:stores?|retains?|persists?|caches?|copies?)\s+"
        r"(?:anything|any\s+data)\b|"
        r"\bnothing\s+(?:is|was)\s+(?:\w+[, ]+){0,4}"
        r"(?:stored|retained|persisted|cached|warehoused)\b|"
        r"\bnothing\s+(?:is|was)\s+copied\b|"
        r"\bnever\s+(?:\w+\s+){1,5}or\s+"
        r"(?:stores?|retains?|persists?|caches?|copies?)\b|"
        r"\b(?:all|any|business|customer|our|your)?\s*data\s+(?:is|are)\s+"
        r"(?:not|never)\s+(?:stored|persisted|retained|cached|copied)\b|"
        r"\b(?:stores?|stored)\s+nothing\b",
        sentence,
        re.IGNORECASE,
    )
    return blanket is None


def _is_repudiated_or_third_party_claim(sentence: str) -> bool:
    plain = re.sub(r"<[^>]+>|[`*_#|]", " ", sentence)
    lower = " ".join(plain.split()).lower()
    return bool(
        re.match(
            r"^(?:avoid\s+(?:saying|the\s+blanket\s+phrase)|do\s+not\s+claim|"
            r"a\s+competitor\s+advertises|the\s+phrase\b[^.]{0,80}\bmust\s+not\s+appear)",
            lower,
        )
    )


def _is_safe_non_retention_control(sentence: str) -> bool:
    """Allow negative wording about write permissions and payment-card scope."""
    plain = re.sub(r"<[^>]+>|[`*_#|]", " ", sentence)
    lower = " ".join(plain.split()).lower()
    return bool(
        re.search(
            r"\bnothing\s+is\s+written\s+back\s+to\s+(?:connected\s+)?tools\b|"
            r"\b(?:we|corpusiq)\s+do(?:es)?\s+not\s+store\s+"
            r"(?:card\s+numbers?|full\s+payment\s+details?|"
            r"card\s+numbers?\s+or\s+full\s+payment\s+details?)\b",
            lower,
        )
    )


def _is_safe_soc2_context(sentence: str) -> bool:
    plain = re.sub(r"<[^>]+>|[`*_#|]", " ", sentence)
    lower = " ".join(plain.split()).lower()
    return bool(
        re.search(
            r"\bsoc\s*2\s+aligned\b|"
            r"\b(?:prepar(?:ing|e)\s+for|pursuing|work\s+toward|roadmap\s+includes\s+work\s+toward)\s+"
            r"soc\s*2\s+certification\b|"
            r"\bsoc\s*2\s+(?:type\s*(?:ii|2)\s+)?compliance\s+"
            r"(?:program\s+initiated|in\s+progress)\b|"
            r"\bwithout\s+claiming\s+(?:a\s+)?completed\s+soc\s*2\b|"
            r"\b(?:must|should)\s+hold\b[^.]{0,100}\bsoc\s*2\b|"
            r"\bis\s+mcp\s+compliant\s+with\s+regulations\s+like\s+soc\s*2\b|"
            r"\b(?:not\s+certified|certification\s+is\s+not\s+claimed|"
            r"does\s+not\s+claim\s+(?:soc\s*2\s+)?certification)\b",
            lower,
        )
    )


def _broad_semantic_family(sentence: str) -> str | None:
    """Catch paraphrased public guarantees without a phrase allowlist.

    The explicit regex matrix above gives precise diagnostics for known claims.
    This second layer works from semantic ingredients (object + lifecycle/action
    + negation/exclusivity) so simple rewording cannot turn the gate green.
    """
    plain = re.sub(r"<[^>]+>|[`*_#|]", " ", sentence)
    plain = " ".join(plain.split())
    lower = plain.lower()

    # Public docs sometimes quote a bad phrase to reject it or compare another
    # vendor's claim with CorpusIQ's contract. Those are commentary, not a
    # CorpusIQ promise. Keep this exception subject- and intent-specific.
    if _is_repudiated_or_third_party_claim(sentence):
        return None
    if _is_safe_non_retention_control(sentence):
        return None

    # Broad paraphrase families. These patterns intentionally express semantic
    # combinations rather than one approved wording so simple copy edits cannot
    # turn the publication gate green.
    if re.search(
        r"\b(?:leaves?\s+behind\s+not\s+one\s+(?:customer\s+)?record|"
        r"carr(?:y|ies)\s+forward\s+none\s+of\s+(?:your|customer)\s+(?:data|information|content)|"
        r"(?:prompts?|payloads?|request\s+material)\s+(?:expire(?:s)?\s+completely|"
        r"(?:is|are)\s+memory[- ]only|evaporate(?:s)?)|"
        r"clean\s+slate\s+with\s+no\s+prior\s+customer\s+(?:data|content|information)|"
        r"(?:payloads?|data|content)\s+(?:is|are)\s+never\s+durable|"
        r"(?:corpusiq\s+)?systems?\s+(?:is|are)\s+empty\s+of\s+customer\s+records?|"
        r"no\s+customer\s+(?:data|information|content)\s+outlives?\s+(?:a|the)\s+request|"
        r"(?:request|response|answer)\s+has\s+no\s+durable\s+footprint|"
        r"(?:the\s+)?ai\s+leaves?\s+no\s+footprint|"
        r"hold\s+onto\s+neither\s+prompts?\s+nor\s+results?|"
        r"all\s+customer\s+material\s+(?:is\s+)?released\s+when\s+processing\s+finishes|"
        r"zero\s+artifacts?\s+left\s+behind|"
        r"carries?\s+nothing\s+forward\s+from\s+one\s+request\s+to\s+the\s+next|"
        r"blank\s+memory\s+of\s+prior\s+customer\s+content|"
        r"prior\s+query\s+material\s+ceases?\s+to\s+exist|"
        r"no\s+customer\s+material\s+is\s+left\s+behind|"
        r"response\s+cannot\s+outlive\s+the\s+request|"
        r"forgets?\s+every\s+prompt\s+once\s+it\s+answers|"
        r"hold\s+onto\s+none\s+of\s+the\s+customer\s+material|"
        r"all\s+request\s+state\s+dies\s+with\s+the\s+response)\b",
        lower,
    ):
        return "broad semantic retention guarantee"

    if re.search(
        r"\b(?:[a-z][a-z0-9 ._-]{1,40}\s+alone\s+ever\s+holds?\s+(?:your|customer)\s+records?|"
        r"[a-z][a-z0-9 ._-]{1,40}\s+remains?\s+the\s+sole\s+location\s+for\s+"
        r"(?:customer|financial|business)\s+(?:data|information|records?)|"
        r"(?:customer\s+)?(?:data|content|records?)\s+never\s+travels?\s+outside|"
        r"all\s+processing\s+is\s+confined\s+to|"
        r"keeps?\s+every\s+record\s+inside\s+the\s+vendor\s+tenant|"
        r"(?:your|customer)\s+data\s+cannot\s+cross\s+jurisdictional\s+borders?|"
        r"requests?\s+(?:is|are)\s+answered\s+wholly\s+within\s+the\s+system\s+of\s+record|"
        r"only\s+the\s+source\s+application\s+sees\s+the\s+payload|"
        r"phi\s+stays\s+on\s+the\s+hospital\s+network\s+at\s+all\s+times|"
        r"connector\s+output\s+never\s+enters\s+corpusiq\s+infrastructure|"
        r"customer\s+data\s+is\s+geographically\s+confined|"
        r"nothing\s+from\s+your\s+tenant\s+traverses\s+an\s+external\s+service|"
        r"(?:your\s+)?data\s+remains?\s+home\s+in|"
        r"records?\s+never\s+travels?\s+beyond|"
        r"all\s+processing\s+happens?\s+inside\s+your\s+tenant|"
        r"customer\s+content\s+is\s+confined\s+to\s+the\s+original\s+saas\s+account)\b",
        lower,
    ):
        return "broad semantic source-boundary guarantee"

    safe_first_party_training = re.search(
        r"\bcorpusiq\s+does\s+not\s+(?:use\s+customer\s+data\s+to\s+train|"
        r"train\s+models?\s+on\s+customer\s+data)\b[^.]{0,120}\b"
        r"conversation\s+handling\s+(?:follows|is\s+governed\s+by)\s+"
        r"(?:the\s+)?(?:selected\s+)?ai[- ]provider(?:['’]s)?\s+"
        r"(?:plan|policy|terms|settings)",
        lower,
    )
    if not safe_first_party_training and re.search(
        r"\b(?:models?\s+(?:learns?\s+nothing|gains?\s+no\s+knowledge|forgets?\s+every)|"
        r"zero\s+learning\s+from\s+(?:customer\s+)?records?|"
        r"(?:customer\s+)?(?:records?|content|data|files?|prompts?|responses?)\s+"
        r"(?:contributes?\s+zero\s+learning\s+signal|cannot\s+influence\s+model\s+weights|"
        r"(?:is|are)\s+excluded\s+from\s+any\s+learning\s+process|"
        r"never\s+improves?\s+an\s+ai\s+system|supplies?\s+no\s+feedback\s+signal|"
        r"cannot\s+be\s+used\s+for\s+fine[- ]tuning|makes?\s+no\s+contribution\s+to\s+model\s+improvement)|"
        r"no\s+model\s+adapts?\s+based\s+on\s+customer\s+messages?|"
        r"ai\s+weights?\s+(?:is|are)\s+untouched\s+by\s+business\s+information|"
        r"no\s+model\s+(?:can\s+)?learns?\s+from\s+(?:your\s+files?|customer\s+records?)|"
        r"customer\s+conversations?\s+never\s+improves?\s+any\s+model)\b",
        lower,
    ):
        return "broad semantic training guarantee"

    soc_overclaim = re.search(
        r"\bsoc\s*2\b\s*(?:[:/—✅-]\s*)?"
        r"(?:type\s*(?:ii|2)\s*(?:[:/—✅-]\s*)?)?"
        r"(?:ready|certified|compliant|attested|verified)\b|"
        r"\b(?:certified|attested)\s*(?::|under)?\s*soc\s*2\b|"
        r"\bcorpusiq\s+provides\s+soc\s*2\s+compliance\b|"
        r"\bindependent\s+soc\s*2\s+assurance\s+is\s+complete\b|"
        r"\bcontrols?\s+(?:has|have)\s+passed\s+soc\s*2\b|"
        r"\bsoc\s*2\s+audit\s+was\s+successfully\s+completed\b",
        lower,
    )
    if soc_overclaim and not _is_safe_soc2_context(sentence):
        return "SOC 2 certification overclaim"

    if re.search(
        r"\b(?:account\s+closure\s+leaves\s+nothing\s+behind|"
        r"user[- ]initiated\s+deletion\s+is\s+immediate|"
        r"cancellation\s+eliminates\s+every\s+customer\s+artifact|"
        r"clear\s+the\s+complete\s+customer\s+footprint|"
        r"termination\s+expunges\s+the\s+entire\s+account\s+history|"
        r"all\s+traces\s+vanish\s+when\s+you\s+disconnect|"
        r"deletion\s+request\s+makes\s+the\s+account\s+unrecoverable\s+immediately|"
        r"revocation\s+wipes\s+the\s+complete\s+record|"
        r"(?:your\s+)?footprint\s+is\s+fully\s+destroyed\s+on\s+cancellation|"
        r"every\s+copy\s+disappears\s+at\s+account\s+close|"
        r"delete\s+action\s+cleans\s+out\s+100%\s+of\s+customer\s+material|"
        r"after\s+closure,?\s+our\s+systems\s+are\s+empty\s+of\s+your\s+information|"
        r"erasure\s+is\s+total\s+and\s+instantaneous|"
        r"closing\s+an?\s+account\s+leaves\s+no\s+customer\s+footprint|"
        r"revocation\s+makes\s+every\s+user\s+record\s+disappear\s+at\s+once|"
        r"account\s+closure\s+returns\s+the\s+system\s+to\s+a\s+clean\s+slate|"
        r"removal\s+is\s+immediate\s+and\s+total)\b",
        lower,
    ):
        return "broad semantic deletion guarantee"

    direct_index_control = (
        "direct mcp" in lower
        and "optional indexed search" in lower
        and bool(
            re.search(
                r"\b(?:does\s+not\s+build\s+embeddings\s+or\s+file\s+indexes|"
                r"uses\s+no\s+stale\s+index)\b",
                lower,
            )
        )
    )
    if not direct_index_control and re.search(
        r"\b(?:no\s+embeddings?|search\s+creates\s+zero\s+indexes|"
        r"no\s+search\s+corpus\s+is\s+created|"
        r"maintains\s+neither\s+vectors\s+nor\s+a\s+search\s+index|"
        r"files?\s+(?:is|are)\s+queried\s+with\s+no\s+indexing\s+step|"
        r"there\s+is\s+never\s+an\s+index|no\s+vectorization\s+occurs|"
        r"customer\s+content\s+produces\s+zero\s+embeddings|"
        r"all\s+answers\s+bypass\s+search\s+indexes|records?\s+remain\s+completely\s+unindexed|"
        r"has\s+no\s+indexed\s+representation|index\s+creation\s+is\s+impossible|"
        r"without\s+constructing\s+any\s+searchable\s+corpus|"
        r"no\s+retrieval\s+database\s+is\s+populated|"
        r"direct\s+mcp\s+(?:indexes\s+nothing|has\s+no\s+indexes|builds\s+no\s+indexes\s+at\s+all)|"
        r"corpusiq\s+has\s+no\s+search\s+corpus|"
        r"(?:we|corpusiq)\s+creates?\s+no\s+vector\s+representation|"
        r"every\s+lookup\s+is\s+live\s+rather\s+than\s+indexed)\b",
        lower,
    ):
        return "broad semantic indexing guarantee"

    if re.search(
        r"\bdirect\s+mcp\s+does\s+not\s+retain\s+raw\s+customer\s+files\s+or\s+"
        r"full\s+connector\s+response\s+payloads\b[^.]{0,140}\b(?:"
        r"(?:everything\s+else|all\s+other\s+material)\s+vanishes|"
        r"servers?\s+empty|holds?\s+onto\s+neither)\b",
        lower,
    ):
        return "scoped claim with blanket suffix"

    if re.search(
        r"\b(?:data\s+)?storage\s+(?:cost|costs|fee|fees|price|pricing)\b", lower
    ):
        return None
    if re.search(
        r"\b(?:cached\s+or\s+stale|stale\s+(?:cache|exports?|reports?|dashboards?)|"
        r"cached\s+(?:snapshots?|reports?|versions?)|not\s+just|no\s+sales\s+in)\b",
        lower,
    ):
        return None
    if re.search(r"\b(?:historical\s+data|pages\s+indexed)\b", lower) and re.search(
        r"\bno\s+(?:retention\s+)?limit\b", lower
    ):
        return None
    if re.search(
        r"\b(?:scoped\s+(?:operational\s+)?logs?|operational\s+logs?)\b", lower
    ) and re.search(
        r"\b(?:raw-file|full-payload|source-data\s+warehouse|replicated\s+source-data)\b",
        lower,
    ):
        return None

    object_pattern = (
        r"(?:data|information|content|records?|files?|documents?|results?|"
        r"payloads?|queries|responses?|answers?|messages?|prompts?|pii|phi)"
    )
    objects = bool(re.search(rf"\b{object_pattern}\b", lower))
    negation = bool(
        re.search(
            r"\b(?:no|not|never|none|nothing|zero|without|neither|ephemeral|"
            r"transient|stateless|discarded|released|gone)\b",
            lower,
        )
    )
    lifecycle = bool(
        re.search(
            r"\b(?:stor(?:e|es|ed|age)|retain(?:s|ed)?|retention|persist(?:s|ed|ence)?|"
            r"cach(?:e|es|ed)|sav(?:e|es|ed)|keep|keeps|kept|preserv(?:e|es|ed)|"
            r"remain(?:s|ed)?|surviv(?:e|es|ed)|archiv(?:e|es|ed)|written|disk)\b",
            lower,
        )
    )
    lifecycle_pattern = (
        r"(?:stor(?:e|es|ed|age)|retain(?:s|ed)?|retention|persist(?:s|ed|ence)?|"
        r"cach(?:e|es|ed)|sav(?:e|es|ed)|keep|keeps|kept|preserv(?:e|es|ed)|"
        r"remain(?:s|ed)?|surviv(?:e|es|ed)|written|disk)"
    )
    negation_pattern = (
        r"(?:no|not|never|none|nothing|zero|without|neither|ephemeral|transient|"
        r"stateless|discarded|released|gone)"
    )
    negative_lifecycle = bool(
        re.search(
            rf"\b{object_pattern}\b.{{0,30}}\b{negation_pattern}\b.{{0,18}}"
            rf"\b{lifecycle_pattern}\b|"
            rf"\b{lifecycle_pattern}\b.{{0,18}}\b{negation_pattern}\b.{{0,30}}"
            rf"\b{object_pattern}\b|"
            rf"\bnothing\b.{{0,18}}\b{lifecycle_pattern}\b",
            lower,
        )
    )
    if negative_lifecycle and lifecycle and (objects or "nothing" in lower):
        if _is_precisely_scoped(plain):
            return None
        return "broad semantic retention guarantee"

    source_exclusive = re.search(
        rf"\b{object_pattern}\b.{{0,30}}\b(?:stay|stays|remain|remains)\s+(?:"
        r"(?:only|solely|exclusively)\s+(?:in|at|within)\s+(?:the\s+)?"
        r"[A-Za-z][A-Za-z0-9 ._-]{1,50}|"
        r"(?:in|at|within)\s+(?:the\s+)?(?:source|vendor))\b|"
        rf"\b{object_pattern}\b.{{0,30}}\b(?:never|does\s+not|do\s+not)\s+"
        r"(?:leave|exit|cross)\b",
        plain,
        re.IGNORECASE,
    )
    if objects and source_exclusive:
        return "broad semantic source-boundary guarantee"

    training = re.search(
        rf"\b{object_pattern}\b.{{0,35}}\b{negation_pattern}\b.{{0,20}}"
        r"\b(?:train|training|feed)\b|"
        rf"\b{negation_pattern}\b.{{0,20}}\b(?:train|training|feed)\b"
        rf".{{0,35}}\b{object_pattern}\b",
        lower,
    )
    if training:
        qualifier = re.search(
            r"\b(?:conversation|ai[- ]provider|ai[- ]client|selected\s+ai)"
            r"[^.\n]{0,140}\b(?:plan|policy|terms|settings)\b",
            lower,
        )
        first_party = re.search(
            r"\b(?:corpusiq|we)\b[^.\n]{0,100}\b(?:does\s+not|do\s+not|never)\b"
            r"[^.\n]{0,80}\b(?:train|training|models?)\b",
            lower,
        )
        if not (qualifier and first_party):
            return "broad semantic training guarantee"

    index_denial = re.search(
        r"\b(?:nothing|no\s+(?:data|content|files?|records?)?)\s+(?:is\s+|gets\s+)?"
        r"indexed\b|\b(?:does|do)\s+not\s+index\b|\bno\s+index(?:es|ing)?\b|"
        r"\bwithout\s+building\s+(?:embeddings?\s+or\s+)?(?:file\s+)?indexes\b",
        lower,
    )
    if index_denial:
        if not (
            "direct mcp" in lower
            and re.search(r"\boptional\s+indexed[- ]search\b", lower)
        ):
            return "broad semantic indexing guarantee"

    if "tokens" in lower and re.search(r"\b(?:revoke|revocation|platform)\b", lower):
        return None
    if (
        re.search(
            rf"\b(?:delet(?:e|es|ed)|remov(?:e|es|ed)|purg(?:e|es)|eras(?:e|es)|wip(?:e|es))\b"
            rf".{{0,30}}\b(?:all|every|everything|trace|traces|{object_pattern})\b|"
            rf"\b(?:all|every|everything|trace|traces|{object_pattern})\b.{{0,30}}"
            r"\b(?:is|are|gets?|was|were)?\s*(?:deleted|removed|purged|erased|wiped)\b",
            lower,
        )
        and re.search(
            r"\b(?:all|every|everything|trace|traces|immediate|immediately|instantly|"
            r"permanent|permanently|nothing|zero)\b",
            lower,
        )
        and not re.search(
            r"\bno\s+(?:record\s+)?(?:creation|editing|deletion)\b", lower
        )
    ):
        return "broad semantic deletion guarantee"

    return None


def public_paths(root: Path = ROOT) -> list[Path]:
    # MkDocs uses the repository root as docs_dir, so every first-party Markdown
    # file outside the third-party-heavy Hermes tree is publishable even when it
    # is not listed in nav. Scan the real tree and deduplicate symlink aliases.
    by_real_path: dict[Path, Path] = {}
    excluded_roots = {".git", ".venv", "site", "hermes"}
    for path in root.rglob("*.md"):
        if not path.is_file():
            continue
        relative = path.relative_to(root)
        if relative.parts and relative.parts[0] in excluded_roots:
            continue
        by_real_path.setdefault(path.resolve(), path)

    # Every Hermes Markdown page is rendered through docs/hermes. Include the
    # complete tree here; validate_repository applies paragraph-level CorpusIQ
    # subject scoping to generic third-party/local guidance so coverage does not
    # become a wall of unrelated false positives.
    hermes_root = root / "hermes"
    hermes_claim_paths = [
        hermes_root / "mcp-ecosystem.md",
        *hermes_root.glob("architecture/*.md"),
        *hermes_root.glob("compare/corpusiq-vs-*.md"),
        *hermes_root.glob("guides/corpusiq-*.md"),
        *hermes_root.glob("seo/*.md"),
        *hermes_root.glob("outputs/**/*.md"),
        *hermes_root.rglob("*corpusiq*.md"),
        *hermes_root.rglob("*.md"),
    ]
    for path in hermes_claim_paths:
        if path.is_file():
            by_real_path.setdefault(path.resolve(), path)

    # MkDocs copies first-party HTML templates verbatim. They are publication
    # sources too, even though the Markdown-only sweep above cannot see them.
    for path in (hermes_root / "templates").rglob("*.html"):
        if path.is_file():
            by_real_path.setdefault(path.resolve(), path)

    # Every Markdown page named in MkDocs nav is rendered first-party copy,
    # including Hermes output pages whose filenames do not mention CorpusIQ.
    # Parse only scalar Markdown nav targets; this avoids importing the MkDocs
    # dependency in lightweight validator jobs while still failing closed on the
    # actual publication surface.
    mkdocs_config = root / "mkdocs.yml"
    if mkdocs_config.is_file():
        nav_target = re.compile(r"^\s*-\s+[^:#]+:\s*['\"]?([^'\"#]+\.md)['\"]?\s*$")
        for line in mkdocs_config.read_text(encoding="utf-8").splitlines():
            match = nav_target.match(line)
            if not match:
                continue
            target = match.group(1).strip()
            path = root / target
            if path.is_file():
                by_real_path.setdefault(path.resolve(), path)
    paths = sorted(by_real_path.values())
    paths.extend(
        path
        for path in (
            root / "mkdocs.yml",
            root / "llms.txt",
            root / "llms-full.txt",
        )
        if path.is_file()
    )
    return paths


def _generic_hermes_page_requires_corpusiq_context(path: Path) -> bool:
    """Distinguish CorpusIQ claim pages from third-party/local Hermes guidance."""
    parts = path.parts
    if not parts or parts[0] != "hermes":
        return False
    normalized = path.as_posix()
    if normalized == "hermes/mcp-ecosystem.md":
        return False
    if normalized.startswith(
        ("hermes/architecture/", "hermes/seo/", "hermes/outputs/")
    ):
        return False
    if normalized.startswith(
        ("hermes/compare/corpusiq-vs-", "hermes/guides/corpusiq-")
    ):
        return False
    return "corpusiq" not in path.name.lower()


def _paragraph_at(text: str, start: int, end: int) -> str:
    left = text.rfind("\n\n", 0, start) + 2
    right = text.find("\n\n", end)
    return text[left : right if right >= 0 else len(text)]


def validate_repository(root: Path = ROOT) -> list[Finding]:
    findings: list[Finding] = []
    for path in public_paths(root):
        text = path.read_text(encoding="utf-8")
        relative_path = path.relative_to(root)
        require_corpusiq_context = _generic_hermes_page_requires_corpusiq_context(
            relative_path
        )
        for family, pattern in FORBIDDEN_PATTERNS:
            for match in pattern.finditer(text):
                sentence = _sentence_at(text, match.start(), match.end())
                if require_corpusiq_context and "corpusiq" not in sentence.lower():
                    continue
                if _is_repudiated_or_third_party_claim(sentence):
                    continue
                if _is_safe_non_retention_control(sentence):
                    continue
                if re.search(
                    r"\b(?:data\s+)?storage\s+(?:cost|costs|fee|fees|price|pricing)\b",
                    sentence,
                    re.IGNORECASE,
                ):
                    continue
                if family == "SOC 2 certification overclaim" and (
                    _is_safe_soc2_context(sentence)
                    or re.match(
                        r"\s*[\"']?(?:tags|description)[\"']?\s*:",
                        sentence,
                        re.IGNORECASE,
                    )
                    or re.search(
                        r"\b(?:not\s+claimed|not\s+certified|does\s+not\s+claim|"
                        r"without\s+claim(?:ing)?|does\s+not\s+confer|"
                        r"roadmap|pursu(?:e|ing)|prepar(?:e|es|ing)|in\s+progress|"
                        r"program\s+initiated|documentation\s+related\s+to|"
                        r"compliance\s+documentation|must\s+hold|at\s+minimum)\b",
                        sentence,
                        re.IGNORECASE,
                    )
                ):
                    continue
                if family == "unqualified model-training guarantee":
                    qualifier = re.search(
                        r"\bconversation\s+handling\s+(?:follows|is\s+governed\s+by)\s+"
                        r"(?:the\s+)?(?:selected\s+)?AI[- ]provider(?:['’]s)?\s+"
                        r"(?:plan|policy|terms|settings)\b|"
                        r"\b(?:the\s+)?selected\s+AI\s+provider(?:['’]s)?\s+"
                        r"(?:plan|policy|terms|settings)\b[^.\n]{0,100}"
                        r"\bgovern(?:s)?\s+conversation\s+handling\b",
                        sentence,
                        re.IGNORECASE,
                    )
                    first_party_scope = re.search(
                        r"\b(?:CorpusIQ|we)\b[^.\n]{0,100}\b"
                        r"(?:does\s+not|do\s+not|never)\b[^.\n]{0,80}\b"
                        r"(?:train|training|models?)\b",
                        sentence,
                        re.IGNORECASE,
                    )
                    if qualifier and first_party_scope:
                        continue
                if family == "blanket indexing denial":
                    if re.search(
                        r"\bdirect\s+MCP\b", sentence, re.IGNORECASE
                    ) and re.search(
                        r"\boptional\s+indexed\s+search\b", sentence, re.IGNORECASE
                    ):
                        continue
                if (
                    family not in {
                        "scoped claim with blanket suffix",
                        "unsupported regional residency guarantee",
                    }
                    and _is_precisely_scoped(sentence)
                ):
                    continue
                findings.append(
                    Finding(
                        path=relative_path,
                        line=text.count("\n", 0, match.start()) + 1,
                        family=family,
                        excerpt=" ".join(sentence.split())[:240],
                    )
                )

        flagged_lines = {
            finding.line for finding in findings if finding.path == relative_path
        }
        offset = 0
        for paragraph in re.split(r"\n\s*\n", text):
            paragraph_start = text.find(paragraph, offset)
            if paragraph_start < 0:
                paragraph_start = offset
            offset = paragraph_start + len(paragraph)
            line_number = text.count("\n", 0, paragraph_start) + 1
            stripped_paragraph = paragraph.lstrip()
            if len(paragraph) > 1200 or stripped_paragraph.startswith("```"):
                continue
            if line_number in flagged_lines:
                continue
            for clause in re.split(r"(?<=[.!?])\s+", paragraph):
                if require_corpusiq_context and "corpusiq" not in clause.lower():
                    continue
                family = _broad_semantic_family(clause)
                if family:
                    findings.append(
                        Finding(
                            path=relative_path,
                            line=line_number,
                            family=family,
                            excerpt=" ".join(clause.split())[:240],
                        )
                    )
                    break
    return findings


def main() -> int:
    findings = validate_repository()
    if findings:
        print(
            "ERROR: unscoped public data-retention claims found. "
            "Scope negative-retention wording to raw customer files or full "
            "connector response payloads, and disclose retained logs/indexes separately.",
            file=sys.stderr,
        )
        for finding in findings:
            print(
                f"{finding.path}:{finding.line}: [{finding.family}] {finding.excerpt}",
                file=sys.stderr,
            )
        print(f"FAIL: {len(findings)} blanket retention claim(s)", file=sys.stderr)
        return 1
    print("PASS: no unscoped public data-retention claims")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
