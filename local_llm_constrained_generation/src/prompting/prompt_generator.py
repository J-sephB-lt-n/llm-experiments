class PromptGenerator:
    def __init__(self) -> None:
        self.parts: dict[str, str] = {
            "global_init": "You are telling a story. ",
            "perspective": (
                "Please address me directly as 'you' in your generated text "
                "(i.e. second-person perspective) as I am "
                "the main character in the story. "
            ),
        }

    def set_global_story_style(self) -> None:
        self.parts["global_story_style"] = input(
            "Please describe the desired genre and "
            "style of the story "
            "(and add any other details/requirements you like) "
            "Examples: \n"
            "   The story takes place in the mind of a businessman who is slowly going mad.\n"
            "   The story is a modern zombie story set in a bustling township in South Africa.\n"
            "   The story is classic fantasy (dragons, ogres, orcs, goblins, elves etc.)\n"
            "   The story is science fiction with an industrial feel.\n"
        ).strip()
        if self.parts["global_story_style"][-1] != ".":
            self.parts["global_story_style"] += "."
        self.parts["global_story_style"] += " "

    def generate_location_names(self, n_locations: int) -> str:
        return (
            self.parts["global_init"]
            + self.parts["global_story_style"]
            + f"Please provide {n_locations} different physical "
            + "locations that would make sense appearing in this "
            + "story. Please do not describe them. "
            + "Each location name should not be more than 10 words long. "
            + f"Please number them 1 to {n_locations}"
        )

    def generate_location_description(self, location_name: str) -> str:
        return (
            self.parts["global_init"]
            + self.parts["global_story_style"]
            + self.parts["perspective"]
            + "Please provide a few sentences "
            + "(up to a maximum of 4 sentences) "
            + "describing the "
            + f"following story location: '{location_name}'. "
            + "What do I see here? "
            + "What do I hear? "
            + "What do I smell? "
            + "How do I feel? "
            + "Who is here? "
        )

    def generate_response_to_user_action(
        self,
        location_name: str,
        location_description: str,
        user_action_description: str,
    ) -> str:
        user_action_description = user_action_description.strip()
        if user_action_description[-1] != ".":
            user_action_description += "."
        return (
            self.parts["global_init"]
            + self.parts["global_story_style"]
            + self.parts["perspective"]
            + f'I am currently in location "{location_name}". '
            + f'The current description of my location is as follows:\n"{location_description}"\n'
            + f'I attempt the following action: "{user_action_description}".\n'
            + "Please describe in 3 sentences how my environment responds to my action (if at all). "
        )

    def user_action_updates_location_description(
        self,
        location_name: str,
        location_description: str,
        user_action_description: str,
        location_response_to_user_action: str,
    ) -> str:
        user_action_description = user_action_description.strip()
        if user_action_description[-1] != ".":
            user_action_description += "."
        return (
            self.parts["global_init"]
            + self.parts["global_story_style"]
            + self.parts["perspective"]
            + f'I am currently in location "{location_name}". '
            + f'The previous description of my location was as follows:\n"{location_description}"\n'
            + f'I attempted the following action in this location: "{user_action_description}".\n'
            + f'The result of my action was: "{location_response_to_user_action}"'
            + "Please generate an updated description of my current location, "
            + "following from my action. "
        )
