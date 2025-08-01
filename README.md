# docker-volumn

1. conda activate mlops_env

2. docker build -t app-container .

3. pwd --> **/mnt/e/MLOps/docker-volume**

4. docker run -v **/mnt/e/MLOps/docker-volume**/data:/data -p 8000:8000 app-container:latest

The updated data should appear instantly without refreshing the tab.
