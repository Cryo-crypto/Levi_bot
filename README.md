# Discord AI Chat Bot powered by ![AI](https://raw.githubusercontent.com/SudhanPlayz/Discord-MusicBot/v5/assets/logo.gif) OpenRouter AI

Created and Maintained by: [Nathaniel](https://discord.com/users/829427219541393428) and [Haruto](https://discord.com/users/1061411114958729287)

## Tutorial on how to get started

### Create NodeJs [Repl](https://replit.com/)
- Navigate to [Replit](https://replit.com/)
- Login if needed
- Go to the home page
- Press on the New Repl button
- Select Node.js from the dropdown

## Clone the repository

### Once you have created the repl
- Navigate to the Shell
- Type in the command `git clone https://github.com/Crypto-Haruto/Levi_bot.git`
- It should take a few seconds to install the project
- If you prefer, you can update the `package.json` to your liking

## Setting up Environmental Variables

### Once the repository has been cloned
- Navigate to the Secrets tab
- Create a secret named `TOKEN` and give it the value of your actual bot token
- Create another secret named `ApiKey` and give it the value of your OpenAI [API Key](https://help.openai.com/en/articles/4936850-where-do-i-find-my-openai-api-key)
- Create another secret named `CHANNELS` and set the value to be the [Channel ID](https://turbofuture.com/internet/Discord-Channel-ID) of the channel you wish the bot to speak in
- Create a final secret named `IGNORE_PREFIX` and this value when put in front of a sentence will tell the bot to ignore the message
