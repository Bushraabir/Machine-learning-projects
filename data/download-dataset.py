import kagglehub

# Download latest version
path = kagglehub.dataset_download("datascientist97/astronomical-data")

print("Path to dataset files:", path)