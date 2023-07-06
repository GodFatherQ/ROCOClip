# PubMedCLIP 
Source code for reproducing ROCOCLIP by fine-tuning CLIP using image--text pairs extracted from PubMed articles as provided in the ROCO dataset.
<br>
The fine-tuned CLIP models with ViT32, RN50 and RN50x4 visual encoders are also provided on [OneDrive](https://1drv.ms/f/s!Ag4nSi2fvYsygZJ9OEEZmpDzEpmXpQ?e=AIviKn).
<br>
## How to use
This project requires Python 3.7 or newer.
1. Download ROCO dataset from [the official repository](https://github.com/razorx89/roco-dataset),
2. Create your virtual environment, activate it and install ``` pip install -r requirements.txt ```,
3. Set the input paths in `run.sh`,
4. Run `run.sh`.
