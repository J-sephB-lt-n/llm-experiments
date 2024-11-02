build_push_container_to_google_artifact_registry:
	gcloud config set project $(GCP_PROJECT_ID)
	gcloud config set run/region $(GCP_REGION)
	docker buildx build \
		--platform linux/amd64 \
		--tag $(GCP_REGION)-docker.pkg.dev/$(GCP_PROJECT_ID)/$(GCP_ARTIFACT_REG_REPO_NAME)/$(CONTAINER_NAME) \
		.
	docker push \
		$(GCP_REGION)-docker.pkg.dev/$(GCP_PROJECT_ID)/$(GCP_ARTIFACT_REG_REPO_NAME)/$(CONTAINER_NAME)
