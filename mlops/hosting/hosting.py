from huggingface_hub import HfApi
import os

api = HfApi(token=os.getenv("HF_TOKEN"))  # Correctly reference the HF_TOKEN environment variable
api.upload_folder(
    folder_path="mlops/deployment",     # the local folder containing your files
    repo_id="SunnyShaurya/Bank-Customer-Churn",          # the target repo
    repo_type="space",                      # dataset, model, or space
    path_in_repo="",                          # optional: subfolder path inside the repo
)
