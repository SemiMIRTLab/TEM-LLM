# TEM-LLM
Automated pipeline for constructing visual question-answering datasets 
from microscopy literature to enable LLM interpretation of scientific images.

This model is associated with the following work (currently under review):

> *AI-Assisted Materials Characterization: A Curriculum-Guided 
> Multimodal Framework for Transmission Electron Microscopy*

## Install
1. Clone this repository and navigate to main folder
```bash
git clone https://github.com/SemiMIRTLab/TEM-LLM.git
cd TEM-LLM
```

2. Install Package
```bash
conda create -n tem-llm python=3.10 -y
conda activate tem-llm
pip install --upgrade pip
pip install -r requirements.txt
```

## Documentation
Follow these steps sequentially for complete pipeline implementation:

| Step | Document | Explanation |
|------|----------|-------------|
| 1 | [🕷️Web Crawling](https://github.com/SemiMIRTLab/TEM-LLM/blob/main/docs/Web%20Crawling.md) | Collect scientific papers from online sources |
| 2 | [📄Data Extraction](https://github.com/SemiMIRTLab/TEM-LLM/blob/main/docs/Data%20Extraction.md) | Extract figures and captions from PDF documents |
| 3 | [🔄Data Preprocessing](https://github.com/SemiMIRTLab/TEM-LLM/blob/main/docs/Data%20Preprocessing.md) | Process and classify TEM images & Caption Reconstruction Using OCR |
| 4 | [📋Data Distillation](https://github.com/SemiMIRTLab/TEM-LLM/blob/main/docs/Data%20distillation.md) | Generate high-quality QA pairs using GPT |
| 5 | **Model Training** | Follow [LLaVA LoRA Training Scripts](https://github.com/haotian-liu/LLaVA/blob/main/scripts/v1_5/finetune_task_lora.sh) |
| 6 | **Model Inference** | Follow [LLaVA Inference Scripts](https://github.com/haotian-liu/LLaVA/blob/main/llava/serve/cli.py) |
| 7 | [📊Model Evaluation](https://github.com/SemiMIRTLab/TEM-LLM/blob/main/docs/Model%20Evaluation.md) | Assess model performance with comprehensive metrics |

⚠️ **Important**: This project requires LLaVA model integration. 
Please complete LLaVA installation before proceeding with steps 5–6. 
See [LLaVA Installation Guide](https://github.com/haotian-liu/LLaVA.git)

---

## Hugging Face
Our fine-tuned model for TEM image analysis is available on Hugging Face:

🤗 **Model**: [LabSmart/TEM-LLM](https://huggingface.co/LabSmart/TEM-LLM)

## Model Details

| | |
|---|---|
| **Base Model** | LLaVA-v1.5-7B (Vicuna-v1.5-7B) |
| **Training Strategy** | Difficulty-Aware Curriculum Learning (4 stages) |
| **Training Data** | ~216K QA pairs across 40K TEM images |
| **Domain** | Transmission Electron Microscopy (TEM) |
| **Modalities** | CTEM, HR-TEM, STEM, Diffraction |
| **Fine-tuning Method** | LoRA (Low-Rank Adaptation) |

---

## Important: Inference Requirements

TEM-LLM is built on LLaVA and **cannot be loaded directly via 
`transformers`**. Inference requires the LLaVA repository.

**Step 1 — Clone LLaVA:**
```bash
git clone https://github.com/haotian-liu/LLaVA.git
cd LLaVA
pip install -e .
```

**Step 2 — Download weights:**
```python
from huggingface_hub import snapshot_download
snapshot_download(
    repo_id="LabSmart/TEM-LLM", 
    local_dir="./TEM-LLM"
)
```

**Step 3 — Run inference:**
```bash
python -m llava.serve.cli \
    --model-path "./TEM-LLM" \
    --image-file "path/to/your/tem_image.jpg" \
    --load-4bit
```
---

## Limitations

- TEM-LLM is optimized for TEM image analysis and may produce 
  unreliable outputs when applied to out-of-scope questions or 
  out-of-domain images.
- The model provides approximate qualitative descriptions rather 
  than exact quantitative measurements.
