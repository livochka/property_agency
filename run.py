from agency import Agent

# Call to the agent
agent = Agent()

# Adding of three properties
for i in range(2):
    agent.add_property()

# Here you can try advising properties for purchasing or rental in order to
# price you could pay
agent.advice_property()

# Show all available properties
print("\nAll properties list:\n")
agent.display_properties()

