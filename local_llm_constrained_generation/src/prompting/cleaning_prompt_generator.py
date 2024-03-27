class CleaningPromptGenerator:
    def get_clean_location_name(self, llm_response: str) -> str:
        return (
            "Please extract only the location name from "
            f"the following text: '{llm_response}'. "
            "Please include ONLY the name itself and no other text whatsoever. "
        )
