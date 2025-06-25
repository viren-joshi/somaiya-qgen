# QuestGen: AI-Powered Crowdsourced Question Generation

QuestGen is a deep learning-based platform designed to simplify and standardize the process of question bank creation for educators. By combining crowdsourced contributions with an intelligent question generation engine, QuestGen enables seamless, scalable, and curriculum-aligned question paper creation.

## Overview

In traditional settings, question bank generation is time-consuming, inconsistent, and highly manual. QuestGen introduces a platform where educators and subject experts can collaboratively generate, validate, and improve questions — with the support of an AI-powered backend that ensures questions align with Bloom’s Taxonomy (BT) levels and educational goals.

## Features

- **Crowdsourcing Model:** Users can post, upvote, downvote, or flag questions and answers anonymously.
- **BT-Level Awareness:** Questions are generated and classified based on complexity levels, using Bloom’s Taxonomy.
- **AI-Driven Generation:** Leveraging transformer models (T5) fine-tuned to generate diverse, contextually rich questions from input paragraphs.
- **Keyword & Frame-Based Construction:** Uses keyword extraction and BT-level heuristics to structure generated questions.
- **Paragraph-Level Understanding:** Enables the model to derive nuanced questions from full paragraph inputs, improving contextual accuracy.
- **Custom Feedback System:** Built-in mechanisms for educators to guide the model by ranking question relevance.

## Tech Stack

- **Frontend:** React, HTML, CSS, JavaScript
- **Backend:** Python, Flask, Django
- **Model:** T5 fine-tuned on question-answer datasets with BT-level tagging
- **Database:** PostgreSQL
- **DevOps & Deployment:** Docker, GitHub Actions

## Dataset Pipeline

1. **Data Collection:** Questions scraped from educational repositories and manually created by contributors.
2. **Labeling:** Each item is paired with its respective paragraph and BT-level tag.
3. **Training:** Input-paragraph and BT-level are fed into a tokenized transformer for fine-tuning and evaluation.

## Research & Model Design

This project explores and improves on both sentence-level and paragraph-level Question Generation (QG) methods. Literature analysis showed that paragraph-level approaches offer better semantic comprehension, which is core to QuestGen’s architecture.

### Key Model Components

- **Input Encoding:** Paragraphs are encoded to extract relevant features.
- **BT-Driven Structuring:** Questions are framed based on complexity indicators.
- **Transformer-Based Generation:** Fine-tuned T5 model handles the generation pipeline.
- **Evaluation:** Outputs are filtered and ranked using both user feedback and BT compliance.

## Results & Impact

- Reduced manual question creation time by 35% for faculty members.
- Improved assessment variety by 20% by enabling diverse question types.
- Crowdsourced feedback loop improved model output relevance over iterative updates.

## Contributors

This project was built by a collaborative student team:

- Viren Joshi  
- Devashish Bhake  
- Divija Kinger  
- Taaha Multani  
