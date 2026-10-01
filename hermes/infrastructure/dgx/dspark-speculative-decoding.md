---
title: DSpark Speculative Decoding on DGX Spark
description: "DSpark speculative decoding for DeepSeek-class models on DGX Spark hardware - a verified two-node vLLM recipe with 1M context and nvfp4 KV."
canonical: "https://www.corpusiq.io/docs/hermes/infrastructure/dgx/dspark-speculative-decoding/"
robots: "index,follow"
last_updated: "2026-10-01"
tags: ["hermes agent", "dspark", "speculative decoding", "dgx spark", "vllm", "inference"]
---

# DSpark Speculative Decoding on DGX Spark

DSpark is an inference architecture that combines **speculative decoding** with
**multi-token prediction (MTP)**. It is lossless - the output distribution is
unchanged; the speedup comes from proposing and verifying draft tokens instead
of decoding one token at a time.

The widely-quoted "up to 400% faster" figure comes from vendor framing. The
dated benchmark in the reference recipe is more conservative and is the number
worth planning against: single-stream decode holds roughly **62-83 tok/s** from
256 through 128K context, with around **162 aggregate tok/s** at six short
concurrent chats. The real wins are in single-stream decode and prefix reuse,
not a free 4x on every workload.

## Why it matters for agent workloads

An agent platform is an inference-heavy consumer. Cheaper decode at long context
is the difference between reasoning over many connected data sources and
reasoning over a few - inference economics directly bound how much data a single
session can work across before cost becomes the constraint.

## Reference recipe

The community reference implementation is
[`MiaAI-Lab/DeepSeek-v4-Flash-DSpark-2x-DGX-Spark`](https://github.com/MiaAI-Lab/DeepSeek-v4-Flash-DSpark-2x-DGX-Spark)
(MIT licensed). It is a two-node DGX Spark recipe:

| Property | Value |
|----------|-------|
| Model | `deepseek-ai/DeepSeek-V4-Flash-Vision-Exp` |
| Parallelism | vLLM tensor parallel, TP=2 |
| Decoding | DSpark speculative decoding |
| Context ceiling | 1M tokens |
| KV cache | `nvfp4_ds_mla` |
| Runtime | Anemll DSpark vLLM image, pinned tag |
| Interconnect | RoCE / NCCL over ConnectX |

Both nodes require the same runtime image. The `prepare` step copies the
checkpoint to the worker, or the worker can mount the head's cache over NFSv4 on
the ConnectX link when `DSPARK_WORKER_HF_NFS=1`.

### Bring-up sequence

1. Copy the environment template and set the fabric variables: worker host,
   master address, NCCL HCA and socket interface names, per-node host IPs, and
   cache paths.
2. Pull the pinned runtime image on **both** nodes. The start script refuses to
   launch if either node is missing it.
3. Prepare the model cache on the head node.
4. Validate the configuration before starting - the recipe ships a dedicated
   config validator.
5. Start the serving stack and confirm health, then run the smoke test.
6. Record decode throughput before and after enabling DSpark on your own
   workload before committing to additional hardware.

### Measured evidence over headline claims

Before adopting, benchmark on the workload you actually run. The recipe's
published tables are dated and method-documented; treat the vendor's headline
multiple as an upper bound and the repo's own numbers as the planning baseline.

## Practical notes

- **No video encoder** exists in the official weights - animated inputs are
  treated as a still frame. Native image input is supported.
- Abliterated weight variants are gated behind the model hub and require a token
  with repository access.
- A single-node variant of the same model family exists if two nodes are not
  available; the decode gains are smaller but the bring-up is much simpler.

## FAQ

### What is DSpark?

DSpark is an inference architecture that combines speculative decoding with
multi-token prediction. It proposes draft tokens and verifies them, which speeds
up decoding without changing the output distribution.

### Is DSpark lossless?

Yes. The output distribution is unchanged. Only the decode path is faster.

### Does DSpark give a 4x speedup?

Not on every workload. The vendor headline is an upper bound. The reference
recipe's own dated benchmark is more conservative: single-stream decode holds
roughly 62-83 tok/s from 256 through 128K context, with around 162 aggregate
tok/s at six short concurrent chats.

### How much hardware does the reference recipe need?

Two DGX Spark nodes with a working RoCE/NCCL link over ConnectX. A single-node
variant of the same model family exists if two nodes are not available.

### What context length does the recipe support?

A 1M-token ceiling, with `nvfp4_ds_mla` KV cache and vLLM tensor parallel TP=2.

### Does it support video input?

No. There is no video encoder in the official weights; animated inputs are
treated as a still frame. Native image input is supported.

### Should I benchmark before adopting?

Always. Measure decode throughput before and after enabling DSpark on the
workload you actually run before committing to additional hardware.

## Related

- [DGX Spark compute pattern](/docs/hermes/infrastructure/dgx/)
- [Model routing](/docs/hermes/infrastructure/routing/)
