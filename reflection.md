# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?  
  The game was easy to understand and ran smoothly the first time I ran it. I didn't face any technical glitches that stopped me from playing the game. The only hinderence was that the hints were backwards.
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").  
  One of the first bugs was that I was unable to submit a new guess after pressing new game. The attempts wouldn't go down, I wouldn't get a hint, and the score wouldn't update. Lastly, I would have less attempts than given. Specifically one less than how many it said were actually left. This meant that the game would end with one attempt left rather than 0.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| New Game | Game restarts | Nothing | none |
| Guess | Score reflects accurately | Score changes unexpectedly | none |
| Difficult Easy | Attempts left increases | Attempts is less than normal difficult | none |
| Incorrect Guess | Accurate hints | Hints point in opposite direction | none |
| Guess | Submit guesses as long as attempts left is not 0. | Game ends with 1 attempt left | none |
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?  
  For this project I used Claude Code for help debugging and refactoring within VSCode. Claude Code also helped me understand the behavior of the code. To research technical concepts I didn't understand, I used Google Gemini. 
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
One AI suggestion that was correct was when it suggested the New Game handler not resetting st.session_state.status as the culprit for the new game bug I found. I verified the result by looking the logic of the code. The suggestions it gave ended up be verified as true since the code would run into st.stop(). Additionally, further verification was done by implementing the suggested fix with successful pytests.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  While doing the project, I didn't find that the AI would give an incorrect suggestion but it did point out other bugs aside from what I pointed out. Many of these bugs were the actual reason for the glitchy behavior but if they weren't directly related, AI would just point them out in brief sentence so it didn't feel misleading.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?  
  There were two main ways to determine a bug was really fixed. Apart from understing the logic that was changed, succesfully pytests that asserted the exepected behavior helped affirm that a bug was fixed. Additionally, I tested it fully by running the app again and trying the new feature. If the pytests and features worked successfully, then, I determined the bug was really fixed.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.  
  One test that I ran was verifying the fixes when running the app. By assessing the results and verifying that the fixes truly addressed the bugs I was then confident that I could move onto the next bug. For example trying a new game successfully allowed me to restart the game with attempts, history, etc. refreshed.

- Did AI help you design or understand any tests? How?  
  Yes AI, mainly helped on designing pytests but apart from asserting the exact fixes we introduced to address the bugs, it gave a lot of context in terms of the logic of the code. With the given logic that it gave me I was confident in the tests that were running and what the results meant. It even helped me fix an error I ran into so that I could run the bare command pytest by implementing conftest.py.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?  
In a traditional app, when you click a button, only that one button changes. In Streamlit, the moment you click a button, move a slider, or type in a box, Streamlit re-runs your entire code file from line 1 to the very end. It effectively redraws the whole screen to reflect the new change. As a result, Streamlit, uses session state to hold memory of data so that it isn't 'forgotten' on every refresh.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.  
One of the main habits I want to use is practicing multiple ways of verifying fixes. Since AI is really good at writing these pytests, I will definitly implement this in the future given how helpful it was to speed up my workflow. 

- What is one thing you would do differently next time you work with AI on a coding task?  
Next time I work on a coding tasks with AI, I'll work on being a bit more specific with my prompts as a way to pinpoint what I'm working on as it can get difficult to keep track of the changes that AI makes. If I break down even a singular bug into multiple steps, it will help me stay on top of the coding agent is doing especially when working on a live environment. 
- In one or two sentences, describe how this project changed the way you think about AI generated code.  
  This project helped me see the full potential of AI in a workflow aside from LLMs and chatbots. Once you give an agent the context you otherwise assume, you can see how meticulous AI is and the reliability of its suggestions. 
