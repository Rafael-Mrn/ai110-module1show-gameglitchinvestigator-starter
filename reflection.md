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
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?  
In a traditional app, when you click a button, only that one button changes. In Streamlit, the moment you click a button, move a slider, or type in a box, Streamlit re-runs your entire code file from line 1 to the very end. It effectively redraws the whole screen to reflect the new change. As a result, Streamlit, uses session state to hold memory of data so that it isn't 'forgotten' on every refresh.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
