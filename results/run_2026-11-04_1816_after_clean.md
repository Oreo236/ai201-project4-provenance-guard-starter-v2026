# Run log — after_clean

- Produced by: `run_eval.py::main`
- Service: `app.py::submit` · scoring: `scoring.py::combine_signals`
- 3 trials per criterion · 2026-11-04 18:16

Fill in Target from `criteria.md`, and Run and Verdict from the output
underneath. Whether a trial passed depends on the criterion you wrote.

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. my own writing |  |   |   |   |  |
| 2. score spread |  |   |   |   |  |
| 3. label coverage |  |   |   |   |  |
| 4. appeal path |  |   |   |   |  |
| 5. bad input |  |   |   |   |  |

---

## What actually came back

Real output. Paste the relevant parts into your README — the rubric
asks for the actual JSON, not a description of it.

### my own writing

**Trial 1**

```json
[
  {
    "status": 200,
    "content_id": "3223afe556a94b38b8a2a989f4fe3cd4",
    "guess": "human",
    "confidence": 0.3168,
    "model_score": 0.2587,
    "style_score": 0.375,
    "label": "We think this was most likely written by a person.",
    "error": null,
    "sent": "This weekend I went back home to celebrate a friends of mines birthday",
    "logged": [
      {
        "status": "decided",
        "guess": "human",
        "combined_score": 0.3168
      }
    ]
  },
  {
    "status": 200,
    "content_id": "7bd723dae07a4946b0a4c517b616b19a",
    "guess": "human",
    "confidence": 0.2772,
    "model_score": 0.261,
    "style_score": 0.2933,
    "label": "We think this was most likely written by a person.",
    "error": null,
    "sent": "i am honesly sooo tired rn. I was meant to be asleep by now but I have",
    "logged": [
      {
        "status": "decided",
        "guess": "human",
        "combined_score": 0.2772
      }
    ]
  },
  {
    "status": 200,
    "content_id": "bebec5cfc9284369a5f6ae47e45892f2",
    "guess": "human",
    "confidence": 0.305,
    "model_score": 0.3042,
    "style_score": 0.3058,
    "label": "We think this was most likely written by a person.",
    "error": null,
    "sent": "I am starving my last meal was at 12 pm. I have another meeting that s",
    "logged": [
      {
        "status": "decided",
        "guess": "human",
        "combined_score": 0.305
      }
    ]
  },
  {
    "status": 200,
    "content_id": "fdf7135872034c1aa0cf62b52d491305",
    "guess": "unsure",
    "confidence": 0.401,
    "model_score": 0.4273,
    "style_score": 0.3747,
    "label": "We can't tell whether this was written by a person or with AI, so we're not making a call either way. A lot of people's own writing lands here, and this is not an accusation. If you wrote this yourself and want someone to take another look, you can appeal.",
    "error": null,
    "sent": "Hi, I recently got charged $29.99 to my bank account when I had assume",
    "logged": [
      {
        "status": "decided",
        "guess": "unsure",
        "combined_score": 0.401
      }
    ]
  },
  {
    "status": 200,
    "content_id": "c5a3d078bd4f48f0a607adcdfbde7af7",
    "guess": "unsure",
    "confidence": 0.4,
    "model_score": 0.6015,
    "style_score": 0.1,
    "label": "We can't tell whether this was written by a person or with AI, so we're not making a call either way. A lot of people's own writing lands here, and this is not an accusation. If you wrote this yourself and want someone to take another look, you can appeal.",
    "error": null,
    "sent": "Hi everyone, I and Jen are planning something really small for Andrea\u2019",
    "logged": [
      {
        "status": "decided",
        "guess": "unsure",
        "combined_score": 0.4
      }
    ]
  },
  {
    "status": 200,
    "content_id": "4850fb7f0f65455fb726345f3771329a",
    "guess": "unsure",
    "confidence": 0.4002,
    "model_score": 0.3381,
    "style_score": 0.4623,
    "label": "We can't tell whether this was written by a person or with AI, so we're not making a call either way. A lot of people's own writing lands here, and this is not an accusation. If you wrote this yourself and want someone to take another look, you can appeal.",
    "error": null,
    "sent": "You know what hurts the most is realizing how much you have celebrated",
    "logged": [
      {
        "status": "decided",
        "guess": "unsure",
        "combined_score": 0.4002
      }
    ]
  },
  {
    "status": 200,
    "content_id": "dd3318b7260548619edf0e7e831254e9",
    "guess": "unsure",
    "confidence": 0.4869,
    "model_score": 0.6738,
    "style_score": 0.3,
    "label": "We can't tell whether this was written by a person or with AI, so we're not making a call either way. A lot of people's own writing lands here, and this is not an accusation. If you wrote this yourself and want someone to take another look, you can appeal.",
    "error": null,
    "sent": "I am based in New York, NY but if I am selected for a San Francisco po",
    "logged": [
      {
        "status": "decided",
        "guess": "unsure",
        "combined_score": 0.4869
      }
    ]
  },
  {
    "status": 200,
    "content_id": "149fcaef3530411b90558e7fb96336b7",
    "guess": "human",
    "confidence": 0.262,
    "model_score": 0.2239,
    "style_score": 0.3,
    "label": "We think this was most likely written by a person.",
    "error": null,
    "sent": "so for example i have an exam going on in two days I have been really ",
    "logged": [
      {
        "status": "decided",
        "guess": "human",
        "combined_score": 0.262
      }
    ]
  },
  {
    "status": 200,
    "content_id": "5e5106ff95834a8c8616bf93732aad9a",
    "guess": "human",
    "confidence": 0.2215,
    "model_score": 0.143,
    "style_score": 0.3,
    "label": "We think this was most likely written by a person.",
    "error": null,
    "sent": "The most I probably realized was that even the groups that had chosen ",
    "logged": [
      {
        "status": "decided",
        "guess": "human",
        "combined_score": 0.2215
      }
    ]
  },
  {
    "status": 200,
    "content_id": "9deb7c207ff847e9ad195f5bebcee563",
    "guess": "human",
    "confidence": 0.2586,
    "model_score": 0.2468,
    "style_score": 0.2705,
    "label": "We think this was most likely written by a person.",
    "error": null,
    "sent": "Looking for accountability partners is so much work. I wish I could ju",
    "logged": [
      {
        "status": "decided",
        "guess": "human",
        "combined_score": 0.2586
      }
    ]
  }
]
```

**Trial 2**

```json
[
  {
    "status": 200,
    "content_id": "2ce586e044de459aa87f48312f7be891",
    "guess": "human",
    "confidence": 0.3168,
    "model_score": 0.2587,
    "style_score": 0.375,
    "label": "We think this was most likely written by a person.",
    "error": null,
    "sent": "This weekend I went back home to celebrate a friends of mines birthday",
    "logged": [
      {
        "status": "decided",
        "guess": "human",
        "combined_score": 0.3168
      }
    ]
  },
  {
    "status": 200,
    "content_id": "1058fde82f8f443bae180ecb1daa9625",
    "guess": "human",
    "confidence": 0.2772,
    "model_score": 0.261,
    "style_score": 0.2933,
    "label": "We think this was most likely written by a person.",
    "error": null,
    "sent": "i am honesly sooo tired rn. I was meant to be asleep by now but I have",
    "logged": [
      {
        "status": "decided",
        "guess": "human",
        "combined_score": 0.2772
      }
    ]
  },
  {
    "status": 200,
    "content_id": "c352d285ddb64cfb95fefdbad041c313",
    "guess": "human",
    "confidence": 0.305,
    "model_score": 0.3042,
    "style_score": 0.3058,
    "label": "We think this was most likely written by a person.",
    "error": null,
    "sent": "I am starving my last meal was at 12 pm. I have another meeting that s",
    "logged": [
      {
        "status": "decided",
        "guess": "human",
        "combined_score": 0.305
      }
    ]
  },
  {
    "status": 200,
    "content_id": "222a00cfa02c472888dfce1378b1ef07",
    "guess": "unsure",
    "confidence": 0.401,
    "model_score": 0.4273,
    "style_score": 0.3747,
    "label": "We can't tell whether this was written by a person or with AI, so we're not making a call either way. A lot of people's own writing lands here, and this is not an accusation. If you wrote this yourself and want someone to take another look, you can appeal.",
    "error": null,
    "sent": "Hi, I recently got charged $29.99 to my bank account when I had assume",
    "logged": [
      {
        "status": "decided",
        "guess": "unsure",
        "combined_score": 0.401
      }
    ]
  },
  {
    "status": 200,
    "content_id": "7eb19a6643ed482f8c1520538b42ea1e",
    "guess": "unsure",
    "confidence": 0.4,
    "model_score": 0.6015,
    "style_score": 0.1,
    "label": "We can't tell whether this was written by a person or with AI, so we're not making a call either way. A lot of people's own writing lands here, and this is not an accusation. If you wrote this yourself and want someone to take another look, you can appeal.",
    "error": null,
    "sent": "Hi everyone, I and Jen are planning something really small for Andrea\u2019",
    "logged": [
      {
        "status": "decided",
        "guess": "unsure",
        "combined_score": 0.4
      }
    ]
  },
  {
    "status": 200,
    "content_id": "325c4263b7ac4ded805f85a58335f236",
    "guess": "unsure",
    "confidence": 0.4002,
    "model_score": 0.3381,
    "style_score": 0.4623,
    "label": "We can't tell whether this was written by a person or with AI, so we're not making a call either way. A lot of people's own writing lands here, and this is not an accusation. If you wrote this yourself and want someone to take another look, you can appeal.",
    "error": null,
    "sent": "You know what hurts the most is realizing how much you have celebrated",
    "logged": [
      {
        "status": "decided",
        "guess": "unsure",
        "combined_score": 0.4002
      }
    ]
  },
  {
    "status": 200,
    "content_id": "ad25964c85834ab8bc9e756f4d7837f4",
    "guess": "unsure",
    "confidence": 0.4869,
    "model_score": 0.6738,
    "style_score": 0.3,
    "label": "We can't tell whether this was written by a person or with AI, so we're not making a call either way. A lot of people's own writing lands here, and this is not an accusation. If you wrote this yourself and want someone to take another look, you can appeal.",
    "error": null,
    "sent": "I am based in New York, NY but if I am selected for a San Francisco po",
    "logged": [
      {
        "status": "decided",
        "guess": "unsure",
        "combined_score": 0.4869
      }
    ]
  },
  {
    "status": 200,
    "content_id": "b8aa155305174762a27b28d5ce0f422e",
    "guess": "human",
    "confidence": 0.262,
    "model_score": 0.2239,
    "style_score": 0.3,
    "label": "We think this was most likely written by a person.",
    "error": null,
    "sent": "so for example i have an exam going on in two days I have been really ",
    "logged": [
      {
        "status": "decided",
        "guess": "human",
        "combined_score": 0.262
      }
    ]
  },
  {
    "status": 200,
    "content_id": "664fd2e37eb249b6988141d77fc32079",
    "guess": "human",
    "confidence": 0.2215,
    "model_score": 0.143,
    "style_score": 0.3,
    "label": "We think this was most likely written by a person.",
    "error": null,
    "sent": "The most I probably realized was that even the groups that had chosen ",
    "logged": [
      {
        "status": "decided",
        "guess": "human",
        "combined_score": 0.2215
      }
    ]
  },
  {
    "status": 200,
    "content_id": "44cf91855f2c4bd1bd2911d8ead4980b",
    "guess": "human",
    "confidence": 0.2586,
    "model_score": 0.2468,
    "style_score": 0.2705,
    "label": "We think this was most likely written by a person.",
    "error": null,
    "sent": "Looking for accountability partners is so much work. I wish I could ju",
    "logged": [
      {
        "status": "decided",
        "guess": "human",
        "combined_score": 0.2586
      }
    ]
  }
]
```

**Trial 3**

```json
[
  {
    "status": 200,
    "content_id": "522bfec760814785b10d653fe24b6b79",
    "guess": "human",
    "confidence": 0.3168,
    "model_score": 0.2587,
    "style_score": 0.375,
    "label": "We think this was most likely written by a person.",
    "error": null,
    "sent": "This weekend I went back home to celebrate a friends of mines birthday",
    "logged": [
      {
        "status": "decided",
        "guess": "human",
        "combined_score": 0.3168
      }
    ]
  },
  {
    "status": 200,
    "content_id": "0a05b9a415e54c05b452477ebfb2ce05",
    "guess": "human",
    "confidence": 0.2772,
    "model_score": 0.261,
    "style_score": 0.2933,
    "label": "We think this was most likely written by a person.",
    "error": null,
    "sent": "i am honesly sooo tired rn. I was meant to be asleep by now but I have",
    "logged": [
      {
        "status": "decided",
        "guess": "human",
        "combined_score": 0.2772
      }
    ]
  },
  {
    "status": 200,
    "content_id": "9f0156610a5e4159bcfa1c5c4a02b540",
    "guess": "human",
    "confidence": 0.305,
    "model_score": 0.3042,
    "style_score": 0.3058,
    "label": "We think this was most likely written by a person.",
    "error": null,
    "sent": "I am starving my last meal was at 12 pm. I have another meeting that s",
    "logged": [
      {
        "status": "decided",
        "guess": "human",
        "combined_score": 0.305
      }
    ]
  },
  {
    "status": 200,
    "content_id": "38ad2bfd7c434d0aa3349a2b47c9e527",
    "guess": "unsure",
    "confidence": 0.401,
    "model_score": 0.4273,
    "style_score": 0.3747,
    "label": "We can't tell whether this was written by a person or with AI, so we're not making a call either way. A lot of people's own writing lands here, and this is not an accusation. If you wrote this yourself and want someone to take another look, you can appeal.",
    "error": null,
    "sent": "Hi, I recently got charged $29.99 to my bank account when I had assume",
    "logged": [
      {
        "status": "decided",
        "guess": "unsure",
        "combined_score": 0.401
      }
    ]
  },
  {
    "status": 200,
    "content_id": "335453a7ef9d473b80264df96cb64598",
    "guess": "unsure",
    "confidence": 0.4,
    "model_score": 0.6015,
    "style_score": 0.1,
    "label": "We can't tell whether this was written by a person or with AI, so we're not making a call either way. A lot of people's own writing lands here, and this is not an accusation. If you wrote this yourself and want someone to take another look, you can appeal.",
    "error": null,
    "sent": "Hi everyone, I and Jen are planning something really small for Andrea\u2019",
    "logged": [
      {
        "status": "decided",
        "guess": "unsure",
        "combined_score": 0.4
      }
    ]
  },
  {
    "status": 200,
    "content_id": "9e378b1e3b2b4300bb729382720c86b6",
    "guess": "unsure",
    "confidence": 0.4002,
    "model_score": 0.3381,
    "style_score": 0.4623,
    "label": "We can't tell whether this was written by a person or with AI, so we're not making a call either way. A lot of people's own writing lands here, and this is not an accusation. If you wrote this yourself and want someone to take another look, you can appeal.",
    "error": null,
    "sent": "You know what hurts the most is realizing how much you have celebrated",
    "logged": [
      {
        "status": "decided",
        "guess": "unsure",
        "combined_score": 0.4002
      }
    ]
  },
  {
    "status": 200,
    "content_id": "db918527666645c58c0bae7fc1b6ff44",
    "guess": "unsure",
    "confidence": 0.4869,
    "model_score": 0.6738,
    "style_score": 0.3,
    "label": "We can't tell whether this was written by a person or with AI, so we're not making a call either way. A lot of people's own writing lands here, and this is not an accusation. If you wrote this yourself and want someone to take another look, you can appeal.",
    "error": null,
    "sent": "I am based in New York, NY but if I am selected for a San Francisco po",
    "logged": [
      {
        "status": "decided",
        "guess": "unsure",
        "combined_score": 0.4869
      }
    ]
  },
  {
    "status": 200,
    "content_id": "c0ddb8d78514496b917498ca67d5fd00",
    "guess": "human",
    "confidence": 0.262,
    "model_score": 0.2239,
    "style_score": 0.3,
    "label": "We think this was most likely written by a person.",
    "error": null,
    "sent": "so for example i have an exam going on in two days I have been really ",
    "logged": [
      {
        "status": "decided",
        "guess": "human",
        "combined_score": 0.262
      }
    ]
  },
  {
    "status": 200,
    "content_id": "0917e3cdd38b4eca888b2d681086713e",
    "guess": "human",
    "confidence": 0.2215,
    "model_score": 0.143,
    "style_score": 0.3,
    "label": "We think this was most likely written by a person.",
    "error": null,
    "sent": "The most I probably realized was that even the groups that had chosen ",
    "logged": [
      {
        "status": "decided",
        "guess": "human",
        "combined_score": 0.2215
      }
    ]
  },
  {
    "status": 200,
    "content_id": "ca44cdb883cc463fb799588175492ae1",
    "guess": "human",
    "confidence": 0.2586,
    "model_score": 0.2468,
    "style_score": 0.2705,
    "label": "We think this was most likely written by a person.",
    "error": null,
    "sent": "Looking for accountability partners is so much work. I wish I could ju",
    "logged": [
      {
        "status": "decided",
        "guess": "human",
        "combined_score": 0.2586
      }
    ]
  }
]
```

### score spread

**Trial 1**

```json
[
  {
    "status": 200,
    "content_id": "4b4636cddcd043fea6c665ad69ced8a9",
    "guess": "unsure",
    "confidence": 0.6842,
    "model_score": 0.7683,
    "style_score": 0.6,
    "label": "We can't tell whether this was written by a person or with AI, so we're not making a call either way. A lot of people's own writing lands here, and this is not an accusation. If you wrote this yourself and want someone to take another look, you can appeal.",
    "error": null,
    "sent": "Remote work has fundamentally transformed the modern workplace, offeri",
    "logged": [
      {
        "status": "decided",
        "guess": "unsure",
        "combined_score": 0.6842
      }
    ]
  },
  {
    "status": 200,
    "content_id": "9dfc0206288944bf9496e2774fea8c07",
    "guess": "unsure",
    "confidence": 0.6,
    "model_score": 0.92,
    "style_score": 0.6,
    "label": "We can't tell whether this was written by a person or with AI, so we're not making a call either way. A lot of people's own writing lands here, and this is not an accusation. If you wrote this yourself and want someone to take another look, you can appeal.",
    "error": null,
    "sent": "Regular exercise plays a crucial role in maintaining both physical and",
    "logged": [
      {
        "status": "decided",
        "guess": "unsure",
        "combined_score": 0.6
      }
    ]
  },
  {
    "status": 200,
    "content_id": "79ca274982124e558b861ba67df5dacf",
    "guess": "unsure",
    "confidence": 0.729,
    "model_score": 0.858,
    "style_score": 0.6,
    "label": "We can't tell whether this was written by a person or with AI, so we're not making a call either way. A lot of people's own writing lands here, and this is not an accusation. If you wrote this yourself and want someone to take another look, you can appeal.",
    "error": null,
    "sent": "Social media has become an integral part of modern society, shaping th",
    "logged": [
      {
        "status": "decided",
        "guess": "unsure",
        "combined_score": 0.729
      }
    ]
  },
  {
    "status": 200,
    "content_id": "83ced47106bc458989731607ee3ee806",
    "guess": "unsure",
    "confidence": 0.6,
    "model_score": 0.9179,
    "style_score": 0.6,
    "label": "We can't tell whether this was written by a person or with AI, so we're not making a call either way. A lot of people's own writing lands here, and this is not an accusation. If you wrote this yourself and want someone to take another look, you can appeal.",
    "error": null,
    "sent": "Climate change represents one of the most pressing challenges facing h",
    "logged": [
      {
        "status": "decided",
        "guess": "unsure",
        "combined_score": 0.6
      }
    ]
  },
  {
    "status": 200,
    "content_id": "a88139c9a0174f719f3f324e1430d715",
    "guess": "unsure",
    "confidence": 0.5926,
    "model_score": 0.7125,
    "style_score": 0.4727,
    "label": "We can't tell whether this was written by a person or with AI, so we're not making a call either way. A lot of people's own writing lands here, and this is not an accusation. If you wrote this yourself and want someone to take another look, you can appeal.",
    "error": null,
    "sent": "Reading offers numerous benefits that extend far beyond simple enterta",
    "logged": [
      {
        "status": "decided",
        "guess": "unsure",
        "combined_score": 0.5926
      }
    ]
  },
  {
    "status": 200,
    "content_id": "8f746eb43fd944429333888c7f1deee8",
    "guess": "human",
    "confidence": 0.3168,
    "model_score": 0.2587,
    "style_score": 0.375,
    "label": "We think this was most likely written by a person.",
    "error": null,
    "sent": "This weekend I went back home to celebrate a friends of mines birthday",
    "logged": [
      {
        "status": "decided",
        "guess": "human",
        "combined_score": 0.3168
      }
    ]
  },
  {
    "status": 200,
    "content_id": "1750d55a98f749bb92ed8870c45cb37e",
    "guess": "human",
    "confidence": 0.2772,
    "model_score": 0.261,
    "style_score": 0.2933,
    "label": "We think this was most likely written by a person.",
    "error": null,
    "sent": "i am honesly sooo tired rn. I was meant to be asleep by now but I have",
    "logged": [
      {
        "status": "decided",
        "guess": "human",
        "combined_score": 0.2772
      }
    ]
  },
  {
    "status": 200,
    "content_id": "9bee6e1450da41ad90b27919ec6dd1e5",
    "guess": "human",
    "confidence": 0.305,
    "model_score": 0.3042,
    "style_score": 0.3058,
    "label": "We think this was most likely written by a person.",
    "error": null,
    "sent": "I am starving my last meal was at 12 pm. I have another meeting that s",
    "logged": [
      {
        "status": "decided",
        "guess": "human",
        "combined_score": 0.305
      }
    ]
  },
  {
    "status": 200,
    "content_id": "05a07f22a2dc49b2825989c1e3181da7",
    "guess": "unsure",
    "confidence": 0.401,
    "model_score": 0.4273,
    "style_score": 0.3747,
    "label": "We can't tell whether this was written by a person or with AI, so we're not making a call either way. A lot of people's own writing lands here, and this is not an accusation. If you wrote this yourself and want someone to take another look, you can appeal.",
    "error": null,
    "sent": "Hi, I recently got charged $29.99 to my bank account when I had assume",
    "logged": [
      {
        "status": "decided",
        "guess": "unsure",
        "combined_score": 0.401
      }
    ]
  },
  {
    "status": 200,
    "content_id": "500175fc0c9642f19898f6c38bbad99f",
    "guess": "unsure",
    "confidence": 0.4,
    "model_score": 0.6015,
    "style_score": 0.1,
    "label": "We can't tell whether this was written by a person or with AI, so we're not making a call either way. A lot of people's own writing lands here, and this is not an accusation. If you wrote this yourself and want someone to take another look, you can appeal.",
    "error": null,
    "sent": "Hi everyone, I and Jen are planning something really small for Andrea\u2019",
    "logged": [
      {
        "status": "decided",
        "guess": "unsure",
        "combined_score": 0.4
      }
    ]
  }
]
```

**Trial 2**

```json
[
  {
    "status": 200,
    "content_id": "7b169c4c2d664060a975020c9aa53086",
    "guess": "unsure",
    "confidence": 0.6842,
    "model_score": 0.7683,
    "style_score": 0.6,
    "label": "We can't tell whether this was written by a person or with AI, so we're not making a call either way. A lot of people's own writing lands here, and this is not an accusation. If you wrote this yourself and want someone to take another look, you can appeal.",
    "error": null,
    "sent": "Remote work has fundamentally transformed the modern workplace, offeri",
    "logged": [
      {
        "status": "decided",
        "guess": "unsure",
        "combined_score": 0.6842
      }
    ]
  },
  {
    "status": 200,
    "content_id": "1352989e2fe04bc29085f0c06de6d008",
    "guess": "unsure",
    "confidence": 0.6,
    "model_score": 0.92,
    "style_score": 0.6,
    "label": "We can't tell whether this was written by a person or with AI, so we're not making a call either way. A lot of people's own writing lands here, and this is not an accusation. If you wrote this yourself and want someone to take another look, you can appeal.",
    "error": null,
    "sent": "Regular exercise plays a crucial role in maintaining both physical and",
    "logged": [
      {
        "status": "decided",
        "guess": "unsure",
        "combined_score": 0.6
      }
    ]
  },
  {
    "status": 200,
    "content_id": "b153df76dfac4e23be5b9d118e060db6",
    "guess": "unsure",
    "confidence": 0.729,
    "model_score": 0.858,
    "style_score": 0.6,
    "label": "We can't tell whether this was written by a person or with AI, so we're not making a call either way. A lot of people's own writing lands here, and this is not an accusation. If you wrote this yourself and want someone to take another look, you can appeal.",
    "error": null,
    "sent": "Social media has become an integral part of modern society, shaping th",
    "logged": [
      {
        "status": "decided",
        "guess": "unsure",
        "combined_score": 0.729
      }
    ]
  },
  {
    "status": 200,
    "content_id": "51f331168fad40c58e176343f99fbd6a",
    "guess": "unsure",
    "confidence": 0.6,
    "model_score": 0.9179,
    "style_score": 0.6,
    "label": "We can't tell whether this was written by a person or with AI, so we're not making a call either way. A lot of people's own writing lands here, and this is not an accusation. If you wrote this yourself and want someone to take another look, you can appeal.",
    "error": null,
    "sent": "Climate change represents one of the most pressing challenges facing h",
    "logged": [
      {
        "status": "decided",
        "guess": "unsure",
        "combined_score": 0.6
      }
    ]
  },
  {
    "status": 200,
    "content_id": "bea24a96253a4d74b35089d43f4ebf8e",
    "guess": "unsure",
    "confidence": 0.5926,
    "model_score": 0.7125,
    "style_score": 0.4727,
    "label": "We can't tell whether this was written by a person or with AI, so we're not making a call either way. A lot of people's own writing lands here, and this is not an accusation. If you wrote this yourself and want someone to take another look, you can appeal.",
    "error": null,
    "sent": "Reading offers numerous benefits that extend far beyond simple enterta",
    "logged": [
      {
        "status": "decided",
        "guess": "unsure",
        "combined_score": 0.5926
      }
    ]
  },
  {
    "status": 200,
    "content_id": "0e8c1f375b264240a4b7ea9c577cea0c",
    "guess": "human",
    "confidence": 0.3168,
    "model_score": 0.2587,
    "style_score": 0.375,
    "label": "We think this was most likely written by a person.",
    "error": null,
    "sent": "This weekend I went back home to celebrate a friends of mines birthday",
    "logged": [
      {
        "status": "decided",
        "guess": "human",
        "combined_score": 0.3168
      }
    ]
  },
  {
    "status": 200,
    "content_id": "3d3b1b283e134ca2886b17143f71a66b",
    "guess": "human",
    "confidence": 0.2772,
    "model_score": 0.261,
    "style_score": 0.2933,
    "label": "We think this was most likely written by a person.",
    "error": null,
    "sent": "i am honesly sooo tired rn. I was meant to be asleep by now but I have",
    "logged": [
      {
        "status": "decided",
        "guess": "human",
        "combined_score": 0.2772
      }
    ]
  },
  {
    "status": 200,
    "content_id": "35133c92a90e4d4babc867107b0fe41f",
    "guess": "human",
    "confidence": 0.305,
    "model_score": 0.3042,
    "style_score": 0.3058,
    "label": "We think this was most likely written by a person.",
    "error": null,
    "sent": "I am starving my last meal was at 12 pm. I have another meeting that s",
    "logged": [
      {
        "status": "decided",
        "guess": "human",
        "combined_score": 0.305
      }
    ]
  },
  {
    "status": 200,
    "content_id": "83ca595710c543ed8fb4e704fcfb73ea",
    "guess": "unsure",
    "confidence": 0.401,
    "model_score": 0.4273,
    "style_score": 0.3747,
    "label": "We can't tell whether this was written by a person or with AI, so we're not making a call either way. A lot of people's own writing lands here, and this is not an accusation. If you wrote this yourself and want someone to take another look, you can appeal.",
    "error": null,
    "sent": "Hi, I recently got charged $29.99 to my bank account when I had assume",
    "logged": [
      {
        "status": "decided",
        "guess": "unsure",
        "combined_score": 0.401
      }
    ]
  },
  {
    "status": 200,
    "content_id": "6fb1dba14cd74081926903989fc5f248",
    "guess": "unsure",
    "confidence": 0.4,
    "model_score": 0.6015,
    "style_score": 0.1,
    "label": "We can't tell whether this was written by a person or with AI, so we're not making a call either way. A lot of people's own writing lands here, and this is not an accusation. If you wrote this yourself and want someone to take another look, you can appeal.",
    "error": null,
    "sent": "Hi everyone, I and Jen are planning something really small for Andrea\u2019",
    "logged": [
      {
        "status": "decided",
        "guess": "unsure",
        "combined_score": 0.4
      }
    ]
  }
]
```

**Trial 3**

```json
[
  {
    "status": 200,
    "content_id": "8255059132564905b7ff4e9500ccc362",
    "guess": "unsure",
    "confidence": 0.6842,
    "model_score": 0.7683,
    "style_score": 0.6,
    "label": "We can't tell whether this was written by a person or with AI, so we're not making a call either way. A lot of people's own writing lands here, and this is not an accusation. If you wrote this yourself and want someone to take another look, you can appeal.",
    "error": null,
    "sent": "Remote work has fundamentally transformed the modern workplace, offeri",
    "logged": [
      {
        "status": "decided",
        "guess": "unsure",
        "combined_score": 0.6842
      }
    ]
  },
  {
    "status": 200,
    "content_id": "17e69d4c4ce044e7a36160b52e7cf990",
    "guess": "unsure",
    "confidence": 0.6,
    "model_score": 0.92,
    "style_score": 0.6,
    "label": "We can't tell whether this was written by a person or with AI, so we're not making a call either way. A lot of people's own writing lands here, and this is not an accusation. If you wrote this yourself and want someone to take another look, you can appeal.",
    "error": null,
    "sent": "Regular exercise plays a crucial role in maintaining both physical and",
    "logged": [
      {
        "status": "decided",
        "guess": "unsure",
        "combined_score": 0.6
      }
    ]
  },
  {
    "status": 200,
    "content_id": "b03584ece3fb49579e16acc552a6f2e6",
    "guess": "unsure",
    "confidence": 0.729,
    "model_score": 0.858,
    "style_score": 0.6,
    "label": "We can't tell whether this was written by a person or with AI, so we're not making a call either way. A lot of people's own writing lands here, and this is not an accusation. If you wrote this yourself and want someone to take another look, you can appeal.",
    "error": null,
    "sent": "Social media has become an integral part of modern society, shaping th",
    "logged": [
      {
        "status": "decided",
        "guess": "unsure",
        "combined_score": 0.729
      }
    ]
  },
  {
    "status": 200,
    "content_id": "fa43e49204684d5a85bffc696e45592e",
    "guess": "unsure",
    "confidence": 0.6,
    "model_score": 0.9179,
    "style_score": 0.6,
    "label": "We can't tell whether this was written by a person or with AI, so we're not making a call either way. A lot of people's own writing lands here, and this is not an accusation. If you wrote this yourself and want someone to take another look, you can appeal.",
    "error": null,
    "sent": "Climate change represents one of the most pressing challenges facing h",
    "logged": [
      {
        "status": "decided",
        "guess": "unsure",
        "combined_score": 0.6
      }
    ]
  },
  {
    "status": 200,
    "content_id": "535ebf9f303a4a7a9ff36430881634a9",
    "guess": "unsure",
    "confidence": 0.5926,
    "model_score": 0.7125,
    "style_score": 0.4727,
    "label": "We can't tell whether this was written by a person or with AI, so we're not making a call either way. A lot of people's own writing lands here, and this is not an accusation. If you wrote this yourself and want someone to take another look, you can appeal.",
    "error": null,
    "sent": "Reading offers numerous benefits that extend far beyond simple enterta",
    "logged": [
      {
        "status": "decided",
        "guess": "unsure",
        "combined_score": 0.5926
      }
    ]
  },
  {
    "status": 200,
    "content_id": "e4db2ed696f345fd8f5bf7a08b06080c",
    "guess": "human",
    "confidence": 0.3168,
    "model_score": 0.2587,
    "style_score": 0.375,
    "label": "We think this was most likely written by a person.",
    "error": null,
    "sent": "This weekend I went back home to celebrate a friends of mines birthday",
    "logged": [
      {
        "status": "decided",
        "guess": "human",
        "combined_score": 0.3168
      }
    ]
  },
  {
    "status": 200,
    "content_id": "17318b0054564c3c807d05649c50833c",
    "guess": "human",
    "confidence": 0.2772,
    "model_score": 0.261,
    "style_score": 0.2933,
    "label": "We think this was most likely written by a person.",
    "error": null,
    "sent": "i am honesly sooo tired rn. I was meant to be asleep by now but I have",
    "logged": [
      {
        "status": "decided",
        "guess": "human",
        "combined_score": 0.2772
      }
    ]
  },
  {
    "status": 200,
    "content_id": "a5992715a5264425b07b96b74407714f",
    "guess": "human",
    "confidence": 0.305,
    "model_score": 0.3042,
    "style_score": 0.3058,
    "label": "We think this was most likely written by a person.",
    "error": null,
    "sent": "I am starving my last meal was at 12 pm. I have another meeting that s",
    "logged": [
      {
        "status": "decided",
        "guess": "human",
        "combined_score": 0.305
      }
    ]
  },
  {
    "status": 200,
    "content_id": "5f8ee86e9e324daba3ee0ee3f53365a9",
    "guess": "unsure",
    "confidence": 0.401,
    "model_score": 0.4273,
    "style_score": 0.3747,
    "label": "We can't tell whether this was written by a person or with AI, so we're not making a call either way. A lot of people's own writing lands here, and this is not an accusation. If you wrote this yourself and want someone to take another look, you can appeal.",
    "error": null,
    "sent": "Hi, I recently got charged $29.99 to my bank account when I had assume",
    "logged": [
      {
        "status": "decided",
        "guess": "unsure",
        "combined_score": 0.401
      }
    ]
  },
  {
    "status": 200,
    "content_id": "b7129ba819824707a2691d8ae3aecce2",
    "guess": "unsure",
    "confidence": 0.4,
    "model_score": 0.6015,
    "style_score": 0.1,
    "label": "We can't tell whether this was written by a person or with AI, so we're not making a call either way. A lot of people's own writing lands here, and this is not an accusation. If you wrote this yourself and want someone to take another look, you can appeal.",
    "error": null,
    "sent": "Hi everyone, I and Jen are planning something really small for Andrea\u2019",
    "logged": [
      {
        "status": "decided",
        "guess": "unsure",
        "combined_score": 0.4
      }
    ]
  }
]
```

### label coverage

**Trial 1**

```json
[
  {
    "status": 200,
    "content_id": "2ab12f0991754632b50b3aca636b11d9",
    "guess": "unsure",
    "confidence": 0.6842,
    "model_score": 0.7683,
    "style_score": 0.6,
    "label": "We can't tell whether this was written by a person or with AI, so we're not making a call either way. A lot of people's own writing lands here, and this is not an accusation. If you wrote this yourself and want someone to take another look, you can appeal.",
    "error": null,
    "sent": "Remote work has fundamentally transformed the modern workplace, offeri",
    "logged": [
      {
        "status": "decided",
        "guess": "unsure",
        "combined_score": 0.6842
      }
    ]
  },
  {
    "status": 200,
    "content_id": "32dde2d4493a4f6dac81bd9499ff2799",
    "guess": "human",
    "confidence": 0.3168,
    "model_score": 0.2587,
    "style_score": 0.375,
    "label": "We think this was most likely written by a person.",
    "error": null,
    "sent": "This weekend I went back home to celebrate a friends of mines birthday",
    "logged": [
      {
        "status": "decided",
        "guess": "human",
        "combined_score": 0.3168
      }
    ]
  },
  {
    "status": 200,
    "content_id": "16f2fe1afa8e49218c9dcb68c57f88bb",
    "guess": "unsure",
    "confidence": 0.5382,
    "model_score": 0.7273,
    "style_score": 0.3491,
    "label": "We can't tell whether this was written by a person or with AI, so we're not making a call either way. A lot of people's own writing lands here, and this is not an accusation. If you wrote this yourself and want someone to take another look, you can appeal.",
    "error": null,
    "sent": "Four score and seven years ago our fathers brought forth on this conti",
    "logged": [
      {
        "status": "decided",
        "guess": "unsure",
        "combined_score": 0.5382
      }
    ]
  }
]
```

**Trial 2**

```json
[
  {
    "status": 200,
    "content_id": "036935e0ca8b491d95f21b739052cb15",
    "guess": "unsure",
    "confidence": 0.6842,
    "model_score": 0.7683,
    "style_score": 0.6,
    "label": "We can't tell whether this was written by a person or with AI, so we're not making a call either way. A lot of people's own writing lands here, and this is not an accusation. If you wrote this yourself and want someone to take another look, you can appeal.",
    "error": null,
    "sent": "Remote work has fundamentally transformed the modern workplace, offeri",
    "logged": [
      {
        "status": "decided",
        "guess": "unsure",
        "combined_score": 0.6842
      }
    ]
  },
  {
    "status": 200,
    "content_id": "bce63be8d6c5481181a749fb5746ff09",
    "guess": "human",
    "confidence": 0.3168,
    "model_score": 0.2587,
    "style_score": 0.375,
    "label": "We think this was most likely written by a person.",
    "error": null,
    "sent": "This weekend I went back home to celebrate a friends of mines birthday",
    "logged": [
      {
        "status": "decided",
        "guess": "human",
        "combined_score": 0.3168
      }
    ]
  },
  {
    "status": 200,
    "content_id": "c7da8ff03adb4c6d9218daecf7b54ec7",
    "guess": "unsure",
    "confidence": 0.5382,
    "model_score": 0.7273,
    "style_score": 0.3491,
    "label": "We can't tell whether this was written by a person or with AI, so we're not making a call either way. A lot of people's own writing lands here, and this is not an accusation. If you wrote this yourself and want someone to take another look, you can appeal.",
    "error": null,
    "sent": "Four score and seven years ago our fathers brought forth on this conti",
    "logged": [
      {
        "status": "decided",
        "guess": "unsure",
        "combined_score": 0.5382
      }
    ]
  }
]
```

**Trial 3**

```json
[
  {
    "status": 200,
    "content_id": "7e32085e79554bad8a052948139bf128",
    "guess": "unsure",
    "confidence": 0.6842,
    "model_score": 0.7683,
    "style_score": 0.6,
    "label": "We can't tell whether this was written by a person or with AI, so we're not making a call either way. A lot of people's own writing lands here, and this is not an accusation. If you wrote this yourself and want someone to take another look, you can appeal.",
    "error": null,
    "sent": "Remote work has fundamentally transformed the modern workplace, offeri",
    "logged": [
      {
        "status": "decided",
        "guess": "unsure",
        "combined_score": 0.6842
      }
    ]
  },
  {
    "status": 200,
    "content_id": "a2c9b34ca2eb4cddaf37522910d9bb26",
    "guess": "human",
    "confidence": 0.3168,
    "model_score": 0.2587,
    "style_score": 0.375,
    "label": "We think this was most likely written by a person.",
    "error": null,
    "sent": "This weekend I went back home to celebrate a friends of mines birthday",
    "logged": [
      {
        "status": "decided",
        "guess": "human",
        "combined_score": 0.3168
      }
    ]
  },
  {
    "status": 200,
    "content_id": "765d6551b2294e3c9ff3d5500a13b2d0",
    "guess": "unsure",
    "confidence": 0.5382,
    "model_score": 0.7273,
    "style_score": 0.3491,
    "label": "We can't tell whether this was written by a person or with AI, so we're not making a call either way. A lot of people's own writing lands here, and this is not an accusation. If you wrote this yourself and want someone to take another look, you can appeal.",
    "error": null,
    "sent": "Four score and seven years ago our fathers brought forth on this conti",
    "logged": [
      {
        "status": "decided",
        "guess": "unsure",
        "combined_score": 0.5382
      }
    ]
  }
]
```

### appeal path

**Trial 1**

```json
[
  {
    "status": 200,
    "content_id": "85a5d4e72cda427cb8ed1f10cc92087a",
    "guess": "unsure",
    "confidence": 0.6842,
    "model_score": 0.7683,
    "style_score": 0.6,
    "label": "We can't tell whether this was written by a person or with AI, so we're not making a call either way. A lot of people's own writing lands here, and this is not an accusation. If you wrote this yourself and want someone to take another look, you can appeal.",
    "error": null,
    "sent": "Remote work has fundamentally transformed the modern workplace, offeri",
    "logged": [
      {
        "status": "decided",
        "guess": "unsure",
        "combined_score": 0.6842
      }
    ],
    "appeal": {
      "status": 200,
      "new_status": "under_review",
      "appeal_entries": 1
    }
  },
  {
    "status": 200,
    "content_id": "4e60aa1f267a434c98615509a50c176b",
    "guess": "unsure",
    "confidence": 0.6,
    "model_score": 0.92,
    "style_score": 0.6,
    "label": "We can't tell whether this was written by a person or with AI, so we're not making a call either way. A lot of people's own writing lands here, and this is not an accusation. If you wrote this yourself and want someone to take another look, you can appeal.",
    "error": null,
    "sent": "Regular exercise plays a crucial role in maintaining both physical and",
    "logged": [
      {
        "status": "decided",
        "guess": "unsure",
        "combined_score": 0.6
      }
    ],
    "appeal": {
      "status": 200,
      "new_status": "under_review",
      "appeal_entries": 1
    }
  },
  {
    "status": 200,
    "content_id": "a0bf78c9fa274c6f9959c0ad4cad0f18",
    "guess": "unsure",
    "confidence": 0.729,
    "model_score": 0.858,
    "style_score": 0.6,
    "label": "We can't tell whether this was written by a person or with AI, so we're not making a call either way. A lot of people's own writing lands here, and this is not an accusation. If you wrote this yourself and want someone to take another look, you can appeal.",
    "error": null,
    "sent": "Social media has become an integral part of modern society, shaping th",
    "logged": [
      {
        "status": "decided",
        "guess": "unsure",
        "combined_score": 0.729
      }
    ],
    "appeal": {
      "status": 200,
      "new_status": "under_review",
      "appeal_entries": 1
    }
  },
  {
    "status": 200,
    "content_id": "1250dfac3537421da09f651ff3854690",
    "guess": "unsure",
    "confidence": 0.6,
    "model_score": 0.9179,
    "style_score": 0.6,
    "label": "We can't tell whether this was written by a person or with AI, so we're not making a call either way. A lot of people's own writing lands here, and this is not an accusation. If you wrote this yourself and want someone to take another look, you can appeal.",
    "error": null,
    "sent": "Climate change represents one of the most pressing challenges facing h",
    "logged": [
      {
        "status": "decided",
        "guess": "unsure",
        "combined_score": 0.6
      }
    ],
    "appeal": {
      "status": 200,
      "new_status": "under_review",
      "appeal_entries": 1
    }
  },
  {
    "status": 200,
    "content_id": "60013cca98f34aadbed6ae25f8070836",
    "guess": "unsure",
    "confidence": 0.5926,
    "model_score": 0.7125,
    "style_score": 0.4727,
    "label": "We can't tell whether this was written by a person or with AI, so we're not making a call either way. A lot of people's own writing lands here, and this is not an accusation. If you wrote this yourself and want someone to take another look, you can appeal.",
    "error": null,
    "sent": "Reading offers numerous benefits that extend far beyond simple enterta",
    "logged": [
      {
        "status": "decided",
        "guess": "unsure",
        "combined_score": 0.5926
      }
    ],
    "appeal": {
      "status": 200,
      "new_status": "under_review",
      "appeal_entries": 1
    }
  },
  {
    "status": 200,
    "content_id": "9b8b8d19742047519b5275e9c13c47a5",
    "guess": "human",
    "confidence": 0.3168,
    "model_score": 0.2587,
    "style_score": 0.375,
    "label": "We think this was most likely written by a person.",
    "error": null,
    "sent": "This weekend I went back home to celebrate a friends of mines birthday",
    "logged": [
      {
        "status": "decided",
        "guess": "human",
        "combined_score": 0.3168
      }
    ],
    "appeal": {
      "status": 200,
      "new_status": "under_review",
      "appeal_entries": 1
    }
  },
  {
    "status": 200,
    "content_id": "e9b752f8311540fa9bc453a8937de711",
    "guess": "human",
    "confidence": 0.2772,
    "model_score": 0.261,
    "style_score": 0.2933,
    "label": "We think this was most likely written by a person.",
    "error": null,
    "sent": "i am honesly sooo tired rn. I was meant to be asleep by now but I have",
    "logged": [
      {
        "status": "decided",
        "guess": "human",
        "combined_score": 0.2772
      }
    ],
    "appeal": {
      "status": 200,
      "new_status": "under_review",
      "appeal_entries": 1
    }
  },
  {
    "status": 200,
    "content_id": "dda8d9c47a8140e2a1cf226c5dae3cbb",
    "guess": "human",
    "confidence": 0.305,
    "model_score": 0.3042,
    "style_score": 0.3058,
    "label": "We think this was most likely written by a person.",
    "error": null,
    "sent": "I am starving my last meal was at 12 pm. I have another meeting that s",
    "logged": [
      {
        "status": "decided",
        "guess": "human",
        "combined_score": 0.305
      }
    ],
    "appeal": {
      "status": 200,
      "new_status": "under_review",
      "appeal_entries": 1
    }
  },
  {
    "status": 200,
    "content_id": "f84c32459ba148479f79ffcfe4bba357",
    "guess": "unsure",
    "confidence": 0.401,
    "model_score": 0.4273,
    "style_score": 0.3747,
    "label": "We can't tell whether this was written by a person or with AI, so we're not making a call either way. A lot of people's own writing lands here, and this is not an accusation. If you wrote this yourself and want someone to take another look, you can appeal.",
    "error": null,
    "sent": "Hi, I recently got charged $29.99 to my bank account when I had assume",
    "logged": [
      {
        "status": "decided",
        "guess": "unsure",
        "combined_score": 0.401
      }
    ],
    "appeal": {
      "status": 200,
      "new_status": "under_review",
      "appeal_entries": 1
    }
  },
  {
    "status": 200,
    "content_id": "3377510d051545018cd0a759d8a8083f",
    "guess": "unsure",
    "confidence": 0.4,
    "model_score": 0.6015,
    "style_score": 0.1,
    "label": "We can't tell whether this was written by a person or with AI, so we're not making a call either way. A lot of people's own writing lands here, and this is not an accusation. If you wrote this yourself and want someone to take another look, you can appeal.",
    "error": null,
    "sent": "Hi everyone, I and Jen are planning something really small for Andrea\u2019",
    "logged": [
      {
        "status": "decided",
        "guess": "unsure",
        "combined_score": 0.4
      }
    ],
    "appeal": {
      "status": 200,
      "new_status": "under_review",
      "appeal_entries": 1
    }
  },
  {
    "sent": "appeal with a made-up content_id",
    "appeal": {
      "status": 404,
      "new_status": null,
      "appeal_entries": 0
    }
  }
]
```

**Trial 2**

```json
[
  {
    "status": 200,
    "content_id": "eb727094f88f4ce6b1d52b548d1a23b5",
    "guess": "unsure",
    "confidence": 0.6842,
    "model_score": 0.7683,
    "style_score": 0.6,
    "label": "We can't tell whether this was written by a person or with AI, so we're not making a call either way. A lot of people's own writing lands here, and this is not an accusation. If you wrote this yourself and want someone to take another look, you can appeal.",
    "error": null,
    "sent": "Remote work has fundamentally transformed the modern workplace, offeri",
    "logged": [
      {
        "status": "decided",
        "guess": "unsure",
        "combined_score": 0.6842
      }
    ],
    "appeal": {
      "status": 200,
      "new_status": "under_review",
      "appeal_entries": 1
    }
  },
  {
    "status": 200,
    "content_id": "0a55c2becd41459db072fa04725838cd",
    "guess": "unsure",
    "confidence": 0.6,
    "model_score": 0.92,
    "style_score": 0.6,
    "label": "We can't tell whether this was written by a person or with AI, so we're not making a call either way. A lot of people's own writing lands here, and this is not an accusation. If you wrote this yourself and want someone to take another look, you can appeal.",
    "error": null,
    "sent": "Regular exercise plays a crucial role in maintaining both physical and",
    "logged": [
      {
        "status": "decided",
        "guess": "unsure",
        "combined_score": 0.6
      }
    ],
    "appeal": {
      "status": 200,
      "new_status": "under_review",
      "appeal_entries": 1
    }
  },
  {
    "status": 200,
    "content_id": "6d035c54977943a3901bb2c5fe445ce3",
    "guess": "unsure",
    "confidence": 0.729,
    "model_score": 0.858,
    "style_score": 0.6,
    "label": "We can't tell whether this was written by a person or with AI, so we're not making a call either way. A lot of people's own writing lands here, and this is not an accusation. If you wrote this yourself and want someone to take another look, you can appeal.",
    "error": null,
    "sent": "Social media has become an integral part of modern society, shaping th",
    "logged": [
      {
        "status": "decided",
        "guess": "unsure",
        "combined_score": 0.729
      }
    ],
    "appeal": {
      "status": 200,
      "new_status": "under_review",
      "appeal_entries": 1
    }
  },
  {
    "status": 200,
    "content_id": "e023096b91ef4cae9aa5f7498412517b",
    "guess": "unsure",
    "confidence": 0.6,
    "model_score": 0.9179,
    "style_score": 0.6,
    "label": "We can't tell whether this was written by a person or with AI, so we're not making a call either way. A lot of people's own writing lands here, and this is not an accusation. If you wrote this yourself and want someone to take another look, you can appeal.",
    "error": null,
    "sent": "Climate change represents one of the most pressing challenges facing h",
    "logged": [
      {
        "status": "decided",
        "guess": "unsure",
        "combined_score": 0.6
      }
    ],
    "appeal": {
      "status": 200,
      "new_status": "under_review",
      "appeal_entries": 1
    }
  },
  {
    "status": 200,
    "content_id": "dc1ab900ef5c4a868ca966211c56748a",
    "guess": "unsure",
    "confidence": 0.5926,
    "model_score": 0.7125,
    "style_score": 0.4727,
    "label": "We can't tell whether this was written by a person or with AI, so we're not making a call either way. A lot of people's own writing lands here, and this is not an accusation. If you wrote this yourself and want someone to take another look, you can appeal.",
    "error": null,
    "sent": "Reading offers numerous benefits that extend far beyond simple enterta",
    "logged": [
      {
        "status": "decided",
        "guess": "unsure",
        "combined_score": 0.5926
      }
    ],
    "appeal": {
      "status": 200,
      "new_status": "under_review",
      "appeal_entries": 1
    }
  },
  {
    "status": 200,
    "content_id": "c1ef7ae027fe4833a47fa2b13f2461d5",
    "guess": "human",
    "confidence": 0.3168,
    "model_score": 0.2587,
    "style_score": 0.375,
    "label": "We think this was most likely written by a person.",
    "error": null,
    "sent": "This weekend I went back home to celebrate a friends of mines birthday",
    "logged": [
      {
        "status": "decided",
        "guess": "human",
        "combined_score": 0.3168
      }
    ],
    "appeal": {
      "status": 200,
      "new_status": "under_review",
      "appeal_entries": 1
    }
  },
  {
    "status": 200,
    "content_id": "a5163b1eae0445469a234506c743ec47",
    "guess": "human",
    "confidence": 0.2772,
    "model_score": 0.261,
    "style_score": 0.2933,
    "label": "We think this was most likely written by a person.",
    "error": null,
    "sent": "i am honesly sooo tired rn. I was meant to be asleep by now but I have",
    "logged": [
      {
        "status": "decided",
        "guess": "human",
        "combined_score": 0.2772
      }
    ],
    "appeal": {
      "status": 200,
      "new_status": "under_review",
      "appeal_entries": 1
    }
  },
  {
    "status": 200,
    "content_id": "ce2df8aef40c4411b892d45903e6f5d7",
    "guess": "human",
    "confidence": 0.305,
    "model_score": 0.3042,
    "style_score": 0.3058,
    "label": "We think this was most likely written by a person.",
    "error": null,
    "sent": "I am starving my last meal was at 12 pm. I have another meeting that s",
    "logged": [
      {
        "status": "decided",
        "guess": "human",
        "combined_score": 0.305
      }
    ],
    "appeal": {
      "status": 200,
      "new_status": "under_review",
      "appeal_entries": 1
    }
  },
  {
    "status": 200,
    "content_id": "42d7bc72872045789ebb39e3f76db5e6",
    "guess": "unsure",
    "confidence": 0.401,
    "model_score": 0.4273,
    "style_score": 0.3747,
    "label": "We can't tell whether this was written by a person or with AI, so we're not making a call either way. A lot of people's own writing lands here, and this is not an accusation. If you wrote this yourself and want someone to take another look, you can appeal.",
    "error": null,
    "sent": "Hi, I recently got charged $29.99 to my bank account when I had assume",
    "logged": [
      {
        "status": "decided",
        "guess": "unsure",
        "combined_score": 0.401
      }
    ],
    "appeal": {
      "status": 200,
      "new_status": "under_review",
      "appeal_entries": 1
    }
  },
  {
    "status": 200,
    "content_id": "e88a91f62dd944a4b73cb3b034bd11f4",
    "guess": "unsure",
    "confidence": 0.4,
    "model_score": 0.6015,
    "style_score": 0.1,
    "label": "We can't tell whether this was written by a person or with AI, so we're not making a call either way. A lot of people's own writing lands here, and this is not an accusation. If you wrote this yourself and want someone to take another look, you can appeal.",
    "error": null,
    "sent": "Hi everyone, I and Jen are planning something really small for Andrea\u2019",
    "logged": [
      {
        "status": "decided",
        "guess": "unsure",
        "combined_score": 0.4
      }
    ],
    "appeal": {
      "status": 200,
      "new_status": "under_review",
      "appeal_entries": 1
    }
  },
  {
    "sent": "appeal with a made-up content_id",
    "appeal": {
      "status": 404,
      "new_status": null,
      "appeal_entries": 0
    }
  }
]
```

**Trial 3**

```json
[
  {
    "status": 200,
    "content_id": "8134365cfb52430b9ae5a0d25d727d5e",
    "guess": "unsure",
    "confidence": 0.6842,
    "model_score": 0.7683,
    "style_score": 0.6,
    "label": "We can't tell whether this was written by a person or with AI, so we're not making a call either way. A lot of people's own writing lands here, and this is not an accusation. If you wrote this yourself and want someone to take another look, you can appeal.",
    "error": null,
    "sent": "Remote work has fundamentally transformed the modern workplace, offeri",
    "logged": [
      {
        "status": "decided",
        "guess": "unsure",
        "combined_score": 0.6842
      }
    ],
    "appeal": {
      "status": 200,
      "new_status": "under_review",
      "appeal_entries": 1
    }
  },
  {
    "status": 200,
    "content_id": "f220d93e9cdd4de18ae1f828f8887207",
    "guess": "unsure",
    "confidence": 0.6,
    "model_score": 0.92,
    "style_score": 0.6,
    "label": "We can't tell whether this was written by a person or with AI, so we're not making a call either way. A lot of people's own writing lands here, and this is not an accusation. If you wrote this yourself and want someone to take another look, you can appeal.",
    "error": null,
    "sent": "Regular exercise plays a crucial role in maintaining both physical and",
    "logged": [
      {
        "status": "decided",
        "guess": "unsure",
        "combined_score": 0.6
      }
    ],
    "appeal": {
      "status": 200,
      "new_status": "under_review",
      "appeal_entries": 1
    }
  },
  {
    "status": 200,
    "content_id": "95aa0b01f11f4d488e83287df197d71e",
    "guess": "unsure",
    "confidence": 0.729,
    "model_score": 0.858,
    "style_score": 0.6,
    "label": "We can't tell whether this was written by a person or with AI, so we're not making a call either way. A lot of people's own writing lands here, and this is not an accusation. If you wrote this yourself and want someone to take another look, you can appeal.",
    "error": null,
    "sent": "Social media has become an integral part of modern society, shaping th",
    "logged": [
      {
        "status": "decided",
        "guess": "unsure",
        "combined_score": 0.729
      }
    ],
    "appeal": {
      "status": 200,
      "new_status": "under_review",
      "appeal_entries": 1
    }
  },
  {
    "status": 200,
    "content_id": "2ed67417fb3143ca8d6d95081994497f",
    "guess": "unsure",
    "confidence": 0.6,
    "model_score": 0.9179,
    "style_score": 0.6,
    "label": "We can't tell whether this was written by a person or with AI, so we're not making a call either way. A lot of people's own writing lands here, and this is not an accusation. If you wrote this yourself and want someone to take another look, you can appeal.",
    "error": null,
    "sent": "Climate change represents one of the most pressing challenges facing h",
    "logged": [
      {
        "status": "decided",
        "guess": "unsure",
        "combined_score": 0.6
      }
    ],
    "appeal": {
      "status": 200,
      "new_status": "under_review",
      "appeal_entries": 1
    }
  },
  {
    "status": 200,
    "content_id": "fdbcea764d714a5497a0e6674833f1aa",
    "guess": "unsure",
    "confidence": 0.5926,
    "model_score": 0.7125,
    "style_score": 0.4727,
    "label": "We can't tell whether this was written by a person or with AI, so we're not making a call either way. A lot of people's own writing lands here, and this is not an accusation. If you wrote this yourself and want someone to take another look, you can appeal.",
    "error": null,
    "sent": "Reading offers numerous benefits that extend far beyond simple enterta",
    "logged": [
      {
        "status": "decided",
        "guess": "unsure",
        "combined_score": 0.5926
      }
    ],
    "appeal": {
      "status": 200,
      "new_status": "under_review",
      "appeal_entries": 1
    }
  },
  {
    "status": 200,
    "content_id": "fd9d15b604be42418902dee262242e03",
    "guess": "human",
    "confidence": 0.3168,
    "model_score": 0.2587,
    "style_score": 0.375,
    "label": "We think this was most likely written by a person.",
    "error": null,
    "sent": "This weekend I went back home to celebrate a friends of mines birthday",
    "logged": [
      {
        "status": "decided",
        "guess": "human",
        "combined_score": 0.3168
      }
    ],
    "appeal": {
      "status": 200,
      "new_status": "under_review",
      "appeal_entries": 1
    }
  },
  {
    "status": 200,
    "content_id": "87135bbe4ac04eebb1c93b3d34e9464e",
    "guess": "human",
    "confidence": 0.2772,
    "model_score": 0.261,
    "style_score": 0.2933,
    "label": "We think this was most likely written by a person.",
    "error": null,
    "sent": "i am honesly sooo tired rn. I was meant to be asleep by now but I have",
    "logged": [
      {
        "status": "decided",
        "guess": "human",
        "combined_score": 0.2772
      }
    ],
    "appeal": {
      "status": 200,
      "new_status": "under_review",
      "appeal_entries": 1
    }
  },
  {
    "status": 200,
    "content_id": "39ad4e3afe684e80ae7f4a5ade291f4b",
    "guess": "human",
    "confidence": 0.305,
    "model_score": 0.3042,
    "style_score": 0.3058,
    "label": "We think this was most likely written by a person.",
    "error": null,
    "sent": "I am starving my last meal was at 12 pm. I have another meeting that s",
    "logged": [
      {
        "status": "decided",
        "guess": "human",
        "combined_score": 0.305
      }
    ],
    "appeal": {
      "status": 200,
      "new_status": "under_review",
      "appeal_entries": 1
    }
  },
  {
    "status": 200,
    "content_id": "76c5946507824347a6623e11aff5a14f",
    "guess": "unsure",
    "confidence": 0.401,
    "model_score": 0.4273,
    "style_score": 0.3747,
    "label": "We can't tell whether this was written by a person or with AI, so we're not making a call either way. A lot of people's own writing lands here, and this is not an accusation. If you wrote this yourself and want someone to take another look, you can appeal.",
    "error": null,
    "sent": "Hi, I recently got charged $29.99 to my bank account when I had assume",
    "logged": [
      {
        "status": "decided",
        "guess": "unsure",
        "combined_score": 0.401
      }
    ],
    "appeal": {
      "status": 200,
      "new_status": "under_review",
      "appeal_entries": 1
    }
  },
  {
    "status": 200,
    "content_id": "5afa037aef2c458baadfa498276e469d",
    "guess": "unsure",
    "confidence": 0.4,
    "model_score": 0.6015,
    "style_score": 0.1,
    "label": "We can't tell whether this was written by a person or with AI, so we're not making a call either way. A lot of people's own writing lands here, and this is not an accusation. If you wrote this yourself and want someone to take another look, you can appeal.",
    "error": null,
    "sent": "Hi everyone, I and Jen are planning something really small for Andrea\u2019",
    "logged": [
      {
        "status": "decided",
        "guess": "unsure",
        "combined_score": 0.4
      }
    ],
    "appeal": {
      "status": 200,
      "new_status": "under_review",
      "appeal_entries": 1
    }
  },
  {
    "sent": "appeal with a made-up content_id",
    "appeal": {
      "status": 404,
      "new_status": null,
      "appeal_entries": 0
    }
  }
]
```

### bad input

**Trial 1**

```json
[
  {
    "status": 400,
    "content_id": null,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "error": "text_too_short",
    "sent": "(empty text)",
    "logged": [
      {
        "event": "rejected",
        "status": "rejected",
        "reason": "text_too_short",
        "http_status": 400
      }
    ]
  },
  {
    "status": 400,
    "content_id": null,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "error": "missing_text",
    "sent": "{\"creator_id\": \"eval_bad_missing\"}",
    "logged": [
      {
        "event": "rejected",
        "status": "rejected",
        "reason": "missing_text",
        "http_status": 400
      }
    ]
  },
  {
    "status": 400,
    "content_id": null,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "error": "missing_text",
    "sent": "{\"text\": null, \"creator_id\": \"eval_bad_null\"}",
    "logged": [
      {
        "event": "rejected",
        "status": "rejected",
        "reason": "missing_text",
        "http_status": 400
      }
    ]
  },
  {
    "status": 400,
    "content_id": null,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "error": "text_not_string",
    "sent": "{\"text\": 12345, \"creator_id\": \"eval_bad_number\"}",
    "logged": [
      {
        "event": "rejected",
        "status": "rejected",
        "reason": "text_not_string",
        "http_status": 400
      }
    ]
  },
  {
    "status": 413,
    "content_id": null,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "error": "text_too_long",
    "sent": "word word word word word word word word word word word word word word ",
    "logged": [
      {
        "event": "rejected",
        "status": "rejected",
        "reason": "text_too_long",
        "http_status": 413
      }
    ]
  },
  {
    "status": 400,
    "content_id": null,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "error": "invalid_json",
    "sent": "[\"a\", \"JSON\", \"list\", \"instead\", \"of\", \"an\", \"object\"]",
    "logged": [
      {
        "event": "rejected",
        "status": "rejected",
        "reason": "invalid_json",
        "http_status": 400
      }
    ]
  }
]
```

**Trial 2**

```json
[
  {
    "status": 400,
    "content_id": null,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "error": "text_too_short",
    "sent": "(empty text)",
    "logged": [
      {
        "event": "rejected",
        "status": "rejected",
        "reason": "text_too_short",
        "http_status": 400
      }
    ]
  },
  {
    "status": 400,
    "content_id": null,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "error": "missing_text",
    "sent": "{\"creator_id\": \"eval_bad_missing\"}",
    "logged": [
      {
        "event": "rejected",
        "status": "rejected",
        "reason": "missing_text",
        "http_status": 400
      }
    ]
  },
  {
    "status": 400,
    "content_id": null,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "error": "missing_text",
    "sent": "{\"text\": null, \"creator_id\": \"eval_bad_null\"}",
    "logged": [
      {
        "event": "rejected",
        "status": "rejected",
        "reason": "missing_text",
        "http_status": 400
      }
    ]
  },
  {
    "status": 400,
    "content_id": null,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "error": "text_not_string",
    "sent": "{\"text\": 12345, \"creator_id\": \"eval_bad_number\"}",
    "logged": [
      {
        "event": "rejected",
        "status": "rejected",
        "reason": "text_not_string",
        "http_status": 400
      }
    ]
  },
  {
    "status": 413,
    "content_id": null,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "error": "text_too_long",
    "sent": "word word word word word word word word word word word word word word ",
    "logged": [
      {
        "event": "rejected",
        "status": "rejected",
        "reason": "text_too_long",
        "http_status": 413
      }
    ]
  },
  {
    "status": 400,
    "content_id": null,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "error": "invalid_json",
    "sent": "[\"a\", \"JSON\", \"list\", \"instead\", \"of\", \"an\", \"object\"]",
    "logged": [
      {
        "event": "rejected",
        "status": "rejected",
        "reason": "invalid_json",
        "http_status": 400
      }
    ]
  }
]
```

**Trial 3**

```json
[
  {
    "status": 400,
    "content_id": null,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "error": "text_too_short",
    "sent": "(empty text)",
    "logged": [
      {
        "event": "rejected",
        "status": "rejected",
        "reason": "text_too_short",
        "http_status": 400
      }
    ]
  },
  {
    "status": 400,
    "content_id": null,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "error": "missing_text",
    "sent": "{\"creator_id\": \"eval_bad_missing\"}",
    "logged": [
      {
        "event": "rejected",
        "status": "rejected",
        "reason": "missing_text",
        "http_status": 400
      }
    ]
  },
  {
    "status": 400,
    "content_id": null,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "error": "missing_text",
    "sent": "{\"text\": null, \"creator_id\": \"eval_bad_null\"}",
    "logged": [
      {
        "event": "rejected",
        "status": "rejected",
        "reason": "missing_text",
        "http_status": 400
      }
    ]
  },
  {
    "status": 400,
    "content_id": null,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "error": "text_not_string",
    "sent": "{\"text\": 12345, \"creator_id\": \"eval_bad_number\"}",
    "logged": [
      {
        "event": "rejected",
        "status": "rejected",
        "reason": "text_not_string",
        "http_status": 400
      }
    ]
  },
  {
    "status": 413,
    "content_id": null,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "error": "text_too_long",
    "sent": "word word word word word word word word word word word word word word ",
    "logged": [
      {
        "event": "rejected",
        "status": "rejected",
        "reason": "text_too_long",
        "http_status": 413
      }
    ]
  },
  {
    "status": 400,
    "content_id": null,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "error": "invalid_json",
    "sent": "[\"a\", \"JSON\", \"list\", \"instead\", \"of\", \"an\", \"object\"]",
    "logged": [
      {
        "event": "rejected",
        "status": "rejected",
        "reason": "invalid_json",
        "http_status": 400
      }
    ]
  }
]
```
